========================
Specification and design
========================

As previously addressed, the overarching goal of this project was to be able to provide a domain specific query language (DSQL) of sufficient flexibility to obtain useful and sufficiently bespoke data from its queries. This was intended to be achieved whilst upholding sensible and intuitive syntactic conventions. The following are more granular objectives which were set to achieve this, accompanied by the design decisions and considerations taken.

The front end aspect of the project was jettisoned due to time constraints, as well as not being at the core of the aspect of computing that this project was attempting to explore.

++++++++++++++
specifications
++++++++++++++

To have query input verification capable of accurately catching and reporting all potential notational and syntactic errors. The verification method should be able to stop any erroneous input from being passed to the web scraper. If time is available, it should also be able to describe the nature of the error to the user.

To have a web scraper that has the versatility to be able to take in input from any valid DSQL statement. This would include the accommodation of any amount of categories of data and their related stipulations and rules.

The ability to further modify and refine scraped data through the instructions of the DSQL statement, being able to apply an unbounded number of filters to rows of data based on their values, as well as apply aggregate functions and order the data.

To be able to graphically display the data in a manner specified by a DSQL statement. The programme’s visualisation capability should be versatile enough to allow the user to generate graphs that clearly display the intended data.

The project should be designed with expandability in mind. This should be reflected in the architecture of the overall program, through which extension of functionality in the form of the addition of new modules or classes should be simple, for example with new spider classes, or modification of existing classes or the addition of entire modules.

The syntax was also designed with the goal of simple implementation of additional functionality, such as new stipulations for the data associated with each category of scraped data, as well as new blocks of functionality responsible for the invocation of new modules that had been added to the project. This was intended to be fulfilled through the mimicking of  data structures such as lists within the language, accommodating an unbounded amount of new clauses, as well as the syntax following a sequence of stages, to which new ones could be appended.



++++++++++++++++++
Technology choices
++++++++++++++++++

The following are the tools which were used to implement the program, accompanied by the reasoning behind their selection.

+++++++++
Languages
+++++++++

The project was developed entirely in the Python version 3.9. Python was chosen due to its ease and speed of implementation, as well as versatility, making the integration between the compiling of the SDQL and passing of variables to the underlying framework more intuitive and less error-prone. It also hosts many of the most popular and highly regarded web scraping frameworks.
