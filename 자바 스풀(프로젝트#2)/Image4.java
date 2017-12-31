import java.awt.*;

import javax.swing.*;

public class Image4 extends JFrame	{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private ImageIcon image1;
	private JLabel label1;


	
	public Image4()	{
		setLayout(new FlowLayout());
		
		image1 = new ImageIcon(getClass().getResource("sudoku4.jpg"));
		
		label1 = new JLabel(image1);
		add(label1);
		
		
	}
	
	
}
