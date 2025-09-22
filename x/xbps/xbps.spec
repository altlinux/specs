%def_with check

%define soversion 6

Name: xbps
Version: 0.60.5
Release: alt1

Summary: The X Binary Package System
License: BSD-2-Clause
Group: System/Base
Url: https://github.com/void-linux/xbps
Vcs: https://github.com/void-linux/xbps

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

%package -n libxbps%soversion
Summary: Library for %name
Group: System/Libraries

%description -n libxbps%soversion
XBPS Library is the base to implement a package manager frontend, such as
is implemented in the xbps command line interfaces.

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
rm -rv %buildroot%_datadir/licenses/%name

%check
# Tests failed in hasher
sed -i '/\tatf_add_test_case reproducible/d' tests/xbps/xbps-install/behaviour_tests.sh
sed -i '/\tatf_add_test_case clean_cache/d' tests/xbps/xbps-remove/basic_test.sh
sed -i '/\tatf_add_test_case clean_cache_dry_run/d' tests/xbps/xbps-remove/basic_test.sh
sed -i '/\tatf_add_test_case clean_cache_dry_run_perm/d' tests/xbps/xbps-remove/basic_test.sh
sed -i '/\tatf_add_test_case empty_string/d' tests/xbps/xbps-digest/basic_test.sh
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
%_man1dir/%name-uhelper.1.xz
%_man1dir/%name-uunshare.1.xz
%_man5dir/%name.d.5.xz
%_man7dir/%name.7.xz
%_datadir/xbps.d
%_datadir/bash-completion/completions/%{name}*
%_datadir/zsh/site-functions/_%{name}*
%_localstatedir/%name

%files -n libxbps%soversion
%_libdir/libxbps.so.%{soversion}*

%files devel
%_libdir/libxbps.so
%_libdir/pkgconfig/*.pc
%_includedir/%name
%_includedir/%name.h

%changelog
* Tue Sep 09 2025 Ulysses Apokin <ulysses@altlinux.org> 0.60.5-alt1
- New version.
- libxbps is packaged separately according to shared libs policy.

* Tue Mar 11 2025 Ulysses Apokin <ulysses@altlinux.org> 0.59.2-alt1
- Initial build for Sisyphus.
