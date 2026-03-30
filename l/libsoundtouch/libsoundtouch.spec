%def_disable snapshot
%define __name SoundTouch
%define _name soundtouch
# soname bumped for CMake build
%define sover 2
%define binary_name soundstretch

%def_enable openmp
%def_disable dll
%def_enable check

Name: libsoundtouch
Version: 2.4.1
Release: alt1

Summary: SoundTouch audio processing library
License: LGPL-2.1-or-later
Group: System/Libraries
Url: http://www.surina.net/soundtouch/

Vcs: https://codeberg.org/soundtouch/soundtouch.git

%if_disabled snapshot
Source: %url/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ libstdc++-devel
%{?_enable_openmp:BuildRequires: libgomp-devel}
%{?_enable_check:BuildRequires: ctest}

%description
SoundTouch is an open-source audio processing library that allows changing
the sound tempo, pitch and playback rate parameters independently from
each other, i.e.:
 - Sound tempo can be increased or decreased while maintaining the original pitch
 - Sound pitch can be increased or decreased while maintaining the original tempo
 - Change playback rate that affects both tempo and pi

%package devel
Summary: Libraries/include files for development with %name
Group: Development/C
Requires: %name = %EVR

%description devel
Libraries/include files for development with %name.

%package -n %binary_name
Summary: soundstretch - audio processing CLI program
Group: Sound
Requires: %name = %EVR

%description -n %binary_name
This package provides utility from SoundTouch package.

%binary_name processes WAV audio files by modifying the sound tempo
pitch and playback rate properties independently from each other.

%prep
%setup -n %_name%{?_enable_snapshot:-%version}
%if_enabled openmp
%ifarch %e2k
# for unknown reason, libtool uses the -nostdlib option when linking,
# and -fopenmp is ignored in this case 
echo "libSoundTouch_la_LDFLAGS+=-lomp" >> source/SoundTouch/Makefile.am
%endif
%endif

%build
%ifarch %ix86
%add_optflags -msse2
%endif
%cmake \
    -DBUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
    %{?_enable_dll:-DSOUNDTOUCH_DLL=ON} \
    %{?_enable_openmp:-DOPENMP=ON} \
%nil
%cmake_build

%install
%cmake_install

# for multispeech and freeswitch
install -pD -m644 %_name.m4 -t %buildroot%_aclocaldir/

rm -rf %buildroot/%_prefix/doc

%check
%ctest

%files
%_libdir/lib%__name.so.%{sover}*
%{?_enable_dll:%_libdir/lib%{__name}DLL.so}
%doc README.*

%files devel
%_includedir/%_name/
%_libdir/lib%__name.so
%_libdir/cmake/%__name/
%_aclocaldir/%_name.m4
%_pkgconfigdir/%_name.pc

%files -n %binary_name
%_bindir/%binary_name

%changelog
* Mon Mar 30 2026 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Mon Jan 26 2026 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt2
- switched build to CMake (ALT #57653)

* Mon Apr 07 2025 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Sat Mar 30 2024 Yuri N. Sedunov <aris@altlinux.org> 2.3.3-alt1
- 2.3.3

* Sun Jan 29 2023 Yuri N. Sedunov <aris@altlinux.org> 2.3.2-alt1
- 2.3.2
- disabled -ffast-math (Suse)

* Thu Mar 10 2022 Michael Shigorin <mike@altlinux.org> 2.3.1-alt2
- E2K: openmp build fix by ilyakurdyukov@

* Tue Sep 07 2021 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Sun Aug 22 2021 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0
- enabled OpenMP support

* Tue Oct 27 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2-alt1
- 2.2

* Wed Dec 05 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1.2-alt1
- updated to 2.1.2-2-g2b2585b

* Thu Nov 22 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1 (fixed CVE-2018-17097)

* Sun Sep 23 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Wed Aug 02 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Fri Feb 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.9.2-alt1
- 1.9.2

* Tue Nov 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0
- removed obsolete patches

* Sat Aug 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt2.qa2
- Rebuilt for debuginfo

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Mon Dec 15 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt2
- fix build with gcc 4.3

* Thu Dec 07 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- correct version (download 1.3.1 from surina.net)
- use native soundtouch-1.0.pc (fix bug #10366, thanks eostapets@)

* Tue Jun 06 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt0.3
- add libSoundTouch.pc (fix bug #9677). Thanks, Debian.

* Mon May 29 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt0.2
- fixes for as-needed

* Mon Feb 06 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt0.1
- initial build for ALT Linux Sisyphus
- build without asm optimization
