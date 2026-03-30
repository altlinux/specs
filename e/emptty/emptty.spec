%define _unpackaged_files_terminate_build 1
%def_with check

Name: emptty
Version: 0.16.1
Release: alt1

Summary: Dead simple CLI Display Manager on TTY
License: MIT
Group: Graphical desktop/Other
VCS: https://github.com/tvrzna/emptty
Url: https://github.com/tvrzna/emptty

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: libpam-devel
BuildRequires: libX11-devel

%description
Dead simple CLI Display Manager on TTY.

%prep
%setup -a1
%patch -p1

%build
export BUILD_VERSION="v%version-%release"
%make_build build

%install
%makeinstall_std install install-manual install-pam-alt install-config install-systemd

%check
%make test

%files
%doc LICENSE README.md SAMPLES.md
%_bindir/emptty
%_unitdir/emptty.service
%dir %_sysconfdir/emptty
%config(noreplace) %_sysconfdir/emptty/conf
%config(noreplace) %_sysconfdir/pam.d/emptty
%_man1dir/emptty.1.*

%changelog
* Mon Mar 30 2026 Egor Ignatov <egori@altlinux.org> 0.16.1-alt1
- New version 0.16.1.

* Sun Dec 07 2025 Egor Ignatov <egori@altlinux.org> 0.15.0-alt1
- New version 0.15.0.

* Sun Jun 08 2025 Egor Ignatov <egori@altlinux.org> 0.14.0-alt1
- First build for ALT.
