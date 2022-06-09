%define oname commentjson

%def_with check

Name: python3-module-%oname
Version: 0.9.0
Release: alt1

Summary: Add Python and JavaScript style comments in your JSON files

License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/commentjson/

# https://github.com/vaidik/commentjson.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-six
BuildRequires: python3-module-lark-parser
BuildRequires: python3-test
%endif

%py3_provides %oname
%py3_requires json

BuildArch: noarch

%description
commentjson (Comment JSON) is a Python package that helps you create
JSON files with Python and JavaScript style inline comments. Its API is
very similar to the Python standard library's json module.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
commentjson (Comment JSON) is a Python package that helps you create
JSON files with Python and JavaScript style inline comments. Its API is
very similar to the Python standard library's json module.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst docs/source/*.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Fri Jun 10 2022 Grigory Ustinov <grenka@altlinux.org> 0.9.0-alt1
- Build new version.

* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4-alt1.git20150110.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.git20150110.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20150110.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20150110
- Initial build for Sisyphus

