import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MtComponent } from './mt/mt.component';
import { MdComponent } from './md/md.component';

const routes: Routes = [
  { path: 'mt', component: MtComponent },
  { path: 'md', component: MdComponent }
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
