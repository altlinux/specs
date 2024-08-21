Name: nix
Version: 2.24.3
Release: alt1

Summary: Nix software deployment system
License: LGPLv2+
Group: System/Configuration/Packaging

Url: https://github.com/NixOS/nix
# Source-url: https://github.com/NixOS/nix/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Source1: %name.conf

Source2: sysusers.conf

Source3: tmpfiles.conf

BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: bison
BuildRequires: bzlib-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-context-devel
BuildRequires: libbrotli-devel
BuildRequires: libeditline-devel
BuildRequires: flex
BuildRequires: libgc-devel
BuildRequires: gcc-c++
BuildRequires: jq
BuildRequires: libjson11-devel
BuildRequires: libarchive-devel
BuildRequires: libcpuid-devel
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

ExclusiveArch: x86_64

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

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%autoreconf
%configure --localstatedir=/nix/var --disable-tests --disable-unit-tests --disable-doc-gen --enable-gc
%make_build

%install
%makeinstall_std

# Delete unused files
rm -r %buildroot%_sysconfdir/init
rm -r %buildroot%_sysconfdir/profile.d/nix.sh
rm -r %buildroot%_sysconfdir/profile.d/nix.fish

mkdir -p %buildroot%_sysusersdir/
mkdir -p %buildroot%_tmpfilesdir/
mkdir -p %buildroot%_sysconfdir/nix/

install -m 0644 %SOURCE1 %buildroot%_sysconfdir/nix/nix.conf
install -m 0644 %SOURCE2 %buildroot%_sysusersdir/%name-daemon.conf
install -m 0644 %SOURCE3 %buildroot%_tmpfilesdir/%name-daemon.conf

# fix permission of nix profile
chmod 755 %buildroot%_sysconfdir/profile.d/nix-daemon.fish
chmod 755 %buildroot%_sysconfdir/profile.d/nix-daemon.sh

patchelf --remove-rpath %buildroot%_bindir/nix %buildroot%_libdir/*.so

%files
%doc COPYING
%doc README.md
%_bindir/nix*
%_libdir/*.so
%config(noreplace) %_sysconfdir/nix/nix.conf
%_sysconfdir/profile.d/nix-daemon.fish
%_sysconfdir/profile.d/nix-daemon.sh
%_libexecdir/nix/build-remote
%_unitdir/nix-daemon.service
%_unitdir/nix-daemon.socket
%_sysusersdir/nix-daemon.conf
%_tmpfilesdir/nix-daemon.conf
%_datadir/bash-completion/completions/nix
%_datadir/fish/vendor_completions.d/nix.fish
%_datadir/zsh/site-functions/_nix
%_datadir/zsh/site-functions/run-help-nix

%files devel
%_includedir/nix/
%_pkgconfigdir/*.pc

%changelog
* Wed Aug 21 2024 Boris Yumankulov <boria138@altlinux.org> 2.24.3-alt1
- new version 2.24.3

* Sun Aug 18 2024 Boris Yumankulov <boria138@altlinux.org> 2.24.2-alt1
- new version 2.24.2

* Thu Jul 11 2024 Boris Yumankulov <boria138@altlinux.org> 2.23.3-alt1
- new version 2.23.3

* Mon Jul 01 2024 Boris Yumankulov <boria138@altlinux.org> 2.23.1-alt1
- initial build for ALT Sisyphus

