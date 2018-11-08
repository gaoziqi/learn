import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ButtonComponent } from './button/button.component';
import { ButtonsIndicatorsComponent } from './buttons-indicators.component';

const routes: Routes = [
  {
    path: '',
    component: ButtonsIndicatorsComponent,
    children: [
      {
        path: 'button',
        component: ButtonComponent
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ButtonsIndicatorsRoutingModule {}
