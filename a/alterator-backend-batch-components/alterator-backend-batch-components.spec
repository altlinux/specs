%define _unpackaged_files_terminate_build 1

Name: alterator-backend-batch-components
Version: 0.3.1
Release: alt1

Summary: Alterator backends for getting information about all components
License: GPLv3
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-backend-batch_components.git

BuildArch: noarch
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
BuildRequires: python3-devel

Requires: alterator-backend-component
Requires: alt-components-base
Requires: alterator-entry >= 0.3.1
Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.14
Requires: alterator-backend-systeminfo >= 0.4.1

%description
%summary.

%prep
%setup

%install
%makeinstall_std

%files
%dir %_libexecdir/%name
%_libexecdir/%name/batch_info.py
%_libexecdir/%name/batch_status.py
%_alterator_datadir/backends/*.backend
%_datadir/dbus-1/interfaces/*.xml
%_datadir/polkit-1/actions/*.policy

%changelog
* Mon Aug 11 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.3.1-alt1
- Fix path of systeminfo according new version.

* Mon Jul 07 2025 Pavel Khromov <hromovpi@altlinux.org> 0.3-alt2
- Change URL

* Thu May 15 2025 Andrey Limachko <liannnix@altlinux.org> 0.3-alt1
- Remove unused imports and clean up batch_status.py
- Remove %_alterator_datadir macro and hardcode path

* Wed Apr 09 2025 Pavel Khromov <hromovpi@altlinux.org> 0.2.2-alt1
- Add requires from alterator-backend-systeminfo

* Wed Mar 26 2025 Pavel Khromov <hromovpi@altlinux.org> 0.2.1-alt1
- New version

* Tue Mar 25 2025 Pavel Khromov <hromovpi@altlinux.org> 0.2-alt1
- Add depenencies from python3-devel
- Spliting batch_components script to two another files

* Mon Mar 03 2025 Andrey Limachko <liannnix@altlinux.org> 0.1-alt1
- refactor: fast getting of uninstall packages (thx Pavel Khromov)

* Mon Mar 03 2025 Andrey Limachko <liannnix@altlinux.org> 0.0.1-alt1
- Initial build (thx Pavel Khromov).
