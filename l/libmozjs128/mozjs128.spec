%def_disable snapshot
%define ver_major 128

%ifnarch %ix86 armh
%def_enable optimize
%endif
%def_with system_icu

## fc
# Big endian platforms
%ifarch ppc ppc64 s390 s390x
%def_enable big_endian
%endif


%if "%(rpmvercmp '%{get_version libicu-devel}' '6.7.1')" < "0"
%def_without system_icu
%endif

Name: libmozjs%ver_major
Version: %ver_major.1.0
Release: alt1

Summary: JavaScript interpreter and libraries
Group: System/Libraries
License: MPL-2.0 and GPL-2.0-or-later LGPL-2.1-or-later and BSD
Url: https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Releases/

%if_disabled snapshot
#Source: https://ftp.gnome.org/pub/gnome/teams/releng/tarballs-needing-help/mozjs/mozjs-%{version}.tar.xz
Source: https://ftp.gnome.org/pub/gnome/teams/releng/tarballs-needing-help/mozjs/mozjs-%{version}gnome1.tar.xz
#Source: https://ftp.mozilla.org/pub/firefox/releases/%{version}esr/source/firefox-%{version}esr.source.tar.xz
%else
Vcs: https://github.com/ptomato/mozjs.git
Source: %name-%version.tar
%endif

Patch10: mozjs128-deb-Fix-math_private.h-for-i386-FTBFS.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: /dev/shm /proc
BuildRequires: python3-devel python3(setuptools) python3(six) python3(curses)
BuildRequires: gcc-c++ nasm cbindgen
BuildRequires: libreadline-devel zip unzip
BuildRequires: libffi-devel libffi-devel-static
BuildRequires: rust-cargo >= 1.76
BuildRequires: llvm
BuildRequires: zlib-devel
%{?_with_system_icu:BuildRequires: libicu-devel}

%description
JavaScript is the Netscape-developed object scripting language used in millions
of web pages and server applications worldwide. Netscape's JavaScript is a
super set of the ECMA-262 Edition 3 (ECMAScript) standard scripting language,
with only mild differences from the published standard.

%package devel
Summary: Header files, libraries and development documentation for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
This package contains the header files, static libraries and development
documentation for %name. If you like to develop programs using %name,
you will need to install %name-devel.

%package devel-static
Summary: SpiderMonkey static libraries
Group: Development/C++
Requires: %name-devel = %EVR

%description devel-static
SpiderMonkey development kit (static libs)

%package tools
Summary: Tools for the SpiderMonkey
Group: Development/Other

%description tools
SpiderMonkey is the code-name for the Mozilla's C implementation of JavaScript.

This package provides standalone SpiderMonkey shell, a command line
interface to the JavaScript engine.

%prep
#%%setup -n firefox-%{version}esr
%setup -Dc -n mozjs-%version
%ifarch %ix86
%patch10 -p1
%endif

%build
[ ! -d _build ] && mkdir _build && \
# prepare (fix) virtualenv directory structure
mkdir -p _build/_virtualenvs/init_py3/lib/python{%__python3_version,3/site-packages}
ln -s ../python3/site-packages _build/_virtualenvs/init_py3/lib/python%__python3_version/site-packages

export srcdir="$PWD"
cd _build

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%add_optflags %optflags_shared %(getconf LFS_CFLAGS)

export CC=gcc
export CXX=g++

export AUTOCONF=%_bindir/autoconf
export CFLAGS="%optflags"
export CXXFLAGS="$CFLAGS"
export SHELL=/bin/sh
export PYTHON=%__python3

../js/src/configure \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--disable-strip \
	--disable-jemalloc \
	--enable-readline \
	--enable-shared-js \
	--disable-tests \
	%{subst_enable optimize} \
	--with-system-zlib \
	%{?_with_system_icu:--with-system-icu} \
	--with-intl-api \
	%{?optflags_lto:--enable-lto}
%nil
%if_enabled big_endian
echo "Generate big endian version of config/external/icu/data/icud67l.dat"
pushd ../..
icupkg -tb config/external/icu/data/icudt67l.dat config/external/icu/data/icudt67b.dat
rm -f config/external/icu/data/icudt*l.dat
popd
%endif

%make_build

%install
cd _build
%makeinstall_std

chmod a-x %buildroot/%_pkgconfigdir/*.pc
[ ! -f %buildroot/%_pkgconfigdir/js.pc ] ||
	mv -f -- \
		%buildroot/%_pkgconfigdir/js.pc \
		%buildroot/%_pkgconfigdir/mozjs-%ver_major.pc

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
cp -p js/src/js-config.h %buildroot/%_includedir/mozjs-%ver_major

%files
%_libdir/libmozjs-%ver_major.so*

%files devel
%_pkgconfigdir/mozjs-%ver_major.pc
%_includedir/mozjs-%ver_major/

%files tools
%_bindir/js%ver_major
%_bindir/js%ver_major-config

%files devel-static
%_libdir/*.a

%changelog
* Thu Aug 08 2024 Yuri N. Sedunov <aris@altlinux.org> 128.1.0-alt1
- first build for Sisyphus



