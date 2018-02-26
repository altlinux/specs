Name: kbdd
Version: 0.6
Release: alt1
License: GPLv3
Summary: Simple daemon and library to make per window layout using XKB.
Group: System/X11
URL: https://github.com/qnikst/kbdd
Packager: Sergey Alembekov <rt@altlinux.ru>

Source: %name.tar

BuildRequires: autoconf libX11-devel libdbus-glib-devel

%description
Simple daemon and library to make per window layout using XKB
(X KeyBoard Extension).

%prep
%setup -n %name

%build
aclocal
autoreconf -i
%configure
%make

%install
%make install DESTDIR=%buildroot

%files
%defattr(-, root, root, 0755)
%_bindir/kbdd
%_datadir/dbus-1/interfaces/kbdd-service-interface.xml
%_man1dir/kbdd.1.gz


%changelog
* Mon Jun 25 2012 Sergey Alembekov <rt@altlinux.ru> 0.6-alt1
- initial 


