import QtQuick 1.1
import com.nokia.meego 1.2
import com.nokia.extras 1.1

ApplicationWindow {
    Button { }
    Label { }
    PageHeader { }
    Slider { }
    Switch { }
    TextArea { }
    TextField { }
    Component {
        // These will be compiled but not instantiated.
        // If instantiation won't result in further caching then place those
        // components here.
        Item {
            ContextMenu { }
            DatePickerDialog { }
            TimePickerDialog { }
            Dialog { }
            ScrollDecorator { }
            Menu {
                MenuItem { }
            }
            Page { }
            Sheet { }
        }
    }
}

