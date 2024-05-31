Name: e4rat
Version: 0.2.3
Release: alt9.1

Summary: e4rat is a toolset to accelerate the boot process as well as application startups

License: GPLv3
Url: http://e4rat.sourceforge.net/
Group: System/Configuration/Boot and Init

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/e4rat/%version/%{name}_%{version}_src.tar
Patch: e4rat-0.2.3-dynamic-link.patch
Patch1: e4rat-0.2.3-alt-use-boost-filesystem-v3.patch
Patch2: %name-%version-alt-gcc6.patch
Patch3: %name-%version-alt-toolchain-compat.patch
Patch4: %name-%version-alt-boost-1.73.0-compat.patch
Patch5: %name-%version-alt-boost-1.76.0-compat.patch
Patch6: %name-%version-alt-audit-3.0.7-compat.patch
Patch7: %name-%version-alt-fix-for-boost-1.85.0.patch

Requires: lsof

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
%patch0 -p2 -b .dynamic-link
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch5 -p2
%patch6 -p2
%patch7 -p2

%build
%cmake_insource
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_localstatedir/%name

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
%dir %_localstatedir/%name

%changelog
* Fri May 31 2024 Ivan A. Melnikov <iv@altlinux.org> 0.2.3-alt9.1
- NMU: fix build with boost 1.85.0

* Mon Jul 31 2023 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt9
- Rebuilt with boost-1.82.0.

* Tue Feb 15 2022 Egor Ignatov <egori@altlinux.org> 0.2.3-alt8
- Fix build with audit-3.0.7
- Add dependency on lsof

* Fri Apr 30 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.3-alt7
- Rebuilt with boost-1.76.0.

* Wed Jun 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.3-alt6
- Rebuilt with boost-1.73.0.

* Wed Nov 13 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.3-alt5
- Fixed build with new toolchain

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.3-alt4.1
- NMU: rebuilt with boost-1.67.0

* Mon Jul 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.3-alt4
- Fixed build with new toolchain

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.2.3-alt3.qa4
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.2.3-alt3.2.1
- rebuild with boost 1.57.0

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt3.2
- Rebuilt with Boost 1.53.0

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt3.1
- Rebuilt with Boost 1.52.0

* Tue Oct 09 2012 Ivan A. Melnikov <iv@altlinux.org> 0.2.3-alt3
- package default working dir

* Mon Oct 08 2012 Ivan A. Melnikov <iv@altlinux.org> 0.2.3-alt2
- port to Boost.Filesystem v3 to build with new boost

* Sat May 19 2012 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt1
- new version 0.2.3 (with rpmrb script)

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.1
- Rebuilt with Boost 1.49.0

* Mon Mar 12 2012 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- initial build for ALT Linux Sisyphus (thanks, Mandriva!)

* Wed May 11 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.2.1-1mdv2011.0
+ Revision: 673556
- Imported to cooker.
  P0: enable dynamic linking.
- Created package structure for e4rat.

