Name: build-essential
Version: 11.0
Release: alt1

Summary: Meta package to install all necessary tools for compiling software with gcc

License: GPLv2
Group: Development/Other
Url: https://bugzilla.altlinux.org/34308

BuildArch: noarch

#Requires: rpm-build

Requires: autoconf
Requires: autoconf-common
Requires: automake
Requires: automake-common
Requires: bash
Requires: binutils
Requires: bzip2
Requires: coreutils
Requires: gcc
Requires: gcc-c++
Requires: gettext-tools
Requires: glibc-devel
#Requires: gnu-config
Requires: gzip
#Requires: kernel-headers
Requires: libtool
Requires: m4
Requires: make
Requires: mktemp
Requires: patch
Requires: procps
Requires: psmisc

Requires: sed
Requires: tar
Requires: which
Requires: xz

%description
This package requires all necessary for compiling software with gcc.

This package can be used to create a basic program build environment.
Also, in most cases, it can be installed
in the same cases as the build-essential package on Debian-based systems.
Therefore, it is called exactly the same, build-essential.

If you need to create a basic environment for building packages,
install the rpm-build package.

%prep

%files

%changelog
* Fri Mar 01 2024 Vitaly Lipatov <lav@altlinux.ru> 11.0-alt1
- initial build for ALT Sisyphus (ALT bug 21608)
