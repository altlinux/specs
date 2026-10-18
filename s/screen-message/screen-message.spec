Name: screen-message
Version: 0.29
Release: alt1

Summary: Screen message show given text in fullscreen

License: GPLv2+
Group: System/X11
Url: https://github.com/nomeata/screen-message

# Source-url: https://github.com/nomeata/screen-message/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar.gz

BuildRequires: libgtk+3-devel

%description
Screen message show given text in fullscreen

%prep
%setup

%build
%autoreconf
%configure
make

%install
make install DESTDIR=%buildroot

%files
%_bindir/sm
%_man1dir/*
%_desktopdir/sm.desktop
%_iconsdir/hicolor/48x48/apps/sm.png

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 0.29-alt1
- New version (0.29)
- Switch to GTK3, build with autoreconf (BuildRequires: libgtk+3-devel instead of libgtk+2-devel)
- Add Url tag
- Drop obsolete python3 port patch (removed BuildRequires: rpm-build-python3)

* Sat Mar 02 2024 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt3
- don't pack unworked sm.py

* Tue Mar 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.6-alt2
- Porting to python3.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Feb 19 2008 Terechkov Evgenii <evg@altlinux.ru> 0.6-alt1
- Rebuild with new sisyphus_check
- Url tag removed (was dummy anyway)

* Thu Aug  2 2007 Terechkov Evgenii <evg@altlinux.ru> 0.6-alt0
- Initial build for Sisyphus
