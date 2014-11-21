%define oname nosepipe

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt1.git20141114
Summary: Plugin for the nose testing framework for running tests in a subprocess
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/nosepipe/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dmccombs/nosepipe.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
Plugin for the nose testing framework for running tests in a subprocess.

Use nosetests --with-process-isolation to enable the plugin. When
enabled, each test is run in a separate process.

%package -n python3-module-%oname
Summary: Plugin for the nose testing framework for running tests in a subprocess
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Plugin for the nose testing framework for running tests in a subprocess.

Use nosetests --with-process-isolation to enable the plugin. When
enabled, each test is run in a separate process.

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
%doc *.txt *.md *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20141114
- Initial build for Sisyphus

