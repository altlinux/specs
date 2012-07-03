Name: ifuse
Version: 1.1.2
Release: alt1

Summary: Filesystem access for the iPhone and iPod Touch
Group: Communications
License: LGPLv2+
URL: http://www.libimobiledevice.org/

Source: %url/downloads/%name-%version.tar.bz2

BuildRequires: libfuse-devel libimobiledevice-devel >= 1.1.4 glib2-devel

%description
iFuse is a FUSE filesystem driver which uses libiphone to connect to devices
without the need for a jailbreak.
It is using the native Apple "AFC" protocol, over the normal USB cable in order
to access the iPhone's or iPod Touch's media files under Linux.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/ifuse
%_man1dir/ifuse.1*
%doc AUTHORS README

%changelog
* Wed May 09 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Sun Apr 08 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt3
- rebuild against libimobiledevice-1.1.3

* Sat May 28 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt2
- rebuild against libimobiledevice-1.1.1

* Wed Jan 19 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Tue Apr 06 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sun Mar 14 2010 Igor Zubkov <icesik@altlinux.org> 0.9.7-alt1
- 0.9.6 -> 0.9.7

* Tue Jan 26 2010 Igor Zubkov <icesik@altlinux.org> 0.9.6-alt1
- 0.9.5 -> 0.9.6

* Wed Dec 23 2009 Igor Zubkov <icesik@altlinux.org> 0.9.5-alt1
- build for Sisyphus

