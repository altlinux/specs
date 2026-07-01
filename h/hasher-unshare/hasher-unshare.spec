Name: hasher-unshare
Version: 0.0.1
Release: alt1

Summary: Rootless drop-in replacement for hasher-priv using user namespaces
License: GPLv2+
Group: Development/Other

Url: https://altlinux.space/alt-security/hasher-unshare
VCS: https://altlinux.space/alt-security/hasher-unshare.git

BuildArch: noarch

Source: %name-%version.tar

%define _libexecdir %_prefix/libexec

%description
hasher-unshare is a drop-in replacement for hasher-priv that lets the hasher
build tool run inside rootless (unprivileged) containers, such as rootless
podman.

Instead of a privileged helper, it uses Linux user namespaces to provide the
separate rooter and builder identities that hasher expects and to build the
chroot. It exposes the same command interface (getconf, getugid, chrootuid),
so hasher works unchanged.

%prep
%setup

%install
install -dm 755 %buildroot%_libexecdir/hasher-unshare
cp -a ./hasher-unshare/* %buildroot%_libexecdir/hasher-unshare

%files
%doc README.md hasher.conf
%_libexecdir/hasher-unshare

%changelog
* Wed Jul 01 2026 Egor Ignatov <egori@altlinux.org> 0.0.1-alt1
- Initial build for ALT.
