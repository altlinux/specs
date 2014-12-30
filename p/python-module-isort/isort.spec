%define oname isort

%def_with python3

Name: python-module-%oname
Version: 3.9.4
Release: alt1.git20141229
Summary: A Python utility / library to sort Python imports
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/isort/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/timothycrosley/isort.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pytest python-module-mock python-module-pies
BuildPreReq: python-module-natsort python-module-enum34
BuildPreReq: python-module-py
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pytest python3-module-mock python3-module-pies
BuildPreReq: python3-module-natsort python3-module-enum34
BuildPreReq: python3-module-py
%endif

%py_provides %oname

%description
isort is a Python utility / library to sort imports alphabetically, and
automatically separated into sections. It provides a command line
utility, Python library and plugins for various editors to quickly sort
all your imports. It currently cleanly supports Python 2.6 - 3.4 using
pies to achieve this without ugly hacks and/or py2to3.

%package -n python3-module-%oname
Summary: A Python utility / library to sort Python imports
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
isort is a Python utility / library to sort imports alphabetically, and
automatically separated into sections. It provides a command line
utility, Python library and plugins for various editors to quickly sort
all your imports. It currently cleanly supports Python 2.6 - 3.4 using
pies to achieve this without ugly hacks and/or py2to3.

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
%endif
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*

%changelog
* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.4-alt1.git20141229
- Version 3.9.4

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt1.git20141218
- Version 3.9.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt1.git20140804
- Initial build for Sisyphus

