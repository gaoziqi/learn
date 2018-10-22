import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-panel-child',
  templateUrl: './panel-child.component.html'
})
export class PanelChildComponent implements OnInit {
  constructor() {}
  items = [{ name: 'Apple', type: 'fruit' }, { name: 'Carrot', type: 'vegetable' }, { name: 'Orange', type: 'fruit' }];

  ngOnInit() {}
}
