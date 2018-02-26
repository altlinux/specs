# TODO:
# - check spelling, typo & rel 1
# - find a nice way to include the /etc/profile.d scripts
# - think bout the %prefix

%define _realname	gnustep-make

Name: gnustep-make-libFoundation
Version: 1.11.0
Release: alt0.1

Summary: GNUstep Makefile package libFoundation version

License: GPL
Group: Development/Other
Source: ftp://ftp.gnustep.org/pub/gnustep/core/%_realname-%version.tar.bz2
Url: http://www.gnustep.org/

# Automatically added by buildreq on Sat Nov 05 2005
BuildRequires: gcc-objc libobjc-devel star

BuildRequires: autoconf
BuildRequires: automake
#%{?with_docs:BuildRequires: gnustep-make-devel}
#BuildRequires: tetex
#BuildRequires: tetex-dvips
#BuildRequires: tetex-format-latex
#BuildRequires: tetex-format-plain
#BuildRequires: texinfo-texi2dvi
Requires: gnustep-dirs
Conflicts: gnustep-core

%define _prefix		/usr/%_lib/GNUstep-libFoundation
%define gsos		linux-gnu
%ifarch %ix86
%define gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define gscpu		%(echo %_target_cpu | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
This package contains the basic tools needed to run GNUstep
applications.

This version of gnustep-make is compiled for support with libFoundation.

%package devel
Summary: Files needed to develop applications with gnustep-make libFoundation version
Summary(pl):	Pliki potrzebne do tworzenia aplikacji przy u¿yciu gnustep-make wersja libFoundation
Group: Development/Other
Requires: %name = %version-%release

%description devel
The makefile package is a simplistic, powerful and extensible way to
write makefiles for a GNUstep-based project. It allows the user to
write a GNUstep-based project without having to deal with the complex
issues associated with the configuration and installation of the core
GNUstep libraries. It also allows the user to easily create
cross-compiled binaries.

This version of gnustep-make is compiled for support with libFoundation.

%prep
%setup -q -n %_realname-%version

%build
cp -f /usr/share/automake/config.* .
%__autoconf
%configure \
	--disable-flattened \
	--with-tar=tar \
	--with-library-combo=gnu-fd-nil

%__make

#%if %{with docs}
#%__make -C Documentation
#%endif

%install
%__make install \
	special_prefix=%buildroot

#libFoundation + friends won't build without that
ln -s Library/Makefiles %buildroot%prefix/System/Makefiles

#%if %{with docs}
#%__make -C Documentation install \
#	GNUSTEP_INSTALLATION_DIR=%buildroot%prefix/System
#%endif

#install -d %buildroot/etc/profile.d
## Create profile files
#cat > %buildroot/etc/profile.d/GNUstep.sh << EOF
##!/bin/sh
#. %prefix/System/Library/Makefiles/GNUstep.sh
#
#if [ ! -d \$GNUSTEP_USER_ROOT ]; then
#	mkdir \$GNUSTEP_USER_ROOT
#	chmod +rwx \$GNUSTEP_USER_ROOT
#	. %prefix/System/Library/Makefiles/GNUstep.sh
#fi
#EOF

#cat > %buildroot/etc/profile.d/GNUstep.csh << EOF
##!/bin/csh
#source %prefix/System/Library/Makefiles/GNUstep.csh
#
#test -d \$GNUSTEP_USER_ROOT
#if (\$status != 0) then
#	mkdir \$GNUSTEP_USER_ROOT
#	chmod +rwx \$GNUSTEP_USER_ROOT
#	source %prefix/System/Library/Makefiles/GNUstep.csh
#endif
#EOF

# not (yet?) supported by rpm-compress-doc
find %buildroot%prefix/System/Library/Documentation \
	-type f ! -name '*.html' ! -name '*.css' ! -name '*.gz' | xargs gzip -9nf

%pre
if [ -d %prefix/System/Makefiles -a ! -L %prefix/System/Makefiles ]; then
	[ -d %prefix/System/Library ] || install -d %prefix/System/Library
	mv -f %prefix/System/Makefiles %prefix/System/Library
	ln -sf Library/Makefiles %prefix/System/Makefiles
	echo 'Reinstall gnustep-make and gnustep-make-devel if some files are missing.' >&2
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog
#%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/profile.d/GNUstep.sh
#%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/profile.d/GNUstep.csh

# GNUstep top-level
%dir %prefix
%prefix/Local
%dir %prefix/System
%prefix/System/Makefiles
# System domain
%prefix/System/Applications
%dir %prefix/System/Library
%prefix/System/share
%attr(755,root,root) %prefix/System/Tools

# System/Library folder
%prefix/System/Library/ApplicationSupport
%prefix/System/Library/Bundles
%prefix/System/Library/ColorPickers
%prefix/System/Library/Colors
%prefix/System/Library/DocTemplates
#%if %{with docs}
#%docdir %prefix/System/Library/Documentation
#%dir %prefix/System/Library/Documentation
#%endif
%prefix/System/Library/Fonts
%prefix/System/Library/Frameworks
%prefix/System/Library/Headers
%prefix/System/Library/Images
%prefix/System/Library/KeyBindings
%prefix/System/Library/Libraries
%dir %prefix/System/Library/Makefiles
%prefix/System/Library/PostScript
%prefix/System/Library/Services
%prefix/System/Library/Sounds
#%if %{with docs}
#%dir %prefix/System/Library/Documentation/Developer
#%dir %prefix/System/Library/Documentation/Developer/Make
#%prefix/System/Library/Documentation/Developer/Make/ReleaseNotes
#%dir %prefix/System/Library/Documentation/User
#%prefix/System/Library/Documentation/User/GNUstep
#%dir %prefix/System/Library/Documentation/info
#%prefix/System/Library/Documentation/info/*.info*
#%dir %prefix/System/Library/Documentation/man
#%dir %prefix/System/Library/Documentation/man/man1
#%prefix/System/Library/Documentation/man/man1/openapp.1*
#%dir %prefix/System/Library/Documentation/man/man7
#%prefix/System/Library/Documentation/man/man7/GNUstep.7*
#%endif

%attr(755,root,root) %prefix/System/Library/Makefiles/config.*
%prefix/System/Library/Makefiles/tar-exclude-list
%attr(755,root,root) %prefix/System/Library/Makefiles/*.sh
%attr(755,root,root) %prefix/System/Library/Makefiles/*.csh
%dir %prefix/System/Library/Makefiles/%gscpu
%dir %prefix/System/Library/Makefiles/%gscpu/%gsos
%attr(755,root,root) %prefix/System/Library/Makefiles/%gscpu/%gsos/user_home
%attr(755,root,root) %prefix/System/Library/Makefiles/%gscpu/%gsos/which_lib

%files devel
%defattr(644,root,root,755)
#%if %{with docs}
#%docdir %prefix/System/Library/Documentation
#%prefix/System/Library/Documentation/Developer/Make/Manual
#%endif

%prefix/System/Library/Makefiles/*.make
%prefix/System/Library/Makefiles/*.template
%prefix/System/Library/Makefiles/Instance
%prefix/System/Library/Makefiles/Master
%prefix/System/Library/Makefiles/%gscpu/%gsos/*.make
%attr(755,root,root) %prefix/System/Library/Makefiles/install-sh
%attr(755,root,root) %prefix/System/Library/Makefiles/mkinstalldirs

%changelog
* Sat Nov 05 2005 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt0.1
- initial build for ALT Linux Sisyphus
- spec from PLD Team <feedback@pld-linux.org>
