Name: fakechroot
Version: 2.19
Release: alt1
Summary: Gives a fake chroot environment
Group: Development/Tools
License: LGPLv2+
Url: https://github.com/dex4er/fakechroot
# Repacked %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

Obsoletes: %name-libs < %EVR

# Automatically added by buildreq on Wed Aug 31 2016
# optimized out: gnu-config perl perl-podlators python-base python3
BuildRequires: perl-devel python3-base

# ldd.fakechroot
Requires: /usr/bin/objdump

%description
fakechroot runs a command in an environment were is additionally
possible to use the chroot(8) call without root privileges. This is
useful for allowing users to create their own chrooted environment
with possibility to install another packages without need for root
privileges.

%prep
%setup

%build
%configure \
	--disable-static \
	--disable-silent-rules \
#
%make_build

# For dependency-clean %%doc.
chmod -x scripts/{relocatesymlinks,restoremode,savemode}.sh

%install
%makeinstall_std
# Drop libtool files
find %buildroot%_libdir -name '*.la' -delete -print

%check
%make check

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
* Wed Feb 22 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.19-alt1
- Updated to 2.19.

* Wed Aug 31 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.18-alt2
- Initial build.
