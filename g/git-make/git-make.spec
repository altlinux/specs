Name: git-make
Version: 0.1.1
Release: alt1

Summary: version control and merging of intended and automatically produced results
Summary(ru_RU.UTF8): контроль версий и слияние желаемых и автоматически произведённых результатов
License: %gagpl3plus
Group: Development/Other
URL: https://www.gitorious.org/git-make
Packager: Ivan Zakharyaschev <imz@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch
BuildPreReq: rpm-build-licenses

%description
git-make is a tool that helps in "inductive" development of results.
(It's a small set of commands implemented on top of git and make.)

On one side, it's a way to get a nice output by manually refining raw
automatic output, without the need to re-do the manual refining for each
new revision of your sources (Git will merge your previous tweaks).

It goes like this. You hold sources in Git, then make an output
automatically (with a rule from Makefile), then tweak something in the
generated output (because the program that produced it wasn't perfect
or didn't perfectly match your wishes), and then on the next
development cycle edit your sources, and get a tweaked (merged) output
from the new revision.

For every branch with sources (say, master), two additional branches are used:

* master_/AUTO/goal to hold what was automatically generated for goal;
* master_/OUT/goal -- your tweaked, manually inspected version of the
output for goal, based on master_/AUTO/goal.

On the other side, it's a kind of test-driven development: you can start by
creating a small example result for "goal", accept it as a one
conforming to your intentions (technically: commit in the special Git
branch: master_/OUT/goal). Since then, this committed example can be
viewed as the expected result of a test. Then you extend the rules in
your sources, so that they produce a larger set of results (saved in
the special branch master_/AUTO/goal), and gradually review them (by
committing to master_/OUT/goal only the things you accept as good).

The diff between master_/AUTO/goal and master_/OUT/goal shows what
doesn't yet work as expected in the current revision of master. If
there is no diff, this means that your rules and the program that
generates the results are correct (i.e., perfectly match your intentions).

%prep
%setup

%install
mkdir -p %buildroot%_bindir
install --preserve-timestamps -m 755 gitmk-* -t %buildroot%_bindir

%files
%_bindir/*

%changelog
* Fri May 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1
- check-GOAL targets should simply not have GOAL as a prerequisite;
  in general, a check makes sense before the transformation, too.
  (This idea allowed us to avoid a hack whose purpose was to avoid a
  re-make after a Git checkout.)
- gitmk-make: proceed if nothing to commit (borrowed from gear --commit).
- more clear short AUTO commit msg (for those who do not know about git-make).

* Sun Jan 11 2015 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1
- Initial release of the tool I've written & used for myself (to work
on a textbook and produce output with pandoc and extra tweaks, 
and to work on a formalized grammatical description for a corpus of
linguistic data).
