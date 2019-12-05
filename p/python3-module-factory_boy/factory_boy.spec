%define oname factory_boy

Name: python3-module-%oname
Version: 2.4.1
Release: alt2

Summary: A test fixtures replacement for Python
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/factory_boy/
BuildArch: noarch

# https://github.com/rbarrois/factory_boy.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx

%py3_provides factory


%description
factory_boy is a fixtures replacement based on thoughtbot's
factory_girl.

As a fixtures replacement tool, it aims to replace static, hard to
maintain fixtures with easy-to-use factories for complex object.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
factory_boy is a fixtures replacement based on thoughtbot's
factory_girl.

As a fixtures replacement tool, it aims to replace static, hard to
maintain fixtures with easy-to-use factories for complex object.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
factory_boy is a fixtures replacement based on thoughtbot's
factory_girl.

As a fixtures replacement tool, it aims to replace static, hard to
maintain fixtures with easy-to-use factories for complex object.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.4.1-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.4.1-alt1.git20140903.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.1-alt1.git20140903.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.4.1-alt1.git20140903.1
- NMU: Use buildreq for BR.

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1.git20140903
- Initial build for Sisyphus

