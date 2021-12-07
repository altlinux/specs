Summary: Tools to access and modify virtual machine disk images
Name: guestfs-tools
Version: 1.47.3
Release: alt1
Group: File tools
License: GPLv2+
Url: http://libguestfs.org/
Source0: %name-%version.tar
Source2: %name-%version-common.tar
BuildRequires: gcc-c++
BuildRequires: libguestfs-devel >= 1.46.0
BuildRequires: perl-Pod-Simple
BuildRequires: perl-Module-Build
BuildRequires: perl-hivex
BuildRequires: perl-libintl
BuildRequires: /usr/bin/pod2text
BuildRequires: po4a
BuildRequires: libpcre2-devel
BuildRequires: libxml2-devel
BuildRequires: libjansson-devel
BuildRequires: libvirt-devel
BuildRequires: libcrypt-devel
BuildRequires: libncurses-devel
BuildRequires: ocaml-libguestfs-devel
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-gettext-devel
BuildRequires: ocaml-ounit-devel
BuildRequires: flex
BuildRequires: bison
BuildRequires: liblzma-devel
BuildRequires: zip
BuildRequires: unzip
BuildRequires: perl-Expect
BuildRequires: /usr/bin/qemu-img
BuildRequires: xorriso
BuildRequires: perl-Sys-Guestfs
BuildRequires: bash-completion

%ifarch %ix86 x86_64 aarch64
Requires: guestfs-data
%endif

# For virt-builder:
Requires: libvirt-daemon-driver-qemu >= 0.10.2
Requires: %_bindir/fusermount
Requires: %_bindir/getopt
Requires: /lib/systemd/systemd-machined
Requires: libosinfo
Requires: curl
Requires: gnupg2
Requires: /usr/bin/qemu-img
Requires: xz
Provides: libguestfs-tools = %EVR
Obsoletes: libguestfs-tools <= %EVR

%description
This package contains miscellaneous system administrator command line
tools for virtual machines.

%package -n virt-win-reg
Summary: Access and modify the Windows Registry of a Windows VM
Group: File tools
BuildArch: noarch

%description -n virt-win-reg
Virt-win-reg lets you look at and modify the Windows Registry of
Windows virtual machines.

%package -n virt-dib
Summary: Safe and secure diskimage-builder replacement
Group: File tools

%description -n virt-dib
Virt-dib is a safe and secure alternative to the OpenStack
diskimage-builder command.  It is compatible with most
diskimage-builder elements.

%prep
%setup -a2
tar -xf %SOURCE2 -C common


%build
%autoreconf
%configure

# Building index-parse.c by hand works around a race condition in the
# autotools cruft, where two or more copies of yacc race with each
# other, resulting in a corrupted file.
make -j1 -C builder index-parse.c

%make V=1

%install
%makeinstall_std

# Move installed documentation back to the source directory so
# we can install it using a %%doc rule.
mv %buildroot%_docdir/%name installed-docs
gzip --best installed-docs/*.xml

%find_lang %name

rm -rf %buildroot%_mandir/{ja,uk}

%files -f %name.lang
%doc COPYING README installed-docs/*
%dir %_sysconfdir/virt-builder
%dir %_sysconfdir/virt-builder/repos.d
%config(noreplace) %_sysconfdir/virt-builder/repos.d/*
%_bindir/virt-alignment-scan
%_bindir/virt-builder
%_bindir/virt-builder-repository
%_bindir/virt-cat
%_bindir/virt-customize
%_bindir/virt-df
%_bindir/virt-diff
%_bindir/virt-edit
%_bindir/virt-filesystems
%_bindir/virt-format
%_bindir/virt-get-kernel
%_bindir/virt-index-validate
%_bindir/virt-inspector
%_bindir/virt-log
%_bindir/virt-ls
%_bindir/virt-make-fs
%_bindir/virt-resize
%_bindir/virt-sparsify
%_bindir/virt-sysprep
%_bindir/virt-tail
%_man1dir/virt-alignment-scan.1*
%_man1dir/virt-builder-repository.1*
%_man1dir/virt-builder.1*
%_man1dir/virt-cat.1*
%_man1dir/virt-customize.1*
%_man1dir/virt-df.1*
%_man1dir/virt-diff.1*
%_man1dir/virt-edit.1*
%_man1dir/virt-filesystems.1*
%_man1dir/virt-format.1*
%_man1dir/virt-get-kernel.1*
%_man1dir/virt-index-validate.1*
%_man1dir/virt-inspector.1*
%_man1dir/virt-log.1*
%_man1dir/virt-ls.1*
%_man1dir/virt-make-fs.1*
%_man1dir/virt-resize.1*
%_man1dir/virt-sparsify.1*
%_man1dir/virt-sysprep.1*
%_man1dir/virt-tail.1*
%dir %_datadir/bash-completion/completions
%_datadir/bash-completion/completions/virt-*

%files -n virt-win-reg
%doc README COPYING
%_bindir/virt-win-reg
%_mandir/man1/virt-win-reg.1*

%files -n virt-dib
%doc README COPYING
%_bindir/virt-dib
%_mandir/man1/virt-dib.1*

%changelog
* Tue Dec 07 2021 Anton Farygin <rider@altlinux.ru> 1.47.3-alt1
- 1.47.2 -> 1.47.3

* Sat Nov 27 2021 Anton Farygin <rider@altlinux.ru> 1.47.2-alt2
- added Requires, which is needed to build images (closes: #41443)

* Sun Nov 07 2021 Anton Farygin <rider@altlinux.ru> 1.47.2-alt1
- first build for Sisyphus
