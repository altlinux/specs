%define _unpackaged_files_terminate_build 1
%define shortname systeminfo

Name: alterator-backend-%{shortname}
Version: 0.4.2
Release: alt1

Summary: Alterator backend for getting system information
License: GPLv3
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-backend-systeminfo

BuildArch: noarch
Source: %name-%version.tar

Requires: alterator-interface-%{shortname} >= 0.4.0
Requires: alterator-backend-%{shortname}-utils = %version-%release
Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.29

BuildRequires(pre): rpm-macros-alterator

%description
%summary.

%package -n alterator-interface-%{shortname}
Summary: Alterator interface for getting system information
Group: System/Configuration/Other

%description -n alterator-interface-%{shortname}
%summary.

%package -n alterator-backend-%{shortname}-utils
Summary: Scripts for alterator-backend-%{shortname}
Group: System/Configuration/Other
Requires: alterator-notes-utils = %version-%release

%description -n alterator-backend-%{shortname}-utils
%summary.

%package -n alterator-notes-utils
Summary: Alterator notes file finder
Group: System/Configuration/Other

%description -n alterator-notes-utils
%summary.

%prep
%setup

%install
%makeinstall_std

%files
%_alterator_datadir/backends
%_alterator_datadir/objects

%files -n alterator-interface-systeminfo
%_datadir/dbus-1/interfaces
%_datadir/polkit-1/actions

%files -n alterator-backend-systeminfo-utils
%_alterator_libdir/backends/%{shortname}

%files -n alterator-notes-utils
%_alterator_libdir/backends/%{shortname}.d/notes

%changelog
* Fri Nov 28 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.4.2-alt1
- Add 'exit_status = true' for new version of executor.

* Thu Aug 14 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.4.1-alt2
- Actualize upstream URL.
- Fix requirements.

* Mon Aug 11 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.4.1-alt1
- Move search of notes to child shell lib.
- Move exec files to /usr/lib/alterator/backends filesystem.

* Fri Jul 25 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.4.0-alt1
- Add GetFinalNotes method with editions support.
- Add editions support for GetReleaseNotes method. 

* Wed Apr 09 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.3.2-alt1
- New version.

* Sat Apr 05 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.3.1-alt1
- New version.

* Fri Mar 28 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.3.0-alt1
- New version.

* Mon Mar 17 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.2-alt1
- New version.

* Fri Mar 14 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.1-alt1
- New version.

* Wed Mar 12 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.0-alt1
- New version.

* Fri Mar 07 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.2-alt2
- Put object file for Alterator Explorer.

* Tue Mar 04 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.2-alt1
- New version.

* Thu Feb 20 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.1-alt1
- New version.

* Wed Sep 25 2024 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.0-alt1
- Initial build.

