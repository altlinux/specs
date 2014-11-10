%define oname detox

%def_with python3

Name: python-module-%oname
Version: 0.9.3
Release: alt1
Summary: Distributing activities of the tox tool
License: AGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/detox/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tox python-module-eventlet
BuildPreReq: python-module-greenlet python-module-virtualenv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tox python3-module-eventlet
BuildPreReq: python3-module-greenlet python3-module-virtualenv
%endif

%py_provides %oname

%description
detox is the distributed version of "tox". It makes efficient use of
multiple CPUs by running all possible activities in parallel. It has the
same options and configuration that tox has.

%package -n python3-module-%oname
Summary: Distributing activities of the tox tool
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
detox is the distributed version of "tox". It makes efficient use of
multiple CPUs by running all possible activities in parallel. It has the
same options and configuration that tox has.

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
export PYTHONPATH=%buildroot%python_sitelibdir
export PATH=$PATH:%buildroot%_bindir
py.test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc CHANGELOG
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1
- Initial build for Sisyphus

