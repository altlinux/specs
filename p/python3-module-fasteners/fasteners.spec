%define oname fasteners

%def_with check

Name: python3-module-fasteners
Version: 0.19
Release: alt1

Summary: A python package that provides useful locks

License: Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/fasteners
VCS: https://github.com/harlowja/fasteners

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-diskcache
BuildRequires: python3-module-eventlet
BuildRequires: python3-module-more-itertools
BuildRequires: python3-module-django-guardian
BuildRequires: python3-module-django-guardian-tests
%endif

BuildArch: noarch

%description
A python package that provides useful locks.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
export DJANGO_SETTINGS_MODULE=guardian.testapp.testsettings
py.test-3 -v

%files
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Thu Sep 21 2023 Grigory Ustinov <grenka@altlinux.org> 0.19-alt1
- Automatically updated to 0.19.

* Fri Oct 21 2022 Grigory Ustinov <grenka@altlinux.org> 0.18-alt1
- Build new version.

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 0.16.3-alt1
- new version 0.16.3 (with rpmrb script)

* Tue Aug 03 2021 Grigory Ustinov <grenka@altlinux.org> 0.15-alt3
- Fixed BuildRequires.
- Fixed license tag.

* Tue Apr 27 2021 Vitaly Lipatov <lav@altlinux.ru> 0.15-alt2
- drop test.py

* Fri Oct 30 2020 Vitaly Lipatov <lav@altlinux.ru> 0.15-alt1
- separate build python3 module version 0.15
- cleanup spec

* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.13.0-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.13.0-alt1
- Initial package.

