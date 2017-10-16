%define oname pathtools

%def_with python3

Name: python-module-%oname
Version: 0.1.2
Release: alt1
Summary: Path utilities for Python
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pathtools/

# https://github.com/gorakhargosh/pathtools.git
Source: %oname-%version.tar

Patch1: %oname-%version-alt-docs.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-dev python-module-setuptools
BuildRequires: flask-sphinx-themes python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
%endif

%description
Pattern matching and various utilities for file systems paths.

%package -n python3-module-%oname
Summary: Path utilities for Python
Group: Development/Python3

%description -n python3-module-%oname
Pattern matching and various utilities for file systems paths.

%prep
%setup -n %oname-%version
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/
mkdir -p docs/source/_themes
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
* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.2-alt1
- Updated to upstream version 0.1.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20111003.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1.git20111003.1
- NMU: Use buildreq for BR.

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20111003
- Initial build for Sisyphus

