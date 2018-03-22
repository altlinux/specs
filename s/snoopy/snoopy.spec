%def_without check
Summary: User monitoring and command logging
Name: snoopy
Version: 2.4.6
Release: alt1
Url: https://github.com/a2o/snoopy
Source: %name-%version.tar.gz
Patch: snoopy-2.4.6-doubleref.patch
Group: Development/Debuggers
License: GPL

BuildRequires: socat

%description
Snoopy Logger, logs all the commands issued by local users on the system.
It is very useful to track and monitor the users.

%prep
%setup
%patch -p1
cat > %name <<@@@
#!/bin/sh
export LD_PRELOAD=%_libdir/libsnoopy.so
exec "\$@"
@@@

%build
%autoreconf
%configure --enable-config-file --enable-filter
%make

%install
%makeinstall_std DESTDIR=%buildroot
install -D -m755 %name %buildroot%_bindir/%name

%files
%doc ChangeLog README* doc
%_sysconfdir/*
%_sbindir/*
%_bindir/*
%_libdir/libsnoopy.so*

%check
make check

%changelog
* Thu Mar 22 2018 Fr. Br. George <george@altlinux.ru> 2.4.6-alt1
- Autobuild version bump to 2.4.6

* Wed Apr 22 2015 Fr. Br. George <george@altlinux.ru> 2.2.7-alt1
- Autobuild version bump to 2.2.7
- Fix build

* Mon Sep 29 2014 Fr. Br. George <george@altlinux.ru> 1.9.0-alt1
- Autobuild version bump to 1.9.0

* Tue Feb 12 2013 Fr. Br. George <george@altlinux.ru> 1.8.1-alt1
- Autobuild version bump to 1.8.1

* Tue Feb 12 2013 Fr. Br. George <george@altlinux.ru> 0.0-alt1
- Initial zero version build

