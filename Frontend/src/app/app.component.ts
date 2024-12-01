import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule, NgFor } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,AppComponent,NgFor,CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'Frontend';

  items: any[] = [];
  newItem = { name: '', description: '' };

  constructor(private apiService: ApiService) {}

  addItem() {

    const data = {
      name: this.newItem.name,
      description: this.newItem.description,
    };

    this.apiService.createItem(data).subscribe({ 
      next: (response: any) => {
        console.log(response);
      }
    });
  }

}
