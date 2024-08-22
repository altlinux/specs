%define _unpackaged_files_terminate_build 1

Name: passt
Version: 20240821
Release: alt1
Summary: User-mode networking daemons for virtual machines and namespaces
License: GPL-2.0-or-later AND BSD-3-Clause
Group: System/Configuration/Other
Vcs: git://passt.top/passt
Url: https://passt.top/
Source: %name-%version.tar

%description
passt implements a translation layer between a Layer-2 network interface and
native Layer-4 sockets (TCP, UDP, ICMP/ICMPv6 echo) on a host. It doesn't
require any capabilities or privileges, and it can be used as a simple
replacement for Slirp.

pasta (same binary as passt, different command) offers equivalent functionality,
for network namespaces: traffic is forwarded using a tap interface inside the
namespace, without the need to create further interfaces on the host, hence not
requiring any capabilities or privileges.

%prep
%setup

%build
# The Makefile creates symbolic links for pasta, but we need actual copies for
# SELinux file contexts to work as intended. Same with pasta.avx2 if present.
# Build twice, changing the version string, to avoid duplicate Build-IDs.
%make_build VERSION="%version-%release.%_arch-pasta"
mv -f passt pasta
%ifarch x86_64
mv -f passt.avx2 pasta.avx2
%make_build passt passt.avx2 VERSION="%version-%release.%_arch"
%else
%make_build passt VERSION="%version-%release.%_arch"
%endif

%install
# Already built (not as symbolic links), see above
touch pasta
%ifarch x86_64
touch pasta.avx2
%endif

%makeinstall_std prefix=%prefix
rm -rf %buildroot%_docdir/%name
%ifarch x86_64
ln -sr %buildroot%_mandir/man1/passt.1 %buildroot%_mandir/man1/passt.avx2.1
ln -sr %buildroot%_mandir/man1/pasta.1 %buildroot%_mandir/man1/pasta.avx2.1
install -p -m 755 %buildroot%_bindir/passt.avx2 %buildroot%_bindir/pasta.avx2
%endif

%files
%doc LICENSES/*.txt
%doc README.plain.md 
%doc doc/demo.sh
%_bindir/passt
%_bindir/pasta
%_bindir/qrap
%_man1dir/passt.1*
%_man1dir/pasta.1*
%_man1dir/qrap.1*
%ifarch x86_64
%_bindir/passt.avx2
%_man1dir/passt.avx2.1*
%_bindir/pasta.avx2
%_man1dir/pasta.avx2.1*
%endif

%changelog
* Thu Aug 22 2024 Alexey Shabalin <shaba@altlinux.org> 20240821-alt1
- 2024_08_21.1d6142f.

* Thu Jul 04 2024 Alexey Shabalin <shaba@altlinux.org> 20240624-alt1
- 2024_06_24.1ee2eca (ALT#50822).

* Mon Apr 15 2024 Alexey Shabalin <shaba@altlinux.org> 20240405.g954589b-alt1
- Initial build.
