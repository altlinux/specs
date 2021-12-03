%define _unpackaged_files_terminate_build 1                                                   
  
%set_verify_elf_method skip
%set_debuginfo_skiplist /*
%set_fixup_skiplist /*

Name: librtpam
Version: 1.0.0
Release: alt1
Summary: PAM module for authentication by Rutoken tokens
Vendor: Aktiv Co.
License: distributable
Group: System/Libraries
URL: https://download.rutoken.ru/Rutoken/PAM

Source0: %name-%version.tar

ExclusiveArch: %ix86 x86_64 mipsel aarch64 armh

%description
%{summary}.

%prep
%setup

%install
%ifarch %ix86
install -Dpm0644 x86/librtpam.so.1.0.0 %buildroot/%_lib/security/librtpam.so
%endif

%ifarch x86_64
install -Dpm0644 x86_64/librtpam.so.1.0.0 %buildroot/%_lib/security/librtpam.so
%endif

%ifarch mipsel
install -Dpm0644 mipsn64el/librtpam.so.1.0.0 %buildroot/%_lib/security/librtpam.so
%endif

%ifarch aarch64
install -Dpm0644 arm64/librtpam.so.1.0.0 %buildroot/%_lib/security/librtpam.so
%endif

%ifarch armh
install -Dpm0644 armv7hf/librtpam.so.1.0.0 %buildroot/%_lib/security/librtpam.so
%endif

%files
/%_lib/security/*.so

%changelog
* Fri Dec 03 2021 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
