Name:		libmozjs24
Version:	24.2.0
Release:	alt4

Summary:	Mozilla SpiderMonkey (JavaScript-C) Engine
Group:		System/Libraries
License:	MPL/GPL/LGPL
URL:		http://www.mozilla.org/js/spidermonkey/
Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	%name-%version.tar
Patch0:		libmozjs-DLL_SUFFIX.patch
Patch1:		mozjs24-perl522.patch

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
%patch1 -p1

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
	--with-pthreads \
	--with-system-nspr \
	--with-system-zlib \
	--enable-system-ffi \
	--enable-threadsafe \
	--enable-readline \
	--enable-jemalloc

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
#ln -s mozjs-24.0.pc mozjs.pc

cd %buildroot/%_libdir
ln -s libmozjs-24.so.1.0.0 libmozjs-24.so.1.0
ln -s libmozjs-24.so.1.0 libmozjs-24.so

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
* Tue Mar 15 2016 Alexey Gladkov <legion@altlinux.ru> 24.2.0-alt4
- Fix build with Perl 5.22

* Wed Oct 28 2015 Yuri N. Sedunov <aris@altlinux.org> 24.2.0-alt3
- rebuild

* Sun Jan 26 2014 Yuri N. Sedunov <aris@altlinux.org> 24.2.0-alt2
- s/17/24/
- removed obsolete e4x configure option

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
