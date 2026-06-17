Name: cmix
Version: 21
Release: alt1
Group: Archiving/Compression
License: GPLv3
Summary: A lossless data compression program aimed at optimizing compression ratio at the cost of high CPU/memory
Source: %name-%version.tar.gz
Patch1: 0001-Use-gcc.patch
Patch2: 0002-Fix-includes.patch
Patch3: 0003-Fix-readme.patch
Patch4: 0004-GCC-15-fix.patch

# Automatically added by buildreq on Sat Feb 03 2024
# optimized out: bash5 glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libstdc++-devel python3-base sh5
BuildRequires: gcc-c++ python3
ExclusiveArch: x86_64

%description
cmix is a lossless data compression program aimed at optimizing
compression ratio at the cost of high CPU/memory usage. cmix can only
compress/decompress single files. To compress multiple files or
directories, create an archive file using "tar" (or some similar tool).

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%make_build

%install
install -D %name %buildroot%_bindir/%name
install -D remap %buildroot%_bindir/%name-remap
install -D enwik9-preproc %buildroot%_bindir/enwik9-preproc
mkdir -p %buildroot%_datadir
cp -a dictionary %buildroot%_datadir/%name

%files
%doc README*
%_bindir/*
%_datadir/%name

%changelog
* Sat Apr 25 2026 Fr. Br. George <george@altlinux.org> 21-alt1
- Autobuild version bump to 21

* Sat Feb 03 2024 Fr. Br. George <george@altlinux.org> 20-alt1
- Autobuild version bump to 20

* Sat Feb 03 2024 Fr. Br. George <george@altlinux.org> 19.1-alt1
- Initial build for ALT
