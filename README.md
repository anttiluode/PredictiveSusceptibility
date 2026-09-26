# Predictive Susceptibility

## How Sequence Learning Turns History into a Geometry of Possible Futures

**Antti Luode**  
Working paper · 26 September 2026

---

## Abstract

A learning system does not need to preserve its past as a literal record for the past to determine its future.

Experience can instead alter the system so that some future perturbations are amplified, some suppressed, and some routed into different subsequent states.

In this view:

> **Memory is not primarily stored information. Memory is learned susceptibility.**

This paper develops that idea from a convergence between neuroscience, small computational experiments, and modern sequence models.

A recent preprint, *Action potential waveforms are state-dependent* (Martin-Burgos et al., 2026), reports that fine-scale action-potential waveform varies systematically with recent input and local network state. The result does **not** establish a waveform-based neural memory code, but it makes the emitted neural event itself a plausible state-dependent component of coupling between dynamical systems.

Three exploratory computational projects expose complementary pieces of the same picture:

- [`ResonaattoriAivo`](https://github.com/anttiluode/ResonaattoriAivo) shows that phase-based response geometry can continue learned sequences across large tempo changes, that prediction residue can identify novelty, and that retuning response geometry can rescue performance under state noise.
- [`FridayRepo`](https://github.com/anttiluode/FridayRepo) shows that the useful effect of an event can depend multiplicatively on sender history and receiver state, and that when a future query is unknown the sender can learn to transmit not its whole history but approximately the missing coordinate the future receiver requires.
- [`KapeaKanava`](https://github.com/anttiluode/KapeaKanava) shows a more fundamental problem: generic sender and receiver networks can possess sufficient computational capacity yet fail to invent a useful communication protocol because neither side initially gives the other a learning gradient. A pre-existing multiplicative susceptibility largely removes this startup barrier.

Together these results motivate a broader hypothesis:

$$
\boxed{
\text{learning converts history into a geometry of possible responses}
}
$$

Sequence memory then becomes a trajectory through this geometry.

Prediction becomes the tendency of the current state to make some futures easier to enter than others.

Communication becomes the interaction between an emitted perturbation and the receiver's current susceptibility.

Intelligence, on this account, does not arise from resonance alone. It arises where many learned sequences overlap, creating branching possible futures; where context selects among those futures; where the system can actively query uncertainty; and where prediction error reshapes the geometry itself.

The proposal is **not** that artificial intelligence is secretly implemented by biological resonance.

It is more general:

$$
\boxed{
\textbf{
biological resonance and modern sequence models may be different realizations
of prediction by learned susceptibility
}
}
$$

---

# 1. From the Frozen Wave to the Frozen Response

The motivating image is simple.

The world reaches an animal as temporal structure:

- light changes,
- pressure changes,
- sounds,
- movements,
- internal body signals,
- consequences of actions,
- other animals,
- and regularities occurring at many timescales.

The nervous system is itself a physical dynamical object immersed in these processes.

Imagine that experience slowly changes this object until familiar temporal structures move it in characteristic ways.

At first this sounds like a claim that memory is stored in persistent resonance.

That cannot be the general answer.

A passive resonator loses energy. For a damped mode,

$$
a(t)=a_0 e^{-\gamma t}e^{i\omega t},
$$

the oscillation disappears.

The thing that can remain for years is not the ringing.

It is the structure that determines how the system will ring when perturbed again.

That structure may include:

- synaptic strengths,
- morphology,
- ion-channel distributions,
- recurrent couplings,
- dendritic nonlinearities,
- conduction delays,
- learned weights,
- or any other slowly changing parameter.

Let these collectively be

$$
\theta.
$$

Let the much faster current condition of the system be

$$
x_t.
$$

Then experience produces two different forms of memory:

$$
\boxed{
\text{slow memory}=\theta
}
$$

and

$$
\boxed{
\text{fast contextual memory}=x_t.
}
$$

The useful meaning of a **frozen wave** is therefore not an oscillation frozen in time.

It is a **frozen susceptibility**:

> A physical or mathematical structure shaped by previous events so that particular future temporal patterns, directions, combinations, or queries can move it particularly easily.

The vibrating state is the reader.

The response geometry is what lasts.

---

# 2. The Ping Does Not Have Meaning by Itself

Consider two dynamical systems.

The first is in state \(x_i\). It emits some event

$$
s_i=G_{\theta_i}(x_i).
$$

The second system is in state \(x_j\), with a response kernel or susceptibility

$$
h_j(\tau\mid x_j,\theta_j).
$$

A minimal temporal interaction is

$$
K_{ij}(x_i,x_j,\Delta t)
=
\int
h_j(\tau\mid x_j,\theta_j)
\,s_i(\tau-\Delta t\mid x_i)
\,d\tau.
$$

The event therefore does not possess a fixed computational meaning.

Its effect depends jointly on:

$$
\text{sender state}
\times
\text{emitted event}
\times
\text{receiver state}
\times
\text{receiver structure}
\times
\text{timing}.
$$

A conventional fixed weight,

$$
y_j=w_{ij}x_i,
$$

is a restricted special case.

The deeper picture is:

$$
\boxed{
\text{meaning is an interaction between perturbation and susceptibility}
}
$$

This is the central object of the paper.

It applies whether \(s_i\) is:

- a biological action potential,
- an analog waveform,
- a vector,
- a token representation,
- a recurrent message,
- or an activation in an artificial network.

---

# 3. Why State-Dependent Action Potentials Matter

The biological motivation became more concrete with the 2026 preprint:

> **Martin-Burgos et al. — *Action potential waveforms are state-dependent***

The authors report that fine-scale action-potential shape varies systematically with recent input and with ongoing network state.

Among the reported results:

- waveform features distinguished stimulation conditions,
- waveform features predicted properties of recent pink-noise input,
- some effects reflected input extending hundreds of milliseconds before the spike,
- many cells exhibited multimodal waveform states,
- waveform state was largely independent of simple firing-interval state,
- and waveform features reflected aspects of the surrounding local field potential beyond firing interval alone.

Most relevant to the present hypothesis, earlier physiology discussed in the paper shows that changing presynaptic action-potential width or duration can alter downstream postsynaptic currents.

The biological evidence therefore supports two pieces:

$$
\text{recent state}
\rightarrow
\text{event shape}
$$

and, in at least some preparations,

$$
\text{event shape}
\rightarrow
\text{different downstream effect}.
$$

It does **not** establish:

$$
\text{waveform shape}
\rightarrow
\text{sequence-memory message}.
$$

That distinction matters.

The paper makes the hypothesis experimentally legitimate.

It does not prove it.

The possibility is instead that a biological event may participate in a state-dependent coupling of the form

$$
x_i
\rightarrow
s_i(x_i)
\rightarrow
h_j(x_j)*s_i
\rightarrow
x_{j,t+1}.
$$

The ping carries traces of the sender.

The listener determines what those traces do.

---

# 4. Sequence Memory Need Not Be a Tape

Suppose an animal experiences:

$$
A\rightarrow B\rightarrow C\rightarrow D.
$$

The obvious memory representation is a chain:

$$
A\mapsto B,\qquad
B\mapsto C,\qquad
C\mapsto D.
$$

But a dynamical system permits another representation.

Event \(A\) changes the state:

$$
x_t\overset{A}{\longrightarrow}x_{t+1}.
$$

That state changes susceptibility.

Under the new susceptibility, \(B\) is now easier to evoke than it was before.

Then \(B\) changes the state again.

Thus:

$$
A
\overset{\Delta H}{\longrightarrow}
B
\overset{\Delta H}{\longrightarrow}
C
\overset{\Delta H}{\longrightarrow}
D.
$$

The sequence is not necessarily represented by a list of explicit links.

It can be represented by a trajectory through a changing response geometry.

$$
\boxed{
\text{sequence memory}
=
\text{trajectory through susceptibilities}
}
$$

The distinction matters when memories overlap.

Suppose experience contains:

$$
A,B,C,D
$$

$$
A,B,E,F
$$

$$
G,B,C,H.
$$

A tape-like memory contains three sequences.

A predictive dynamical memory faces a different problem.

After \(B\), several transitions have historically been possible.

The relevant state therefore represents something closer to

$$
P(x_{t+1}\mid x_t,\text{context}).
$$

The memory has become a **branching surface of possible futures**.

This gives a more precise version of the intuition:

$$
\boxed{
\text{the useful summary of the past is whatever distinguishes possible futures}
}
$$

Once histories are compressed this way, memory and prediction stop being separate functions.

Memory becomes the part of the past required to generate the future distribution.

---

# 5. ResonaattoriAivo: Entering a Sequence by Rhythm

[`ResonaattoriAivo`](https://github.com/anttiluode/ResonaattoriAivo) tested a small version of this idea using temporal phase.

A bank of damped resonators received musical sequences. Rather than representing tempo only in absolute milliseconds, the system used a phase-locked clock.

This allowed temporal location inside a sequence to remain meaningful as tempo changed.

A model trained at one tempo retained roughly **94–95% next-beat accuracy** across playback ranging from approximately **0.6× to 1.6×** the training tempo.

Freezing the clock at the training tempo largely destroyed this transfer.

After a 12-beat cue, the model could continue the sequence without further input with high accuracy.

This is a small but useful demonstration of:

$$
\boxed{
\text{recall as re-entry into an appropriate dynamical coordinate}
}
$$

Absolute physical time need not be the coordinate in which temporal memory is easiest.

Phase can turn:

> What happened 600 milliseconds ago?

into:

> What happened two positions earlier in this cycle?

The experiment also produced important negative results.

The proposed slow-band context mechanism was initially unnecessary on a short junction task and became fragile under noise.

More importantly, persistent memory did not reside in ongoing resonance itself.

The stronger result appeared when the **response geometry** was allowed to change.

Under injected state noise, fixed geometry deteriorated substantially. Retuning a small number of resonator parameters or a larger set of mode-to-unit couplings restored much of the lost performance.

The experiment therefore pushed the hypothesis away from

$$
\text{memory}=\text{ongoing resonance}
$$

and toward

$$
\boxed{
\text{memory}=\text{learned geometry determining future resonance}
}
$$

---

# 6. FridayRepo: Transmit What the Future Listener Lacks

[`FridayRepo`](https://github.com/anttiluode/FridayRepo) examined the interaction more directly.

Early experiments constructed tasks in which neither sender state nor receiver state was sufficient.

The answer depended on their interaction.

When the architecture was given a multiplicative sender-emission × receiver-susceptibility form, learning recovered the hidden states from histories and solved the task while controls that removed either side collapsed toward chance.

But a generic recurrent network exposed an escape route.

If it knew in advance which question would eventually be asked, it often computed the relevant interaction **before the nominal communication event occurred**.

The late ping became unnecessary.

This gives a general lesson:

$$
\boxed{
\text{a learner will not preserve or communicate history merely because we intended it to}
}
$$

If the eventual computation can be performed earlier, optimization may simply perform it earlier.

The stronger experiment separated sender and receiver and withheld the eventual query until **after** the sender had already emitted its message.

Now the sender had to communicate something useful without knowing exactly how it would later be used.

The surprising result was compression.

The sender did not need to transmit a rich copy of its history.

Even when wider communication channels were available, the learned message remained approximately one-dimensional and aligned very strongly with one hidden task direction.

The emerging principle is:

$$
\boxed{
\text{communication need not transmit the past}
}
$$

It may only need to transmit:

$$
\boxed{
\text{the part of the past the future listener cannot reconstruct}
}
$$

Write sender history as \(H_s\), receiver context as \(C_r\), and the eventual query as \(q\).

The naïve message is

$$
m=f(H_s).
$$

The more interesting message is closer to

$$
m=f(H_s\mid C_r,q_{\text{future distribution}}).
$$

The transmitted object is not a memory dump.

It is a **historical residue**.

---

# 7. KapeaKanava: Representation Is Not Enough

[`KapeaKanava`](https://github.com/anttiluode/KapeaKanava) exposed an even more basic constraint.

Two learners were placed on opposite sides of a narrow noisy channel.

Each possessed private history.

The correct answer depended on an interaction between sender history and receiver history.

A receiver given a perfect message could solve the task.

The architecture therefore had sufficient representational capacity.

Yet generic sender/receiver pairs frequently failed to learn communication at all.

Why?

Suppose the target contains only an interaction:

$$
y=f(H_s,H_r),
$$

while

$$
E[y\mid H_s]\approx0
$$

and

$$
E[y\mid H_r]\approx0.
$$

The sender's message by itself initially tells the receiver almost nothing.

The receiver therefore has little reason to become sensitive to variations in the message.

But if the receiver is insensitive, changing the sender's message also does not improve the loss.

Schematically,

$$
\nabla_{\text{sender}}L\approx0
$$

because the listener is deaf, while

$$
\nabla_{\text{listener}}L\approx0
$$

because the sender says nothing useful.

Each learner waits for the other.

This is a **startup barrier**.

A multiplicative receiver of the form

$$
r(H_r,m)\sim g(H_r)\odot m
$$

greatly improved startup.

The factorization was no longer something learning first had to invent.

It was already represented in the listener's susceptibility.

KapeaKanava therefore distinguishes two questions that are often conflated:

1. Can this architecture represent the solution?
2. Can learning reach the solution from its starting geometry?

The answers can be:

$$
\text{yes}
$$

and

$$
\text{no}.
$$

This suggests:

$$
\boxed{
\text{initial susceptibility determines which computations are learnable}
}
$$

That may be one reason biological systems do not begin as blank universal learners.

---

# 8. Why Evolution Might Give the Listener a Head Start

Animals are not born as arbitrary neural networks.

Evolution and development provide extensive prior structure.

That structure need not encode a representation of every future object.

It may instead define a useful family of susceptibilities.

Let the initial system be

$$
\theta_0.
$$

Lifetime learning then produces

$$
\theta_0
\rightarrow
\theta_1
\rightarrow
\theta_2
\rightarrow\cdots
$$

as experience assigns significance to the available dynamics.

The present proposal adds a learning argument:

$$
\boxed{
\text{preconfiguration may be necessary not only for efficiency, but for gradient access}
}
$$

A system with the wrong initial susceptibility may theoretically contain the desired computation somewhere in parameter space while having no practical learning path toward it.

KapeaKanava is far too small to establish this as a biological principle.

But it turns innate structure into a precise computational question:

> Which initial response geometries make useful interactions discoverable by learning?

---

# 9. Memory as Prediction

Why would evolution favor such a machine?

Because animals live in sequences.

A falling object continues falling.

A predator's movement predicts its next location.

A step changes the expected sensory state of the body.

A sound unfolds.

A social gesture predicts consequences.

An animal cannot wait for an event to finish before acting.

It must continually estimate

$$
P(\text{future}\mid\text{past and present}).
$$

A susceptibility-based memory naturally performs this operation.

If past sequences have shaped the system so that state \(x_t\) makes one continuation easier than another, then merely evolving under its dynamics already constitutes a prediction.

The system does not need to consult a separate memory database.

Its past has been compiled into its present dynamics.

$$
\boxed{
\text{prediction is memory expressed as dynamics}
}
$$

This is the strongest meaning of the phrase **frozen sequence**.

The literal sequence is gone.

Its statistical consequences remain in how the system can move.

---

# 10. Prediction by Cancellation

A prediction becomes especially useful when compared against reality.

Let the system generate an expected sensory trajectory:

$$
\hat u_{t+1}.
$$

Reality supplies

$$
u_{t+1}.
$$

The discrepancy is

$$
e_{t+1}=u_{t+1}-\hat u_{t+1}.
$$

If prediction is good,

$$
e_{t+1}\approx0.
$$

Predictable reality becomes quiet.

Unexpected structure remains.

For the present theory, cancellation has a second role.

The residue tells the system where its susceptibility is wrong.

Thus the full cycle becomes:

$$
\boxed{
\text{susceptibility}
\rightarrow
\text{prediction}
\rightarrow
\text{residue}
\rightarrow
\text{updated susceptibility}
}
$$

or

$$
\theta_t
\rightarrow
\hat u_{t+1}
\rightarrow
e_{t+1}
\rightarrow
\theta_{t+1}.
$$

This is learning as repeated conversation with the world.

The system expresses its current expectation.

The world answers.

The mismatch changes the system.

---

# 11. Where Intelligence Begins

A perfectly linear resonator is not enough.

For a linear system,

$$
R(A+B)=R(A)+R(B).
$$

It can recognize, filter, reconstruct and retrieve.

But no genuinely new interaction appears.

The recent projects repeatedly point toward a stronger mechanism:

$$
\boxed{
\text{the response geometry itself depends on state}
}
$$

For example,

$$
\dot a_k
=
(-\gamma_k+i\omega_k)a_k
+
\sum_{ij}C_{kij}a_i a_j
+
b_k u.
$$

Then

$$
R(A+B)\neq R(A)+R(B).
$$

A combination can enter a dynamical region that neither component reaches alone.

This suggests a hierarchy:

$$
\textbf{resonance}
\rightarrow
\text{recognition and retrieval}
$$

$$
\textbf{state-dependent susceptibility}
\rightarrow
\text{context and sequence}
$$

$$
\textbf{nonlinear interaction}
\rightarrow
\text{composition}
$$

$$
\textbf{prediction-error-driven plasticity}
\rightarrow
\text{learning}
$$

But even that is not a complete account of intelligence.

The difficult regime occurs at **junctions**.

Suppose the present state supports several plausible futures:

$$
x_t
\rightarrow
\{A,B,C,\ldots\}.
$$

Now the system must select.

Three operations become especially important.

### 11.1 Contextual selection

Which continuation fits the broader state?

### 11.2 Active querying

Which observation, internal probe, action, or memory retrieval would best distinguish the alternatives?

### 11.3 Structural updating

When none of the existing continuations predicts reality well, how should the response geometry change?

A resonator with one inevitable continuation is a playback machine.

A system whose state encodes a distribution over futures, seeks information when uncertain, and changes itself when surprised is something more.

---

# 12. The Same Abstraction Appears in Modern AI

The hypothesis does **not** require claiming that artificial neural networks historically derive from biological resonance.

They do not.

But surprisingly much modern AI can be written in the same mathematical language.

## 12.1 Transformer Attention as Susceptibility

For a Transformer token state \(x_j\), define

$$
q_j=W_Qx_j.
$$

For another token \(x_i\),

$$
k_i=W_Kx_i.
$$

Their interaction is proportional to

$$
q_j^\top k_i.
$$

This can be read as

$$
\boxed{
\text{effect}
=
\langle
\text{listener},
\text{incoming pattern}
\rangle
}
$$

Compare this with a temporal matched filter:

$$
K_{ij}
=
\int
h_j(\tau)s_i(\tau)d\tau.
$$

One is an inner product in learned vector coordinates.

The other is an inner product in a function space over time.

The computational motif is the same.

The incoming item does not determine its own significance.

Its significance depends on the current query — the listener.

## 12.2 Recurrent Networks

For an RNN,

$$
x_{t+1}=F_\theta(x_t,u_t).
$$

The effect of \(u_t\) already depends on \(x_t\).

Every recurrent model therefore implements a primitive form of state-dependent susceptibility.

The interesting question is not whether recurrence has this property.

It does.

The question is what learning makes the geometry represent.

## 12.3 State-Space Models

A continuous state-space model begins with

$$
\dot x=Ax+Bu,
\qquad
y=Cx+Du.
$$

The eigenstructure of \(A\) determines characteristic temporal modes and decay rates.

This is already close to a bank of temporal susceptibilities.

Modern structured state-space architectures make this machinery computationally useful for long sequences.

Selective state-space systems go further by making parts of the effective dynamics depend on the current input.

In different language:

$$
\text{current event}
\rightarrow
\text{changed susceptibility}.
$$

## 12.4 Next-Token Prediction

A language model is trained approximately by minimizing

$$
L(\theta)
=
-\sum_t
\log P_\theta(w_{t+1}\mid w_{\le t}).
$$

This asks one question again and again:

> Given this past, what comes next?

Training changes \(\theta\).

After training, \(\theta\) is a structure through which previously unseen sequences produce useful distributions over possible continuations.

Thus:

$$
\text{many past sequences}
\rightarrow
\theta
\rightarrow
P_\theta(\text{possible future}\mid\text{new history}).
$$

The training corpus is not preserved merely as a collection of tapes.

Statistical structure becomes embodied in how the network responds.

In this abstract sense,

$$
\boxed{
\text{weights are frozen consequences of past sequences}
}
$$

and inference is

$$
\boxed{
\text{a new sequence moving through that frozen response geometry}
}
$$

---

# 13. A Common Mathematical Form

The complete model can be written without committing to neurons, oscillators, or Transformers.

Let:

- \(\theta_t\) = slowly changing learned structure,
- \(x_t\) = fast current state,
- \(u_t\) = incoming perturbation,
- \(s_t\) = emitted event,
- \(H_\theta(x)\) = state-dependent susceptibility,
- \(\hat u_{t+1}\) = predicted future input.

### Emission

$$
s_t=G_{\theta_t}(x_t).
$$

### Reception

$$
r_t
=
H_{\theta_t}(x_t)[s_t,u_t].
$$

### State evolution

$$
x_{t+1}
=
F_{\theta_t}(x_t,r_t).
$$

### Prediction

$$
\hat u_{t+1}
=
P_{\theta_t}(x_{t+1}).
$$

### Error

$$
e_{t+1}
=
u_{t+1}-\hat u_{t+1}.
$$

### Slow learning

$$
\theta_{t+1}
=
\theta_t
+
\eta\,
\Phi(e_{t+1},x_t,x_{t+1},u_t).
$$

The loop is therefore

$$
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
\theta_{t+1}
}
$$

History exists in two compiled forms.

Fast history:

$$
H_{\text{recent}}\rightarrow x_t.
$$

Long accumulated history:

$$
H_{\text{long}}\rightarrow\theta_t.
$$

Neither must contain an explicit record of the events that created it.

They need only preserve distinctions relevant to possible futures.

---

# 14. Predictive Susceptibility

We can now state the central definition.

> **Predictive susceptibility is the learned, state-dependent tendency of a dynamical system to respond differently to perturbations according to the futures those perturbations imply.**

Memory becomes:

$$
\boxed{
\text{history compiled into predictive susceptibility}
}
$$

Recall becomes:

$$
\boxed{
\text{a probe entering the region of state space where an old continuation becomes likely}
}
$$

Communication becomes:

$$
\boxed{
\text{a perturbation whose useful effect exists only relative to a listener}
}
$$

Prediction becomes:

$$
\boxed{
\text{the future toward which current susceptibility most readily evolves}
}
$$

Surprise becomes:

$$
\boxed{
\text{the component of reality not absorbed by current susceptibility}
}
$$

Learning becomes:

$$
\boxed{
\text{surprise reshaping susceptibility}
}
$$

And intelligence may be:

$$
\boxed{
\text{the adaptive management of branching possible futures}
}
$$

---

# 15. Why Many Memories Can Become More Than Many Memories

Suppose an organism contains thousands of independent sequence memories.

That is useful.

But suppose those memories instead share one response geometry.

Now states encountered in many different sequences overlap.

At each shared state, multiple continuations coexist.

The system has automatically constructed a graph — or more accurately a manifold — of possible futures.

A novel trajectory can then be produced without having been stored whole.

Parts of old trajectories can be recombined because they pass through compatible predictive states.

Thus:

$$
\text{experience}_1
+
\text{experience}_2
+
\cdots
+
\text{experience}_n
$$

does not merely produce

$$
n\text{ memories}.
$$

It can produce

$$
\boxed{
\text{a reusable geometry of possible worlds}
}
$$

That is a plausible bridge from memory to flexible intelligence.

The same mechanism creates its own danger.

When several histories collapse into one predictive state, detail is lost.

When too many incompatible continuations occupy the same region, interference grows.

So abstraction and forgetting may be two sides of the same operation.

The system discards differences in the past that no longer change its prediction of the future.

That may not be memory failure.

It may be the computation.

---

# 16. Falsifiable Predictions

A useful theory must risk failure.

## Prediction 1 — Same Event, Different Listener State

Hold the emitted event and timing fixed.

Place the receiver in two different hidden states.

The downstream result should differ when the task requires history-dependent interaction.

If receiver state does not matter, the strong coupling claim fails.

---

## Prediction 2 — Same Timing, Different Event Shape

Create events with identical timing and controlled gross properties but different fine temporal shape.

If the receiver has learned shape-sensitive susceptibility, the events should produce different continuations.

Shuffling event shape between histories while preserving timing should impair performance.

This is the most direct computational experiment suggested by the waveform paper.

---

## Prediction 3 — Identical Present, Different Hidden History

Construct two trials with

$$
u_t^{(1)}=u_t^{(2)}
$$

and identical present observable state, but different earlier histories.

A successful history-compiled system should produce different responses if those histories imply different futures.

---

## Prediction 4 — Listener-First Learning

Use one fixed task and manipulate only the curriculum.

**Condition A:** first teach the receiver that incoming signals must be interpreted jointly with receiver state.

**Condition B:** first teach the receiver a state-independent shortcut.

Then introduce the same history-dependent communication problem.

The theory predicts:

$$
\text{Condition A}>\text{Condition B}
$$

for successful emergence of historical communication.

This is the clean controlled experiment currently missing between FridayRepo and KapeaKanava.

---

## Prediction 5 — Predictive-State Clustering

Generate many different histories, deliberately arranging some to imply the same future distribution.

After training a sequence learner, compare representational similarity.

The theory predicts that sufficiently compressed internal states should cluster more strongly by

$$
P(\text{future}\mid\text{history})
$$

than by literal similarity of their histories.

---

## Prediction 6 — Temporal Susceptibility Should Aid Time Warps

On tasks where relevant structure is defined by relative phase rather than absolute duration, a model whose memory coordinate explicitly follows phase should generalize better to untrained speed transformations than a comparably sized model tied to absolute time.

ResonaattoriAivo is an initial toy demonstration, not a general result.

---

## Prediction 7 — Surprise Should Modify the Geometry Responsible for Prediction

If prediction residue is the learning signal, systematic errors should reshape the relevant susceptibility more strongly than already-predicted events.

---

# 17. What Would Falsify the Biological Version?

Several outcomes would substantially weaken the biological interpretation.

1. State-dependent somatic action-potential waveform variation may prove largely irrelevant to downstream targets.
2. Biologically realistic receivers may fail to extract useful historical variables from plausible waveform differences once propagation, synaptic noise, and population variability are included.
3. Temporal susceptibility may be adequately explained by conventional spike timing, synaptic weights, and recurrence, with fine waveform carrying no additional computational advantage.
4. The listener-first effect may disappear under architecture- and task-matched experiments.
5. Predictive-state compression may prove too generic to explain anything uniquely.

The theory earns value only if its specific decomposition produces distinctive predictions:

- state-dependent emission,
- state-dependent reception,
- learning startup constraints,
- predictive compression,
- and error-driven reshaping of response geometry.

---

# 18. What This Paper Does Not Claim

This paper does **not** claim that:

- neurons contain permanent standing waves,
- action-potential waveform is proven to encode long-term memories,
- chandelier cells are sequence-release switches,
- basket cells constitute a complete gamma clock,
- the brain is a Transformer,
- Transformer attention evolved from neuronal resonance,
- next-token prediction explains biological intelligence,
- ResonaattoriAivo, FridayRepo, or KapeaKanava establish a theory of cognition,
- prediction alone is sufficient for intelligence.

The defensible statement is narrower:

$$
\boxed{
\text{learning can be viewed as converting histories into state-dependent response geometry}
}
$$

Once that transformation has occurred, apparently different mechanisms — resonance, recurrence, attention, associative retrieval, and state-space dynamics — can all perform computation by allowing new events to act on learned geometry.

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

A state-space model may acquire useful temporal modes.

A language model may acquire an internal state from which one continuation is vastly more probable than another.

In every case:

$$
\text{past interaction}
\rightarrow
\text{changed future response}.
$$

That is memory at its most abstract.

But sequence learning adds something important.

The future response is not arbitrary.

It becomes shaped by regularities of what historically came next.

The system therefore slowly becomes an approximation to the temporal structure of its environment.

Not a photographic model of the universe.

Not a database containing the universe.

A machine whose **possible motions increasingly resemble possible motions of the world**.

The phrase "inverse model of the universe" can therefore be replaced by something more precise:

$$
\boxed{
\text{the learner becomes a predictive dynamical complement to its environment}
}
$$

Its structure embodies what usually follows.

Its activity proposes what follows now.

Its errors mark where the proposal failed.

Its plasticity changes what it will propose next time.

---

# 20. Conclusion

The central proposal can be written in one line:

$$
\boxed{
\textbf{history becomes susceptibility; susceptibility generates possible futures}
}
$$

A physical resonator is one possible implementation.

A recurrent network is another.

Attention implements a learned match between an incoming representation and a current query.

State-space models explicitly construct temporal response dynamics.

Prediction training reshapes all of them according to regularities in sequences.

This does not make these systems equivalent.

It identifies a common computational object beneath them.

The most interesting consequence concerns intelligence.

If every remembered sequence remained isolated, memory would be a collection of recordings.

But when many sequences modify one shared response geometry, their overlaps create branching possible futures.

The system can generalize, recombine, predict, query uncertainty, and change itself when reality follows none of the expected paths.

The past has disappeared as a literal event.

Yet it remains present everywhere in what can happen next.

That is **predictive susceptibility**.

---

# Evidence Ledger

## Established or externally supported

- Action-potential waveform can vary systematically with recent input and network state.
- Presynaptic action-potential shape can affect synaptic output in established experimental preparations.
- Predictive-coding frameworks can express feed-forward activity as residual error relative to predictions.
- Preconfigured internal neural dynamics and internally generated trajectories are established research programs, though strong claims about specific preplay phenomena remain contested.
- Transformer attention has a formal connection to modern Hopfield associative-memory updates.
- Structured and selective state-space models are successful sequence-model architectures.
- Emergent communication can exhibit a joint exploration/startup problem and can benefit from signalling/listening biases.

## Measured in the exploratory repositories

### ResonaattoriAivo

- phase-based tempo transfer,
- free continuation after cueing,
- prediction residue as novelty signal,
- noise fragility,
- recovery from plastic response geometry.

### FridayRepo

- sender-state × receiver-state coupling,
- early precomputation when the future question is known,
- compressed historical communication when the query arrives later.

### KapeaKanava

- generic communication startup failure despite adequate receiver capacity,
- improvement from an explicitly multiplicative listener,
- rank-bound behavior when communication starts,
- shortcut capture of the channel in the original attacker.

## Proposed here

- **Predictive susceptibility** as a common abstraction joining slow memory, fast context, communication, prediction, and learning.
- Sequence memories as trajectories through susceptibility rather than necessarily stored chains.
- Communication as conditional historical residue that the future listener cannot reconstruct itself.
- Evolutionary/developmental priors as possible solutions to a communication/interaction startup problem.
- Flexible intelligence as management of branching futures produced when many learned sequences share one response geometry.
- Biological resonance and modern AI sequence computation as distinct realizations of the same higher-level computational pattern.

---

# Related Repositories

- [`ResonaattoriAivo`](https://github.com/anttiluode/ResonaattoriAivo)
- [`FridayRepo`](https://github.com/anttiluode/FridayRepo)
- [`KapeaKanava`](https://github.com/anttiluode/KapeaKanava)
- [`The_Ping_And_The_Listener`](https://github.com/anttiluode/The_Ping_And_The_Listener)
- [`Query-Addressable-Rate-Distortion-Memory`](https://github.com/anttiluode/Query-Addressable-Rate-Distortion-Memory)
- [`TransformerToX`](https://github.com/anttiluode/TransformerToX)
- [`Rytmi`](https://github.com/anttiluode/Rytmi)
- [`Sihti`](https://github.com/anttiluode/Sihti)
- [`SihtiMuisti`](https://github.com/anttiluode/SihtiMuisti)

---

# References

- Buzsáki, G. (2019). *The Brain from Inside Out*. Oxford University Press.
- Dragoi, G., & Tonegawa, S. (2011). Preplay of future place cell sequences by hippocampal cellular assemblies. *Nature*, 469, 397–401.
- Eccles, T., Bachrach, Y., Lever, G., Lazaridou, A., & Graepel, T. (2019). Biases for emergent communication in multi-agent reinforcement learning.
- Gu, A., Goel, K., & Ré, C. (2021). Efficiently modeling long sequences with structured state spaces.
- Gu, A., & Dao, T. (2023). Mamba: Linear-time sequence modeling with selective state spaces.
- Martin-Burgos, B., Juavinett, A., Rivière, P. D., Hammonds, R., & Voytek, B. (2026). *Action potential waveforms are state-dependent*. bioRxiv 2026.09.15.751814.
- Ramsauer, H., et al. (2020). *Hopfield Networks is All You Need*.
- Rao, R. P. N., & Ballard, D. H. (1999). Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience*, 2, 79–87.
- Shalizi, C. R., & Crutchfield, J. P. (2001). Computational mechanics: Pattern and prediction, structure and simplicity. *Journal of Statistical Physics*, 104, 817–879.
- Luode, A. (2026). *ResonaattoriAivo*. Exploratory software repository.
- Luode, A. (2026). *FridayRepo*. Exploratory software repository.
- Luode, A. (2026). *KapeaKanava*. Exploratory software repository.
- Luode, A. (2026). *The Ping and the Listener*. Working paper and exploratory synthesis.

---

## Short version

> **The past does not need to remain as a recording.**
>
> It can remain as the shape of what the system is now able to do.
>
> Sequence learning turns histories into a geometry of possible futures.
>
> New events probe that geometry.
>
> Prediction expresses it.
>
> Surprise changes it.
>
> **History becomes susceptibility; susceptibility generates possible futures.**
