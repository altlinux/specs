%define oname pathtools

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20111003.1
Summary: Path utilities for Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pathtools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gorakhargosh/pathtools.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel flask-sphinx-themes
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: flask-sphinx-themes python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv rpm-build-python3 time

%description
Pattern matching and various utilities for file systems paths.

%package -n python3-module-%oname
Summary: Path utilities for Python
Group: Development/Python3

%description -n python3-module-%oname
Pattern matching and various utilities for file systems paths.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/
cp -fR %_datadir/flask-sphinx-themes/* docs/source/_themes/

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%files
%doc AUTHORS README docs/build/html
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS README docs/build/html
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1.git20111003.1
- NMU: Use buildreq for BR.

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20111003
- Initial build for Sisyphus

