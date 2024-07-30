%global _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

# man build has heavy pandoc dependency
%ifnarch %e2k
%def_enable man
%else
%def_disable man
%endif

Name:		fscryptctl
Version: 1.2.0
Release: alt2
Summary:	A small C tool for Linux filesystem encryption

Group:		System/Kernel and hardware
License:	Apache-2.0
URL:		https://github.com/google/fscryptctl
Source:     %name-%version.tar

%{?!_without_check:%{?!_disable_check:BuildRequires: rpm-build-vm-createimage python3-module-pytest e2fsprogs}}
%{?!_disable_man:BuildRequires: pandoc}

%description
fscryptctl is a low-level tool written in C that handles raw keys and
manages policies for Linux filesystem encryption, see [1], specifically
the "fscrypt" kernel interface which is supported by the ext4, f2fs,
UBIFS, and CephFS filesystems.

fscryptctl is mainly intended for embedded systems which can't use
the full-featured fscrypt tool, or for testing or experimenting with
the kernel interface to Linux filesystem encryption. fscryptctl does
*not* handle key generation, key stretching, key wrapping, or PAM
integration. Most users should use the fscrypt tool instead, which
supports these features and generally is much easier to use.

[1] https://www.kernel.org/doc/html/latest/filesystems/fscrypt.html

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
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
    PREFIX=%_prefix

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
* Sat Jul 27 2024 Vitaly Chikunov <vt@altlinux.org> 1.2.0-alt2
- spec: Remove R:kernel. The kernel package does not need to be installed for
  this tool to work. Perhaps, if the tool is running, the kernel is already
  there. Also, the installed kernel is not necessarily the booted kernel.
  The Requires tag is not a commentary on which kernel is best for the tool.
  Therefore, a Requires tag was misused.

* Sun Mar 24 2024 Vitaly Chikunov <vt@altlinux.org> 1.2.0-alt1
- Update to v1.2.0 (2024-03-20).

* Mon Jun 05 2023 Vitaly Chikunov <vt@altlinux.org> 1.1.0-alt1
- Update to v1.1.0 (2023-01-30).

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
