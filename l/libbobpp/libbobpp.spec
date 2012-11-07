%define oname bobpp
Name: libbobpp
Version: 0.2.0
Release: alt1.1

Summary: Library for easy implementation of sequential and parallel search algorithms

License: GPL
Group: Development/Tools
Url: http://bobpp.prism.uvsq.fr

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://software.prism.uvsq.fr/releases/bobpp/%oname-%version.tar.bz2
Patch: libbobpp-0.2.0-alt-glibc-2.16.patch

# Automatically added by buildreq on Sun Jul 12 2009
BuildRequires: doxygen gcc-c++ graphviz texlive-latex-base

%description
The Bob++ Library is a set of C++ classes. Its goal is to allow easy
implementation of sequential and parallel search algorithms (Branch and X,
Dynamic programming, etc) to solve your own problems.

%package devel
Summary: Development files for the Bob++ Library
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files for %name library.

%prep
%setup -n %oname-%version
%patch -p2

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc README
%_bindir/boblistener
%_bindir/bobtree
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Wed Nov 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.1
- Fixed build with glibc 2.16

* Sun Jul 12 2009 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- initial build for ALT Linux Sisyphus
