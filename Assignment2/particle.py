"""Assignment N.2 
Luana Michela Modafferi
Write a program to explore the properties of a few elementary Particles.
The program must contain a Base class Particle and two Child classes, Proton and Alpha, that inherit from it."""
import math

LIGHT_SPEED = 1 

class Particle:
    """A class that describes the properties of an elementary Particle.
    Arguments:
    -name of the particle
    -mass of particle (MeV/c^2)
    -charge of the particle (e)
    -momentum of the particle (MeV/c)
    """
    def __init__(self, name, mass, charge, momentum=0.):
        self.name = name    
        self._mass = mass   #the underscore preceeding the argument means that I want it to be private.
        self._charge = charge
        self.momentum = momentum    # 'momentum' is NOT private. This line sends the interpreter to the momentum.setter
                                    # propriety that we used to check the limit of the value

    def print_info(self):
        print('***Particle Info***\nName: {}\nMass: {:.3f} MeV/c^2\nCharge: {} e\nMomentum:{:.4f} MeV/c\n***********'.format(self.name, self.mass, self.charge, self.momentum))
 


    @property       #Note that I'm not making a setter for the mass and charge: I don't want the user to modify them!
    def mass(self):
        return self._mass
    
    @property
    def charge(self):
        return self._charge
    
    @property
    def momentum(self):
        return self._momentum
    
    @momentum.setter
    def momentum(self, value):
        if value < 0:
            print('Cannot set momentum to a value inferior to zero.\nThe momentum will be set to zero!')
            self._momentum = 0.
        else:
            self._momentum  = value 
    @property
    def energy(self):
        return math.sqrt( (self.momentum * LIGHT_SPEED)**2 + (self.mass * LIGHT_SPEED**2)**2 )
    
    @energy.setter
    def energy(self, value):
        if value < self.mass:
            print('Value Error: Cannot set particle energy to a value smaller than its mass ({}).'.format(self.mass))
            return math.sqrt( (self.momentum * LIGHT_SPEED)**2 + (self.mass * LIGHT_SPEED**2)**2 )
        self.momentum = math.sqrt(value**2 - self.mass**2 * LIGHT_SPEED**4) / LIGHT_SPEED

    @property
    def beta(self):
        return ( self.momentum * LIGHT_SPEED ) / self.energy

    @beta.setter
    def beta(self, value):
        if (value < 0.) or (value > 1.):
            print('Value Error: Beta must be in range [0,1].')
            return
        if (value >= 1.) and (self.mass > 0):
            print('Only massles particles can travel at Beta = 1!')
            return
        self.momentum = LIGHT_SPEED * value * self.mass / math.sqrt(1 - value**2)

    @property
    def gamma(self):
        return 1./ math.sqrt( 1.- self.beta**2) 
    
    @gamma.setter
    def gamma(self, value):
        if value < 1:
            print('Value Error: Gamma is always greater that 1!')
            return
        self.momentum = self.mass * LIGHT_SPEED * math.sqrt( value**2 - 1)


class Proton(Particle):
    """Class describing a proton. We inherit it from class Particle.
    """
    NAME = 'Proton'     #Fixed arguments: it is a convention to use caps.
    MASS = 938
    CHARGE = +1
    def __init__(self, momentum=0.):    #These are the arguments given by the user
        super().__init__(self.NAME, self.MASS, self.CHARGE, momentum)


class Alpha(Particle):
    """Class describing an Alpha nucleum. We inherit it from class Particle.
    """   
    NAME = 'Alpha'
    MASS = 3727.3
    CHARGE = +4
    def __init__(self, momentum=0.):
        super().__init__(self.NAME, self.MASS, self.CHARGE, momentum)



if __name__ == '__main__':
    my_particle = Particle(name='luanone', mass=10, charge=-1, momentum=100.)
    my_proton = Proton(10)  
    my_proton.print_info()      #Checking if the code works...
    my_alpha = Alpha(200)
    my_alpha.gamma = 22
    print(my_alpha.gamma)