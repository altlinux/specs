%define _unpackaged_files_terminate_build 1
%define sover 0
%define githash fda30fb

Name: sonic
Version: 0.2.0.13+b1
Release: alt4.%githash

Summary: Simple utility to speed up or slow down speech
License: Apache-2.0
Group: Sound
Url: https://github.com/espeak-ng/sonic
VCS: https://github.com/espeak-ng/sonic.git

Source: %name-%version.tar
Source1: sonic.1

Patch0: sover-fix.patch

# patches from upstream pullrequests
Patch1: 0001-Fix-downSampleBuffer-overflow-when-numChannels-1.patch
Patch2: 0002-Basic-unit-tests-and-fuzzing.patch
Patch3: 0003-Change-CC-variable-assignment-to-conditional.patch
Patch4: 0004-Add-sonic_api_test.c-to-tests-Makefile-s-TEST_SRC.patch
Patch5: 0005-Fix-signed-integer-overflow-UB-in-interpolate-s-FIR-.patch
Patch6: 0006-Fix-integer-overflow-in-insertPitchPeriod-enlargeOut.patch
Patch7: 0007-Clamp-float-samples-to-1-1-before-scaling-to-short.patch
Patch8: 0008-Basic-unit-tests-and-fuzzing.patch
Patch9: 0009-Add-GitHub-Actions-CI-and-SECURITY.md.patch
Patch10: 0010-Fix-NULL-stream-crash-and-div-by-zero-on-malformed-W.patch
Patch11: 0011-Restore-vocal-chord-emulation-linear-pitch-scaling.patch
Patch12: 0012-Fix-rate-position-desync-from-repeated-sonicSetPitch.patch
Patch13: 0013-Fix-sonicFlushStream-understating-duration-at-low-sp.patch


#BuildRequires:

%description
Sonic is a very simple utility that reads and writes wav files,
 and speeds them up or slows them down, with low distortion.
 The key new feature in Sonic versus other libraries is very
 high quality at speed up factors well over 2X.

%package -n lib%name%sover
Summary: Lib files for %name
Group: System/Libraries

%description -n lib%name%sover
%summary

%package -n lib%name-devel
Summary: Devel files fore %name
Group: Development/C++
Provides: %name-devel = %EVR

%description -n lib%name-devel
%summary

%package doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch 

%description doc
%summary

%prep
%setup
%autopatch -p1
%__subst 's|LIBDIR=\$(PREFIX)/lib|LIBDIR=%_libdir|g' Makefile

%build
%make_build

%install
%makeinstall_std

install -D -m 644 %SOURCE1 %buildroot%_man1dir/%name.1

rm %buildroot%_libdir/*.a

%check
%make_build check

%files
%_bindir/%name
%_man1dir/%name.1.xz

%files -n lib%name%sover
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.%sover.*

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/%name.h

%files doc
%doc README TODO doc/%name.odt

%changelog
* Wed Sep 30 2026 Artem Semenov <savoptik@altlinux.org> 0.2.0.13+b1-alt4.fda30fb
- Applyed patches from upstream PRs.
- Fixed segmentation fault after the sonic utility finishes running (Closes: 60628).
- Fixed abnormal termination after the sonic utility finishes running (Closes: 60629).
- Man pages moved to bin package.

* Mon Sep 14 2026 Artem Semenov <savoptik@altlinux.org> 0.2.0.13+b1-alt3.0060c87
- Packaged man pages.

* Wed Feb 11 2026 Artem Semenov <savoptik@altlinux.org> 0.2.0.13+b1-alt2
- Fixed SONAME of libsonic: now set to libsonic.so.0

* Wed Feb 11 2026 Artem Semenov <savoptik@altlinux.org> 0.2.0.13+b1-alt1
- Initial build for Sisyphus
