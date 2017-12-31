import java.util.Random;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Sudoku3 extends JFrame{
	private static JLabel label3;
	private static JButton button;
	private static JLabel label4;
	private static JButton button2;
	private static int x=0;
	
	static int sudoku_grid[][]=new int[9][9];
	JTextField[][] igrid=new JTextField[9][9];
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

		   
	static int grid[][]=new int[9][9];


	public static void main(String[] args) throws InterruptedException{
		// TODO Auto-generated method stub
		Sudoku3 all = new Sudoku3();
		all.inputs();
	}
	
	public void inputs()	{
		JFrame sudoku = new JFrame();
		sudoku.setTitle("My Sudoku Solver");
		sudoku.setSize(600,600);
		JPanel Board = new JPanel();
		Board.setLayout(new GridLayout(10,10));
		for (int i=0;i<9;i++)	{
			for (int j=0;j<9;j++)	{
				this.igrid[i][j]=new JTextField();
				this.igrid[i][j].setBounds(60*(i+1), 60*(j+1), 60, 60);
				this.igrid[i][j].setBorder(BorderFactory.createLineBorder(Color.DARK_GRAY));
				Font font = new Font("Bauhaus 93", Font.PLAIN, 20);
				this.igrid[i][j].setFont(font);
				this.igrid[i][j].setBackground(Color.white);
				this.igrid[i][j].setText("0");
				this.igrid[i][j].setOpaque(true);
				this.igrid[i][j].setHorizontalAlignment(JTextField.CENTER);
				Board.add(this.igrid[i][j]);
			}
		}
		button = new JButton("ÈùÆ®");
		Board.add(button);
		label3=new JLabel("");
		Board.add(label3);
		button2 = new JButton("´ä");
		Board.add(button2);
		label4=new JLabel("");
		Board.add(label4);
		event e = new event();
		button.addActionListener(e);
		button2.addActionListener(e);
		sudoku.add(Board);
		sudoku.setVisible(true);
		
	}
	public class event implements ActionListener	{
		public void actionPerformed(ActionEvent e)	{
			
			for (int i=0;i<9;i++)	{
				for (int j=0;j<9;j++)	{
					if (igrid[i][j].getText()!="0")	{
						sudoku_grid[i][j]=Integer.parseInt(igrid[i][j].getText());
					}
					else	{
						sudoku_grid[i][j]=0;
					}
				}
			}
			for (int i=0;i<9;i++)	{
				for (int j=0;j<9;j++)	{
					grid[i][j]=sudoku_grid[i][j];
				}
			}
			grid=run(0,0,grid);
			if(x==0) {
			if (e.getActionCommand()=="ÈùÆ®") {
				Random random = new Random();
				int n = random.nextInt(9);
				show(hint(n, grid));
				
			}
			else if	(e.getActionCommand()=="´ä") {
				show(grid);
				events gui = new events();
				//gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
				gui.setVisible(true);
				gui.setSize(400,200);
				gui.setTitle("More Sudoku");
			}
			}
		}
	}

	
	public void show(int[][] grid)	{
		setTitle("My Sudoku Solver");
		setSize(450,450);
		JPanel Board = new JPanel();
		Board.setLayout(new GridLayout(9,9));
		
		JLabel[][] bgrid=new JLabel[9][9];
		for (int i=0;i<9;i++)	{
			for (int j=0;j<9;j++)	{
				bgrid[i][j]=new JLabel();
				bgrid[i][j].setBounds(50*(i+1), 50*(j+1), 50, 50);
				bgrid[i][j].setBorder(BorderFactory.createLineBorder(Color.DARK_GRAY));
				Font font = new Font("Bauhaus 93", Font.PLAIN, 20);
				bgrid[i][j].setFont(font);
				bgrid[i][j].setBackground(Color.white);
				bgrid[i][j].setText(String.valueOf(grid[i][j]));
				bgrid[i][j].setOpaque(true);
				bgrid[i][j].setHorizontalAlignment(JTextField.CENTER);
				Board.add(bgrid[i][j]);
			}
		}
		this.add(Board);
		setVisible(true);
	}
	
	
	public static int[][] hint(int n, int[][] grid)	{
		int x,y;
		for (x=0;x<=n;x++)	{
			for (y=0;y<n;y++)	{
				grid[x][y]=0;
			}
		}
		for (x=n+1; x<9; x++)	{
			for(y=0; y<9; y++) {
				grid[x][y]=0;
			}
		}
		for (x=0; x<n; x++) {
			for(y=n; y<9; y++) {
				grid[x][y]=0;
			}
		}
		for (y=n+1; y<9; y++)	{
			grid[n][y]=0;
		}
		return grid;
	}
	public static boolean check(int x, int y, int[][] grid)	{
		String its="";
		for (int i=0;i<9;i++)	{
			its+=new Integer(grid[i][y]).toString();
			its+=new Integer(grid[x][i]).toString();
			its+=new Integer(grid[(x/3)*3+i/3][(y/3)*3+i%3]).toString();
		}
		int cnt=0, index=-1;
		while ((index=its.indexOf(new Integer(grid[x][y]).toString(), index+1))!=-1)	{
			cnt++;
		}
		return cnt==3;
	}
	public static int[][] run(int y, int x, int[][] grid)	{
		while(!check(8, 8, grid) || grid[8][8]==0)	{
			if (sudoku_grid[y][x]!=0)	{
				
				int ny,nx;
				if (x==8)	{
					ny=y+1;
					nx=0;
				}
				else	{
					ny=y;
					nx=x+1;
				}
				run(ny, nx, grid);
			}
		
			else	{
				if (grid[y][x]<9)	{
					grid[y][x]++;
					if (check(y, x, grid))	{
						int ny,nx;
						if (x==8)	{
							ny=y+1;
							nx=0;
						}
						else	{
							ny=y;
							nx=x+1;
						}
						run(ny, nx, grid);
					}
				}
				else	{
					grid[y][x]=0;
					break;
				}
			}	
		}
		return grid;
	}
}
