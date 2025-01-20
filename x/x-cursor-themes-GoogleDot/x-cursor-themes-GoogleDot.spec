%define _name GoogleDot

Name: x-cursor-themes-%_name
Version: 2.0.0
Release: alt1

Summary: An opensource cursor theme inspired by Google

Group: Graphical desktop/Other
License: GPL-3.0
URL: https://github.com/ful1e5/Google_Cursor
VCS: https://github.com/ful1e5/Google_Cursor.git

BuildArch: noarch
ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
Source1: node_modules.tar.gz
Patch: build.toml.patch

BuildRequires: clickgen yarn
BuildRequires: /proc

%description
%summary.

%prep
%setup
%autopatch -p1
tar -xf %SOURCE1

%build
yarn build

%install
mkdir -p %buildroot%_iconsdir
cp -a ./themes/%_name-* %buildroot%_iconsdir

%files
%doc LICENSE *.md
%_iconsdir/%_name-*
%exclude %_iconsdir/%_name-*-Windows

%changelog
* Thu Dec 26 2024 Alexander Kovalev <alexvk@altlinux.org> 2.0.0-alt1
- Initial build for ALT.
