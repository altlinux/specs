# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define origname TwistedCore
%define major 20.3
%define prefx3 python3-module-twisted

Name: python3-module-twisted-core
Version: %major.0
Release: alt3

Summary: An asynchronous networking framework written in Python

Group: Development/Python3
License: MIT
Url: http://twistedmatrix.com/trac/wiki/TwistedCore

# Source-url: https://twistedmatrix.com/Releases/Twisted/%major/Twisted-%version.tar.bz2
Source: %name-%version.tar
Source1: README.ALT-ru_RU.UTF-8

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-zope.interface python3-module-incremental

Requires: %prefx3-logger = %EVR
Obsoletes: %prefx3-lore <= %EVR
Provides: %prefx3-lore = %EVR
#py3_provides lore
Requires: python3-module-OpenSSL
#Requires: python3-module-autobahn

%add_python3_req_skip AppKit Carbon Foundation GDK PAM cfsupport
%add_python3_req_skip kqsyscall msvcrt pythoncom pywintypes win32api
%add_python3_req_skip win32com win32event win32file win32gui win32pipe
%add_python3_req_skip win32process win32security win32con CFNetwork
%add_python3_req_skip CoreFoundation
%add_python3_req_skip win32com.shell

%description
An extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

It is expected that one day the project will expanded to the point
that the framework will seamlessly integrate with mail, web, DNS,
netnews, IRC, RDBMSs, desktop environments, and your toaster.

%package -n twisted-core-tools
Summary: Tools for Twisted Core (Python 3)
Group: Development/Python3
Requires: %name = %EVR
Conflicts: python-module-twisted-core

%description -n twisted-core-tools
Tools for Twisted Core.


%package -n %prefx3-core-gui
Summary: GUI for Twisted Core (Python 3)
Group: Development/Python3
Requires: %name = %EVR
####add_python_req_skip pyui wx wxPython gtk Tkinter gnome tkFileDialog tkMessageBox tkSimpleDialog
%add_python3_req_skip pyui gtk

%description -n %prefx3-core-gui
GUI for Twisted Core

%package -n %prefx3-core-gui-wx
Summary: GUI for Twisted Core (wxWidgets) (Python 3)
Group: Development/Python3
Requires: %name = %EVR

%description -n %prefx3-core-gui-wx
GUI for Twisted Core (wxWidgets)

%package -n %prefx3-core-gui-tk
Summary: GUI for Twisted Core (TK) (Python 3)
Group: Development/Python3
Requires: python3-module-twisted-core-gui = %EVR
Requires: %name = %EVR

%description -n %prefx3-core-gui-tk
GUI for Twisted Core (TK)

%package -n %prefx3-core-gui-gnome
Summary: GUI for Twisted Core (Gnome) (Python 3)
Group: Development/Python3
Requires: python3-module-twisted-core-gui = %EVR

%description -n %prefx3-core-gui-gnome
GUI for Twisted Core (Gnome)

%package -n %prefx3-core-doc
Summary: Documentation for Twisted Core (Python 3)
Group: Documentation
BuildArch: noarch
Requires: python3-module-twisted-core = %version-%release

%description -n %prefx3-core-doc
Documentation for Twisted Core.

%package -n %prefx3-core-zsh
Summary: Tab completion for Zsh and Twisted Core
Group: Shells
Requires: python3-module-twisted-core = %version-%release
Requires: zsh

%description -n %prefx3-core-zsh
Tab completions for Zsh and Twisted Core.

%package -n %prefx3-news
Summary: Twisted News is an NNTP server and programming library (Python 3)
Group: Development/Python3
Requires: %prefx3-core = %EVR
Requires: %prefx3-mail = %EVR

%description -n %prefx3-news
Twisted is an event-based framework for internet applications.

Twisted News is an NNTP protocol (Usenet) programming library. The
library contains server and client protocol implementations. A simple
NNTP server is also provided.

%package -n %prefx3-lore
Summary: Twisted documentation system (Python 3)
Group: Development/Python3
Requires: %prefx3-core = %EVR
Requires: %prefx3-web = %EVR

%description -n %prefx3-lore
Twisted is an event-based framework for internet applications.

Lore is a complete documentation system based on XHTML and can generate
documentation into other formats such as PDF, HTML.

%package -n %prefx3-runner
Summary: Twisted Runner process management library and inetd replacement (Python 3)
Group: Development/Python3
Requires: %prefx3-core = %EVR

%description -n %prefx3-runner
Twisted is an event-based framework for internet applications.

Twisted Runner contains code useful for persistent process management
with Python and Twisted, and has an almost full replacement for inetd.

%package -n %prefx3-mail
Summary: A Twisted Mail library, server and client (Python 3)
Group: Development/Python3
Requires: %prefx3-core = %EVR
Requires: %prefx3-names = %EVR
Conflicts: python-module-twisted-core-mail

%description -n %prefx3-mail
Twisted is an event-based framework for internet applications.

Twisted Mail contains high-level, efficient protocol implementations
for both clients and servers of SMTP, POP3, and IMAP4. Additionally,
it contains an "out of the box" combination SMTP/POP3 virtual-hosting
mail server. Also included is a read/write Maildir implementation and
a basic Mail Exchange calculator.

%package -n %prefx3-web
Summary: Twisted web server, programmable in Python 3
Group: Development/Python3
%add_python3_req_skip Tkinter

%description -n %prefx3-web
Twisted is an event-based framework for internet applications.

Twisted Web is a complete web server, aimed at hosting web
applications using Twisted and Python, but fully able to serve static
pages, also.

%package -n %prefx3-conch
Summary: Twisted SSHv2 implementation (Python 3)
Group: Development/Python3
Requires: %prefx3-core
Conflicts: python-module-twisted-core-conch

%description -n %prefx3-conch
Twisted is an event-based framework for internet applications.

Conch is an SSHv2 implementation written in Python. SSH is a protocol designed
to allow remote access to shells and commands, but it is generic enough to
allow everything from TCP forwarding to generic filesystem access. Since conch
is written in Python, it interfaces well with other Python projects, such as
Imagination. Conch also includes a implementations of the telnet and vt102
protocols, as well as support for rudamentary line editing behaviors. A new
implementation of Twisted's Manhole application is also included, featuring
server-side input history and interactive syntax coloring.

%package -n %prefx3-conch-gui
Summary: GUI for Twisted Conch (Python 3)
Group: Development/Python3
Requires: %prefx3-conch = %version-%release

%description -n %prefx3-conch-gui
GUI for Twisted Conch

%package -n %prefx3-names
Summary: A Twisted DNS implementation (Python 3)
Group: Development/Python3
Requires: %prefx3-core = %EVR

%description -n %prefx3-names
Twisted is an event-based framework for internet applications.

Twisted Names is both a domain name server as well as a client
resolver library. Twisted Names comes with an "out of the box"
nameserver which can read most BIND-syntax zone files as well as a
simple Python-based configuration format. Twisted Names can act as an
authoritative server, perform zone transfers from a master to act as a
secondary, act as a caching nameserver, or any combination of
these. Twisted Names' client resolver library provides functions to
query for all commonly used record types as well as a replacement for
the blocking gethostbyname() function provided by the Python stdlib
socket module.

%package -n %prefx3-words
Summary: Twisted Words contains Instant Messaging implementations (Python 3)
Group: Development/Python3
Requires: %prefx3-core = %EVR
%add_python3_req_skip java javax

%description -n %prefx3-words
Twisted is an event-based framework for internet applications.

Twisted Words contains implementations of many Instant Messaging
protocols, including IRC, Jabber, MSN, OSCAR (AIM & ICQ), TOC (AOL),
and some functionality for creating bots, inter-protocol gateways, and
a client application for many of the protocols.

In support of Jabber, Twisted Words also contains X-ish, a library for
processing XML with Twisted and Python, with support for a Pythonic DOM and
an XPath-like toolkit.

%package -n %prefx3-pair
Summary: Low-level networking transports and utilities (Python 3)
Group: Development/Python3
Requires: %prefx3-core
%add_python3_req_skip eunuchs

%description -n %prefx3-pair
Twisted is an event-based framework for internet applications.

Twisted Pair: The framework of your ethernet.
Low-level networking transports and utilities.

%package -n %prefx3-positioning
Summary: The Twisted positioning framework (Python 3)
Group: Development/Python3
Requires: %prefx3-core = %EVR

%description -n %prefx3-positioning
Twisted is an event-based framework for internet applications.

The Twisted positioning framework.

%package -n %prefx3-logger
Summary: Classes and functions to do granular logging (Python 3)
Group: Development/Python3
Requires: %prefx3-core = %EVR

%description -n %prefx3-logger
Twisted is an event-based framework for internet applications.

This package contains classes and functions to do granular logging.

%package -n %prefx3-core-tests
Summary: Unit tests for Twisted Core (Python 3)
Group: Development/Python3
Requires: python3-module-twisted-core = %EVR
Provides: python3-module-twisted-core-test = %EVR
Obsoletes: python3-module-twisted-core-test
Conflicts: python-module-twisted-core-test
%add_python3_req_skip idonotexist

%description -n %prefx3-core-tests
Unit tests for Twisted Core.


%prep
%setup

%build
%python3_build

# README.ALT
cp %SOURCE1 README.ALT-ru_RU.UTF-8

%install
%python3_install

# cfsupport is support for MacOSX Core Foundations, so we can delete it
rm -rf %buildroot%python3_sitelibdir/twisted/internet/cfsupport

# iocpreactor is a win32 reactor, so we can delete it
rm -rf %buildroot%python3_sitelibdir/twisted/internet/iocpreactor

# Man pages
mkdir -p %buildroot%_man1dir/
cp -a docs/core/man/*.1 docs/mail/man/*.1 \
	docs/conch/man/*.1 \
	%buildroot%_man1dir/

rm -rfv docs/core/man docs/lore/man docs/mail/man docs/conch/man \
	docs/words/man

ln -s trial %buildroot%_bindir/trial-3

%check

%files -n twisted-core-tools
%_bindir/twist
%_bindir/twistd
%_bindir/pyhtmlizer
%_man1dir/pyhtmlizer.1*
%_man1dir/twistd.1*

%files
%doc LICENSE NEWS.rst README.rst
%doc README.ALT-ru_RU.UTF-8
%python3_sitelibdir/Twisted*.egg-info
%dir %python3_sitelibdir/twisted/
%python3_sitelibdir/twisted/*.py
%python3_sitelibdir/twisted/__pycache__/
%python3_sitelibdir/twisted/python/_pydoctortemplates/

%python3_sitelibdir/twisted/application/
%exclude %python3_sitelibdir/twisted/application/test/
%exclude %python3_sitelibdir/twisted/application/twist/test/
%exclude %python3_sitelibdir/twisted/application/runner/test/
%python3_sitelibdir/twisted/cred/
%exclude %python3_sitelibdir/twisted/cred/test/
%python3_sitelibdir/twisted/_threads/
%exclude %python3_sitelibdir/twisted/_threads/test/
%python3_sitelibdir/twisted/enterprise/
%python3_sitelibdir/twisted/internet/
%exclude %python3_sitelibdir/twisted/internet/testing.py
%exclude %python3_sitelibdir/twisted/internet/test
%exclude %python3_sitelibdir/twisted/internet/wxreactor.py
%exclude %python3_sitelibdir/twisted/internet/__pycache__/wxreactor.*
%exclude %python3_sitelibdir/twisted/internet/wxsupport.py
%exclude %python3_sitelibdir/twisted/internet/__pycache__/wxsupport.*

%python3_sitelibdir/twisted/persisted/
%exclude %python3_sitelibdir/twisted/persisted/test

%dir %python3_sitelibdir/twisted/plugins/
%python3_sitelibdir/twisted/plugins/*.py*
%python3_sitelibdir/twisted/plugins/__pycache__/
%exclude %python3_sitelibdir/twisted/plugins/twisted_trial.py
%exclude %python3_sitelibdir/twisted/plugins/__pycache__/twisted_trial.*
%exclude %python3_sitelibdir/twisted/plugins/twisted_conch.py
%exclude %python3_sitelibdir/twisted/plugins/__pycache__/twisted_conch*
%exclude %python3_sitelibdir/twisted/plugins/twisted_web.py
%exclude %python3_sitelibdir/twisted/plugins/__pycache__/twisted_web.*

%dir %python3_sitelibdir/twisted/protocols/
%python3_sitelibdir/twisted/protocols/*.py*
%python3_sitelibdir/twisted/protocols/__pycache__/

%python3_sitelibdir/twisted/protocols/haproxy/
%exclude %python3_sitelibdir/twisted/protocols/haproxy/test/

%dir %python3_sitelibdir/twisted/python/
%python3_sitelibdir/twisted/python/*.py*
%python3_sitelibdir/twisted/python/__pycache__/
%exclude %python3_sitelibdir/twisted/python/_setup.py


%python3_sitelibdir/twisted/scripts/
%exclude %python3_sitelibdir/twisted/scripts/test
%exclude %python3_sitelibdir/twisted/scripts/trial.py
%exclude %python3_sitelibdir/twisted/scripts/__pycache__/trial.*

%dir %python3_sitelibdir/twisted/spread/
%python3_sitelibdir/twisted/spread/*.py
%python3_sitelibdir/twisted/spread/__pycache__/

%python3_sitelibdir/twisted/tap/


%files -n %prefx3-core-doc
%doc docs/core

%files -n %prefx3-core-gui
#python3_sitelibdir/twisted/internet/pyuisupport.py*
#python3_sitelibdir/twisted/internet/gtk2reactor.py*
#python3_sitelibdir/twisted/internet/glib2reactor.py*

%files -n %prefx3-core-gui-wx
%python3_sitelibdir/twisted/internet/wxreactor.py
%python3_sitelibdir/twisted/internet/__pycache__/wxreactor.*
%python3_sitelibdir/twisted/internet/wxsupport.py
%python3_sitelibdir/twisted/internet/__pycache__/wxsupport.*

%files -n %prefx3-core-gui-tk
#python3_sitelibdir/twisted/internet/tksupport.py*

%files -n %prefx3-core-zsh
%python3_sitelibdir/twisted/python/twisted-completion.zsh


%files -n %prefx3-news
#python3_sitelibdir/twisted/news/
#exclude %python3_sitelibdir/twisted/news/test
#python3_sitelibdir/twisted/plugins/twisted_news.py*

%files -n %prefx3-runner
%python3_sitelibdir/twisted/runner/
%exclude %python3_sitelibdir/twisted/runner/test

%files -n %prefx3-mail
%doc docs/mail/*
%_bindir/mailmail
%_man1dir/mailmail.1*
%python3_sitelibdir/twisted/mail/
%exclude %python3_sitelibdir/twisted/mail/test

%files -n %prefx3-web
%doc docs/web/*
%python3_sitelibdir/twisted/web
%python3_sitelibdir/twisted/plugins/twisted_web.py
%python3_sitelibdir/twisted/plugins/__pycache__/twisted_web.*
%exclude %python3_sitelibdir/twisted/web/test

%files -n %prefx3-conch
%doc docs/conch/*
%_bindir/cftp
%_bindir/ckeygen
%_bindir/conch
%_bindir/tkconch
%_man1dir/cftp.1*
%_man1dir/ckeygen.1*
%_man1dir/conch.1*
%_man1dir/tkconch.1*
%python3_sitelibdir/twisted/conch/
%python3_sitelibdir/twisted/plugins/twisted_conch.py
%python3_sitelibdir/twisted/plugins/__pycache__/twisted_conch.*
%exclude %python3_sitelibdir/twisted/conch/ui
%exclude %python3_sitelibdir/twisted/conch/scripts/tkconch.py
%exclude %python3_sitelibdir/twisted/conch/scripts/__pycache__/tkconch.*

%exclude %python3_sitelibdir/twisted/conch/test

%files -n %prefx3-conch-gui
%python3_sitelibdir/twisted/conch/ui
%python3_sitelibdir/twisted/conch/scripts/tkconch.py
%python3_sitelibdir/twisted/conch/scripts/__pycache__/tkconch.*

%files -n %prefx3-names
%doc docs/names/*
%python3_sitelibdir/twisted/names/
%exclude %python3_sitelibdir/twisted/names/test

%files -n %prefx3-words
%doc docs/words/*
%python3_sitelibdir/twisted/words/
%exclude %python3_sitelibdir/twisted/words/test

%files -n %prefx3-pair
%doc docs/pair/*
%python3_sitelibdir/twisted/pair/
%exclude %python3_sitelibdir/twisted/pair/test

%files -n %prefx3-positioning
%python3_sitelibdir/twisted/positioning/
%exclude %python3_sitelibdir/twisted/positioning/test

%files -n %prefx3-logger
%python3_sitelibdir/twisted/logger/
%exclude %python3_sitelibdir/twisted/logger/test

%files -n %prefx3-core-tests
%_bindir/trial
%_bindir/trial-3
%_man1dir/trial.1*
%python3_sitelibdir/twisted/trial/
%python3_sitelibdir/twisted/test
%python3_sitelibdir/twisted/python/test
%python3_sitelibdir/twisted/scripts/test
%python3_sitelibdir/twisted/internet/testing.py
%python3_sitelibdir/twisted/internet/test
%python3_sitelibdir/twisted/protocols/test
%python3_sitelibdir/twisted/protocols/haproxy/test
%python3_sitelibdir/twisted/plugins/twisted_trial.py
%python3_sitelibdir/twisted/plugins/__pycache__/twisted_trial.*
%python3_sitelibdir/twisted/scripts/trial.py
%python3_sitelibdir/twisted/scripts/__pycache__/trial.*
%python3_sitelibdir/twisted/application/test
%python3_sitelibdir/twisted/application/runner/test/
%python3_sitelibdir/twisted/application/twist/test
%python3_sitelibdir/twisted/runner/test
%python3_sitelibdir/twisted/web/test
%python3_sitelibdir/twisted/conch/test
%python3_sitelibdir/twisted/names/test
%python3_sitelibdir/twisted/pair/test
%python3_sitelibdir/twisted/cred/test
%python3_sitelibdir/twisted/_threads/test
%python3_sitelibdir/twisted/persisted/test
%python3_sitelibdir/twisted/positioning/test
%python3_sitelibdir/twisted/spread/test
%python3_sitelibdir/twisted/logger/test
%python3_sitelibdir/twisted/python/_setup.py

%changelog
* Mon Oct 25 2021 Igor Vlasenko <viy@altlinux.org> 20.3.0-alt3
- NMU: added trial-3 compat symlink

* Mon Nov 09 2020 Vitaly Lipatov <lav@altlinux.ru> 20.3.0-alt2
- pack tools to twisted-core-tools (ALT bug 39226)
- fix tests packing (no more tests package requires from the packages)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 20.3.0-alt1
- new version 20.3.0 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 18.9.0-alt2
- build python3 package separately

* Mon Apr 08 2019 Grigory Ustinov <grenka@altlinux.org> 18.9.0-alt1
- Build new version for python3.7.

* Sat Aug 25 2018 Anton Midyukov <antohami@altlinux.org> 18.7.0-alt1
- new version (18.7.0) with rpmgs script

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 17.5.0-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 17.5.0-alt2
- Enabled python-3 build.
- Cleaned up the spec.

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 17.5.0-alt1
- new version (17.5.0) with rpmgs script

* Thu Aug 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 15.3.0-alt1
- Version 15.3.0
- Added requirement on logger for core (ALT #31188)

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 15.2.1-alt1
- Version 15.2.1

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.0.2-alt1
- Version 14.0.2

* Wed Jul 30 2014 Vladimir Didenko <cow@altlinux.org> 14.0.0-alt2
- rebuild with new pyOpenSSL

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.0.0-alt1
- Version 14.0.0

* Mon May 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 13.2.0-alt2
- Avoid requirement on python-devel for %name

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 13.2.0-alt1
- Version 13.2.0

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 13.1.0-alt1
- Version 13.1.0

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 13.0.0-alt1
- Version 13.0.0

* Mon Sep 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 12.2.0-alt1
- Version 12.2.0

* Wed Apr 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 12.0.0-alt1
- Version 12.0.0

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 11.1.0-alt2.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Jan 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11.1.0-alt2
- Moved all tests into tests package

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11.1.0-alt1
- Version 11.1.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 11.0.0-alt2.1
- Rebuild with Python-2.7

* Wed Sep 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11.0.0-alt2
- Moved all tests into tests package

* Tue Sep 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11.0.0-alt1
- Version 11.0.0 (ALT #26336)

* Mon Mar 21 2011 Sergey Alembekov <rt@altlinux.ru> 10.1.0-alt6
- /usr/bin/trial needs  twisted/scripts/trial.py. enable in for test
  subpackage

* Wed Sep 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.1.0-alt5
- Moved trials into test subpackage

* Mon Aug 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.1.0-alt4
- Extracted packages: gui-wx, gui-tk and gui-gnome (ALT #23853)
- Moved all tests into test package

* Wed Aug 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.1.0-alt3
- Moved all tests into test package

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.1.0-alt2
- Set doc package as noarch

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.1.0-alt1
- Version 10.1.0 (ALT #23065)

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.2.0-alt1.1
- Rebuilt with python 2.6

* Tue Sep 01 2009 Sergey Alembekov <rt@altlinux.ru> 8.2.0-alt1
 - versioning policy change
 - python-2.6 ready

* Mon Feb 11 2008 Sergey Alembekov <rt@altlinux.ru> 2.5.0-alt2.2
 - added forgotten _epoll.so

* Tue Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.5.0-alt2.1
 - Rebuilt with python-2.5.

* Tue Nov 06 2007 Sergey Alembekov <rt@altlinux.ru> 2.5.0-alt2
 - skip_requires for GUI libs which is using Tkinter, gtk and wx
 - add README.ALT-ru_RU.UTF-8

* Thu Mar 29 2007 Sergey Alembekov <rt@altlinux.ru> 2.5.0-alt1
 - Build for new upstream version

