%define oname libpymux

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt2.git20140220
Summary: Python terminal multiplexer (Pure Python tmux clone)
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/libpymux/

# https://github.com/jonathanslenders/libpymux.git
Source: %name-%version.tar

%if_with python2
BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-pyte python-module-docopt
BuildRequires: python2.7(asyncio)
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-pyte python3-module-docopt
BuildRequires: python3(asyncio)
%endif

%py_provides %oname
%py_requires pyte docopt asyncio

%description
Library for terminal multiplexing in Python. This is the library that's
used by pymux, a pure Python tmux clone.

%if_with python3
%package -n python3-module-%oname
Summary: Python terminal multiplexer (Pure Python tmux clone)
Group: Development/Python3
%py3_provides %oname
%py3_requires pyte docopt asyncio

%description -n python3-module-%oname
Library for terminal multiplexing in Python. This is the library that's
used by pymux, a pure Python tmux clone.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.txt *.rst examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt2.git20140220
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20140220.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20140220.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140220
- Initial build for Sisyphus

