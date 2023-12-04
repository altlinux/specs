%define git %nil

Name: libopus
Version: 1.4
Release: alt1.2

Summary: Opus Audio Codec library
License: BSD
Group: System/Libraries
Url: http://opus-codec.org/
# http://downloads.xiph.org/releases/opus/%name-%version.tar.gz
Source: opus-%version.tar
Patch: libopus-silk-fix-missing-have_arm_intrinsics_or_asm.patch

BuildRequires(pre): meson, cmake

%def_disable static
%def_enable doc

%description
The Opus codec is designed for interactive speech and audio transmission
over the Internet. It is designed by the IETF Codec Working Group and
incorporates technology from Skype's SILK codec and Xiph.Org's CELT codec.

%package devel
Summary: Development files for libopus
Group: Development/C
PreReq: %name = %version-%release
%if_enabled doc
BuildRequires: doxygen, graphviz, fonts-ttf-dejavu
%endif

%description devel
This package contains the header files and documentation needed
to develop applications with libopus.

%package devel-static
Summary: Static libraries for libopus
Group: Development/C
PreReq: %name-devel = %version-%release

%description devel-static
This package contains development libraries required for packaging
statically linked libopus-based software.

%prep
%setup -n opus-%version
%patch -p2

%build
printf 'PACKAGE_VERSION="%s"\n' '%version' > package_version
%meson -Dintrinsics=auto \
       -Dcheck-asm=true \
       -Dcustom-modes=true \
%ifarch x86_64
       -Drtcd=disabled
%endif
%meson_build

%install
%meson_install

%check
%__meson_test -t 1000

%files
%_libdir/*.so.*
%doc AUTHORS README COPYING LICENSE_PLEASE_READ.txt

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%if_enabled doc
%dir %_docdir/opus/
%_docdir/opus/*
%endif

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Mon Dec 04 2023 Ivan A. Melnikov <iv@altlinux.org> 1.4-alt1.2
- NMU: add with_doc knob to simplify bootstrap (asheplyakov@)

* Mon Nov 27 2023 L.A. Kostis <lakostis@altlinux.ru> 1.4-alt1.1
- enable custom modes (closes #48590).

* Fri Apr 28 2023 L.A. Kostis <lakostis@altlinux.ru> 1.4-alt1
- 1.4.

* Mon Oct 03 2022 Ivan A. Melnikov <iv@altlinux.org> 1.3.1-alt158.gbce1f392.1
- increase tests timeout to enable %%check on armh, mipsel and riscv64

* Mon Sep 26 2022 L.A. Kostis <lakostis@altlinux.ru> 1.3.1-alt158.gbce1f392
- v1.3.1-158-gbce1f392.
- switch to meson.
- build/meson: fix missing have_arm_intrinsics_or_asm variable.
- don't run tests on armh due timeouts.

* Wed Mar 18 2020 Oleg Solovyov <mcpain@altlinux.org> 1.3.1-alt3
- remove git garbage from opus.pc (Closes: 38210)

* Thu Mar 12 2020 Oleg Solovyov <mcpain@altlinux.org> 1.3.1-alt2
- fix unknown version in opus.pc (Closes: 38210)

* Sun Mar 08 2020 L.A. Kostis <lakostis@altlinux.ru> 1.3.1-alt1
- 1.3.1.

* Tue Sep 05 2017 L.A. Kostis <lakostis@altlinux.ru> 1.2.1-alt1.1
- disable run-time cpu detection only on x86_64.

* Tue Sep 05 2017 L.A. Kostis <lakostis@altlinux.ru> 1.2.1-alt1
- 1.2.1.
- enable checks.
- enable check-asm (to test correctness for asm optimisation).
- enable experimental Ambisonics support.

* Mon Jun 06 2016 L.A. Kostis <lakostis@altlinux.ru> 1.1.2-alt1
- 1.1.2 (closes #31585).
- enabled intrinsics asm optimizations.

* Thu Jul 16 2015 Anton Farygin <rider@altlinux.ru> 1.1-alt1
- 1.1

* Wed Mar 04 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sat Mar 02 2013 L.A. Kostis <lakostis@altlinux.ru> 1.0.2-alt1
- 1.0.2 (closes #28622).

* Sat Aug 25 2012 L.A. Kostis <lakostis@altlinux.ru> 1.0.1-alt0.1.rc2
- 1.0.1rc2.

* Mon Jul 23 2012 L.A. Kostis <lakostis@altlinux.ru> 0.9.14-alt1
- Updated to 0.9.14;
- initial build for ALTLinux.

