%set_verify_elf_method unresolved=strict

Name: gnustep-base
Version: 1.24.6
Release: alt5.svn20140226
Epoch: 1

Summary: GNUstep Base library package

License: LGPL
Group: Development/Objective-C
Url: http://www.gnustep.org/

# http://svn.gna.org/svn/gnustep/libs/base/trunk/
Source: %name-%version.tar
Source1: %name.init

Requires: lib%name = %epoch:%version-%release

BuildRequires: gnustep-make gnustep-make-devel libgnutls-devel
BuildRequires: libgnustep-objc2-devel pkgconfig gcc-objc libssl-devel
BuildRequires: libxml2-devel libxslt-devel zlib-devel libffi-devel mount
BuildPreReq: libffcall-devel libgmp-devel libbfd-devel libgcrypt-devel
Requires: gnustep-make >= 2.0.6-alt4 glibc-locales glibc-gconv-modules
BuildPreReq: libicu-devel libcommoncpp2-devel /proc
BuildPreReq: texinfo texi2html texlive-latex-base gnustep-make-doc

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
Conflicts: %name < %epoch:%version-%release

%description -n lib%name
Shared libraries of %name.

%package devel
Summary: Header files and static libraries from %name
Group: Development/Objective-C
Requires: %name = %epoch:%version-%release
Requires: lib%name = %epoch:%version-%release

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
#cp -fR Headers/ObjectiveC2/objc Headers/ObjectiveC2/objc2
%define _libexecdir %_libdir

%build
#. %_datadir/GNUstep/Makefiles/GNUstep.sh
%undefine __libtoolize

%{expand:%%add_optflags %(pkg-config --cflags libffi) -D__GNUSTEP_RUNTIME__}
%autoreconf
%configure \
	--libexecdir=%_libdir \
	--enable-pass-arguments \
	--with-openssl-include=%_includedir/openssl \
	--with-openssl-library=/%_lib/ \
	CC=gcc CPP='gcc -E'
#	--disable-environment-config-file \
#	--disable-importing-config-file \

%make \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes

export LD_LIBRARY_PATH=$PWD/Source/obj
%make_build -C Documentation \
	messages=yes

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make install \
	INSTALL_ROOT_DIR=%buildroot \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	DESTDIR=%buildroot

%makeinstall_std -C Documentation \
     GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -d %buildroot%_initdir
sed -e "s!@TOOLSARCHDIR@!%prefix/System/Tools!" %SOURCE1 > %buildroot%_initdir/gdomap
rm -Rf %buildroot%_libexecdir/GNUstep/Libraries/gnustep-base/Versions/1.14/Resources/NSTimeZones/

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

for i in ChangeLog*; do
	gzip $i
done

%post
grep -q '^gdomap' /etc/services \
|| (echo "gdomap 538/tcp # GNUstep distributed objects" >> /etc/services \
&& echo "gdomap 538/udp # GNUstep distributed objects" >> /etc/services)


%postun
mv -f /etc/services /etc/services.orig
grep -v "^gdomap 538" /etc/services.orig > /etc/services
rm -f /etc/services.orig

%files
%_initdir/gdomap
%doc ANNOUNCE COPYING COPYING.LIB ChangeLog*
%doc NEWS README
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
%_includedir/gnustep

%files doc
%_docdir/GNUstep
%_infodir/*
 
%changelog
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
