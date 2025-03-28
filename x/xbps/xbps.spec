%def_with check

Name: xbps
Version: 0.59.2
Release: alt1

Summary: The X Binary Package System
License: BSD-2-Clause
Group: System/Base
Url: https://github.com/voidlinux/xbps
Vcs: https://github.com/voidlinux/xbps

Source: %name-%version.tar

BuildRequires: openssl-devel
BuildRequires: zlib-devel
BuildRequires: libarchive-devel

%if_with check
BuildRequires: atf-tests kyua
%endif

%description
The X Binary Package System (in short XBPS) is a new binary package system
designed and implemented from scratch. Its goal is to be fast, easy to use,
bug-free, featureful and portable as much as possible.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
Header files and libraries for the package %name.

%prep
%setup

%build
# Not GNU Autotools
%configure \
	--dbdir=%_localstatedir/%name/db \
	--enable-tests
sed -i '/CFLAGS +=\t-Werror/d' config.mk
%make_build

%install
%makeinstall_std
rm -v %buildroot%_libdir/lib%name.a
rm -rv %buildroot%prefix/tests

%check
# Passed test in hasher
sed -i '/\tatf_add_test_case reproducible/d' tests/xbps/xbps-install/behaviour_tests.sh

%make_build check

%files
%doc TODO README.md NEWS LICENSE* 3RDPARTY
%_bindir/%name-alternatives
%_bindir/%name-checkvers
%_bindir/%name-create
%_bindir/%name-dgraph
%_bindir/%name-digest
%_bindir/%name-fbulk
%_bindir/%name-fetch
%_bindir/%name-install
%_bindir/%name-pkgdb
%_bindir/%name-query
%_bindir/%name-reconfigure
%_bindir/%name-remove
%_bindir/%name-rindex
%_bindir/%name-uchroot
%_bindir/%name-uhelper
%_bindir/%name-uunshare
%_libdir/lib%name.so.*
%_man1dir/%name-alternatives.1.xz
%_man1dir/%name-checkvers.1.xz
%_man1dir/%name-create.1.xz
%_man1dir/%name-dgraph.1.xz
%_man1dir/%name-digest.1.xz
%_man1dir/%name-fbulk.1.xz
%_man1dir/%name-fetch.1.xz
%_man1dir/%name-install.1.xz
%_man1dir/%name-pkgdb.1.xz
%_man1dir/%name-query.1.xz
%_man1dir/%name-reconfigure.1.xz
%_man1dir/%name-remove.1.xz
%_man1dir/%name-rindex.1.xz
%_man1dir/%name-uchroot.1.xz
%_man1dir/%name-uunshare.1.xz
%_man5dir/%name.d.5.xz
%_datadir/xbps.d
%_datadir/bash-completion/completions/%{name}*
%_datadir/zsh/site-functions/_%{name}*
%_localstatedir/%name/db/keys/*

%files devel
%_libdir/lib%name.so
%_libdir/pkgconfig/*.pc
%_includedir/%name/*.h
%_includedir/%name.h

%changelog
* Tue Mar 11 2025 Ulysses Apokin <ulysses@altlinux.org> 0.59.2-alt1
- Initial build for Sisyphus.
