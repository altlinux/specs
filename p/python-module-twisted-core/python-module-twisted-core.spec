%define origname TwistedCore

%define prefx python-module-twisted
Name: %prefx-core
Version: 12.0.0
Release: alt1
%setup_python_module twisted-core
Summary: An asynchronous networking framework written in Python

Group: Development/Python
License: MIT
Url: http://twistedmatrix.com/trac/wiki/TwistedCore
Source: http://tmrc.mit.edu/mirror/twisted/Core/10.1/%origname-%version.tar.bz2
Source1: README.ALT-ru_RU.UTF-8

BuildRequires: python-devel python-modules-compiler
Requires: python-module-OpenSSL

Conflicts: %name-core < %version-%release

%add_python_req_skip AppKit Carbon Foundation GDK PAM cfsupport
%add_python_req_skip kqsyscall msvcrt pythoncom pywintypes win32api
%add_python_req_skip win32com win32event win32file win32gui win32pipe
%add_python_req_skip win32process win32security win32con CFNetwork
%add_python_req_skip CoreFoundation

%description
An extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

It is expected that one day the project will expanded to the point
that the framework will seamlessly integrate with mail, web, DNS,
netnews, IRC, RDBMSs, desktop environments, and your toaster.

%package gui
Summary: GUI for Twisted Core
Group: Development/Python
Requires: python-module-twisted-core = %version-%release
####add_python_req_skip pyui wx wxPython gtk Tkinter gnome tkFileDialog tkMessageBox tkSimpleDialog
%add_python_req_skip pyui

%description gui
GUI for Twisted Core

%package gui-wx
Summary: GUI for Twisted Core (wxWidgets)
Group: Development/Python
Requires: python-module-twisted-core-gui = %version-%release

%description gui-wx
GUI for Twisted Core (wxWidgets)

%package gui-tk
Summary: GUI for Twisted Core (TK)
Group: Development/Python
Requires: python-module-twisted-core-gui = %version-%release

%description gui-tk
GUI for Twisted Core (TK)

%package gui-gnome
Summary: GUI for Twisted Core (Gnome)
Group: Development/Python
Requires: python-module-twisted-core-gui = %version-%release

%description gui-gnome
GUI for Twisted Core (Gnome)

%package doc
Summary: Documentation for Twisted Core
Group: Documentation
BuildArch: noarch
Requires: python-module-twisted-core = %version-%release

%description doc
Documentation for Twisted Core.

%package zsh
Summary: Tab completion for Zsh and Twisted Core
Group: Shells
Requires: python-module-twisted-core = %version-%release
Requires: zsh

%description zsh
Tab completions for Zsh and Twisted Core.

%package test
Summary: Unit tests for Twisted Core
Group: Development/Python
Requires: python-module-twisted-core = %version-%release
AutoReqProv: nopython
Obsoletes: %prefx-news-tests
Obsoletes: %prefx-lore-tests
Obsoletes: %prefx-runner-tests
Obsoletes: %prefx-mail-tests
Obsoletes: %prefx-web-tests
Obsoletes: %prefx-conch-tests
Obsoletes: %prefx-names-tests
Obsoletes: %prefx-words-tests

%description test
Unit tests for Twisted Core.

%package -n %prefx-news
Summary: Twisted News is an NNTP server and programming library
Group: Development/Python
Requires: %name
Requires: %prefx-mail

%description -n %prefx-news
Twisted is an event-based framework for internet applications.

Twisted News is an NNTP protocol (Usenet) programming library. The
library contains server and client protocol implementations. A simple
NNTP server is also provided.

%package -n %prefx-lore
Summary: Twisted documentation system
Group: Development/Python
Requires: %name
Requires: %prefx-web

%description -n %prefx-lore
Twisted is an event-based framework for internet applications.

Lore is a complete documentation system based on XHTML and can generate
documentation into other formats such as PDF, HTML.

%package -n %prefx-runner
Summary: Twisted Runner process management library and inetd replacement
Group: Development/Python
Requires: %name

%description -n %prefx-runner
Twisted is an event-based framework for internet applications.

Twisted Runner contains code useful for persistent process management
with Python and Twisted, and has an almost full replacement for inetd.

%package -n %prefx-mail
Summary: A Twisted Mail library, server and client
Group: Development/Python
Requires: %name
Requires: %prefx-names

%description -n %prefx-mail
Twisted is an event-based framework for internet applications.

Twisted Mail contains high-level, efficient protocol implementations
for both clients and servers of SMTP, POP3, and IMAP4. Additionally,
it contains an "out of the box" combination SMTP/POP3 virtual-hosting
mail server. Also included is a read/write Maildir implementation and
a basic Mail Exchange calculator.

%package -n %prefx-web
Summary: Twisted web server, programmable in Python
Group: Development/Python
%add_python_req_skip Tkinter

%description -n %prefx-web
Twisted is an event-based framework for internet applications.

Twisted Web is a complete web server, aimed at hosting web
applications using Twisted and Python, but fully able to serve static
pages, also.

%package -n %prefx-conch
Summary: Twisted SSHv2 implementation
Group: Development/Python
Requires: %name
Requires: python-module-Crypto

%description -n %prefx-conch
Twisted is an event-based framework for internet applications.

Conch is an SSHv2 implementation written in Python. SSH is a protocol designed
to allow remote access to shells and commands, but it is generic enough to
allow everything from TCP forwarding to generic filesystem access. Since conch
is written in Python, it interfaces well with other Python projects, such as
Imagination. Conch also includes a implementations of the telnet and vt102
protocols, as well as support for rudamentary line editing behaviors. A new
implementation of Twisted's Manhole application is also included, featuring
server-side input history and interactive syntax coloring.

%package -n %prefx-conch-gui
Summary: GUI for Twisted Conch
Group: Development/Python
Requires: %prefx-conch = %version-%release

%description -n %prefx-conch-gui
GUI for Twisted Conch

%package -n %prefx-names
Summary: A Twisted DNS implementation
Group: Development/Python
Requires: %name

%description -n %prefx-names
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

%package -n %prefx-words
Summary: Twisted Words contains Instant Messaging implementations
Group: Development/Python
Requires: %name
%add_python_req_skip java javax

%description -n %prefx-words
Twisted is an event-based framework for internet applications.

Twisted Words contains implementations of many Instant Messaging
protocols, including IRC, Jabber, MSN, OSCAR (AIM & ICQ), TOC (AOL),
and some functionality for creating bots, inter-protocol gateways, and
a client application for many of the protocols.

In support of Jabber, Twisted Words also contains X-ish, a library for
processing XML with Twisted and Python, with support for a Pythonic DOM and
an XPath-like toolkit.

%package -n %prefx-pair
Summary: Low-level networking transports and utilities
Group: Development/Python
Requires: %name

%description -n %prefx-pair
Twisted is an event-based framework for internet applications.

Twisted Pair: The framework of your ethernet.
Low-level networking transports and utilities.

%prep
%setup -n %origname-%version

# Generate a brief README.zsh
awk '/^Zsh Notes:/,/^Have fun!/' twisted/python/zshcomp.py > README.zsh

%build
%python_build

# README.ALT
#install -p -m 644 -D %SOURCE1 %buildroot/%_docdir/README.ALT-ru_RU.UTF-8
cp %SOURCE1 README.ALT-ru_RU.UTF-8

%install
%python_install

# cfsupport is support for MacOSX Core Foundations, so we can delete it
rm -rf %buildroot%python_sitelibdir/twisted/internet/cfsupport

# iocpreactor is a win32 reactor, so we can delete it
rm -rf %buildroot%python_sitelibdir/twisted/internet/iocpreactor

# Man pages
mkdir -p %buildroot%_man1dir/
cp -a doc/core/man/*.1 doc/lore/man/*.1 doc/mail/man/*.1 \
	doc/conch/man/*.1 \
	%buildroot%_man1dir/
rm -rf doc/core/man doc/lore/man doc/mail/man doc/conch/man \
	doc/words/man

# Zsh tab complete stub
#mkdir -p %buildroot%_datadir/zsh/Completion/Python
#sed 's#python -c#python -c#g' < twisted/python/_twisted_zsh_stub > _twisted_zsh_stub.MOD
#install -m 644 _twisted_zsh_stub.MOD %buildroot%_datadir/zsh/Completion/Python/_twisted_zsh_stub
#rm -Rf twisted/python/_twisted_zsh_stub

touch %buildroot%python_sitelibdir/twisted/trial/__init__.py

%files
%doc LICENSE NEWS README
%doc README.ALT-ru_RU.UTF-8
%doc %python_sitelibdir/twisted/topfiles
%_bindir/manhole
%_bindir/tap2deb
%_bindir/tap2rpm
%_bindir/tapconvert
#_bindir/mktap
%_bindir/twistd
%_bindir/pyhtmlizer

%_man1dir/*
%exclude %_man1dir/lore.1*
%exclude %_man1dir/cftp.1*
%exclude %_man1dir/ckeygen.1*
%exclude %_man1dir/conch.1*
%exclude %_man1dir/tkconch.1*
#exclude %_man1dir/im.1*
%exclude %_man1dir/mailmail.1*

%python_sitelibdir/Twisted*.egg-info
%dir %python_sitelibdir/twisted/
%python_sitelibdir/twisted/*.py*
%python_sitelibdir/twisted/python/*.c
#python_sitelibdir/twisted/protocols/_c_urlarg.c

%python_sitelibdir/twisted/application/
%exclude %python_sitelibdir/twisted/application/test
%python_sitelibdir/twisted/cred/
%python_sitelibdir/twisted/enterprise/
%python_sitelibdir/twisted/internet/
%exclude %python_sitelibdir/twisted/internet/test
%exclude %python_sitelibdir/twisted/internet/pyuisupport.py*
%exclude %python_sitelibdir/twisted/internet/wxreactor.py*
%exclude %python_sitelibdir/twisted/internet/wxsupport.py*
%exclude %python_sitelibdir/twisted/internet/gtk2reactor.py*
%exclude %python_sitelibdir/twisted/internet/glib2reactor.py*
%exclude %python_sitelibdir/twisted/internet/gtkreactor.py*
%exclude %python_sitelibdir/twisted/internet/tksupport.py*

%dir %python_sitelibdir/twisted/manhole/
%python_sitelibdir/twisted/manhole/*.py*
%exclude %python_sitelibdir/twisted/manhole/gladereactor.py*
%exclude %python_sitelibdir/twisted/manhole/_inspectro.py*

%python_sitelibdir/twisted/persisted/
%exclude %python_sitelibdir/twisted/persisted/test

%dir %python_sitelibdir/twisted/plugins/
%python_sitelibdir/twisted/plugins/*.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_trial.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_news.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_lore.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_runner.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_mail.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_conch.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_words.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_web.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_names.py*

%dir %python_sitelibdir/twisted/protocols/
%python_sitelibdir/twisted/protocols/*.py*
#python_sitelibdir/twisted/protocols/*.so

%python_sitelibdir/twisted/protocols/gps/
%python_sitelibdir/twisted/protocols/mice/

%dir %python_sitelibdir/twisted/python/
%python_sitelibdir/twisted/python/*.py*
%python_sitelibdir/twisted/python/*.so

%dir %python_sitelibdir/twisted/python/zsh/
%python_sitelibdir/twisted/python/zsh/README.txt
%python_sitelibdir/twisted/python/zsh/_*

%python_sitelibdir/twisted/scripts/
%exclude %python_sitelibdir/twisted/scripts/test
%exclude %python_sitelibdir/twisted/scripts/tkunzip.py*
%exclude %python_sitelibdir/twisted/scripts/trial.py*

%dir %python_sitelibdir/twisted/spread/
%python_sitelibdir/twisted/spread/*.py*

%python_sitelibdir/twisted/tap/


%files doc
%doc doc/core doc/fun doc/historic

%files gui
%python_sitelibdir/twisted/internet/pyuisupport.py*
%python_sitelibdir/twisted/internet/gtk2reactor.py*
%python_sitelibdir/twisted/internet/glib2reactor.py*
%python_sitelibdir/twisted/internet/gtkreactor.py*
%dir %python_sitelibdir/twisted/manhole/ui
%python_sitelibdir/twisted/manhole/ui/*
%exclude %python_sitelibdir/twisted/manhole/ui/test
%python_sitelibdir/twisted/manhole/*.glade
%exclude %python_sitelibdir/twisted/manhole/inspectro.glade
%python_sitelibdir/twisted/manhole/gladereactor.py*

%dir %python_sitelibdir/twisted/spread/ui/
%python_sitelibdir/twisted/spread/ui/*.py*
%exclude %python_sitelibdir/twisted/spread/ui/tkutil.py*
%exclude %python_sitelibdir/twisted/spread/ui/tktree.py*
%python_sitelibdir/twisted/spread/ui/*.glade

%files gui-wx
%python_sitelibdir/twisted/internet/wxreactor.py*
%python_sitelibdir/twisted/internet/wxsupport.py*

%files gui-gnome
%python_sitelibdir/twisted/manhole/inspectro.glade
%python_sitelibdir/twisted/manhole/_inspectro.py*

%files gui-tk
%python_sitelibdir/twisted/internet/tksupport.py*
%python_sitelibdir/twisted/spread/ui/tkutil.py*
%python_sitelibdir/twisted/spread/ui/tktree.py*
%python_sitelibdir/twisted/scripts/tkunzip.py*

%files zsh
%defattr(-,root,root,-)
%doc README.zsh
#_datadir/zsh/Completion/Python/_twisted_zsh_stub
#python_sitelibdir/twisted/python/_twisted_zsh_stub
%python_sitelibdir/twisted/python/twisted-completion.zsh

%files test
%_bindir/trial
%python_sitelibdir/twisted/test
%python_sitelibdir/twisted/manhole/ui/test
%python_sitelibdir/twisted/manhole/test
%python_sitelibdir/twisted/python/test
%python_sitelibdir/twisted/scripts/test
%python_sitelibdir/twisted/internet/test
%python_sitelibdir/twisted/protocols/test
%python_sitelibdir/twisted/trial
%python_sitelibdir/twisted/plugins/twisted_trial.py*
%python_sitelibdir/twisted/scripts/trial.py*
%python_sitelibdir/twisted/application/test
%python_sitelibdir/twisted/news/test
%python_sitelibdir/twisted/lore/test
%python_sitelibdir/twisted/runner/test
%python_sitelibdir/twisted/mail/test
%python_sitelibdir/twisted/web/test
%python_sitelibdir/twisted/conch/test
%python_sitelibdir/twisted/names/test
%python_sitelibdir/twisted/pair/test
%python_sitelibdir/twisted/persisted/test

%files -n %prefx-news
%python_sitelibdir/twisted/news/
%exclude %python_sitelibdir/twisted/news/test
%python_sitelibdir/twisted/plugins/twisted_news.py*

%files -n %prefx-lore
%doc doc/lore/*
%_bindir/lore
%_man1dir/lore.1*
%python_sitelibdir/twisted/lore/
%exclude %python_sitelibdir/twisted/lore/test
%python_sitelibdir/twisted/plugins/twisted_lore.py*

%files -n %prefx-runner
%python_sitelibdir/twisted/runner/
%exclude %python_sitelibdir/twisted/runner/test
%python_sitelibdir/twisted/plugins/twisted_runner.py*

%files -n %prefx-mail
%doc doc/mail/*
%_bindir/mailmail
%python_sitelibdir/twisted/mail/
%exclude %python_sitelibdir/twisted/mail/test
%python_sitelibdir/twisted/plugins/twisted_mail.py*
%_man1dir/mailmail.1*

%files -n %prefx-web
%doc doc/web/*
%python_sitelibdir/twisted/web
%python_sitelibdir/twisted/plugins/twisted_web.py*
# There are no SOAPpy in ALT Linux Sisyphus - remove it support
%exclude %python_sitelibdir/twisted/web/soap.py*
%exclude %python_sitelibdir/twisted/web/test

%files -n %prefx-conch
%doc doc/conch/*
%_bindir/cftp
%_bindir/ckeygen
%_bindir/conch
%_bindir/tkconch
%_man1dir/cftp.1*
%_man1dir/ckeygen.1*
%_man1dir/conch.1*
%_man1dir/tkconch.1*
%python_sitelibdir/twisted/conch/
%python_sitelibdir/twisted/plugins/twisted_conch.py*
%exclude %python_sitelibdir/twisted/conch/ui
%exclude %python_sitelibdir/twisted/conch/scripts/tkconch.py
%exclude %python_sitelibdir/twisted/conch/test

%files -n %prefx-conch-gui
%python_sitelibdir/twisted/conch/ui
%python_sitelibdir/twisted/conch/scripts/tkconch.py

%files -n %prefx-names
%doc doc/names/*
%python_sitelibdir/twisted/names/
%exclude %python_sitelibdir/twisted/names/test
%python_sitelibdir/twisted/plugins/twisted_names.py*

%files -n %prefx-words
%doc doc/words/*
#_man1dir/im.1*
%python_sitelibdir/twisted/words/
%exclude %python_sitelibdir/twisted/words/test
%python_sitelibdir/twisted/plugins/twisted_words.py*

%files -n %prefx-pair
%doc doc/pair/*
%python_sitelibdir/twisted/pair/
%exclude %python_sitelibdir/twisted/pair/test

%changelog
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

