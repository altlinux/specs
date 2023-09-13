Name: python3-module-adb-shell
Version: 0.4.4
Release: alt1

Summary: ADB shell and FileSync functionality implemented in Python 
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/adb-shell/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
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
%python3_sitelibdir/adb_shell
%python3_sitelibdir/adb_shell-%version.dist-info

%changelog
* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.4-alt1
- 0.4.4 released

* Fri Jul 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.3-alt1
- 0.4.3 released

* Thu Feb 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt1
- 0.4.2 released

* Tue Jun 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.4-alt1
- 0.3.4 released

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.1-alt1
- 0.2.1 released

* Mon Jul 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- initial
