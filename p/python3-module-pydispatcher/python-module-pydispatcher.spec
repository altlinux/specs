%define oname PyDispatcher
%define sname pydispatcher

%def_with check

Name: python3-module-%sname
Version: 2.0.6
Release: alt1

Summary: Multi-producer-multi-consumer signal dispatching mechanism

Group: Development/Python3
License: BSD-like, see license.txt
Url: http://pydispatcher.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# bzr branch lp:pydispatcher
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
%endif

%py3_provides %sname

%description
The dispatcher provides loosely-coupled message passing between
Python objects (signal senders and receivers). It began as one of the
highest-rated recipes on the Python Cookbook website.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The dispatcher provides loosely-coupled message passing between
Python objects (signal senders and receivers). It began as one of the
highest-rated recipes on the Python Cookbook website.

This package contains documentation for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test-3 -v

%files
%doc license.txt
%python3_sitelibdir/pydispatch/
%python3_sitelibdir/*egg-info

%changelog
* Mon Oct 31 2022 Grigory Ustinov <grenka@altlinux.org> 2.0.6-alt1
- Build new version.
- Build with check.

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.5-alt2.bzr20150114
- Drop python2 support.

* Thu Apr 30 2020 Stanislav Levin <slev@altlinux.org> 2.0.5-alt1.bzr20150114.3
- Fixed FTBFS.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.0.5-alt1.bzr20150114.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.5-alt1.bzr20150114.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt1.bzr20150114
- Version 2.0.5

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1.bzr20150101
- Version 2.0.4

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1.bzr20130112
- Version 2.0.3
- Added module for Python 3

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt2.1.1
- Rebuild with Python-2.7

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt2.1
- Rebuilt with python 2.6

* Fri Feb 20 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt2
- build as noarch

* Mon Dec 01 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- initial build for ALT Linux Sisyphus
