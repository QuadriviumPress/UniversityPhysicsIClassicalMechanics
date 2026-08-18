---
title: "4. Kinetic Energy"
short_title: "Chapter 4"
label: ch-4
---

## 4.1 Kinetic Energy {#kinetic-energy-1}

For a long time in the development of classical mechanics, physicists were aware of the existence of two different quantities that one could define for an object of inertia $m$ and velocity $v$. One was the momentum, $m v$, and the other was something proportional to $m v^{2}$. Despite their obvious similarities, these two quantities exhibited different properties and seemed to be capturing different aspects of motion.

When things got finally sorted out, in the second half of the 19th century, the quantity $\frac{1}{2} m v^{2}$ came to be recognized as a form of energy - itself perhaps the most important concept in all of physics. Kinetic energy, as this quantity is called, may be the most obvious and intuitively understandable kind of energy, and so it is a good place to start our study of the subject.

We will use the letter $K$ to denote kinetic energy, and, since it is a form of energy, we will express it in the units especially named for this purpose, which is to say joules (J). 1 joule is $1 \mathrm{~kg} \cdot \mathrm{m}^{2} / \mathrm{s}^{2}$. In the definition

$$\begin{equation*}
K=\frac{1}{2} m v^{2} \tag{4.1}
\end{equation*}$$

the letter $v$ is meant to represent the magnitude of the velocity vector, that is to say, the speed of the particle. Hence, unlike momentum, kinetic energy is not a vector, but a scalar: there is no sense of direction associated with it. In three dimensions, one could write

$$\begin{equation*}
K=\frac{1}{2} m\left(v_{x}^{2}+v_{y}^{2}+v_{z}^{2}\right) \tag{4.2}
\end{equation*}$$

There is, therefore, some amount of kinetic energy associated with each component of the velocity vector, but in the end they are all added together in a lump sum.

For a system of particles, we will treat kinetic energy as an additive quantity, just like we did for momentum, so the total kinetic energy of a system will just be the sum of the kinetic energies of all the particles making up the system. Note that, unlike momentum, this is a scalar (not a vector) sum, and most importantly, that kinetic energy is, by definition, always positive, so there can be no question of a \"cancellation\" of one particle's kinetic energy by another, again unlike what happened with momentum. Two objects of equal mass moving with equal speeds in opposite directions have a total momentum of zero, but their total kinetic energy is definitely nonzero. Basically, the kinetic energy of a system can never be zero as long as there is any kind of motion going on in the system.

### 4.1.1 Kinetic energy in collisions {#kinetic-energy-in-collisions}

To gain some further insights into the concept of kinetic energy, and the ways in which it is different from momentum, it is useful to look at it in the same setting in which we \"discovered\" momentum, namely, one-dimensional collisions in an isolated system. If we look again at the collision represented in Figure 1 of Chapter 3, reproduced below,

![image](../images/2024_09_14_9969b06773f10b6936e8g-088.jpg)

Figure 4.1: Elastic collision in an isolated system. (Figure 3.1.)\
we can use the definition (4.1) to calculate the initial and final values of $K$ for each object, and for the system as a whole. Remember we found that, for this particular system, $m_{2}=2 m_{1}$, so we can just set $m_{1}=1 \mathrm{~kg}$ and $m_{2}=2 \mathrm{~kg}$, for simplicity. The initial and final velocities are $v_{1 i}=1 \mathrm{~m} / \mathrm{s}$,\
$v_{2 i}=0, v_{1 f}=-1 / 3 \mathrm{~m} / \mathrm{s}, v_{2 f}=2 / 3 \mathrm{~m} / \mathrm{s}$, and so the kinetic energies are

$$K_{1 i}=\frac{1}{2} \mathrm{~J}, K_{2 i}=0 ; \quad K_{1 f}=\frac{1}{18} \mathrm{~J}, K_{2 f}=\frac{4}{9} \mathrm{~J}$$

Note that $1 / 18+4 / 9=9 / 18=1 / 2$, and so

$$K_{s y s, i}=K_{1 i}+K_{2 i}=\frac{1}{2} \mathrm{~J}=K_{1 f}+K_{2 f}=K_{s y s, f}$$

In words, we find that, in this collision, the final value of the total kinetic energy is the same as its initial value, and so it looks like we have \"discovered\" another conserved quantity (besides momentum) for this system.

This belief may be reinforced if we look next at the collision depicted in Figure 2 of Chapter 3, again reproduced below. Recall I pointed out back then that we can think of this as being really the same collision as depicted in Figure 3.1, only looked at from another frame of reference (one moving initially to the right at $1 \mathrm{~m} / \mathrm{s}$ ). We will have more to say about how to transform quantities from a frame of reference to another by the end of the chapter.

![image](../images/2024_09_14_9969b06773f10b6936e8g-089.jpg)

Figure 4.2: Another elastic collision, equivalent to the one in Figure 1 as seen from another reference frame. (Figure 3.2.)

In any case, as observed there, all we need to do is add $-1 \mathrm{~m} / \mathrm{s}$ to all the velocities in the previous problem, so we have $v_{1 i}=0, v_{2 i}=-1 \mathrm{~m} / \mathrm{s}, v_{1 f}=-4 / 3 \mathrm{~m} / \mathrm{s}, v_{2 f}=-1 / 3 \mathrm{~m} / \mathrm{s}$. The corresponding kinetic energies are, accordingly, $K_{1 i}=0, K_{2 i}=1 \mathrm{~J}, K_{1 f}=\frac{8}{9} \mathrm{~J}, K_{2 f}=\frac{1}{9} \mathrm{~J}$. These are all different\
from the values we had in the previous example, but note that once again the total kinetic energy after the collision equals the total kinetic energy before-namely, 1 J in this case ${ }^{1}$.

Things are, however, very different when we consider the third collision example shown in Chapter 3 , namely, the one where the two objects are stuck together after the collision.

![image](../images/2024_09_14_9969b06773f10b6936e8g-090.jpg)

Figure 4.3: A totally inelastic collision. (Figure 3.3.)

Their joint final velocity, consistent with conservation of momentum, is $v_{1 f}=v_{2 f}=1 / 3 \mathrm{~m} / \mathrm{s}$. Since the system starts as in Figure 4.1, its kinetic energy is initially $K_{\text {sys }, i}=\frac{1}{2} \mathrm{~J}$, but after the collision we have only

$$K_{\text {sys }, f}=\frac{1}{2}(3 \mathrm{~kg})\left(\frac{1}{3} \frac{\mathrm{m}}{\mathrm{s}}\right)^{2}=\frac{1}{6} \mathrm{~J}$$

So kinetic energy is not conserved in this case at all.\
What this shows, however, is that unlike the total momentum of a system, which is completely unaffected by internal interactions, the total kinetic energy does depend on the details of the interaction, and thus conveys some information about its nature. We can then refine our study of collisions to distinguish two kinds: the ones where the initial kinetic energy is recovered after the collision, which we will call elastic, and the ones where it is not, which we call inelastic. A

special case of inelastic collision is the one called totally inelastic, where the two objects end up stuck together, as in Figure 4.3. As we shall see later, the kinetic energy \"deficit\" is largest in that case.

I have said above that in an elastic collision the kinetic energy is \"recovered,\" and I prefer this terminology to \"conserved,\" because, in fact, unlike the total momentum, the total kinetic energy of a system does not remain constant throughout the interaction, not even during an elastic collision. The simplest example to show this would be an elastic, head-on collision between two objects of equal mass, moving at the same speed towards each other. In the course of the collision, both objects are brought momentarily to a halt before they reverse direction and bounce back, and at that instant, the total kinetic energy is zero.

You can also examine Figures 4.1 and 4.2 above, and calculate, from the graphs, the value of the total kinetic energy during the collision. You will see that it dips to a minimum, and then comes back to its initial value (see also Figure 4.5, later in this chapter). Conventionally, we may talk of kinetic energy as being \"conserved\" in elastic collisions, but it is important to realize that we are looking at a different kind of \"conservation\" than what we had with the total momentum, which was constant before, during, and after the interaction, as long as the system remained isolated.

Elastic collisions do suggest that, whatever the ultimate nature of this thing we call \"energy\" might be, it may be possible to store it in some form (in this case, during the course of the collision), and then recover it, as kinetic energy, eventually. This paves the way for the introduction of other kinds of \"energy\" besides kinetic energy, as we shall see in a later chapter, and the possibility of interconversion to take place among these kinds. For the moment, we shall simply say that in an elastic collision some amount of kinetic energy is temporarily stored as some kind of \"internal energy,\" and after the collision this is converted back into kinetic energy; whereas, in an inelastic collision, some amount of kinetic energy gets irrevocably converted into some \"internal energy,\" and we never get it back.

Since whatever ultimately happens depends on the details and the nature of the interaction, we will be led to distinguish between \"conservative\" interactions, where kinetic energy is reversibly stored as some other form of energy somewhere, and \"dissipative\" interactions, where the energy conversion is, at least in part, irreversible. Clearly, elastic collisions are associated with conservative interactions and inelastic collisions are associated with dissipative interactions. This preliminary classification of interactions will have to be reviewed a little more carefully, however, in the next chapter.

### 4.1.2 Relative velocity and coefficient of restitution {#relative-velocity-and-coefficient-of-restitution}

An interesting property of elastic collisions can be disclosed from a careful study of figures 4.1 and 4.2. In both cases, as you can see, the relative velocity of the two objects colliding has the same magnitude (but opposite sign) before and after the collision. In other words: in an elastic collision, the objects end up moving apart at the same rate as they originally came together.

Recall that, in Chapter 1, we defined the velocity of object 2 relative to object 1 as the quantity

$$\begin{equation*}
v_{12}=v_{2}-v_{1} \tag{4.3}
\end{equation*}$$

(compare Eq. (1.21); and similarly the velocity of object 1 relative to object 2 is $v_{21}=v_{1}-v_{2}$. With this definition you can check that, indeed, the collisions shown in Figs. 4.1 and 4.2 satisfy the equality

$$\begin{equation*}
v_{12, i}=-v_{12, f} \tag{4.4}
\end{equation*}$$

(note that we could equally well have used $v_{21}$ instead of $v_{12}$ ). For instance, in Fig. 4.1, $v_{12, i}=$ $v_{2 i}-v_{1 i}=-1 \mathrm{~m} / \mathrm{s}$, whereas $v_{12, f}=2 / 3-(-1 / 3)=1 \mathrm{~m} / \mathrm{s}$. So the objects are initially moving towards each other at a rate of 1 m per second, and they end up moving apart just as fast, at 1 m per second. Visually, you should notice that the distance between the red and blue curves is the same before and after (but not during) the collision; the fact that they cross accounts for the difference in sign of the relative velocity, which in turns means simply that before the collision they were coming together, and afterwards they are moving apart.

It takes only a little algebra to show that Eq. (4.4) follows from the joint conditions of conservation of momentum and conservation of kinetic energy. The first one $\left(p_{i}=p_{f}\right)$ clearly has the form

$$\begin{equation*}
m_{1} v_{1 i}+m_{2} v_{2 i}=m_{1} v_{1 f}+m_{2} v_{2 f} \tag{4.5}
\end{equation*}$$

whereas the second one $\left(K_{i}=K_{f}\right)$ can be written as

$$\begin{equation*}
\frac{1}{2} m_{1} v_{1 i}^{2}+\frac{1}{2} m_{2} v_{2 i}^{2}=\frac{1}{2} m_{1} v_{1 f}^{2}+\frac{1}{2} m_{2} v_{2 f}^{2} \tag{4.6}
\end{equation*}$$

We can cancel out all the factors of $1 / 2$ in Eq. $(4.6)^{2}$, then rearrange it so that quantities belonging to object 1 are on one side, and quantities belonging to object 2 are on the other. We get

$$\begin{align*}
m_{1}\left(v_{1 i}^{2}-v_{1 f}^{2}\right) & =-m_{2}\left(v_{2 i}^{2}-v_{2 f}^{2}\right) \\
m_{1}\left(v_{1 i}-v_{1 f}\right)\left(v_{1 i}+v_{1 f}\right) & =-m_{2}\left(v_{2 i}-v_{2 f}\right)\left(v_{2 i}+v_{2 f}\right) \tag{4.7}
\end{align*}$$

(using the fact that $a^{2}-b^{2}=(a+b)(a-b)$ ). Note, however, that Eq. (4.5) can also be rewritten as

$$m_{1}\left(v_{1 i}-v_{1 f}\right)=-m_{2}\left(v_{2 i}-v_{2 f}\right)$$

This immediately allows us to cancel out the corresponding factors in Eq (4.7), so we are left with $v_{1 i}+v_{1 f}=v_{2 i}+v_{2 f}$, which can be rewritten as

$$\begin{equation*}
v_{1 f}-v_{2 f}=v_{2 i}-v_{1 i} \tag{4.8}
\end{equation*}$$

and this is equivalent to (4.4).\
So, in an elastic collision the speed at which the two objects move apart is the same as the speed at which they came together, whereas, in what is clearly the opposite extreme, in a totally inelastic collision the final relative speed is zero-the objects do not move apart at all after they collide. This suggests that we can quantify how inelastic a collision is by the ratio of the final to the initial magnitude of the relative velocity. This ratio is denoted by $e$ and is called the coefficient of restitution. Formally,

$$\begin{equation*}
e=-\frac{v_{12, f}}{v_{12, i}}=-\frac{v_{2 f}-v_{1 f}}{v_{2 i}-v_{1 i}} \tag{4.9}
\end{equation*}$$

For an elastic collision, $e=1$, as required by Eq. (4.4). For a totally inelastic collision, like the one depicted in Fig. 3, $e=0$. For a collision that is inelastic, but not totally inelastic, $e$ will have some value in between these two extremes. This knowledge can be used to \"design\" inelastic collisions (for homework problems, for instance!): just pick a value for $e$, between 0 and 1, in Eq. (4.9), and combine this equation with the conservation of momentum requirement (4.5). The two equations then allow you to calculate the final velocities for any values of $m_{1}, m_{2}$, and the initial velocities. Figure 4.4 below, for example, shows what the collision in Figure 4.1 would have been like, if the coefficient of restitution had been 0.6 instead of 1 . You can check, by solving (4.5) and (4.9) together, and using the initial velocities, that $v_{1 f}=-1 / 15 \mathrm{~m} / \mathrm{s}=-0.0667 \mathrm{~m} / \mathrm{s}$, and $v_{2 f}=8 / 15 \mathrm{~m} / \mathrm{s}$ $=0.533 \mathrm{~m} / \mathrm{s}$.

![image](../images/2024_09_14_9969b06773f10b6936e8g-093.jpg)

Figure 4.4: An $e=0.6$ collision between objects with the same inertias and initial velocities as in Figure 1.

Although, as I just mentioned, for most \"normal\" collisions the coefficient of restitution will be a positive number between 1 and 0 , there can be exceptions to this. If one of the objects passes through the other (like a bullet through a target, for instance), the value of $e$ will be negative (although still between 0 and 1 in magnitude). And $e$ can be greater than 1 for so-called \"explosive collisions,\" where some amount of extra energy is released, and converted into kinetic energy, as the objects collide. (For instance, two hockey players colliding on the rink and pushing each other away.) In this case, the objects may well fly apart faster than they came together.

An extreme example of a situation with $e>0$ is an explosive separation, which is when the two objects are initially moving together and then fly apart. In that case, the denominator of Eq. (4.9) is zero, and so $e$ is formally infinite. This suggests, what is in fact the case, namely, that although explosive processes are certainly important, describing them through the coefficient of restitution is rare, even when it would be formally possible. In practice, use of the coefficient of restitution is mostly limited to the elastic-to-completely inelastic range, that is, $0 \leq e \leq 1$.

## 4.2 \"Convertible\" and \"translational\" kinetic energy {#convertible-and-translational-kinetic-energy}

Figure 4.5 shows how the total kinetic energy varies with time, for the two objects shown colliding in Figure 4.1, depending on the details of the collision, namely, on the value of $e$. The three curves shown cover the elastic case, $e=1$ (Figure 4.1), the totally inelastic case, $e=0$ (Figure 4.3), and the inelastic case with $e=0.6$ of Figure 4.4. Recall that the total momentum is conserved in all three cases.

![image](../images/2024_09_14_9969b06773f10b6936e8g-094.jpg)

Figure 4.5: The total kinetic energy as a function of time for the collisions shown in Figures 1, 3 and 4, respectively.

Figure 4.5 shows that the greatest loss of kinetic energy happens for the totally inelastic collision, which, as we will see in a moment, is, in fact, a general result. That being the case, the figure also shows that it may not be always be possible to bring the total kinetic energy down to zero, even temporarily. The reason for this is that, if momentum is conserved, the velocity of the center of mass cannot change, so if the center of mass was moving before the collision, it must still be moving afterwards; and, as mentioned in this chapter's introduction, as long as there is motion in a system, its total kinetic energy cannot be zero.

All of this suggests that it should be possible to break up a system's total kinetic energy into two parts: one part associated with the motion of the center of mass, which cannot change in any momentum-conserving collision, and one part associated with the relative motion of the parts that make up the system. This second part would vanish irreversibly in a totally inelastic collision, whereas it would recover its original value in an elastic collision.

The way to see this mathematically, for a system of two objects with masses $m_{1}$ and $m_{2}$, is to introduce the center of mass velocity $v_{c m}$ \[Eq. (3.10)\]

$$v_{c m}=\frac{m_{1} v_{1}+m_{2} v_{2}}{m_{1}+m_{2}}$$

and the relative velocity $v_{12}=v_{2}-v_{1}$ (Eq. (4.3) above), and observe that the velocities $v_{1}$ and $v_{2}$ can be written, respectively, as

$$\begin{align*}
& v_{1}=v_{c m}-\frac{m_{2}}{m_{1}+m_{2}} v_{12} \\
& v_{2}=v_{c m}+\frac{m_{1}}{m_{1}+m_{2}} v_{12} \tag{4.10}
\end{align*}$$

Substituting the equations (4.10) into the expression $K_{\text {sys }}=\frac{1}{2} m_{1} v_{1}^{2}+\frac{1}{2} m_{2} v_{2}^{2}$, one finds that the cross-terms vanish, and all that is left is

$$K_{\text {sys }}=\frac{1}{2}\left(m_{1}+m_{2}\right) v_{c m}^{2}+\frac{1}{2} \frac{m_{1} m_{2}^{2}+m_{2} m_{1}^{2}}{\left(m_{1}+m_{2}\right)^{2}} v_{12}^{2}$$

A factor of $\left(m_{1}+m_{2}\right)$ may be canceled in the last term, and the final expression takes the form

$$\begin{equation*}
K_{\text {sys }}=K_{c m}+K_{c o n v} \tag{4.11}
\end{equation*}$$

where the center of mass kinetic energy (or translational energy) is just what one would have if the whole system was a single particle of mass $M=m_{1}+m_{2}$ moving at the center of mass speed:

$$\begin{equation*}
K_{c m}=\frac{1}{2} M v_{c m}^{2} \tag{4.12}
\end{equation*}$$

and the \"convertible energy\" $K_{\text {conv }}$ is the part associated with the relative motion, which can be\
made to vanish entirely in an inelastic collision ${ }^{3}$ :

$$\begin{equation*}
K_{\text {conv }}=\frac{1}{2} \frac{m_{1} m_{2}}{m_{1}+m_{2}} v_{12}^{2}=\frac{1}{2} \mu v_{12}^{2} \tag{4.13}
\end{equation*}$$

The last equation implicitly defines a useful quantity that we call the reduced mass of a system of two particles, and denote by $\mu$ :

$$\begin{equation*}
\mu=\frac{m_{1} m_{2}}{m_{1}+m_{2}} \tag{4.14}
\end{equation*}$$

Equation (4.11), with the definitions (4.12) and (4.13), pretty much explains everything that we see going on in Figure 4.5. The total kinetic energy is the sum of two terms, the first of which, $K_{c m}$, can never change: it is, in fact, as constant as the total momentum itself, since it involves the center of mass velocity, $v_{c m}$, which is proportional to the total momentum of the system (recall equation (3.11)). The term that can, and does change, is the second one, the convertible energy. In fact, in an ordinary collision in which the objects do not pass through each other, there must be at least an instant in time when $K_{\text {conv }}=0$. This is because it involves the relative velocity, and since the relative velocity must change sign at some point (the objects are initially coming together, but end up moving apart), it must be zero at that time.

This explains why all the curves in Fig. 4.5 have the same minimum value (even though they may reach it at different times): that value is clearly $K_{c m}$ for the system (since $K_{\text {conv }}$ is zero at that time). It is the same for all the curves because all the systems considered have the same total mass and momentum (as determined by the initial velocities)---we just chose them that way.

Since $K_{c m}$ cannot change for an isolated system, the maximum kinetic energy that can be lost in a collision in such a system is the initial value of $K_{\text {conv }}$, which we would denote as $K_{\text {conv }, i}$. This is, in fact, completely lost in a totally inelastic collision, since in that case $v_{12, f}=0$, and Eq. (4.13) then gives $K_{\text {conv,f }}=0$. In fact, using Eq. (4.9), we can relate the final value of the convertible energy to its initial value via the coefficient of restitution:

$$\begin{equation*}
K_{\text {conv }, f}=\frac{1}{2} \mu v_{12, f}^{2}=\frac{1}{2} \mu e^{2} v_{12, i}^{2}=e^{2} K_{\text {conv }, i} \tag{4.15}
\end{equation*}$$

Thus, for example, in a collision with $e=0.6$, the final value of the convertible energy would be only 0.36 times its initial value: $64 \%$ of it would have been \"lost.\" (This is not, however, the same as $64 \%$ of the total initial energy, since the latter still includes $K_{c m}$, which does not change.) We can also write Eq. (4.15) as

$$\begin{equation*}
\Delta K_{\text {sys }}=\left(e^{2}-1\right) K_{\text {conv }, i}=\left(e^{2}-1\right) \frac{1}{2} \mu v_{12, i}^{2} \tag{4.16}
\end{equation*}$$

since the only possible change in $K_{\text {sys }}$ must come from the convertible energy.

Although we have derived the decomposition (4.11) for the very restricted situation of two objects moving in one dimension, the basic result is quite general: first, everything in the derivation works if $v_{1}$ and $v_{2}$ are replaced by vectors $\vec{v}_{1}$ and $\vec{v}_{2}$, so the results holds in three dimensions as well. Second, for a system of any number of particles, one still can write $K_{\text {sys }}$ as $K_{c m}+$ another term that depends only on the relative motion of all the pairs of particles. This \"generalized convertible energy,\" or kinetic energy of relative motion would have the form

$$K_{\text {rel }}=\frac{1}{2} \mu_{12} v_{12}^{2}+\frac{1}{2} \mu_{13} v_{13}^{2}+\ldots+\frac{1}{2} \mu_{23} v_{23}^{2}+\ldots$$

(in this expression, something like $\mu_{23}$ means a reduced mass like the one in Eq. (4.14), only for masses $m_{2}$ and $m_{3}$, and so forth).

When we get to the study of rotational motion, for instance, we will see that the total kinetic energy of an extended rigid object can be written as $K_{c m}+K_{r o t}$, where $K_{\text {rot }}$, the rotational kinetic energy, is just the same kind of thing as what we have called the \"convertible energy\" here.

All of the above still leaves unanswered the question of what happens to the convertible energy that is lost in an inelastic collision. Just what is it that it gets converted into? The answer to this question will be the subject of the following chapter.

### 4.2.1 Kinetic energy and momentum in different reference frames {#kinetic-energy-and-momentum-in-different-reference-frames}

I have pointed out repeatedly before that all motion is relative, and so, to some extent, kinetic energy and momentum must be somewhat relative as well. A car in a freight train has a lot of momentum relative to an observer on the ground, but its momentum relative to another car on the same train is zero, since they are not moving relative to each other. The same could be said about its kinetic energy.

In general, if you have a system with a total momentum $\vec{p}_{\text {sys }}$ and inertia $M$, its center of mass will have a velocity $\vec{v}_{c m}=\vec{p}_{s y s} / M$. Then, if you were to move alongside the system with a velocity exactly equal to $\vec{v}_{c m}$, the total momentum of the system relative to you would be zero. If the system was a solid object, it would not \"hit\" you if you made contact; there would be no collision. It may help here to think, for instance, of aircraft refueling in flight: if the two planes' velocities are exactly matched, they can make contact without any damage, just as if they were at rest. A reference frame moving at a system's center of mass velocity is, for this reason, called a zero-momentum frame for the system in question.

Clearly, in such a reference frame, the translational kinetic energy of the system, $K_{c m}=\frac{1}{2} M v_{c m}^{2}$, will also be zero (since, in that frame, the center of mass is not moving at all). However, the relative motion term, $K_{\text {conv }}$, would be completely unaffected by the change in reference frame. This is because, as you may have noticed by now, to convert velocities from one frame of reference to\
another we just add or subtract from all the velocities the relative velocity of the two frames. This operation, however, will not change any of the relative velocities of the parts of the system, since these are all differences to begin with. Mathematically,

$$\left(v_{2}+v^{\prime}\right)-\left(v_{1}+v^{\prime}\right)=v_{2}-v_{1}$$

regardless of the value of $v^{\prime}$.\
So there something we might call absolute (as opposed to \"relative\") about the convertible kinetic energy: it is the same, it will have the same value, for any observer, regardless of how fast or in what direction that observer may be moving relative to the system as a whole. We may think of it as an intrinsic (meaning, observer-independent) property of the system.

## 4.3 In summary {#in-summary}

1.  The kinetic energy of a particle of mass $m$ moving with velocity $v$ is defined as $K=\frac{1}{2} m v^{2}$. It is a scalar quantity, and it is always positive. For a system of particles or an extended object, we define $K_{\text {sys }}$ as the sum of the kinetic energies of all the particles making up the system.

2.  For any system, the total kinetic energy can be written as the sum of the translational (or center of mass) kinetic energy, $K_{c m}$, and another term that involves the motion of the parts of the system relative to each other. (See Eq. (4.11) above.) The translational kinetic energy is constant for an isolated system, and is always given by $K_{c m}=\frac{1}{2} M v_{c m}^{2}$.

3.  The kinetic energy of relative motion (which, in the context of collisions, is called the convertible energy) is given, for the special case of a system consisting of two particles (or two non-rotating extended objects), by $K_{\text {conv }}=\frac{1}{2} \mu v_{12}^{2}$, where $\mu=m_{1} m_{2} /\left(m_{1}+m_{2}\right)$ is the reduced mass, and $v_{12}=v_{2}-v_{1}$ is the relative velocity of the two objects.

4.  In a one-dimensional collision between two objects that do not pass through each other, the convertible energy always drops to zero at some point, as a result of the interaction; that is, it is converted entirely into some other form of energy. At the end of the interaction, all the convertible energy may be recovered (elastic collision), or only part of it (inelastic collision), or none of it (completely inelastic collision).

5.  In terms of the coefficient of restitution $e$, defined as $e=-v_{12, f} / v_{12, i}$, elastic collisions have $e=1$, totally inelastic collisions have $e=0$, and inelastic collisions $0<e<1$. The total change in kinetic energy in the collision can be written as $\Delta K_{\text {sys }}=\Delta K_{\text {conv }}=\left(e^{2}-1\right) K_{\text {conv }, i}$.

6.  Another way to say the above is that in an elastic collision in one dimension, the two objects move apart after the collision at the same rate (relative speed) at which they approached each other initially. In a totally inelastic collision, conversely, the two objects do not move apart at all after the collision-they become \"stuck together.\"

7.  Besides the cases considered above, one may have collisions where the objects pass through each other, giving $e<0$, and \"explosive collisions,\" where $e>1$. In these latter collisions some internal source of energy is converted into additional kinetic energy when the objects interact. The extreme case of this is an explosive separation, which is the reverse of a totally inelastic collision-two objects initially moving together fly apart, with a net increase in the system's kinetic energy.

8.  The translational kinetic energy of a system will, in general, have different values for observers moving with different velocities. The convertible kinetic energy, on the other hand, is seen by all observers to have the same value, regardless of their relative state of motion.

## 4.4 Examples {#examples}

### 4.4.1 Collision graph revisited {#collision-graph-revisited}

Look again at the collision graph from example 3.5.1 from the point of view of the kinetic energy of the two carts.\
(a) What is the initial kinetic energy of the system?\
(b) How much of this is in the center of mass motion, and how much of is convertible?\
(c) Does the convertible kinetic energy go to zero at some point during the collision? If so, when? Is it fully recovered after the collision is over?\
(d) What kind of collision is this? (Elastic, inelastic, etc.) What is the coefficient of restitution?

### Solution {#solution}

\(a\) From the solution to example 3.5 .1 we know that

$$\begin{aligned}
v_{1 i} & =-1 \frac{\mathrm{m}}{\mathrm{s}} & v_{2 i} & =0.5 \frac{\mathrm{m}}{\mathrm{s}} \\
v_{1 f} & =1 \frac{\mathrm{m}}{\mathrm{s}} & v_{2 f} & =-0.5 \frac{\mathrm{m}}{\mathrm{s}}
\end{aligned}$$

and $m_{1}=1 \mathrm{~kg}$ and $m_{2}=2 \mathrm{~kg}$. So the initial kinetic energy is

$$\begin{equation*}
K_{s y s, i}=\frac{1}{2} m_{1} v_{1 i}^{2}+\frac{1}{2} m_{2} v_{2 i}^{2}=0.5 \mathrm{~J}+0.25 \mathrm{~J}=0.75 \mathrm{~J} \tag{4.17}
\end{equation*}$$

\(b\) To calculate $K_{c m}=\frac{1}{2}\left(m_{1}+m_{2}\right) v_{c m}^{2}$, we need $v_{c m}$, which in this case is equal to

$$v_{c m}=\frac{m_{1} v_{1 i}+m_{2} v_{2 i}}{m_{1}+m_{2}}=\frac{-1+2 \times 0.5}{3}=0$$

so $K_{c m}=0$, which means all the kinetic energy is convertible. We can also calculate that directly:

$$\begin{equation*}
K_{\text {conv }, i}=\frac{1}{2} \mu v_{12, i}^{2}=\frac{1}{2}\left(\frac{1 \times 2}{1+2} \mathrm{~kg}\right) \times\left(0.5 \frac{\mathrm{m}}{\mathrm{s}}-(-1) \frac{\mathrm{m}}{\mathrm{s}}\right)^{2}=\frac{1.5^{2}}{3} \mathrm{~J}=0.75 \mathrm{~J} \tag{4.18}
\end{equation*}$$

\(c\) If we look at figure 3.5, we can see that the carts do not pass through each other, so their relative velocity must be zero at some point, and with that, the convertible energy. In fact, the figure makes it quite clear that both $v_{1}$ and $v_{2}$ are zero at $t=5 \mathrm{~s}$, so at that point also $v_{12}=0$, and the convertible energy $K_{\text {conv }}=0$. (And so is the total $K_{\text {sys }}=0$ at that time, since $K_{c m}=0$ throughout.)

On the other hand, it is also clear that $K_{\text {conv }}$ is fully recovered after the collision is over, since the relative velocity just changes sign:

$$\begin{align*}
& v_{12, i}=v_{2 i}-v_{1 i}=0.5 \frac{\mathrm{m}}{\mathrm{s}}-(-1) \frac{\mathrm{m}}{\mathrm{s}}=1.5 \frac{\mathrm{m}}{\mathrm{s}} \\
& v_{12, f}=v_{2 f}-v_{1 f}=-0.5 \frac{\mathrm{m}}{\mathrm{s}}-1 \frac{\mathrm{m}}{\mathrm{s}}=-1.5 \frac{\mathrm{m}}{\mathrm{s}} \tag{4.19}
\end{align*}$$

Therefore

$$K_{\text {conv }, f}=\frac{1}{2} \mu v_{12, f}^{2}=\frac{1}{2} \mu v_{12, i}^{2}=K_{\text {conv }, i}$$

\(d\) Since the total kinetic energy (which in this case is only convertible energy) is fully recovered when the collision is over, the collision is elastic. Using equation (4.19), we can see that the coefficient of restitution is

$$e=-\frac{v_{12, f}}{v_{12, i}}=-\frac{-1.5}{1.5}=1$$

as it should be.

### 4.4.2 Inelastic collision and explosive separation {#inelastic-collision-and-explosive-separation}

Analyze example 3.5.2 from the point of view of the system's kinetic energy. In particular, answer the following questions:\
(a) What is the total kinetic energy of the system (i) before the players collide, (ii) right after the collision, when they are holding to one another, and (iii) after they separate. How much of this energy is translational (that is, center-of-mass kinetic energy), and how much is convertible?\
(b) Answer the same questions from the point of view of the player who is skating at a constant $1.5 \mathrm{~m} / \mathrm{s}$ to the right (player 3 )\
(To avoid needless repetition, you may use already established results, such as conservation of momentum.)

Solution (a) Before the players collide, we have

$$\begin{equation*}
K_{s y s, i}=\frac{1}{2} m_{1} v_{1 i}^{2}+\frac{1}{2} m_{2} v_{2 i}^{2}=\frac{1}{2}(80 \mathrm{~kg}) \times\left(3 \frac{\mathrm{m}}{\mathrm{s}}\right)^{2}+\frac{1}{2}(90 \mathrm{~kg}) \times\left(-2 \frac{\mathrm{m}}{\mathrm{s}}\right)^{2}=540 \mathrm{~J} \tag{4.20}
\end{equation*}$$

While they are still holding to each other, we know from the solution to example 3.5.2 that their joint velocity is 0.353 , and that this has to be also the velocity of their center of mass, which is unchanged by the collision. So, we have

$$\begin{equation*}
K_{c m}=\frac{1}{2}\left(m_{1}+m_{2}\right) v_{c m}^{2}=\frac{1}{2}(170 \mathrm{~kg})\left(0.353 \frac{\mathrm{m}}{\mathrm{s}}\right)^{2}=10.6 \mathrm{~J} \tag{4.21}
\end{equation*}$$

This is $K_{c m}$ throughout, as well as $K_{\text {sys }}$ right after the collision, since the collision is totally inelastic and that means that $K_{\text {conv }}$ drops to zero. Also, subtracting this from (4.20) will give us the initial value of the convertible energy, without the need for a separate calculation, so

$$\begin{equation*}
K_{c o n v, i}=K_{s y s, i}-K_{c m}=540 \mathrm{~J}-10.6 \mathrm{~J}=529.4 \mathrm{~J} \simeq 529 \mathrm{~J} \tag{4.22}
\end{equation*}$$

After the separation, the new total kinetic energy (for which I will use the subscript $f$ ) is

$$\begin{equation*}
K_{\text {sys }, i}=\frac{1}{2} m_{1} v_{1 f}^{2}+\frac{1}{2} m_{2} v_{2 f}^{2}=\frac{1}{2}(80 \mathrm{~kg}) \times\left(-0.176 \frac{\mathrm{m}}{\mathrm{s}}\right)^{2}+\frac{1}{2}(90 \mathrm{~kg}) \times\left(0.824 \frac{\mathrm{m}}{\mathrm{s}}\right)^{2}=31.8 \mathrm{~J} \tag{4.23}
\end{equation*}$$

where I have gotten the values for $v_{1 f}$ and $v_{2 f}$ from the solution to part (d) of Example 3.5.2. Subtracting $K_{c m}$ from this will give us the final value of the convertible energy:

$$\begin{equation*}
K_{c o n v, f}=K_{s y s, f}-K_{c m}=31.8 \mathrm{~J}-10.6 \mathrm{~J}=21.2 \mathrm{~J} \tag{4.24}
\end{equation*}$$

To summarize, then, we have:

- Before the collision:

$$K_{\text {sys }, i}=540 \mathrm{~J}, \quad K_{c m}=10.6 \mathrm{~J}, \quad K_{\text {conv }, i}=529.4 \mathrm{~J}$$

- Right after the collision (players still holding to each other):

$$K_{\text {sys }}=K_{c m}=10.6 \mathrm{~J}, \quad K_{c o n v}=0$$

- After the (explosive) separation:

$$K_{\text {sys }, f}=31.8 \mathrm{~J}, \quad K_{c m}=10.6 \mathrm{~J}, \quad K_{\text {conv }, i}=21.2 \mathrm{~J}$$

So, in the collision, approximately 529 J of kinetic energy \"disappeared\" from the system (or, we could say, were \"converted into some form of internal energy\"), whereas the players' pushing on each other managed to put about 21 J of kinetic energy back into the system; we will explore these kinds of processes in more detail in the following chapter!\
(b) We need to repeat all the above calculations with all the velocities shifted down by $1.5 \mathrm{~m} / \mathrm{s}$, to bring them to the reference frame of player 3. Instead of putting a subscript \" 3 \" on all the quantities, since we already have tons of subscripts to worry about, I'm going to follow an alternative convention and use a \"prime\" superscript (') to denote all the quantities in this frame of reference. In brief, we have

$$\begin{equation*}
K_{\text {sys }, i}^{\prime}=\frac{1}{2} m_{1}\left(v_{1 i}^{\prime}\right)^{2}+\frac{1}{2} m_{2}\left(v_{2 i}^{\prime}\right)^{2}=\frac{1}{2}(80 \mathrm{~kg}) \times\left(1.5 \frac{\mathrm{m}}{\mathrm{s}}\right)^{2}+\frac{1}{2}(90 \mathrm{~kg}) \times\left(-3.5 \frac{\mathrm{m}}{\mathrm{s}}\right)^{2}=641.3 \mathrm{~J} \tag{4.25}
\end{equation*}$$

$$\begin{gather*}
K_{c m}^{\prime}=\frac{1}{2}\left(m_{1}+m_{2}\right)\left(v_{c m}^{\prime}\right)^{2}=\frac{1}{2}(170 \mathrm{~kg})\left(0.353 \frac{\mathrm{m}}{\mathrm{s}}-1.5 \frac{\mathrm{m}}{\mathrm{s}}\right)^{2}=111.8 \mathrm{~J}  \tag{4.26}\\
K_{\text {conv }, i}^{\prime}=K_{\text {sys }, i}^{\prime}-K_{c m}^{\prime}=641.3 \mathrm{~J}-111.8 \mathrm{~J}=529.5 \mathrm{~J} \simeq 529 \mathrm{~J} \tag{4.27}
\end{gather*}$$

This shows explicitly that the convertible energy, as I pointed out earlier in this chapter, is the same in every reference frame! (The equality is exact, if you keep enough decimals in the calculation.)

Knowing this, we can simplify the calculation of the final kinetic energy, after the explosive separation: the convertible energy, $K_{\text {conv,f }}^{\prime}$, will be the same as in the earth reference frame, that is to say, 21.2 J, and the total kinetic energy will be $K_{\text {sys, } f}^{\prime}=K_{c m}^{\prime}+K_{c o n v, f}^{\prime}=111.8 \mathrm{~J}+21.2 \mathrm{~J}=133 \mathrm{~J}$.

So, in this frame of reference, we have (to three significant figures):

$$\begin{aligned}
K_{\text {sys }, i}^{\prime}=641 \mathrm{~J}, \quad K_{c m}^{\prime}=112 \mathrm{~J}, \quad K_{\text {conv }, i}^{\prime}=529 \mathrm{~J} & \text { (before the collision) } \\
K_{\text {sys }}^{\prime}=K_{c m}^{\prime}=112 \mathrm{~J}, \quad K_{\text {conv }}^{\prime}=0 & \text { (right after the collision) } \\
K_{\text {sys }, f}^{\prime}=133 \mathrm{~J}, \quad K_{c m}^{\prime}=112 \mathrm{~J}, \quad K_{\text {conv }, i}^{\prime}=21.2 \mathrm{~J} & \text { (after the separation) }
\end{aligned}$$

So, even though the total kinetic energy is different in the two reference frames, all the (inertial) observers will agree as to the amount of kinetic energy \"lost\" in the collision, as well as the amount of kinetic energy put back into the system by the players' pushing on each other.

## 4.5 Problems {#problems}

### Problem 1 {#problem-1}

A 71-kg man can throw a $1-\mathrm{kg}$ ball with a maximum speed of $6 \mathrm{~m} / \mathrm{s}$ relative to himself. Imagine that one day he decides to try to do that on roller skates. Starting from rest, he throws the ball as hard as he can, so it ends up moving at $6 \mathrm{~m} / \mathrm{s}$ relative to him, but he himself is recoiling as a result of the throw.\
(a) Assuming conservation of momentum, find the velocities of the man and the ball relative to the ground.\
(b) What is the kinetic energy of the system right after the throw? (By the system here we mean the man and the ball throughout.) Where did this kinetic energy come from?\
(c) Is the man's reference frame inertial throughout this process? Why or why not?\
(d) Does the center of mass of the system move at all throughout this process?

### Problem 2 {#problem-2}

Analyze Problem 1 from Chapter 3 from the point of view of the system's kinetic energy. In particular, answer the following questions:\
(a) What is the total kinetic energy of the system before and after the collision? How much of this energy is translational (that is, center-of-mass kinetic energy), and how much is convertible?\
(b) What kind of collision is this? (Elastic, inelastic, etc.) What is the coefficient of restitution?

### Problem 3 {#problem-3}

Analyze Problem 2 from Chapter 3 from the point of view of the system's kinetic energy. In particular, answer the following questions:\
(a) What is the coefficient of restitution for the collision described in part (a) of the problem, and how much kinetic energy is \"lost\" in that collision?\
(b) What is the coefficient of restitution for the collision described in part (b) of the problem, and how much kinetic energy is \"lost\" in that collision?

### Problem 4 {#problem-4}

A $0.012-\mathrm{kg}$ bullet, traveling at $850 \mathrm{~m} / \mathrm{s}$, hits a $2-\mathrm{kg}$ block of wood that is initially at rest, and goes straight through it. Assume that the final velocity of the bullet relative to the block is $400 \mathrm{~m} / \mathrm{s}$, and that the system is isolated.\
(a) What is the coefficient of restitution for this collision?\
(b) How much kinetic energy is \"lost\" in the collision?\
(c) What is the final velocity of the block?

### Problem 5 {#problem-5}

A 2-kg object, moving at $1 \mathrm{~m} / \mathrm{s}$, collides with a $1-\mathrm{kg}$ object that is initially at rest. Assume they form an isolated system.\
(a) What is the initial kinetic energy of the system? How much of this is center of mass energy, and how much is convertible?\
(b) What is the maximum amount of kinetic energy that could be \"lost\" (converted to other forms of energy) in this collision?\
(c) If $60 \%$ of the amount you calculated in part (b) is in fact converted into other forms of energy in the collision, what are the final velocities of the two objects?
