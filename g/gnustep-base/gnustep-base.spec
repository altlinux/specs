%set_verify_elf_method unresolved=strict
%define gnustep_ver 1.29
%def_without build_debug
%def_without objc2
%def_with doc

Name: gnustep-base
Version: 1.29.0
Release: alt1
Epoch: 1

Summary: GNUstep Base library package

License: LGPL-2.1+ and GPL-3.0+
Group: Development/Objective-C
Url: http://www.gnustep.org/

# http://svn.gna.org/svn/gnustep/libs/base/trunk/
Source: %name-%version.tar
Source1: %name.init
Patch1: %name-alt-objc2.patch
Patch2: %name-use_system-wide_crypto-policies.patch

Requires: lib%name = %EVR

BuildRequires: gnustep-make-devel libgnutls-devel
%if_with objc2
BuildRequires: libgnustep-objc2-devel
%endif
BuildRequires: pkgconfig libssl-devel
BuildRequires: libxml2-devel libxslt-devel zlib-devel libffi-devel mount
BuildRequires: libffcall-devel libgmp-devel libbfd-devel libgcrypt-devel
BuildRequires: libicu-devel /proc
%if_with doc
BuildRequires: texinfo texi2html texlive-latex-base gnustep-make-doc
%endif
BuildRequires: tzdata ca-certificates

Requires: gnustep-make >= 2.0.6-alt4 glibc-locales glibc-gconv-modules

%description
The GNUstep Base Library is a powerful fast library of general-purpose,
non-graphical Objective C classes, inspired by the superb OpenStep API but
implementing Apple and GNU additions to the API as well.  It includes for
example classes for unicode strings, arrays, dictionaries, sets, byte
streams, typed coders, invocations, notifications, notification dispatchers,
scanners, tasks, files, networking, threading, remote object messaging
support (distributed objects), event loops, loadable bundles, attributed
unicode strings, xml, mime, user defaults. This package includes development
headers too.

%package -n lib%name
Summary: Shared libraries of %name
Group: System/Libraries
Conflicts: %name < %EVR

%description -n lib%name
Shared libraries of %name.

%package devel
Summary: Header files and static libraries from %name
Group: Development/Objective-C
Requires: %name = %EVR
Requires: lib%name = %EVR

%description devel
Libraries and includes files for developing programs based on %name.

%package doc
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch
Requires: gnustep-make-doc

%description doc
Development documentation for %name.

%prep
%setup
%if_with objc2
%patch1 -p1
%endif
%patch2 -p1

%build
%if_with objc2
export OBJCFLAGS="$OBJCFLAGS -D__GNU_LIBOBJC__=1"
%endif
%undefine _configure_gettext
%undefine __libtoolize
%autoreconf
%configure \
	--libexecdir=%_libdir \
	--enable-pass-arguments

%make \
%if_with build_debug
	messages=yes \
	debug=yes \
%endif
	strip=no \
	shared=yes

%if_with doc
export LD_LIBRARY_PATH=$PWD/Source/obj
%make_build -C Documentation \
%if_with build_debug
	messages=yes
%endif
%endif

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%if_with doc
%makeinstall_std -C Documentation \
     GNUSTEP_INSTALLATION_DOMAIN=SYSTEM
%endif

install -d %buildroot%_initdir
sed -e "s!@TOOLSARCHDIR@!%prefix/System/Tools!" %SOURCE1 > %buildroot%_initdir/gdomap
rm -Rf %buildroot%_libdir/GNUstep/Libraries/gnustep-base/Versions/1.14/Resources/NSTimeZones/

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

for i in ChangeLog*; do
	gzip $i
done

# Set symlinks to system timezones, localtime and ca-certificates
cd %buildroot%_libdir/GNUstep/Libraries/gnustep-base/Versions/%gnustep_ver/Resources/NSTimeZones
rm -rf zones
cd %buildroot%_libdir/GNUstep/Libraries/gnustep-base/Versions/%gnustep_ver/Resources/GSTLS
rm -rf ca-certificates.crt
ln -s /usr/share/ca-certificates/ca-bundle.crt ca-certificates.crt

%post
t="%_libdir/GNUstep/Libraries/gnustep-base/Versions/%gnustep_ver/Resources/NSTimeZones/zones"
if [ ! -d "$t" ];then
    ln -s /usr/share/zoneinfo "$t"
fi

%postun
t="%_libdir/GNUstep/Libraries/gnustep-base/Versions/%gnustep_ver/Resources/NSTimeZones/zones"
if [ -L "$t" ];then
    rm -f "$t"
fi

%files
%_initdir/gdomap
%doc ANNOUNCE COPYING COPYING.LIB ChangeLog*
%doc NEWS README.md
%_bindir/*
%_libdir/GNUstep/*
%_man1dir/*
%_man8dir/*

%files -n lib%name
%_libdir/libgnustep-base.so.*

%files devel
%_datadir/GNUstep/Makefiles/Additional/base.make
%_libdir/libgnustep-base.so
%_includedir/Foundation
%_includedir/GNUstepBase

%if_with doc
%files doc
%_docdir/GNUstep
%_infodir/*
%endif
 
%changelog
* Tue Jan 10 2023 Andrey Cherepanov <cas@altlinux.org> 1:1.29.0-alt1
- New version.

* Thu Dec 29 2022 Andrey Cherepanov <cas@altlinux.org> 1:1.28.1-alt1
- New version.

* Tue Dec 27 2022 Andrey Cherepanov <cas@altlinux.org> 1:1.28.0-alt3.git47b6e9d05
- New upstream snapshot.

* Fri Jun 11 2021 Andrey Cherepanov <cas@altlinux.org> 1:1.28.0-alt2
- Use sources from base-1_28_0.

* Wed Apr 28 2021 Andrey Cherepanov <cas@altlinux.org> 1:1.28.0-alt1
- New version.

* Tue Oct 13 2020 Andrey Cherepanov <cas@altlinux.org> 1:1.27.0-alt1
- New version.
- Fix License tag according to SPDX.
- Build without gnustep-objc2.

* Fri Apr 24 2020 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1:1.24.6-alt9.svn20140226
- Blindly s/libcommoncpp2-devel//g to fix FTBFS.

* Sat Feb 09 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:1.24.6-alt8.svn20140226
- Built for aarch64 architecture.
- Removed useless services(5) hacking from %%post and %%postun scripts.

* Mon Sep 26 2016 Andrey Cherepanov <cas@altlinux.org> 1:1.24.6-alt7.svn20140226
- Set symlinks to system timezones and ca-certificates

* Wed Feb 17 2016 Andrey Cherepanov <cas@altlinux.org> 1:1.24.6-alt6.svn20140226
- Rebuild with libicu56

* Wed Dec 16 2015 Andrey Cherepanov <cas@altlinux.org> 1:1.24.6-alt5.svn20140226
- Build with gcc instead of clang

* Mon Mar 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.6-alt4.svn20140226
- New snapshot

* Mon Feb 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.6-alt4.svn20140126
- BuildPreReq: gnustep-make-doc

* Mon Feb 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.6-alt3.svn20140126
- Added documentation

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.6-alt2.svn20140126
- Built with clang

* Tue Jan 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.6-alt1.svn20140126
- New snapshot

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.6-alt1.git20131231
- Version 1.24.6

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.5-alt1.git20130910
- Version 1.24.5

* Sun May 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.4-alt2.git20130501
- New snapshot

* Wed Mar 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.4-alt2.git20130317
- New snapshot

* Wed Mar 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.4-alt2.git20130303
- Rebuilt

* Mon Mar 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.4-alt1.git20130303
- Version 1.24.4

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.2-alt5.git20130129
- New snapshot

* Fri Jan 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.2-alt5.git20130112
- Fixed for autoreconf

* Sat Jan 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.2-alt4.git20130112
- New snapshot

* Sun Dec 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.2-alt4.git20121227
- New snapshot

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.2-alt3.svn20121208
- Rebuilt with fixed gnustep-make

* Mon Dec 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.2-alt2.svn20121208
- Compressed ChangeLogs
- Moved shared libraries into separate package

* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.24.2-alt1.svn20121208
- Version 1.24.2

* Wed Dec 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.14.1-alt6.2
- Fixed build (forced with gcc 4.6)

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.14.1-alt6.1
- NMU: rebuild to fix autogenerated provides. (closes: 27414)

* Mon Jan 31 2011 Sergey Alembekov <rt@altlinux.ru> 1:1.14.1-alt6
- ALT bug #4769

* Sun Aug 22 2010 Sergey Alembekov <rt@altlinux.ru> 1:1.14.1-alt5
- rebuild with new libffi
- fix repocop warning rpm-obsolete-self

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1:1.14.1-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * backup-file-in-package for gnustep-base
  * postclean-05-filetriggers for spec file

* Fri Apr 10 2009 Sergey Alembekov <rt@altlinux.ru> 1:1.14.1-alt4
- add missed requires 
- remove unneeded NSTimeZones

* Mon Apr 06 2009 Sergey Alembekov <rt@altlinux.ru> 1:1.14.1-alt3
- rebuild with gnustep-make using fhs mode

* Fri Mar 27 2009 Sergey Alembekov <rt@altlinux.ru> 1:1.14.1-alt2
- rebuild with gnustep-make using flattened mode
- fix initscript

* Wed Sep 03 2008 Sergey Alembekov <rt@altlinux.ru> 1:1.14.1-alt1.3
- chmod libgnustep-base.1.14.1 to 644 from 600

* Tue Aug 05 2008 Sergey Alembekov <rt@altlinux.ru> 1:1.14.1-alt1.2
- downgrade to version 1.14.1 becouse of SOAP incompatibility 
- fix x86_64 build
- TODO: initscript fix

* Tue Jul 15 2008 Sergey Alembekov <rt@altlinux.ru> 1.16.3-alt1.1
- version update
- add changelog from old orphaned package
- remove using ld.conf by copying *.so to %_libdir

* Thu Jul 03 2008 Sergey Alembekov <rt@altlinux.ru> 1.16.2-alt1
- build for ALTLinux

* Sat Nov 05 2005 Vitaly Lipatov <lav@altlinux.ru> 1.11.1-alt0.1
- initial build for ALT Linux Sisyphus
- spec from PLD Team <feedback@pld-linux.org>
