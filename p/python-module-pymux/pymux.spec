%define oname pymux

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.git20141024.1
Summary: Python terminal multiplexer (Pure Python tmux clone)
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pymux/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jonathanslenders/pymux.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests /dev/pts
BuildPreReq: python-module-libpymux python-module-asyncio
BuildPreReq: python-module-pyte python-module-docopt
BuildPreReq: python-module-asyncio_amp
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests /dev/pts
BuildPreReq: python3-module-libpymux python3-module-asyncio
BuildPreReq: python3-module-pyte python3-module-docopt
BuildPreReq: python3-module-asyncio_amp
%endif

%py_provides %oname
Requires: /dev/pts
%py_requires libpymux asyncio pyte docopt asyncio_amp

%description
Still experimental, but the idea is to create a fully functional tmux
clone in pure Python.

%package -n python3-module-%oname
Summary: Python terminal multiplexer (Pure Python tmux clone)
Group: Development/Python3
%py3_provides %oname
Requires: /dev/pts
%py3_requires libpymux asyncio pyte docopt asyncio_amp

%description -n python3-module-%oname
Still experimental, but the idea is to create a fully functional tmux
clone in pure Python.

%package -n %oname
Summary: Python terminal multiplexer (Pure Python tmux clone)
Group: Terminals
Requires: python3-module-%oname = %EVR

%description -n %oname
Still experimental, but the idea is to create a fully functional tmux
clone in pure Python.

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
%doc *.txt *.rst
%python_sitelibdir/*
%endif

%files -n %oname
%_bindir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20141024.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141024
- Initial build for Sisyphus

