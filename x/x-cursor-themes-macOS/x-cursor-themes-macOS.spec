%define _name macOS

Name: x-cursor-themes-%_name
Version: 2.0.1
Release: alt1

Summary: Free & Open source macOS Cursors

Group: Graphical desktop/Other
License: GPL-3.0
URL: https://github.com/ful1e5/apple_cursor
VCS: https://github.com/ful1e5/apple_cursor.git

BuildArch: noarch
ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
Source1: node_modules.tar.gz

BuildRequires: clickgen yarn npm zip
BuildRequires: /proc

%description
Open source macOS Cursors for Windows and Linux with HiDPI Support.

%prep
%setup
tar -xf %SOURCE1

%build
yarn --offline generate

%install
mkdir -p %buildroot%_iconsdir
cp -a ./themes/%{_name}* %buildroot%_iconsdir

%files
%doc LICENSE *.md
%_iconsdir/%{_name}*
%exclude %_iconsdir/%{_name}*-Windows

%changelog
* Thu Dec 26 2024 Alexander Kovalev <alexvk@altlinux.org> 2.0.1-alt1
- Initial build for ALT.
