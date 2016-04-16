%def_disable static

Name: libiec61883
Version: 1.2.0
Release: alt1.qa1

Summary: Streaming library for IEEE1394
License: LGPLv2+
Group: System/Libraries
Url: https://ieee1394.wiki.kernel.org/index.php/Libraries#libiec61883

#Source: http://prdownloads.sourceforge.net/libraw1394/%name-%version.tar
Source: https://www.kernel.org/pub/linux/libs/ieee1394/libiec61883-%version.tar

BuildRequires: gcc-c++ libraw1394-devel

%description
This library is an implementation of IEC 61883, part 1 (CIP, plug
registers, and CMP), part 2 (DV-SD), part 4 (MPEG2-TS), and part 6
(AMDTP). Outside of IIDC, nearly all FireWire multimedia devices use
IEC 61883 protocols.

The libiec61883 library provides a higher level API for streaming DV,
MPEG-2 and audio over Linux IEEE 1394. This includes both reception
and transmission. It uses the new "rawiso" API of libraw1394, which
transparently provides mmap-ed DMA for efficient data transfer. It
also represents the third generation of I/O technology for Linux 1394
for these media types thereby removing the complexities of additional
kernel modules, /dev nodes, and procfs. It also consolidates features
for plug control registers and connection management that previously
existed in experimental form in an unreleased version of libavc1394.

%package devel
Summary: libiec61883 header files
Group: Development/Other
Requires: %name = %version-%release

%description devel
libiec61883 devel package.

%prep
%setup

%build
%configure %{subst_enable static}
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_libdir/%name.so.*
%_man1dir/*
%doc AUTHORS ChangeLog NEWS README

%files devel
%_libdir/libiec61883.so
%_includedir/%name/
%_pkgconfigdir/%name.pc
%doc examples

%changelog
* Sat Apr 16 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2.0-alt1.qa1
- NMU: removed redundant libraw1394 and libraw1394-devel requirements.

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)
- cleanup spec

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.qa2
- Removed bad RPATH

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1.qa1
- rebuild for setversion provides

* Sat Dec 13 2008 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0 release
- removed obsolete post{,un}_ldconfig calls

* Sun Sep 10 2006 L.A. Kostis <lakostis@altlinux.ru> 1.1.0-alt0.svn.r68
- NMU;
- SVN rel 68.

* Mon Feb 13 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD Team)
- All persons listed below can be reached at <cvs_login>@pld-linux.org
