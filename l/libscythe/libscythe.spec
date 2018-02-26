Name: libscythe
Version: 1.0.2
Release: alt1
Summary: C++ library for statistical computation

Group: Development/C++
License: GPL
Url: http://scythe.wustl.edu/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://scythe.wustl.edu/dist/scythestat-1.0.2.tar.gz
Source1: http://scythe.wustl.edu/jstatsoftScythe.pdf

BuildPreReq: gcc-c++

%description
The Scythe Statistical Library is an open source C++ library for
statistical computation. It includes a suite of matrix manipulation
functions, a suite of pseudo-random number generators, and a suite
of numerical optimizers. Programs written using Scythe are generally
much faster than those written in commonly used interpreted
languages, such as R, Matlab, and GAUSS; and can be compiled on any
system with the GNU GCC compiler (and perhaps with other C++
compilers). One of the primary design goals of the Scythe developers
has been ease of use for non-expert C++ programmers. Ease of use is
provided through three primary mechanisms: (1) operator and function
over-loading, (2) numerous pre-fabricated utility functions, and (3)
clear documentation and example programs. Additionally, Scythe is
quite flexible and entirely extensible because the source code is
available to all users. Scythe is distributed under the GNU General
Public License, and has been thoroughly tested on Linux and MacOS X.

%package devel
Summary: C++ library for statistical computation
Group: Development/C++
BuildArch: noarch

%description devel
The Scythe Statistical Library is an open source C++ library for
statistical computation. It includes a suite of matrix manipulation
functions, a suite of pseudo-random number generators, and a suite
of numerical optimizers. Programs written using Scythe are generally
much faster than those written in commonly used interpreted
languages, such as R, Matlab, and GAUSS; and can be compiled on any
system with the GNU GCC compiler (and perhaps with other C++
compilers). One of the primary design goals of the Scythe developers
has been ease of use for non-expert C++ programmers. Ease of use is
provided through three primary mechanisms: (1) operator and function
over-loading, (2) numerous pre-fabricated utility functions, and (3)
clear documentation and example programs. Additionally, Scythe is
quite flexible and entirely extensible because the source code is
available to all users. Scythe is distributed under the GNU General
Public License, and has been thoroughly tested on Linux and MacOS X.

This package contains headers of Scythe library.

%package doc
Summary: Documentation for Scythe
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation for Scythe.

%prep
%setup -n scythestat
install -p -m644 %SOURCE1 .

%build
%configure

%install
%make_install DESTDIR=%buildroot install

%files devel
%_includedir/scythestat

%files doc
%doc jstatsoftScythe.pdf

%changelog
* Tue Mar 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
