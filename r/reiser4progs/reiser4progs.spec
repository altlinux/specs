%def_enable minimal

Name: reiser4progs
Version: 1.1.0
Release: alt1
Summary: Utilities for reiser4 filesystems
License: GPLv2
Group: System/Kernel and hardware
URL: http://reiser4.sourceforge.net/

%define reiser_libver %(echo %version | cut -d . -f 1-2)

Source: %name-%version.tar
Patch1: %name-%version-alt-format.patch
Patch2: %name-%version-alt-linking.patch

# Automatically added by buildreq on Wed Mar 17 2010
BuildRequires: libaal-devel-static libaal-minimal-devel libncurses-devel libreadline-devel libuuid-devel

%description
Utilities for manipulating reiser4 filesystems.

%package -n libreiser4
Summary: Libraries for use by reiser4 tools
Group: Development/C

%description -n libreiser4
Libraries for use by reiser4 tools.

%package -n libreiser4-devel
Summary: Development libraries and headers for developing reiser4 tools
Group: Development/C
Requires: libreiser4 = %version-%release, libaal-devel

%description -n libreiser4-devel
Development libraries and headers for developing reiser4 tools.

%package -n libreiser4-devel-static
Summary: Static libraries for developing reiser4 tools
Group: Development/C
Requires: libreiser4-devel = %version-%release

%description -n libreiser4-devel-static
Static libraries for developing reiser4 tools.

%package -n libreiser4-minimal
Summary: Minimal utilities for reiser4 filesystem
Group: Development/C
Requires: libaal-minimal, libreiser4 = %version-%release

%description -n libreiser4-minimal
Development libraries and headers for developing minimal reiser4 tools.

%package -n libreiser4-minimal-devel
Summary: Development libraries and headers for developing minimal reiser4 tools
Group: Development/C
Requires: libreiser4-minimal = %version-%release, libaal-minimal-devel, libreiser4-devel = %version-%release

%description -n libreiser4-minimal-devel
Development libraries and headers for developing minimal reiser4 tools.

%package -n libreiser4-minimal-devel-static
Summary: Static libraries for developing minimal reiser4 tools
Group: Development/C
Requires: libreiser4-minimal-devel = %version-%release, libaal-minimal-devel, libreiser4-devel = %version-%release

%description -n libreiser4-minimal-devel-static
Static libraries for developing minimal reiser4 tools.

%prep
%setup
%patch1 -p2
%patch2 -p2
sed -i -r '/^[[:blank:]]+\.\/run-ldconfig/d' Makefile.{am,in}

%build
%configure \
	--sbindir=/sbin \
	--libdir=/%_lib \
%if_enabled minimal
	--enable-libminimal \
	--disable-fnv1-hash \
	--disable-rupasov-hash \
	--disable-tea-hash \
	--disable-deg-hash \
	--disable-short-keys \
	--disable-special \
	--disable-dot_o_fibre \
	--disable-ext_3_fibre \
	--disable-lexic_fibre \
%endif
	--with-readline

# Hackish way to fix underlinking in 1.0.7:
subst 's@LDFLAGS =@LDFLAGS = ../libmisc/.libs/libmisc.a -luuid@' libreiser4/Makefile

# We need these to be built before build in libreiser4 directory:
for d in lib{aux,misc}; do
	%make_build -C $d
done
%make_build

%install
install -d -m 0755 %buildroot/%_libdir
%makeinstall_std

pushd %buildroot
for f in ./%_lib/*.so; do
	v=$(objdump -p "$f" | sed -n '/^[[:blank:]]*SONAME[[:blank:]]/s/^.*[[:blank:]]\(lib.*$\)/\1/p')
	[ -n "$v" ] && ln -sf $(relative /%_lib/"$v" /%_prefix/"$f") "$f"
done
popd

mv %buildroot{/%_lib/*.{so,a},%_libdir/}

%files
/sbin/*
%_man8dir/*

%files -n libreiser4
/%_lib/libreiser4-%{reiser_libver}.so.*
/%_lib/librepair-%{reiser_libver}.so.*

%files -n libreiser4-devel
%_includedir/reiser4
%_includedir/repair
%_datadir/aclocal/libreiser4.m4
%_libdir/libreiser4.so
%_libdir/librepair.so

%files -n libreiser4-devel-static
%_libdir/libreiser4.a
%_libdir/librepair*.a

%if_enabled minimal
%files -n libreiser4-minimal
/%_lib/libreiser4-minimal-%{reiser_libver}.so.*

%files -n libreiser4-minimal-devel
%_libdir/libreiser4-minimal.so

%files -n libreiser4-minimal-devel-static
%_libdir/libreiser4-minimal.*a
%endif

%changelog
* Wed Nov 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1
- Updated to upstream version 1.1.0.

* Sat Aug 31 2013 Led <led@altlinux.ru> 1.0.8-alt1
- 1.0.8
- fixed format string using
- cleaned up spec
- fixed URL

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt2.1
- Removed bad RPATH

* Wed Dec 22 2010 Victor Forsiuk <force@altlinux.org> 1.0.7-alt2
- Rebuilt for soname set-versions.
- libreiser4-devel requires libaal-devel.

* Tue Mar 16 2010 Victor Forsiuk <force@altlinux.org> 1.0.7-alt1
- 1.0.7
- Fix underlinking of libreiser4.
- Built with readline.
- Move static libraries to own subpackages, also split library and utilities.
- Rename packages to be more in line with library packages naming policy.
- List of disabled features for libminimal taken from upstream readme.

* Thu Aug 17 2006 Sergey Ivanov <seriv@altlinux.org> 1.0.5-alt2
- fix bug #9885

* Fri Aug 12 2005 Sergey Ivanov <seriv@altlinux.ru> 1.0.5-alt1
- updated to version 1.0.5 from namesys.com

* Mon Feb 21 2005 Sergey Ivanov <seriv@altlinux.ru> 1.0.4-alt1
- new version from namesys with the following changes:
- A bugfix in file body convertion code.
- Enable libminimal by default.
- Do not configure empty utils(resizer, cpfs).
- Some bug fixes in tree balancing, fs check, syncing code.

* Sat Dec 11 2004 Sergey Ivanov <seriv@altlinux.ru> 1.0.3-alt1
- new version from namesys.com, includes:
- a lot of bug fixes,
- correct handling of super block backups,
- recovery according to the super block backups,
- demos/busy is a reiser4progs-busy-box program that is able
  to create/remove/copy/read/ls/etc on reiser4 working through
  libreiser4, without kernel reiser4 support. This feature is not 
  yet packed, if you need it, rpm -bc, please.

It happened that the previous super block backups were created
with a mistake and to resync them now you need to run
        fsck.reiser4 --build-sb <device>


* Wed Nov 17 2004 Sergey Ivanov <seriv@altlinux.ru> 1.0.2-alt2
- Fix [#5223] (*progs are installed into /usr/..., should into /sbin);
  *-minimal files moved to separate package, removed false g77 dependency.


* Tue Oct 26 2004 Sergey Ivanov <seriv@altlinux.ru> 1.0.2-alt1
- update to 1.0.2; descriptions, files, options taken from source's *.tar.gz

* Wed Aug 25 2004 Sergey Ivanov <seriv@altlinux.ru> 1.0.0-alt1
- initial build
