# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: rpm-pesign-checkinstall
Summary: Verify pesigned binaries (helper for checkinstall)
Version: 2
Release: alt1
License: GPL-2.0-only
Group: Development/Other

Source: %name-%version.tar

Requires: alt-uefi-certs
Requires: openssl
%ifnarch ppc64le
Requires: sbsigntools
%endif

%description
%summary.

%prep
%setup

%install
install -Dp -m755 check-pesign.sh %buildroot%_bindir/check-pesign-helper
%ifarch x86_64
  install -Dp -m755 filetrigger   %buildroot%_rpmlibdir/check-pesign.filetrigger
%endif

%post
%ifarch x86_64
%_bindir/check-pesign-helper
%endif

%files
%_bindir/check-pesign-helper
%ifarch x86_64
%_rpmlibdir/check-pesign.filetrigger
%endif

%changelog
* Wed Aug 11 2021 Vitaly Chikunov <vt@altlinux.org> 2-alt1
- Force check for the files specified in command line.
- Make package multiarch.

* Mon Aug 09 2021 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- First version.
