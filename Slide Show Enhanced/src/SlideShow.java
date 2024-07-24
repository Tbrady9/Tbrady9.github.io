import java.awt.BorderLayout;
import java.awt.CardLayout;
import java.awt.EventQueue;
import java.awt.FlowLayout;
import java.awt.HeadlessException;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import java.awt.Dimension;
import javax.swing.BorderFactory;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Vector;


// Declaration of destination class
class Destination {
	public String destination;
	public String description;
	public int rating;
	public String image;
	
		
	// Constructor
	Destination(String destination, String description, int rating, String image) {
		this.destination = destination;
		this.description = description;
		this.rating = rating;
		this.image = image;
		}
	

	// Destination array
	static Destination[] destination_array;
	

	// Method to fill destination object array with data
	static void fillArray() {
		
	
	// Allocating memory
	destination_array = new Destination[8];
	
				
	// Initializing all array elements
	destination_array[0] = new Destination("Grand Canyon",
			"Spectacular canyon views and hiking. Everyone should see the Grand Canyon"
			+ " at least once in their lifetime",
			8,
			"/resources/TestImage1.jpg");
	destination_array[1] = new Destination("Paris",
			"World-class museums, fashion, cuisin and atmophere. Come see what Ernest"
			+ " Hemingway called the city of 'many splendors'",
			9,
			"/resources/Paris.jpg");
	destination_array[2] = new Destination("Barcelona",
			"Located on the Mediterranean Sea, Barcelona is a hub of new trends in the world"
			+ " of culture, fashion, and cuisine famous for Gaudi and Art Nouveau architecture",
			8,
			"/resources/Barcelona.jpg");
	destination_array[3] = new Destination("Rome",
			"Called the 'Eternal City' by the ancient Romans, Rome is home to glorious monuments"
			+ " and colossal remains",
			6,
			"/resources/Rome.jpg");
	destination_array[4] = new Destination("Amsterdam",
			"Capital of the Netherlands with famous scenic canals, rich history, and iconic cultural scene",
			7,
			"/resources/Amsterdam.jpg");
	destination_array[5] = new Destination("Chichen Itza",
			"This sacred city, built between the 9th and 12th century, contains beautifully restored "
			+ "stepped pyramids and temples",
			7,
			"/resources/ChichenItza.jpg");
	destination_array[6] = new Destination("Las Vegas",
			"With gambling, shows, nightclubs, dayclubs, dining, shows, and fabulous outdoor opportunities, "
			+ "see why Las Vegas is one of the most-visited destinations in the world",
			7,
			"/resources/Vegas.jpeg");
	destination_array[7] = new Destination("Venice",
			"Glide in a gondola through the quiet canals. Home of St. Mark's Basilica and"
			+ " many other wonderous sights",
			8,
			"/resources/Venice.jpg");
	}
	
	
	// Method to return the destination name
	String getDestination() {
		return this.destination;
	}
	
	
	// Method to return the destination description
	String getDescription() {
		return this.description;
	}
	
	
	// Method to return the destination rating
	int getRating() {
		return this.rating;
	}
	
	
	// Method to return the destination image path
	String getImage() {
		return this.image;
	}
	
	
	/*
	 *  Sort by rating functionality
	 *  sorts the array items by the destination name
	 *  Input: None, Output: None 
	 */
	static void sortDestination() {
		Arrays.sort(destination_array, new DestinationComparator());
	}
	
	
	/*
	 *  Sort by rating functionality
	 *  sorts the array items by the rating
	 *  Input: None, Output: None 
	 */
	static void sortRating() {
		Arrays.sort(destination_array, new RatingComparator());
	}
}


// Class to compare descriptions for sorting the array of destination objects
class DestinationComparator implements Comparator<Destination> {

	@Override
	public int compare(Destination o1, Destination o2) {
		return o1.getDestination().compareTo(o2.getDestination());
	}
	
}


// Class to compare ratings for sorting the array of destination objects
class RatingComparator implements Comparator<Destination> {

	@Override
	public int compare(Destination o1, Destination o2) {
		return o2.getRating() - o1.getRating();
	}
	
}


// Class to allow use of combo box to sort and refresh the panels
class comboBox {
	// String array for sorting combo box
	static String[] sortOptions = {"Sorted by Rating", "Sorted by Name"};
		
	// Combo box for sorting drop down
	static JComboBox<String> sortBox = new JComboBox<>(sortOptions);
}


// Slide show class to create the application layout
public class SlideShow extends JFrame {

	// Declare Variables
	private JPanel slidePane;
	private JPanel textPane;
	private JPanel buttonPane;
	private CardLayout card;
	private CardLayout cardText;
	private JButton btnPrev;
	private JButton btnNext;
	private JLabel lblSlide;
	private JLabel lblTextArea;	
	

	// Create the application
	public SlideShow() throws HeadlessException {
		initComponent();
	}
	

	/*
	 *  Initialize frame content
	 *  Sets up the layout and options for the frame and everything within it
	 *  Input: None, Output: None 
	 */
	private void initComponent() {
		// Initialize variables
		card = new CardLayout();
		cardText = new CardLayout();
		slidePane = new JPanel();
		textPane = new JPanel();
		
		
		// Text pane settings
		textPane.setBackground(new java.awt.Color(220, 220, 255));
		textPane.setBounds(145, 517, 500, 80);
		textPane.setVisible(true);		
		textPane.setBorder(BorderFactory.createCompoundBorder(BorderFactory.createLineBorder(new java.awt.Color(35, 35, 35), 1),
				BorderFactory.createLineBorder(new java.awt.Color(250, 200, 200), 2)));
		
		
		// Button settings
		buttonPane = new JPanel();
		btnPrev = new JButton();
		btnNext = new JButton();
		lblSlide = new JLabel();
		lblTextArea = new JLabel();
		
		
		// Setup frame attributes
		setSize(800, 700);
		setLocationRelativeTo(null);
		setTitle("Top Destinations SlideShow");
		getContentPane().setLayout(new BorderLayout(10, 95));
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setResizable(false);
		

		// Setting the layouts for the panels
		slidePane.setLayout(card);
		slidePane.setBackground(new java.awt.Color(220, 220, 255));
		slidePane.setBorder(BorderFactory.createCompoundBorder(BorderFactory.createLineBorder(new java.awt.Color(35, 35, 35), 1),
				BorderFactory.createLineBorder(new java.awt.Color(250, 200, 200), 2)));
		textPane.setLayout(cardText);
		buttonPane.setBackground(new java.awt.Color(220, 220, 255));
		buttonPane.setBorder(BorderFactory.createCompoundBorder(BorderFactory.createLineBorder(new java.awt.Color(35, 35, 35), 1),
				BorderFactory.createLineBorder(new java.awt.Color(250, 200, 200), 2)));
		
		
		// Logic to add each of the slides and text
		for (int i = 0; i <= 7; i++) {
			lblSlide = new JLabel();
			lblTextArea = new JLabel();
			lblSlide.setText(getResizeIcon(i));
			lblTextArea.setText(getTextDescription(i));
			slidePane.add(lblSlide, "card" + i);
			textPane.add(lblTextArea, "cardText" + i);
		}

		getContentPane().add(slidePane, BorderLayout.CENTER);
		getContentPane().add(textPane, BorderLayout.SOUTH);
		buttonPane.setLayout(new FlowLayout(FlowLayout.CENTER, 20, 10));

		
		/*
		 *  Previous button setup
		 *  Sets up the layout and options for the 'previous' button
		 *  Input: None, Output: None 
		 */
		btnPrev.setText("Previous");
		btnPrev.setBorder(BorderFactory.createCompoundBorder(BorderFactory.createLineBorder(new java.awt.Color(35, 35, 35), 1),
				BorderFactory.createLineBorder(new java.awt.Color(250, 200, 200), 2)));
		btnPrev.setPreferredSize(new Dimension(75, 20));	
		btnPrev.addActionListener(new ActionListener() {

			public void actionPerformed(ActionEvent e) {
				goPrevious();
			}
		});
		buttonPane.add(btnPrev);
		
		
		/*
		 *  Sorting combo box setup
		 *  Sets up the layout and options for the drop down box for sorting
		 *  Input: None, Output: None 
		 */
		comboBox.sortBox.setBorder(BorderFactory.createCompoundBorder(BorderFactory.createLineBorder(new java.awt.Color(35, 35, 35), 1),
				BorderFactory.createLineBorder(new java.awt.Color(250, 200, 200), 2)));
		buttonPane.add(comboBox.sortBox);
		getContentPane().add(buttonPane, BorderLayout.SOUTH);
		

		/*
		 *  Next button setup
		 *  Sets up the layout and options for the 'next' button
		 *  Input: None, Output: None 
		 */
		btnNext.setText("Next");
		btnNext.setBorder(BorderFactory.createCompoundBorder(BorderFactory.createLineBorder(new java.awt.Color(35, 35, 35), 1),
				BorderFactory.createLineBorder(new java.awt.Color(250, 200, 200), 2)));
		btnNext.setPreferredSize(new Dimension(75, 20));
		btnNext.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				goNext();
			}
		});
		buttonPane.add(btnNext);
	}
	

	/*
	 *  Next button functionality
	 *  Loads the previous slide
	 *  Input: None, Output: None 
	 */
	private void goPrevious() {
		card.previous(slidePane);
		cardText.previous(textPane);
	}
	
	
	/*
	 *  Next button functionality
	 *  Loads the next slide
	 *  Input: None, Output: None 
	 */
	private void goNext() {
		card.next(slidePane);
		cardText.next(textPane);
	}
	
	
	/*
	 *  Re-Sort combo box functionality (sort by destination)
	 *  Calls the sort function to sort by destination
	 *  Input: None, Output: None 
	 */
		private static void destinationSort() {
			Destination.sortDestination();
	}
	
	
	/*
	 *  Re-Sort combo box functionality (sort by rating)
	 *  Calls the sort function to sort by rating
	 *  Input: None, Output: None 
	 */
		private static void ratingSort() {
			Destination.sortRating();
		}
		
		
	/*
	 *  Get and format the image
	 *  Finds the image associated with the array index and formats it for the slide
	 *  Input: array index, Output: destination image 
	 */
	private String getResizeIcon(int i) {
		String image = "";
		String imagePath = "";
		imagePath = Destination.destination_array[i].image;
		image = "<html><body style='padding-left: 50px;'><img width=655 height=450 src='" 
				+ getClass().getResource(imagePath) + "'</body></html>";
		return image;
	}
	
	/*
	 *  Get and format the text
	 *  Finds the text data associated with the array index and formats it for the slide
	 *  Input: array index, Output: destination text data 
	 */
	private String getTextDescription(int i) {
		String destination = "";
		String description = "";
		int rating;
		String text = "";
		
		
		// Setting the information for each destination
		destination = Destination.destination_array[i].destination;
		description = Destination.destination_array[i].description;
		rating = Destination.destination_array[i].rating;
		text = "<html><body style='text-align: center; padding-left: 2px; font-family: 'Barlow', sans-serif;>"
				+ "<font size='4'>"
			    + "#" + (i+1) + ": " + destination
				+ "</font>" + "<br>"
				+ description
				+ "<br>" + "<font size='3'>"
				+ "Average Rating: " + rating + " out of 10"
				+ "</font>" + "</body></html>";
		return text;
	}
	
	// Declare a SlideShow vector for holing each frame
	static Vector<SlideShow> slideVector = new Vector<>();
	
	
	// Launch the application
	public static void main(String[] args) {
		
		// Initially fill and sort the destination array
		if (Destination.destination_array == null) {
			Destination.fillArray();
			Destination.sortRating();
		}
		
		// Run the program and create a slideshow
		EventQueue.invokeLater(new Runnable() {

			@Override
			public void run() {

				// Create new slideshow and add it to a vector of slideshows
				slideVector.addElement(new SlideShow());
				slideVector.lastElement().setVisible(true);
				
				// Drop down box action listener for sorting
				comboBox.sortBox.addActionListener(new ActionListener() {
					
					// Sort according to drop down option chosen
					@Override
					public void actionPerformed(ActionEvent e) {
						// re-sort the destination object array by user choice
						if (comboBox.sortBox.getSelectedItem().equals("Sorted by Rating")) {
							ratingSort();
						}
						else {
							destinationSort();
						}
						
						/*
						 *  For each change of the drop down sort box, this will
						 *  dispose of the last slideshow, remove it from the array,
						 *	and create a new slideshow
						 */
						slideVector.lastElement().dispose();
						slideVector.remove(0);
						slideVector.addElement(new SlideShow());
						slideVector.lastElement().setVisible(true);						
					}
				});
			}
		});
	}
}


				
