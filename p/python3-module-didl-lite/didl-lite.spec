Name: python3-module-didl-lite
Version: 1.4.0
Release: alt1

Summary: DIDL-Lite (Digital Item Declaration Language) tools for Python
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/python-didl-lite/

Source0: %name-%version-%release.tar

BuildArch: noarch

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
%doc LICENSE.* README.*
%python3_sitelibdir/didl_lite
%python3_sitelibdir/python_didl_lite-%version.dist-info

%changelog
* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.2-alt1
- 1.3.2 released

* Tue Oct 12 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Thu Apr 08 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.6-alt1
- 1.2.6 released

* Tue Jan 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.4-alt1
- initial
