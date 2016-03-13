%define oname progressbar2

%def_with python3

Name: python-module-%oname
Version: 2.6.9
Release: alt1.git20141119.1.1
Summary: Text progress bar library for Python
License: LGPLv2.1+ or BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/progressbar2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/WoLpH/python-progressbar.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides progressbar
Conflicts: python-module-progressbar

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pluggy python-module-py python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-pluggy python3-module-py python3-module-setuptools xz
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-pytest python3-module-pytest rpm-build-python3 time

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.9-alt1.git20141119.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.6.9-alt1.git20141119.1
- NMU: Use buildreq for BR.

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.9-alt1.git20141119
- Initial build for Sisyphus

