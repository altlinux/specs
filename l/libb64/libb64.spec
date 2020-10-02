%define shared_lib libb64.so
%define soversion 0
%define soname %shared_lib.%soversion

Name: libb64
Version: 2.0.0.1
Release: alt2

Summary: Base64 Encoding/Decoding Routines

License: Public-Domain
Group: System/Libraries
Url: https://github.com/libb64/libb64/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/libb64/libb64/archive/v%version.tar.gz
Source: %name-%version.tar

Patch4: override-cflags.diff
Patch6: disable-werror.diff
Patch20: replace-elseif-with-elif.patch
Patch21: use-stddef-h.patch
BuildRequires: gcc-c++

%description
libb64 is a library of ANSI C routines for fast encoding/decoding data into and
from a base64-encoded format. C++ wrappers are included, as well as the source
code for standalone encoding and decoding executables.

%package devel
Summary: A library for working with base64 encoding/decoding
Group: Development/C
Requires: %name = %EVR

%description devel
libb64 is a library of ANSI C routines for fast encoding/decoding data into and
from a base64-encoded format. C++ wrappers are included, as well as the source
code for standalone encoding and decoding executables.

%prep
%setup
%patch4 -p1
%patch6 -p1
%patch20 -p1
%patch21 -p1

%build
pushd src
# TODO: push to upstream
export CFLAGS="%optflags -fPIC"
%make_build
cc -shared -Wl,-soname,%soname *.o -o %soname
ln -sf %soname %shared_lib
popd

%install
# We need to use different name to avoid conflict with coreutils
#install -D -m755 base64/base64 %buildroot%_bindir/libb64-base64
install -D -m755 src/%soname %buildroot%_libdir/%soname
mkdir -p %buildroot/%_includedir
cp -r include/b64 %buildroot/%_includedir
cd %buildroot%_libdir
ln -s %soname %shared_lib

%files
%doc CHANGELOG.md README.md LICENSE.md AUTHORS.md BENCHMARKS.md
#_bindir/libb64-base64
%_libdir/%soname

%files devel
%_libdir/%shared_lib
%dir %_includedir/b64/
%_includedir/b64/*.h

%changelog
* Wed Sep 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0.1-alt2
- Fixed library for 32bit clients.

* Mon Sep 21 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.0.1-alt1
- new version (2.0.0.1) with rpmgs script
- change upstream to github repo

* Tue Sep 18 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- build on aarch64

* Thu Jan 05 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus

* Wed Jan 27 2016 Anatholy Scryabin <ascryabin@cloudlinux.com> 1.2.1-2.1
- initial build for Cloud Linux
