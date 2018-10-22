import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MtComponent } from './mt/mt.component';
import { MdComponent } from './md/md.component';
import { PanelComponent } from './panel/panel.component';

const routes: Routes = [
  { path: 'mt', component: MtComponent },
  { path: 'md', component: MdComponent },
  { path: 'panel', component: PanelComponent },
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
