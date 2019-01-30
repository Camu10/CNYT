import java.util.*;

public class Complex {
	
	private double real;
	private double imag;
	
	public Complex() {
		real = 0.0;
		imag = 0.0;
	}
	
	public Complex(double real, double imag) {
		this.real = real;
		this.imag = imag;
	}
	
	
	public static double modulo(Complex c) {
		return Math.sqrt(Math.pow(c.real,2)+Math.pow(c.imag,2));
	}
	
	public static Complex conjugado(Complex c) {
		double x = -c.imag;
		return new Complex(c.real , x);
	}
	
	public double getImag() {
		return imag;
	}
	
	public double getReal() {
		return real;
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
		
		Complex resultado = ComplexMath.producto(c1,c2);
		//System.out.println(resultado.real + " " + resultado.imag);
		impresion(resultado);
		Vector<Vector<Complex>> v = new Vector<Vector<Complex>>();
		v.addElement(c1);
		
	}
}