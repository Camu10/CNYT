
public class ComplexMath {
	public static Complex suma(Complex c1, Complex c2) {
		double x = c1.getReal() + c2.getReal();
		double y = c1.getImag()+c2.getImag();
		return new Complex(x,y);
	}
	
	public static Complex resta(Complex c1, Complex c2) {
		double x = c1.getReal() - c2.getReal();
		double y = c1.getImag() - c2.getImag();
		return new Complex(x,y);
	}
	
	public static Complex producto(Complex c1, Complex c2) {
		double x = c1.getReal() * c2.getReal() - c1.getImag() * c2.getImag();
		double y = c1.getReal() * c2.getImag() + c2.getReal() * c1.getImag();
		return new Complex(x,y);
	}
	
	public static Complex division(Complex c1, Complex c2) {
		double divisor = Math.pow(c1.getImag(),2)+ Math.pow(c2.getImag(), 2);
		double dividendo1 = c1.getReal() * c1.getImag() + c2.getReal() * c2.getImag();
		double dividendo2 = c1.getImag() * c2.getReal() - c1.getReal() * c2.getImag();
		return new Complex(dividendo1/divisor,dividendo2/divisor);
	}
	
	public static sumMatriz(){
		
	}
}
