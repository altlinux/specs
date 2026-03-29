%def_with check

Name: python3-module-ciso8601
Version: 2.3.3
Release: alt1.1

Summary: ISO8601/RFC3339 date time strings converter
License: MIT
Group: Development/Python
Url: https://pypi.org/project/ciso8601
VCS: https://github.com/closeio/ciso8601

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytz
%endif

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%python3_sitelibdir/ciso8601
%python3_sitelibdir/ciso8601.*.so
%python3_sitelibdir/ciso8601-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.3.3-alt1.1
- Demodernized packaging.

* Fri Sep 19 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.3.3-alt1
- 2.3.3 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.3.2-alt1
- 2.3.2 released

* Thu Jul 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.0-alt2
- drop deps on now retired nose

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.0-alt1
- 2.3.0 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt1
- 2.2.0 released

* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.3-alt1
- initial
