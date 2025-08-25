%define _unpackaged_files_terminate_build 1

Name: nix
Version: 2.30.2
Release: alt1

Summary: Nix software deployment system
License: LGPLv2+
Group: System/Configuration/Packaging

Url: https://github.com/NixOS/nix
# Source-url: https://github.com/NixOS/nix/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Source1: %name.conf

Source2: sysusers.conf

Patch: nix-2.29.0-alt-remove-unused-sh-files.patch
Patch1: nix-2.30.2-alt-drop-broken-ssl-path.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-systemd
BuildRequires: meson
BuildRequires: cmake
BuildRequires: bison
BuildRequires: bzlib-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-context-devel
BuildRequires: boost-coroutine-devel
BuildRequires: libbrotli-devel
BuildRequires: libeditline-devel
BuildRequires: flex
BuildRequires: libgc-devel
BuildRequires: gcc-c++
BuildRequires: jq
BuildRequires: libjson11-devel
BuildRequires: libarchive-devel
BuildRequires: libcurl-devel
BuildRequires: libseccomp-devel
BuildRequires: libsodium-devel
BuildRequires: liblowdown-devel
BuildRequires: libssl-devel
BuildRequires: libsqlite3-devel
BuildRequires: liblzma-devel
BuildRequires: patchelf
BuildRequires: nlohmann-json-devel
BuildRequires: libgit2-devel
BuildRequires: libgc-devel
BuildRequires: libtoml11-devel
BuildRequires: libblake3-devel
BuildRequires: graphviz
BuildRequires: rsync
BuildRequires: curl
BuildRequires: /proc
BuildRequires: lowdown
BuildRequires: mdbook-linkcheck
BuildRequires: doxygen

%ifarch x86_64
BuildRequires: libcpuid-devel
%endif

Requires: %name-doc = %EVR

%description
Nix is a purely functional package manager. It allows multiple
versions of a package to be installed side-by-side, ensures that
dependency specifications are complete, supports atomic upgrades and
rollbacks, allows non-root users to install software, and has many
other features. It is the basis of the NixOS Linux distribution, but
it can be used equally well under other Unix systems

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %EVR

%package -n  lib%name
Summary: libs for %name
Group: System/Libraries

%description -n lib%name
%summary.

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%prep
%setup
%patch -p1
%patch1 -p1

%build
# Test disabled because rapidcheck is not builded
# pkgconfig.prov: ERROR: %_usrsrc/tmp/librapidcheck-devel-buildroot/usr/lib64/pkgconfig/rapidcheck.pc: invalid pkg-config output: rapidcheck =
# Perl bindings build requires to libnix
%meson -Dnix:profile-dir=%_sysconfdir/profile.d -Dbindings=false -Ddoc-gen=true -Dunit-tests=false
%meson_build

%install
%meson_install

mkdir -p %buildroot%_sysconfdir/nix/
mkdir -p %buildroot%_sysusersdir/

install -m 0644 %SOURCE1 %buildroot%_sysconfdir/nix/nix.conf
install -m 0644 %SOURCE2 %buildroot%_sysusersdir/%name-daemon.conf

# fix permission of nix profile
chmod 755 %buildroot%_sysconfdir/profile.d/nix-daemon.fish
chmod 755 %buildroot%_sysconfdir/profile.d/nix-daemon.sh

patchelf --remove-rpath %buildroot%_bindir/nix %buildroot%_libdir/*.so

%pre
%sysusers_create_package %name %SOURCE2

%files
%doc COPYING
%doc README.md
%_bindir/nix*
%config(noreplace) %_sysconfdir/nix/nix.conf
%_libexecdir/tmpfiles.d/nix-daemon.conf
%_sysusersdir/nix-daemon.conf
%_sysconfdir/profile.d/nix-daemon.fish
%_sysconfdir/profile.d/nix-daemon.sh
%_libexecdir/nix/build-remote
%_unitdir/nix-daemon.service
%_unitdir/nix-daemon.socket
%_datadir/bash-completion/completions/nix
%_datadir/fish/vendor_completions.d/nix.fish
%_datadir/zsh/site-functions/_nix
%_datadir/zsh/site-functions/run-help-nix

%files devel
%_includedir/nix/
%_includedir/*.h
%_includedir/*.hh
%_pkgconfigdir/*.pc

%files -n lib%name
%_libdir/*.so

%files doc
%_docdir/nix/
%_man1dir/nix*
%_man5dir/nix*
%_man8dir/nix*

%changelog
* Mon Aug 25 2025 Boris Yumankulov <boria138@altlinux.org> 2.30.2-alt1
- new version 2.30.2
- fix ssl patch (ALT bug: 55674) 

* Thu Jul 10 2025 Boris Yumankulov <boria138@altlinux.org> 2.30.0-alt1
- new version 2.30.0
- drop ExclusiveArch

* Sun Jul 06 2025 Boris Yumankulov <boria138@altlinux.org> 2.29.1-alt1
- new version 2.29.1

* Sun May 25 2025 Boris Yumankulov <boria138@altlinux.org> 2.29.0-alt1
- new version 2.29.0
- create users and group using %%sysusers_create_package macro

* Wed Mar 12 2025 Boris Yumankulov <boria138@altlinux.org> 2.24.10-alt3
- clean spec
- build nix-doc package

* Wed Dec 25 2024 Boris Yumankulov <boria138@altlinux.org> 2.24.10-alt2
- apply shared libs policy

* Sun Nov 03 2024 Boris Yumankulov <boria138@altlinux.org> 2.24.10-alt1
- new version 2.24.10

* Thu Oct 03 2024 Boris Yumankulov <boria138@altlinux.org> 2.24.9-alt1
- new version 2.24.9

* Wed Aug 21 2024 Boris Yumankulov <boria138@altlinux.org> 2.24.3-alt1
- new version 2.24.3

* Sun Aug 18 2024 Boris Yumankulov <boria138@altlinux.org> 2.24.2-alt1
- new version 2.24.2

* Thu Jul 11 2024 Boris Yumankulov <boria138@altlinux.org> 2.23.3-alt1
- new version 2.23.3

* Mon Jul 01 2024 Boris Yumankulov <boria138@altlinux.org> 2.23.1-alt1
- initial build for ALT Sisyphus

