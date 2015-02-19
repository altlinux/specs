%define oname CommandLineApp

%def_without python3

Name: python-module-%oname
Version: 3.0.7
Release: alt1.hg20120720
Summary: Base class for command line applications
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/CommandLineApp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/dhellmann/commandlineapp
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Paver python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Paver python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname commandlineapp

%description
Base class for building command line applications.

The CommandLineApp class makes creating command line applications as
simple as defining callbacks to handle options when they appear in
sys.argv.

%package -n python3-module-%oname
Summary: Base class for command line applications
Group: Development/Python3
%py3_provides %oname commandlineapp

%description -n python3-module-%oname
Base class for building command line applications.

The CommandLineApp class makes creating command line applications as
simple as defining callbacks to handle options when they appear in
sys.argv.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
paver generate_setup
%python_build_debug

%if_with python3
pushd ../python3
paver.py3 generate_setup
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

mv docs/source doc

%check
python setup.py test
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
popd
%endif

%files
%doc ChangeLog *.txt doc
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog *.txt doc
%python3_sitelibdir/*
%endif

%changelog
* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.7-alt1.hg20120720
- Initial build for Sisyphus

