%define _unpackaged_files_terminate_build 1
%define oname pymeta3

%def_disable check

Name: python3-module-%oname
Version: 0.5.1
Release: alt2
Summary: Pattern-matching language based on OMeta for Python 2 and 3
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/PyMeta3/

# https://github.com/wbond/pymeta3.git
Source0: https://pypi.python.org/packages/ce/af/409edba35fc597f1e386e3860303791ab5a28d6cc9a8aecbc567051b19a9/PyMeta3-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname pymeta

BuildRequires: python3-module-zope python3-module-pytest

%description
This is a fork of PyMeta 0.5.0 that supports Python 2 and 3.

PyMeta is an implementation of OMeta, an object-oriented
pattern-matching language developed by Alessandro Warth
(http://www.cs.ucla.edu/~awarth/ometa/). PyMeta provides a compact
syntax based on Parsing Expression Grammars (PEGs) for common lexing,
parsing and tree-transforming activities in a way that's easy to reason
about for Python programmers.

%prep
%setup -n PyMeta3-%{version}

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=$PWD
py.test-%_python3_version -vv

%files
%doc NEWS README examples extras
%python3_sitelibdir/*

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 0.5.1-alt2
- Drop python2 support.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20150114.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.git20150114.1
- NMU: Use buildreq for BR.

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20150114
- Initial build for Sisyphus

