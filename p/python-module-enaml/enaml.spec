%define oname enaml

%def_without python3

Name: python-module-%oname
Version: 0.1.1
Release: alt2.git20120508
Epoch: 1
Summary: Enaml is not a Markup Language
License: BSD
Group: Development/Python
Url: https://github.com/enthought/enaml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/enthought/enaml.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute python-module-ply
BuildPreReq: python-module-sphinx-devel python-module-ETSDevTools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python3-module-ply python-tools-2to3
%endif

%description
Enaml is a framework for writing declarative user interfaces in Python.
It provides a Yaml-ish/Pythonic syntax language for declaring a ui
that binds and reacts to changes in the user's models. Code can freely
call back and forth between Python and Enaml.

%if_with python3
%package -n python3-module-%oname
Summary: Enaml is not a Markup Language (Python 3)
Group: Development/Python3
%add_python3_req_skip etsdevtools

%description -n python3-module-%oname
Enaml is a framework for writing declarative user interfaces in Python.
It provides a Yaml-ish/Pythonic syntax language for declaring a ui
that binds and reacts to changes in the user's models. Code can freely
call back and forth between Python and Enaml.

%package -n python3-module-%oname-tests
Summary: Tests for Enaml (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %epoch:%version-%release

%description -n python3-module-%oname-tests
Enaml is a framework for writing declarative user interfaces in Python.
It provides a Yaml-ish/Pythonic syntax language for declaring a ui
that binds and reacts to changes in the user's models. Code can freely
call back and forth between Python and Enaml.

This package contains tests for Enaml.
%endif

%package tests
Summary: Tests for Enaml
Group: Development/Python
Requires: %name = %epoch:%version-%release

%description tests
Enaml is a framework for writing declarative user interfaces in Python.
It provides a Yaml-ish/Pythonic syntax language for declaring a ui
that binds and reacts to changes in the user's models. Code can freely
call back and forth between Python and Enaml.

This package contains tests for Enaml.

%package pickles
Summary: Pickles for Enaml
Group: Development/Python

%description pickles
Enaml is a framework for writing declarative user interfaces in Python.
It provides a Yaml-ish/Pythonic syntax language for declaring a ui
that binds and reacts to changes in the user's models. Code can freely
call back and forth between Python and Enaml.

This package contains pickles for Enaml.

%package docs
Summary: Documentation for Enaml
Group: Development/Documentation

%description docs
Enaml is a framework for writing declarative user interfaces in Python.
It provides a Yaml-ish/Pythonic syntax language for declaring a ui
that binds and reacts to changes in the user's models. Code can freely
call back and forth between Python and Enaml.

This package contains documentation for Enaml.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source

%build
%python_build_debug
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i ||:
done
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
	mv $i py3_$i
done
popd
%endif
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname

%files
%doc *.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/py3_*
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests
%exclude %python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/%oname/tests

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html examples

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%_bindir/py3_*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Sun Jun 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.1.1-alt2.git20120508
- Fixed bild

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.1.1-alt1.git20120508
- Version 0.1.1

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1a-alt1.git20120125
- New snapshot

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1a-alt1.git20111221
- Initial build for Sisyphus

