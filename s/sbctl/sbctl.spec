%define _unpackaged_files_terminate_build 1
%def_with check

Name: sbctl
Version: 0.18
Release: alt1

Summary: Secure Boot key manager
License: MIT
Group: System/Configuration/Boot and Init
VCS: https://github.com/Foxboron/sbctl
Url: https://github.com/Foxboron/sbctl

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang
BuildRequires(pre): rpm-macros-systemd

BuildRequires: asciidoc-a2x
BuildRequires: libpcsclite-devel

%description
sbctl intends to be a user-friendly secure boot key manager capable of
setting up secure boot, offer key management capabilities, and keep
track of files that needs to be signed in the boot chain.

%prep
%setup -a1
%patch0 -p1

%build
echo '%version-%release' > VERSION
%make_build

%install
%makeinstall_std PREFIX=%prefix
rm %buildroot%_datadir/licenses/sbctl/LICENSE

%check
%gotest

%files
%doc README.md LICENSE
%_bindir/sbctl
%_kernel_installdir/91-sbctl.install
%_libexecdir/kernel/postinst.d/91-sbctl.install
%_man5dir/sbctl.conf.5.xz
%_man8dir/sbctl.8.xz
%_datadir/bash-completion/completions/sbctl
%_datadir/zsh/site-functions/_sbctl
%_datadir/fish/vendor_completions.d/sbctl.fish

%changelog
* Wed Nov 12 2025 Egor Ignatov <egori@altlinux.org> 0.18-alt1
- New version 0.18.

* Wed Jun 11 2025 Egor Ignatov <egori@altlinux.org> 0.17-alt2
- Fix 'invalid pe header' errors (closes: #54781).

* Tue May 06 2025 Egor Ignatov <egori@altlinux.org> 0.17-alt1
- New version 0.17.

* Wed Apr 16 2025 Egor Ignatov <egori@altlinux.org> 0.16-alt1
- First build for ALT.
