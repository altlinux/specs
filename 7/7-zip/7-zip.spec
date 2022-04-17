Name: 7-zip
Version: 21.07
Release: alt1
Group: Archiving/Compression
License: LGPLv2+ with UnRAR exception
Url: https://www.7-zip.org
Source: %name-%version.tar.xz
Patch1: nostrip.patch
Summary: Official 7-zip for linux, the file archiver with a high compression ratio
Provides: 7zz = %version-%release

# Automatically added by buildreq on Fri Jul 02 2021
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libstdc++-devel python3-base sh4
BuildRequires: gcc-c++

%description
    High compression ratio in 7z format with LZMA and LZMA2 compression
    Supported formats:
        Packing / unpacking: 7z, XZ, BZIP2, GZIP, TAR, ZIP and WIM
        Unpacking only: AR, ARJ, CAB, CHM, CPIO, CramFS, DMG, EXT, FAT, GPT,
            HFS, IHEX, ISO, LZH, LZMA, MBR, MSI, NSIS, NTFS, QCOW2, RAR, RPM,
            SquashFS, UDF, UEFI, VDI, VHD, VMDK, WIM, XAR and Z.
    For ZIP and GZIP formats, 7-Zip provides a compression ratio that is
        2-10% better than the ratio provided by PKZip and WinZip
    Strong AES-256 encryption in 7z and ZIP formats
    Self-extracting capability for 7z format
    Integration with Windows Shell
    Powerful File Manager
    Powerful command line version
    Plugin for FAR Manager
    Localizations for 87 languages

%prep
%setup
%patch1 -p1

%build
cd CPP/7zip/Bundles/Alone2
%make_build -f ../../cmpl_gcc.mak \
%ifarch %e2k
	CFLAGS_WARN="-Wno-error -O%_optlevel" \
%else
	MY_LIBS="-flto=auto"
%endif
	LOCAL_FLAGS="%optflags"

%install
install -D CPP/7zip/Bundles/Alone2/b/g/7zz %buildroot%_bindir/7zz

%files
%doc DOC/*
%_bindir/*

%changelog
* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 21.07-alt1
- Autobuild version bump to 21.07

* Tue Nov 09 2021 Fr. Br. George <george@altlinux.ru> 21.04-alt1
- Manual version up
- Update patches

* Sat Jul 17 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 21.02-alt2
- added -Wno-error and restored optlevel for Elbrus
- proper passing of optflags

* Thu Jul 15 2021 Fr. Br. George <george@altlinux.ru> 21.02-alt1
- Version up

* Fri Jul 02 2021 Fr. Br. George <george@altlinux.ru> 21.01-alt1
- Initial build for ALT
