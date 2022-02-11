%define _unpackaged_files_terminate_build 1

Name: isoinspector
Version: 0.1.0
Release: alt2

Summary: Tool that inspect ALT Linux distribution ISO using ALTRepo API
License: GPL-3.0
Group: Development/Tools
URL: https://git.altlinux.org/gears/i/isoinspector.git

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

Requires: fuseiso
Requires: squashfuse

Source0: %name-%version.tar
Patch1: %name-%version-%release.patch

%description
Isoinspector is an utility to validate consistency of RPM packages from
distribution ISO image with base branch in ALTRepo DB using ALTRepo API.

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
* Fri Feb 11 2022 Danil Shein <dshein@altlinux.org> 0.1.0-alt2
- clear spec file

* Fri Feb 11 2022 Danil Shein <dshein@altlinux.org> 0.1.0-alt1
- Initial build


