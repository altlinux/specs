%define _unpackaged_files_terminate_build 1

Name: topgit
Version: 0.9
Release: alt2.git20130407

Summary: A different patch queue manager for Git
License: GPLv2
Group: Development/Tools
Url: https://github.com/greenrd/topgit
BuildArch: noarch

Source0: topgit-%version.tar
Patch0: topgit-tg_rename.patch

BuildRequires(check): git-core

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

%build
touch --date=tomorrow precheck
%make_build prefix=%_prefix
rm -f precheck

%install
%makeinstall

%check
make precheck
# TODO: it has a check against a hardcoded Git version;
# we want to automatically add that version to RPM deps.

%files 
%_bindir/*
%_datadir/%name
%_prefix/libexec/%name
%doc README COPYING

%changelog
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

