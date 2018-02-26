Name: torsmo
Version: 0.18
Release: alt3.qa2
Summary: Torsmo is a system monitor like gkrellm, but lightweight

Source0: %name-%version.tar.gz
Patch0: torsmo-0.18-alt-makefile.patch
Patch1: torsmo-0.18-alt-memory.patch
URL: http://torsmo.sourceforge.net/
Group: Monitoring
License: BSD

Packager: Ilya Mashkin <oddity at altlinux dot ru>

Requires: /proc
# Automatically added by buildreq on Tue Feb 07 2006
BuildRequires: libX11-devel


%description
Torsmo is a system monitor that sits in the corner of your desktop. It's very
simple, customizable and it renders only text on the desktop (and
percentagebars if you want it to ;) and the only lib it uses is Xlib.
Torsmo can show various information about your system and it's peripherals.

%prep

%setup -q
%patch0 -p1
%patch1 -p1

%build

autoreconf -fisv
%configure --x-libraries=%_libdir

%make

%install


%makeinstall BINDIR=$RPM_BUILD_ROOT%_bindir

# menu
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Torsmo
Comment=Torsmo is a lightweight system monitor
Icon=%{name}
Exec=%name -d
Terminal=false
Categories=System;Monitor;
EOF


%files
%doc AUTHORS COPYING README torsmorc.sample ChangeLog
%_man1dir/torsmo.1*
%_bindir/torsmo
%_desktopdir/%{name}.desktop

%changelog
* Thu Apr 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.18-alt3.qa2
- NMU: converted debian menu to freedesktop

* Mon Dec 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.18-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for torsmo
  * postclean-05-filetriggers for spec file

* Tue May 18 2006 Ilya Mashkin  <oddity at altlinux dot ru> 0.18-alt3
- fixed build (thanks to avm@ for patches)

* Fri Mar 04 2005 Ilya Mashkin  <oddity at altlinux dot ru> 0.18-alt2
- fixed menu (#6148)

* Tue Feb 01 2005 Ilya Mashkin  <oddity at altlinux dot ru> 0.18-alt1
- Initial build for ALT Linux
