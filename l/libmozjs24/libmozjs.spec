Summary:	Mozilla SpiderMonkey (JavaScript-C) Engine
Name:		libmozjs24
Version:	24.2.0
Release:	alt1
License:	MPL/GPL/LGPL
URL:		http://www.mozilla.org/js/spidermonkey/
Group:		System/Libraries
Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	%name-%version.tar
Patch0:		libmozjs-DLL_SUFFIX.patch

BuildRequires: gcc-c++ libnspr-devel libreadline-devel zip unzip
BuildRequires: libffi-devel libffi-devel-static
BuildRequires: python-module-distribute
BuildRequires: python-module-json
BuildRequires: zlib-devel

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

%patch0 -p2

%build
cd js/src

sed -i -e 's/^MOZILLA_VERSION = @MOZILLA_VERSION@/MOZILLA_VERSION = %version/' config/autoconf.mk.in

%add_optflags %optflags_shared
XCFLAGS="$XCFLAGS %optflags"
XCFLAGS="$XCFLAGS -DJS_C_STRINGS_ARE_UTF8"
SHELL=/bin/sh
export XCFLAGS SHELL

%__autoconf

%configure \
	--disable-e4x \
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

%files
%_libdir/*.so.*

%files tools
%_bindir/*

%files devel
%_includedir/*
%_pkgconfigdir/*.pc
%_libdir/*.so

%files devel-static
%_libdir/*.a

%changelog
* Sat Dec 28 2013 Alexey Gladkov <legion@altlinux.ru> 24.2.0-alt1
- New version (24.2.0).

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
