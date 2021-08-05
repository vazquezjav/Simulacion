import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { NoticiasTextoPageRoutingModule } from './noticias-texto-routing.module';

import { NoticiasTextoPage } from './noticias-texto.page';
import { NoticiasTextoComponent } from '../components/noticias-texto/noticias-texto.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    NoticiasTextoPageRoutingModule
  ],
  declarations: [NoticiasTextoPage, NoticiasTextoComponent],
  exports: [NoticiasTextoComponent]
})
export class NoticiasTextoPageModule {}
