Name: python-module-supybot-plugins-Dicebot
Version: 0.5
Release: alt1.1

Summary: IRC bot written in Python - Dicebot plugin
License: BSD
Group: Networking/IRC
Url: http://www.assembla.com/spaces/supybot-plugin-Dicebot

BuildArch: noarch

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

Provides: Supybot-plugin-Dicebot = %version-%release
Obsoletes: Supybot-plugin-Dicebot

BuildPreReq: python-devel Supybot

%description
Supybot is a flexible IRC bot written in python.
It features many plugins, is easy to extend and to use.

This package contains a plugin for rolling dices in D&D style.

%prep
%setup
%patch -p1

%build
%python_build

%install
%python_install

%check
supybot-test --no-network --plugins-dir=%buildroot%python_sitelibdir/supybot/plugins

%files
%python_sitelibdir/supybot/plugins/Dicebot/
%python_sitelibdir/*.egg-info
%doc docs/*.txt

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.1
- Rebuild with Python-2.7

* Sat Feb 13 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.5-alt1
- 0.5

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt3.1
- Rebuilt with python 2.6

* Sat Sep 19 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.4-alt3
- re-enable autoreq
- move tests to %%check section

* Sat Feb 21 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.4-alt2
- rename to python-module-supybot-plugins-Dicebot
- package as noarch
- use %%python_{build,install}
- package directories along with files

* Sun Dec 21 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.4-alt1
- 0.4
- disable broken autoreq

* Sat Sep 13 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt1
- 0.3

* Tue Aug 26 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt1
- 0.2

* Sat Aug 11 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.1-alt1
- initial
