import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { CommonModule } from '@angular/common'; // Add this line

import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms'; // Add this line

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    CommonModule, // Add this
    FormsModule   // Add this for ngModel
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
