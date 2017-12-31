import java.awt.*;

import javax.swing.*;

public class Image7 extends JFrame	{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private ImageIcon image1;
	private JLabel label1;


	
	public Image7()	{
		setLayout(new FlowLayout());
		
		image1 = new ImageIcon(getClass().getResource("sudoku7.jpg"));
		
		label1 = new JLabel(image1);
		add(label1);
		
		
	}
	
	
}
