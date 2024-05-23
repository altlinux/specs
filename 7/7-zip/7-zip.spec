%def_enable profiling
%def_enable check

Name: 7-zip
Version: 24.05
Release: alt2
Group: Archiving/Compression
License: LGPLv2+ with UnRAR-exception
Url: https://www.7-zip.org
Source: %name-%version.tar.xz
Source1: check.tar
Patch2: dangling-pointer.patch
Patch3: uninitialized.patch
Patch100: ALT-armh.patch
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
        2-10 percent better than the ratio provided by PKZip and WinZip
    Strong AES-256 encryption in 7z and ZIP formats
    Self-extracting capability for 7z format
    Integration with Windows Shell
    Powerful File Manager
    Powerful command line version
    Plugin for FAR Manager
    Localizations for 87 languages

%prep
%setup -a1
%patch2 -p1
%patch3 -p1
##patch100 -p1
%ifarch %e2k
%add_optflags -msse4.1 -mno-sse4.2
%endif

sed -Ei "s@7zCon.sfx@%_libdir/7z/7zCon.sfx@" CPP/7zip/UI/Console/Main.cpp

sed -Ei '
s@7zCon.sfx@%buildroot%_libdir/7z/7zCon.sfx@g
/brotli|zstd|lz[45]|lizard|flzma2|7za433_7zip.7z|7za.exe.lz$/,/^\s*$/s/^/# NOT IN ORIGINAL 7z # /
' p7zip/check/check.sh

%build
%if_without lto
%define optflags_lto %nil
%endif

%ifarch %arm
%define optflags_lto %nil
%add_optflags -mno-unaligned-access -DZ7_DISABLE_ARM_NEON
# error: 'compressedSize' may be used uninitialized
sed -i 's/UInt64 compressedSize;/UInt64 compressedSize = 0;/' \
	CPP/7zip/Archive/Chm/ChmHandler.cpp
%endif

%ifarch %e2k
pgo_flags="-fprofile-generate-parallel"
%else
pgo_flags="-fprofile-generate -fprofile-update=atomic"
%endif

%make_build -C CPP/7zip/Bundles/Alone2 -f ../../cmpl_gcc.mak \
        DEBUG_BUILD=1 \
%if_enabled profiling
	LOCAL_FLAGS="%optflags $pgo_flags" LD_arch="$pgo_flags" \
%else
	LOCAL_FLAGS="%optflags" \
%endif
	MY_LIBS="" \
%ifarch %e2k
	CFLAGS_WARN="-Wno-error -O%_optlevel" \
%endif
	%nil

%if_enabled profiling
pushd CPP/7zip/Bundles/Alone2
# run benchmark (1 iteration, small dictionary, 1 thread, all methods)
stdbuf -o L b/g/7zz b 1 -md21 -mmt1 -mm="*"
%ifarch %e2k
eprof -d . -s eprof.sum
%endif
# clean object files
rm -f b/g/*.o
popd
# build with profile
%make_build -C CPP/7zip/Bundles/Alone2 -f ../../cmpl_gcc.mak \
        DEBUG_BUILD=1 \
	LOCAL_FLAGS="%optflags -fprofile-use" \
	MY_LIBS="" \
%ifarch %e2k
	CFLAGS_WARN="-Wno-error -O%_optlevel" \
%endif
	%nil
%endif

%make_build -C CPP/7zip/Bundles/SFXCon -f makefile.gcc \
        DEBUG_BUILD=1 \
%ifarch %e2k
	CFLAGS_WARN="-Wno-error -O%_optlevel" \
%endif
	%nil

%install
install -D CPP/7zip/Bundles/Alone2/b/g/7zz %buildroot%_bindir/7zz
install -D CPP/7zip/Bundles/SFXCon/_o/7zCon %buildroot%_libdir/7z/7zCon.sfx

%files
%doc DOC/*
%_bindir/*
%_libdir/7z

%if_enabled check
%check
cd p7zip/check
sh check.sh %buildroot%_bindir/7zz
%endif

%changelog
* Thu May 23 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 24.05-alt2
- remove obsolete patch for Elbrus

* Mon May 20 2024 Fr. Br. George <george@altlinux.org> 24.05-alt1
- Manual version bump to 24.05

* Tue Mar 05 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 23.01-alt2
- update patch for Elbrus
- compile with profiling
- fix armh build

* Sat Mar 02 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 23.01-alt1.1
- simd patch for Elbrus

* Thu Sep 28 2023 Fr. Br. George <george@altlinux.org> 23.01-alt1
- Autobuild version bump to 23.01
- Fix armh build

* Fri Sep 09 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 22.01-alt1.1
- Fixed build for Elbrus

* Wed Sep 07 2022 Fr. Br. George <george@altlinux.org> 22.01-alt1
- Manual version bump
- Introduce check section
- Introduce SFX module

* Thu Jul 07 2022 Vasiliy Tsukanov <palar@altlinux.org> 21.07-alt2
- FTBFS: description field was fixed

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
