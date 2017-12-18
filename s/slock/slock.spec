Name: slock
Version: 1.4
Release: alt3

Summary: Simple X display locker
Summary(ru_RU.UTF-8): Простой блокировщик экрана
Summary(uk_UA.UTF-8): Простий блокувач екрану

License: MIT/X11
Group: System/X11
Url: http://tools.suckless.org/slock/

Packager: Vladimir D. Seleznev <vseleznv@altlinux.org>
# packaged release tag from http://git.suckless.org/slock
Source: %name-%version.tar
Source1: %name.watch
# http://git.altlinux.org/gears/s/slock.git
Patch1: %name-%version-alt.patch

# Automatically added by buildreq on Mon Dec 18 2017
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libXrender-devel python-base python-modules xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: libXext-devel libXrandr-devel libpam-devel

Requires(post): /sbin/setcap

%description
Simple X display locker.

%description -l ru_RU.UTF-8
Простой блокировщик экрана.

%description -l uk_UA.UTF-8
Простий блокувач екрану.

%prep
%setup
%patch1 -p1

%build
export CFLAGS="%optflags"
make

%install
make DESTDIR=%buildroot PREFIX=%_prefix install

%post
/sbin/setcap cap_sys_resource,cap_dac_override+ep %_bindir/slock

%files
%doc LICENSE
%config(noreplace) %_sysconfdir/pam.d/slock
%_bindir/*
%_man1dir/*

%changelog
* Mon Dec 18 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4-alt3
- dropped suid
- added support for pam auth
- applied fixes from upstream:
  + Fix resize with multiple monitors and portrait
  + there can only be one window in the event
  + Properly clear the last entered character

* Thu Feb 16 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4-alt2
- fixed build for debuginfo.
- packaged tarball from release tag.
- changed gear scheme.
- added ru/uk descriptions.
- added support for watchfile.
- packaged LICENSE file.
- does not treat cleared input like a wrong password.

* Thu Nov 24 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4-alt1
- new version

* Tue Mar 22 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.3-alt1
- new version

* Thu Mar 10 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2-alt1.1
- Rebuilt to fix requires.

* Mon Dec 07 2015 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.2-alt1
- Initial build.
