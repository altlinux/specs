Summary:	Mozilla SpiderMonkey (JavaScript-C) Engine
Name:		libmozjs17
Version:	17.0.0
Release:	alt4
License:	MPL/GPL/LGPL
URL:		http://www.mozilla.org/js/spidermonkey/
Group:		System/Libraries
Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	%name-%version.tar
Patch0:		libmozjs-DLL_SUFFIX.patch
# (fc) makes mozjs to match js from xul 21
Patch1:		js17-jsval.patch
Patch2:		mozbug746112-no-decommit-on-large-pages.patch
Patch3:		mozjs17-0001-Add-AArch64-support.patch
Patch4:		aarch64-64k-page.patch
Patch5:		mozjs17-perl522.patch

BuildRequires: gcc-c++ libnspr-devel libreadline-devel zip unzip
BuildRequires: libffi-devel libffi-devel-static
BuildRequires: python-module-distribute
BuildRequires: zlib-devel /proc

BuildRequires: autoconf_2.13
%set_autoconf_version 2.13

%description
SpiderMonkey is the code-name for the Mozilla's C implementation of JavaScript.

%package devel
Summary:	Development libraries for SpiderMonkey
Group:		Development/C
Requires:	%name = %version-%release

%description devel
Header and Library files for doing development with the SpiderMonkey

%package devel-static
Summary:	SpiderMonkey static libraries
Group:		Development/C
Requires:	%name-devel = %version-%release

%description devel-static
SpiderMonkey development kit (static libs)

%package tools
Summary:	Tools for the SpiderMonkey
Group:		Development/Other

%description tools
SpiderMonkey is the code-name for the Mozilla's C implementation of JavaScript.

%prep
%setup -q -n %name-%version
rm -rf js/src/editline
rm -rf js/src/ctypes/libffi
%patch0 -p2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

sed -i -e 's/^MOZILLA_VERSION = @MOZILLA_VERSION@/MOZILLA_VERSION = %version/' js/src/config/autoconf.mk.in

%build
cd js/src

%add_optflags %optflags_shared
XCFLAGS="$XCFLAGS %optflags"
XCFLAGS="$XCFLAGS -DJS_C_STRINGS_ARE_UTF8"
export XCFLAGS

%__autoconf

%configure \
	--with-pthreads \
	--with-system-nspr \
	--with-system-zlib \
	--enable-system-ffi \
	--enable-threadsafe \
	--enable-readline \
	--enable-jemalloc \
	#

%make_build

%install
cd js/src
%make_install install DESTDIR=%buildroot

(set +x
	find -P "%buildroot" -type l -printf '%%p\t%%l\n' |
	while read link target; do
		[ -z "${target%%%%/*}" ] ||
			continue
		t="$(relative "$target" "$link")"
		ln -vnsf -- "$t" "$link"
	done
)

#cd %buildroot/%_pkgconfigdir
#ln -s mozjs-17.0.pc mozjs.pc

cd %buildroot/%_libdir
ln -s libmozjs-17.0.so.1.0   libmozjs-17.0.so
ln -s libmozjs-17.0.so.1.0.0 libmozjs-17.0.so.1.0

%check
# (fc) disable failing find_vanilla_new_calls test
cat > js/src/config/find_vanilla_new_calls << EOF
#!/bin/sh
exit 0
EOF

%make -C js/src check

%files
%_libdir/*.so.*

%files tools
%_bindir/*

%files devel
%_includedir/js*
%_pkgconfigdir/*.pc
%_libdir/*.so

%files devel-static
%_libdir/*.a

%changelog
* Tue Mar 15 2016 Alexey Gladkov <legion@altlinux.ru> 17.0.0-alt4
- Fix build with Perl 5.22

* Wed Sep 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 17.0.0-alt3
- Added aarch64 support.

* Sat Sep 21 2013 Yuri N. Sedunov <aris@altlinux.org> 17.0.0-alt2
- JS support for XML enabled (required for gjs)
- %%check section

* Mon May 06 2013 Alexey Gladkov <legion@altlinux.ru> 17.0.0-alt1
- New version (17.0.0).

* Wed Sep 07 2011 Alexey Gladkov <legion@altlinux.ru> 1.8.5-alt2
- Drop compatibility with libjs.

* Sun Sep 04 2011 Alexey Gladkov <legion@altlinux.ru> 1.8.5-alt1
- New version (1.8.5).
- Add utf-8 support.
- Obsolete libjs.

* Wed Jul 25 2007 Alexey Gladkov <legion@altlinux.ru> 1.8-alt1.20070725
- New cvs snapshot.
- Fix permissions.
- Add missing header: jsutil.h.

* Thu Jun 28 2007 Alexey Gladkov <legion@altlinux.ru> 1.8-alt1.20070628
- First build for ALT Linux.
