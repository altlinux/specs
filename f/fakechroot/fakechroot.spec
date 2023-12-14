%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lfs=relaxed

Name: fakechroot
Version: 2.20.1
Release: alt4
Summary: Gives a fake chroot environment
Group: Development/Tools
License: LGPL-2.1-or-later
Url: https://github.com/dex4er/fakechroot
# For ldd.fakechroot
Requires: /usr/bin/objdump

Source: %name-%version.tar
BuildRequires: perl-devel
BuildRequires: python3-base
BuildRequires: /usr/bin/pod2man

%description
fakechroot runs a command in an environment were is additionally
possible to use the chroot(8) call without root privileges. This is
useful for allowing users to create their own chrooted environment
with possibility to install another packages without need for root
privileges.

%prep
%setup
# We have even stronger fortify level by default.
grep -Zlr '_FORTIFY_SOURCE' | xargs -0 sed -i '/^#define _FORTIFY_SOURCE 2/d'

%build
%ifarch x86_64
%add_optflags -fanalyzer
%endif
%add_optflags -Wno-unused-variable
%autoreconf
%configure \
	--disable-static \
	--disable-silent-rules \
	%nil
%make_build

# For dependency-clean %%doc.
chmod -x scripts/{relocatesymlinks,restoremode,savemode}.sh

%install
%makeinstall_std
# Drop libtool files
find %buildroot%_libdir -name '*.la' -delete -print

%check
%make_build check || {
	cat test/test-suite.log
	exit 1
}

%files
%doc scripts/{relocatesymlinks,restoremode,savemode}.sh
%doc NEWS.md README.md
%doc COPYING LICENSE
%_bindir/%name
%_bindir/env.%name
%_bindir/ldd.%name
%_sbindir/chroot.%name
%_libdir/%name/
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/chroot.env
%config(noreplace) %_sysconfdir/%name/debootstrap.env
%config(noreplace) %_sysconfdir/%name/rinse.env
%_mandir/man1/%name.1*

%changelog
* Wed Dec 13 2023 Vitaly Chikunov <vt@altlinux.org> 2.20.1-alt4
- Recreate after deletion by ftbfs cleaner, based on Debian version
  2.20.1+ds-15 (2023-02-06) and upstream PRs.

* Wed Oct 13 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.20.1-alt3
- Added glibc 2.33+ support patches from
  https://github.com/dex4er/fakechroot/pull/85 (thanks to Ilya Lipnitskiy), and
  https://github.com/dex4er/fakechroot/pull/86 (thanks to neok-m4700).

* Tue Apr 27 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.20.1-alt2
- Backported upstream commit adding support of libc wrapper for
  statx(1) syscall.

* Fri Aug 16 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.20.1-alt1
- Updated to 2.20.1.

* Fri Aug 18 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.19-alt2
- Added support of LFS-compatible fts functions.

* Wed Feb 22 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.19-alt1
- Updated to 2.19.

* Wed Aug 31 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.18-alt2
- Initial build.
