
public class Complex {
	
	private double real;
	private double imag;
	
	private Complex() {
		real = 0.0;
		imag = 0.0;
	}
	
	private Complex(double real, double imag) {
		this.real = real;
		this.imag = imag;
	}
	
	public static Complex suma(Complex c1, Complex c2) {
		double x = c1.real + c2.real;
		double y = c1.imag+c2.imag;
		return new Complex(x,y);
	}
	
	public static Complex resta(Complex c1, Complex c2) {
		double x = c1.real - c2.real;
		double y = c1.imag - c2.imag;
		return new Complex(x,y);
	}
	
	public static Complex producto(Complex c1, Complex c2) {
		double x = c1.real * c2.real - c1.imag * c2.imag;
		double y = c1.real * c2.imag + c2.real * c1.imag;
		return new Complex(x,y);
	}
	
	public static Complex division(Complex c1, Complex c2) {
		double divisor = Math.pow(c1.imag,2)+ Math.pow(c2.imag, 2);
		double dividendo1 = c1.real * c1.imag + c2.real * c2.imag;
		double dividendo2 = c1.imag * c2.real - c1.real * c2.imag;
		return new Complex(dividendo1/divisor,dividendo2/divisor);
	}
	
	public static double modulo(Complex c) {
		return Math.sqrt(Math.pow(c.real,2)+Math.pow(c.imag,2));
	}
	
	public static Complex conjugado(Complex c) {
		double x = -c.imag;
		return new Complex(c.real , x);
	}
	
	public static Complex cartesianoPolar(Complex c) {
		double angulo = Math.atan((c.imag/c.real));
		double p = Math.sqrt(Math.pow(c.real,2)+Math.pow(c.imag,2));
		return new Complex(p , angulo);
	}
	
	public static Complex polarCartesiano(Complex c) {
		double x = c.real*Math.cos(c.imag);
		double y = c.real*Math.sin(c.imag);
		return new Complex(x , y);
	}
	
	public static double fase(Complex c) {
		double angulo = Math.atan((c.imag/c.real));
		return angulo;
	}
	
	public static void impresion(Complex c) {
		if(c.imag == 0) {
			System.out.println(c.real);
			return;
		}if(c.real == 0 ) {
			if (c.imag == 1) {
				System.out.println("i");
				return;
			}else if(c.imag == -1) {
				System.out.println( "-i");
				return;
			}
			System.out.println(c.imag+"i");
			return;
		}
		else if(c.imag > 0) {
			if (c.imag == 1) {
				System.out.println(c.real + " + i");
				return;
			}
			System.out.println(c.real + " + " + c.imag +"i");
			return;
		}
		else if(c.imag == -1) {
			System.out.println(c.real + " - i");
			return;
		}
		System.out.println(c.real+" - "+ Math.abs(c.imag) +"i");
		return;
	}
	
	public static void main(String[] args) {
		Complex c1 = new Complex(3.0,-2.0);
		Complex c2 = new Complex(1.0,2.0);
		Complex resultado = producto(c1,c2);
		//System.out.println(resultado.real + " " + resultado.imag);
		impresion(resultado);
	}
}