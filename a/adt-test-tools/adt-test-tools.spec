%define _unpackaged_files_terminate_build 1

Name: adt-test-tools
Version: 0.1.7
Release: alt1

Summary: Test tools for ADT.
License: GPLv2+
Group: Other
URL: https://github.com/AlexSP0/adt-test-tools

BuildArch: noarch

Source0: %name-%version.tar

%description
Test tools for ADT.

%prep
%setup

%install
mkdir -p %buildroot%_libexecdir/%name
mkdir -p %buildroot%_sysconfdir/alterator/backends/system
mkdir -p %buildroot%_sysconfdir/alterator/backends/user

mkdir -p %buildroot%_datadir/alterator/diagnostic_tool
mkdir -p %buildroot%_datadir/alterator/diagnostic_tool_user

mkdir -p %buildroot%_datadir/alterator/diagnostic_tool2
mkdir -p %buildroot%_datadir/alterator/diagnostic_tool2_user

mkdir -p %buildroot%_datadir/alterator/diagnostic_tool3_user

install -v -p -m 755 -D adt-test-tool %buildroot%_libexecdir/%name
install -v -p -m 755 -D adt-test-tool-user %buildroot%_libexecdir/%name

install -v -p -m 644 -D diagnostic_tool.backend %buildroot%_sysconfdir/alterator/backends/system
install -v -p -m 644 -D diagnostic_tool_user.backend %buildroot%_sysconfdir/alterator/backends/user

install -v -p -m 644 -D diagnostic_tool2.backend %buildroot%_sysconfdir/alterator/backends/system
install -v -p -m 644 -D diagnostic_tool2_user.backend %buildroot%_sysconfdir/alterator/backends/user

install -v -p -m 644 -D diagnostic_tool3.backend %buildroot%_sysconfdir/alterator/backends/user

install -v -p -m 644 -D diagnostic_tool_sys.diag %buildroot%_datadir/alterator/diagnostic_tool
install -v -p -m 644 -D diagnostic_tool_user.diag %buildroot%_datadir/alterator/diagnostic_tool_user

install -v -p -m 644 -D diagnostic_tool2_sys.diag %buildroot%_datadir/alterator/diagnostic_tool2
install -v -p -m 644 -D diagnostic_tool2_user.diag %buildroot%_datadir/alterator/diagnostic_tool2_user

install -v -p -m 644 -D diagnostic_tool3_user.diag %buildroot%_datadir/alterator/diagnostic_tool3_user

%files
%_libexecdir/%name/adt-test-tool
%_libexecdir/%name/adt-test-tool-user

%_sysconfdir/alterator/backends/system/diagnostic_tool.backend
%_sysconfdir/alterator/backends/user/diagnostic_tool_user.backend

%_sysconfdir/alterator/backends/system/diagnostic_tool2.backend
%_sysconfdir/alterator/backends/user/diagnostic_tool2_user.backend

%_sysconfdir/alterator/backends/user/diagnostic_tool3.backend

%_datadir/alterator/diagnostic_tool/diagnostic_tool_sys.diag
%_datadir/alterator/diagnostic_tool_user/diagnostic_tool_user.diag

%_datadir/alterator/diagnostic_tool2/diagnostic_tool2_sys.diag
%_datadir/alterator/diagnostic_tool2_user/diagnostic_tool2_user.diag

%_datadir/alterator/diagnostic_tool3_user/diagnostic_tool3_user.diag

%changelog
* Mon Dec 09 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.7-alt1
- refator ini files to toml files

* Mon Sep 02 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.6-alt2
- fix: fix path diagnostic_tool2_user

* Wed Aug 28 2024 Elena Dyatlenko <lenka@altlinux.org> 0.1.6-alt1
- add diag3 on session bus
- add diag and diag2 session bus

* Mon Aug 26 2024 Elena Dyatlenko <lenka@altlinux.org> 0.1.5-alt1
- add diag on session bus

* Thu Mar 14 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.4-alt1
- aligned with specifications

* Sat Feb 17 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.3-alt1
- add ReportSuffix key

* Wed Feb 14 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.2-alt1
- fix report method

* Wed Feb 07 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.1-alt1
- add pauses during simulating tests

* Tue Dec 12 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- initial build
