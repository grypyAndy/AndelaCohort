'''My OOP mobile phone project
	This allows one to see the original price of the phone
	and the discount attached to it depending on the offer holiday
	Black Friday
	Easter Holiday
	Christmas Offer

'''
class mobile(object):
	
	def __init__(self,man="Nokia",offer="blackFriday",os="Symbian",model="N18",cost=25000):
		#defines the manufacturer, operating system,model and initial cost
		
		self.man=man
		self.os=os
		self.model=model
		self.cost=cost


	def obtainModel(model):
		#This function get the model from the client registration
		print(model)
		

	def getinputs():
		if offer == 1:
			return xmas
		elif offer==2:
			return easter
		elif offer==3:
			return blackFriday	

	def getDiscount(self,offer):
		''' This section test for the offer in the season and determines
			the price of the phone at that period.
		'''
		if offer==xmas:
			discount=0.5*cost
			amount=cost-discount
			self.cost=amount
			return amount
		elif offer==easter:
			discount=0.4*cost
			amount=cost-discount
			self.cost=amount
			return amount
		elif offer==blackFriday:
			discount=0.75*cost
			amount=cost-discount
			self.cost=amount
			return amount
		else:
			return cost

		print("Welcome to Grypy Wares and Tech")
		print("Your Wish List: ")
		print("Model: ",model)
		print("Manufacturer: ",man)
		print("Cost: ",cost)
		print("Amount: ",amount)




