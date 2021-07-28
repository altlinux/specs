Name:          python3-module-pyinotify
Version:       0.9.6
Release:       alt3

Summary:       Monitor filesystem events with Python under Linux

License:       MIT
Group:         Development/Python3
URL:           https://github.com/seb-m/pyinotify

# https://github.com/seb-m/pyinotify.git
Source0:       %name-%version.tar
Source2:       py3inotify

BuildRequires(pre): rpm-build-python3

BuildArch:     noarch

Provides:      python3-module-inotify = %version-%release
%py3_provides pyinotify

%description
This is a Python module for watching filesystems changes. pyinotify
can be used for various kind of fs monitoring. pyinotify relies on a
recent Linux Kernel feature (merged in kernel 2.6.13) called
inotify. inotify is an event-driven notifier, its notifications are
exported from kernel space to user space.

%package       examples
Summary:       Examples for Python inotify module
Group:         Development/Python
Requires:      python-module-inotify = %version-%release

%description   examples
This package includes some examples usage of the Python inotify module.

%prep
%setup

%build
%python3_build

%install
%python3_install
install -D -m 0755 -p %SOURCE2 %buildroot%_bindir/py3inotify

%files
%doc ACKS COPYING README.md
%_bindir/py3inotify
%python3_sitelibdir_noarch/*

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.6-alt3
- Drop python2 support.

* Sat Feb 08 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.6-alt2
- run scripts via python2

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.4-alt1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1
- Version 0.9.4

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.9.2-alt4.1
- Rebuild with Python-3.3

* Thu Jan 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt4
- add python3 module build

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt3
- Rebuild with Python-2.7

* Thu Sep 29 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt2
- merge python-module-inotify and python-module-pyinotify packages

* Wed Sep 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt1
- 0.9.2 build on Fedora spec

* Mon Sep 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.0-alt1
- 0.9.0 (ALT #23991)

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt1head.1
- Rebuilt with python 2.6

* Fri May 22 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.6-alt1head
- new version from HEAD (fix bug #20123)

* Sat Feb 21 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt2
- build as noarch

* Sun Jan 25 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- new version 0.8.1 (with rpmrb script)

* Sun May 11 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.0q-alt1
- initial build for ALT Linux Sisyphus
