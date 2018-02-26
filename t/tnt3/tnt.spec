Name: tnt3
Version: 3.0.12
Release: alt1.beta
Summary: Template Numerical Toolkit (TNT) v3
License: Public domain
Group: Sciences/Mathematics
Url: http://math.nist.gov/tnt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://math.nist.gov/tnt/tnt_3_0_12.zip

BuildPreReq: unzip doxygen

%description
The Template Numerical Toolkit (TNT) is a collection of interfaces and
reference implementations of numerical objects useful for scientific
computing in C++. The toolkit defines interfaces for basic data
structures, such as multidimensional arrays and sparse matrices,
commonly used in numerical applications. The goal of this package is to
provide reusable software components that address many of the
portability and maintennace problems with C++ codes.

TNT provides a distinction between interfaces and implementations of TNT
components. For example, there is a TNT interface for two-dimensional
arrays which describes how individual elements are accessed and how
certain information, such as the array dimensions, can be used in
algorithms; however, there can be several implementations of such an
interface: one that uses expression templates, or one that uses BLAS
kernels, or another that is instrumented to provide debugging
information. By specifying only the interface, applications codes may
utilize such algorithms, while giving library developers the greatest
flexibility in employing optimization or portability strategies.

%package devel
Summary: Development files of the Template Numerical Toolkit (TNT) v3
Group: Development/C++
BuildArch: noarch
Requires: gcc-c++
Conflicts: tnt-devel

%description devel
The Template Numerical Toolkit (TNT) is a collection of interfaces and
reference implementations of numerical objects useful for scientific
computing in C++. The toolkit defines interfaces for basic data
structures, such as multidimensional arrays and sparse matrices,
commonly used in numerical applications. The goal of this package is to
provide reusable software components that address many of the
portability and maintennace problems with C++ codes.

TNT provides a distinction between interfaces and implementations of TNT
components. For example, there is a TNT interface for two-dimensional
arrays which describes how individual elements are accessed and how
certain information, such as the array dimensions, can be used in
algorithms; however, there can be several implementations of such an
interface: one that uses expression templates, or one that uses BLAS
kernels, or another that is instrumented to provide debugging
information. By specifying only the interface, applications codes may
utilize such algorithms, while giving library developers the greatest
flexibility in employing optimization or portability strategies.

This package contains development files of TNT v3.

%package docs
Summary: Documentation for the Template Numerical Toolkit (TNT) v3
Group: Development/Documentation
BuildArch: noarch

%description docs
The Template Numerical Toolkit (TNT) is a collection of interfaces and
reference implementations of numerical objects useful for scientific
computing in C++. The toolkit defines interfaces for basic data
structures, such as multidimensional arrays and sparse matrices,
commonly used in numerical applications. The goal of this package is to
provide reusable software components that address many of the
portability and maintennace problems with C++ codes.

TNT provides a distinction between interfaces and implementations of TNT
components. For example, there is a TNT interface for two-dimensional
arrays which describes how individual elements are accessed and how
certain information, such as the array dimensions, can be used in
algorithms; however, there can be several implementations of such an
interface: one that uses expression templates, or one that uses BLAS
kernels, or another that is instrumented to provide debugging
information. By specifying only the interface, applications codes may
utilize such algorithms, while giving library developers the greatest
flexibility in employing optimization or portability strategies.

This package contains development documentation for TNT v3.

%prep
%setup

%build
doxygen tnt.h

%install
install -d %buildroot%_includedir
install -p -m644 *.h %buildroot%_includedir

%files devel
%_includedir/*

%files docs
%doc html/*

%changelog
* Fri Sep 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.12-alt1.beta
- Initial build for Sisyphus

