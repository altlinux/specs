Name:    espeakup
Version: 0.90
Release: alt1

Summary: A light weight connector for espeak-ng and speakup
License: GPL-3.0
Group:   Accessibility
Url:     https://github.com/linux-speakup/espeakup

Source: %name-%version.tar

BuildRequires:  meson cmake ninja-build
BuildRequires: libespeak-ng-devel
BuildRequires: libalsa-devel

%description
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc *.md
%_bindir/*

%changelog
* Wed May 15 2024 Artem Semenov <savoptik@altlinux.org> 0.90-alt1
- Initial build for Sisyphus (ALT bug: 50362)
