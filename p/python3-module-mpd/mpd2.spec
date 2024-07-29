%def_with check

Name: python3-module-mpd
Version: 3.1.1
Release: alt1

Summary: A client interface for the Music Player Daemon

Group: Development/Python3
License: LGPLv3+
URL: https://pypi.org/project/python-mpd2
VCS: https://github.com/Mic92/python-mpd2

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-twisted
%endif

BuildArch: noarch

%description
Python library providing a client interface for MPD.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE.txt README.rst
%python3_sitelibdir/mpd
%python3_sitelibdir/python_mpd2-%version.dist-info

%changelog
* Sun Jul 28 2024 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Automatically updated to 3.1.1.

* Tue Mar 08 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.5-alt1
- Build new version.

* Thu Jun 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.5-alt3
- drop excessive python3-module-jinja2-tests BR

* Thu Jun 03 2021 Grigory Ustinov <grenka@altlinux.org> 0.5.5-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 0.5.5-alt1
- Autobuild version bump to 0.5.5

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.4-alt1.1
- NMU: Use buildreq for BR.

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 0.5.4-alt1
- Autobuild version bump to 0.5.4

* Thu Mar 27 2014 Fr. Br. George <george@altlinux.ru> 0.5.3-alt1
- Autobuild version bump to 0.5.3

* Thu Mar 27 2014 Fr. Br. George <george@altlinux.ru> 0.5.2-alt1
- Initial build from scratch

