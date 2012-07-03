Name: qgit
Version: 2.4
Release: alt1

Summary: Git GUI viewer built on Qt4/C++
Group: Development/Tools
License: GPLv2
Url: http://libre.tibirna.org/projects/qgit/

Packager: Ivan A. Melnikov <iv@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Provides: qgit4 = %name-%version
Obsoletes: qgit4 < %name-%version

BuildPreReq: gcc-c++ libqt4-devel >= 4.3

%description
With qgit you will be able to browse revisions history, view
patch content and changed files, graphically following different
development branches.

Features:

* View revisions, diffs, files history, files annotation,
  archive tree.

* Commit changes visually cherry picking modified files.

* Apply or format patch series from selected commits, drag and
  drop commits between two instances of qgit.

* qgit implements a GUI for the most common StGIT commands like
  push/pop and apply/format patches. You can also create new
  patches or refresh current top one using the same semantics of
  git commit,  i.e. cherry picking single modified files.

%prep
%setup
%patch -p1
sed -i 's,debug_and_release,release,' qgit.pro
sed -i 's,debug_and_release,release,' src/src.pro
sed -i 's,VERSION "2.3",VERSION "%version",' src/config.h
sed -i '/QMAKE_CXXFLAGS_RELEASE/s,-O2 ,%optflags ,g' src/src.pro

%build
qmake-qt4 qgit.pro
%make_build

%install
install -pD -m755 bin/qgit %buildroot%_bindir/%name

%files
%doc README
%_bindir/%name

%changelog
* Thu Mar 08 2012 Ivan A. Melnikov <iv@altlinux.org> 2.4-alt1
- new upstream
- new version (closes: #25675)

* Fri Aug 20 2010 Andrey Rahmatullin <wrar@altlinux.org> 2.3-alt2
- qgit-2.0rc1-306-gd8be482
- rename to qgit

* Sat May 16 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.3-alt1
- 2.3

* Fri May 01 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.2-alt3
- qgit-2.0rc1-278-g50d839b

* Sun Feb 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.2-alt2
- qgit-2.0rc1-266-g24c04d0

* Sat Jul 19 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.2-alt1
- 2.2

* Fri Jan 04 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Sat Dec 01 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.0-alt2
- add buildreqs

* Fri Nov 30 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.0-alt1
- 2.0

* Thu Nov 29 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.5.7-alt1
- 1.5.7

* Sun Sep 02 2007 Sir Raorn <raorn@altlinux.ru> 1.5.6-alt2
- Updated to 1.5.6-5a135439
- Use QProcess instead of temporary files (CVE-2007-4631 workaround)

* Tue Aug 07 2007 Sir Raorn <raorn@altlinux.ru> 1.5.6-alt1
- [1.5.6]

* Fri Feb 02 2007 Sir Raorn <raorn@altlinux.ru> 1.5.4-alt1
- [1.5.4]

* Mon Nov 20 2006 Sir Raorn <raorn@altlinux.ru> 1.5.3-alt1
- [1.5.3]

* Wed Nov 08 2006 Sir Raorn <raorn@altlinux.ru> 1.5.2-alt1
- [1.5.2]

* Sun Sep 03 2006 Sir Raorn <raorn@altlinux.ru> 1.4-alt1
- [1.4]

* Fri May 12 2006 Sir Raorn <raorn@altlinux.ru> 1.2-alt1
- Built for Sisyphus

