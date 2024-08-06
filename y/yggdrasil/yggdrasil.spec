%define _unpackaged_files_terminate_build 1
%define import_path github.com/yggdrasil-network/yggdrasil-go

%define _libexecdir /usr/libexec

Name: yggdrasil
Version: 0.5.7
Release: alt1

Summary: End-to-end encrypted IPv6 networking
License: LGPLv3
Group: Security/Networking
Url: https://yggdrasil-network.github.io
Vcs: https://github.com/yggdrasil-network/yggdrasil-go

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
Yggdrasil is an overlay network implementation of a new routing scheme for mesh
networks. It is designed to be a future-proof decentralised alternative to the
structured routing protocols commonly used today on the Internet and other
networks.

The current implementation of Yggdrasil is a lightweight userspace software
router which is easy to configure and supported on a wide range of platforms.
It provides end-to-end encrypted IPv6 routing between all network participants.
Peerings between nodes can be configured using TCP/TLS connections over local
area networks, point-to-point links or the Internet. Even though the Yggdrasil
Network provides IPv6 routing between nodes, peering connections can be set up
over either IPv4 or IPv6.

%prep
%setup -a1
%autopatch -p1

# fix 'chmod' path
sed -i '/chmod/s|/usr||' contrib/systemd/yggdrasil-default-config.service

%build
export GO111MODULE=off
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
export PKGSRC="%import_path/src/version"
export PKGNAME="%name"
export PKGVER="%version-%release"
export LDFLAGS="-X $PKGSRC.buildName=$PKGNAME -X $PKGSRC.buildVersion=$PKGVER"
%golang_build cmd/*

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

# move 'genkeys' to %%_libexecdir
mkdir -p %buildroot%_libexecdir/yggdrasil
mv %buildroot{%_bindir,%_libexecdir/yggdrasil}/genkeys

# install systemd services
cd contrib/systemd
install -pD -m0644 {,%buildroot%_unitdir/}yggdrasil.service
install -pD -m0644 {,%buildroot%_unitdir/}yggdrasil-default-config.service

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/%{name}*
%_libexecdir/%name/
%_unitdir/*.service

%pre
/usr/sbin/groupadd -r -f yggdrasil

%changelog
* Tue Aug 06 2024 Anton Zhukharev <ancieg@altlinux.org> 0.5.7-alt1
- Updated to 0.5.7.

* Fri May 31 2024 Anton Zhukharev <ancieg@altlinux.org> 0.5.6-alt1
- Updated to 0.5.6.

* Thu Apr 04 2024 Anton Zhukharev <ancieg@altlinux.org> 0.5.5-alt2
- Built real 0.5.5.

* Thu Feb 08 2024 Anton Zhukharev <ancieg@altlinux.org> 0.5.5-alt1
- Updated to 0.5.5.

* Wed Dec 20 2023 Anton Zhukharev <ancieg@altlinux.org> 0.5.4-alt1
- Updated to 0.5.4.

* Tue Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Tue Oct 31 2023 Anton Zhukharev <ancieg@altlinux.org> 0.5.1-alt1
- Updated to 0.5.1.

* Tue Jan 17 2023 Anton Zhukharev <ancieg@altlinux.org> 0.4.7-alt2
- package 'genkeys' util
- clean up spec
- add Vcs tag

* Tue Nov 22 2022 Anton Zhukharev <ancieg@altlinux.org> 0.4.7-alt1
- update to 0.4.7

* Fri Nov 04 2022 Anton Zhukharev <ancieg@altlinux.org> 0.4.6-alt1
- update to 0.4.6

* Sat Jul 30 2022 Anton Zhukharev <ancieg@altlinux.org> 0.4.4-alt2
- add go vendor modules into source tree instead of using patch

* Sun Jul 24 2022 Anton Zhukharev <ancieg@altlinux.org> 0.4.4-alt1
- update to 0.4.4

* Tue Jun 07 2022 Anton Zhukharev <ancieg@altlinux.org> 0.4.3-alt2
- change instructions for golang building
- add buildName and buildVersion to the output of `yggdrasil -version'

* Mon May 30 2022 Anton Zhukharev <ancieg@altlinux.org> 0.4.3-alt1
- initial build for Sisyphus
