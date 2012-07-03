Name: mithraen-build-utils
Summary: Simple utilites that simplify development to me
Version: 0.1.10
Release: alt1
License: GPL
Group: Development/Other
BuildArch: noarch
BuildRequires: apt-repo-tools dialog etersoft-build-utils gear perl-DBM perl-RPM subversion termutils
Obsoletes: seiros-build-utils
Packager: Denis Smirnov <mithraen@altlinux.ru>
Requires: git-svn
Source: %name-%version.tar
Requires: specgen

%description
Simple utilites that simplify development to me


%prep
%setup

%install
mkdir -p %buildroot%_bindir
install -m755 * %buildroot/%_bindir/

%files
%_bindir/*

%changelog
* Mon Jun 25 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.10-alt1
- gear-clone: fix work with new girar-nmu

* Tue Jun 19 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.9-alt1
- add gear-clone utility

* Thu Sep 16 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.8-alt1
- Add:
  + mass-push.
  + mass-task-add.
  + option '-f' to Gpush.
  + update-asterisk-1.6.2.

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.7-alt1
- Add:
  + git-show-roots.
  + git-clone-bare-hardlink.
  + find-big-gits.
  + altlinux-fetch-gear.
- multiple small fixes.

* Thu May 06 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.6-alt1
- fix h-gen

* Sun Apr 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.5-alt1
- add requires to specgen

* Sun Apr 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.4-alt1
- Add:
  + branch-5.1 and build-5.1 scripts.
- cleanup to build-daemon.

* Sat Mar 20 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.3-alt1
- Add:
  + tasks-rerun.
  + task-rm.
  + task-ls-queue.
  + git-autobranches.
- Update:
  + task-run.
  + task-add.

* Mon Oct 05 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt1
- add build-daemon

* Mon Oct 05 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1.1-alt1
- small fixes in h-cleanup-*

* Sat Aug 29 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build for Sisyphus

