%define module_name blinker

Name: python3-module-%module_name
Version: 1.5
Release: alt1

Group: Development/Python3
License: MIT License
Summary: Fast, simple object-to-object and broadcast signaling
URL: https://pypi.org/project/blinker/

# https://github.com/pallets-eco/blinker
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel)

%description
Blinker provides a fast dispatching system that allows any number of
interested parties to subscribe to events, or "signals".

Signal receivers can subscribe to specific senders or receive signals
sent by any sender.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc docs/ CHANGES.rst LICENSE.rst README.rst MANIFEST.in
%python3_sitelibdir/%{module_name}*

%changelog
* Tue Jan 03 2023 Anton Vyatkin <toni@altlinux.org> 1.5-alt1
- new version 1.5

* Tue Jun 29 2021 Grigory Ustinov <grenka@altlinux.org> 1.4-alt1
- Build new version.

* Mon Jun 07 2021 Grigory Ustinov <grenka@altlinux.org> 1.3-alt2.git20130703
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt1.git20130703.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20130703.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3-alt1.git20130703.1
- NMU: Use buildreq for BR.

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20130703
- Shapshot from git
- Added module for Python 3

* Sun Oct 20 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3-alt1
- build for ALT
