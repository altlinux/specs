%define oname aften

Name: libaften
Version: 0.0.8
Release: alt4
Epoch: 1

Summary: Aften: A/52 audio encoder
License: LGPLv2+
Group: System/Libraries

Url: http://%oname.sourceforge.net/
Source: http://dl.sourceforge.net/%oname/%oname-%version.tar.bz2
Patch2000: %name-e2k-simd.patch
Patch3500: %name-nosimd-arches.patch
Packager: Vitaly Lipatov <lav@altlinux.ru>

ExcludeArch: ppc64le

# Automatically added by buildreq on Thu Aug 02 2007
BuildRequires: cmake yasm

%description
A simple AC3-compatible audio encoder based on FFmpeg.

%package devel
Summary: Header files for %name library
Group: Development/C++
Requires: %name = %{?serial:%serial:}%version-%release

%description devel
Header files for %name library.

%prep
%setup -n %oname-%version
%ifarch %e2k
%patch2000 -p1
%endif
%patch3500 -p1

%build
mkdir -p default && cd default
cmake .. -DCMAKE_INSTALL_PREFIX:STRING="%_usr" -DSHARED=yes
%make_build

%install
cd default
%makeinstall_std
# hack due to broken install target in CMakeList
test -d %buildroot%_libdir || mv %buildroot%_prefix/lib %buildroot%_libdir

%files
%_bindir/*
%doc README
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/*

%changelog
* Wed Dec 06 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:0.0.8-alt4
- NMU: fixed FTBFS on non-x86 architectures (except ppc64).
  While at it wiped out extraneous build requirements.

* Tue Jun 08 2021 Michael Shigorin <mike@altlinux.org> 1:0.0.8-alt3
- built for sisyphus (with minor spec cleanup)

* Tue Jun 08 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1:0.0.8-alt2
- added SIMD patch for Elbrus

* Thu Aug 30 2012 Repocop Q. A. Robot <repocop@altlinux.org> 1:0.0.8-alt1.qa3
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for libaften

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 1:0.0.8-alt1.qa2
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1:0.0.8-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libaften
  * postun_ldconfig for libaften
  * postclean-05-filetriggers for spec file

* Thu Sep 20 2007 Vitaly Lipatov <lav@altlinux.ru> 1:0.0.8-alt1
- new version 0.0.8 (with rpmrb script)
- add Serial:1 due version format change

* Fri Aug 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt2
- use yasm instead nasm
- fix build on x86_64

* Thu Aug 02 2007 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt1
- initial build for ALT Linux Sisyphus

