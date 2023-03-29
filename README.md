# Hermes parcel label

In this project, hermes parcel labels are created automatically in two different ways.
1. possibility
In the "entering" folder, parcel labels are created automatically after a request for parcel label data.

2nd possibility
A structure for the automatic creation of hermes parcel labels is specified in the text file user_input.txt (see folder reading).

First name Last name
Street
House number
Postcode
City
Email
Phone number
----
First name Last name
Street
House number
Postcode
City
Email
Telephone number
###
...................

The block from the beginning to the # character (use at least once for separation) is a parcel label with recipient and sender.
This block can follow several times in succession. Finally, a dot . follows at least once as the end of the file.

