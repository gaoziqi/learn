
import { fakeAsync, ComponentFixture, TestBed } from '@angular/core/testing';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MnComponent } from './mn.component';

describe('MnComponent', () => {
  let component: MnComponent;
  let fixture: ComponentFixture<MnComponent>;

  beforeEach(fakeAsync(() => {
    TestBed.configureTestingModule({
      imports: [MatSidenavModule],
      declarations: [MnComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should compile', () => {
    expect(component).toBeTruthy();
  });
});
