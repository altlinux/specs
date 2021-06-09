%define _unpackaged_files_terminate_build 1
%define oname dbfread

Name: python3-module-%oname
Version: 2.0.7
Release: alt4
Summary: Read DBF Files with Python
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/dbfread/

# https://github.com/olemb/dbfread.git
Source: %{oname}-%{version}.tar.gz
Patch: dbfread-2.0.7-Fix-Pytest4.x-compatibility-errors.patch

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest
BuildRequires: python3-module-sphinx

%py3_provides %oname

%description
DBF is a file format used by databases such dBase, Visual FoxPro, and
FoxBase+. This library reads DBF files and returns the data as native
Python data types for further processing. It is primarily intended for
batch jobs and one-off scripts.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
DBF is a file format used by databases such dBase, Visual FoxPro, and
FoxBase+. This library reads DBF files and returns the data as native
Python data types for further processing. It is primarily intended for
batch jobs and one-off scripts.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
DBF is a file format used by databases such dBase, Visual FoxPro, and
FoxBase+. This library reads DBF files and returns the data as native
Python data types for further processing. It is primarily intended for
batch jobs and one-off scripts.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
DBF is a file format used by databases such dBase, Visual FoxPro, and
FoxBase+. This library reads DBF files and returns the data as native
Python data types for further processing. It is primarily intended for
batch jobs and one-off scripts.

This package contains documentation for %oname.

%prep
%setup -q -n %{oname}-%{version}
%patch -p1

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install

%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
py.test3 -vv

%files
%doc *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Wed Jun 09 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.7-alt4
- Drop python2 support.

* Wed May 29 2019 Stanislav Levin <slev@altlinux.org> 2.0.7-alt3
- Fixed Pytest4.x compatibility errors.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.7-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.7-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.4-alt1.git20150207.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.4-alt1.git20150207.1
- NMU: Use buildreq for BR.

* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1.git20150207
- Initial build for Sisyphus

