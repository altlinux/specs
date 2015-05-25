Name: megasimplesync
Version: 2.5.0
Release: alt1

Summary: Megasimplesync console client for mega.co.nz

License: LGPL
Group: Office
Url: https://github.com/meganz/sdk

Source: %name-%version.tar
Source2: megasimplesync
Source4: megasimplesync.service

Packager: Danil Mikhailov <danil@altlinux.org>

#doxygen gcc-c++ glibc-devel libcares-devel libcrypto7 libcryptopp-devel libcurl-devel libdb4-devel libfreeimage-devel libfuse-devel libreadline-devel libsqlite3-devel libssl-devel. zlib-devel
# Automatically added by buildreq on Mon May 25 2015
# optimized out: gnu-config libcloog-isl4 libcom_err-devel libkrb5-devel libstdc++-devel python3-base texlive-base-bin texlive-latex-base
BuildRequires: cppcheck doxygen gcc4.9-c++ glibc-devel libcares-devel libcrypto7 libcryptopp-devel libcurl-devel libdb4-devel libfreeimage-devel libfuse-devel libreadline-devel libsqlite3-devel libssl-devel zlib-devel

%description
Megasimplesync console client for mega.co.nz

%prep
%setup

%build
sh autogen.sh
%configure --with-termcap=no
%make_build

%install
%makeinstall_std

rm -rf %buildroot%_includedir/
rm -rf %buildroot/%_libdir/pkgconfig/
rm -f %buildroot/%_libdir/libmega.so

%check

%pre
%files
%_bindir/*
%_libdir/libmega.so.500
%_libdir/libmega.so.500.0.0

%changelog
* Mon May 25 2015 Danil Mikhailov <danil@altlinux.org> 2.5.0-alt1
- initial build for ALT Linux Sisyphus
