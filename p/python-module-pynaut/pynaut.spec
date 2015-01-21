%define oname pynaut

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 0.2.11
Release: alt1.git20150121
Summary: A tool for recursively exploring arbitrary python objects
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pynaut/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/stnbu/pynaut.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-urwid python-module-UniCurses
BuildPreReq: python-module-nose ipython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-urwid python3-module-UniCurses
BuildPreReq: python3-module-nose ipython3
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires urwid unicurses IPython

%description
pynaunt allows you to deeply explore and introspect arbitrary python
objects.

%package -n python3-module-%oname
Summary: A tool for recursively exploring arbitrary python objects
Group: Development/Python3
%py3_provides %oname
%py3_requires urwid unicurses IPython

%description -n python3-module-%oname
pynaunt allows you to deeply explore and introspect arbitrary python
objects.

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
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.11-alt1.git20150121
- Initial build for Sisyphus

