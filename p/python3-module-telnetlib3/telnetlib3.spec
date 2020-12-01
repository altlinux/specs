%define _unpackaged_files_terminate_build 1
%define oname telnetlib3

%def_enable check

Name: python3-module-%oname
Version: 1.0.3
Release: alt1
Summary: Telnet server and client Protocol library using asyncio
License: ISC
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/telnetlib3/

# https://github.com/jquast/telnetlib3.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(asyncio)
BuildRequires: python3-module-html5lib

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%py3_provides %oname
%py3_requires asyncio

%description
telnetlib3 is a Telnet Client and Server Protocol library for python.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc LICENSE.txt *.rst docs/*.rst
%_bindir/*
%python3_sitelibdir/*

%changelog
* Tue Dec 01 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.3-alt1
- Automatically updated to 1.0.3.
- Clean transfer on python3.

* Tue Apr 23 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- new version 1.0.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Updated to upstream version 1.0.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.3-alt1.git20140629.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1.git20140629.1
- NMU: Use buildreq for BR.

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20140629
- Initial build for Sisyphus

