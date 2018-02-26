Name: python-module-supybot-plugins
Version: 20060723
Release: alt4.1.1

Summary: IRC bot written in Python - additional plugins
License: BSD
Group: Networking/IRC

Url: http://supybot.sf.net/

BuildArch: noarch

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source0: %name-%version.tar
Source1: %name-%version-setup.py

Provides: Supybot-plugins = %version-%release
Obsoletes: Supybot-plugins

BuildPreReq: python-devel

%description
Supybot is a flexible IRC bot written in python.
It features many plugins, is easy to extend and to use.

This package contains additional official plugins.

%prep
%setup
install -m644 %SOURCE1 setup.py

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/supybot/plugins/
%python_sitelibdir/*.egg-info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20060723-alt4.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20060723-alt4.1
- Rebuilt with python 2.6

* Thu May 21 2009 Andrey Rahmatullin <wrar@altlinux.ru> 20060723-alt4
- remove plugins included in Supybot 0.83.4

* Sat Feb 21 2009 Andrey Rahmatullin <wrar@altlinux.ru> 20060723-alt3
- rename to python-module-supybot-plugins
- package as noarch
- use %%python_install
- package directories along with files
- fix Url
- add Packager

* Mon Aug 25 2008 Andrey Rahmatullin <wrar@altlinux.ru> 20060723-alt2
- package readme files

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 20060723-alt1.1
- Rebuilt with python-2.5.

* Mon Jul 24 2006 Andrey Rahmatullin <wrar@altlinux.ru> 20060723-alt1
- 20060723

* Tue May 02 2006 Andrey Rahmatullin <wrar@altlinux.ru> 20050830-alt1
- initial build
