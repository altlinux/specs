%define oname Cgc
Name: Coin%oname
Version: 20100905
Release: alt3
Summary: Coin Graph Classes
License: CPL v1.0
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/Cgc
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar.gz

BuildPreReq: gcc-c++

%description
The purpose of the Cgc collection of Network Representations and
Algorithms is to facilitate the development and implementation of
Network Algorithms.

%package devel
Summary: Headers of Coin Graph Classes
Group: Development/C++
BuildArch: noarch

%description devel
The purpose of the Cgc collection of Network Representations and
Algorithms is to facilitate the development and implementation of
Network Algorithms.

This package contains headers of Cgc.

%package examples
Summary: Examples for Coin Graph Classes
Group: Sciences/Mathematics

%description examples
The purpose of the Cgc collection of Network Representations and
Algorithms is to facilitate the development and implementation of
Network Algorithms.

This package contains examples for Cgc.

%package doc
Summary: Documentation for Coin Graph Classes
Group: Development/Documentation
BuildArch: noarch

%description doc
The purpose of the Cgc collection of Network Representations and
Algorithms is to facilitate the development and implementation of
Network Algorithms.

This package contains development documentation for Cgc.

%prep
%setup

%build
%make_build -C %oname/examples

%install
install -d %buildroot%_includedir
install -p -m644 %oname/src/* %buildroot%_includedir

install -d %buildroot%_bindir
for i in simple simpleShortestPath pathFindExample sspsolver;
do
	install -m755 %oname/examples/$i %buildroot%_bindir/%oname-$i
done

%files devel
%_includedir/*

%files doc
%doc doc/*

%files examples
%doc %oname/examples/*.c* %oname/examples/Makefile
%_bindir/*

%changelog
* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100905-alt3
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100905-alt2
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100905-alt1
- Version 20100905

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100227-alt1
- Initial build for Sisyphus

