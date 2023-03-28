arXiv:cs/0211008v1 [cs.AI] 9 Nov 2002

## Can the whole brain be simpler than its "parts"?

Victor Eliashberg

Avel Electronics, Palo Alto, CA

  

> > > I am intolerant of those who regard the whole of biological data, of the
> phenomena of biological organization and intelligence, as not more than a
> grab bag from which to abstract technological goodies. My intolerance is
> tempered only by the belief that such casual abstraction cannot succeed...
> The point is, it is not a grab bag. The items therein show connection, and
> to attempt to draw out just one glittering generalization entails a host of
> contradictory loose ends.
>>>

>>> George W. Zopf, Jr. Attitude and Context. 1962.

  

### Abstract

This is the first in a series of connected papers discussing the problem of a
dynamically reconfigurable universal learning neurocomputer that could serve
as a computational model for the whole human brain. The whole series is
entitled "The Brain Zero Project. My Brain as a Dynamically Reconfigurable
Universal Learning Neurocomputer." (For more information visit the website
www.brain0.com.) This introductory paper is concerned with general
methodology. Its main goal is to explain why it is critically important for
both neural modeling and cognitive modeling to pay much attention to the basic
requirements of the whole brain as a complex computing system. The author
argues that it can be easier to develop an adequate computational model for
the whole "unprogrammed" (untrained) human brain than to find adequate formal
representations of some nontrivial parts of brain's performance. (In the same
way as, for example, it is easier to describe the behavior of a complex
analytical function than the behavior of its real and/or imaginary part.) The
"curse of dimensionality" that plagues purely phenomenological ("brainless")
cognitive theories is a natural penalty for an attempt to represent
insufficiently large parts of brain's performance in a state space of
insufficiently high dimensionality. A "partial" modeler encounters "Catch 22."
An attempt to simplify a cognitive problem by artificially reducing its
dimensionality makes the problem more difficult.

### 0.0   Introduction

The goal of this paper is to create the right methodological mental set for
understanding the general approach to brain modeling and cognitive modeling
adopted in this study. The paper consists of the following sections:

**Section 0.1   The Power of Mental Set** illustrates the power of a wrong
mental set and prepares the reader for the "unsuspected or the unwanted." (See
quotation from Burns (1958) at the end of this section.)

**Section 0.2   The Whole Human Brain as a Universal Learning Neurocomputer**
argues that the popular belief that universal learning systems don't exist is
a myth. This myth is a result of an inadequate "general" definition of the
concept of learning that doesn't include the "special case" of human learning.

**Section 0.3   On the Parts and the Whole** explains why the problem of the
parts of the brain and/or parts of brain's performance should not be separated
from the problem of the whole brain. It also formulates four general
propositions about the complexity of the models of the whole brain and the
models of behavior of cognitive system (Man,World).

**Section 0.4   Motivation and General Approach: the concept of E-machine**
outlines the general approach to brain modeling adopted in this study and
gives a verbal description of the metaphor the brain as an E-machine.

**Section 0.5   The Brain 0 Project** describes a reverse engineering
methodology for the development of an adequate computational model for the
"untrained" human brain.

**Section 0.6   Methodological Pitfalls** illustrates some pitfalls that await
a "partial" brain modeler and/or a "partial" cognitive modeler.

**Section 0.7   On Brain Hardware, Brain Software, and the Algorithms of
Thinking** presents a brief system engineering analysis of the strong and the
weak points of Artificial Intelligence (AI) and Artificial Neural Networks
(ANN) research as applied to the problem of the human brain and human
behavior.

**Section 0.8   The "Biological Grab Bag" Mentality Has not Succeeded**
suggests that Zopf, Jr. (1962) was right (see the epigraph above). It is
important to try to understand the real brain before making "glittering
generalizations." The catch is that such "generalizations" tend to include
everything, but the real brain.

**Section 0.9   Summary** summarizes the main claims made in this paper.

**References**

**Answers to Questions from Section 0.1**

### 0.1  The Power of Mental Set

Trying to describe and understand a new system we use concepts associated with
the systems we already know and understand. This metaphorical approach works
well when the concepts we are trying to use are applicable to the new system.
If not, we may get caught into the pitfall of a misleading metaphor. A
misleading metaphor creates a wrong mental set that prevents us from
understanding the new system. This powerful psychological phenomenon is well
illustrated by the following old anecdote.

The action takes place when streetcars were just introduced to replace horse
driven cabs. A cabman attends a lecture on the principles of operation of a
streetcar. After the lecture he makes the following comment: "I understood
almost everything. The only part I missed is where they attach the horse."

The cabman familiar with the concept of a horse driven vehicle had no
difficulties recognizing a streetcar as a vehicle. His knowledge base
associated with horse driven cabs contained such useful concepts as wheels,
shock absorbers, etc. that are applicable to streetcars as well. However, the
familiar notion of the driving force coming from a horse turned out to be
misleading. It created a wrong mental set that prevented the cabman from
understanding the novel idea of an electrically driven vehicle.

The reader should be aware of the power of mental set. To experience this
power, try to answer the following four questions. Check how long it will take
you to find the answers. If it takes too long, click on the answers.

  * **Question 1** (requires knowledge of American history)  
_   Which American presidents are not buried in American soil?_ (answer)

  * **Question 2** (requires knowledge of zoology)  
_   What big white animal can see backward as well as it can see forward?_
(answer)

  * **Question 3** (requires knowledge of physics)  
_   A dog has a bunch of empty cans attached to his tale. How fast should the
dog run to hear no sound from the clinging cans?_ (answer)

  * **Question 4** (requires knowledge of mathematics)  
_   There are two wallets and two pennies. How should you divide the money
between wallets so one wallet would have two times more money than the other?_
(answer)

If you didn't known all the answers in advance, you, probably, got some idea
as to how a wrong mental set can influence your thinking. Now, you are better
prepared to discuss the problem of the whole brain. When it comes to the whole
brain, it is essential not to be too sure about anything. Bear with me.

In the modern era of information processing systems, a researcher trying to
understand the brain has no difficulty recognizing the brain as an information
processing system. Depending on his/her background and interests, he/she then
tries to use concepts associated with the known systems for understanding the
brain. Quite often, he/she gets caught into a "streetcar-horse" pitfall.

The brain is such a remarkable system, that different aspects of its
organization and work evoke associations with many known systems. Like the
magical mirror from the J.K. Rowling novel, the brain shows everyone what one
wants to see. A computer scientist familiar with symbol manipulation
algorithms finds symbol manipulation algorithms. An expert in dynamical
processes finds dynamical processes. An applied mathematician interested in
optimization procedures finds optimization procedures. A fuzzy logic guru
finds fuzzy logic. A physicist finds spin-glasses, holographic memory, and
annealing. The list goes on and on. Referring to this phenomenon,  the
neurophysiologist Burns (1958) wrote that (when one is dealing with the brain)
"it is distressingly easy to find what one is looking for and remarkably
difficult to discern the unsuspected or the unwanted."

### 0.2   The Whole Human Brain as a Universal Learning Neurocomputer

There exists a large and rapidly growing set of various computational models
aimed at understanding what can be loosely referred to as "parts" of the brain
and/or "parts" of its performance. It would take thousands of pages just to
list the titles of the respective publications. Important and interesting as
they are, such partial models cannot address the most fundamental question
associated with the whole brain as a computing system:

_

  * How does the whole brain learn to perform mental computations?_    (Or simply speaking, how does the whole brain learn to think?) 

Imagine a theory of an airplane that discusses numerous parts of the airplane
and tries to explain how these parts work. The only question the theory
doesn't address is how the whole airplane flies. I believe, this metaphor
gives a fair characterization of the current state of computational theory of
the brain. To substantiate this claim consider the following observations.

A person with a sufficiently large external memory device can perform, in
principle, any effective computational procedure. As is well known, this
observation had led famous English mathematician Alan Turing (1936) to the
invention of his machine and to a formalization of the intuitive notion of an
algorithm.

We can extend Turing's observation and notice that a person with a good visual
memory can perform, in principle, any mental computations using an imaginary
memory device. (See Baddeley, 1982.) Ignoring some severe, but theoretically
unimportant limitations on the size of the working space available via such a
mechanism of mental imagery, we can conclude that the human brain itself (not
just a person with an external memory device) is a universal computing system.

We are not born with the knowledge of all possible algorithms. Nevertheless,
we can learn to perform, in principle, any algorithm. By learning to perform
certain computations with the use of an external memory device we
automatically learn to perform similar mental computations. This observation
shows that the whole human brain is a universal programmable computing system
and that the effect of universal programming can be achieved via process we
call learning. This means that the whole human brain is a universal learning
computing system.

There is a popular myth that universal learning systems don't exist. This myth
is based on the "rigorous proof" that no system can learn to simulate a
grammar of Chomsky type 2 (context-free) and higher (types 1 and 0). This
proof obviously contradicts to the fact that we humans are universal learning
systems.

_

  * How can one explain this paradox?_ 
The explanation is very simple. The formal definition of learning used to
obtain the above rigorous proof doesn't include the "special case" of human
learning. (see www.brain0.com)

**REMARK.** This paradox gives an example of a well known pitfall associated
with the use of the so-called "mathematical" mentality in connection with
"physical" problems. The catch is that to find an adequate mathematical
definition of a nontrivial physical problem is as difficult as to solve this
problem. For example, try to give a formal definition, of the problem of
simulating the behavior of electromagnetic field in a complex microwave device
without the Maxwell equations.

**NOTE.** In this paper, I use the Maxwell equation metaphor several times.
Interestingly enough, many aspects of this metaphor turn out to be quite
relevant to the issue of the general methodology of brain modeling and
cognitive modeling. Don't take this metaphor literally. Its goal is to obviate
some subtle methodological pitfalls associated with the use of "mathematical"
(or "engineering") mentality in connection with the "physical" (biological)
problem of the human brain and human behavior.

_

  * What is the nature of the brain's universality as a computing system? 
  * How can a brain-like universal computing system be implemented in a way consistent with modern neurobiological data? 
  * What data storage algorithm can be used by such a system to make it a universal learning system? 
  * What is short-term memory (working memory)? 
  * What is the explanation of mental imagery? 
  * How do we learn to perform computations with the use of an imaginary memory device after performing similar computations with the real device? 
  * What is mental set? 
  * How does the brain dynamically change its attitude to adjust to a combinatorial number of different contexts? 
  * How can various psychological phenomena of short-term memory and mental set be connected with the properties of protein molecules embedded in neural membranes?_ (Modern neurobiological data point in this direction.) 

The strategy of partial modeling produced no meaningful answer to this set of
basic questions associated with the whole human brain as a complex computing
system. Therefore, the above-mentioned airplane metaphor may not be as big an
exaggeration as it may seem.

### 0.3   On the Parts and the Whole

_

  * Why is everybody so busy developing "parts" for a complex system and nobody seems to care about the fundamental requirements of the whole system?_

The answer is mental set. It is "well known" that the whole brain is such an
enormously complex and unexplored a system that trying to develop its
computational model at the present time would be a waste of time. Therefore,
one should concentrate for a while on more limited problems associated with
"parts" of the brain and/or "parts" of brain's performance. ("A bird in the
hand is worth two in the bush.")

  * _Is this a reasonable attitude?_

I argue that it is not. In real life, it is seldom possible to develop right
parts for a complex system without paying much attention to the requirements
of the whole system. The same holds for reverse engineering. It is hardly
possible to reverse engineer nontrivial parts of a complex system without
having a good working hypothesis as to what this system is doing as a whole.
Ignoring the whole leads one into the pitfall of the parts that don't fit the
whole.

_

  * How complex should a meaningful computational model for the whole brain be?
  * Does it make sense to think about "simple" models of the whole brain? 
  * Is it worth talking about the so called "basic mechanisms" of the brain?
  * Why has the traditional Artificial Intelligence (AI) research failed to explain the phenomenon of human thinking?
  * Doesn't this failure prove that the whole brain is indeed an enormously complex system?
_

To get some answers to these important questions, we need to view the brain as
a part of a system (Man,World). Let (W,D,B) be a model of this system, where W
is an external world, D is a set of man-like sensory and motor devices, and B
is a computing system simulating the work of man's nervous system. For the
sake of simplicity, I will refer to system B as a model of the brain or simply
the brain. (At this general level, one can think of the rest of nervous system
as being a part of D).

It is useful to represent system (W,D,B) as a composition of two subsystems: B
and (W,D); where B is the brain, and (W,D) is the external world, W, as it
appears to the brain via the set of devices, D. In this representation, both
subsystems can be treated as abstract computing systems (machines), the inputs
of B being the outputs of (W,D) and vice versa. System B has a finite formal
representation. System (W,D) may have no finite formal representation. It
doesn't matter, however, from the viewpoint of simulation, since the external
world W is "always there" to experiment with.

Let B(t) be a formal representation of B after time t, where t=0 corresponds
to the "unprogrammed" (untrained) human brain. I argue that the following
general propositions are true:

  * **Proposition 1.** It is possible to find a relatively small (not too small!) formal representation of B(0).  
**Reason:** This representation is encoded in some form in the human genome.
Some data suggest that it may be small enough to fit into a single floppy
disk. (Smaller than traditional AI programs.)  
  

  * **Proposition 2.** Any adequate formal representation of B(t) with time t greater than, say, 10 years, must be very big: hundreds of gigabytes or, perhaps, terabytes. (Bigger than traditional AI programs.)  
**Reason:** This representation must include, in some form, the description of
the individual experience of a person.  
  

  * **Proposition 3.** It is practically impossible to reverse-engineer B(t) (for a big t) without first reverse-engineering B(0).  
**Reason:** The main part of description of B(t) depends on the properties of
the "informal" external world W. This part of description of B(t) cannot be
"preprogrammed" (at least for the first time).  
  

  * **Proposition 4.** It is practically impossible to develop adequate models of nontrivial parts of behavior of system (W,D,B(t)) without a formal representation of B(t). That is, it is practically impossible to have adequate purely phenomenological ("brainless") cognitive theories.  
**Reason:** It is like trying to simulate the behavior of the electromagnetic
field in a complex microwave device without the Maxwell equations describing
the "basic mechanisms" of the electromagnetic field. (See section 0.6.5).  
  

Let us assume that propositions 1-4 are true. _What should be the right
methodology of brain modeling and cognitive modeling?_ I argue that

  1. The main goal of brain modeling should be reverse-engineering B(0).
  2. The main goal of cognitive modeling should be deriving models of different specific cognitive phenomena from  the same  model of B(0) (or B(t) ) interacting with  different "external systems" (W,D).

**REMARK.** Using the Maxwell equation metaphor, item 1 can be loosely
compared with the problem of finding the Maxwell equations. Item 2 can be
compared with the problem of deriving different specific classical
electromagnetic phenomena from the same Maxwell equations coupled with
different boundary conditions and sources (different external worlds).

### 0.4  Motivation and General Approach: the Concept of E-machine

As a system engineer with a strong background in physics and mathematics, and
some knowledge of neurobiology and psychology, I became seriously interested
in the problem of the whole brain as a computing system in 1966. This study is
an attempt to summarize and systematize some insights resulted from this long-
term interest. I hope some of these system engineering insights will be found
thought-provoking by a broad range of readers interested in brain modeling and
cognitive modeling. I also hope that some of these insights will be of
interest to all users of the brain. After all, the whole brain is a complex
engineering system (designed by a very smart "system engineer"), and it is the
job of a system engineer to deal with the problem of reverse engineering this
system.

I want to emphasize that, in this study I am not interested in brain-inspired
engineering and/or brain-inspired mathematics. I believe that these popular
approaches ( whatever useful and important they might be from an engineering
and/or a mathematical viewpoint) do not help in understanding the real brain.
On the contrary, they tend to create misleading metaphors that inhibit one's
ability to understand the brain. The truth is, that the moment one defines a
brain-inspired engineering and/or mathematical problem one gets a problem
quite different from the original biological problem. What is even worse, this
irrelevant problem looks relevant and leads one into the pitfall of a
misleading metaphor.

I argue that in the case of the "physical" problem of the human brain and
human intelligence, the whole game of definitions doesn't make much sense.
_What does the word "define" mean? What does the word "mean" mean? What does
it mean "to understand?"_ And so on. These are "physical" questions! To answer
these questions one needs to understand how these words (or any other words of
our language) interact with our brain (more accurately, with the whole system
(W,D,B(t)) mentioned in section 0.3).

_Is it valid to use words which are not defined?_ For a person with a
"physical" mentality (like me) the answer is "yes". As Oliver Heaviside, the
inventor of the operational calculus, once said: "Shall I refuse my dinner,
because I do not fully understand .. digestion?" For a person with an orthodox
"mathematical" mentality this question is a nightmare. When it comes to the
problem of the whole human brain, everything becomes a "physical" problem,
even the mathematics itself.

Many people (especially engineers) believe that the main motivation for the
study of the brain as an information processing system is to learn how to
build intelligent robots. Though, as an engineer, I am very interested in
robots, I do not share this belief. As the owners and the users of the brains
we don't need any additional motivation to be interested in understanding the
brain.

The brain is our most important "personal computer." We need to understand
this computer to become better users. We need to know how to program (educate)
this computer and how to fix it when something goes wrong. And with all the
brainwashing going on around the world, we need to know how to protect this
computer against all kinds of "software viruses".

In this study, I am going to make several controversial propositions about the
basic computational mechanisms of the whole brain. To avoid accusations that I
will be making overly broad claims I provide the following

**DISCLAIMER.** I only claim that the ideas discussed in this study are
applicable to my own brain (since this was the only brain I could experiment
with). I leave it to the reader to decide as to whether these ideas are also
applicable to his or her brain.

My main claim is that the whole brain is a dynamically reconfigurable
universal learning neurocomputer arranged on the principle of E-machine.
(Eliashberg, 1967, 1979, 1981, 1988b, 1989, 1990b). In Eliashberg (1967), some
systems similar to those discussed in this study were called Associative
Automata. The name E-machines was introduced in (this author, 1979) to
distinguish these rather specific systems from other types of associative
learning machines. The letter "E" implies the word "Excitation." It was meant
to emphasize a connection between the concept of E-machine and the old
neurophysiological notion of "residual excitation" in the brain as the
mechanism of mental set (Vvedensky, 1901).

**NOTE.** There is a public company eMACHINES Inc. that makes personal
computers. The products of this company have nothing to do with the E-machines
discussed in this study. As was mentioned above, the name E-machine was
introduced in 1979 (before the creation of the above company). When this
company was created, I called its CEO and told him that the name E-machines is
used in my copyrighted manuscript. He didn't pay any attention. I understand
that a trademark and a copyright are two different things. At any rate, I
believe that my copyright (officially registered with the Library of Congress)
allows me to use this name without violating anybody's trademark.

  * _What is an E-machine?_

In the general case, an E-machine is a complex associative learning system
built from several (many) primitive associative learning systems referred to
as primitive E-machines or associative fields. A complex E-machine may also
include blocks called nuclei that provide interface among associative fields
and between associative fields and the external (sensory and motor) devices.

Associative fields can form associations of different modalities and can be
organized in hierarchical structures. In such hierarchical structures,
associative fields interact via large sets of associative fibers. A complex
E-machine may also include an "activating system" and "centers of emotion." By
mentioning the latter mechanisms, I want to emphasize that the existence of
such "noncomputational" mechanisms in the brain does not contradict the
general notion of the whole brain as a dynamically reconfigurable universal
learning neurocomputer.

A primitive E-machine has two main types of states:

  1. The states of encoded ("symbolic") long-term memory (LTM) that represent knowledge (the brain's software). These states are referred to as G-states, the letter "G" implying the notion of a modifiable synaptic Gain.
  
  

  2. The states of distributed analog ("dynamical") short-term memory (STM) and intermediate-term memory (ITM) that serve as a mechanism for the dynamic reconfiguration of the knowledge stored in LTM. These states are referred to as E-states, the letter "E" implying the notion of "residual Excitation". 

Paper 2 describes a formalism that connects the dynamics of the
phenomenological E-states with the conformational dynamics of ensembles of
protein molecules embedded in neural membranes. (Eliashberg, 1989, 1990a.) If
correct, this approach would justify quite complex assumptions about the
dynamic properties of E-states. (The program CHANNELS.EXE (see www.brain0.com)
illustrates some nontrivial possibilities of this formalism by allowing the
user to experiment with different assumptions about the microscopic structure
of ionic channels.)

In a primitive E-machine, G-state can have three components: G=(GX,GS,GY),
where GX is the state of Input LTM (ILTM) that represents the input parts of
associations, GY is the state of Output LTM (OLTM) that represents the output
parts of associations, and GS is the state of Structural LTM (SLTM) that
represents intermediate connections (and other modifiable parameters). GX and
GY can be characterized as encoded ("symbolic") memories, and GS, as a
"connectionist" memory. (Many traditional associative neural network models
can be viewed as implementations of some special cases of primitive
E-machines.)

In the general case, a primitive E-machine is a probabilistic rather than a
deterministic system: it employs a random choice to retrieve data from OLTM.
In the case of a neural implementation, this choice is accomplished via
reciprocal inhibition and fluctuation phenomena. Coupled with such a random
choice, the transformations of dynamical E-states provide a flexible mechanism
that controls the probabilities of symbolic processes in E-machines. Because
of this property, in Eliashberg (1979), the E-machines were characterized as
"non-classical symbolic processors."

**NOTE.** The basic concepts associated with classical symbolic machines are
useful for understanding some important aspects of the behavior of E-machines
(in the same way as, say, the concepts associated with linear systems are
useful for understanding some important aspects of the behavior of nonlinear
systems.) In the general case, however, an E-machine is just an E-machine, and
its behavior cannot be properly characterized in either "purely symbolic" or
"purely dynamic" terms.

At the general information processing level, the metaphor the brain as an
E-machine provides a nontrivial explanation of how the brain can process
symbolic information without moving symbols in a "symbolic" read/write memory.
Interestingly enough, the effect of such a symbolic read/write memory (working
memory) is achieved via transformations of "dynamical" E-states. Since the
transformations of E-states are done in a massively parallel way, this general
style of information processing allows the brain to combine the ability to
accumulate practically unlimited amount of data in the course of learning with
the ability to quickly process this data in the course of decision making. As
will be shown, this general approach leads to a rather simple (not too simple)
concept of a universal learning computing system (a model of B(0) from
Proposition 1).

An explicit example of a universal learning system is described in detail in
Paper 3. The program EROBOT.EXE (see www.brain0.com) allows the user to
perform interesting experiments with this educational model. Papers 1 and 2
(from this series of connected papers) provide a neurobiological background
that allows one to understand how the brain of this robot could be implemented
as a neural network.

**NOTE.** The general idea that the brain uses a combination of symbolic and
dynamical computational mechanisms is rather old. Several researchers
entertained different versions of this idea. (See, for example, Collins and
Quilian, 1972, Anderson, 1976). From time to time, this old idea is
rediscovered by new enthusiasts (who soon find out that it is a hard nut to
crack.) The metaphor the brain as an E-machine uses a specific formalization
and extrapolation of this general idea and integrates it with some other basic
ideas.

**DISCLAIMER.** To avoid misunderstanding, I want to emphasize that many
"partial" ideas employed and developed in this study (perhaps all such ideas)
can be found in a variety of different forms elsewhere. It is a specific
formalization, extrapolation and integration of such partial ideas that makes
a difference. The whole system is more than the sum of its parts and the devil
is in the details.

### 0.5  The Brain 0 Project

In section 0.3, I argued that the main goal of brain modeling should be
reverse engineering the "unprogrammed" brain B(0). I also argued that, without
an adequate model of B(0), one cannot reverse engineer B(t) for a big t, and
without B(t), it is impossible to do a simulation of nontrivial cognitive
phenomena in system (W,D,B(t)).Therefore, the main goal of this study is to
show how the metaphor the brain as an E-machine, outlined in the previous
section, can be used as a tool (a working hypothesis) for reverse engineering
B(0). I will refer to the corresponding reverse engineering project as the
**Brain 0 Project** (pronounced "the brain zero project.")

In what follows, I formulate five basic methodological principles (the "five
commandments") that determine the general methodology of this project. In
section 0.6, I will demonstrate some methodological pitfalls that result from
a violation of these principles.

#### 0.5.1   Methodological Principles (the "Five Commandments")

**Principle 1**   One should view the problem of developing a mathematical
(computational) model of B(0) as a "physical" (biological) rather than a
"mathematical" (or engineering) problem. That is, one should not try to
"define" this problem. One just needs to reverse engineer B(0) in whatever
possible way. (To define a physical problem is essentially the same as to
solve this problem!)

**Principle 2**   One should not use the criterion of  efficiency to evaluate
the quality of a model of B(0). The quality of such a model is determined only
by its ability to explain psychological and neurobiological facts.

**Principle 3**   One should try to falsify a model of B(0). If one finds a
fact that seems to contradict the model one needs to either show how a model
can explain this fact or try to modify the model, so it is capable of
explaining this fact. There should be no such thing as an unfalsifiable model
of B(0). (An unfalsifiable model is either a perfect model of B(0), which is
extremely unlikely, or an irrelevant model.)

**Principle 4**   One should reject wrong metaphors. (An uncontrolled
accumulation of misleading metaphors is a killer for any reverse engineering
project.)

**Principle 5**   First of all, one should try to reverse-engineer  the most
fundamental principles of organization and functioning of B(0) as a computing
system. These fundamental principles are independent of a specific
implementation of B(0). However, one should pay much attention to the specific
neurobiological implementation of B(0) to be able to reverse engineer the
above fundamental principles.

I want to emphasize the importance of principles 3 and 4 (which are not
popular among brain modelers and cognitive modelers). There is a tacit
agreement that one can ignore these principles (at least for a while), because
there is not enough reliable data about the brain to separate right metaphors
from wrong metaphors. I argue that this is far from the truth. As the users of
the brain we have an unlimited source of reliable psychological data about the
whole human brain. The analysis of language gives one an especially rich and
important source of such data. Combined with the stream of increasingly
reliable neurobiological data this psychological information allows one to
efficiently use principles 3 and 4.

Principle 2 is also critically important. To understand why efficiency is a
wrong criterion, see sections 0.6.2 and 0.6.4. Also consider the following
metaphor.

Imagine a group of mathematicians trying to solve a system of many equation,
each mathematician concentrating on just a few equations. These mathematicians
would be able to find many partial solutions satisfying their respective
subsets of equations. It is obvious, however, that not all such partial
solutions would satisfy the whole system of equations. Therefore, paraphrasing
a well known AI thesis about sufficiency, efficiency and necessity I can say
that to reverse engineer B(0), it is not sufficient to concentrate on
efficient solutions of just some psychological and/or neurobiological
equations. It is also necessary to try to select those solutions that satisfy
increasingly larger sets of such equations and reject those that don't.

The importance of the first part of Principle 5 is easy to understand. The
most fundamental constraints have higher weights than any other more specific
constraints, so they should be satisfied first. To understand why, consider
the following metaphor:  
Imagine a model of an electrical transformer that simulates the ability of
this transformer to produce noise and heat, but doesn't address the question
as to how this transformer transforms electricity. The ability to explain how
a transformer produces heat and noise may be an important advantage of a
model. However, it is important only in a model that also explains how a
transformer transforms electricity. Similarly, one should not expect too much
from a computational model of the brain that simulates the brain's ability to
produce, say, oscillations, but doesn't address the question as to how these
oscillations are connected with the brain's ability to process information.

The importance of the second part of Principle 5 is less obvious. This issue
is discussed in Section 0.7. The catch is that one cannot easily separate the
problem of the computations performed by the brain (the problem of the
"algorithms of thinking" per se) from the problem of brain hardware.

#### 0.5.2  Iterative Reverse Engineering Strategy

To be able to deal with a large number of "equations" needed for reverse
engineering B(0), I use a strategy that can be loosely described as the
following iterative algorithm. (The real reverse engineering process is never
so straightforward, so this algorithm is just a useful metaphor.)

**Step 0**   Formulate a set of questions addressing some fundamental
properties of B(0) as a computing system. Invent an initial approximation for
B(0), call it B0(0), that seems to answer these questions. Study B0(0) to show
that it does answer the above mentioned set of questions.

**Step 1**   Expand the set of questions and improve the current model, call
it Bi(0), to answer this expanded set of questions.

**Step 2**   Study Bi(0) to see if it indeed answers the current set of
questions. If not all questions can be answered, try to adjust the model to
answer all the questions.

**Step 3**   If step 2 is a success, go to step 1. Else, go to step 0 and try
to invent a better initial approximation.

#### 0.5.3  Initial Approximation. Converging vs. Diverging Iterations

As is well known, the success of an iterative process depends on the quality
of its initial approximation. I argue that this is true for the iterative
reverse engineering process described in section 0.5.2.

If the initial approximation for B(0), invented at step 0, is "supercritical"
(is sufficiently close to the original) one will get a "converging" process.
The more one will improve such an initial approximation the more possibilities
for its further improvements one will find. Eventually, one will converge to
an adequate model of B(0).

If the initial approximation is too far from the original ("subcritical"), one
will get a "diverging" process. The more one will try to improve such an
inadequate initial approximation the more discrepancies one will see. Soon it
will become obvious that this initial approximation doesn't work.

Using this metaphorical language, the metaphor the brain as an E-machine,
outlined in section 0.4, can be characterized as an attempt to develop a
"supercritical" initial approximation for B(0).

#### 0.5.4  Conceptual Levels

The enormous progress in system engineering was largely a result of two
critically important developments:

  1. Development of a set of system-theoretical and system engineering concepts that allow system engineers to efficiently deal with different conceptual levels of design (and understanding) of complex information processing systems.
  2. Development of computer-based tools satisfying the requirements of these different conceptual levels.

Since the whole brain is a complex information processing system, I argue that
the issue of conceptual levels and computer-based tools, supporting these
levels, is of critical importance for the development and understanding of
models of B(0).

The E-machine formalism corresponds to some "intermediate" conceptual level
for the representation of B(0). I will try to show that at this level the
models of B(0) become, in some sense, the most simple and the most
understandable without losing their essential properties as computing systems.
From this intermediate level, one can go "up" -- toward cognitive models
(models of behavior of system (W,D,B(0) ), and "down" -- toward neural network
models. Interestingly enough, to find a consistent neurobiological
interpretation of the phenomenological E-states, we will need to go "below"
traditional neural network models and deal with the statistical dynamics of
ensembles of protein molecules.

In contrast with the "top-down" methodology of AI and the "bottom-up"
methodology of ANN, the methodology of this study can be best characterized as
the "middle-up-down-middle" approach. (Note that this term implies a loop!)

#### 0.5.5  The Models of B(0) Can Be and Must Be Represented Explicitly

According to Proposition 1 from section 0.3, it is possible to find a
relatively simple formal representation of B(0). Therefore all models of B(0)
can and must be represented explicitly, so all the claims could be verified. I
argue that no special language is needed for such a representation, and such
popular languages as C or C++ are good enough. In this study, a combination of
a C-like notation and a scientific notation is used during the discussion of
the models. The Microsoft Visual C++ version 6.0 is used for computer
simulation.

As a system engineer, I am biased against the so-called "verbal models" of the
brain. It has been my experience, that a good intuition about the principles
of organization and functioning of a computing system can always be
transformed into an adequate formalism. If, by whatever reason, such a
transformation is not possible, it usually means that there is something wrong
with the intuition.

A model doesn't have to be (in fact, should not be) as complex as the original
to serve as a useful metaphor for understanding the original. However, as
Einstein said, "everything should be made as simple as possible, but not
simpler." That is, a model of a working system must be a working system. A
model of B(0) that "explains", but does not work, does not explain either.

#### 0.5.6  In the General Case, The External System (W,D) Has No Formal
Representation

Let us return to the cognitive system (W,D,B(0)) discussed in Section 0.3.
Though the models of B(0) can be and must be represented explicitly, in the
general case, the external system (W,D) has no finite representation.
Therefore, there is a good excuse for having informal theories of behavior of
system (W,D,B(0)), more so, system (W,D,B(t)).

**REMARK.** There are informal theories and informal theories. A good informal
theory should be associated with a formal model of B(0) (or B(t)). Given an
explicit model of B(0), all predictions of such an informal cognitive theory
can be verified experimentally (at least, in principle), since devices, D,
have a finite representation and the "informal" external world, W, is "always
there" to experiment with. Simply playing with words and trying to define one
set of vague verbal concepts through another set of equally vague verbal
concepts doesn't decrease the total level of vagueness.

It is interesting to mention that to reverse engineer the main principles of
organization and functioning of B(0), it may be sufficient to deal with rather
simple models of (W,D). Such models can often be described explicitly and used
in computer simulation. The program EROBOT.EXE (see www.brain0.com)
illustrates this methodology.

#### 0.5.7  On Engineering Expertise and Physical Mental Set

Reverse engineering B(0) requires an unusual combination of the knowledge base
of a system engineer and the mental set of a physicist. The reason for this
requirement can be explained as follows.

  * First of all, B(0) is a real complex information processing system. Reverse engineering such a system requires a broad system engineering expertise.
  * Second of all, B(0) is a system designed by Mother Nature (not by human system engineers). Deciphering such a natural system requires a "physical" (rather than "engineering") mentality. 

_   Why is traditional engineering mentality inadequate for reverse
engineering B(0)?_

Evolution uses design principles quite different from those employed by system
engineers. We try to make our systems more understandable and testable. This
costs us additional resources. Evolution tends to solve its problems with
minimum resources. This makes its designs look clever. This also makes them
difficult (for a human system engineer) to understand. One needs a "physical"
mental set, to crack such designs. Section 0.6 explains why.

#### 0.5.8  Asking the Right Questions

To make a progress in reverse engineering B(0) via the metaphorical loop of
Section 0.5.2, one needs to ask the right questions at **Step 1** of this
loop. Formulating the right questions is not a trivial task. Quite often,
finding the right question is even more important than finding the right
answer to this question.  
  
One of the strong points of the loop of section 0.5.2 is that it helps one to
formulate the right questions. If the iterative process 1-2-3-1... goes in the
right direction (is "converging"), the current approximation, Bi(0), generates
a system of concepts that can be efficiently used to formulate questions
needed for the synthesis of the next approximation Bi+1(0).

### 0.6  Methodological Pitfalls

  * _What can go wrong if a brain modeler or a cognitive modeler ignores the "physical" methodological principles (the "five commandments") from section 0.5.1?_

The following subsections attempt to give an answer to this question.
According to the Murphy's law, if something can go wrong it will.

####  0.6.1  Redefining a "Physical" Problem

Referring to this pitfall, Zopf, Jr. (1962) wrote: "I do hope that we shall
not fall into the trap for a time occupied by a friend of mine who, speaking
of a device he had built, said, in all seriousness, "If the conditional reflex
were only like this, then what I have built is a model of the conditional
reflex.""

#### 0.6.2  Concentrating on Efficiency and Ignoring Necessity

To obviate this pitfall, consider the following digging-for-a-treasure
metaphor. Imagine a crowd of diggers with sophisticated equipment digging in
wrong places and a person with a shovel digging in the right place.
(Everybody, except this person, knows that one should not dig in this place!)
In this (unlikely, but not impossible!) situation this single person would be
able to make more progress than the crowd. The point is that it doesn't matter
how efficiently one can dig if one is digging in a wrong place. In fact, the
more efficiency the more mess.  
Using this metaphor, one can say that to find the treasure (an adequate model
of B(0)) it is not sufficient to have efficient equipment and good working
conditions (soft soil, a lot of light, etc.) It is absolutely necessary to dig
in the right place, no matter how difficult the working conditions there might
be.

#### 0.6.3  Underestimating the Power of Basic Mechanisms

The example of physics warns us that one should not underestimate the power of
simple basic mechanisms of Mother Nature. I argue that this warning is
relevant to the problem of reverse engineering B(0).

Sometimes, an adequate formalization, extrapolation and integration of a set
of simple basic mechanisms produce a "critical mass" effect. The introduction
of the so-called "displacement current" in the Maxwell equations gives a
classical example of this interesting phenomenon. All of a sudden, this simple
addition to the set of known basic laws of electricity and magnetism, allowed
J.C. Maxwell to create his famous equations that cover the whole range of
arbitrarily complex classical electromagnetic phenomena.

I argue that the addition of E-states to the set of traditional mechanisms of
associative memory and learning is capable of producing a somewhat similar
"critical mass" effect. All of a sudden, it becomes possible to get a uniform
explanation of a broad range of psychological phenomena of working memory and
mental set. Quite remarkably, it also becomes possible to naturally connect
these "high level" psychological phenomena with a "very low level"
neurobiological data about the properties of protein molecules. (There is
something here to think about!)

#### 0.6.4  Looking for the Best Solution among Wrong Solutions

Optimization is a very important word in engineering. In this competitive
world, one needs to have a better product than the competition to be able to
sell this product. So one needs to optimize, optimize and optimize. This
optimization mentality is naturally transferred to brain modeling. A lot of
time is spent in discussions as to why a certain neural network works better
than other neural networks and why a certain AI algorithm displays a better
performance than other AI algorithms. (Try to sell a brain modeling idea, and
you are immediately asked to prove that your idea can solve a certain
engineering problem better than other known "brain inspired" ideas.)

Several years ago, I had a privilege to work on a government sponsored ANN
project with a team of prominent researchers (Prof. B. Widrow, Dr. M.E. Hoff
and Dr. M. Gluck). Our goal was to design a system for the recognition of a
thousand or more trajectories of ballistic objects by analyzing several frames
that contained positions of the objects at different time moments. We got
better than 90% recognition rate, whereas a previous team got less than 80%.
Since this was a brain-inspired engineering project (not a brain modeling
project!) we could say that our "neural network" was better than their "neural
network."

Unfortunately, such a simple engineering criterion of quality leads one into a
pitfall when applied to the problem of reverse engineering the brain.
Consider, for example, the popular problem of pattern recognition. There are
many different ANN models and AI algorithms that compete for the title of the
best pattern classifier. Such systems learn from examples and seem to provide
good metaphors for understanding the process of pattern recognition in the
brain.

  * _Should the best classifier also win the title of the best brain modeling metaphor for pattern recognition?_

The situation is not so simple. I argue that the whole class of models that
learn to perform optimal pattern classification is largely irrelevant to the
problem of pattern recognition in the brain. The trouble is that the human
pattern recognition is context dependent.

Consider the question: _"What is this?"_ In the context created by this
question a person will behave as a pattern classifier. He/she may answer, for
example, that this is a book. His/her brain was able to distinguish a book
from other objects, say, a box, a hard disk drive, etc. Now consider the
instruction: _"take this."_ In this context, it is no longer important that
"this" is a book. What is important is the object's size, weight, etc. The
experience that the brain acquired by learning to take a book is applicable to
the situation when one needs to take a box or a disk drive. In other words,
the same object can be treated as a member of different classes depending on
context.

Zopf, Jr. (1962) had emphasized the critical importance of this issue.
Optimizing performance in one context may completely destroy performance in a
large number of other contexts.

#### 0.6.5  "Pure" Phenomenology

Imagine a physicist who wants to simulate the behavior of electromagnetic
field in a complex microwave device, say, the Stanford Linear Accelerator
(SLAC). Assume that this physicist doesn't know about the existence of the
Maxwell equations and, even more importantly, doesn't believe that the complex
behavior he observes may have something to do with such simple equations. (In
the AI jargon this physicist would be called a "scruffy." If he believed in
the existence of the basic equations he would be called a "neat.").

So this "scruffy physicist" sets out to do a purely phenomenological computer
simulation of the observed complex behavior per se. Anyone who has been
involved in a computer simulation of the behavior of electromagnetic field in
a linear accelerator can easily predict the results of this gedanken
experiment. (I spent a few years doing such a simulation as a computational
physicist at the medical division of Varian Associates.)

In the best case scenario, the above mentioned scruffy physicist comes up with
a computer program (with a large number of empirical parameters) that would be
able to simulate the behavior of electromagnetic field in a very narrow range.
This computer program would have no extrapolating power  and would not be
accepted by the SLAC community as a theory of a linear accelerator.

Note that it would be impossible to reverse engineer the Maxwell equations (a
metaphorical counterpart of B(0)) from the analysis of the behavior of
electromagnetic field in such a complex "external world" as SLAC. I argue
that, similarly, it is impossible to reverse engineer B(0) from the analysis
of such complex cognitive phenomena in system (W,D,B(t)) as playing chess,
solving complex mathematical problems, story telling, etc. No wonder AI got
into trouble with the "physical" problem of the human brain and human
intelligence.

#### 0.6.6  "Brainless" Theories of Language

I argue that an adequate information processing (computational) theory of
language can only be derived from an adequate computational model of B(0). It
takes a lot of time (t > 1year) for the "language-ready" B(0) to change into a
B(t) that has some rudimentary language. According to Proposition 2 from
Section 0.3, B(t) has a much more complex representation than B(0). To
understand how B(t) uses language one needs to understand the process of
learning that transforms B(0) into B(t). The metaphor the brain as an
E-machine offers some nontrivial insights into this problem. It suggests that

  * The grammar of a natural language can be learnt
  * There is no such thing as a representation of a grammar independent of the representation of many other activities of B(t)
  * Any sufficiently expressive "free" motor channel can be used to represent a natural language.

I argue that an attempt to artificially separate language from other human
activities leads one into the pitfall of a wrong dimensionality similar to the
attempt to separate the description of the behavior of electric field from the
description of the behavior of the whole electromagnetic field. This pitfall
of a wrong dimensionality can be formulated as the following "catch 22":  An
attempt to artificially reduce the dimensionality of a "physical" problem, to
simplify this problem, makes the problem more difficult.

#### 0.6.7  "Pure" Neurodynamics

A large number of publications have been devoted to the study of the so-called
emergent collective computational properties of distributed neural networks.
The mathematical attraction and challenge of this research is to show how a
network of simple elements can produce sophisticated collective dynamical
effects. (This is a very interesting mathematical and, to some extent,
engineering problem.)

The trouble is, however, that the whole brain B(0) doesn't seem to make much
use of such collective dynamical computations. There is a growing
neurobiological evidence (that is supported at the information processing
level by this study) that the whole brain can do much better by relying on the
complexity of individual cells than on the above mentioned collective
neurodynamical effects. (See, for example, Changeux, 1993)

Neurodynamics is very important! However, an attempt to simulate
neurodynamical effects per se (that is, without connecting them with the
properties of the whole brain as a computing system) can hardly give much for
reverse engineering B(0).

#### 0.6.8  Inadequate "Physical" Formalism

One of the great intellectual achievements of the last century was the
discovery of universal languages. For example, any computable function can be
described in terms of any universal computing system, say, a universal Turing
machine.

This important mathematical result, taken out of its proper theoretical
context, and improperly applied to a "physical" problem, may lead one into a
pitfall. The catch is that not all mathematically equivalent formal
representations of a real "physical" system are equally useful for our brain.
Only a handful of such representations qualify as adequate "physical"
representations.

An adequate "physical" formalism uses variables and functions that make
"physical" sense. As a result of that, it generates a system of intuitive
concepts (a metaphorical language) that allows our brain to efficiently deal
with (mentally simulate) the "physical" system in question, and to understand
the implications of the formalism. In turn, an adequate metaphorical language
provides heuristic considerations for the development of an adequate
formalism. And so on.

It is easy to verify that these two critically important components (an
adequate formalism and an adequate system of intuitive concepts) are present
in any good science and any good engineering. To clearly see the pitfall
associated with an inadequate "physical" formalism, consider the following two
extreme (intentionally exaggerated) examples.

At one extreme, imagine a program for a universal Turing machine that
simulates the Maxwell equations (with some boundary conditions) with a great
accuracy (say, 128 bit). Ignoring the "practical" considerations of time and
efficiency, this program would, eventually, produce correct simulation
results. This "correct" representation, however, would not qualify as an
adequate "physical" formalism because it would not generate an adequate
metaphorical language. Accordingly, our brain would not be able to deal with
this representation.

At another extreme, imagine a system of millions of nonlinear differential
equations (with some initial conditions) describing the "low level" dynamics
of the circuitry of a personal computer running a complex piece of software,
say, the Microsoft Office. The main problem here is not in the differential
equations themselves (which, in fact, would not be too difficult to describe),
but in their initial conditions which, in this example, represent the
Microsoft Office. The same set of differential equations with different
initial conditions would represent Linux and any other possible computer
program. This "correct" representation, however, would not qualify as an
adequate "physical" formalism, because our brain would be unable to
efficiently deal with such a representation.

#### 0.6.9  Confusing the Problem of Reverse Engineering the Human Brain with
the Problem of Understanding the Human Mind

I want to emphasize that the problem of reverse engineering B(0) is quite
different from the problem of understanding the behavior of system (W,D,B(0))
or, even more so, system (W,D,B(t)) with a large t. The former problem is
complex, but finite (and solvable). The latter problem is infinite. Given an
adequate model of B(0) we will always be able to improve our understanding of
the behavior of (W,D,B(t)), with bigger and bigger t, but will never be able
to say that we have reached a "complete" understanding.

It is important to emphasize that the human mind and human intelligence are
not the properties of the human brain alone, but the properties of the whole
system (W,D,B(t)), where the external world W includes other people. We are
all parts of the same giant system (People,World), and we cannot understand
ourselves without understanding the whole system. While the generations of
people come and go, our world becomes more and more complex. New brains B(0)
are exposed to this more complex world and become more complex systems B(t)
which makes our world even more complex. And so on. The whole system
(W,D,B(t)) is developing, not just the brain.

The mystery of the human brain can be eventually solved, but the mystery of
the human mind will remain forever. I feel good about it! The last thing we
want is to completely understand ourselves. Fortunately, this is impossible,
in principle. Hopefully, by reverse engineering B(0) we will learn how to
better use and educate our brain and how to cure it.

Of course, we can also learn how to build intelligent robots, but I don't
worry about that right now. If we learn how to use our brains, we will figure
out how to deal with robots. We should realize, however, that if we ever
create really intelligent robots (which is possible in principle), we will
create a mystery of robot's mind. It is the "physical" world W where the main
mystery is. A robot will become intelligent in the human sense, only if it is
exposed to the same rich and mysterious world W as we are.

**Note:** It is interesting to mention that people who limit their exposure to
the rich external world (like some fanatics do) do not become intelligent
people. Their brains do not develop in a right way, and this problem is
difficult to fix at a later time. I argue that the human LTM is pretty much a
one-time-programmable memory, so you don't want to put a wrong "BIOS" in this
memory. (This "BIOS" is formed at a very young age, and, unfortunately, not
many people pay enough attention to this critically important problem.)

#### 0.6.10  Creating a Jigsaw Puzzle

Imagine a round cardboard cut into many intricate pieces to create a jigsaw
puzzle. The shape of each piece can be quite difficult to describe. However,
assembling these pieces together in a right way produces the shape that is
easy to describe.

I argue that this metaphor is relevant to brain modeling and cognitive
modeling. Due to many different reasons, the problem of the whole brain as a
complex computing system is divided (rather artificially) into many intricate
pieces. Researchers dealing with these separate pieces encounter many complex
issues that often have more to do with how the problem is cut into pieces,
than with the complexity of the brain itself. Assemble these pieces together
in a right way, and a simpler and more meaningful picture appears. The
artificially created issues become non-issues.

Concentrating on parts per se (especially inadequate parts), it is easy to
lose the big picture. When one is too preoccupied with the trees, one can't
see the forest for the trees.

### 0.7  On Brain Hardware, Brain Software, and the Algorithms of Thinking

Through the history of brain modeling and cognitive modeling, this topic has
been a subject of a heated debate between AI and ANN researchers. Let us
forget for a while about the all important issue of "physical" vs.
"mathematical" mentality and compare the strong and the week points of AI and
ANN from a system engineering viewpoint.

AI has concentrated on the problem of complex algorithms underlying human
thinking. It proposed that the problem of the algorithms of thinking per se
can be (and should be) separated from the problem of brain hardware. AI
methodologists used the following reasoning.

Imagine a system engineer trying to understand the work of a complex computer
with sophisticated software by studying the wiring diagram of this computer
and the transient processes in its gates and flip-flops. A brain researcher
trying to understand the work of the brain by studying its neural circuitry is
trapped in a similar methodological pitfall. This type of reasoning has
practically killed all brain modeling research in the seventies. (The time
known as the "Dark Ages" of brain modeling.)

This metaphor has a strong point and a weak point. Its strong point is that it
emphasizes a critical importance of brain software (whatever representation
such a software may have in the brain's memory). Its weak point is in
suggesting that the general relationship between brain hardware and the
complex computations underlying mental processes (thinking) is similar to that
in a conventional (von Neumann) computer. This part of the metaphor is
misleading.

The brain is a slow and massively parallel computer. From the basic timing
considerations one can conclude that some interesting algorithms of thinking
require only a few of the massively parallel computational "steps" performed
by brain hardware. (Feldman's 100-step principle.) Traditional AI algorithms
are quite long and violate this principle. Such algorithms cannot be performed
by a brain-like hardware.

The traditional neural network research has concentrated on the problem of
brain hardware. It's gone to another extreme and dismissed the whole idea of
algorithms of thinking and brain software. It assumed that, somehow, the
distributed modifiable connections can do the job. That is, one doesn't need
to understand how these distributed sets of connections work. One just needs
to figure out the right weight modification (learning) procedure and
everything will happen automatically. Let us do experiments and the miracle
will happen. (The good old Perceptron mentality.)

It should be mentioned, that this approach does work in many practically
interesting cases, so small miracles do happen. However, a big miracle is not
going to happen. The spoiler is the general level of computing power. The
popular feedforward neural networks have the general level of computing power
similar to that of combinatorial machines. (The analog vs. digital distinction
is of no principal importance at this level of generality.) With feedback,
such systems can reach the general level of computing power of state-machines
(Chomsky type 3).

To go above type 3, one needs a working memory, and the problem of working
memory is a stumbling block for the connectionist approach. A system with a
lower general level of computing power cannot simulate the work of a system
with a higher level of computing power. This is a fundamental restriction that
cannot be defeated by a smart design. (As mentioned in section 0.1, the human
brain has the highest general level of computing power (Turing machines or
Chomsky type 0).

**REMARK.** An attempt to simulate the work of the human brain using a
computational model that has a level of computing power lower than the brain
resembles an attempt to design a Perpetual Motion machine in violation of the
energy conservation law. It doesn't matter how smart a learning algorithm is.
A system cannot learn to do, what it cannot do in principle.

Let us summarize the results of this system engineering discussion:

  * Traditional AI has concentrated on the problem of the algorithms of thinking and ignored the problem of brain hardware. It developed models of the algorithms of thinking that cannot be implemented in brain hardware.
  * Traditional neural network research has concentrated on the problem of brain hardware and ignored the problem of the algorithms of thinking. It developed models of brain hardware that don't have enough computing power to perform nontrivial algorithms of thinking.

To avoid these pitfalls, a meaningful model of B(0) should satisfy the
following requirements:

  * Be implementable as a neurobiologically meaningful brain hardware.
  * Have enough computing power to perform psychologically meaningful algorithms of thinking.
  * Use a data storage procedure that would allow it to form almost all its software in the process of learning (starting with a relatively small initial "firmware").

### 0.8  The "Biological Grab Bag" Mentality Has Not Succeeded

I began this paper with the epigraph containing two quotations from George W.
Zopf, Jr.'s (1962) article entitled "Attitude and context". I assembled these
two quotations together, so they look like a single one. (I first read this
article in Russian translation in 1967. It had a considerable influence on my
general methodological mental set.)

Forty years has passed since this entertaining, but rather deep article was
presented at the Illinois Symposium on the Principles of Self-organization.
Nowadays, it is difficult to find people who have read this article. The truth
is, however, that Zopf, Jr. was right. It is becoming increasingly obvious to
any unbiased person that the "biological grab bag" mentality has not succeeded
in understanding the fundamental biological phenomenon of the human brain and
human intelligence.

Let us admit that Mother Nature is smarter than human engineers and
mathematicians, and let us try to understand how the real biological brain
works before making broader generalizations. Otherwise, we will keep producing
"glittering generalizations" that include everything but the brain.

It is appropriate to end this methodological discussion with another quotation
from the above mentioned article. Wrote Zopf, Jr.: "And for a bedtime story
tonight I suggest Hans Christian Andersen's "The Emperor's New Clothes."
Fellow emperors - and weavers - may we become as little children."

### 0.9  Summary

  * Like the magical mirror in the J.K. Rowling novel the brain shows everyone what one wants to see. Referring to this phenomenon, the neurophysiologist Burns (1958) wrote that (when one is dealing with the brain) "it is distressingly easy to find what one is looking for and remarkably difficult to discern the unsuspected or the unwanted." (Section 0.1.) 
  
  

  * The methodology of "partial" brain modeling and "partial" cognitive modeling has failed to address the most fundamental question associated with the whole human brain as a computing system: _"How does the whole brain learn to perform mental computations?"_ This approach ignores the basic requirements of the whole brain as a complex computing system and leads one into the pitfall of the "parts that don't fit the whole." (Section 0.2.) 
  
  

  * The fact that a person with a good visual memory can learn to perform, in principle, any mental computations means that the whole human brain is a universal learning computing system. That is, the popular belief that universal learning systems don't exist is a myth. This myth is a result of an inadequate "definition" of the concept of learning that does not include the case of human learning. (Section 0.2.) 
  
  

  * To understand the brain, one should view it as a part of a cognitive system (Man,World). Let (W,D,B) be a model of this system, where W is an external world, D is the set of man-like sensory and motor devices, and B is a computing system simulating the work of man's nervous system. For the sake of simplicity, B is referred to as a model of the brain or, simply the brain. Let B(t) be a formal representation of B at the time t, where t=0 correspond to the "untrained" ("unprogrammed") brain, B(0). (Section 0.3. ) 
  
  

  * It is convenient to view system (W,D,B) as a composition of two subsystems: (W,D) and B, where (W,D) is the external world as it appears to the brain B via the set of devices D. System B has a finite formal representation. In the general case, system (W,D) doesn't have a finite formal representation. However, the external world W is "always there" to experiment with, so, given a model of B, and a model of D, one can simulate the whole system. (Section 0.3.) 
  
  

  * It is possible to find a relatively small (not too small) formal representation of B(0). This representation may fit into a single floppy disk. (Section 0.3.) 
  
  

  * Any formal representation of B(t) with a big t (say t> 10 years) must be very big. It is practically impossible to reverse engineer B(t) without first reverse engineering B(0). (Section 0.3.) 
  
  

  * It is practically impossible to simulate some nontrivial parts of the behavior of system (W,D,B(t)) without having an adequate formal representation of B(t). All purely phenomenological ("brainless") computational theories of cognitive phenomena fell pray to this pitfall. (Section 0.3 and Section 0.6.) 
  
  

  * The main goal of brain modeling should be reverse engineering B(0). The main goal of cognitive modeling should be understanding how B(0) changes into different B(t)'s, with bigger and bigger t, as a result of interaction with different external systems (W,D). (Section 0.3.) 
  
  

  * To reverse engineer B(0) one should invent a "supercritical" initial approximation for B(0) and use iterative reverse engineering strategy described in Section 0.5.
  
  

  * The metaphor the brain as an E-machine discussed in this study is an attempt to introduce a "supercritical" initial approximation for B(0) that can be efficiently used in the above mentioned reverse engineering process. (Section 0.4.) 
  
  

  * The main goal of this study is to initiate a project aimed at reverse engineering the structure of a complex E-machine that could serve as a computational model of B(0). This project is referred to as the Brain 0 project. (Section 0.5.) 
  
  

  * Traditional AI research has concentrated on the problem of the "algorithms of thinking," but ignored the problem of "brain hardware." It developed models of the algorithms of thinking that can not be performed by a brainlike hardware. (Section 0.7.) 
  
  

  * Traditional ANN research has concentrated on the problem of brain hardware, but ignored the problem of the algorithms of thinking. It developed models of brain hardware that don't have enough computing power to perform nontrivial algorithms of thinking. (Section 0.7.) 
  
  
To avoid these pitfalls a model of B(0) must

    * be implementable as a neurobiologically meaningful brain hardware 
    * have enough computing power to perform psychologically meaningful algorithms of thinking 
    * be able to create the main part (almost all) its software in the course of learning (starting with a relatively small initial "firmware") 

### References

Anderson, J.R. (1976). Language, Memory, and Thought. Hillsdale, New Jersey:
Lawrence Erlbaum Associates, Publishers.  
  
Baddeley, A.D. (1982). Your memory. A user's guide. Macmilan Publishing Co.,
Inc.  
  
Burns, B.D., (1958). The Mamalian Cerebral Cortex. Arnold.  
  
Changeux, J.P. (1993). Chemical Signaling in the Brain. Scientific American,
Novemeber, 58-62.  
  
Chomsky, N. (1956). Three models for the description of language. _I.R.E.
Transactions on Information Theory._ JT-2, 113-124.  
  
Collins, A.M., & Quillian, M.R., (1972). How to make a language user. _In E.
Tulving & W. Donaldson (Eds.) Organization and memory._ New York: Academic
Press.  
  
Eliashberg, V. (1967). On a class of learning machines. _Proceedings of the
Conference on Automation in the Pulp & Paper industry, April 1967, Leningrad
USSR. Proc of VNIIB, #54,_ 350-398. (in Russian)  
  
Eliashberg, V. (1979). The concept of E-machine and the problem of context-
dependent behavior. Txu 40-320, US Copyright Office.  
  
Eliashberg, V. (1981). The concept of E-machine: On brain hardware and the
algorithms of thinking. _Proceedings of the Third Annual Meeting of the
Cognitive Science Society,_ 289-291.  
  
Eliashberg, V. (1982). The states of residual excitation in neural networks as
the mechanism of short-term memory and mental set. Abstract. _Neuroscience,_
Supplement to volume 7, p. S63.  
  
Eliashberg, V. (1988a). Neuron layer with reciprocal inhibition as a mechanism
of random choice. _Proceedings of the IEEE ICNN 88._  
  
Eliashberg, V. (1988b). The E-machines: Associative neural networks as
nonclassical symbolic processors. Abstract, _The First Annual Meeting of
INNS._  
  
Eliashberg, V. (1989). Context-sensitive associative memory: "Residual
excitation" in neural networks as the mechanism of STM and mental set.
_Proceedings of IJCNN-89, June 18-22, 1989, Washington, D.C._ vol. I, 67-75.  
  
Eliashberg, V. (1990a). Molecular dynamics of short-term memory. _Mathematical
and Computer modeling in Science and Technology._ vol. 14, 295-299.  
  
Eliashberg, V. (1990b). Universal learning neurocomputer. _Proceeding of the
Fourth Annual parallel processing symposium. California state university,
Fullerton. April 4-6, 1990._ , 181-191.  
  
Eliashberg, V. (1993). A relationship between neural networks and programmable
logic arrays. 0-7803-0999-5/93, IEEE, 1333-1337.  
  
Rosenblatt, F. (1962). Principles of neurodynamics. Washington D.C.: Spartan
Books.  
  
Turing, A.M. (1936). On computable numbers, with an application to the
Entscheidungsproblem. _Proc. London Math. Society,_ ser. 2, 42  
  
Vvedensky, N.E. (1901). Excitation, inhibition, and narcosis. _In Complete
collection of works._ USSR, 1953.  
  
Zopf, G.W., Jr. (1962). Attitude and Context. _In "Principles of Self-
organization",_ Pergamon Press, 325-346.  
  
  

### Answers to Questions from Section 0.1

**Answer to Question 1:**

All presidents who are alive. The word "buried" makes you think about dead
presidents. The particle  "not" is ignored.

**Answer to Question 2:**

A blind white horse. The word "see" prevents you from thinking about the
animals that cannot see at all.

**Answer to Question 3:**

The speed=0. The dog should sit quiet. The words "run" and "fast" create a
misleading mental set. You imagine a supersonic dog crossing the sound
barrier.

**Answer to Question 4:**

Put one penny in each wallet, and put one wallet inside the other. The idea of
"dividing money" makes it difficult to think of this solution.

