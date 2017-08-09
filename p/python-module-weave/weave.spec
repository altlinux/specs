%define oname weave

%def_without python3

Name: python-module-%oname
Version: 0.16.0
Release: alt1
Summary: Weave - tools for including C/C++ code within Python code.
License: BSD
Group: Development/Python
Url: https://github.com/scipy/weave

# https://github.com/scipy/weave.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel python-module-numpy-testing python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-numpy-testing python3-module-nose
%endif

%description
Weave provides tools for including C/C++ code within Python code.
Inlining C/C++ code within Python generally results
in speedups of 1.5x to 30x over algorithms written in pure Python.

Weave is the stand-alone version of the deprecated Scipy submodule scipy.weave.
It is Python 2.x only, and is provided for users that need new versions of Scipy
(from which the weave submodule may be removed) but have existing code
that still depends on scipy.weave. For new code, users are recommended to use Cython.

%if_with python3
%package -n python3-module-%oname
Summary: Weave - tools for including C/C++ code within Python code
Group: Development/Python3

%description -n python3-module-%oname
Weave provides tools for including C/C++ code within Python code.
Inlining C/C++ code within Python generally results
in speedups of 1.5x to 30x over algorithms written in pure Python.

Weave is the stand-alone version of the deprecated Scipy submodule scipy.weave.
It is Python 2.x only, and is provided for users that need new versions of Scipy
(from which the weave submodule may be removed) but have existing code
that still depends on scipy.weave. For new code, users are recommended to use Cython.
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
PYTHONPATH=$(pwd) python runtests.py
%if_with python3
pushd ../python3
PYTHONPATH=$(pwd) python3 runtests.py
popd
%endif

%files
%doc README.rst LICENSE.txt examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst LICENSE.txt examples
%python3_sitelibdir/*
%endif

%changelog
* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.16.0-alt1
- Initial build for ALT.
