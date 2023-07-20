Name: python3-module-ciso8601
Version: 2.3.0
Release: alt2

Summary: ISO8601/RFC3339 date time strings converter
License: MIT
Group: Development/Python
Url: https://pypi.org/project/ciso8601/

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/ciso8601
%python3_sitelibdir/ciso8601.*.so
%python3_sitelibdir/ciso8601-%version.dist-info

%changelog
* Thu Jul 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.0-alt2
- drop deps on now retired nose

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.0-alt1
- 2.3.0 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt1
- 2.2.0 released

* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.3-alt1
- initial
