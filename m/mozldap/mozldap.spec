%define major  6
%define minor  0
%define submin 7

Summary:	Mozilla LDAP C SDK
Name:		mozldap
Version:	6.0.7
Release:	alt1
License:	MPL/GPL/LGPL
URL:		https://wiki.mozilla.org/LDAP_C_SDK
Group:		System/Libraries
Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	mozldap.tar
Source2:	fix_headers.sh

Patch2:		ldapcsdk-5.1.7-alt-rpath-link.patch
Patch3:		mozldap-alt-allow-x86_64-host-build.patch
Patch5:		mozldap-alt-pc-fix.patch
Patch6:		mozldap-fix-pthread-link.patch

# Automatically added by buildreq on Mon Feb 26 2007 (-bi)
BuildRequires: chrpath gcc-c++ libsasl2-devel libsvrcore-devel nss-utils python-base

Conflicts: mozilla < 1.8

BuildRequires: autoconf_2.13
%set_autoconf_version 2.13

%description
The Mozilla LDAP C SDK is a set of libraries that
allow applications to communicate with LDAP directory
servers.  These libraries are derived from the University
of Michigan and Netscape LDAP libraries.  They use Mozilla
NSPR and NSS for crypto.

%package tools
Summary:          Tools for the Mozilla LDAP C SDK
Group:            Development/Other
Requires:         %name = %version-%release

%description tools
The mozldap-tools package provides the ldapsearch,
ldapmodify, and ldapdelete tools that use the
Mozilla LDAP C SDK libraries.

%package devel
Summary:          Development libraries and examples for Mozilla LDAP C SDK
Group:            Development/C
Requires:         %name = %version-%release

%description devel
Header and Library files for doing development with the Mozilla LDAP C SDK

%prep
%setup -q -n %name-%version -c
cd mozldap

%patch2 -p0 -b .fix2
%patch3 -p0 -b .fix3
%patch5 -p0 -b .fix5
%patch6 -p0 -b .fix6

%build
cd mozldap/c-sdk

# Enable compiler optimizations and disable debugging code
export BUILD_OPT=1

# Generate symbolic info for debuggers
export XCFLAGS="$RPM_OPT_FLAGS $(pkg-config --cflags-only-I nss) $(pkg-config --cflags-only-I nspr)"
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1

%ifarch x86_64
export USE_64=1
%endif

# Build ldapsdk
%add_optflags %optflags_shared
%__subst 's|AC_CONFIG_AUX_DIR(\${srcdir}/config/autoconf)|AC_CONFIG_AUX_DIR(config/autoconf)|' configure.in
%__autoconf

%configure \
    --with-sasl \
    --enable-clu \
    --with-system-nss \
    --with-system-nspr \
    --with-system-svrcore \
    --with-pthreads \
    \
    --enable-strip \
    --enable-optimize="$RPM_OPT_FLAGS" \
    --enable-mdupdate \
    --disable-debug \
%ifarch x86_64
    --enable-64bit \
%endif
    #
%make

%install
# There is no make install target so we'll do it ourselves.
mkdir -p %buildroot/%_bindir \
    %buildroot/%_includedir/%name \
    %buildroot/%_libdir/%name \
    %buildroot/%_datadir/%name/etc \
    #

# Copy the binary libraries we want
find dist/lib/ -name '*.so' -execdir %__install -m 755 -t %buildroot/%_libdir \{\} \;

# Copy the binaries we want
find dist/bin/ -name 'ldap*' |
while read f; do
    install -m 755 -- "$f" "%buildroot/%_bindir/moz${f##*/}"
done

# Copy the include files
find dist/public/ldap -name '*.h' -execdir %__install -m 644 -t %buildroot/%_includedir/%name \{\} \;
%SOURCE2 %_includedir %buildroot/%_includedir/%name

# Copy the developer files
cp -r mozldap/c-sdk/ldap/examples %buildroot/%_datadir/%name

install -m 644 -t %buildroot/%_datadir/%name/etc \
    mozldap/c-sdk/ldap/examples/xmplflt.conf \
    mozldap/c-sdk/ldap/libraries/libldap/ldaptemplates.conf \
    mozldap/c-sdk/ldap/libraries/libldap/ldapfilter.conf \
    mozldap/c-sdk/ldap/libraries/libldap/ldapsearchprefs.conf \
    #

# Set up our package file
mkdir -p %buildroot/%_libdir/pkgconfig
sed \
    -e "s,%%bindir%%,%_bindir,g" \
    -e "s,%%libdir%%,%_libdir,g" \
    -e "s,%%prefix%%,%_prefix,g" \
    -e "s,%%exec_prefix%%,%_prefix,g" \
    -e "s,%%includedir%%,%_includedir/%name,g" \
    -e "s,%%major%%,%major,g" \
    -e "s,%%minor%%,%minor,g" \
    -e "s,%%submin%%,%submin,g" \
    -e "s,%%libsuffix%%,%major%minor,g" \
    -e "s,%%NSPR_VERSION%%,$(pkg-config --modversion nspr),g" \
    -e "s,%%NSS_VERSION%%,$(pkg-config --modversion nss),g" \
    -e "s,%%MOZLDAP_VERSION%%,%version,g" \
    mozldap/c-sdk/mozldap.pc.in > \
    %buildroot/%_libdir/pkgconfig/%name.pc

# Rename the libraries and create the symlinks
cd %buildroot/%_libdir
for f in *.so; do
  mv    "$f"                       "$f.%major.%minor.%submin"
  ln -s "$f.%major"                "$f"
  ln -s "$f.%major.%minor"         "$f.%major"
  ln -s "$f.%major.%minor.%submin" "$f.%major.%minor"  
done

find -type f |
while read f; do
  file "$f" |grep -qs ELF || continue
  if chrpath -l "$f" |fgrep -qs "RPATH="; then
    chrpath -d "$f"
  fi
done

%files
%_libdir/*.so*

%files tools
%_bindir/*

%files devel
%_libdir/pkgconfig/*.pc
%_includedir/%name
%_datadir/%name

%changelog
* Thu Mar 10 2011 Alexey Gladkov <legion@altlinux.ru> 6.0.7-alt1
- New version (6.0.7).

* Fri Dec 17 2010 Alexey Gladkov <legion@altlinux.ru> 6.0.6-alt3
- Rebuilt for new depends.

* Mon Dec 21 2009 Alexey Gladkov <legion@altlinux.ru> 6.0.6-alt2
- Remove obsolete macros.

* Wed Nov 19 2008 Alexey Gladkov <legion@altlinux.ru> 6.0.6-alt1
- New version (6.0.6).

* Fri Jul 04 2008 Alexey Gladkov <legion@altlinux.ru> 6.0.4-alt1
- New version (6.0.4).

* Sat Feb 24 2007 Alexey Gladkov <legion@altlinux.ru> 6.0.2-alt1
- New version (6.0.2).
- Build with system libsvrcore.
- Build with libsasl2.

* Wed Nov 22 2006 Alexey Gladkov <legion@altlinux.ru> 6.0.0-alt1
- new version (6.0.0).
- new svrcore (4.0.2).
- add support for submit/patch level (3rd level) in version numbering.
- add svrcore.pc.
- move ldap/svrcore.h to svrcore/svrcore.h.
- Patch disabling OS_TEST autoguessing for %%ix86 builds on x86_64 host.
- SONAME change.

* Sun Aug 20 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.7-alt2.20060820
- Bugfix build from CVS.
- Correct confilcts.

* Mon Apr 03 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.7-alt1
- SVRCORE build inside.
- Removed RPATH.
- first build for ALT Linux.

* Tue Jan 31 2006 Rich Megginson <rmeggins@redhat.com> - 5.17-2
- use --with-system-svrcore to configure

* Mon Dec 19 2005 Rich Megginson <rmeggins@redhat.com> - 5.17-1
- Initial revision

