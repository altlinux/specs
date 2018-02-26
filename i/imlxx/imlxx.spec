Name: imlxx
Version: 1.2a
Release: alt2
Summary: Iterative Methods Library
License: MIT
Group: Sciences/Mathematics
Url: http://math.nist.gov/iml++/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildArch: noarch

Source: %name.tar.gz
Source1: ftp://math.nist.gov/pub/pozo/docs/iml.ps.gz

%description
IML++ is a C++ templated library of modern iterative methods for solving both
symmetric and nonsymmetric linear systems of equations. The algorithms are
fully templated in that the same source code works for dense, sparse, and
distributed matrices.

%package -n lib%name-devel
Summary: Headers of Iterative Methods Library (IML++)
Group: Development/C++

%description -n lib%name-devel
IML++ is a C++ templated library of modern iterative methods for solving both
symmetric and nonsymmetric linear systems of equations. The algorithms are
fully templated in that the same source code works for dense, sparse, and
distributed matrices.

This package contains headers of IML++.

%prep
%setup
install -m644 %SOURCE1 .
gunzip iml.ps.gz

%install
install -d %buildroot%_includedir

install -m644 *.h %buildroot%_includedir

%files
%doc iml.ps

%files -n lib%name-devel
%_includedir/*

%changelog
* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2a-alt2
- Set devel package as noarch

* Fri Jul 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2a-alt1
- Initial build for Sisyphus

