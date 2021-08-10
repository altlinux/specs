# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: rpm-pesign-checkinstall
Summary: Verify pesigned binaries (helper for checkinstall)
Version: 1
Release: alt1
License: GPL-2.0-only
Group: Development/Other

ExcludeArch: ppc64le
Source: %name-%version.tar

Requires: alt-uefi-certs
Requires: openssl
Requires: sbsigntools

%description
%summary.

%prep
%setup

%install
install -Dp -m755 check-pesign.sh %buildroot%_bindir/check-pesign-helper
install -Dp -m755 filetrigger     %buildroot%_rpmlibdir/check-pesign.filetrigger

%post
%_bindir/check-pesign-helper

%files
%_bindir/check-pesign-helper
%_rpmlibdir/check-pesign.filetrigger

%changelog
* Mon Aug 09 2021 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- First version.
