import { OfferService } from '../../../shared/service/OfferService';
import { Component, inject } from '@angular/core';

@Component({
  selector: 'app-services',
  standalone: true,
  imports: [],
  templateUrl: './offer.html'
})
export class Services {
  private offerService = inject(OfferService);
}
