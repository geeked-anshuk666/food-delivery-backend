# Food Delivery Backend

A microservices-based backend for a food delivery application.

## Services

- **User Service**: Handles user management, restaurant listings, and order placement
- **Restaurant Service**: Manages restaurant menus, availability, and order processing
- **Delivery Service**: Manages delivery agents and order delivery status

## Deployment Instructions (Free Hosting on Render with Docker)

1. Create a free account on [Render](https://render.com/).
2. Push your project to a GitHub repository.
3. Connect your GitHub repository to Render:
   - Go to the Render Dashboard.
   - Click "New" and select "Blueprint".
   - Connect your GitHub account and select this repository.
   - Render will automatically detect the `render.yaml` file, build the Docker image for each service, and deploy them.
4. Once deployed, your services will be available at:
   - User Service: https://food-delivery-user-service.onrender.com
   - Restaurant Service: https://food-delivery-restaurant-service.onrender.com
   - Delivery Service: https://food-delivery-delivery-service.onrender.com

4. Access the API documentation at:
   - User Service: https://food-delivery-user-service.onrender.com/docs
   - Restaurant Service: https://food-delivery-restaurant-service.onrender.com/docs
   - Delivery Service: https://food-delivery-delivery-service.onrender.com/docs

## Alternative Free Hosting Options

### Railway

1. Create a free account on [Railway](https://railway.app/)
2. Install the Railway CLI: `npm i -g @railway/cli`
3. Login: `railway login`
4. Initialize your project: `railway init`
5. Deploy each service:
   ```bash
   cd user_service
   railway up
   cd ../restaurant_service
   railway up
   cd ../delivery_service
   railway up