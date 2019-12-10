Name: fossology-nomos
Version: 3.6.0.0.89.g9cbe36ba0
Release: alt1

Summary: Architecture for analyzing software, nomos standalone
License: GPL-2.0-or-later
Group: Other
Url: https://github.com/fossology/fossology

Source: %name-%version.tar

BuildRequires: glib2-devel
BuildRequires: libjson-c-devel
BuildRequires: postgresql-devel

%description
The FOSSology project is a web based framework that allows you to
upload software to be picked apart and then analyzed by software
agents which produce results that are then browsable via the web
interface. Existing agents include license analysis, metadata
extraction, and MIME type identification.

This package contains the nomos agent programs and their resources.

%prep
%setup

%build
%make_build -C src/nomos
%make_build -C src/nomos/agent -f Makefile.sa nomossa

%install
install -Dm0755 -p src/nomos/agent/nomossa %buildroot%_bindir/nomossa

%files
%doc README.md LICENSE src/nomos/agent/README src/nomos/agent/Notes
%_bindir/nomossa

%changelog
* Tue Dec 10 2019 Vitaly Chikunov <vt@altlinux.org> 3.6.0.0.89.g9cbe36ba0-alt1
- First release for ALT.
