%define oname zmqdecorators

%def_with python3

Name: python-module-%oname
Version: 0.7.4
Release: alt1.dev.git20150202
Summary: Decorators for pyZMQ to make it almost as easy to use a DBUS
License: LGPLv2.1+
Group: Development/Python
Url: https://pypi.python.org/pypi/zmqdecorators/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rambo/python-zmqdecorators.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests git
BuildPreReq: python-module-tornado python-module-zmq
BuildPreReq: python-module-pybonjour
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests git
BuildPreReq: python3-module-tornado python3-module-zmq
BuildPreReq: python3-module-pybonjour
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires tornado zmq pybonjour

%description
Decorators for pyZMQ to make it almost as easy to use a DBUS (requires
Bonjour for discovery magic)

%if_with python3
%package -n python3-module-%oname
Summary: Decorators for pyZMQ to make it almost as easy to use a DBUS
Group: Development/Python3
%py3_provides %oname
%py3_requires tornado zmq pybonjour

%description -n python3-module-%oname
Decorators for pyZMQ to make it almost as easy to use a DBUS (requires
Bonjour for discovery magic)
%endif

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

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
%python_install
mv %buildroot%python_sitelibdir/%oname-%{version}*-py%_python_version.egg-info \
	%buildroot%python_sitelibdir/%oname-%version-py%_python_version.egg-info

%if_with python3
pushd ../python3
%python3_install
mv %buildroot%python3_sitelibdir/%oname-%{version}*-py%_python3_version.egg-info \
	%buildroot%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
popd
%endif

%check
python setup.py test
py.test -vv %oname/*.py
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv %oname/*.py
popd
%endif

%files
%doc *.md examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%python3_sitelibdir/*
%endif

%changelog
* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt1.dev.git20150202
- Initial build for Sisyphus

