import java.awt.*;

import javax.swing.*;

public class Image extends JFrame	{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private ImageIcon image1;
	private JLabel label1;


	
	public Image()	{
		setLayout(new FlowLayout());
		
		image1 = new ImageIcon(getClass().getResource("sudoku1.jpg"));
		
		label1 = new JLabel(image1);
		add(label1);
		
	}
	
	
}
