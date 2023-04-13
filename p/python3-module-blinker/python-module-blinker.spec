%define oname blinker

%def_with check

Name: python3-module-%oname
Version: 1.6.2
Release: alt1

Group: Development/Python3
License: MIT
Summary: Fast, simple object-to-object and broadcast signaling
URL: https://pypi.org/project/blinker/
VCS: https://github.com/pallets-eco/blinker

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-pytest-asyncio
%endif

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
%doc docs *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Thu Apr 13 2023 Anton Vyatkin <toni@altlinux.org> 1.6.2-alt1
- New version 1.6.2.

* Mon Apr 10 2023 Anton Vyatkin <toni@altlinux.org> 1.6.1-alt1
- New version 1.6.1.

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
