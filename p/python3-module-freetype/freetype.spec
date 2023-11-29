%define oname freetype

Name: python3-module-%oname
Version: 2.4.0
Release: alt1

Summary: Freetype python bindings
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/freetype-py/

BuildArch: noarch

# https://github.com/rougier/freetype-py.git
Source: %name-%version.tar
Patch1: %oname-1.1-alt-build.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: pyinstaller
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: libfreetype

BuildRequires: /proc

Requires: lib%oname

%description
Freetype python provides bindings for the FreeType library. Only the
high-level API is bound.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Freetype python provides bindings for the FreeType library. Only the
high-level API is bound.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Freetype python provides bindings for the FreeType library. Only the
high-level API is bound.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

sed -i 's|sphinx-build|&-3|' doc/Makefile

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%tox_check_pyproject

%files
%doc *.rst *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc examples doc/_build/html

%changelog
* Tue Nov 28 2023 Grigory Ustinov <grenka@altlinux.org> 2.4.0-alt1
- Build new version (Closes: #48597).

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.1.0.post1-alt2
- Build for python2 disabled.

* Wed May 15 2019 Grigory Ustinov <grenka@altlinux.org> 2.1.0.post1-alt1
- Build new version (Closes: #36320).

* Thu Jan 24 2019 Grigory Ustinov <grenka@altlinux.org> 2.0-alt1
- Build new version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1-alt1
- Updated to upstream version 1.1.

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.git20150409.1.1.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.git20150409.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1.git20150409.1
- NMU: Use buildreq for BR.

* Wed Apr 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20150409
- Initial build for Sisyphus

