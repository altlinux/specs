%define oname pathtools

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20111003
Summary: Path utilities for Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pathtools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gorakhargosh/pathtools.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel flask-sphinx-themes
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

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
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20111003
- Initial build for Sisyphus

