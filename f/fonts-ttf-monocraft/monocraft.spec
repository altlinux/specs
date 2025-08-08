%define _unpackaged_files_terminate_build 1
%define fname monocraft

Name: fonts-ttf-%fname
Version: 4.1
Release: alt1

Summary: Monocraft font
License: OFL-1.1
Group: System/Fonts/True type
Url: https://github.com/IdreesInc/Monocraft
Vcs: https://github.com/IdreesInc/Monocraft.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-fonts
BuildRequires: python3
BuildRequires: fontforge

%description
A monospaced programming font inspired by the Minecraft typeface.

%prep
%setup

%build
cd src
%__python3 monocraft.py

%install
cd dist
%ttf_fonts_install %fname

%files -f dist/%fname.files
%doc LICENSE README.md

%changelog
* Fri Aug 08 2025 Ajrat Makhmutov <rauty@altlinux.org> 4.1-alt1
- New version.

* Sun Aug 18 2024 Ajrat Makhmutov <rauty@altlinux.org> 4.0-alt1
- New version.

* Thu Feb 29 2024 Ajrat Makhmutov <rauty@altlinux.org> 3.0-alt1
- First build for ALT.
