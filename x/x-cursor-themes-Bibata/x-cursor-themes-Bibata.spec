%define _name Bibata

Name: x-cursor-themes-%_name
Version: 2.0.7
Release: alt1

Summary: Bibata cursor themes

Group: Graphical desktop/Other
License: GPL-3.0
URL: https://github.com/ful1e5/Bibata_Cursor

BuildArch: noarch
ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
Source1: node_modules.tar.gz

BuildRequires: clickgen yarn npm zip
BuildRequires: /proc

%description
Bibata is an open source, compact, and material designed cursor set
that aims to improve the cursor experience for users.

%prep
%setup
tar -xf %SOURCE1

%build
# fix version
sed -i 's/^version=.*$/version="v%version"/' build.sh
yarn --offline generate

%install
mkdir -p %buildroot%_iconsdir
cp -a ./themes/%_name-* %buildroot%_iconsdir

%files
%doc LICENSE *.md
%_iconsdir/%_name-*
%exclude %_iconsdir/%_name-*-Windows

%changelog
* Thu Dec 19 2024 Alexander Kovalev <alexvk@altlinux.org> 2.0.7-alt1
- Initial build for ALT.
