import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ButtonsIndicatorsComponent } from './buttons-indicators.component';
import { ButtonsIndicatorsRoutingModule } from './buttons-indicators-routing.module';
import { ButtonComponent } from './button/button.component';

@NgModule({
  declarations: [ButtonsIndicatorsComponent, ButtonComponent],
  imports: [CommonModule, ButtonsIndicatorsRoutingModule]
})
export class ButtonsIndicatorsModule {}
