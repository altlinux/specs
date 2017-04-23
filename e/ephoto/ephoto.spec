%define _libexecdir %_prefix/libexec
%define beta %nil

Name: ephoto
Version: 1.0
Release: alt1

Summary: The Enlightenment Photo Viewer
Group: Graphical desktop/Enlightenment
License: GPLv3+
URL: http://www.smhouston.us/%name/

# VCS: git://git.enlightenment.org/apps/ephoto.git
Source: http://www.smhouston.us/stuff/%name-%version%beta.tar.xz

BuildRequires: libelementary-devel >= 1.18.0

%description
Photo Viewer for Enlightenment desktop.

%prep
%setup -n %name-%version%beta

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libdir/%name/%{name}_thumbnail
%_datadir/%name/
%_desktopdir/%name.desktop
%_datadir/pixmaps/%name.png
%doc AUTHORS ChangeLog NEWS README TODO

%changelog
* Tue Apr 18 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0 release

* Thu Mar 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt0.2
- 1.0-beta3

* Tue Aug 30 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt0.1
- 1.0-beta2

* Tue Feb 11 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt0.2
- updated to f3cff05b
- built for E18

* Mon Jan 21 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt0.1
- first preview for Sisyphus (2dad9dc6)


