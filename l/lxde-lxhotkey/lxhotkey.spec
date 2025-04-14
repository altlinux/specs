%define upstreamname lxhotkey
%define gtkver 3
Name: lxde-%upstreamname
Version: 0.1.2
Release: alt1

Summary: Setup hot keys for LXDE
License: GPL-2.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/lxde/lxhotkey
Vcs: https://github.com/lxde/lxhotkey.git

Source: %name-%version.tar
Source1: %upstreamname-gtk.desktop 

BuildPreReq: libgtk+%gtkver-devel libfm-devel libunistring-devel intltool

%description
%summary.

%package devel
Summary: devel files for %upstreamname
Group: Development/Other

%description devel
devel files for %upstreamname.

%prep
%setup -n %name-%version

%build
%autoreconf
%configure --enable-man \
           --enable-dbus \
           --with-gtk=%gtkver

%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_desktopdir
install -m644 %SOURCE1 %buildroot%_desktopdir

%find_lang %upstreamname

%files -f %upstreamname.lang
%doc ChangeLog COPYING
%_bindir/*
%_desktopdir/*
%_libdir/%upstreamname
%_man1dir/*

%files devel
%dir %_includedir/%upstreamname
%_includedir/%upstreamname/*.h
%_pkgconfigdir/*.pc

%changelog
* Fri Apr 11 2025 Anton Midyukov <antohami@altlinux.org> 0.1.2-alt1
- nev version
- build with gtk+3
- update Url tag
- add Vcs tag

* Wed Feb 15 2017 Anton Midyukov <antohami@altlinux.org> 0.1.0-alt1.20160215.1
- Initial build for ALT Linux Sisyphus.
