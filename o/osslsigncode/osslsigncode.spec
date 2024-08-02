%define _unpackaged_files_terminate_build 1

Name: osslsigncode
Version: 2.9
Release: alt1

Summary: Tool for Authenticode signing of EXE/CAB files
License: GPLv2+
Group: File tools
Url: https://github.com/mtrojnar/osslsigncode

Source: %name-%version.tar

Patch0: osslsigncode-2.9-alt-fix-test-server-on-python3.12.patch
Patch1: osslsigncode-2.7-alt-fix-test-python-cryptography-submodule-import.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: libssl-devel
BuildRequires: libcurl-devel
BuildRequires: libgsf-devel libgsf-gir-devel
BuildRequires: zlib-devel
BuildRequires: libfaketime
BuildRequires: cmake ctest
BuildRequires: openssl

%description
Tool for Authenticode signing of EXE/CAB files.

%prep
%setup -q

%patch0 -p1
%patch1 -p1


%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest -j1

%files
%doc COPYING.txt LICENSE.txt NEWS.md README.md
%_bindir/osslsigncode
%_datadir/bash-completion/completions/osslsigncode.bash

%changelog
* Fri Aug 02 2024 Nikolai Kostrigin <nickel@altlinux.org> 2.9-alt1
- new version
  + remove upstream-fixed-windows-segmentation-fault patch
  + update alt-fix-test-server-on-python3.12 patch 2.7 -> 2.9
  + add alt-fix-test-python-cryptography-submodule-import patch (thx egori@)

* Mon Feb 12 2024 Egor Ignatov <egori@altlinux.org> 2.7-alt1
- new version

* Fri Sep 17 2021 Nikolai Kostrigin <nickel@altlinux.org> 2.2-alt1
- new version

* Tue Nov 03 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.1-alt1
- new version

* Tue Dec 25 2018 Nikolai Kostrigin <nickel@altlinux.org> 2.0-alt1
- new version
  + switch to Michal Trojnara's fork
  + buildable against OpenSSL 1.1.x
  + remove unneeded cumulative patch

* Tue Dec 25 2018 Nikolai Kostrigin <nickel@altlinux.org> 1.7.1-alt2
- add latest features of abandoned original upstream
  + add support for pkcs11-based hardware tokens
  + improved error reporting of timestamping errors
  + buildable against OpenSSL 1.0.x

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1_2
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_5
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_2
- update to new release by fcimport

* Tue May 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_1
- moved to Sysiphus - required by mjg59, requested by mike@

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_1
- initial fc import

