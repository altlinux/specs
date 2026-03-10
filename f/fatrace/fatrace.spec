# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
Name: fatrace
Version: 0.19.1
Release: alt1

Summary: Reports file access events from all running processes

Group: File tools
License: GPLv3+
Url: https://github.com/martinpitt/fatrace

# Source-url: https://github.com/martinpitt/fatrace/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
fatrace reports file access events from all running processes.

Its main purpose is to find processes which keep waking up the disk
unnecessarily and thus prevent some power saving.

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=%prefix

%files
%doc COPYING README.md
%_sbindir/fatrace
%_sbindir/power-usage-report
%_mandir/man*/*

%changelog
* Tue Mar 10 2026 Vitaly Lipatov <lav@altlinux.ru> 0.19.1-alt1
- new version 0.19.1 (with rpmrb script)
- switch Source-url to GitHub

* Sat Jul 03 2021 Vitaly Lipatov <lav@altlinux.ru> 0.15-alt1
- NMU: new version 0.15 (with rpmrb script), cleanup sepec

* Wed Dec 04 2019 Lenar Shakirov <snejok@altlinux.org> 0.13-alt2
- First build for ALT (thanks to Autoimports!)
- Spec cleaned, thanks to "cleanup_spec"

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_2
- update by mgaimport

* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_1
- new version

