Name:     pdf-compress
Version:  0.4
Release:  alt1

Summary:  Performing PDF compression operations using graphics
License:  GPL-3.0
Group:    Archiving/Other
URL:      https://github.com/Felixxz/pdf-compress
VCS:      https://github.com/Felixxz/pdf-compress

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: libgtk+3-devel
Requires: icon-theme-hicolor
Requires: ghostscript-classic

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/*
%doc *.md
%_iconsdir/hicolor/*/apps/*
%_desktopdir/%name.desktop

%changelog
* Fri Sep 12 2025 Kirill Izmestev <felixz@altlinux.org> 0.4-alt1
- New version 0.4.
- Set max length, add file names checks (ALT#55928).

* Wed Sep 03 2025 Kirill Izmestev <felixz@altlinux.org> 0.3-alt1
- Initial build for Sisyphus.
