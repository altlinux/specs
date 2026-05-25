%define _unpackaged_files_terminate_build 1

Name: gitlogue
Version: 0.9.0
Release: alt1

Summary: Playback of Git commits in the terminal as an animated story
License: ISC
Group: Development/Other
URL: https://github.com/unhappychoice/gitlogue

Source: %name-%version.tar
# Prepare using:
# cargo-vendor-alt \
#   --exclude-crate-path libgit2-sys#libgit2 \
#   --exclude-crate-path libssh2-sys#libssh2 \
#   --exclude-crate-path libz-sys#src/zlib \
#   --exclude-crate-path libz-sys#src/zlib-ng \
#   --exclude-crate-path openssl-src#openssl
Source1: vendor.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libgit2)
BuildRequires: pkgconfig(libssh2)
BuildRequires: pkgconfig(zlib)
BuildRequires: perl-IPC-Cmd
BuildRequires: perl-Time-Piece

%description
A cinematic Git commit replay tool for the terminal,
turning your Git history into a living, animated story.

Watch commits unfold with realistic typing animations,
syntax highlighting, and file tree transitions,
transforming code changes into a visual experience.

%prep
%setup -a 1 -q
%patch -p1
%rust_prep

%build
export OPENSSL_NO_VENDOR=1
export LIBSSH2_SYS_USE_PKG_CONFIG=1
export LIBGIT2_NO_VENDOR=1
%rust_build

%install
%rust_install

%check
export OPENSSL_NO_VENDOR=1
export LIBSSH2_SYS_USE_PKG_CONFIG=1
export LIBGIT2_NO_VENDOR=1
%rust_test

%files
%_bindir/*
%doc README.md CHANGELOG.md

%changelog
* Tue May 19 2026 Sergey Savelev <medovi@altlinux.org> 0.9.0-alt1
- New version 0.9.0.

* Thu Feb 12 2026 Sergey Savelev <medovi@altlinux.org> 0.8.0-alt1
- New version 0.8.0.

* Mon Jan 19 2026 Sergey Savelev <medovi@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
