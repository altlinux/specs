Name: megasimplesync
Version: 2.5.0
Release: alt1.3

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
BuildRequires: cppcheck doxygen gcc5-c++ glibc-devel libcares-devel libcrypto10 libcryptopp-devel libcurl-devel libdb4-devel libfreeimage-devel libfuse-devel libreadline-devel libsqlite3-devel libssl-devel zlib-devel

%description
Megasimplesync console client for mega.co.nz

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
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
* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1.3
- NMU: autorebuild with libcryptopp-5.6.5

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.0-alt1.2
- Updated build dependencies

* Sat Jul 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.1
- Rebuilt with gcc5

* Mon May 25 2015 Danil Mikhailov <danil@altlinux.org> 2.5.0-alt1
- initial build for ALT Linux Sisyphus
