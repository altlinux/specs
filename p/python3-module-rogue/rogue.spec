%define oname rogue

Name: python3-module-%oname
Version: 0.0.2
Release: alt1

Summary: A devious little programming language
License: GPLv3+
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/rogue/
# https://bitbucket.org/johannestaas/rogue.git

Source: %name-%version.tar
Patch0: python2-to-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%py3_provides %oname


%description
A devious little programming language.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A devious little programming language.

This package contains tests for %oname.

%prep
%setup
%patch0 -p1

## py2 -> py3
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')
##

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py build_ext -i

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*


%changelog
* Mon Nov 25 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.2-alt1
- version updated to 0.0.2
- porting to python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.1-alt2.git20150217.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.1-alt2.git20150217
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.git20150217.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20150217
- Initial build for Sisyphus

