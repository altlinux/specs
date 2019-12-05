%define oname mincss

Name: python3-module-%oname
Version: 0.8.4
Release: alt2

Summary: Clears the junk out of your CSS
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/mincss/
BuildArch: noarch

# https://github.com/peterbe/mincss.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python3-module-sphinx

%py3_provides %oname
%py3_requires lxml cssselect


%description
Clears the junk out of your CSS by finding out which selectors are
actually not used in your HTML.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Clears the junk out of your CSS by finding out which selectors are
actually not used in your HTML.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Clears the junk out of your CSS by finding out which selectors are
actually not used in your HTML.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ \( -name '*.py' -o -name 'fake_phantomjs' \))

%build
%python3_build_debug

%install
%python3_install

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc *.rst example proxy
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.8.4-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.4-alt1.git20150203.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.4-alt1.git20150203.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.4-alt1.git20150203.1
- NMU: Use buildreq for BR.

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt1.git20150203
- Initial build for Sisyphus

