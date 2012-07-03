Packager: Repocop Q. A. Robot <repocop@altlinux.org>
%def_with pic
%def_enable shared
%def_enable static
%def_with tcp_wrappers
%def_with zlib
%def_enable int_usbids
%define usbids_dir %_datadir/hwdatabase
#----------------------------------------------------------------------
%define subst_with_to() %{expand:%%{?_with_%{1}:--with-%{2}}} %{expand:%%{?_without_%{1}:--without-%{2}}}
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}

%define svnrev 82

%define Name USB/IP
Name: usbip
%define lname lib%name
Summary: USB device sharing system over IP network
%define module_name %name
Version: 0.1.7
%define rel 2
Release: alt%{?svnrev:0.}%rel
License: %gpl2plus
Group: System/Configuration/Networking
%ifdef svnrev
Source: %name-svn-r%svnrev.tar
%else
Source: %name-%version.tar
%endif
Patch0: %name-0.1.5-configure.patch
Patch1: %name-0.1.5-alt-hwdatabase.patch
Patch2: %name-0.1.5-zlib.patch
Patch3: %name-svn-r82-alt.patch
URL: http://%name.sourceforge.net/

# Automatically added by buildreq on Mon Jul 30 2007
#BuildRequires: gcc-c++ glib2-devel glibc-devel-static libsysfs-devel libwrap-devel zlib-devel

BuildRequires: glib2-devel >= 2.6.0
BuildRequires: libsysfs-devel
%{?_enable_static:BuildRequires: glibc-devel-static}
%{?_with_tcp_wrappers:BuildRequires: libwrap-devel}
%{?_with_zlib:BuildRequires: zlib-devel}
BuildRequires: kernel-build-tools rpm-build-licenses

%description
The %Name Project aims to develop a general USB device sharing system
over IP network. To share USB devices between computers with their full
functionality, %Name encapsulates "USB requests" into IP packets and
transmits them between computers. Original USB device drivers and
applications can be also used for remote USB devices without any
modification of them. A computer can use remote USB devices as if they
were directly attached; for example, we can:
  - USB storage devices: fdisk, mkfs, mount/umount, file operations,
    play a DVD movie and record a DVD-R media.
  - USB keyboards and USB mice: use with linux console and X Window
    System.
  - USB webcams and USB speakers: view webcam, capture image data and
    play some music.
  - USB printers, USB scanners, USB serial converters and USB Ethernet
    interfaces: ok, use fine.


%package common
Summary: %Name common files
Group: System/Configuration/Networking
BuildArch: noarch

%description common
The %Name Project aims to develop a general USB device sharing system
over IP network. To share USB devices between computers with their full
functionality, %Name encapsulates "USB requests" into IP packets and
transmits them between computers. Original USB device drivers and
applications can be also used for remote USB devices without any
modification of them. A computer can use remote USB devices as if they
were directly attached; for example, we can:
  - USB storage devices: fdisk, mkfs, mount/umount, file operations,
    play a DVD movie and record a DVD-R media.
  - USB keyboards and USB mice: use with linux console and X Window
    System.
  - USB webcams and USB speakers: view webcam, capture image data and
    play some music.
  - USB printers, USB scanners, USB serial converters and USB Ethernet
    interfaces: ok, use fine.

This package contains common files for %name-server and %name-client.


%if_enabled shared
%package -n %lname
Summary: Shared library for %Name utils
Group: System/Libraries

%description -n %lname
The %Name Project aims to develop a general USB device sharing system
over IP network. To share USB devices between computers with their full
functionality, %Name encapsulates "USB requests" into IP packets and
transmits them between computers. Original USB device drivers and
applications can be also used for remote USB devices without any
modification of them. A computer can use remote USB devices as if they
were directly attached; for example, we can:
  - USB storage devices: fdisk, mkfs, mount/umount, file operations,
    play a DVD movie and record a DVD-R media.
  - USB keyboards and USB mice: use with linux console and X Window
    System.
  - USB webcams and USB speakers: view webcam, capture image data and
    play some music.
  - USB printers, USB scanners, USB serial converters and USB Ethernet
    interfaces: ok, use fine.

This package contains shared library for %Name utils.
%endif


%package -n %lname-devel
Summary: Development files for %lname
Group: Development/C
Provides: %name-devel = %version-%release
Requires: %lname = %version-%release

%description -n %lname-devel
The %Name Project aims to develop a general USB device sharing system
over IP network. To share USB devices between computers with their full
functionality, %Name encapsulates "USB requests" into IP packets and
transmits them between computers. Original USB device drivers and
applications can be also used for remote USB devices without any
modification of them. A computer can use remote USB devices as if they
were directly attached; for example, we can:
  - USB storage devices: fdisk, mkfs, mount/umount, file operations,
    play a DVD movie and record a DVD-R media.
  - USB keyboards and USB mice: use with linux console and X Window
    System.
  - USB webcams and USB speakers: view webcam, capture image data and
    play some music.
  - USB printers, USB scanners, USB serial converters and USB Ethernet
    interfaces: ok, use fine.

This package contains the libraries and header files needed to develop
programs which make use of %lname.


%package -n %lname-devel-static
Summary: Static %lname
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
The %Name Project aims to develop a general USB device sharing system
over IP network. To share USB devices between computers with their full
functionality, %Name encapsulates "USB requests" into IP packets and
transmits them between computers. Original USB device drivers and
applications can be also used for remote USB devices without any
modification of them. A computer can use remote USB devices as if they
were directly attached; for example, we can:
  - USB storage devices: fdisk, mkfs, mount/umount, file operations,
    play a DVD movie and record a DVD-R media.
  - USB keyboards and USB mice: use with linux console and X Window
    System.
  - USB webcams and USB speakers: view webcam, capture image data and
    play some music.
  - USB printers, USB scanners, USB serial converters and USB Ethernet
    interfaces: ok, use fine.

This package contains the static %lname.


%package client
Summary: %Name client utility
Group: System/Configuration/Networking
Requires: %name-common = %version-%release
%{?_enable_shared:Requires: %lname = %version-%release}

%description client
The %Name Project aims to develop a general USB device sharing system
over IP network. To share USB devices between computers with their full
functionality, %Name encapsulates "USB requests" into IP packets and
transmits them between computers. Original USB device drivers and
applications can be also used for remote USB devices without any
modification of them. A computer can use remote USB devices as if they
were directly attached; for example, we can:
  - USB storage devices: fdisk, mkfs, mount/umount, file operations,
    play a DVD movie and record a DVD-R media.
  - USB keyboards and USB mice: use with linux console and X Window
    System.
  - USB webcams and USB speakers: view webcam, capture image data and
    play some music.
  - USB printers, USB scanners, USB serial converters and USB Ethernet
    interfaces: ok, use fine.

This package contains %Name client utility.


%package server
Summary: %Name server utils
Group: System/Configuration/Networking
Requires: %name-common = %version-%release
%{?_enable_shared:Requires: %lname = %version-%release}

%description server
The %Name Project aims to develop a general USB device sharing system
over IP network. To share USB devices between computers with their full
functionality, %Name encapsulates "USB requests" into IP packets and
transmits them between computers. Original USB device drivers and
applications can be also used for remote USB devices without any
modification of them. A computer can use remote USB devices as if they
were directly attached; for example, we can:
  - USB storage devices: fdisk, mkfs, mount/umount, file operations,
    play a DVD movie and record a DVD-R media.
  - USB keyboards and USB mice: use with linux console and X Window
    System.
  - USB webcams and USB speakers: view webcam, capture image data and
    play some music.
  - USB printers, USB scanners, USB serial converters and USB Ethernet
    interfaces: ok, use fine.

This package contains %Name client utils.


%package -n kernel-source-%module_name
Summary: Linux %module_name modules sources
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%module_name
This package contains sources for %module_name kernel modules.


%prep
%setup %{?svnrev:-n %name-svn-r%svnrev}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
pushd src
%autoreconf
%configure \
    %{subst_with pic} \
    %{subst_enable shared} \
    %{subst_enable static} \
    %{subst_with zlib} \
    %{subst_enable_to int_usbids usbids-install} \
    %{?_disable_int_usbids:--with-usbids-dir=%usbids-dir} \
    %{subst_with_to tcp_wrappers tcp-wrappers}
%make_build
popd

install -d -m 0755 kernel-source-%module_name-%version
cp -r drivers/* kernel-source-%module_name-%version/



%install
%make_install -C src DESTDIR=%buildroot install
%{?_enable_int_usbids:%{?_with_zlib:gzip --best %buildroot%_datadir/%name/usb.ids}}
install -d -m 0755 %buildroot%_docdir/%name-%version
install -m 0644 src/{AUTHORS,README.usbaid} NEWS README %buildroot%_docdir/%name-%version/
install -m 0644 src/README %buildroot%_docdir/%name-%version/README.%name-utils
install -d -m 0755 %buildroot%_usrsrc/kernel/sources
tar -c kernel-source-%module_name-%version | bzip2 --best --stdout > \
    %buildroot%_usrsrc/kernel/sources/kernel-source-%module_name-%version.tar.bz2


%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%endif


%files client
%_bindir/%name


%files common
%_docdir/%name-%version/AUTHORS
%_docdir/%name-%version/NEWS
%_docdir/%name-%version/README
%_docdir/%name-%version/README.%name-utils
%if_enabled int_usbids
%dir %_datadir/%name
%_datadir/%name/*
%endif


%files server
%_docdir/%name-%version/README.usbaid
%_bindir/%{name}d
%_bindir/usbaid
%_bindir/bind_driver


%files -n %lname-devel
%{?_enable_shared:%_libdir/*.so}
%_includedir/%name


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%files -n kernel-source-%module_name
%kernel_src/*


%changelog
* Sat Apr 09 2011 Lenar Shakirov <snejok@altlinux.ru> 0.1.7-alt0.2
- intersections with system packages fixed:
  * %%_usrsrc/ -> %%kernel_src/

* Tue Nov 03 2009 Igor Vlasenko <viy@altlinux.ru> 0.1.7-alt0.1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libusbip
  * postun_ldconfig for libusbip

* Sun Aug 10 2008 Led <led@altlinux.ru> 0.1.7-alt0.1
- SVN revision 82

* Tue May 06 2008 Led <led@altlinux.ru> 0.1.6-alt2
- fixed kernel-source-%module_name

* Tue May 06 2008 Led <led@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Mon Jul 30 2007 Led <led@altlinux.ru> 0.1.5-alt1
- Initial build
- added %name-0.1.5-configure.patch
- added %name-0.1.5-alt-hwdatabase.patch
- added %name-0.1.5-zlib.patch
