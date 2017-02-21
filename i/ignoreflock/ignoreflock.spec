Name: ignoreflock
Version: 1
Release: alt2

Summary: A small wrapper to disable flock function

Group: File tools
License: GPLv3
Url: https://github.com/Etersoft/ignoreflock

# Source-git: https://github.com/Etersoft/ignoreflock.git
Source: %name-%version.tar

%description
ignoreflock is LD_PRELOAD library that disables flock function.
On local Linux filesystems, POSIX locks and BSD locks are invisible to one another.
But on network filesystems flock implemented open POSIX locks and
have intersections with fcntl style locking.

%prep
%setup

%build
%__subst 's|$(dirname $0)|%_libdir|g' %name
%make

%install
install -D %name %buildroot%_bindir/%name
install -D -m0644 lib%name.so.0 %buildroot%_libdir/lib%name.so.0

%files
%doc README.md
%_bindir/%name
%_libdir/*.so*

%changelog
* Tue Feb 21 2017 Vitaly Lipatov <lav@altlinux.ru> 1-alt2
- fix packing

* Mon Feb 20 2017 Vitaly Lipatov <lav@altlinux.ru> 1-alt1
- initial build for ALT Linux Sisyphus
