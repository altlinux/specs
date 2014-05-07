Name: libmowgli2
Version: 2.0.0
Release: alt1

Summary: libmowgli is a class library containing performance and usability oriented extensions to C

License: see COPYING
Group: System/Libraries
Url: https://github.com/atheme/libmowgli-2

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/atheme/libmowgli-2
Source: %name-%version.tar

# manually removed:  python3 ruby ruby-stdlibs
# Automatically added by buildreq on Wed May 07 2014
# optimized out: gnu-config libcloog-isl4 libcom_err-devel libkrb5-devel pkg-config python3-base termutils
BuildRequires: libssl-devel

%description
mowgli is a development framework for C (like GLib), which provides
high performance and highly flexible algorithms. It can be used as a
suppliment to GLib (to add additional functions (dictionaries, hashes),
or replace some of the slow GLib list manipulation functions), or stand
alone. It also provides a powerful hook system and convenient logging
for your code, as well as a high performance block allocator.

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for %name.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%_includedir/*

%changelog
* Wed May 07 2014 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- initial build for ALT Linux Sisyphus

