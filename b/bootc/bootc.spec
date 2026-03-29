%define _unpackaged_files_terminate_build 1

Name: bootc
Version: 1.13.0
Release: alt2

Summary: Boot and upgrade via container images
License: Apache-2.0 AND BSD-3-Clause AND MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
Group: System/Base
Url: https://github.com/containers/bootc
Vcs: https://github.com/containers/bootc.git

# i586 not supported
# https://github.com/containers/bootc/blob/main/lib/src/install/baseline.rs#L252
ExclusiveArch: x86_64 ppc64le aarch64

Source: %name-%version.tar
Source10: vendor.tar
Patch: %name-%version-%release.patch

Requires: composefs
Requires: ostree
Requires: skopeo
Requires: podman
Requires: bootupd
Requires: bubblewrap

BuildRequires: rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: go-md2man
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(ostree-1) >= 2025.3

%description
Transactional, in-place operating system updates using OCI/Docker container images.

Contains update, test and create commands.

%package -n system-reinstall-%name
Summary: Utility to reinstall the current system via %name
Group: Other

Requires: podman

%description -n system-reinstall-%name
This package provides a utility to simplify reinstalling the current system to a given %name image.

%prep
%setup -a10
%autopatch -p1

%build
%make_build

%install
%makeinstall_std
# Remove broken link
rm -fv -- %buildroot/%_prefix/lib/%name/storage
# Needs only for Rad Hat
rm -fv -- %buildroot/%_unitdir/%name-publish-rhsm-facts.service

%post
# Create link to ostree bootc storage removed at %install
if [ -e /sysroot/ostree/%name/storage ] && [ ! -L "%_prefix/lib/%name/storage" ]; then
    ln -s -- /sysroot/ostree/%name/storage "%_prefix/lib/%name/storage"
fi

%preun
# Remove file created in %post
if [ -e "%_prefix/lib/%name/storage" ]; then
    rm -fv -- "%_prefix/lib/%name/storage"
fi

%files
%_bindir/%name
%_prefix/lib/%name/
%_prefix/lib/dracut/modules.d/51%name
%_gen_dir/%name-systemd-generator/
%_unitdir/%name-*
%_docdir/%name/
%_man5dir/%{name}*
%_man8dir/%{name}*
%_man8dir/system-reinstall-%{name}*
%_datadir/bash-completion/completions/%name
%_datadir/elvish/lib/%name.elv
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/powershell/Modules/Bootc/Bootc.psm1
%_datadir/zsh/site-functions/_%name
%doc README.md

%files -n system-reinstall-%name
%_bindir/system-reinstall-%name

%changelog
* Mon Mar 23 2026 Vladimir Romanov <rirusha@altlinux.org> 1.13.0-alt2
- Added runtime dependency on bubblewrap.

* Tue Feb 24 2026 Vladimir Romanov <rirusha@altlinux.org> 1.13.0-alt1
- New version: 1.13.0.

* Tue Feb 17 2026 Vladimir Romanov <rirusha@altlinux.org> 1.12.1-alt1
- New version: 1.12.1.

* Sun Dec 07 2025 Vladimir Romanov <rirusha@altlinux.org> 1.11.0-alt1
- New version: 1.11.0.
- Removed broken tests.

* Sat Oct 11 2025 Vladimir Romanov <rirusha@altlinux.org> 1.9.0-alt1
- New version: 1.9.0.

* Tue Sep 09 2025 Vladimir Vaskov <rirusha@altlinux.org> 1.8.0-alt1
- New version: 1.8.0.
- Created subpackage with utility for system reinstalling with bootc image.

* Fri Feb 14 2025 Vladimir Vaskov <rirusha@altlinux.org> 1.1.4-alt1
- Initial build.
