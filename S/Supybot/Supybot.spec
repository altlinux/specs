Name: Supybot
Version: 0.83.4.1
Release: alt1.1.1

Summary: IRC bot written in Python
License: BSD
Group: Networking/IRC

Url: http://supybot.sourceforge.net/

BuildArch: noarch

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

# some plugins were merged
Conflicts: Supybot-plugins  < 20060723-alt4 
Conflicts: python-module-supybot-plugins < 20060723-alt4

%setup_python_module supybot
%add_python_req_skip _winreg
%py_requires dateutil feedparser sqlite

%description
Supybot is a flexible IRC bot written in python.
It features many plugins, is easy to extend and to use.

To run it, just use supybot-wizard to create the configuration file.

%prep
%setup
%patch -p1

# simplejson
rm -rf plugins/Google/local/
# feedparser
rm -rf plugins/RSS/local/
# dateutil
rm -rf plugins/Time/local/

%build
%python_build

%install
%python_install
mkdir -p %buildroot%_man1dir
cp -a docs/man/* %buildroot%_man1dir
rm -rf docs/man/

%files
%_bindir/*
%python_sitelibdir/supybot/
%python_sitelibdir/*.egg-info
%_mandir/man?/*
%doc ACKS LICENSE README RELNOTES ChangeLog docs/
#%%doc sandbox/Debug/

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.83.4.1-alt1.1.1
- Rebuild with Python-2.7

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.83.4.1-alt1.1
- Rebuilt with python 2.6

* Mon May 25 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.83.4.1-alt1
- 0.83.4.1

* Thu May 21 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.83.4-alt1
- 0.83.4
- remove local copies of modules already present in Sisyphus

* Sat Feb 21 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.83.3-alt2
- package as noarch
- use %%python_{build,install}
- package directories along with files
- add Packager

* Wed Oct 24 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.83.3-alt1
- 0.83.3

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.83.2-alt1.1
- Rebuilt using rpm-build-python-0.29-alt4.

* Mon Jul 24 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.83.2-alt1
- 0.83.2

* Thu Apr 06 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.83.1-alt3
- add buildrequires
- add RusNet NickServ support

* Tue Apr 04 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.83.1-alt2
- move -data to separate package
- apply minor fixes from Debian

* Sun Apr 02 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.83.1-alt1
- initial build
