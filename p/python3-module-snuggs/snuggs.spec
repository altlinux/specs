%define _unpackaged_files_terminate_build 1
%define oname snuggs

%def_with check

Name: python3-module-%oname
Version: 1.4.7
Release: alt2
Summary: Snuggs are s-expressions for Numpy
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/snuggs

# https://github.com/mapbox/snuggs.git
Source: %name-%version.tar
Patch: snuggs-fix-test-failures.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(hypothesis)
BuildRequires: python3(numpy)
BuildRequires: python3(pyparsing)
BuildRequires: python3(pytest)
%endif

%description
Snuggs are s-expressions for Numpy.

%prep
%setup
%patch -p1

%build
%python3_build_debug

%install
%python3_install

%check
py.test3 -vv

%files
%doc *.txt *.rst
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%python3_sitelibdir/%oname/__init__.py
%python3_sitelibdir/%oname/__pycache__/__init__.cpython-*.py*

%changelog
* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 1.4.7-alt2
- Fixed FTBFS.

* Fri Sep 04 2020 Grigory Ustinov <grenka@altlinux.org> 1.4.7-alt1
- Automatically updated to 1.4.7.

* Tue Sep 01 2020 Grigory Ustinov <grenka@altlinux.org> 1.4.6-alt2
- Drop python2 support.

* Wed Aug 14 2019 Stanislav Levin <slev@altlinux.org> 1.4.6-alt1
- 1.4.1 -> 1.4.6.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.1-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt3
- Updated build dependencies.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt2
- Fixed build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt1.git20150403.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt1.git20150403.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20150403
- Initial build for Sisyphus

