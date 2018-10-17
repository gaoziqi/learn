import * as THREE from 'three'

//创建场景.
let scene = new THREE.Scene()
//相机
let camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)
//渲染器
let renderer = new THREE.WebGLRenderer()
//拾取器
let raycaster = new THREE.Raycaster()
//鼠标
let mouse = new THREE.Vector2()
//摄像机控制
let controls: THREE.OrbitControls
//初始化
function init() {
    //设置画布大小
    renderer.setSize(window.innerWidth, window.innerHeight)
    //加入到body
    document.body.appendChild(renderer.domElement)
    initCamera()
    initLight()
    document.addEventListener(
        'mousemove',
        function(event) {
            event.preventDefault()
            mouse.x = (event.clientX / window.innerWidth) * 2 - 1
            mouse.y = -(event.clientY / window.innerHeight) * 2 + 1
            raycaster.setFromCamera(mouse, camera)
            //document.addEventListener('click', _mouse_click, false)
        },
        false
    )
}

//相机初始化
function initCamera() {
    camera.position.set(0, 0, 100)
    camera.lookAt(new THREE.Vector3(0, 0, 0))
    controls = new THREE.OrbitControls(camera)
}

//灯光初始化
function initLight() {
    var directionalLight = new THREE.DirectionalLight(0xffffff)
    directionalLight.position.set(-25, -25, 10)
    directionalLight.name = '-1'
    scene.add(directionalLight)
    var directionalLight = new THREE.DirectionalLight(0xffffff)
    directionalLight.position.set(25, 25, 10)
    directionalLight.name = '-2'
    scene.add(directionalLight)
}

//渲染循环
function animate() {
    requestAnimationFrame(animate)
    
    renderer.render(scene, camera)
    controls.update()
}

init()
animate()