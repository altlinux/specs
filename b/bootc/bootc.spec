%define _unpackaged_files_terminate_build 1

Name: bootc
Version: 1.1.4
Release: alt1

Summary: Boot and upgrade via container images
License: Apache-2.0 AND BSD-3-Clause AND MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
Group: System/Base
Url: https://github.com/containers/bootc
Vcs: https://github.com/containers/bootc.git

# i586 not supported
# https://github.com/containers/bootc/blob/main/lib/src/install/baseline.rs#L252
ExclusiveArch: x86_64 ppc64le aarch64

Source: %name-%version.tar
Patch: %name-%version-alt.patch

Requires: composefs
Requires: ostree
Requires: skopeo
Requires: podman

BuildRequires: rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(ostree-1)

%description
Transactional, in-place operating system updates using OCI/Docker container images.

Contains update, test and create commands.

%prep
%setup
%autopatch -p1

%build
%make_compile

%install
%makeinstall_std
# Remove broken link
rm -fv -- %buildroot/%_prefix/lib/%name/storage
# Needs only for Rad Hat
rm -fv -- %buildroot/%_unitdir/bootc-publish-rhsm-facts.service

%check
%make test-bin-archive

%post
# Check if system is immutable and create link removed at %install
if [ -d "/sysroot" ]; then
    ln -s -- /sysroot/ostree/bootc/storage %_prefix/lib/%name/storage
fi

%preun
# Remove file created in %post
rm -fv -- %_prefix/lib/%name/storage

%files
%_bindir/%name
%_prefix/lib/%name/
%_gen_dir/bootc-systemd-generator/
%_unitdir/bootc-*
%_unitdir/multi-user.target.wants/bootc-*
%_docdir/%name/
%doc README.md

%changelog
* Thu Feb 14 2025 Vladimir Vaskov <rirusha@altlinux.org> 1.1.4-alt1
- Initial build.
