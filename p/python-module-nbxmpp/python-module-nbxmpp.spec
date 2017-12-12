%global modname nbxmpp
Name: python-module-%modname
Version: 0.6.1
Release: alt1
Summary: Python library for non-blocking use of Jabber/XMPP
License: GPLv3
Url: https://python-nbxmpp.gajim.org/
Group: Development/Python

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: https://python-nbxmpp.gajim.org/downloads/%modname-%version.tar.gz
BuildArch: noarch
BuildRequires: python-devel
Requires: python-module-OpenSSL
Requires: python-module-pygobject
Requires: python-module-kerberos

%description
python-nbxmpp is a Python library that provides a way for Python applications
to use Jabber/XMPP networks in a non-blocking way.

Features:
- Asynchronous
- ANONYMOUS, EXTERNAL, GSSAPI, SCRAM-SHA-1, DIGEST-MD5, PLAIN, and
    X-MESSENGER-OAUTH2 authentication mechanisms.
- Connection via proxies
- TLS
- BOSH (XEP-0124)
- Stream Management (XEP-0198)

%package doc
Summary: Developer documentation for %name
Group: Development/Python

%description doc
python-nbxmpp is a Python library that provides a way for Python applications
to use Jabber/XMPP networks in a non-blocking way.

This sub-package contains the developer documentation for python-nbxmpp.

%prep
%setup -n %modname-%version

%build
# let's have no executable files in doc/
find doc/ -type f -perm /111 -exec chmod -x {} +
%__python setup.py build

%install
%__python setup.py install -O1 --skip-build --root %buildroot

%files
%doc COPYING README ChangeLog
%python_sitelibdir_noarch/%modname
%python_sitelibdir_noarch/%modname-%version-*.egg-info

%files doc
%doc COPYING doc/*

%changelog
* Tue Dec 12 2017 Ilya Mashkin <oddity@altlinux.ru> 0.6.1-alt1
- 0.6.1 (Closes: #34321)

* Sat Dec 09 2017 Ilya Mashkin <oddity@altlinux.ru> 0.5.6-alt1
- 0.5.6

* Sat Feb 18 2017 Ilya Mashkin <oddity@altlinux.ru> 0.5.5-alt1
- 0.5.5

* Sat Sep 12 2015 Ilya Mashkin <oddity@altlinux.ru> 0.5.3-alt1
- 0.5.3

* Tue Apr 17 2014 Ilya Mashkin <oddity@altlinux.ru> 0.4-alt1
- Build for Sisyphus

* Wed Mar 19 2014 Michal Schmidt <mschmidt@redhat.com> - 0.4-1
- Initial Fedora packaging.
