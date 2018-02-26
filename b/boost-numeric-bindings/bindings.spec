Name: boost-numeric-bindings
Version: 0.91
Release: alt1
Summary: Comprehensive linear algebra library for Python
License: BSD-style
Group: Development/Python
Url: http://mathema.tician.de//software/pylinear
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

#	http://git.tiker.net/trees/boost-numeric-bindings.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel

%description
PyLinear is a comprehensive linear algebra library for Python. It wraps
Boost UBlas into a Numeric-like shell, while adding bindings to UMFPACK,
ARPACK and LAPACK and a collection of home-grown algorithms such as
preconditioned CG, preconditioned BiCGSTAB and more. It is mature, but
has a few rough edges in the build process.

%prep
%setup

%build
./configure --prefix=%buildroot%prefix

%install
%makeinstall_std

%files
%doc LICENSE*
%_includedir/boost/*

%changelog
* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91-alt1
- Initial build for Sisyphus

