Name: nosync
Version: 1.1
Release: alt1

Summary: Preload library for disabling file's content synchronization
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/kjn/nosync

# Source-url: https://github.com/kjn/nosync/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

# Eliminate dependency on ELF constructor ordering
# Fixes segfaults during buildroot population with openssl
# https://github.com/kjn/nosync/pull/4
Patch0: 4.patch

Packager: Vitaly Lipatov <lav@altlinux.ru>

%description
nosync is a small preload library that can be used to disable
synchronization of file's content with storage devices on GNU/Linux.
It works by overriding implementations of certain standard functions
like fsync or open.

Usage:
    nosync command
or explicitly:
    LD_PRELOAD=%_libdir/nosync/nosync.so command

%prep
%setup
%patch0 -p1

%build
%make CFLAGS="%optflags"

%install
make install libdir=%buildroot%_libdir

# restore the convenience wrapper shipped by the old 0.1 package:
#   nosync <command>  runs the command with the preload library active
install -d %buildroot%_bindir
cat > %buildroot%_bindir/nosync <<EOF
#!/bin/sh
LD_PRELOAD=%_libdir/nosync/nosync.so exec "\$@"
EOF
chmod 0755 %buildroot%_bindir/nosync

%files
%doc README.md AUTHORS LICENSE NOTICE
%_bindir/nosync
%_libdir/nosync/

%changelog
* Fri Jul 17 2026 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- new version 1.1 (switch to upstream github.com/kjn/nosync)
- restore /usr/bin/nosync convenience wrapper

* Mon Jul 06 2009 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt2
- build from git, add README

* Mon Jul 06 2009 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
