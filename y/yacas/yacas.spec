Name: yacas
Version: 1.4.1
Release: alt1

Summary: Yet Another Computer Algebra System
License: GPL
Group: Sciences/Mathematics

Url: http://yacas.sourceforge.net
Source0: http://yacas.sourceforge.net/backups/%name-%version.tar.gz
Source100: yacas.watch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Mar 22 2015
# optimized out: libcloog-isl4 libstdc++-devel texlive-base-bin texlive-latex-base
BuildRequires: gcc-c++

BuildRequires: /usr/bin/latex /usr/bin/dvips

%description
Yacas (Yet Another Computer Algebra System) is a small and
highly flexible computer algebra language. The syntax uses
an infix-operator grammar parser.  The distribution contains
a small library of mathematical functions, but its real strength
is in the language in which you can easily write your own symbolic
manipulation algorithms. It supports arbitrary precision arithmetic.

%package -n lib%name
Summary: Shared library for YACAS
Group: System/Libraries

%description -n lib%name
This package contains shared library for YACAS.

%package -n lib%name-devel
Summary: Development headers for YACAS
Group: Development/C

%description -n lib%name-devel
This package contains files needed to link against YACAS library.

%package docs
BuildArch: noarch
Summary: YACAS intro, algos, coding, essays and reference manuals
Group: Documentation

%description docs
YACAS intro, algos, coding, essays and reference manuals

%prep
%setup
# https://sourceforge.net/p/yacas/tickets/96/
touch README

%build
%autoreconf
CXXFLAGS="%optflags" %configure --enable-gmp --disable-static
%make_build

%install
%makeinstall_std
# I can't see any use for these, no libs installed
rm -rf %buildroot%_datadir/%name/include

%files
%doc AUTHORS NEWS README TODO
%doc docs/*.html docs/*.gif
%_bindir/*
%_datadir/%name/
%exclude %_datadir/%name/documentation/

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/%name/

%files docs
%dir %_datadir/%name/
%_datadir/%name/documentation/

# TODO:
# - figure out if/how to install ytxt2tex, see manmake/README
# - JavaYacas?

%changelog
* Sun Mar 06 2016 Michael Shigorin <mike@altlinux.org> 1.4.1-alt1
- new version (watch file uupdate)

* Sat Mar 05 2016 Michael Shigorin <mike@altlinux.org> 1.4.0-alt1
- new version (watch file uupdate)
  + repackaged tarball from zipfile, see also
    https://sourceforge.net/p/yacas/tickets/95/

* Sun Mar 22 2015 Michael Shigorin <mike@altlinux.org> 1.3.6-alt1
- new version (watch file uupdate)
- added shared library subpackage
- buildreq

* Tue Apr 15 2014 Michael Shigorin <mike@altlinux.org> 1.3.4-alt1
- new version (watch file uupdate)

* Tue Oct 08 2013 Michael Shigorin <mike@altlinux.org> 1.3.3-alt1
- new version (watch file uupdate)

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 1.3.2-alt1
- 1.3.2
- dropped patch (already there)

* Mon Dec 14 2009 Michael Shigorin <mike@altlinux.org> 1.2.2-alt5
- package %_datadir/%name/ into docs subpackage too

* Sun Dec 13 2009 Michael Shigorin <mike@altlinux.org> 1.2.2-alt4
- tweaked *tex buildreqs (repocop)

* Sat Aug 01 2009 Michael Shigorin <mike@altlinux.org> 1.2.2-alt3
- docs subpackage made noarch (repocop)
- minor spec cleanup

* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 1.2.2-alt2
- fixed build with gcc 4.3

* Fri Mar 28 2008 Michael Shigorin <mike@altlinux.org> 1.2.2-alt1
- 1.2.2
- added ytxt2tex

* Fri Sep 21 2007 Michael Shigorin <mike@altlinux.org> 1.2.0-alt1
- 1.2.0
- it finally builds again!
- split documentation into subpackage of its own

* Mon Aug 06 2007 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1
- 1.1.0
- build fixup unfinished

* Thu Apr 24 2003 Michael Shigorin <mike@altlinux.org> 1.0.52-alt1
- built for ALT Linux

