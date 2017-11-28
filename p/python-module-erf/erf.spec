%define _unpackaged_files_terminate_build 1
%define oname erf

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt1
Summary: A pure-Python implementation of the error function and inverse error function.
License: GPLv3
Group: Development/Python
BuildArch: noarch
Url: https://github.com/dougthor42/pyerf

# https://github.com/dougthor42/pyerf.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(hypothesis)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(hypothesis)
%endif

%description
pyerf is a pure-Python implementation of the error function
and inverse error function using the same functions that SciPy uses
(namely parts of the Cephes math library, cprob/ndtr.c and cprob/ndtri.c).

This is a useful package for when you need to calculate some error fuctions
but you don't want to install all of the SciPy/NumPy stuff.

%if_with python3
%package -n python3-module-%oname
Summary: A pure-Python implementation of the error function and inverse error function.
Group: Development/Python3

%description -n python3-module-%oname
pyerf is a pure-Python implementation of the error function
and inverse error function using the same functions that SciPy uses
(namely parts of the Cephes math library, cprob/ndtr.c and cprob/ndtri.c).

This is a useful package for when you need to calculate some error fuctions
but you don't want to install all of the SciPy/NumPy stuff.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Initial build for ALT.
