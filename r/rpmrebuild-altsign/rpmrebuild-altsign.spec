%define _unpackaged_files_terminate_build 1

Name: rpmrebuild-altsign
Version: 0.3.0
Release: alt1

Summary: Signer for packages using altsign (alt-signer client)
License: GPL-2.0-only
URL: https://git.altlinux.org/gears/r/rpmrebuild-altsign.git
VCS: https://git.altlinux.org/gears/r/rpmrebuild-altsign.git
Group: Development/Other
BuildArch: noarch

Source: %name-%version.tar

Requires: altsign
Requires: rpmrebuild
Requires: file
Requires: xz
Requires: zstd
Requires: gzip

%description
rpmrebuild plugins for signing PE files and kernel modules
using altsign (alt-signer client). Supports UEFI Secure Boot binaries
and compressed kernel modules (.ko, .ko.xz, .ko.zst, .ko.gz).

Two plugins are provided:
- altsign-pe.plug: for PE files (UEFI binaries, vmlinuz)
- altsign-module.plug: for kernel modules

Use ALTSIGN_PE_SESSION_SOCKET and ALTSIGN_MODULE_SESSION_SOCKET
environment variables to specify custom socket paths.

%prep
%setup

%install
mkdir -p %buildroot%_libexecdir/rpmrebuild/plugins/
install -pm644 altsign-pe.plug altsign-module.plug \
	%buildroot%_libexecdir/rpmrebuild/plugins/
install -pm755 altsign-pe-change-files.sh \
	altsign-module-change-files.sh \
	altsign-pe-change-spec.sh \
	altsign-module-change-spec.sh \
	%buildroot%_libexecdir/rpmrebuild/plugins/

%files
%doc README.md LICENSE
%_libexecdir/rpmrebuild/plugins/altsign*

%changelog
* Tue Feb 10 2026 Egor Ignatov <egori@altlinux.org> 0.3.0-alt1
- altsign-module: improve module detection, strip signatures, add dedicated
  change-spec

* Mon Feb 03 2026 Egor Ignatov <egori@altlinux.org> 0.2.0-alt1
- Rename to rpmrebuild-altsign
- Rename alt-signer-sign dependency to altsign
- Update environment variables to ALTSIGN_*
- Make session socket optional (altsign uses internal default)

* Mon Feb 02 2026 Egor Ignatov <egori@altlinux.org> 0.1.0-alt1
- First build for ALT.
