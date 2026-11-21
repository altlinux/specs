%define _unpackaged_files_terminate_build 1

Name: proot
Version: 5.5.0
Release: alt1

Summary: User-space implementation of chroot, mount --bind and binfmt_misc
License: GPL-2.0-or-later
Group: Development/Other

URL: https://proot-me.github.io/
VCS: https://github.com/proot-me/proot.git

Source: %name-%version.tar
Source1: uthash.tar

Patch1: %name-%version-%release.patch

BuildRequires: libtalloc-devel
BuildRequires: /proc

%description
PRoot provides chroot, bind mounts and execution of foreign architectures
using ptrace, without privileges or kernel modules.

%prep
%setup -a1
%autopatch -p1

%build
%make_build -C src

%install
%makeinstall_std PREFIX=%_prefix -C src

%check
src/proot --version
src/proot -r / /bin/true
src/proot -0 /bin/sh -c 'test "$(id -u)" = 0'

%files
%_bindir/proot
%doc AUTHORS README.rst CHANGELOG.rst doc/proot/manual.rst

%changelog
* Tue Nov 03 2026 Vladimir Romanov <rirusha@altlinux.org> 5.5.0-alt1
- Initial build.
