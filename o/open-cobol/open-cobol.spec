Name: open-cobol
Version: 1.1
Release: alt3

Summary: OpenCOBOL - COBOL compiler
License: GPLv2+ and LGPLv2+
Group: Development/Other
Url: http://www.opencobol.org
Packager: Ilya Mashkin <oddity@altlinux.ru>

# Source:	http://downloads.sourceforge.net/%name/%name-%version.tar.gz
Source: http://www.sim-basis.de/%name-%version.tar.gz

# Automatically added by buildreq on Wed Jun 06 2012
# optimized out: libtinfo-devel
BuildRequires: libdb4-devel libgmp-devel libncurses-devel

Requires: libcob = %version-%release
Obsoletes: libcob-devel < %version

%description
OpenCOBOL is an open-source COBOL compiler, which translates COBOL
programs to C code and compiles it using GCC.

%package -n libcob
Summary: OpenCOBOL runtime library
License: LGPLv2+
Group: Development/Other

%description -n libcob
OpenCOBOL is an open-source COBOL compiler, which translates COBOL
programs to C code and compiles it using GCC.

This package contains OpenCOBOL runtime library.

%prep
%setup

%build
%add_optflags %optflags_shared
%configure --disable-rpath --disable-static
# get rid of RPATH
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool

%make_build

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
%_datadir/open-cobol
%_infodir/open-cobol.info*
%_includedir/*
%_libdir/libcob.so

%files -n libcob
%doc COPYING.LIB
%_libdir/libcob.so.*

%changelog
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

