%global _unpackaged_files_terminate_build 1

# man build has heavy pandoc dependency
%ifnarch %e2k
%def_enable man
%else
%def_disable man
%endif

Name:		fscryptctl
Version:	1.0.0
Release:	alt4
Summary:	A low-level tool for the management of Linux kernel filesystem encryption

Group:		System/Kernel and hardware
License:	Apache-2.0
URL:		https://github.com/google/fscryptctl
Source:     %name-%version.tar

%{?!_without_check:%{?!_disable_check:BuildRequires: rpm-build-vm-createimage python3-module-pytest e2fsprogs}}
%{?!_disable_man:BuildRequires: pandoc}

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
    CFLAGS="%optflags" \
    %{?_disable_man:fscryptctl}

%install
%if_enabled man
    target=install
%else
    target=install-bin
%endif

%make_install $target \
    DESTDIR=%buildroot \
    PREFIX="/usr"

%if_enabled man
# duplicates man
rm %name.1.md
%endif

%check
sed -i '/mountpoint/s/--quiet/-q/' Makefile
vm-run --kvm=cond --sbin --user make test-all

%files
%_bindir/%name
%if_enabled man
%_man1dir/%name.1*
%endif
%doc *.md

%changelog
* Fri Nov 11 2022 Vitaly Chikunov <vt@altlinux.org> 1.0.0-alt4
- Unimportant update to improve %%check.

* Wed Dec 01 2021 Andrew Savchenko <bircoph@altlinux.org> 1.0.0-alt3
- Fix tests on kernels >= 5.15 where key entropy requirement is
  relaxed, upstream issue #26.
- Build man page on arches where pandoc is available.

* Mon May 10 2021 Vitaly Chikunov <vt@altlinux.org> 1.0.0-alt2
- spec: Run tests in %%check.

* Sat May 08 2021 Andrew Savchenko <bircoph@altlinux.org> 1.0.0-alt1
- Initial version
