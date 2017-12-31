import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;


public class events extends JFrame {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private JLabel label3;
	private JButton button;
	private int x=0;
	
	public events()	{
		setLayout(new FlowLayout());
		button = new JButton("If you want more sudoku, Click here");
		add(button);
		label3=new JLabel("");
		add(label3);
		event e = new event();
		button.addActionListener(e);
	}
	
	public class event implements ActionListener	{
		Random random = new Random();
		int n = random.nextInt(8);
		public void actionPerformed(ActionEvent e)	{
			label3.setText("You can solve more Sudoku");
			if(x==0) {
				switch (n)	{
				case 0 : {
					Image gui = new Image();
					//gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
					gui.setVisible(true);
					gui.pack();
					gui.setTitle("More Sudoku");
					break;
					}
				case 1 : {
					Image2 gui = new Image2();
					//gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
					gui.setVisible(true);
					gui.pack();
					gui.setTitle("More Sudoku");
					break;
					}
				case 2 :  {
					Image3 gui = new Image3();
					//gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
					gui.setVisible(true);
					gui.pack();
					gui.setTitle("More Sudoku");
					break;
					}
				case 3 :  {
					Image4 gui = new Image4();
					//gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
					gui.setVisible(true);
					gui.pack();
					gui.setTitle("More Sudoku");
					break;
					}
				case 4 :  {
					Image5 gui = new Image5();
					//gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
					gui.setVisible(true);
					gui.pack();
					gui.setTitle("More Sudoku");
					break;
					}
				case 5 :  {
					Image6 gui = new Image6();
					//gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
					gui.setVisible(true);
					gui.pack();
					gui.setTitle("More Sudoku");
					break;
					}
				case 6 :  {
					Image7 gui = new Image7();
					//gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
					gui.setVisible(true);
					gui.pack();
					gui.setTitle("More Sudoku");
					break;
					}
				case 7 :  {
					Image8 gui = new Image8();
					//gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
					gui.setVisible(true);
					gui.pack();
					gui.setTitle("More Sudoku");
					break;
					}
				}
			}
		}
	}
}
