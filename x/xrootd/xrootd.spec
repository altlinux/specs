Name:     xrootd
Version:  4.9.1
Release:  alt1

# Default optional switches
%def_enable fuse
%def_enable perl
%def_enable crypto
%def_enable krb5
%def_enable readline
%def_disable systemd
%def_enable libxml2
%def_enable curl

Summary:  High performance, scalable fault tolerant access to data repositories of many kinds.
License:  %lgpl3plus
Group:    Other
Url:      http://www.xrootd.org/index.html

Packager: Nikita Ermakov <arei@altlinux.org>

Source:   %name-%version.tar

BuildPreReq: rpm-build-licenses rpm-macros-cmake
BuildRequires: cmake gcc-c++ zlib-devel libjson-c-devel libuuid-devel
%{?_enable_perl:BuildRequires: rpm-build-perl perl-devel}
%{?_enable_fuse:BuildRequires: libfuse-devel}
%{?_enable_crypto:BuildRequires: libcrypt-devel libssl-devel}
%{?_enable_krb5:BuildRequires: libkrb5-devel}
%{?_enable_readline:BuildRequires: libreadline-devel}
%{?_enable_systemd:BuildRequires: libsystemd-devel}
%{?_enable_libxml2:BuildRequires: libxml2-devel}
%{?_enable_curl:BuildRequires: libcurl-devel}

# TODO: Need python macaroons include dirs
# %%{?_enable_python3:BuildRequires: python3-dev python3-module-pymacaroons-pynacl}

%description
XRootD software framework is a fully generic suite for fast, low latency and
scalable data access, which can serve natively any kind of data, organized as a
hierarchical filesystem-like namespace, based on the concept of directory.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/C++

%description devel
High performance, scalable fault tolerant access to data repositories of many kinds.
This package contains libraries and headers for developing.

%if_enabled perl
%package perl
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/C++

%description perl
High performance, scalable fault tolerant access to data repositories of many kinds.
This package contains perl utils for %name.
%endif

%prep
%setup

%build
# Option -fsigned-char is for ARM
%cmake -DCMAKE_CXX_FLAGS="-O2 -g -fsigned-char" -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%{?_disable_perl:-DENABLE_PERL=FALSE} \
%{?_disable_fuse:-DENABLE_FUSE=FALSE} \
%{?_disable_crypto:-DENABLE_CRYPTO=FALSE} \
%{?_disable_krb5:-DENABLE_KRB5=FALSE} \
%{?_disable_readline:-DENABLE_READLINE=FALSE}

%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%_libdir/libXrdAppUtils.so
%_libdir/libXrdAppUtils.so.1
%_libdir/libXrdAppUtils.so.1.0.0
%_libdir/libXrdCl.so
%_libdir/libXrdCl.so.2
%_libdir/libXrdCl.so.2.0.0
%_libdir/libXrdClient.so
%_libdir/libXrdClient.so.2
%_libdir/libXrdClient.so.2.0.0
%_libdir/libXrdCrypto.so
%_libdir/libXrdCrypto.so.1
%_libdir/libXrdCrypto.so.1.0.0
%_libdir/libXrdFfs.so
%_libdir/libXrdFfs.so.2
%_libdir/libXrdFfs.so.2.0.0
%_libdir/libXrdPosix.so
%_libdir/libXrdPosix.so.2
%_libdir/libXrdPosix.so.2.0.0
%_libdir/libXrdServer.so
%_libdir/libXrdServer.so.2
%_libdir/libXrdServer.so.2.0.0
%_libdir/libXrdUtils.so
%_libdir/libXrdUtils.so.2
%_libdir/libXrdUtils.so.2.0.0
%_libdir/libXrdXml.so
%_libdir/libXrdXml.so.2
%_libdir/libXrdXml.so.2.0.0
%_man1dir/*
%_man8dir/*

%if_enabled perl
%files perl
%_datadir/%name/utils/
%endif

%files devel
%_includedir/%name
%_libdir/libXrdBlacklistDecision-4.so
%_libdir/libXrdBwm-4.so
%_libdir/libXrdCksCalczcrc32-4.so
%_libdir/libXrdClProxyPlugin-4.so
%_libdir/libXrdCryptoLite.so
%_libdir/libXrdCryptoLite.so.1
%_libdir/libXrdCryptoLite.so.1.0.0
%_libdir/libXrdCryptossl-4.so
%_libdir/libXrdFileCache-4.so
%_libdir/libXrdHttp-4.so
%_libdir/libXrdHttpUtils.so
%_libdir/libXrdHttpUtils.so.1
%_libdir/libXrdHttpUtils.so.1.0.0
%_libdir/libXrdN2No2p-4.so
%_libdir/libXrdOssSIgpfsT-4.so
%_libdir/libXrdPosixPreload.so
%_libdir/libXrdPosixPreload.so.1
%_libdir/libXrdPosixPreload.so.1.0.0
%_libdir/libXrdPss-4.so
%_libdir/libXrdSec-4.so
%_libdir/libXrdSecProt-4.so
%_libdir/libXrdSecgsi-4.so
%_libdir/libXrdSecgsiAUTHZVO-4.so
%_libdir/libXrdSecgsiGMAPDN-4.so
%_libdir/libXrdSeckrb5-4.so
%_libdir/libXrdSecpwd-4.so
%_libdir/libXrdSecsss-4.so
%_libdir/libXrdSecunix-4.so
%_libdir/libXrdSsi-4.so
%_libdir/libXrdSsiLib.so
%_libdir/libXrdSsiLib.so.1
%_libdir/libXrdSsiLib.so.1.0.0
%_libdir/libXrdSsiLog-4.so
%_libdir/libXrdSsiShMap.so
%_libdir/libXrdSsiShMap.so.1
%_libdir/libXrdSsiShMap.so.1.0.0
%_libdir/libXrdThrottle-4.so
%_libdir/libXrdXrootd-4.so

%changelog
* Fri May 10 2019 Nikita Ermakov <arei@altlinux.org> 4.9.1-alt1
- Initial build for ALT Linux Sisyphus.
