%define oname igakit
Name: python-module-%oname
Version: 0.1
Release: alt1.hg20130902
Summary: Toolkit for IsoGeometric Analysis (IGA)
License: BSD
Group: Development/Python
Url: https://petiga-igakit.readthedocs.org/en/latest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/dalcinl/igakit
Source: %name-%version.tar

BuildPreReq: python-devel libnumpy-devel gcc-fortran

%description
igakit: Toolkit for IsoGeometric Analysis (IGA).

%prep
%setup

%build
%add_optflags %optflags_shared
%python_build_debug

%install
%python_install

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Thu Jul 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.hg20130902
- Initial build for Sisyphus

