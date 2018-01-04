%define ver_major 52

%def_disable optimize
%def_with system_icu
%def_without system_nspr
%if_without system_nspr
%def_enable posix_nspr_emulation
%endif

%if "%(rpmvercmp '%{get_version libicu-devel}' '5.8.1')" < "0"
%def_disable system_icu
%endif

Name: libmozjs%ver_major
Version: %ver_major.2.1
Release: alt2

Summary: JavaScript interpreter and libraries
Group: System/Libraries
License: MPL/GPL/LGPL
Url: https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Releases/52

#Source: %name-%version.tar
Source: https://ftp.gnome.org/pub/gnome/teams/releng/tarballs-needing-help/mozjs/mozjs-52.2.1gnome1.tar.gz
#Source: https://ftp.mozilla.org/pub/firefox/releases/%{version}esr/source/firefox-%{version}esr.source.tar.xz

BuildRequires: gcc-c++ libreadline-devel zip unzip
BuildRequires: libffi-devel libffi-devel-static
BuildRequires: python-module-distribute
BuildRequires: python-module-json
BuildRequires: zlib-devel
%{?_with_system_icu:BuildRequires: libicu-devel}
%{?_with_system_nspr:BuildRequires: libnspr-devel}

BuildRequires: autoconf_2.13
%set_autoconf_version 2.13

%description
JavaScript is the Netscape-developed object scripting language used in millions
of web pages and server applications worldwide. Netscape's JavaScript is a
super set of the ECMA-262 Edition 3 (ECMAScript) standard scripting language,
with only mild differences from the published standard.

%package devel
Summary: Header files, libraries and development documentation for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains the header files, static libraries and development
documentation for %name. If you like to develop programs using %name,
you will need to install %name-devel.

%package devel-static
Summary: SpiderMonkey static libraries
Group: Development/C++
Requires: %name-devel = %version-%release

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
%setup -n mozjs-%{version}gnome1

# Correct sed expression for new sed
sed -i 's|\^\[:space:\]|^\[\[:space:\]\]|g' js/src/configure

%build
export srcdir="$PWD"
cd js/src

%add_optflags %optflags_shared

export CFLAGS="%optflags"
export CXXFLAGS="$CFLAGS -fno-tree-vrp -fno-strict-aliasing -fno-delete-null-pointer-checks"
export SHELL=/bin/sh
export PYTHON=/usr/bin/python

./configure \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--disable-strip \
	--enable-pie \
	--disable-jemalloc \
	--enable-readline \
	--enable-shared-js \
	%{?_with_system_nspr:--with-system-nspr} \
	%{?_enable_posix_nspr_emulation:--enable-posix-nspr-emulation} \
	%{subst_enable optimize} \
	--with-system-zlib \
	%{?_with_system_icu:--with-system-icu} \
	--with-intl-api
%make

%install
cd js/src
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
%_libdir/*.so

%files devel
%_pkgconfigdir/*.pc
%_includedir/*

%files tools
%_bindir/js%ver_major
%_bindir/js%ver_major-config

%files devel-static
%_libdir/*.a


%changelog
* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 52.2.1-alt2
- rebuilt with system libicu60-60.2

* Fri Aug 04 2017 Yuri N. Sedunov <aris@altlinux.org> 52.2.1-alt1
- first build for Sisyphus


