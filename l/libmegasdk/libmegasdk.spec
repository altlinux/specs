Name: libmegasdk
Version: 3.2.8
Release: alt1

Summary: MEGA SDK - Client Access Engine Coverity Scan Build Status

License: BSD 2-clause Simplified License
Group: System/Libraries
Url: https://github.com/meganz/sdk

# Source-url: https://github.com/meganz/sdk/archive/v%version.tar.gz
Source: %name-%version.tar

#Source1: %name
#Source2: %name.service
#Source3: %name.conf
#Source4: %name-serv

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Automatically added by buildreq on Mon May 25 2015
# optimized out: gnu-config libcloog-isl4 libcom_err-devel libkrb5-devel libstdc++-devel python3-base texlive-base-bin texlive-latex-base
BuildRequires: doxygen gcc5-c++ glibc-devel libcares-devel libcrypto10 libcryptopp-devel libcurl-devel libdb4-devel libfreeimage-devel libfuse-devel libreadline-devel libsqlite3-devel libssl-devel zlib-devel

%description
MEGA SDK - Client Access Engine Coverity Scan Build Status.

MEGA --- The Privacy Company --- is a Secure Cloud Storage provider
that protects your data thanks to end-to-end encryption.
We call it User Controlled Encryption, or UCE, and all our clients automatically manage it.

All files stored on MEGA are encrypted. All data transfers from and to MEGA are encrypted.
And while most cloud storage providers can and do claim the same,
MEGA is different - unlike the industry norm where the cloud storage provider holds the decryption key,
with MEGA, you control the encryption, you hold the keys, and you decide who you grant or deny access to your files.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: libmegasdk = %EVR

%description devel
This package contains the header and object files necessary for developing with
%name.

%package tools
Summary: Tools from MEGA SDK
Group: File tools
Requires: libmegasdk = %EVR

Conflicts: megafuse

%description tools
Example tools from MEGA SDK - Client Access Engine
* megacli (a powerful command line tool that allows to use all SDK features)
* megasimplesync (a command line tool that allows to use the synchronization engine)

%prep
%setup
# hack against missed --tag=CXX during linking
%__subst 's|ANDROID|TRUE|' Makefile.am

%build
%autoreconf
%configure --disable-static --with-termcap=no
%make_build

%install
%makeinstall_std

#mkdir -p %buildroot%_initdir/ %buildroot/lib/systemd/system/ %buildroot/etc/
#cp %SOURCE1 %buildroot%_initdir/
#cp %SOURCE2 %buildroot/lib/systemd/system/
#cp %SOURCE3 %buildroot/etc/
#cp %SOURCE4 %buildroot%_bindir/

%files
%_libdir/libmega.so.*
%_libdir/libmega.so.*.*

%files devel
%_includedir/mega/
%_includedir/*.h
%_libdir/pkgconfig/libmega.pc
%_libdir/libmega.so

%files tools
%_bindir/megacli
%_bindir/megafuse
%_bindir/megasimplesync

%changelog
* Fri Dec 22 2017 Vitaly Lipatov <lav@altlinux.ru> 3.2.8-alt1
- rename source package, cleanup spec
- new version (3.2.8), change packager

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1.3
- NMU: autorebuild with libcryptopp-5.6.5

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.0-alt1.2
- Updated build dependencies

* Tue Aug 18 2015 Danil Mikhailov <danil@altlinux.org> 2.5.0-alt3
- added two new packages libmegasdk and libmegasdk-devel

* Thu Aug 13 2015 Danil Mikhailov <danil@altlinux.org> 2.5.0-alt2
- fix bugs with /bin/sh in mss-serv, added $ to CONFIG var
- remove megafuse, use megafuse package

* Sat Jul 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.1
- Rebuilt with gcc5

* Mon May 25 2015 Danil Mikhailov <danil@altlinux.org> 2.5.0-alt1
- initial build for ALT Linux Sisyphus
