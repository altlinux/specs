Name: gnucobol
Version: 2.2
Release: alt1

Summary: GnuCOBOL (formely Open COBOL) - COBOL compiler

License: GPLv2+ and LGPLv2+
Group: Development/Other
Url: http://www.opencobol.org

Packager: Ilya Mashkin <oddity@altlinux.ru>

# Source:	http://downloads.sourceforge.net/%name/%name-%version.tar.gz
# Source-url: https://ftp.gnu.org/gnu/gnucobol/gnucobol-%version.tar.xz
Source: %name-%version.tar

# Automatically added by buildreq on Wed Jun 06 2012
# optimized out: libtinfo-devel
BuildRequires: libdb4-devel libgmp-devel libncurses-devel help2man

Requires: libcob = %version-%release
Obsoletes: libcob-devel < %version
# explicitly added texinfo for info files
BuildRequires: texinfo

Provides: open-cobol = %version-%release
Obsoletes: open-cobol < %version

%description
GnuCOBOL is an open-source COBOL compiler, which translates COBOL
programs to C code and compiles it using GCC.

%package -n libcob
Summary: GnuCOBOL runtime library
License: LGPLv2+
Group: Development/Other

%description -n libcob
GnuCOBOL is an open-source COBOL compiler, which translates COBOL
programs to C code and compiles it using GCC.

This package contains GnuCOBOL runtime library.

%prep
%setup
# hack to work around break -frecord-gcc-switches
subst 's!/-g/!/-g /!' ./configure.ac
%autoreconf

%build
%add_optflags %optflags_shared
%configure --disable-rpath --disable-static --enable-debug
# get rid of RPATH
#sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool

%make_build || %make

%install
%makeinstall_std

%find_lang %name

%check
%make_build -k check

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog NEWS README THANKS
%_bindir/cobc
%_bindir/cob-config
%_bindir/cobcrun
%_datadir/gnucobol/
%_infodir/gnucobol.info*
%_includedir/*
%_libdir/libcob.so
%dir %_libdir/gnucobol/
%_libdir/gnucobol/CBL_OC_DUMP.so
%_man1dir/*

%files -n libcob
%doc COPYING.LESSER
%_libdir/libcob.so.*

%changelog
* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- new version (2.2) with rpmgs script
- rename package from open-cobol to gnucobol

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3.1
- NMU: added BR: texinfo

* Wed Jun 06 2012 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt3
- Rebuilt with libgmp10.

* Wed Jun 06 2012 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt2
- Fixed package dependencies.

* Sun Mar 20 2011 Ilya Mashkin <oddity@altlinux.ru> 1.1-alt1
- Build version 20090206 for ALT Linux

* Mon Mar 23 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.1-0.20090206
- Adapt version to naming guidelines

* Mon Dec  1 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0.95-3
- Obsoleting libcob-devel

* Tue Oct 21 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0.95-2
- Fix Changelog entry
- Rebuild

* Mon Oct 20 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0.95-1
- New upstream relase
- Fix FORTIFY_SOURCE issue (#464554)

* Mon Sep 15 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0.90-4
- Remove _FORTIFY_SOURCE as adviced by the upstream

* Thu Sep 11 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0.90-3
- Add -D__NO_STRING_INLINES for the i86 arch

* Sun Aug 17 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0.90-2
- Fix dependency open-cobol -> libcob

* Tue Aug 12 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0.90-1
- Prerelease of opben-cobol-1.1

* Tue Aug  5 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0-3
- Blocking Test #98 to failing

* Wed Jul 30 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0-2
- OpenCOBOL req. libcob-devel
- Fix URIs
- Fix tiwce groups

* Wed Jul 30 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0-1
- Initional Fedora RPM package

