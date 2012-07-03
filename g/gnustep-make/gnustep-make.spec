Name: gnustep-make
Version: 2.0.6
Release: alt4.3
Source: ftp://ftp.gnustep.org/pub/gnustep/core/%name-%version.tar.gz
License: GPL
Group: Development/Other
Summary: GNUstep Makefile package
Packager: Sergey Alembekov <rt@altlinux.ru>
Url: http://www.gnustep.org/

BuildRequires: gcc-objc libobjc-devel star
Requires: gnustep-dirs

%description
This package contains the basic scripts, makefiles and directory
layout needed to run and compile any GNUstep software.  This package
was configured using flattened mode using the system
GNUstep filesystem layout

%package devel
Summary: Files needed to develop applications with gnustep-make
Group: Development/Other
Requires: %name = %version-%release

%description devel
The makefile package is a simplistic, powerful and extensible way to
write makefiles for a GNUstep-based project. It allows the user to
write a GNUstep-based project without having to deal with the complex
issues associated with the configuration and installation of the core
GNUstep libraries. It also allows the user to easily create
cross-compiled binaries.


%prep
%setup -q

%build
sed -i 's,@lib@,%_lib,' FilesystemLayouts/fhs-system-alt
%__autoconf
%configure \
        --enable-flattened \
	--with-layout=fhs-system-alt

%install
%__make install \
        DESTDIR=%buildroot

#install -d %buildroot/etc/profile.d

#cat > %buildroot/etc/profile.d/GNUstep.sh << EOF
##!/bin/sh
#. %_datadir/GNUstep/Makefiles/GNUstep.sh
#
#if [ ! -d \$GNUSTEP_USER_ROOT ]; then
#        mkdir \$GNUSTEP_USER_ROOT
#        chmod +rwx \$GNUSTEP_USER_ROOT
#        . %_datadir/GNUstep/Makefiles/GNUstep.sh
#fi
#EOF

#find %buildroot%_datadir/GNUstep/Makefiles/Instance/Documentation \
#        -type f ! -name '*.html' ! -name '*.css' ! -name '*.gz' | xargs gzip -9nf 

%ifarch x86_64
sed -i -e 's/i586/x86_64/g' $(find %buildroot%_datadir/GNUstep -type f)
%endif

%files
%doc ChangeLog
%_sysconfdir/GNUstep/
%_bindir/*
#%attr(755,root,root) %_sysconfdir/profile.d/*
%dir %_datadir/GNUstep
%dir %_datadir/GNUstep/Makefiles
%dir %_datadir/GNUstep/Makefiles
%attr(755,root,root) %_datadir/GNUstep/Makefiles/*.csh
%attr(755,root,root) %_datadir/GNUstep/Makefiles/*.sh
#%attr(755,root,root) %_datadir/Tools
%_datadir/GNUstep/Makefiles/tar-exclude-list
%_datadir/GNUstep/Makefiles/config.guess
%_datadir/GNUstep/Makefiles/config.sub
%_datadir/GNUstep/Makefiles/gnustep-make-help
%_man1dir/*
%_man7dir/*

%files devel
%_datadir/GNUstep/Makefiles/*.make
%_datadir/GNUstep/Makefiles/*.template
%_datadir/GNUstep/Makefiles/Instance
%_datadir/GNUstep/Makefiles/Master
%attr(755,root,root) %_datadir/GNUstep/Makefiles/install-sh
%attr(755,root,root) %_datadir/GNUstep/Makefiles/mkinstalldirs

%changelog
* Mon Jun 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.6-alt4.3
- Fixed arch type for x86_64

* Fri Jun 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.6-alt4.2
- Set %name-devel as noarch package

* Tue Jun 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.6-alt4.1
- Fixed requires on lsattr

* Mon Apr 06 2009 Sergey Alembekov <rt@altlinux.ru> 2.0.6-alt4
- fix probable x86_64 problems (thanks to raorn@)

* Mon Mar 30 2009 Sergey Alembekov <rt@altlinux.ru> 2.0.6-alt3
- rebuild using filesystem layout fhs-system

* Fri Mar 27 2009 Sergey Alembekov <rt@altlinux.ru> 2.0.6-alt2
- rebuild using flattened mode

* Thu Jul 03 2008 Sergey Alembekov <rt@altlinux.ru> 2.0.6-alt1
- build with new upstream version

* Thu Jul 03 2008 Sergey Alembekov <rt@altlinux.ru> 2.0.4-alt1
- build with new version

* Sun Dec 31 2006 Vitaly Lipatov <lav@altlinux.ru> 1.13.0-alt0.1
- new version 1.13.0 (with rpmrb script)
- fix duplicate GNUStep dir

* Sat Nov 05 2005 Vitaly Lipatov <lav@altlinux.ru> 1.11.1-alt0.1
- initial build for ALT Linux Sisyphus
- spec from PLD Team <feedback@pld-linux.org>
