%define freetypemajorversion 6

Name: libfreetype-infinality
Version: 2.4.10
Release: alt2

Summary: A free and portable font rendering engine
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
Patch91: freetype-add-subpixel-hinting-infinality-20120616-01.patch
Patch92: freetype-enable-subpixel-hinting-infinality-20120615-01.patch
Patch93: freetype-entire-infinality-patchset-20120615-01.patch

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

%package devel
Summary: Header files and library for development with FreeType2
Group: Development/C
Requires: %name = %version-%release
Provides: freetype2-devel = %version
Obsoletes: freetype2-devel < %version
Conflicts: libfreetype-devel

%description devel
This package contains the header files and development libraries needed
to develop programs that use the FreeType2 library.

%package devel-static
Summary: The FreeType2 static library
Group: Development/C
Requires: %name-devel = %version-%release
Provides: freetype2-devel-static = %version
Obsoletes: freetype2-devel-static < %version
Conflicts: libfreetype-devel-static

%description devel-static
This package contains the FreeType2 static library.

%prep
%setup -n freetype-%version -a1 

%patch1 -p1
%patch2 -p1
%patch3 -p1

%patch11 -p1
%patch12 -p1

%patch91 -p1
%patch92 -p1
%patch93 -p1

%build
%add_optflags -fno-strict-aliasing
%configure %{subst_enable static}

# get rid of RPATH
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' builds/unix/libtool

%make_build

%install
%makeinstall_std


wordsize=$(echo -e '#include <bits/wordsize.h>\n__WORDSIZE' |cpp -P)
[ "$wordsize" -ge 32 ]
mv %buildroot%_includedir/freetype2/freetype/config/ftconfig{,-$wordsize}.h
cat >%buildroot%_includedir/freetype2/freetype/config/ftconfig.h <<'EOF'
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
%define develdocdir %_docdir/%name-devel-%version
mkdir -p %buildroot%docdir
mkdir -p %buildroot%develdocdir
cp -a docs/* %buildroot%develdocdir/
pushd %buildroot%develdocdir
	bzip2 -9 CHANGES raster.txt
	rm INSTALL* release
popd
mv %buildroot%develdocdir/{FTL.TXT,LICENSE.TXT,CHANGES.bz2} %buildroot%docdir/

%define ld_preload_script_name %{name}-%{_arch}.sh
%define ld_preload_script %buildroot%{_sysconfdir}/profile.d/%ld_preload_script_name

mkdir -p %buildroot%{_sysconfdir}/profile.d/
/bin/echo "PRELOAD=1; if [ -f /etc/sysconfig/fonts ]; then . /etc/sysconfig/fonts; fi; A1=\`arch\`; A2=%{_arch}; if [ \"\${A1:0:1}\" = \"\${A2:0:1}\" -a ! \"\$PRELOAD\" = \"0\" ]; then ADDED=\`/bin/echo \$LD_PRELOAD | grep \"%{_libdir}/libfreetype.so.6\" | wc -l\`; if [ \"\$ADDED\" = \"0\" ]; then export LD_PRELOAD=%{_libdir}/%{name}/libfreetype.so.%{freetypemajorversion}:\$LD_PRELOAD ; fi; fi" > %ld_preload_script
chmod 755 %ld_preload_script

install -pD -m755 %SOURCE91 %buildroot%_sysconfdir/profile.d/

cp %SOURCE91 %buildroot%docdir
cp %SOURCE92 %buildroot%docdir
cp %PATCH91 %buildroot%docdir
cp %PATCH92 %buildroot%docdir
cp %PATCH93 %buildroot%docdir
cp %ld_preload_script %buildroot%docdir

# Move library to avoid conflict with official FreeType package
mkdir %buildroot%{_libdir}/%{name}
mv -f %buildroot%{_libdir}/libfreetype.so.* \
      %buildroot%{_libdir}/%{name}

%set_verify_elf_method strict

%files
%docdir
%_libdir/%name/*.so.*
%{_sysconfdir}/profile.d/%ld_preload_script_name
%config %{_sysconfdir}/profile.d/infinality-settings.sh

%files devel
%develdocdir
%_bindir/*-config
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_datadir/aclocal/*.m4

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Wed Dec 19 2012 Vladimir Didenko <cow@altlinux.ru> 2.4.10-alt2
- Removed dependency on official freetype package

* Mon Dec 10 2012 Vladimir Didenko <cow@altlinux.ru> 2.4.10-alt1
- Initial build 
