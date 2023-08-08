Name: nsxiv
Version: 31
Release: alt1

Summary: Neo Simple X Image Viewer

License: GPLv2
Group: Graphics
Url: https://github.com/nsxiv/nsxiv

# Source-url: https://github.com/nsxiv/nsxiv/archive/refs/tags/v31.tar.gz
Source: %name-%version.tar

BuildRequires: imlib2-devel libXft-devel libexif-devel libgif-devel libwebp-devel fontconfig-devel

Obsoletes: sxiv < 27

%description
nsxiv is a fork of the now-unmaintained sxiv
with the purpose of being a (mostly) drop-in replacement for sxiv,
maintaining its interface and adding simple, sensible features.
nsxiv is free software licensed under GPLv2
and aims to be easy to modify and customize.

%prep
%setup
%__subst 's|CC = c99|CC = gcc|' config.mk
%__subst 's|CFLAGS =|CFLAGS = %optflags|' config.mk

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix install-all
ln -s nsxiv %buildroot%_bindir/sxiv

%files
%_bindir/nsxiv
%_bindir/sxiv
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_docdir/%name/
%_man1dir/*
%doc README.md LICENSE

%changelog
* Tue Aug 08 2023 Vitaly Lipatov <lav@altlinux.ru> 31-alt1
- build as nsxiv, change url and source
- Obsoletes: sxiv

* Sun Jun 07 2020 Andrey Bergman <vkni@altlinux.org> 26-alt1
- Version update.

* Mon Mar 04 2019 Andrey Bergman <vkni@altlinux.org> 25-alt2
- Updated build req.

* Mon Mar 04 2019 Andrey Bergman <vkni@altlinux.org> 25-alt1
- Version update.

* Tue Dec 22 2015 Andrey Bergman <vkni@altlinux.org> 1.32-alt1
- Version update.

* Tue Mar 31 2015 Andrey Bergman <vkni@altlinux.org> 1.31-alt1.2
- Added skiplist.

* Sun Mar 22 2015 Andrey Bergman <vkni@altlinux.org> 1.31-alt1.1
- Added missed directories ownership.

* Sun Mar 22 2015 Andrey Bergman <vkni@altlinux.org> 1.31-alt1
- Initial version for Sisyphus.

