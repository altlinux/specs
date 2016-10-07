%define oname 7z

Name: fuse-7z
Version: 0.2
Release: alt3

Summary: A FUSE filesystem that uses the 7-zip library to interacts with all kind of archives

Group: System/Kernel and hardware
License: GPL v3
Url: https://github.com/exmakhina/fuse-7z

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/exmakhina/fuse-7z.git
Source: %name-%version.tar
Patch: fuse-7z-0.1-alt-link.patch

Requires: %{get_dep fuse}

# we use /usr/lib64/p7zip/7z.so from it
Requires: p7zip

# manually removed: rpm-build-java rpm-build-mono rpm-build-seamonkey rpm-macros-fillup xorg-sdk  python-module-mwlib python-module-paste
# Automatically added by buildreq on Fri Aug 17 2012
# optimized out: libstdc++-devel pkg-config python-base python-module-distribute python-module-peak python-module-zope python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging
BuildRequires: gcc-c++ libfuse-devel waf

%description
A FUSE filesystem that uses the 7-zip library to interacts with all kind
of archives, and in particular the .7z files.

Only reads are supported at the moment, and this is a work in progress (started 2011-09-05).

Contributions are welcome.

%prep
%setup
# TODO: fix in upstream
#patch -p1

%build
waf configure
waf

cat <<EOF >wrapper/fuse-7z
#!/bin/sh
LD_LIBRARY_PATH=%_libdir/p7zip exec %_libexecdir/%name/fuse-7z "\$@"
EOF

%install
install -D build/fuse-7z %buildroot%_libexecdir/%name/fuse-7z
install -D wrapper/fuse-7z %buildroot%_bindir/fuse-7z
#exeinto /usr/libexec/fuse-7z
#doexe build/fuse-7z

%files
%doc README
%_bindir/fuse-7z
%_libexecdir/%name/

%changelog
* Fri Oct 07 2016 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt3
- update Url, fix shell wrapper (against speces in name)

* Mon Sep 22 2014 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt2
- fast hack for fix wchar_t to utf8 convert

* Mon Sep 22 2014 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- build new version, fix build

* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.1
- Completed linking

* Fri Aug 17 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
