Name:    jthread
Version: 1.3.1
Release: alt1

Summary: JThread provides classes to make use of threads easy on different platforms
License: MIT
Group:   System/Libraries
URL:     http://research.edm.uhasselt.be/~jori/page/index.php?n=CS.Jthread

Source0: http://research.edm.uhasselt.be/jori/jthread/jthread-%{version}.tar.bz2

BuildRequires(pre): cmake
BuildRequires: /usr/bin/pdflatex
BuildRequires: gcc-c++
BuildRequires: texlive-latex-recommended

%description
JThread provides some classes to make use of threads easy on different
platforms. The classes are actually rather simple wrappers around
existing thread implementations.

%package devel
Summary: Development files for JThread
Group:   Development/C
Requires: jthread = %{version}-%{release}

%description devel
Development files for JThread

%prep
%setup -q

%build
%cmake
%cmake_build
pushd doc
pdflatex manual.tex
pdflatex manual.tex
popd

%install
%cmakeinstall_std
rm -f %buildroot%_libdir/libjthread.a

%files
%doc ChangeLog LICENSE.MIT README.TXT TODO
%_libdir/libjthread.so.*

%files devel
%doc doc/manual.pdf doc/manual.tex
%_includedir/jthread
%_libdir/libjthread.so
%_libdir/cmake/*
%_pkgconfigdir/jthread.pc

%changelog
* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- New version
- Build by cmake

* Fri Jul 26 2013 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt2
- Build in Sisyphus from Autoimports (thanks viy@ and Fedora maintainers)

* Wed Aug 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_9
- new version
