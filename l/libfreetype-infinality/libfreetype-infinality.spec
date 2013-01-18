%define freetypemajorversion 6

Name: libfreetype-infinality
Version: 2.4.11
Release: alt3

Summary: A free and portable font rendering engine with patches from http://www.infinality.net
License: FTL or GPLv2+
Group: System/Libraries
Url: http://www.freetype.org/
Packager: Vladimir Didenko <cow@altlinux.ru>

Source0: freetype-%version.tar
Source1: freetype-doc-%version.tar

Source91: infinality-settings.sh
Source92: README.infinality

Patch1: freetype-2.4.10-alt-compat-version-script.patch
Patch2: freetype-2.4.10-alt-freetype-config.patch
Patch3: freetype-2.4.10-alt-fttrigon.patch

Patch11: freetype-2.4.10-rh-enable-subpixel-rendering.patch
Patch12: freetype-2.4.10-rh-enable-valid.patch

#Infinality patches
Patch91: freetype-enable-subpixel-hinting-infinality-20120615-01.patch
Patch92: freetype-entire-infinality-patchset-20130104-01.patch

Provides: freetype2-infinality = %version
Obsoletes: freetype2-infinality < %version

%def_disable static

BuildRequires: libX11-devel zlib-devel

%description
The FreeType engine is a free and portable TrueType font rendering
engine, developed to provide TrueType support for a variety of
platforms and environments.  FreeType is a library which can open
and manages font files as well as efficiently load, hint and render
individual glyphs.  FreeType is not a font server or a complete
text-rendering library.

This version is compiled with the Infinality patches. It transparently
overrides the system library using ld.so.conf.d.

%prep
%setup -n freetype-%version -a1 

%patch1 -p1
%patch2 -p1
%patch3 -p1

%patch11 -p1
%patch12 -p1

%patch91 -p1
%patch92 -p1

%build
%add_optflags -fno-strict-aliasing
%configure %{subst_enable static}

# get rid of RPATH
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' builds/unix/libtool

%make_build

%install
%makeinstall_std

wordsize=$(echo -e '#include <bits/wordsize.h>\n__WORDSIZE' | cpp -P | sed '/^$/d')
[ "$wordsize" -ge 32 ]
mv %buildroot%_includedir/freetype2/freetype/config/ftconfig{,-$wordsize}.h
cat >%buildroot%_includedir/freetype2/freetype/config/ftconfig.h <<EOF
#ifndef __FTCONFIG_H__MULTILIB
#define __FTCONFIG_H__MULTILIB

#include <bits/wordsize.h>

#if __WORDSIZE == 32
# include <freetype/config/ftconfig-32.h>
#elif __WORDSIZE == 64
# include <freetype/config/ftconfig-64.h>
#else
# error "unexpected value for __WORDSIZE macro"
#endif

#endif
EOF

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir

%define ld_preload_script_name infinality-ld-preload.sh
%define ld_preload_script %buildroot%{_sysconfdir}/profile.d/%ld_preload_script_name

mkdir -p %buildroot%{_sysconfdir}/profile.d/
/bin/echo "export LD_PRELOAD=/usr/'\$LIB'/%{name}/libfreetype.so.%{freetypemajorversion}:\$LD_PRELOAD" > %ld_preload_script
chmod 755 %ld_preload_script

install -pD -m755 %SOURCE91 %buildroot%_sysconfdir/profile.d/

cp %SOURCE91 %buildroot%docdir
cp %SOURCE92 %buildroot%docdir
cp %PATCH91 %buildroot%docdir
cp %PATCH92 %buildroot%docdir
cp %ld_preload_script %buildroot%docdir

# Move library to avoid conflict with official FreeType package
mkdir %buildroot%{_libdir}/%{name}
mv -f %buildroot%{_libdir}/libfreetype.so.* \
      %buildroot%{_libdir}/%{name}

#remove devel data. Infinality package is not oriented on any development
rm -f %buildroot%_bindir/*-config
rm -f %buildroot%_libdir/*.so
rm -fr %buildroot%_includedir/
rm -f %buildroot%_pkgconfigdir/*.pc
rm -f %buildroot%_datadir/aclocal/*.m4

%set_verify_elf_method strict

%files
%docdir
%_libdir/%name/
%{_sysconfdir}/profile.d/%ld_preload_script_name
%config %{_sysconfdir}/profile.d/infinality-settings.sh

%changelog
* Thu Jan 17 2013 Vladimir Didenko <cow@altlinux.ru> 2.4.11-alt3
- Include %_libdir/%name/ directory

* Thu Jan 17 2013 Vladimir Didenko <cow@altlinux.ru> 2.4.11-alt2
- Fixed ld preload script to properly work on biarch systems

* Wed Jan 9 2013 Vladimir Didenko <cow@altlinux.ru> 2.4.11-alt1
- 2.4.11

* Fri Dec 21 2012 Vladimir Didenko <cow@altlinux.ru> 2.4.10-alt3
- Deleted devel packages

* Wed Dec 19 2012 Vladimir Didenko <cow@altlinux.ru> 2.4.10-alt2
- Removed dependency on official freetype package

* Mon Dec 10 2012 Vladimir Didenko <cow@altlinux.ru> 2.4.10-alt1
- Initial build 
