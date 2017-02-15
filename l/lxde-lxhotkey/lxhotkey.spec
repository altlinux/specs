%define upstreamname lxhotkey
%define gtkver 2
Name: lxde-%upstreamname
Version: 0.1.0
Release: alt1.20160215.1

Summary: Setup hot keys for LXDE
License: GPL
Group: Graphical desktop/Other
Url: https://git.lxde.org/gitweb/?p=lxde/lxhotkey.git

Source: %name-%version.tar
Source1: %upstreamname-gtk.desktop 

BuildPreReq: libgtk+%gtkver-devel libfm-devel libunistring-devel intltool

%description
Setup hot keys for LXDE

%package devel
Summary: devel files for %upstreamname
Group: Development/Other

%description devel
devel files for %upstreamname

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
* Wed Feb 15 2017 Anton Midyukov <antohami@altlinux.org> 0.1.0-alt1.20160215.1
- Initial build for ALT Linux Sisyphus.
