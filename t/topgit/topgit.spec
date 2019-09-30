%define _unpackaged_files_terminate_build 1

Name: topgit
Version: 0.9
Release: alt6.git20150225

Summary: A different patch queue manager for Git
License: GPLv2
Group: Development/Tools
Url: https://github.com/greenrd/topgit
BuildArch: noarch

Source0: topgit-%version.tar
Patch0: topgit-tg_rename.patch
Patch1: topgit-custom-merge.patch

%{?!_without_test:%{?!_disable_test:%{?!_without_check:%{?!_disable_check:BuildRequires: git-core}}}}

%description
TopGit aims to make handling of large amounts of interdependent topic
branches easier.  It is designed especially for the case
when you maintain a queue of third-party patches on top of another
(perhaps Git-controlled) project and want to easily organize, maintain
and submit them - TopGit achieves that by keeping a separate topic
branch for each patch and providing a few tools to maintain the branches.

TopGit has been designed around three main tenets:

(i) TopGit is as thin layer on top of Git as possible.
You still maintain your index and commit using Git, TopGit will
only automate few indispensable tasks.

(ii) TopGit is anxious about _keeping_ your history. It will
never rewrite your history and all metadata is also tracked by Git,
smoothly and non-obnoxiously. It is good to have a _single_ point
when the history is cleaned up, and that is at the point of inclusion
in the upstream project; locally, you can see how your patch has evolved
and easily return to older versions.

(iii) TopGit is specifically designed to work in distributed
environment. You can have several instances of TopGit-aware repositories
and smoothly keep them all up-to-date and transfer your changes between
them.

%prep
%setup
%patch0 -p1
rm -f .topdeps .topmsg # clean up topgit internal files
%patch1 -p1
rm -f .topdeps .topmsg # clean up topgit internal files

# TODO: the problem with topgit internal files should be solved.
# The problem is like this
# (http://www.altlinux.org/Git/MergingBranches#.D0.B2.D0.BC.D0.B5.D1.81.D1.82.D0.B5_.D1.81_gear):
#
# `tg export` exports nice patches, but it can't be called from `gear`.
# Gear is stupid and includes them in the patches.
#
# Possible solutions:
#
# * teach Gear to use topgit (extra dependency?);
# * modify TopGit not to store the meta-info (.topmsg, .topdeps)
#   in Git trees (https://github.com/greenrd/topgit/issues/38);
# * somehow adapt `tg export` to the needs of a Gear-based workflow
#   (some relevant remarks and objections:
#   https://github.com/greenrd/topgit/issues/42#issuecomment-75389885).

%build
touch --date=tomorrow precheck
%make_build prefix=%_prefix
rm -f precheck

%install
touch --date=tomorrow precheck
%makeinstall
rm -f precheck

%check
rm -f precheck
make precheck
# TODO: it has a check against a hardcoded Git version;
# we want to automatically add that version to RPM deps.

%files
%_bindir/*
%_datadir/%name
%_prefix/libexec/%name
%doc README COPYING

%changelog
* Mon Sep 30 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt6.git20150225
- Fixed build without check.

* Wed Feb 27 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt5.git20150225
- (.spec) Corrected the BuildRequires tag name
  to fix build with rpm-build-4.0.4-alt125.

* Thu Feb 25 2015 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt4.git20150225
- tg update, tg create: pass a custom merge command with either TG_MERGE or
  --this-with (useful for rebasing or for "merge -s ours" in certain
  gear-workflows at ALT, partially solves ALT#30757).

* Wed Feb 11 2015 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt3.git20130407
- tg_rename: Clean up the old ref (with "tg delete -f").

* Fri Jan 30 2015 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt2.git20130407
- tg rename: a simple shortcut, implemented for leaves only

* Mon Jan 26 2015 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt1.git20130407
- new upstream release+Git changes from a new upstream maintainer:
  https://github.com/greenrd/topgit/tags

* Fri Jul 24 2009 Maxim Ivanov <redbaron at altlinux.org> 0.7-alt3.git20090527
- Corrected prefix

* Sat Jun 13 2009 Maxim Ivanov <redbaron at altlinux.org> 0.7-alt2.git20090527
- Update from upstream

* Sun May 17 2009 Maxim Ivanov <redbaron at altlinux.org> 0.7-alt2.git20090512
- Added README and COPYING files

* Sun May 17 2009 Maxim Ivanov <redbaron at altlinux.org> 0.7-alt1.git20090512
- Initial build for Sisyphus

