%define oname progressbar2

%def_with python3

Name: python-module-%oname
Version: 3.34.4
Release: alt1.1
Summary: Text progress bar library for Python
License: LGPLv2.1+ or BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/progressbar2/

# https://github.com/WoLpH/python-progressbar.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-doc.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pytest python-module-pytest-runner python-module-pytest-cov python-module-pytest-pep8 python-module-pytest-flakes
BuildRequires: python2.7(python_utils) python2.7(changelog)
BuildRequires: python-module-sphinx-devel
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest python3-module-pytest-runner python3-module-pytest-cov python3-module-pytest-pep8 python3-module-pytest-flakes
BuildRequires: python3(python_utils) python3(changelog)
%endif

%py_provides progressbar
Conflicts: python-module-progressbar

%description
A text progress bar is typically used to display the progress of a long
running operation, providing a visual cue that processing is underway.

The ProgressBar class manages the current progress, and the format of
the line is given by a number of widgets. A widget is an object that may
display differently depending on the state of the progress bar.

%if_with python3
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
%endif

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
%patch1 -p1

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
# tests may fail on 32bit arches due to time overflow
export PYTHONPATH=$PWD
py.test progressbar tests ||:
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test3 progressbar tests ||:
popd
%endif

%files
%doc examples.py *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc examples.py *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.34.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.34.4-alt1
- Updated to upstream version 3.34.4.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.9-alt1.git20141119.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.6.9-alt1.git20141119.1
- NMU: Use buildreq for BR.

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.9-alt1.git20141119
- Initial build for Sisyphus

