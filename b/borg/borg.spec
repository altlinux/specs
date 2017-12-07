Name: borg
Version: 1.1.3
Release: alt1

Summary: Deduplicating backup program with compression and authenticated encryption

License: BSD like
Group: File tools
Url: https://borgbackup.github.io/borgbackup/

# Source-url: https://github.com/borgbackup/borg/archive/0.24.0.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# Automatically added by buildreq on Fri Aug 14 2015
# optimized out: i586-libcrypto10  libssl-devel python-base python-module-distribute python-module-oslo.i18n python-module-oslo.utils python3 python3-base python3-dev python3-module-BeautifulSoup python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cssselect python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-invoke python3-module-jinja2 python3-module-jsonschema python3-module-matplotlib python3-module-numpy python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-xstatic python3-module-xstatic-term.js python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zope python3-module-zope.interface
BuildRequires: libacl-devel ipython3 python3-module-Cython libssl-devel python3-dev
BuildRequires: liblz4-devel python3-module-setuptools_scm
# python3-module-html5lib

Requires: python3-module-msgpack >= 0.4.6
Requires: python3-module-zmq

%description
BorgBackup (short: Borg) is a deduplicating backup program.
Optionally, it supports compression and authenticated encryption.

The main goal of Borg is to provide an efficient and secure way to backup data.
The data deduplication technique used makes Borg suitable for daily backups
since only changes are stored.

The authenticated encryption technique makes it suitable for backups to not
fully trusted targets.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%files
%doc LICENSE AUTHORS CHANGES.rst README.rst
%_bindir/borg
%_bindir/borgfs
%python3_sitelibdir/*

%changelog
* Thu Dec 07 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.3-alt1
- update version to 1.1.3

* Fri Nov 17 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.2-alt1
- update version to 1.1.2

* Mon Oct 30 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.1-alt1
- update version to 1.1.1

* Sat Oct 14 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.0-alt2
- update version to 1.1.0

* Tue Oct 03 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.0-alt1.rc4
- update version to 1.1.0rc4

* Tue Sep 19 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.0-alt1.rc3
- update version to 1.1.0rc3

* Mon Aug 28 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.0-alt1.rc2
- update version to 1.1.0rc2

* Tue Aug 15 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.0-alt1.rc1
- update version to 1.1.0rc1

* Fri Aug 05 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- new version 1.0.6 (with rpmrb script)

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- new version 1.0.5 (with rpmrb script)

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.24.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Aug 14 2015 Vitaly Lipatov <lav@altlinux.ru> 0.24.0-alt1
- initial build for ALT Linux Sisyphus
