import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MtComponent } from './mt/mt.component';
import { MnComponent } from './mn/mn.component';
import { MdComponent } from './md/md.component';

const routes: Routes = [
  { path: 'mt', component: MtComponent },
  { path: 'md', component: MdComponent },
  { path: 'mn', component: MnComponent }
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
