%define kernel_version   4.9
%define kernel_source /usr/src/kernel/sources/kernel-source-%kernel_version.tar
%define source_dir tools/usb/usbip

Name: usbip
Summary: Utility for manage usbip devices
Version: 2.0.4
Release: alt2

%define lname lib%name

Group: System/Configuration/Networking
License: GPLv2+
Url: http://www.kernel.org

Source: %name-%version.tar

Packager: Pavel Vainerman <pv@altlinux.org>

BuildRequires: libudev-devel libwrap-devel

BuildRequires: kernel-source-%kernel_version

%description
On a USB/IP  server, devices can be listed, bound, and unbound
using this program. On a USB/IP client, devices exported by USB/IP
servers can be listed, attached and detached.

%package -n %{name}d
Summary: %name server daemon
Group: System/Configuration/Networking
Requires: %lname = %version-%release

%description -n %{name}d
%{name} server daemon.

%package -n %lname
Summary: %name shared library
Group: System/Libraries

%description -n %lname
%name shared library.

%package -n %lname-devel
Summary: %name devel files
Group: Development/C

%description -n %lname-devel
%name devel files.

%package -n %lname-devel-static
Summary: %name static library
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
%name static library.

%prep
%setup
tar -xvf %kernel_source kernel-source-%kernel_version/%source_dir
cp -rf kernel-source-%kernel_version/%source_dir/* ./
rm -rf kernel-source-%kernel_version

%build
./autogen.sh
%configure --with-usbids-dir=%_datadir/misc
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_unitdir

install -Dp -m644 usbipd %buildroot%_sysconfdir/sysconfig/%{name}d
install -Dp -m644 usbipd.service %buildroot%_unitdir/%{name}d.service

%files
%_sbindir/%name
%_man8dir/*
%doc README

%files -n %{name}d
%_sbindir/%{name}d
%_sysconfdir/sysconfig/%{name}d
%_unitdir/%{name}d.service

%files -n %lname
%_libdir/*.so.*

%files -n %lname-devel
%_includedir/*
%_libdir/*.so

%files -n %lname-devel-static
%_libdir/*.a

%changelog
* Thu Feb 15 2018 Pavel Vainerman <pv@altlinux.ru> 2.0.4-alt2
- added service file

* Sat Dec 16 2017 Pavel Vainerman <pv@altlinux.ru> 2.0.4-alt1
- added kernel major version for package name

* Thu Dec 14 2017 Pavel Vainerman <pv@altlinux.ru> 2.0.1-alt0.1
- initial commit for build from kernel sources (usbip API 2.0)

* Fri Oct 11 2013 Led <led@altlinux.ru> 1.1.1-alt2
- updated from 3.12 kernel tree

* Thu Aug 08 2013 Led <led@altlinux.ru> 1.1.1-alt1
- 1.1.1
- build from kernel source tree
- subpackages usbip-common and usbip-client replaced with usbip
- subpackage usbip-server replaced with usbipd

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
- fixed kernel-source-usbip

* Tue May 06 2008 Led <led@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Mon Jul 30 2007 Led <led@altlinux.ru> 0.1.5-alt1
- Initial build
- added %name-0.1.5-configure.patch
- added %name-0.1.5-alt-hwdatabase.patch
- added %name-0.1.5-zlib.patch
