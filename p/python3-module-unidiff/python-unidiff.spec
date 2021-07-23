Name:		python3-module-unidiff
Version:	0.1
Release:	alt1.3
License:	MIT
Source:		v%{version}.tar.gz
Group:		Development/Python3
Summary:	Parse and interact with unified diff data
BuildArch:	noarch
URL:		https://github.com/matiasb/python-unidiff
BuildPreReq:	rpm-build-python3

%description
Simple Python library to parse and interact with unified diff data.

%prep
%setup -n python-unidiff-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/*

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.1-alt1.3
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 22 2014 Fr. Br. George <george@altlinux.ru> 0.1-alt1
- Initial build

