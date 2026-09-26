# Predictive Susceptibility

## How Sequence Learning Turns History into a Geometry of Possible Futures

**Antti Luode**  
Working paper · 26 September 2026

## Abstract

A learning system does not need to preserve its past as a record in order for the past to determine its future. Experience can instead alter the system so that some future perturbations are amplified, some suppressed, and some routed into different subsequent states. In this view, memory is not primarily stored information. It is **learned susceptibility**.

This paper develops that idea from a convergence between neuroscience, small computational experiments, and modern sequence models. A recent preprint reports that action-potential waveform is state-dependent: fine-scale spike shape varies systematically with recent input and local network state, and can contain information about input statistics extending hundreds of milliseconds into the past. The result does not establish a waveform-based neural code, but it makes the emitted neural event itself a plausible state-dependent component of coupling between dynamical systems.

Three exploratory computational projects expose complementary pieces of the same picture. **ResonaattoriAivo** shows that phase-based response geometry can continue learned sequences across large tempo changes, that prediction residue can identify novelty, and that retuning response geometry can rescue performance under state noise. **FridayRepo** shows that the useful effect of an event can depend multiplicatively on sender history and receiver state, and that when a future query is unknown the sender can learn to transmit not its entire history but approximately the missing coordinate the future receiver requires. **KapeaKanava** shows a more fundamental problem: generic sender and receiver networks can possess sufficient computational capacity yet fail to invent a useful communication protocol because neither side initially gives the other a learning gradient. A pre-existing multiplicative susceptibility largely removes this startup barrier.

Together these results motivate a broader hypothesis:

\[
\boxed{
\text{learning converts history into a geometry of possible responses}
}
\]

Sequence memory then becomes a trajectory through this geometry. Prediction becomes the tendency of the current state to make some futures easier to enter than others. Communication becomes the interaction between an emitted perturbation and the receiver's current susceptibility. Intelligence, on this account, does not arise from resonance alone. It arises where many learned sequences overlap, creating branching possible futures; where context selects among those futures; where the system can actively query its own uncertainty; and where prediction error reshapes the geometry itself.

This formulation also provides a common mathematical language for several successful forms of artificial intelligence. Transformer attention, associative memory, recurrent networks, and state-space models can all be interpreted as implementations of learned response geometry. Next-token prediction trains parameters not to preserve every training sequence literally, but to produce internal states from which appropriate future continuations become likely.

The proposal is therefore not that artificial intelligence is secretly implemented by biological resonance. It is more general:

\[
\boxed{
\textbf{biological resonance and modern sequence models may be different realizations of prediction by learned susceptibility.}
}
\]

The paper derives this statement, marks the boundary between evidence and speculation, and proposes experiments that can falsify it.

---

# 1. From the frozen wave to the frozen response

The motivating image is simple.

The world reaches an animal as temporal structure: light changes, pressure changes, sounds, movements, internal body signals, consequences of actions, other animals, and regularities occurring at many timescales. The nervous system is itself a physical dynamical object immersed in these processes.

Imagine that experience slowly changes this object until familiar temporal structures move it in characteristic ways.

At first this sounds like a claim that memory is stored in persistent resonance.

That cannot be the general answer.

A passive resonator loses energy. For a damped mode,

\[
a(t)=a_0 e^{-\gamma t}e^{i\omega t},
\]

the oscillation disappears.

The thing that can remain for years is not the ringing. It is the structure that determines how the system will ring when perturbed again.

That structure may include synaptic strengths, morphology, ion-channel distributions, recurrent couplings, dendritic nonlinearities, conduction delays, learned weights, or any other slowly changing parameter.

Let these collectively be

\[
\theta.
\]

Let the much faster current condition of the system be

\[
x_t.
\]

Then experience produces two very different kinds of memory:

\[
\boxed{
\text{slow memory}=\theta
}
\]

and

\[
\boxed{
\text{working/contextual memory}=x_t.
}
\]

The useful meaning of a “frozen wave” is therefore not an oscillation frozen in time.

It is a **frozen susceptibility**:

> a physical or mathematical structure shaped by previous events so that particular future temporal patterns, directions, combinations, or queries can move it particularly easily.

This distinction already appears in the trajectory of the recent experiments. The resonating state in ResonaattoriAivo was fragile under noise, while changing the response geometry itself recovered much of the lost performance. The broader lesson was not that a particular resonance frequency constitutes memory, but that the **shape of possible response** is plastic.

---

# 2. The ping does not have meaning by itself

Consider two dynamical systems.

The first is in state \(x_i\). It emits some event

\[
s_i = G_{\theta_i}(x_i).
\]

The second system is in state \(x_j\), with a response kernel or susceptibility

\[
h_j(\tau\mid x_j,\theta_j).
\]

A minimal temporal interaction is

\[
K_{ij}
=
\int
h_j(\tau\mid x_j,\theta_j)
\,s_i(\tau-\Delta t\mid x_i)
\,d\tau.
\]

The event therefore does not possess a fixed computational meaning.

Its effect depends jointly on:

\[
\text{sender state}
\times
\text{emitted event}
\times
\text{receiver state}
\times
\text{receiver structure}
\times
\text{timing}.
\]

A conventional fixed weight,

\[
y_j=w_{ij}x_i,
\]

is a restricted special case.

The deeper picture is:

\[
\boxed{
\text{meaning is an interaction between perturbation and susceptibility}.
}
\]

This is the central object of the paper.

It applies whether \(s_i\) is a biological action potential, an analog waveform, a vector, a token representation, a recurrent message, or an activation in an artificial network.

---

# 3. Why state-dependent action potentials matter

The biological motivation became more concrete with Martin-Burgos et al.'s 2026 preprint, *Action potential waveforms are state-dependent*.

The authors explicitly challenge the reduction of each action potential to a binary event. In high-temporal-resolution intracellular recordings, fine-scale waveform features varied systematically with input drive and with ongoing network state.

Under controlled stimulation, waveform features predicted which of three stimulation classes had driven the neuron with 78.4% accuracy against 33.3% chance. Under pink-noise stimulation, waveform features predicted recent current mean, variance and spectral exponent, with some effects extending several hundred milliseconds before the spike.

In a second dataset, 30 of 40 cells exhibited significant multimodality in at least one waveform feature. Waveform state was largely independent of simple inter-spike-interval state, and waveform features reflected aspects of the surrounding local field potential beyond firing interval alone. 

Most relevant to the present hypothesis, prior physiology reviewed in the paper establishes that changing the width or duration of a presynaptic action potential can alter the amplitude and duration of downstream excitatory postsynaptic currents.

The preprint therefore supports:

\[
\text{recent state}
\rightarrow
\text{event shape}
\]

and existing physiology supports, in at least some settings,

\[
\text{event shape}
\rightarrow
\text{different downstream effect}.
\]

It does **not** establish

\[
\text{waveform shape}
\rightarrow
\text{sequence-memory message}.
\]

That distinction is essential.

The data make the hypothesis experimentally legitimate. They do not establish it.

The intriguing possibility is instead that a biological event may participate in exactly the type of state-dependent coupling described above:

\[
x_i
\rightarrow
s_i(x_i)
\rightarrow
h_j(x_j)*s_i
\rightarrow
x_{j,t+1}.
\]

The ping carries traces of the sender.

The listener determines what those traces do.

---

# 4. Sequence memory need not be a tape

Suppose an animal experiences

\[
A\rightarrow B\rightarrow C\rightarrow D.
\]

The obvious memory representation is a chain.

\[
A\mapsto B,\quad
B\mapsto C,\quad
C\mapsto D.
\]

But a dynamical system permits another representation.

Event \(A\) changes the state of the system:

\[
x_t\overset{A}{\longrightarrow}x_{t+1}.
\]

That new state changes susceptibility.

Under this susceptibility, \(B\) is now easier to evoke than it was previously.

Then \(B\) moves the system again.

Thus:

\[
A
\overset{\Delta H}{\longrightarrow}
B
\overset{\Delta H}{\longrightarrow}
C
\overset{\Delta H}{\longrightarrow}
D.
\]

The sequence is not necessarily represented by a list of explicit links.

It can be represented by a trajectory through a changing response geometry.

\[
\boxed{
\text{sequence memory}
=
\text{trajectory through susceptibilities}.
}
\]

The distinction matters when memories overlap.

Suppose experience contains

\[
A,B,C,D
\]

and

\[
A,B,E,F
\]

and

\[
G,B,C,H.
\]

A tape-like memory contains three sequences.

A predictive dynamical memory must solve a different problem.

After \(B\), several transitions have historically been possible.

The relevant internal state therefore represents something like

\[
P(x_{t+1}\mid x_t,\text{context}).
\]

The memory has become a **branching surface of possible futures**.

This resembles the causal-state construction in computational mechanics: histories can be grouped according to whether they imply the same probability distribution over futures, producing a minimal predictive representation.

That provides a precise version of the intuition:

\[
\boxed{
\text{the useful summary of the past is whatever distinguishes possible futures}.
}
\]

Once histories are compressed this way, memory and prediction cease to be entirely separate functions.

Memory is the part of the past required to generate the future distribution.

---

# 5. ResonaattoriAivo: entering a sequence by rhythm

ResonaattoriAivo tested a small version of this idea using temporal phase.

A bank of damped resonators received musical sequences. Rather than representing tempo only in absolute milliseconds, the system used a phase-locked clock, allowing temporal location within a sequence to remain meaningful as tempo changed.

A model trained at one tempo retained roughly 94–95% next-beat accuracy across playback ranging from approximately \(0.6\times\) to \(1.6\times\) the training tempo. Freezing the clock at the training tempo largely destroyed this transfer.

After a 12-beat cue, the model could continue the sequence without further input with high accuracy.

This is a small but useful demonstration of:

\[
\boxed{
\text{recall as re-entry into an appropriate dynamical coordinate}.
}
\]

The important result is not that musical memory has been explained.

It is that absolute physical time need not be the coordinate in which temporal memory is easiest.

Phase can turn:

> “what happened 600 milliseconds ago?”

into:

> “what happened two positions earlier in this cycle?”

This is relevant to the familiar subjective phenomenon of recovering a forgotten sequence by reinstating part of its rhythm or preceding context. That subjective experience is not evidence for the mechanism. But the mechanism makes the phenomenon computationally intelligible.

ResonaattoriAivo also produced two important negative results.

First, its proposed slow-band context mechanism was initially unnecessary on the short junction task and became fragile under noise.

Second, the persistent memory did not reside in ongoing resonance itself.

The stronger result appeared when the response geometry was allowed to change. Under injected state noise, fixed geometry deteriorated substantially, whereas retuning a very small number of resonator parameters or a larger set of mode-to-unit couplings restored much of the performance.

So the experiment pushed the hypothesis away from:

\[
\text{memory}=\text{ongoing resonance}
\]

and toward:

\[
\boxed{
\text{memory}=\text{learned geometry determining future resonance}.
}
\]

---

# 6. FridayRepo: the sender should transmit what the future listener lacks

FridayRepo examined the interaction more directly.

Early experiments constructed tasks in which neither sender state nor receiver state was sufficient. The answer depended on their interaction.

When the architecture was given a multiplicative sender-emission × receiver-susceptibility form, learning recovered the hidden states from histories and solved the task while controls that removed either side collapsed toward chance.

But a generic recurrent network exposed an important escape route.

If it knew in advance which question would eventually be asked, it often computed the relevant interaction **before the nominal communication event occurred**.

The late ping was unnecessary.

This is a general lesson:

\[
\boxed{
\text{a learner will not preserve or communicate history merely because we intended it to}.
}
\]

If the eventual computation can be performed earlier, optimization may simply perform it earlier.

The stronger experiment therefore separated sender and receiver and withheld the eventual query until **after** the sender had already emitted its message.

Now the sender had to communicate something useful without knowing exactly how it would later be used.

The surprising result was compression.

The sender did not need to transmit a rich copy of its history. Even when wider communication channels were available, the learned message remained approximately one-dimensional and aligned almost perfectly with one hidden task direction. Destroying sender history severely degraded performance.

The emerging principle is:

\[
\boxed{
\text{communication need not transmit the past;}
}
\]

\[
\boxed{
\text{it need only transmit the part of the past the future listener cannot reconstruct}.
}
\]

Write sender history as \(H_s\), receiver context as \(C_r\), and future query as \(q\).

The naïve message is:

\[
m=f(H_s).
\]

The more interesting message is closer to:

\[
m=f(H_s\mid C_r,q_{\text{future distribution}}).
\]

That is a form of conditional predictive compression.

The transmitted object is not a memory dump.

It is a **historical residue**.

---

# 7. KapeaKanava: representation is not enough; learning needs a way in

KapeaKanava exposed an even more basic constraint.

Two learners were placed on opposite sides of a narrow noisy channel.

Each possessed private history. The correct answer depended on an interaction between sender history and receiver history. The channel width and task rank were systematically varied.

A receiver given an oracle message could solve the task.

The architecture therefore had sufficient representational capacity.

Yet generic sender/receiver pairs frequently failed to learn communication at all.

Why?

Near initialization, suppose the target contains only an interaction:

\[
y=f(H_s,H_r),
\]

with

\[
E[y\mid H_s]\approx0
\]

and

\[
E[y\mid H_r]\approx0.
\]

The sender's message by itself initially tells the receiver almost nothing.

The receiver therefore has little reason to become sensitive to variations in the message.

But if the receiver is insensitive, changing the sender's message also does not improve the loss.

Schematically,

\[
\nabla_{\text{sender}}L\approx0
\]

because the listener is deaf, while

\[
\nabla_{\text{listener}}L\approx0
\]

because the sender says nothing useful.

Each learner waits for the other.

This is a learning **startup barrier**.

A multiplicative receiver of the form

\[
r(H_r,m)
\sim
g(H_r)\odot m
\]

greatly improved startup.

The factorization was no longer something learning first had to invent. It was already represented in the listener's susceptibility.

KapeaKanava therefore distinguishes two questions that are often conflated:

1. **Can this architecture represent the solution?**
2. **Can learning reach the solution from its starting geometry?**

The answers can be:

\[
\text{yes}
\]

and

\[
\text{no}.
\]

This is one of the most important observations in the present theory.

\[
\boxed{
\text{initial susceptibility determines which computations are learnable}.
}
\]

The broader emergent-communication literature has encountered an analogous joint-exploration problem. Eccles et al. introduced explicit positive-signalling and positive-listening biases to make communication easier to discover.

KapeaKanava supplies a particularly simple dynamical interpretation:

> before a signal can acquire meaning, something on the receiving side must already be capable of hearing differences in it.

---

# 8. Why evolution might give the listener a head start

The startup result offers a computational reason for an old biological fact: animals are not born as arbitrary universal networks.

Evolution and development provide extensive prior structure.

That prior structure need not explicitly encode a representation of every future object.

Instead, it may define a family of useful susceptibilities.

In the present framework:

\[
\theta_0
\]

is not knowledge of a particular world.

It is an initial geometry from which ecologically useful learning can actually begin.

Lifetime learning then produces

\[
\theta_0
\rightarrow
\theta_1
\rightarrow
\theta_2
\rightarrow\cdots
\]

as experience assigns significance to the available dynamics.

This resembles Buzsáki's inside-out account, in which brain dynamics are substantially preconfigured and experience maps internally available trajectories onto useful meanings and consequences. His account explicitly emphasizes internally organized sequences and downstream reader mechanisms rather than treating the nervous system as a blank slate receiving externally defined representations.

The current proposal adds a learning argument:

\[
\boxed{
\text{preconfiguration may be necessary not only for efficiency,
but for gradient access}.
}
\]

A system with the wrong initial susceptibility may theoretically contain the desired computation somewhere in parameter space while having no practical learning path toward it.

KapeaKanava is far too small to establish this as a biological principle.

But it turns “innate structure” from a vague appeal to evolution into a precise computational question:

> Which initial response geometries make useful interactions discoverable by local learning?

---

# 9. From susceptibility to prediction

Why would evolution favor such a machine?

Because animals live in sequences.

A falling object continues falling.

A predator's movement predicts its next location.

A step changes the expected sensory state of the body.

A sound unfolds.

A social gesture predicts consequences.

An animal cannot wait for an event to finish before acting.

It must continually estimate:

\[
P(\text{future}\mid\text{past and present}).
\]

A susceptibility-based memory naturally performs this operation.

If past sequences have shaped the system so that state \(x_t\) makes one continuation easier than another, then merely evolving under its dynamics already constitutes a prediction.

The system does not have to consult a separate memory database and ask what occurred previously.

Its past has been compiled into its present dynamics.

\[
\boxed{
\text{prediction is memory expressed as dynamics}.
}
\]

This is the strongest meaning of the phrase **frozen sequence**.

The literal sequence is gone.

Its statistical consequences remain in how the system can move.

---

# 10. Prediction by cancellation

A prediction becomes particularly useful when it is compared against reality.

Let the system generate an expected sensory trajectory:

\[
\hat u_{t+1}.
\]

Reality supplies

\[
u_{t+1}.
\]

The discrepancy is

\[
e_{t+1}
=
u_{t+1}-\hat u_{t+1}.
\]

If prediction is good,

\[
e_{t+1}\approx0.
\]

Predictable reality becomes quiet.

Unexpected structure remains.

This general motif is established in predictive-coding models. Rao and Ballard, for example, modelled feedback as predictions and feed-forward activity as residual error between prediction and observed lower-level activity.

For the present theory, cancellation has a second role.

The residue tells the system where its susceptibility is wrong.

Thus the full cycle becomes:

\[
\boxed{
\text{susceptibility}
\rightarrow
\text{prediction}
\rightarrow
\text{residue}
\rightarrow
\text{updated susceptibility}.
}
\]

Or:

\[
\theta_t
\rightarrow
\hat u_{t+1}
\rightarrow
e_{t+1}
\rightarrow
\theta_{t+1}.
\]

This is learning as repeated conversation with the world.

The system speaks its current expectation through action or internal prediction.

The world replies.

The mismatch changes the system.

---

# 11. Where intelligence begins

A perfectly linear resonator is not enough.

For a linear system,

\[
R(A+B)=R(A)+R(B).
\]

It can recognize, filter, reconstruct and retrieve.

But no genuinely new interaction appears.

The recent projects repeatedly point toward a stronger mechanism:

\[
\boxed{
\text{the response geometry itself depends on state}.
}
\]

For example, modes \(a_i\) might interact through

\[
\dot a_k
=
(-\gamma_k+i\omega_k)a_k
+
\sum_{ij} C_{kij}a_i a_j
+
b_k u.
\]

Then:

\[
R(A+B)\neq R(A)+R(B).
\]

A combination can enter a dynamical region that neither component reaches alone.

This provides a natural hierarchy:

\[
\textbf{resonance}
\rightarrow
\text{recognition and retrieval},
\]

\[
\textbf{state-dependent susceptibility}
\rightarrow
\text{context and sequence},
\]

\[
\textbf{nonlinear interaction}
\rightarrow
\text{composition},
\]

\[
\textbf{plasticity driven by prediction error}
\rightarrow
\text{learning}.
\]

But even that is not yet a complete account of intelligence.

The difficult regime occurs at **junctions**.

Suppose the present state supports several historically plausible futures:

\[
x_t
\rightarrow
\{A,B,C,\ldots\}.
\]

Now the system must select.

Three operations become especially important.

### 11.1 Contextual selection

Which continuation fits the broader state?

### 11.2 Active querying

Which observation, internal probe, action or memory retrieval would best distinguish the alternatives?

### 11.3 Structural updating

When none of the existing continuations predicts reality well, how should the response geometry change?

These are candidate locations for intelligence because they transform a collection of remembered trajectories into adaptive behavior.

A resonator with one inevitable continuation is a playback machine.

A system whose state encodes a distribution over futures, seeks information when uncertain, and changes itself when surprised is something more.

---

# 12. The same abstraction appears inside modern AI

The hypothesis does **not** require claiming that artificial neural networks historically derive from biological resonance.

They do not.

But surprisingly much modern AI can be written in the same mathematical language.

## 12.1 Transformer attention as susceptibility

For a Transformer token state \(x_j\), define

\[
q_j=W_Qx_j.
\]

For another token \(x_i\),

\[
k_i=W_Kx_i.
\]

Their interaction is proportional to

\[
q_j^\top k_i.
\]

This can be read as:

\[
\boxed{
\text{effect}
=
\langle
\text{listener},
\text{incoming pattern}
\rangle.
}
\]

Compare this with a temporal matched filter:

\[
K_{ij}
=
\int
h_j(\tau)s_i(\tau)d\tau.
\]

One is an inner product in learned vector coordinates.

The other is an inner product in a function space over time.

The computational motif is the same.

The incoming item does not determine its own significance.

Its significance depends on the query—the current susceptibility of the reader.

The equivalence between modern Hopfield associative-memory updates and Transformer attention makes this relationship particularly explicit: attention can itself be interpreted as a learned associative retrieval operation.

## 12.2 Recurrent networks

For an RNN,

\[
x_{t+1}=F_\theta(x_t,u_t).
\]

The effect of \(u_t\) already depends on \(x_t\).

Every recurrent model therefore implements a primitive form of state-dependent susceptibility.

The important question is not whether recurrence possesses this mathematical property.

It does.

The question is what learning makes the geometry represent.

## 12.3 State-space models

A continuous state-space model begins with

\[
\dot x=Ax+Bu,
\qquad
y=Cx+Du.
\]

The eigenstructure of \(A\) determines characteristic temporal modes and decay rates.

This is already extremely close to a bank of learned temporal susceptibilities.

S4 showed that structured state-space systems can be turned into powerful long-sequence learners by carefully parameterizing this dynamics.

Mamba then made the connection more relevant still: important state-space parameters become functions of the current input, permitting selective propagation or forgetting depending on what arrives.

That is, in different language,

\[
\text{current event}
\rightarrow
\text{changed susceptibility}.
\]

## 12.4 Next-token prediction

A language model is trained approximately by minimizing

\[
L(\theta)
=
-\sum_t
\log
P_\theta(w_{t+1}\mid w_{\le t}).
\]

This objective asks one question billions or trillions of times:

> Given this past, what comes next?

Training changes \(\theta\).

After training, \(\theta\) is a structure through which previously unseen sequences produce useful distributions over possible continuations.

Thus:

\[
\text{many past sequences}
\rightarrow
\theta
\rightarrow
P_\theta(\text{possible future}\mid\text{new history}).
\]

This is almost exactly the abstract mechanism proposed here.

The training corpus is not preserved simply as a collection of tapes.

The statistical structure of sequences becomes embodied in how the network responds.

In that abstract sense:

\[
\boxed{
\text{weights are frozen consequences of past sequences}.
}
\]

And inference is:

\[
\boxed{
\text{a new sequence moving through that frozen response geometry}.
}
\]

---

# 13. A proposed common abstraction

We can now state the complete model without committing to neurons, oscillators or Transformers.

Let:

- \(\theta_t\) denote slowly changing learned structure;
- \(x_t\) denote fast current state;
- \(u_t\) denote an incoming perturbation;
- \(s_t\) denote an event emitted by the current state;
- \(H_{\theta}(x)\) denote state-dependent susceptibility;
- \(\hat u_{t+1}\) denote predicted future input.

Emission:

\[
s_t=G_{\theta_t}(x_t).
\]

Reception:

\[
r_t
=
H_{\theta_t}(x_t)[s_t,u_t].
\]

State evolution:

\[
x_{t+1}
=
F_{\theta_t}(x_t,r_t).
\]

Prediction:

\[
\hat u_{t+1}
=
P_{\theta_t}(x_{t+1}).
\]

Error:

\[
e_{t+1}
=
u_{t+1}-\hat u_{t+1}.
\]

Slow learning:

\[
\theta_{t+1}
=
\theta_t
+
\eta\,\Phi(e_{t+1},x_t,x_{t+1},u_t).
\]

The essential loop is:

\[
\boxed{
(\theta_t,x_t)
\rightarrow
\text{susceptibility}
\rightarrow
\text{interaction}
\rightarrow
x_{t+1}
\rightarrow
\text{prediction}
\rightarrow
\text{error}
\rightarrow
\theta_{t+1}.
}
\]

History therefore exists in two compiled forms.

Fast recent history:

\[
H_{\text{recent}}
\rightarrow x_t.
\]

Long accumulated history:

\[
H_{\text{long}}
\rightarrow\theta_t.
\]

Neither must contain an explicit record of the events that created it.

They need only preserve distinctions relevant to possible futures.

---

# 14. Predictive susceptibility

This suggests a definition.

> **Predictive susceptibility is the learned, state-dependent tendency of a dynamical system to respond differently to perturbations according to the futures those perturbations imply.**

Memory is then:

\[
\boxed{
\text{history compiled into predictive susceptibility}.
}
\]

Recall is:

\[
\boxed{
\text{a probe entering the region of state space where an old continuation becomes likely}.
}
\]

Communication is:

\[
\boxed{
\text{a perturbation whose useful effect exists only relative to a listener}.
}
\]

Prediction is:

\[
\boxed{
\text{the future toward which current susceptibility most readily evolves}.
}
\]

Surprise is:

\[
\boxed{
\text{the component of reality not absorbed by current susceptibility}.
}
\]

Learning is:

\[
\boxed{
\text{surprise reshaping susceptibility}.
}
\]

And intelligence may be:

\[
\boxed{
\text{the adaptive management of branching possible futures}.
}
\]

---

# 15. Why many memories can become more than many memories

This final point is the one that motivated the present paper.

Suppose an organism contains thousands of independent sequence memories.

That is useful.

But suppose those memories instead share a response geometry.

Now states encountered in many different sequences overlap.

At each shared state, multiple continuations coexist.

The system has automatically constructed a graph—or more accurately a manifold—of possible futures.

A novel trajectory can then be produced without having been stored whole.

Parts of old trajectories can be recombined because they pass through compatible predictive states.

Thus:

\[
\text{experience}_1
+
\text{experience}_2
+
\cdots
+
\text{experience}_n
\]

does not merely produce

\[
n\text{ memories}.
\]

It can produce:

\[
\boxed{
\text{a reusable geometry of possible worlds}.
}
\]

That is a plausible bridge from memory to flexible intelligence.

The same mechanism creates its own danger.

When several histories collapse into one predictive state, detail is lost.

When too many incompatible continuations occupy the same region, interference grows.

So abstraction and forgetting may be two sides of the same operation.

The system discards differences in the past that no longer change its prediction of the future.

That is not necessarily memory failure.

It may be the computation.

---

# 16. Falsifiable predictions

A useful theory must risk failure.

The predictive-susceptibility account makes several testable predictions.

## Prediction 1: same event, different listener state

Hold an emitted event and its timing fixed.

Place the receiver in two different hidden states.

The downstream result should differ when the task requires history-dependent interaction.

If receiver state does not matter, the strong coupling claim fails.

## Prediction 2: same timing, different event shape

Create events with identical timing and tightly controlled gross properties but different fine temporal shape.

If the receiver has learned shape-sensitive susceptibility, these events should produce different continuations.

Shuffling event shape between histories while preserving timing should impair performance.

This is the direct computational experiment suggested by the state-dependent-waveform preprint.

## Prediction 3: identical present, different hidden history

Construct two trials with:

\[
u_t^{(1)}=u_t^{(2)}
\]

and identical present observable state, but different earlier histories.

A successful history-compiled system should produce different responses if those histories imply different futures.

This connects predictive susceptibility to the earlier HistoryCompiler criterion.

## Prediction 4: listener-first learning

Use one fixed task and manipulate only the curriculum.

Condition A first teaches the receiver that incoming signals must be interpreted jointly with receiver state.

Condition B first teaches the receiver a state-independent shortcut.

Then introduce an identical history-dependent communication problem.

The theory predicts:

\[
\text{A}
>
\text{B}
\]

for successful emergence of historical communication.

This is the clean controlled experiment currently missing between FridayRepo and KapeaKanava.

## Prediction 5: predictive-state clustering

Generate many different histories, deliberately arranging some to imply the same future distribution.

After training a sequence learner, compare representational similarity.

The theory predicts that sufficiently compressed internal states should cluster more strongly by:

\[
P(\text{future}\mid\text{history})
\]

than by literal similarity of the histories themselves.

## Prediction 6: temporal susceptibility should aid time warps

On tasks where relevant structure is defined by relative phase rather than absolute duration, a model whose memory coordinate explicitly follows phase should generalize better to untrained speed transformations than a comparably sized model whose representation is tied to absolute time.

ResonaattoriAivo is an initial toy demonstration, not a general result.

## Prediction 7: novelty should preferentially alter the geometry that caused the prediction

If prediction residue is the learning signal, perturbations associated with systematic errors should reshape the relevant susceptibility more strongly than already-predicted events.

---

# 17. What would falsify the biological version?

Several outcomes would substantially weaken the biological interpretation.

First, state-dependent somatic action-potential waveform variation may prove largely irrelevant to downstream targets. The 2026 preprint demonstrates state dependence, not a functional sequence code.

Second, biologically realistic receiving neurons may fail to extract any useful historical variable from plausible waveform differences once axonal propagation, synaptic noise and population variability are included.

Third, temporal susceptibility may prove adequately explained by conventional spike timing, synaptic weights and network recurrence, with fine waveform carrying no additional computational advantage.

Fourth, the listener-first effect observed in the toy systems may disappear under architecture- and task-matched experiments.

Fifth, predictive-state compression may be too generic a description to explain anything uniquely. Almost any recurrent learner can be described as history changing future response. The theory earns value only if its specific decomposition—state-dependent emission, state-dependent reception, startup constraints, predictive compression and error-driven geometry—produces distinctive empirical predictions.

---

# 18. What this paper does not claim

This paper does **not** claim that:

- neurons literally contain permanent standing waves;
- action-potential waveform is proven to encode long-term memories;
- chandelier cells are sequence-release switches;
- basket cells constitute a complete gamma clock;
- the brain is a Transformer;
- Transformer attention evolved from neuronal resonance;
- next-token prediction explains biological intelligence;
- ResonaattoriAivo, FridayRepo or KapeaKanava establish a theory of cognition;
- prediction alone is sufficient for intelligence.

The stronger and more defensible statement is narrower:

\[
\boxed{
\text{learning can be viewed as converting histories into state-dependent response geometry}.
}
\]

Once that transformation has occurred, apparently different mechanisms—resonance, recurrence, attention, associative retrieval and state-space dynamics—can all perform computation by allowing new events to act on the learned geometry.

---

# 19. Discussion

The original image was a brain catching a world that arrives in waves.

The useful part of that image survives, but in a different form.

The brain need not preserve those waves.

The waves can disappear.

What remains is what they have done to the thing that received them.

A dendrite may become differently excitable.

A synapse may strengthen.

A channel distribution may change.

A circuit may develop a trajectory.

An artificial weight matrix may rotate.

An attention head may acquire a query-key geometry.

A state-space model may acquire modes with useful decay constants.

A language model may acquire an internal state from which one continuation is enormously more probable than another.

In every case:

\[
\text{past interaction}
\rightarrow
\text{changed future response}.
\]

That is memory at its most abstract.

But sequence learning adds something important.

The future response is not arbitrary.

It becomes shaped by the regularities of what historically came next.

The system therefore slowly becomes an approximation to the temporal structure of its environment.

Not a photographic model of the universe.

Not a database containing the universe.

A machine whose **possible motions increasingly resemble possible motions of the world**.

In this sense the phrase “inverse model of the universe” can be replaced by something more precise:

\[
\boxed{
\text{the learner becomes a predictive dynamical complement to its environment}.
}
\]

Its structure embodies what usually follows.

Its activity proposes what follows now.

Its errors mark where the proposal failed.

Its plasticity changes what it will propose next time.

---

# 20. Conclusion

The central proposal can be written in one line:

\[
\boxed{
\textbf{history becomes susceptibility; susceptibility generates possible futures.}
}
\]

A physical resonator is one possible implementation.

A recurrent network is another.

Attention implements a learned match between an incoming representation and the current query.

State-space models explicitly construct temporal response dynamics.

Prediction training reshapes all of them according to regularities in sequences.

This does not make these systems equivalent.

It identifies a common computational object beneath them.

The most interesting consequence concerns intelligence.

If every remembered sequence remained isolated, memory would be a collection of recordings.

But when many sequences modify one shared response geometry, their overlaps create branching possible futures. The system can generalize, recombine, predict, query uncertainty, and change itself when reality follows none of the expected paths.

The past has disappeared as a literal event.

Yet it remains present everywhere in what can happen next.

That is predictive susceptibility.

---

## Evidence ledger

### Established or externally supported

- Action-potential waveform varies systematically with recent input and network state; the cited 2026 result is currently a bioRxiv preprint rather than peer-reviewed work.
- Presynaptic action-potential shape can affect synaptic output in established preparations.
- Predictive coding can formulate feed-forward activity as residual error relative to feedback predictions.
- Internally generated neural trajectories and preconfigured dynamics are established theoretical and empirical research programs, though strong claims about specific preplay phenomena remain contested.
- Transformer attention has an exact mathematical relationship to modern Hopfield associative-memory updates.
- Structured and selective state-space models are successful sequence-model architectures.
- Emergent communication can exhibit a joint exploration/startup problem and benefit from signalling/listening biases.

### Measured in the exploratory repositories

- ResonaattoriAivo: phase-based tempo transfer, free continuation after cueing, prediction residue as novelty signal, noise fragility, and recovery from plastic response geometry.
- FridayRepo: sender-state × receiver-state coupling, early precomputation when the future question is known, and compressed historical communication when the query arrives later.
- KapeaKanava: generic communication startup failure despite adequate receiver capacity, improvement from an explicitly multiplicative listener, rank-bound behavior when communication starts, and shortcut capture of the channel in its original attacker.

### Proposed here

- **Predictive susceptibility** as a common abstraction joining slow memory, fast context, communication, prediction and learning.
- Sequence memories as trajectories through susceptibility rather than necessarily stored chains.
- Communication as the conditional historical residue the future listener cannot reconstruct itself.
- Evolutionary/developmental priors as possible solutions to a communication/interaction startup problem.
- Flexible intelligence as management of branching futures produced when many learned sequences share one response geometry.
- Biological resonance and modern AI sequence computation as distinct physical/mathematical realizations of the same higher-level computational pattern.

---

## References

Buzsáki, G. (2019). *The Brain from Inside Out*. Oxford University Press.

Dragoi, G., & Tonegawa, S. (2011). Preplay of future place cell sequences by hippocampal cellular assemblies. *Nature*, 469, 397–401.

Eccles, T., Bachrach, Y., Lever, G., Lazaridou, A., & Graepel, T. (2019). Biases for emergent communication in multi-agent reinforcement learning.

Gu, A., Goel, K., & Ré, C. (2021). Efficiently modeling long sequences with structured state spaces.

Gu, A., & Dao, T. (2023). Mamba: Linear-time sequence modeling with selective state spaces.

Martin-Burgos, B., Juavinett, A., Rivière, P. D., Hammonds, R., & Voytek, B. (2026). Action potential waveforms are state-dependent. *bioRxiv*, 2026.09.15.751814.

Ramsauer, H., et al. (2020). Hopfield Networks is All You Need.

Rao, R. P. N., & Ballard, D. H. (1999). Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience*, 2, 79–87.

Shalizi, C. R., & Crutchfield, J. P. (2001; preprint 1999). Computational mechanics: Pattern and prediction, structure and simplicity. *Journal of Statistical Physics*, 104, 817–879.

Luode, A. (2026). *ResonaattoriAivo*. Exploratory software repository.

Luode, A. (2026). *FridayRepo*. Exploratory software repository.

Luode, A. (2026). *KapeaKanava*. Exploratory software repository.

Luode, A. (2026). *The Ping and the Listener*. Working paper and exploratory synthesis.
