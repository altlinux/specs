%define _unpackaged_files_terminate_build 1

Name: fonts-ttf-miracode
Version: 1.0
Release: alt1

Summary: A sharp, readable, vector-y version of Monocraft, the programming font based on Minecraft
License: OFL-1.1
Group: System/Fonts/True type
Url: https://github.com/IdreesInc/Miracode
Vcs: https://github.com/IdreesInc/Miracode
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-fonts
BuildRequires: python3
BuildRequires: fontforge

%description
A sharp, readable, vector-y version of Monocraft, the programming font
based on Minecraft.

%prep
%setup

%build
cd src
%__python3 miracode.py

%install
cd dist
%ttf_fonts_install miracode

%files -f dist/miracode.files
%doc LICENSE README.md

%changelog
* Tue Apr 08 2025 Sergey Zhidkih <rx1513@altlinux.org> 1.0-alt1
- First build for alt.
