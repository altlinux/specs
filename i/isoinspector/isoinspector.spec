%define _unpackaged_files_terminate_build 1

Name: isoinspector
Version: 0.2.3
Release: alt1

Summary: Tool that inspect ALT Linux distribution ISO/IMG images using ALTRepo API
License: GPL-3.0
Group: Development/Tools
URL: https://git.altlinux.org/gears/i/isoinspector.git

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

Requires: xz
Requires: fuseiso
Requires: squashfuse
Requires: libguestfs
Requires: guestfs-data
Requires: qemu-img
Requires: qemu-kvm

Source0: %name-%version.tar
Patch1: %name-%version-%release.patch

%description
Isoinspector is an utility to validate consistency of RPM packages from
distribution ISO/IMG image with base branch state in ALTRepo DB using ALTRepo API.

%prep
%setup
%autopatch -p1

%build
#pass

%install
install -Dm0755 isoinspector %buildroot%_bindir/isoinspector

%files
%_bindir/isoinspector
%doc LICENSE README.* AUTHORS.txt

%changelog
* Thu Feb 12 2026 Danil Shein <dshein@altlinux.org> 0.2.3-alt1
- new version
  + add missing runtime dependencies on Qemu

* Thu Jan 29 2026 Danil Shein <dshein@altlinux.org> 0.2.2-alt1
- new version 0.2.2
  + fix image type detection (closes: #57704)

* Thu Jan 22 2026 Danil Shein <dshein@altlinux.org> 0.2.1-alt1
- new version 0.2.1
  + add support for compressed and uncompressed IMG images

* Mon May 22 2023 Danil Shein <dshein@altlinux.org> 0.1.2-alt1
- new version 0.1.2

* Tue Sep 13 2022 Danil Shein <dshein@altlinux.org> 0.1.1-alt1
- new version 0.1.1

* Fri Feb 11 2022 Danil Shein <dshein@altlinux.org> 0.1.0-alt2
- clear spec file

* Fri Feb 11 2022 Danil Shein <dshein@altlinux.org> 0.1.0-alt1
- Initial build
