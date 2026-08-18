---
title: "13. Thermodynamics"
short_title: "Chapter 13"
label: ch-13
---

(sec-13.1)=
## 13.1 Introduction

The last two lectures this semester are about thermodynamics, an extremely important branch of physics that developed throughout the 19th century, motivated in part by the development of the steam engines that brought about the Industrial Revolution. Physics majors will study thermodynamics at much greater length in University Physics III and subsequent courses, whereas Engineering and Chemistry majors will encounter it also in specialized courses in their own disciplines.

There is really no escaping thermodynamics, but you may wonder why bring it up here (in this course, at this time) at all? The answer is twofold:

- From the point of view of the study of energy and its transformations, which has been one of the major themes of this course, thermodynamics provides us with the last missing pieces: it is here that we find out what thermal energy really is, and how it is different from other forms of energy (so much so, that we say that energy has been \"dissipated\" or \"lost\" when it becomes thermal energy). It is also here that we deal with the other way that energy can be transferred from a system to another (other, that is, than by doing work): this is the \"direct transfer of thermal energy,\" or what is normally called an exchange of heat.

- From the point of view of the study of motion, which has been also another running theme, thermodynamics also represents the next logical step beyond what we have learned so far. Recall that we started looking at the motion of extended objects as if they were simple point particles, moving as a whole along with their center of mass, and slowly introduced tools to deal with more complex kinds of motion: first rigid body rotations, then elastic deformations\
  (waves) in which the constituent parts of an object move relative to each other in a way that looks \"organized,\" or synchronized, from a macroscopic perspective. What is needed next is to account for the random motion, on a microscopic scale, of the smallest parts (atoms or molecules) that make up an extended object. This motion is constantly happening, and it is a key ingredient of the concepts of thermal energy and temperature.

Conceptually, thermodynamics involves the introduction of two new physical quantities, temperature and entropy. Temperature will be introduced in this lecture, and entropy in the next one. It is interesting to note from the start, however, that these are very different from all the quantities we have introduced so far this semester, in a fundamental way. In classical physics, at least, there is no difficulty in extending all those other quantities to the study of the smallest parts making up an object: we can perfectly well talk about the position, velocity or energy of a molecule. But temperature and entropy are statistical quantities, which are only properly defined, from a fundamental point of view, for a large collection of (small) subsystems: it makes no sense to speak about the temperature or the entropy of a single molecule. This shows that there was really a profound change in perspective and methodology in classical physics when statistical mechanics (the part of physics that provides a microscopic foundation for thermodynamics) was developed.

(sec-13.2)=
## 13.2 Introducing temperature

(sec-13.2.1)=
### 13.2.1 Temperature and heat capacity

The change in perspective that I just mentioned also means that it is not easy to even define temperature, beyond our natural intuition of \"hot\" and \"cold,\" or the somewhat circular notion that temperature is simply \"what thermometers measure.\" Roughly speaking, though, temperature is a measure of the amount (or, to be somewhat more precise, the concentration) of thermal energy in an object. When we directly put an amount of thermal energy, $\Delta E_{t h}$ (what we will be calling heat in a moment), in an object, we typically observe its temperature to increase in a way that is approximately proportional to $\Delta E_{t h}$, at least as long as $\Delta E_{t h}$ is not too large:

:::{math}
:label: eq-13.1
\Delta T=\frac{\Delta E_{t h}}{C}
:::

The proportionality constant $C$ is called the heat capacity of the object: according to {numref}`Eq. %s <eq-13.1>`, a system with a large heat capacity could absorb (or give off - the equation is supposed to apply in either case) a large amount of thermal energy without experiencing a large change in temperature. If the system does not do any work in the process (recall {numref}`Eq. %s <eq-7.20>`!), then its internal energy will increase (or decrease) by exactly the same amount of thermal energy it has taken in (or given off) ${ }^{1}$,

and we can use the heat capacity ${ }^{2}$ to, ultimately, relate the system's temperature to its energy content in a one-to-one-way.

What is found experimentally is that the heat capacity of a homogeneous object (that is, one made of just one substance) is, in general, proportional to its mass. This is why, instead of tables of heat capacities, what we compile are tables of specific heats, which are heat capacities per kilogram (or sometimes per mole, or per cubic centimeter\... but all these things are ultimately proportional to the object's mass). In terms of a specific heat $c=C / m$, and again assuming no work done or by the system, we can rewrite {numref}`Eq. %s <eq-13.1>` to read

:::{math}
:label: eq-13.2
\Delta E_{\text {sys }}=m c \Delta T
:::

or, again,

:::{math}
:label: eq-13.3
\Delta T=\frac{\Delta E_{s y s}}{m c}
:::

which shows what I said above, that temperature really measures, not the total energy content of an object, but its concentration - the thermal energy \"per unit mass,\" or, if you prefer (and somewhat more fundamentally) \"per molecule.\" An object can have a great deal of thermal energy just by virtue of being huge, and yet still be pretty cold (water in the ocean is a good example).

In fact, we can also rewrite Eqs. (13.1-13.3) in the (somewhat contrived-looking) form

:::{math}
:label: eq-13.4
C=m c=m \frac{\Delta E_{s y s} / m}{\Delta T}
:::

which tells you that an object can have a large heat capacity in two ways: one is simply to have a lot of mass, and the other is to have a large specific heat. The first of these ways is kind of boring (but potentially useful, as I will discuss below); the second is interesting, because it means that a relatively large change in the internal energy per molecule (roughly speaking, the numerator of {eq}`eq-13.4`) will only show as a relatively small change in temperature (the denominator of {eq}`eq-13.4`; a large numerator and a small denominator make for a large fraction!).

Put differently, and somewhat fancifully, substances with a large specific heat are very good at hiding their thermal energy from thermometers (see {numref}`Fig. %s <fig-13.1>` for an example). This, as I said, is an interesting observation, but it also means that measuring heat capacities - or, for that matter, measuring temperature itself-may not be an easy matter. How do we get at the object's internal energy if not through its temperature? Where does one start?

:::{figure} ../images/2024_09_14_9969b06773f10b6936e8g-324.jpg
:label: fig-13.1
In this simple model of a gas of diatomic molecules, each molecule can store \"vibrational\" potential energy (both potential and kinetic, through the oscillations of the \"spring\" that models the interaction between the atoms), plus as at least two kinds of rotational kinetic energy (corresponding to rotations around the axes shown), in addition to just the translational kinetic energy of its center of mass. The latter is the only one directly measured by a gas thermometer, so a diatomic gas has many more ways of \"hiding\" its thermal energy (and hence, a larger specific heat) than a monoatomic gas.
:::

(sec-13.2.2)=
### 13.2.2 The gas thermometer

A good start, at least conceptually, is provided by looking at a system that has no place to hide its thermal energy - it has to show it all, have it, as it were, in full view all the time. Such a system is what has come to be known as an ideal gas - which we model, microscopically, as a collection of molecules (or, more properly, atoms) with no dimension and no structure: just pointlike things whizzing about and continually banging into each other and against the walls of their container. For such a system the only possible kind of internal energy is the sum of the molecules' translational kinetic energy. We may expect this to be easily detected by a thermometer (or any other energysensitive probe), because as the gas molecules bang against the thermometer, they will indirectly reveal the energy they carry, both by how often and how hard they collide.

As it turns out, we can be a lot more precise than that. We can analyze the theoretical model of an ideal gas that we have just described fairly easily, using nothing but the concepts we have introduced earlier in the semester (plus a few simple statistical ideas) and obtain the following result for the gas' pressure and volume:

:::{math}
:label: eq-13.5
P V=\frac{2}{3} N\left\langle K_{\text {trans }}\right\rangle
:::

where $N$ is the total number of molecules, and $\left\langle K_{\text {trans }}\right\rangle$ is the average translational kinetic energy per molecule. Now, you are very likely to have seen, in high-school chemistry, the experimentally derived \"ideal gas law,\"

:::{math}
:label: eq-13.6
P V=n R T
:::

where $n$ is the number of moles, and $R$ the \"ideal gas constant.\" Comparing {numref}`Eq. %s <eq-13.5>` (a theoretical prediction for a mathematical model) and {numref}`Eq. %s <eq-13.6>` (an empirical result approximately valid for\
many real-world gases under a wide range of pressure and temperature, where \"temperature\" literally means simply \"what any good thermometer would measure\") immediately tells us what temperature is, at least for this extremely simple system: it is just a measure of the average (translational) kinetic energy per molecule.

It would be tempting to leave it at that, and immediately generalize the result to all kinds of other systems. After all, presumably, a thermometer inserted in a liquid is fundamentally responding to the same thing as a thermometer inserted in an ideal gas: namely, to how often, and how hard, the liquid's molecules bang against the thermometer's wall. So we can assume that, in fact, it must be measuring the same thing in both cases - and that would be the average translational kinetic energy per molecule. Indeed, there is a result in classical statistical mechanics that states that for any system (liquid, solid, or gas) in \"thermal equilibrium\" (a state that I will define more precisely later), the average translational kinetic energy per molecule must be

:::{math}
:label: eq-13.7
\left\langle K_{\text {trans }}\right\rangle=\frac{3}{2} k_{B} T
:::

where $k_{B}$ is a constant called Boltzmann's constant ( $k_{B}=1.38 \times 10^{-23} \mathrm{~J} / \mathrm{K}$ ), and $T$, as in {numref}`Eq. %s <eq-13.6>` is measured in degrees Kelvin.

There is nothing wrong with this way to think about temperature, except that it is too selflimiting. To simply identify temperature with the translational kinetic energy per molecule leaves out a lot of other possible kinds of energy that a complex system might have (a sufficiently complex molecule may also rotate and vibrate, for instance, as shown in {numref}`Fig. %s <fig-13.1>`; these are some of the ways the molecule can \"hide\" its energy from the thermometer, as I suggested above). Typically, all those other forms of internal energy also go up as the temperature increases, so it would be at least a bit misleading to think of the temperature as having to do with only $K_{\text {trans }}$, {numref}`Eq. %s <eq-13.7>` notwithstanding. Ultimately, in fact, it is the total internal energy of the system that we want to relate to the temperature, which means having to deal with those pesky specific heats I introduced in the previous section. (As an aside, the calculation of specific heats was one of the great challenges to the theoretical physicists of the late 19th and early 20th century, and eventually led to the introduction of quantum mechanics - but that is another story!)

In any case, the ideal gas not only provides us with an insight into the microscopic picture behind the concept of temperature, it may also serve as a thermometer itself. {numref}`Equation %s <eq-13.6>` shows that the volume of an ideal gas held at constant pressure will increase in a way that's directly proportional to the temperature. This is just how a conventional, old-fashioned mercury thermometer worked-as the temperature rose, the volume of the liquid in the tube went up. The ideal gas thermometer is a bit more cumbersome (a relatively small temperature change may cause a pretty large change in volume), but, as I stated earlier, typically works well over a very large temperature range.

By using an ideal (or nearly ideal) gas as a thermometer, based on {numref}`Eq. %s <eq-13.6>`, we are, in fact, implicitly defining a specific temperature scale, the Kelvin scale (indeed, you may recall that for

{numref}`Eq. %s <eq-13.6>` to work, the temperature must be measured in degrees Kelvin). The zero point of that scale (what we call absolute zero) is the theoretical point at which an ideal gas would shrink to precisely zero volume. Of course, no gas stays ideal (or even gaseous!) at such low temperatures, but the point can easily be found by extrapolation: for instance, imagine plotting experimental values of $V$ vs $T$, at constant pressure, for a nearly ideal gas, using any kind of thermometer scale to measure $T$, over a wide range of temperatures. Then, connect the points by a straight line, and extend the line to where it crosses the $T$ axis (so $V=0$ ); that point gives you the value of absolute zero in the scale you were using, such as -273.15 Celsius, for instance, or -459.67 Fahrenheit.

:::{figure} ../images/2024_09_14_9969b06773f10b6936e8g-326.jpg
:label: fig-13.2
Illustrating how a gas thermometer can be used to define the Kelvin, or absolute, temperature scale.
:::

The connection between Kelvin (or absolute) temperature and microscopic motion expressed by equations like {eq}`eq-13.5` through {eq}`eq-13.7` immediately tells us that as you lower the temperature the atoms in your system will move more and more slowly, until, when you reach absolute zero, all microscopic motion would cease. This does not quite happen, because of quantum mechanics, and we also believe that it is impossible to really reach absolute zero for other reasons, but it is true to a very good approximation, and experimentalists have recently become very good at cooling small ensembles of atoms to temperatures extremely close to absolute zero, where the atoms move, literally, slower than snails (instead of whizzing by at close to the speed of sound, as the air molecules do at room temperature).

(sec-13.2.3)=
### 13.2.3 The zero-th law

Historically, thermometers became useful because they gave us a way to quantify our natural perception of cold and hot, but the quantity they measure, temperature, would have been pretty useless if it had not exhibited an important property, which we naturally take for granted, but which is, in fact, surprisingly not trivial. This property, which often goes by the name of the zero-th law of thermodynamics, can be stated as follows:

Suppose you place two systems $A$ and $B$ in contact, so they can directly exchange thermal energy (more about this in the next section), while isolating them from the rest of the world (so their joint\
thermal energy has no other place to go). Then, eventually, they will reach a state, called thermal equilibrium, in which they will both have the same temperature.

This is important for many reasons, not the least of which being that that is what allows us to measure temperature with a thermometer in the first place: the thermometer tells us the temperature of the object with which we place it in contact, by first adopting itself that temperature! Of course, a good thermometer has to be designed so that it will do that while changing the temperature of the system being measured as little as possible; that is to say, the thermometer has to have a much smaller heat capacity than the system it is measuring, so that it only needs to give or take a very small amount of thermal energy in order to match its temperature. But the main point here is that the match actually happens, and when it does, the temperature measured by the thermometer will be the same for any other systems that are, in turn, in thermal equilibrium with - that is, at the same temperature as-the first one.

The zero-th law only assures us that thermal equilibrium will eventually happen, that is, the two systems will eventually reach one and the same temperature; it does not tell us how long this may take, nor even, by itself, what that final temperature will be. The latter point, however, can be easily determined if you make use of conservation of energy (the first law, coming up!) and the concept of heat capacity introduced above (think about it for a minute).

Still, as I said above, this result is far from trivial. Just imagine, for instance, two different ideal gases, whose molecules have different masses, that you bring to a state of joint thermal equilibrium. Equations {eq}`eq-13.5` through {eq}`eq-13.7` tell us that in this final state the average translational kinetic energy of the \" $A$ \" molecules and the \" $B$ \" molecules will be the same. This means, in particular, that the more massive molecules will end up moving more slowly, on average, so $m_{a} v_{a, a v}^{2}=m_{b} v_{b, a v}^{2}$. But why is that? Why should it be the kinetic energies that end up matching, on average, and not, say, the momenta, or the molecular speeds themselves? The result, though undoubtedly true, defied a rigorous mathematical proof for decades, if not centuries; I am not sure that a rigorous proof exists, even now.

(sec-13.3)=
## 13.3 Heat and the first law

(sec-13.3.1)=
### 13.3.1 \"Direct exchange of thermal energy\" and early theories of heat

In the previous section I have considered the possibility of \"direct exchange of thermal energy\" between two objects. This is a phenomenon with which we are all familiar: when a colder object is placed in contact with a warmer one, the warmer one cools off and the colder one warms up. This \"warmth\" that seems to flow out of one object and into the other is conventionally called \"heat.\"

Naturally, this observation was made long before the concept of \"energy\" was even developed, and so heat was thought of, for a time, as an \"invisible fluid\" (called, at one point, \"caloric fluid\"), a sort of indestructible \"substance\" that literally passed from one body to another. By \"indestructible\" I mean that they had a notion of this caloric fluid being conserved: it was not created or destroyed, only exchanged from one body to another. This makes sense, in a way: if it was really something material, how could it be created or destroyed? Conservation of matter was pretty much accepted scientific \"dogma\" already by the end of the 18th century.

This idea of conservation of the caloric fluid led to the whole field of \"calorimetry,\" as essentially a way to try to quantify (that is, measure) the amount of \"caloric\" that materials would take in or give off. The connection with temperature led directly to the definition of heat capacities and specific heats, just as I have introduced them above (in {ref}`section 2.1 <sec-2.1>`); only instead of \"change in energy\" you would use \"change in caloric content.\" This would be measured in units, called calories, defined by the amount of caloric that led to a given temperature change in a reference substance, such as water.

To be precise, let 1 calorie be the amount of \"caloric\" needed to raise the temperature of one gram of water by one degree Celsius at a pressure of one atmosphere. This makes the specific heat of water, by definition, 1 calorie/ ${ }^{\circ} \mathrm{C}$ $\cdot$gram. Now imagine you place a hot object in a container of water, insulated from the rest of the world, and wait until thermal equilibrium is reached. Then you can calculate the \"amount of caloric that flowed into the water,\" from the change in its temperature, and if you assume that all this came from the hot object then you can calculate its heat capacity (in calories $/{ }^{\circ} \mathrm{C}$ ) from the change in its temperature. By proceeding in this fashion, scientists developed tables of specific heats that do not need any change today-only the recognition that \"caloric\" is not really a fluid at all, but a form of energy, and can, therefore, be measured in energy units.

Clearly, conservation of caloric was a very good idea in its own way, since much of what was established back then still works if you simply replace the word \"caloric\" or \"heat\" by \"thermal energy.\" It was, however, ultimately unsatisfactory precisely because it restricted itself to what we would today recognize as just one kind of energy, and so it failed to recognize thermal energy as something that could be converted into, or from, other kinds of energy.

In hindsight, it is a bit surprising that the belief in the conservation of caloric could have held for so long. What today appear to us like obvious instances of the transformation of (macroscopic) mechanical energy into thermal energy, such as the warmth generated when you rub two objects together, were explained away as instances of mechanically \"squeezing\" caloric fluid out of the objects. Around the turn of the 19th century, an American expatriate, Count Rumford, observed one of the most egregious instances of this in the enormous amount of \"heat\" that was generated in the boring of cannons (which involved, basically, a huge metal tool drilling a hole in a large metal cylinder). He noticed that the total mass of the metal, including all the shavings, did not appear to change in the process, and concluded that caloric had to be virtually massless, since enormous quantities of it could be \"squeezed\" out without an appreciable mass loss. He speculated that\
caloric was not a fluid at all, but rather \"a form of motion,\" since only something like that could be made to increase without any apparent limit.

Rumford's theory was not generally accepted at the time, but later in the 19th century the direct conversion of mechanical energy into thermal energy was established beyond a doubt by James Prescott Joule in a series of painstaking experiments in which he used a system of weights to turn some vanes, or paddles, that stirred water in a container and eventually caused its temperature to rise. By measuring the mechanical energy deficit (gravitational plus kinetic) of his system of weights and paddles, he could tell how much energy the water must have gained, and by measuring the water's change in temperature he could then establish the equivalent \"amount of caloric\" that had gone into it. He thus established what was called \"the mechanical equivalent of heat,\" which we would express today by saying that a calorie does not measure the amount of some (nonexistent) caloric fluid, but simply an amount of energy equal to 4.18 joules (and yes, the Joule is named after him!).

(sec-13.3.2)=
### 13.3.2 The first law of thermodynamics

The upshot of all this experimentation was the full development of the concept of energy as a conserved quantity that manifested itself in different ways and could be \"converted\" among different kinds. To the observation, already familiar from macroscopic mechanics, that the energy of a system could be changed by doing work on it (or letting it do work on its environment) was added the observation, coming from thermal physics, that thermal energy could also be directly exchanged between two objects merely by placing them in contact, without any macroscopic work being involved. The two things taken together led to the principle of conservation of energy in its most general (pre-relativistic) form:

:::{math}
:label: eq-13.8
\Delta E=W+Q
:::

which says simply that a change in the total energy of a system may result from work $(W)$ or from \"heat exchange\" $(Q)$. \"Heat,\" in physics usage today, is simply what we call the thermal energy that is directly transferred from one object to another, typically by contact; the convention used for this term is the same as for the work term, that is, $Q$ is positive if thermal energy flows into the system and negative if thermal energy leaves the system.

{numref}`Equation %s <eq-13.8>` is the first law of thermodynamics. Note that, in terms of $Q$, the precise definition of a system's heat capacity is $C=Q / \Delta T$, and so this will only be equal to $\Delta E / \Delta t$ when the system does no work, which is why I was careful to include that condition in the derivation of {numref}`Eq. %s <eq-13.2>`.

(sec-13.4)=
## 13.4 The second law and entropy

The second law of thermodynamics is really little more than a formal statement of the observation that heat always flows spontaneously from a warmer to a colder object, and never in reverse.

More precisely, consider two systems, at different temperatures, that can exchange heat with each other but are otherwise isolated from the rest of the world. The second law states that under those conditions the heat will only flow from the warmer to the colder one.

The closure of the system - its isolation from any sources of energy-is important in the above statement. It is certainly possible to build devices that will remove heat from a relatively cold place (like the inside of your house on a hot summer day) and exhaust it to a warmer environment. These devices are called refrigerators or heat pumps, and the main thing about them is that they need to be plugged in to operate: that is, they require an external energy source.

If you have an energy source, then, you can move heat from a colder to a warmer object. To avoid unnecessary complications and loopholes (what if the energy source is a battery that is physically inside your \"closed\" system?) an alternative formulation of the basic principle, due to Clausius, goes as follows:

No process is possible whose sole result is the transfer of heat from a cooler to a hotter body\
The words \"sole result\" are meant to imply that in order to accomplish this \"unnatural\" transfer of heat you must draw energy from some source, and so you must be, in some way, depleting that source (the battery, for instance). On the other hand, for the reverse, \"spontaneous\" process-the flow from hotter to cooler-no such energy source is necessary.

A mathematical way to formulate the second law would be as follows. Consider two systems, in thermal equilibrium at temperatures $T_{1}$ and $T_{2}$, that you place in contact so they can exchange heat. For simplicity, assume that exchange of heat is all that happens; no work is done either by the systems or on them, and no heat is transferred to or from the outside world either. Then, if $Q_{1}$ and $Q_{2}$ are the amounts of heat gained by each system, we must have, by the conservation of energy, $Q_{2}=-Q_{1}$, so one of these is positive and the other one is negative, and, by the second law, the system with the positive $Q$ (the one that gains thermal energy) must be the colder one. This is ensured by the following inequality:

:::{math}
:label: eq-13.9
Q_{1}\left(T_{2}-T_{1}\right) \geq 0
:::

So, if $T_{2}>T_{1}, Q_{1}$ must be positive, and if $T_{1}>T_{2}, Q_{1}$ must be negative. (The equal sign is there to allow for the case in which $T_{1}=T_{2}$, in which case the two systems are initially in thermal equilibrium already, and no heat transfer takes place.)

{numref}`Equation %s <eq-13.9>` is valid regardless of the temperature scale. If we use the Kelvin scale, in which all the temperatures are positive ${ }^{3}$, we can rewrite it by dividing both sides by the product $T_{1} T_{2}$, and using $Q_{2}=-Q_{1}$, as

:::{math}
:label: eq-13.10
\frac{Q_{1}}{T_{1}}+\frac{Q_{2}}{T_{2}} \geq 0
:::

This more symmetric statement of the second law is a good starting point from which to introduce the concept of entropy, which I will proceed to do next.

(sec-13.4.1)=
### 13.4.1 Entropy

In Equations {eq}`eq-13.9` and {eq}`eq-13.10`, we have taken $T_{1}$ and $T_{2}$ to be the initial temperatures of the two systems, but in general, of course, these temperatures will change during the heat transfer process. It is useful to consider an \"infinitesimal\" heat transfer, $d Q$, so small that it leads to a negligible temperature change, and then define the change in the system's entropy by

:::{math}
:label: eq-13.11
d S=\frac{d Q}{T}
:::

Here, $S$ denotes a new system variable, the entropy, which is implicitly defined by {numref}`Eq. %s <eq-13.11>`. That is to say, suppose you take a system from one initial state to another by adding or removing a series of infinitesimal amounts of heat. We take the change in entropy over the whole process to be

:::{math}
:label: eq-13.12
\Delta S=S_{f}-S_{i}=\int_{i}^{f} \frac{d Q}{T}
:::

Starting from an arbitrary state, we could use this to find the entropy for any other state, at least up to a (probably) unimportant constant (a little like what happens with the energy: the absolute value of the energy does not typically matter, it is only the energy differences that are meaningful). This may be easier said than done, though; there is no a priori guarantee that any two arbitrary states of a system could be connected by a process for which {eq}`eq-13.12` could be calculated, and conversely, it might also happen that two states could be connected by several possible processes, and the integral in {eq}`eq-13.12` would have different values for all those. In other words, there is no guarantee that the entropy thus defined will be a true state function-something that is uniquely determined by the other variables that characterize a system's state in thermal equilibrium.

Nevertheless, it turns out that it is possible to show that the integral {eq}`eq-13.12` is indeed independent of the \"path\" connecting the initial and final states, at least as long as the physical processes considered are \"reversible\" (a constraint that basically amounts to the requirement that heat be exchanged, and work done, only in small increments at a time, so that the system never departs

too far from a state of thermal equilibrium). I will not attempt the proof here, but merely note that this provides the following, alternative formulation of the second law of thermodynamics:

For every system in thermal equilibrium, there is a state function, the entropy, with the property that it can never decrease for a closed system.

You can see how this covers the case considered in the previous section, of two objects, 1 and 2 , in thermal contact with each other but isolated from the rest of the world. If object 1 absorbs some heat $d Q_{1}$ while at temperature $T_{1}$ its change in entropy will be $d S_{1}=d Q_{1} / T_{1}$, and similarly for object 2 . The total change in the entropy of the closed system formed by the two objects will then be

:::{math}
:label: eq-13.13
d S_{\text {total }}=d S_{1}+d S_{2}=\frac{d Q_{1}}{T_{1}}+\frac{d Q_{2}}{T_{2}}
:::

and the requirement that this cannot be negative (that is, $S_{\text {total }}$ must not decrease) is just the same as {numref}`Eq. %s <eq-13.10>`, in differential form.

Once again, this simply means that the hotter object gives off the heat and the colder one absorbs it, but when you look at it in terms of entropy it is a bit more interesting than that. You can see that the entropy of the hotter object decreases (negative $d Q$ ), and that of the colder one increases (positive $d Q$ ), but by a different amount: in fact, it increases so much that it makes the total change in entropy for the system positive. This shows that entropy is rather different from energy (which is simply conserved in the process). You can always make it increase just by letting a process \"take its normal course\" - in this case, just letting the heat flow from the warmer to the colder object until they reach thermal equilibrium with each other (at which point, of course, the entropy will stop increasing, since it is a function of the state and the state will no longer change).

Although not immediately obvious from the above, the absolute (or Kelvin) temperature scale plays an essential role in the definition of the entropy, in the sense that only in such a scale (or another scale linearly proportional to it) is the entropy, as defined by {numref}`Eq. %s <eq-13.12>`, a state variable; that is, only when using such a temperature scale is the integral {eq}`eq-13.12` path-independent. The proof of this (which is much too complicated to even sketch here) relies essentially on the Carnot principle, to be discussed next.

(sec-13.4.2)=
### 13.4.2 The efficiency of heat engines

By the beginning of the 19th century, an industrial revolution was underway in England, due primarily to the improvements in the efficiency of steam engines that had taken place a few decades earlier. It was natural to ask how much this efficiency could ultimately be increased, and in 1824, a French engineer, Nicolas Sadi Carnot, wrote a monograph that provided an answer to this question.

Carnot modeled a \"heat engine\" as an abstract machine that worked in a cycle. In the course of each cycle, the engine would take in an amount of heat $Q_{h}$ from a \"hot reservoir,\" give off (or \"exhaust\") an amount of heat $\left|Q_{c}\right|$ to a \"cold reservoir,\" and produce an amount of work $|W|$. (I am using absolute value bars here because, from the point of view of the engine, $Q_{c}$ and $W$ must be negative quantities.) At the end of the cycle, the engine should be back to its initial state, so $\Delta E_{\text {engine }}=0$. The hot and cold reservoirs were supposed to be systems with very large heat capacities, so that the change in their temperatures as they took in or gave off the heat from or to the engine would be negligible.

If $\Delta E_{\text {engine }}=0$, we must have

:::{math}
:label: eq-13.14
\Delta E_{\text {engine }}=Q_{h}+Q_{c}+W=Q_{h}-\left|Q_{c}\right|-|W|=0
:::

that is, the work produced by the engine must be

:::{math}
:label: eq-13.15
|W|=Q_{h}-\left|Q_{c}\right|
:::

The energy input to the engine is $Q_{h}$, so it is natural to define the efficiency as $\epsilon=|W| / Q_{h}$; that is to say, the Joules of work done per Joule of heat taken in. A value of $\epsilon=1$ would mean an efficiency of $100 \%$, that is, the complete conversion of thermal energy into macroscopic work. By {numref}`Eq. %s <eq-13.15>`, we have

:::{math}
:label: eq-13.16
\epsilon=\frac{|W|}{Q_{h}}=\frac{Q_{h}-\left|Q_{c}\right|}{Q_{h}}=1-\frac{\left|Q_{c}\right|}{Q_{h}}
:::

which shows that $\epsilon$ will always be less than 1 as long as the heat exhausted to the cold reservoir, $Q_{c}$, is nonzero. This is always necessarily the case for steam engines: the steam needs to be cooled off at the end of the cycle, so a new cycle can start again.

Carnot considered a hypothetical \"reversible\" engine (sometimes called a Carnot machine), which could be run backwards, while interacting with the same two reservoirs. In backwards mode, the machine would work as a refrigerator or heat pump. It would take in an amount of work $W$ per cycle (from some external source) and use that to absorb the amount of heat $\left|Q_{c}\right|$ from the cold reservoir and dump the amount $Q_{h}$ to the hot reservoir. Carnot argued that no heat engine could have a greater efficiency than a reversible one working between the same heat reservoirs, and, consequently, that all reversible engines, regardless of their composition, would have the same efficiency when working in between the same temperatures. His argument was based on the observation that a hypothetical engine with a greater efficiency than the reversible one could be used to drive a reversible one in refrigerator mode, to produce as the sole result the transfer of some net amount of heat from the cold to the hot reservoir ${ }^{4}$, something that we argued in {ref}`Section 13.1 <sec-13.1>` should be impossible.

What makes this result more than a theoretical curiosity is the fact that an ideal gas would, in fact, provide a suitable working substance for a Carnot machine, if put through the following cycle (the so-called \"Carnot cycle\"): an isothermal expansion, followed by an adiabatic expansion, then an isothermal compression, and finally an adiabatic compression. What makes this ideally reversible is the fact that the heat is exchanged with each reservoir only when the gas is at (nearly) the same temperature as the reservoir itself, so by just \"nudging\" the temperature up or down a little bit you can get the exchange to go either way. When the ideal gas laws are used to calculate the efficiency of such a machine, the result (the Carnot efficiency) is

:::{math}
:label: eq-13.17
\epsilon_{C}=1-\frac{T_{c}}{T_{h}}
:::

where the temperatures must be measured in degrees Kelvin, the natural temperature scale for an ideal gas.

It is actually easy to see the connection between this result and the entropic formulation of the second law presented above. Suppose for a moment that Carnot's principle does not hold, that is to say, that we can build an engine with $\epsilon>\epsilon_{C}=1-T_{c} / T_{h}$. Since {eq}`eq-13.16` must hold in any case (because of conservation of energy), we find that this would imply

:::{math}
:label: eq-13.18
1-\frac{\left|Q_{c}\right|}{Q_{h}}>1-\frac{T_{c}}{T_{h}}
:::

and then some very simple algebra shows that

:::{math}
:label: eq-13.19
-\frac{Q_{h}}{T_{h}}+\frac{\left|Q_{c}\right|}{T_{c}}<0
:::

But now consider the total entropy of the system formed by the engine and the two reservoirs. The engine's entropy does not change (because it works in a cycle); the entropy of the hot reservoir goes down by an amount $-Q_{h} / T_{h}$; and the entropy of the cold reservoir goes $u p$ by an amount $\left|Q_{c}\right| / T_{c}$. So the left-hand side of {numref}`Eq. %s <eq-13.19>` actually equals the total change in entropy, and {numref}`Eq. %s <eq-13.19>` is telling us that this change is negative (the total entropy goes down) during the operation of this hypothetical heat engine whose efficiency is greater than the Carnot limit {eq}`eq-13.17`. Since this is impossible (the total entropy of a closed system can never decrease), we conclude that the Carnot limit must always hold.

As you can see, the seemingly trivial observation with which I started this section (namely, that heat always flows spontaneously from a hotter object to a colder object, and never in reverse) turns out to have profound consequences. In particular, it means that the complete conversion of thermal energy into macroscopic work is essentially impossible ${ }^{5}$, which is why we treat mechanical energy as \"lost\" once it is converted to thermal energy. By Carnot's theorem, to convert some of that

thermal energy back to work we would need to introduce a colder reservoir (and take advantage, so to speak, of the natural flow of heat from hotter to colder), and then we would only get a relatively small conversion efficiency, unless the cold reservoir is really at a very low Kelvin temperature (and to create such a cold reservoir would typically require refrigeration, which again consumes energy). It is easy to see that Carnot efficiencies for reservoirs close to room temperature are rather pitiful. For instance, if $T_{h}=300 \mathrm{~K}$ and $T_{c}=273 \mathrm{~K}$, the best conversion efficiency you could get would be 0.09 , or $9 \%$.

(sec-13.4.3)=
### 13.4.3 But what IS entropy, anyway?

The existence of this quantity, the entropy, which can be measured or computed (up to an arbitrary reference constant) for any system in thermal equilibrium, is one of the great discoveries of 19th century physics. There are tables of entropies that can be put to many uses (for instance, in chemistry, to figure out which reactions will happen spontaneously and which ones will not), and one could certainly take the point of view that those tables, plus the basic insight that the total entropy can never decrease for a closed system, are all one needs to know about it. From this perspective, entropy is just a convenient number that we can assign to any equilibrium state of any system, which gives us some idea of which way it is likely to go if the equilibrium is perturbed.

Nonetheless, it is natural for a physicist to ask to what, exactly, does this number correspond? What property of the equilibrium state is actually captured by this quantity? Especially, in the context of a microscopic description, since that is, by and large, how physicists have always been trying to explain things, by breaking them up into little pieces, and figuring out what the pieces were doing. What are the molecules or atoms of a system doing in a state of high entropy that is different from a state of low entropy?

The answer to this question is provided by the branch of physics known as Statistical Mechanics, which today is mostly quantum-based (since you need quantum mechanics to describe most of what atoms or molecules do, anyway), but which started in the context of pure classical mechanics in the mid-to-late 1800's and, despite this handicap, was actually able to make surprising headway for a while.

From this microscopic, but still classical, perspective (which applies, for instance, moderately well to an ideal gas), the entropy can be seen as a measure of the spread in the velocities and positions of the molecules that make up the system. If you think of a probability distribution, it has a mean value and a standard deviation. In statistical mechanics, the molecules making up the system are described statistically, by giving the probability that they might have a certain velocity or be at some point or another. These probability distributions may be very narrow (small standard deviation), if you are pretty certain of the positions or the velocities, or very broad, if you are not very certain at all, or rather expect the actual velocities and positions to be spread over a\
considerable range of values. A state of large entropy corresponds to a broad distribution, and a state of small entropy to a narrow one.

For an ideal gas, the temperature determines both the average molecular speed and the spread of the velocity distribution. This is because the average velocity is zero (since it is just as likely to be positive or negative), so the only way to make the average speed (or root-mean-square speed) large is to have a broad velocity distribution, which makes large speeds comparatively more likely. Then, as the temperature increases, so does the range of velocities available to the molecules, and correspondingly the entropy. Similarly (but more simply), for a given temperature, a gas that occupies a smaller volume will have a smaller entropy, since the range of positions available to the molecules will be smaller.

These considerations may help us understand an important property of entropy, which is that it increases in all irreversible processes. To begin with, note that this makes sense, since, by definition, these are processes that do not \"reverse\" spontaneously. If a process involves an increase in the total entropy of a closed system, then the reverse process will not happen, because it would require a spontaneous decrease in entropy, which the second law forbids. But, moreover, we can see the increase in entropy directly in many of the irreversible processes we have considered this semester, such as the ones involving friction. As I just pointed out above, in general, we may expect that increasing the temperature of an object will increase its entropy (other things being equal), regardless of how the increase in temperature comes about. Now, when mechanical energy is lost due to friction, the temperature of both of the objects (surfaces) involved increases, so the total entropy will increase as well. That marks the process as irreversible.

Another example of an irreversible process might be the mixing of two gases (or of two liquids, like cream and coffee). Start with all the \"brown\" molecules to the left of a partition, and all the \"white\" molecules to the right. After you remove the partition, the system will reach an equilibrium state in which the range of positions available to both the brown and white molecules has increased substantially - and this is, according to our microscopic picture, a state of higher entropy (other things, such as the average molecular speeds, being equal ${ }^{6}$ ).

For quantum mechanical systems, where the position and velocity are not simultaneously well defined variables, one uses the more abstract concept of \"state\" to describe what each molecule is doing. The entropy of a system in thermal equilibrium is then defined as a measure of the total number of states available to its microscopic components, compatible with the constraints that determine the macroscopic state (such as, again, total energy, number of particles, and volume).

(sec-13.5)=
## 13.5 In summary

1.  Temperature is a statistical quantity that provides a (typically indirect) measure of the concentration of thermal energy in a system. For a system that is (approximately) well described by classical mechanics, the temperature, as measured by a conventional thermometer, is directly proportional to the average translational kinetic energy per molecule.

2.  In a process in which a system does no work, a change in the system's temperature is related to a change in its total internal energy (which typically includes more than just translational kinetic energy contributions) by $\Delta E=C \Delta T$, where $C$ is the system's heat capacity for the process.

3.  The transfer of thermal energy between two systems without either one doing macroscopic work on each other is generally possible. Thermal energy transferred in this way is called heat, and denoted by the symbol $Q$.

4.  The actual definition of a system's heat capacity is $C=Q / \Delta T$. For a homogeneous system (made of just one substance), $C=m c$, where $m$ is the system's mass and $c$ the substance's specific heat. Specific heats typically depend on temperature in nontrivial ways.

5.  Two systems isolated from the rest of the world but allowed to exchange thermal energy with each other will eventually reach a state of thermal equilibrium in which their temperatures will be the same (zero-th law of thermodynamics).

6.  The work done on (or by) a system by (or on) its environment, plus the heat given to (or taken from) the system by its environment, always equals the net change in the system's total energy (conservation of energy, or first law of thermodynamics; {numref}`Eq. %s <eq-13.8>`).

7.  For any system in thermal equilibrium, there exists a state variable, called entropy, with the property that it can never decrease for a closed system. When a system at temperature $T$ takes in a small amount of heat $d Q$, its change in entropy is given by $d S=d Q / T$.

8.  This principle of never-decreasing entropy is equivalent to the statement that \"No process is possible whose sole result is the transfer of heat from a cooler to a hotter body.\"

9.  The principle 7. is also equivalent to Carnot's theorem, which states that \"it is impossible for an engine that operates in a cycle, taking in heat from a hot reservoir at temperature $T_{h}$ and exhausting heat to a cold reservoir at temperature $T_{c}$, to do work with an efficiency greater than $1-T_{c} / T_{h} . "$

10. Either one of 7., 8., or 9., above, may be regarded as an equivalent statement of the second law of thermodynamics.

11. Carnot's theorem shows the limitations inherent in the conversion of thermal energy into macroscopic work, which is the reason why one usually regards mechanical energy that is converted into thermal energy as \"lost.\"

12. Microscopically, the entropy of a system is a measure of the range of distinct states available to its microscopic components (atoms or molecules) that are compatible with the set of macroscopic constraints that determine its thermal equilibrium state. More entropy means a greater range of possible \"microstates.\"

13. Entropy always increases in irreversible processes.

(sec-13.6)=
## 13.6 Examples

(sec-13.6.1)=
### 13.6.1 Calorimetry

The specific heat of aluminum is $900 \mathrm{~J} / \mathrm{kg} \cdot \mathrm{K}$, and that of water is $4186 \mathrm{~J} \cdot \mathrm{K}$. Suppose you drop a block of aluminum of mass 1 kg at a temperature of $80^{\circ} \mathrm{C}$ in a liter of water (which also has a mass of 1 kg ) at a temperature of $20^{\circ} \mathrm{C}$. What is the final temperature of the system, assuming no exchange of heat with the environment takes place? How much energy does the aluminum lose/the water gain?

(ch-13-solution)=
### Solution

Let us call $T_{\mathrm{Al}}$ the initial temperature of the aluminum, $T_{\text {water }}$ the initial temperature of the water, and $T_{f}$ their final common temperature. The thermal energy given off by the aluminum equals $\Delta E_{\mathrm{Al}}=C_{\mathrm{Al}}\left(T_{f}-T_{\mathrm{Al}}\right)$ (this follows from the definition {eq}`eq-13.1` of heat capacity; we could equally well call this quantity \"the heat given off by the aluminum\"). In the same way, the thermal energy change of the water (heat absorbed by the water) equals $\Delta E_{\text {water }}=C_{\text {water }}\left(T_{f}-T_{\text {water }}\right)$. If the total system is closed, the sum of these two quantities, each with its appropriate sign, must be zero:

:::{math}
:label: eq-13.20
0=\Delta E_{\mathrm{Al}}+\Delta E_{\text {water }}=C_{\mathrm{Al}}\left(T_{f}-T_{\mathrm{Al}}\right)+C_{\text {water }}\left(T_{f}-T_{\text {water }}\right)
:::

This equation for $T_{f}$ has the solution

:::{math}
:label: eq-13.21
T_{f}=\frac{C_{\mathrm{Al}} T_{\mathrm{Al}}+C_{\text {water }} T_{\text {water }}}{C_{\mathrm{Al}}+C_{\text {water }}}
:::

As you can see, the result is a weighted average of the two starting temperatures, with the corresponding heat capacities as the weighting factors.

The heat capacities $C$ are equal to the given specific heats multiplied by the respective masses. In this case, the mass of aluminum and the mass of the water are the same, so they will cancel in the final result. Also, we can use the temperatures in degrees Celsius, instead of Kelvin. This is not immediately obvious from the final expression {eq}`eq-13.21`, but if you look at {eq}`eq-13.20` you'll see it involves only temperature differences, and those have the same value in the Kelvin and Celsius scales.

Substituting the given values in {eq}`eq-13.21`, then, we get

:::{math}
:label: eq-13.22
T_{f}=\frac{900 \times 80+4186 \times 20}{900+4186}=30.6^{\circ} \mathrm{C}
:::

This is much closer to the initial temperature of the water, as expected, since it has the greater heat capacity. The amount of heat exchanged is

:::{math}
:label: eq-13.23
C_{\text {water }}\left(T_{f}-T_{\text {water }}\right)=4186 \times(30.6-20)=44,440 \mathrm{~J}=44.4 \mathrm{~kJ}
:::

So, 1 kg of aluminum gives off 44.4 kJ of thermal energy and its temperature drops almost $50^{\circ} \mathrm{C}$, from $80^{\circ} \mathrm{C}$ to $30.6^{\circ} \mathrm{C}$, whereas 1 kg of water takes in the same amount of thermal energy and its temperature only rises about $10.6^{\circ} \mathrm{C}$.

(sec-13.6.2)=
### 13.6.2 Equipartition of energy

Estimate the speed of an oxygen molecule in air at room temperature (about 300 K ).

(ch-13-solution-1)=
### Solution

Recall that in {ref}`Section 13.2.2 <sec-13.2.2>` I mentioned that the average translational kinetic energy of a molecule in a system at a temperature $T$ is $\frac{3}{2} k_{B} T$ ({numref}`Eq. %s <eq-13.7>`, where $k_{B}$, Boltzmann's constant, is equal to $1.38 \times 10^{-23} \mathrm{~J} / \mathrm{K}$. So, at $T=300 \mathrm{~K}$, a molecule of oxygen (or of anything else, for that matter) should have, on average, a kinetic energy of

:::{math}
:label: eq-13.24
\left\langle K_{\text {trans }}\right\rangle=\frac{3}{2} k_{B} T=\frac{3}{2} \times 1.38 \times 10^{-23} \times 300 \mathrm{~J}=6.21 \times 10^{-21} \mathrm{~J}
:::

Since $K=\frac{1}{2} m v^{2}$, we can figure out the average value of $v^{2}$ if we know the mass of an oxygen molecule. This is something you can look up, or derive like this: One mole of oxygen atoms has a mass of 16 grams ( 16 is the atomic mass number of oxygen) and contains Avogadro's number of atoms, $6.02 \times 10^{23}$. So a single atom has a mass of $0.016 \mathrm{~kg} / 6.02 \times 10^{23}=2.66 \times 10^{-26} \mathrm{~kg}$. A molecule of oxygen contains two atoms, so it has twice the mass, $m=5.32 \times 10^{-26} \mathrm{~kg}$. Then,

:::{math}
:label: eq-13.25
\left\langle v^{2}\right\rangle=\frac{2\left\langle K_{\text {trans }}\right\rangle}{m}=\frac{2 \times 6.21 \times 10^{-21} \mathrm{~J}}{5.32 \times 10^{-26} \mathrm{~kg}}=2.33 \times 10^{5} \frac{\mathrm{m}^{2}}{\mathrm{~s}^{2}}
:::

The square root of this will give us what is called the \"root mean square\" velocity, or $v_{r m s}$ :

:::{math}
:label: eq-13.26
v_{r m s}=\sqrt{2.33 \times 10^{5} \frac{\mathrm{m}^{2}}{\mathrm{~s}^{2}}}=483 \frac{\mathrm{m}}{\mathrm{s}}
:::

This is of the same order of magnitude as (but larger than) the speed of sound in air at room temperature (about $340 \mathrm{~m} / \mathrm{s}$, as you may recall from {ref}`Chapter 12 <ch-12>`).

(sec-13.7)=
## 13.7 Problems

(ch-13-problem-1)=
### Problem 1

Consider a system of two objects in contact, one initially hotter than the other, so they may directly exchange thermal energy, in isolation from the rest of the world. According to the laws of thermodynamics, what must happen to the system's total energy and entropy? (Do they change, increase, decrease, stay constant\...?)

(ch-13-problem-2)=
### Problem 2

Consider the same two objects in Problem 1 and suppose the heat capacity of the colder object is much greater than the heat capacity of the hotter one. When the system reaches thermal equilibrium, will its final temperature will be closer to the initial temperature of the hot object, the colder object, or exactly halfway between the two initial temperatures? Why?

(ch-13-problem-3)=
### Problem 3

Which of the following is not a valid formulation of the second law of thermodynamics?\
(a) For any system in thermal equilibrium, there exists a state variable, called entropy, with the property that it can never decrease for a closed system.\
(b) No process is possible whose sole result is the transfer of heat from a cooler to a hotter body.\
(c) It is impossible for an engine that operates in a cycle, taking in heat from a hot reservoir at temperature $T_{h}$ and exhausting heat to a cold reservoir at temperature $T_{c}$, to do work with an efficiency greater than $1-T_{c} / T_{h}$.\
(d) The entropy of any system goes to zero as $T$ (the absolute, or Kelvin) temperature goes to zero.

(ch-13-problem-4)=
### Problem 4

Which of the following statements is true?\
(a) Once the entropy of a system increases, it is impossible to bring it back down.\
(b) Once some amount of mechanical energy is converted to thermal energy, it is impossible to turn any of it back into mechanical energy.\
(c) It is always possible to reduce the entropy of a system, for instance, by cooling it.\
(d) All of the above statements are true.\
(e) None of the above statements are true.

(ch-13-other-questions)=
### Other questions

- Can you tell the temperature of a gas by measuring the translational kinetic energy of a single molecule?

- Does a shuffled deck of cards have more or less entropy (in the thermodynamic sense) than an identical, ordered set of cards? Assume they are at the same temperature.

- A diatomic gas molecule, such as $O_{2}$, can store kinetic energy in the form of vibrations and rotations, in addition to just translation of the center of mass. By contrast, a monoatomic gas molecule such as $C$ has virtually no kinetic energy (at normal temperatures) other than translational kinetic energy. Which kind of gas do you expect to have a larger molar heat capacity (heat capacity per molecule)?
