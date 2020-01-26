package Jan;

import java.util.Scanner;

public class ChefStreetFood {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while (t-->0) {
			
			int n = sc.nextInt();
			int mprofit = 0;
			while (n-->0) {
				int s=sc.nextInt();
				int p=sc.nextInt();
				int v= sc.nextInt();
				
				int cp= p/(s+1);
				int profit = cp*v;
				if (profit>mprofit) mprofit=profit;
				
			}
			System.out.println(mprofit);
		}
		

	}

}
