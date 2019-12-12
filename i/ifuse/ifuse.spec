Name: ifuse
Version: 1.1.3
Release: alt5

Summary: Filesystem access for the iPhone and iPod Touch
Group: Communications
License: LGPLv2+
URL: http://www.libimobiledevice.org/

%if_disabled snapshot
Source: %url/downloads/%name-%version.tar.bz2
%else
# VCS: https://github.com/libimobiledevice/ifuse
Source: %name-%version.tar
%endif

Requires: fuse

BuildRequires: libfuse-devel libimobiledevice-devel >= 1.1.4 glib2-devel

%description
iFuse is a FUSE filesystem driver which uses libiphone to connect to devices
without the need for a jailbreak.
It is using the native Apple "AFC" protocol, over the normal USB cable in order
to access the iPhone's or iPod Touch's media files under Linux.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/ifuse
%_man1dir/ifuse.1*
%doc AUTHORS README

%changelog
* Thu Dec 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt5
- updated to 1.1.3-6-ge75d32c

* Mon Feb 23 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt4
- rebuilt against libimobiledevice.so.6

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt3
- rebuilt against libimobiledevice.so.5/libplist.so.3

* Fri Jun 20 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt2
- rebuilt against libplist.so.2

* Thu Mar 06 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt1
- 1.1.3

* Thu Apr 11 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt2
- rebuilt against libimobiledevice.so.4

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

