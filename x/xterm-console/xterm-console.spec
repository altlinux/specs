%define _unpackaged_files_terminate_build 1

Name: xterm-console
Version: 1.1
Release: alt1
Summary: Locking wrapper script
Group: Terminals
License: MIT
Url: https://github.com/os-autoinst/xterm_console
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: bdftopcf kbd fontpackages-devel rpm-build-python3

Requires: xterm

%description
xterm-console runs an xterm that tries to look as much as possible
like a console. It reads the current color configuration from the
kernel, and the package includes copies of the system console fonts
converted to the PCF format for xterm to use.

%prep
%setup

%install
mkdir -p %buildroot%_bindir
install -m 0755 xterm-console %buildroot%_bindir

%files
%doc README.md
%_bindir/xterm-console

%changelog
* Thu May 26 2022 Alexandr Antonov <aas@altlinux.org> 1.1-alt1
- initial build for ALT
