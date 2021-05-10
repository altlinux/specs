%global _unpackaged_files_terminate_build 1

Name:		fscryptctl
Version:	1.0.0
Release:	alt2
Summary:	A low-level tool for the management of Linux kernel filesystem encryption

Group:		System/Kernel and hardware
License:	Apache-2.0
URL:		https://github.com/google/fscryptctl
Source:     %name-%version.tar

%{?!_without_check:%{?!_disable_check:BuildRequires: rpm-build-vm python3-module-pytest e2fsprogs}}

Requires:   kernel >= 5.4

%description
Fscryptctl is a low-level tool written in C that handles raw keys and manages
policies for Linux filesystem encryption, see
https://www.kernel.org/doc/html/latest/filesystems/fscrypt.html ,
specifically the "fscrypt" kernel interface which is supported by the ext4,
f2fs, and UBIFS filesystems.

Fscryptctl is mainly intended for embedded systems which can't use the
full-featured fscrypt tool (https://github.com/google/fscrypt), or for
testing or experimenting with the kernel interface to Linux filesystem
encryption. Fscryptctl does *not* handle key generation, key stretching, key
wrapping, or PAM integration.

%prep
%setup -q

%build
%make_build \
    CFLAGS="%optflags"

%install
%makeinstall_std \
    PREFIX="/usr"

%check
mkdir -p /usr/src/bin
ln -sf /usr/bin/time /usr/src/bin/sudo
sed -i '/mountpoint/s/--quiet/-q/' Makefile
vm-run --kvm=cond --sbin make test-all

%files
%_bindir/%name
%doc *.md

%changelog
* Mon May 10 2021 Vitaly Chikunov <vt@altlinux.org> 1.0.0-alt2
- spec: Run tests in %%check.

* Sat May 08 2021 Andrew Savchenko <bircoph@altlinux.org> 1.0.0-alt1
- Initial version
