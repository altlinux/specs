%def_disable static
%define sover 9

Name: libmtp
Version: 1.1.3
Release: alt1
Packager: Dmitriy Khanzhin <jinn@altlinux.ru>

Summary: a library for accessing Media Transfer Protocol devices

License: LGPLv2.1+
Group: System/Libraries
Url: http://libmtp.sourceforge.net/

Source: %name-%version.tar
Patch1: %name-1.1.3-alt-udev-rules.patch

# Automatically added by buildreq on Sat Apr 18 2009
BuildRequires: libusb-devel

%package -n %name%sover
Summary: a library for accessing Media Transfer Protocol devices
Group: System/Libraries
Provides: %name = %version-%release
Obsoletes: %{name}7
Obsoletes: %name < %version-%release

%package -n %name-devel
Summary: %name development environment
Group: Development/C
Requires: %name = %version-%release

%package -n %name-devel-static
Summary: %name static development environment
Group: Development/C
Requires: %name-devel = %version-%release

%package -n %name-examples
Summary: %name usage examples
Group: Accessibility
Requires: %name = %version-%release

%description
Libmtp is a LGPL library implementation of the Media Transfer Protocol (MTP),
a superset of the Picture Transfer Protocol (PTP).

%description -n %name%sover
Libmtp is a LGPL library implementation of the Media Transfer Protocol (MTP),
a superset of the Picture Transfer Protocol (PTP).

%description -n %name-devel
This package contains all files which are needs to compile programs using
the %name library.

%description -n %name-devel-static
This package contains libraries which are needs to compile programs statically
linked against %name library.

%description -n %name-examples
This package contains example programs for communicating with MTP devices.

%prep
%setup
%patch1 -p1

%build
%configure %{subst_enable static}
%make_build

%install
%make DESTDIR=%buildroot install
/bin/bzip2 -9 ChangeLog
/bin/install -D -m644 %name.fdi %buildroot%_datadir/hal/fdi/information/20thirdparty/10-usb-music-players-%name%sover.fdi

rm -rf %buildroot%_docdir/%name-%version/html

%pre -n %name%sover
# create group
/usr/sbin/groupadd -fr camera || :

%files -n %name%sover
%_libdir/*.so.*
/lib/udev/rules.d/*
/lib/udev/mtp-probe
%_datadir/hal/fdi/information/20thirdparty/*
%doc AUTHORS ChangeLog* README TODO

%files -n %name-devel
%_includedir/*
%_libdir/pkgconfig/*
%_libdir/*.so

%if_enabled static
%files -n %name-devel-static
%_libdir/*.a
%endif

%files -n %name-examples
%_bindir/*

%changelog
* Sun May 20 2012 Dmitriy Khanzhin <jinn@altlinux.ru> 1.1.3-alt1
- 1.1.3
- replaced libusb-compat-devel to libusb-devel in BuildRequires

* Sat Jan 21 2012 Dmitriy Khanzhin <jinn@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Tue Oct 12 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Mon Mar 22 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 1.0.2-alt1
- 1.0.2
- disabled unneeded patch
- disabled packaging html docs

* Sat Sep 12 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Sun Aug 16 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Sat Apr 18 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 0.3.7-alt1
- 0.3.7
- updated build requires

* Wed Dec 24 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.3.4-alt2
- binary package renamed to %%name%%soversion

* Thu Dec 18 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.3.4-alt1
- 0.3.4
- removed obsolete patch3

* Sat Dec 13 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.2.6.1-alt3
- removed obsolete post{,un}_ldconfig calls

* Sat May 24 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.2.6.1-alt2
- moved HAL support into %name, %name-hal has removed

* Thu May 22 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.2.6.1-alt1
- 0.2.6.1
- corrected wrong location of hal device information file
- disabled build devel-static package by default
- supported hal >= 0.5.11

* Mon Mar 10 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.2.6-alt1
- updated to 0.2.6
- created %name-hal binary package

* Wed Jun 06 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 0.1.5-alt0.2
- usage examples moved into %name-examples package
- udev rules adapted for udev >= 098,
  for access to device user must be added into group "camera"

* Wed Apr 04 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 0.1.5-alt0.1
- initial build
