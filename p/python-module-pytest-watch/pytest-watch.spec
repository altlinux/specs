%define oname pytest-watch

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.0.0
Release: alt2.git20150206
Summary: Local continuous test runner with pytest and watchdog
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-watch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/joeyespo/pytest-watch.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-pytest python-module-watchdog
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-docopt python-module-watchdog
#BuildPreReq: python-module-argh python-module-yaml
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-docopt python3-module-watchdog
#BuildPreReq: python3-module-argh python3-module-yaml
BuildPreReq: python-tools-2to3
BuildRequires: python3-module-pytest python3-module-watchdog
%endif

%py_provides pytest_watch
#%py_requires docopt watchdog pytest

%description
pytest-watch a zero-config CLI tool that runs pytest, and reruns it when
a file in your project changes.

%package -n python3-module-%oname
Summary: Local continuous test runner with pytest and watchdog
Group: Development/Python3
%py3_provides pytest_watch
#%py3_requires docopt watchdog pytest

%description -n python3-module-%oname
pytest-watch a zero-config CLI tool that runs pytest, and reruns it when
a file in your project changes.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.0.0-alt2.git20150206
- Rebuild with "def_disable check"
- Cleanup buildreq

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150206
- Version 1.0.0

* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20150111
- Initial build for Sisyphus

