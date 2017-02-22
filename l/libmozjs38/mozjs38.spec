Summary:	JavaScript interpreter and libraries
Name:		libmozjs38
Version:	38.2.1
Release:	alt2
Group:		System/Libraries
License:	MPL/GPL/LGPL
Packager:	Alexey Gladkov <legion@altlinux.ru>
URL:		https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Releases/38
Source0:	%name-%version.tar

BuildRequires: gcc-c++ libnspr-devel libreadline-devel zip unzip
BuildRequires: libffi-devel libffi-devel-static
BuildRequires: libicu-devel
BuildRequires: python-module-distribute
BuildRequires: python-module-json
BuildRequires: zlib-devel

BuildRequires: autoconf_2.13
%set_autoconf_version 2.13

%description
JavaScript is the Netscape-developed object scripting language used in millions
of web pages and server applications worldwide. Netscape's JavaScript is a
super set of the ECMA-262 Edition 3 (ECMAScript) standard scripting language,
with only mild differences from the published standard.

%package devel
Summary: Header files, libraries and development documentation for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the header files, static libraries and development
documentation for %name. If you like to develop programs using %name,
you will need to install %name-devel.

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
%setup -q

%build
export srcdir="$PWD"
cd js/src

%add_optflags %optflags_shared

# Need -fpermissive due to some macros using nullptr as bool false
export CFLAGS="%optflags"
export CXXFLAGS="$CFLAGS -fpermissive"
export SHELL=/bin/sh
export PYTHON=/usr/bin/python

%configure \
	--with-system-nspr \
	--enable-threadsafe \
	--enable-readline \
	--enable-xterm-updates \
	--enable-shared-js \
	--enable-gcgenerational \
	--enable-optimize \
	--with-system-zlib \
	--enable-system-ffi \
	--with-system-icu \
	--with-intl-api

%make -j1

%install
cd js/src
%make_install install DESTDIR=%buildroot

chmod a-x %buildroot/%_pkgconfigdir/*.pc
[ ! -f %buildroot/%_pkgconfigdir/js.pc ] ||
	mv -f -- \
		%buildroot/%_pkgconfigdir/js.pc \
		%buildroot/%_pkgconfigdir/mozjs-38.pc

(set -x
	for f in %buildroot/%_libdir/*.ajs; do
		mv -vf -- "$f" "${f%%js}"
	done
)
# Install files, not symlinks to build directory
(set +x
	find -P "%buildroot/%_includedir" -type l -printf '%%p\n' |
	while read link; do
		t="$(readlink -ev "$link")"
		rm -f -- "$link"
		cp -f -- "$t" "$link"
	done
)
cp -p js/src/js-config.h %buildroot/%_includedir/mozjs-38

%files
%_libdir/*.so

%files tools
%_bindir/*

%files devel
%_pkgconfigdir/*.pc
%_includedir/*

%files devel-static
%_libdir/*.a

%changelog
* Wed Feb 22 2017 Alexey Gladkov <legion@altlinux.ru> 38.2.1-alt2
- Rebuilt with Internationalization API.

* Wed Feb 15 2017 Alexey Gladkov <legion@altlinux.ru> 38.2.1-alt1
- First build for ALTLinux.

* Thu Dec 15 2016 Alexey Gladkov <legion@altlinux.ru> 31.2.0-alt1
- First build for ALTLinux.

* Fri May 20 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 31.2.0-8
- Correct arm hard fp build

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 31.2.0-7
- rebuild for ICU 57.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 31.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 31.2.0-5
- rebuild for ICU 56.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 31.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 31.2.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 15 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 31.2.0-2
- Update licenses
- Remove INSTALL from devel package

* Sat Mar 14 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 31.2.0-1
- Initial mozjs31 spec.
