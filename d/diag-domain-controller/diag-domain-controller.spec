%define _unpackaged_files_terminate_build 1
%define diagnostic_tool domain-controller
Name: diag-%diagnostic_tool
Version: 0.0.1
Release: alt2

Summary: Domain Controller Diagnostic Tool
License: GPLv3
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/diag-domain-controller
BuildArch: noarch
Source: %name-%version.tar

BuildRequires: rpm-macros-alterator

%description
Domain Controller Diagnostic Tool.

%prep
%setup

%build
sed -i 's/^VERSION=.*/VERSION=%version/' %name

%install
mkdir -p %buildroot%_alterator_datadir/diagnostictools/%name

install -p -D -m755 %name %buildroot%_bindir/%name
install -p -D -m644 %name.backend %buildroot%_alterator_datadir/backends/%name.backend
install -p -D -m644 %diagnostic_tool.diag %buildroot%_alterator_datadir/diagnostictools/%diagnostic_tool.diag
install -p -D %name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%files
%_bindir/%name
%_alterator_datadir/backends/%name.backend
%_alterator_datadir/diagnostictools/%diagnostic_tool.diag
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Thu Aug 22 2024 Evgeny Sinelnikov <sin@altlinux.org> 0.0.1-alt2
- initial first build for Sisyphus

* Thu Aug 08 2024 Sergey Savelev <savelevsa@basealt.ru> 0.0.1-alt1
- initial build

