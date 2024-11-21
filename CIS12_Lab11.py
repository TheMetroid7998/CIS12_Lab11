from MindMapLeaf import MindMapLeaf
from MindMapComposite import MindMapComposite

def main():
    if __name__ == "__main__":
        root = MindMapComposite( "The Battle at Wolf 359", "circle" )

        characters = MindMapComposite( "Characters", "oval" )
        characters.append( MindMapLeaf( "Jean-Luc Picard / Locutus", "plain" ) )
        characters.append( MindMapLeaf( "William Riker", "plain" ) )
        characters.append( MindMapLeaf( "Data", "plain" ) )
        characters.append( MindMapLeaf( "Worf", "plain" ) )
        characters.append( MindMapLeaf( "Borg Queen (implied presence)", "plain" ) )
        root.append( characters )

        plot_points = MindMapComposite( "Plot Points", "square" )
        plot_points.append( MindMapLeaf( "Picard is assimilated by the Borg", "plain" ) )
        plot_points.append( MindMapLeaf( "Riker takes command of the Enterprise", "plain" ) )
        plot_points.append( MindMapLeaf( "The Federation fleet suffers heavy losses", "plain" ) )
        plot_points.append( MindMapLeaf( "Enterprise crew devises a plan to stop the Borg", "plain" ) )
        root.append( plot_points )

        themes = MindMapComposite( "Themes", "cloud" )
        themes.append( MindMapLeaf( "Identity and loss of self", "plain" ) )
        themes.append( MindMapLeaf( "Duty and leadership", "plain" ) )
        themes.append( MindMapLeaf( "Humanity vs. technology", "plain" ) )
        themes.append( MindMapLeaf( "Collectivism vs. individuality", "plain" ) )
        root.append( themes )

        setting = MindMapComposite( "Setting", "hexagon" )
        setting.append( MindMapLeaf( "USS Enterprise-D", "plain" ) )
        setting.append( MindMapLeaf( "Wolf 359 (space battle location)", "plain" ) )
        setting.append( MindMapLeaf( "Borg Cube", "plain" ) )
        setting.append( MindMapLeaf( "Starfleet Command (background communication)", "plain" ) )
        root.append( setting )

        conflicts = MindMapComposite( "Major Conflicts", "bang" )
        conflicts.append( MindMapLeaf( "Federation vs. Borg (existential threat)", "plain" ) )
        conflicts.append( MindMapLeaf( "Riker’s internal struggle as acting captain", "plain" ) )
        conflicts.append( MindMapLeaf( "Enterprise's fight to save Picard from assimilation", "plain" ) )
        root.append( conflicts )

        dialogue = MindMapComposite( "Dialogue Highlights", "oval" )
        dialogue.append( MindMapLeaf( "“I am Locutus of Borg. Resistance is futile.”", "plain" ) )
        dialogue.append( MindMapLeaf( "Riker: \"Mr. Worf, fire.\"", "plain" ) )
        dialogue.append( MindMapLeaf( "Guinan advising Riker on letting go of Picard", "plain" ) )
        root.append( dialogue )

        stage_directions = MindMapComposite( "Significant Stage Directions", "square" )
        stage_directions.append( MindMapLeaf( "Close-up of Picard’s face as Locutus", "plain" ) )
        stage_directions.append( MindMapLeaf( "Panoramic view of the devastated fleet at Wolf 359", "plain" ) )
        stage_directions.append( MindMapLeaf( "Enterprise maneuvering to evade the Borg", "plain" ) )
        stage_directions.append( MindMapLeaf( "Tense bridge scenes as the crew works together", "plain" ) )
        root.append( stage_directions )

        root.display()


if __name__ == "__main__":
    main()