%global _unpackaged_files_terminate_build 1

Name:		fscryptctl
Version:	1.0.0
Release:	alt1
Summary:	A low-level tool for the management of Linux kernel filesystem encryption

Group:		System/Kernel and hardware
License:	Apache-2.0
URL:		https://github.com/google/fscryptctl
Source:     %name-%version.tar

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

%files
%_bindir/%name
%doc *.md

%changelog
* Sat May 08 2021 Andrew Savchenko <bircoph@altlinux.org> 1.0.0-alt1
- Initial version
