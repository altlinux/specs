%define oname progressbar2

%def_with python3

Name: python-module-%oname
Version: 2.6.9
Release: alt1.git20141119
Summary: Text progress bar library for Python
License: LGPLv2.1+ or BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/progressbar2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/WoLpH/python-progressbar.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides progressbar
Conflicts: python-module-progressbar

%description
A text progress bar is typically used to display the progress of a long
running operation, providing a visual cue that processing is underway.

The ProgressBar class manages the current progress, and the format of
the line is given by a number of widgets. A widget is an object that may
display differently depending on the state of the progress bar.

%package -n python3-module-%oname
Summary: Text progress bar library for Python
Group: Development/Python3
%py3_provides progressbar
Conflicts: python3-module-progressbar

%description -n python3-module-%oname
A text progress bar is typically used to display the progress of a long
running operation, providing a visual cue that processing is underway.

The ProgressBar class manages the current progress, and the format of
the line is given by a number of widgets. A widget is an object that may
display differently depending on the state of the progress bar.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A text progress bar is typically used to display the progress of a long
running operation, providing a visual cue that processing is underway.

The ProgressBar class manages the current progress, and the format of
the line is given by a number of widgets. A widget is an object that may
display differently depending on the state of the progress bar.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A text progress bar is typically used to display the progress of a long
running operation, providing a visual cue that processing is underway.

The ProgressBar class manages the current progress, and the format of
the line is given by a number of widgets. A widget is an object that may
display differently depending on the state of the progress bar.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=$PWD
py.test
python examples.py
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test-%_python3_version
python3 examples.py
popd
%endif

%files
%doc ChangeLog.yaml examples.py *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog.yaml examples.py *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.9-alt1.git20141119
- Initial build for Sisyphus

