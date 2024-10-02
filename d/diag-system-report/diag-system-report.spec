%define _unpackaged_files_terminate_build 1
%define diagnostic_tool system-report
Name: diag-%diagnostic_tool
Version: 0.0.2
Release: alt1

Summary: Diagnostic Tool for collecting system information
License: GPLv3
Group: System/Configuration/Other
BuildArch: noarch
Source: %name-%version.tar

Requires: system-report

BuildRequires: rpm-macros-alterator

%description
Diagnostic Tool for collecting system information.

%prep
%setup

%build
sed -i 's/^VERSION=.*/VERSION=%version%release/' %name

%install
mkdir -p %buildroot%_alterator_datadir/diagnostictools/%name

install -p -D -m755 %name %buildroot%_bindir/%name
install -p -D -m644 alterator/%name.backend %buildroot%_alterator_datadir/backends/%name.backend
install -p -D -m644 alterator/%diagnostic_tool.diag %buildroot%_alterator_datadir/diagnostictools/%diagnostic_tool.diag
install -p -D %name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%files
%_bindir/%name
%_alterator_datadir/backends/%name.backend
%_alterator_datadir/diagnostictools/%diagnostic_tool.diag
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Wed Oct 02 2024 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.0.2-alt1
- Add icon. Author: Elena Dyatlenko
- Expanded description
- Fix ReportSuffix

* Tue Oct 01 2024 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.0.1-alt1
- Initial Build


