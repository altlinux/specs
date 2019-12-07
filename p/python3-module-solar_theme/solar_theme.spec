%define oname solar_theme

Name: python3-module-%oname
Version: 1.3.2
Release: alt2

Summary: Theme for Python Sphinx
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/solar-theme/
BuildArch: noarch

# https://github.com/biotechcoder/solar-theme.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-sphinxcontrib-apidoc
BuildRequires: python3-module-nose

%py3_provides %oname
%py3_requires sphinx


%description
Solar is an attempt to create a theme for the Python Sphinx
documentation generator based on the Solarized color scheme.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Solar is an attempt to create a theme for the Python Sphinx
documentation generator based on the Solarized color scheme.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Solar is an attempt to create a theme for the Python Sphinx
documentation generator based on the Solarized color scheme.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-apidoc|sphinx-apidoc-3|' Makefile
sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%make docs
%make -C docs pickle

%install
%python3_install

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Sat Dec 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.2-alt2
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1.git20140312.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.2-alt1.git20140312.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.2-alt1.git20140312.1
- NMU: Use buildreq for BR.

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1.git20140312
- Initial build for Sisyphus

