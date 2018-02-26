Name: python-module-supybot-plugins-ALTLinux
Version: 0.3.2
Release: alt1.1.1

Summary: IRC bot written in Python - ALTLinux plugin
License: BSD
Group: Networking/IRC
Url: http://altlinux.ru/

BuildArch: noarch

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source0: %name-%version.tar

Provides: Supybot-plugin-ALTLinux = %version-%release
Obsoletes: Supybot-plugin-ALTLinux

BuildPreReq: python-devel

%description
Supybot is a flexible IRC bot written in python.
It features many plugins, is easy to extend and to use.

This package contains a plugin for ALT Linux channels.


%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/supybot/plugins/ALTLinux/
%python_sitelibdir/*.egg-info


%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.1
- Rebuilt with python 2.6

* Sat Sep 19 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.3.2-alt1
- use inotify(7) instead of polling in the git.alt mail handler

* Wed Apr 29 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.3.1-alt1
- rewrite git.alt mail handler to fetch from a local mbox

* Sat Feb 21 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt2
- rename to python-module-supybot-plugins-ALTLinux
- package as noarch
- use %%python_{build,install}
- package directories along with files

* Fri Sep 26 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt1
- add git.alt repository list search

* Sun Sep 14 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt1
- add interaction with ALT Linux Bugzilla (search and bug info)

* Fri Sep 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.1.3-alt1
- second try to port to email module

* Thu Sep 11 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.1.2-alt1
- use email module instead of obsolete rfc822

* Sun Aug 24 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.1.1-alt1
- use X-git-URL instead of X-git-dir, process only packages/ dir (raorn@)

* Sat Apr 21 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.1-alt2
- print repo gitweb URL

* Wed Mar 07 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.1-alt1
- initial, based on Mailbox plugin

