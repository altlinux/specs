%ifndef x86_64
%define x86_64 x86_64
%endif

Name: rpm-build-xen
Version: 4.4.0
Release: alt3
Summary: Arch-specific requirement to build XEN
License: GPLv3+
Group: Development/Other
ExclusiveArch: %ix86 %x86_64 armh aarch64

%ifarch %x86_64 %ix86
%def_enable stubdom
%else
%def_disable stubdom
%endif
%ifarch %x86_64
%def_with efi
%else
%def_without efi
%endif
%ifarch %ix86
%def_without hypervisor
%def_without xsm
%else
%def_with hypervisor
%def_with xsm
%endif

%ifarch %x86_64 %ix86
Requires: dev86
%endif
%ifarch %x86_64
Requires: %_includedir/gnu/stubs-32.h
%endif
%{?_with_xsm:Requires: checkpolicy m4}
%{?_with_efi:Requires: rpm-build-uefi mingw64-binutils}
%{?_enable_stubdom:Requires: makeinfo libSDL-devel libXext-devel}
%{?_with_hypervisor:Requires: flex libfdt-devel libgcrypt-devel liblzo2-devel perl-HTML-Parser}

%description
Arch-specific requirement to build XEN.


%files


%changelog
* Sat Apr 16 2022 Igor Vlasenko <viy@altlinux.org> 4.4.0-alt3
- NMU: use rpm-build-uefi instead of rpm-macros-uefi

* Thu Sep 13 2018 Alexey Shabalin <shaba@altlinux.org> 4.4.0-alt2
- drop libvde-devel from Requires

* Tue Apr 15 2014 Led <led@altlinux.ru> 4.4.0-alt1
- added requires rpm-macros-uefi

* Fri Feb 14 2014 Led <led@altlinux.ru> 4.3.1-alt1
- initial, for build XEN 4.3.1
