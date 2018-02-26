Name: e4rat
Version: 0.2.1
Release: alt1.1

Summary: e4rat is a toolset to accelerate the boot process as well as application startups

License: GPLv3
Url: http://e4rat.sourceforge.net/
Group: System/Configuration/Boot and Init

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://downloads.sourceforge.net/project/dracut/%{name}_%{version}_src.tar
Patch: e4rat_0.2.1-dynamic-link.patch

# Automatically added by buildreq on Mon Mar 12 2012
# optimized out: boost-devel cmake cmake-modules libcom_err-devel libstdc++-devel perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators
BuildRequires: boost-devel-headers boost-filesystem-devel boost-signals-devel ccmake dpkg gcc-c++ libaudit-devel libblkid-devel libe2fs-devel perl-Pod-Parser

%description
e4rat ("Ext4 - Reducing Access Times") is a toolset to accelerate the boot
process as well as application startups. Through physical file realloction
e4rat eliminates both seek times and rotational delays. This leads to a high
disk transfer rate.

Placing files on disk in a sequentially ordered way allows to efficiently
read-ahead files in parallel to the program startup. The combination of
sequentially reading and a high cache hit rate may reduce the boot time by a
factor of three, as the example below shows.

e4rat is based on the online defragmentation ioctl EXT4_IOC_MOVE_EXT from the
Ext4 filesystem, which was introduced in Linux Kernel 2.6.31. Other filesystem
types and/or earlier versions of extended filesystems are not supported.

%prep
%setup -n %name-%version
%patch0 -p1 -b .dynamic-link

%build
%cmake_insource
%make_build

%install
%makeinstall_std

# (eugeni) remove left-over static library
rm -f %buildroot%_libdir/libe4rat-core.a

%files
%doc README
%config %_sysconfdir/%name.conf
%_sbindir/%name-collect
%_sbindir/%name-preload
%_sbindir/%name-realloc
%_man5dir/%name.conf.5*
%_man8dir/%name-collect.8*
%_man8dir/%name-preload.8*
%_man8dir/%name-realloc.8*

%changelog
* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.1
- Rebuilt with Boost 1.49.0

* Mon Mar 12 2012 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- initial build for ALT Linux Sisyphus (thanks, Mandriva!)

* Wed May 11 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.2.1-1mdv2011.0
+ Revision: 673556
- Imported to cooker.
  P0: enable dynamic linking.
- Created package structure for e4rat.

