Name: apt-blacklist
Version: 0.01
Release: alt2.3.1

Summary: Forbids installation of packages based on some criteria
License: GPLv3+
Group: System/Configuration/Packaging

BuildArch: noarch

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source0: %name-%version.tar

%description
This small tool checks packages that apt wants to install and aborts the
installation process if some criteria are met. Now it has only one
criterion: last changelog entry author must not contain lines from
%_sysconfdir/%name/packagers. Also, it can warn you when apt going to
install package that changed by author from %_sysconfdir/%name/warning
and inform about packager changes for authors from %_sysconfdir/%name/watch.

%prep
%setup

%install
mkdir -p %buildroot{%_bindir,%_sysconfdir/%name}
install -p -m755 %name %buildroot%_bindir/
touch %buildroot%_sysconfdir/%name/packagers
touch %buildroot%_sysconfdir/%name/warning
touch %buildroot%_sysconfdir/%name/watch
install -pD -m644 apt.conf %buildroot/etc/apt/apt.conf.d/10-%name.conf

%files
%_bindir/*
%config(noreplace) /etc/apt/apt.conf.d/*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/packagers
%config(noreplace) %_sysconfdir/%name/warning
%config(noreplace) %_sysconfdir/%name/watch

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.01-alt2.3.1
- Rebuild with Python-2.7

* Fri Mar 26 2010 Terechkov Evgenii <evg@altlinux.ru> 0.01-alt2.3
- Fix new package installation (with just one changelog entry)

* Sat Mar 20 2010 Terechkov Evgenii <evg@altlinux.ru> 0.01-alt2.2
- Watching for packager change added (#23182)

* Mon Dec 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.01-alt2.1
- Rebuilt with python 2.6

* Fri Oct 09 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.01-alt2
- Sisyphus build

* Sun Sep 13 2009 Terechkov Evgenii <evg@altlinux.ru> 0.01-alt1.1
- Warn list support added

* Sat Sep 12 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.01-alt1
- initial version
