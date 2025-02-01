# Graphical Abstract Generator

This project is designed to generate graphical abstracts from research papers. It integrates text extraction, visualization, and user customization options to create visually appealing representations of research findings.

## Features

- **Text Extraction**: Extracts key components from research papers, including titles, key findings, methods, and conclusions.
- **Visualization**: Generates structured charts and illustrations, overlaying text on images for clarity.
- **Customization**: Allows users to customize color schemes, layout styles, and design types to suit their preferences.

## Project Structure

```
graphical-abstract-generator
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── text_extraction
│   │   ├── __init__.py
│   │   └── extractor.py
│   ├── visualization
│   │   ├── __init__.py
│   │   └── visualizer.py
│   ├── customization
│   │   ├── __init__.py
│   │   └── customizer.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/graphical-abstract-generator.git
   ```
2. Navigate to the project directory:
   ```
   cd graphical-abstract-generator
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Customization Options

Users can customize the graphical abstract by adjusting the following settings:

- **Color Scheme**: Choose between dark mode, light mode, or custom themes.
- **Layout Style**: Select from vertical, horizontal, or mind-map layouts.
- **Design Type**: Opt for icon-based or text-heavy designs.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.