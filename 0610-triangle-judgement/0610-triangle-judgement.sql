select x,y,z, if( (x+y>z AND z+x>y AND y+z>x), 'Yes','No') as triangle
from Triangle;


