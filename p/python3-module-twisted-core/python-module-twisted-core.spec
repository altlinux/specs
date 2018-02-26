%define origname TwistedCore
%define oname twisted-core

%define prefx python3-module-twisted
Name: %prefx-core
Version: 11.1.0
Release: alt1.hg20120216
Summary: An asynchronous networking framework written in Python 3

Group: Development/Python3
License: MIT
Url: http://twistedmatrix.com/trac/wiki/TwistedCore
# hg clone https://bitbucket.org/pitrou/t3k
Source: %origname-%version.tar.bz2
Source1: README.ALT-ru_RU.UTF-8
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
Requires: python3-module-OpenSSL

%add_python3_req_skip AppKit Carbon Foundation GDK PAM cfsupport
%add_python3_req_skip kqsyscall msvcrt pythoncom pywintypes win32api
%add_python3_req_skip win32com win32event win32file win32gui win32pipe
%add_python3_req_skip win32process win32security win32con CFNetwork
%add_python3_req_skip CoreFoundation

%description
An extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

It is expected that one day the project will expanded to the point
that the framework will seamlessly integrate with mail, web, DNS,
netnews, IRC, RDBMSs, desktop environments, and your toaster.

%package gui
Summary: GUI for Twisted Core (Python 3)
Group: Development/Python3
Requires: python3-module-twisted-core = %version-%release
####add_python_req_skip pyui wx wxPython gtk Tkinter gnome tkFileDialog tkMessageBox tkSimpleDialog
%add_python3_req_skip pyui gtk

%description gui
GUI for Twisted Core

%package gui-wx
Summary: GUI for Twisted Core (wxWidgets) (Python 3)
Group: Development/Python3
Requires: python3-module-twisted-core-gui = %version-%release

%description gui-wx
GUI for Twisted Core (wxWidgets)

%package gui-tk
Summary: GUI for Twisted Core (TK) (Python 3)
Group: Development/Python3
Requires: python3-module-twisted-core-gui = %version-%release

%description gui-tk
GUI for Twisted Core (TK)

%package gui-gnome
Summary: GUI for Twisted Core (Gnome) (Python 3)
Group: Development/Python3
Requires: python3-module-twisted-core-gui = %version-%release

%description gui-gnome
GUI for Twisted Core (Gnome)

%package doc
Summary: Documentation for Twisted Core (Python 3)
Group: Documentation
BuildArch: noarch
Requires: python3-module-twisted-core = %version-%release

%description doc
Documentation for Twisted Core.

%package zsh
Summary: Tab completion for Zsh and Twisted Core
Group: Shells
Requires: python3-module-twisted-core = %version-%release
Requires: zsh

%description zsh
Tab completions for Zsh and Twisted Core.

%package test
Summary: Unit tests for Twisted Core (Python 3)
Group: Development/Python3
Requires: python3-module-twisted-core = %version-%release
%add_python3_req_skip idonotexist
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
Summary: Twisted News is an NNTP server and programming library (Python 3)
Group: Development/Python3
Requires: %name
Requires: %prefx-mail

%description -n %prefx-news
Twisted is an event-based framework for internet applications.

Twisted News is an NNTP protocol (Usenet) programming library. The
library contains server and client protocol implementations. A simple
NNTP server is also provided.

%package -n %prefx-lore
Summary: Twisted documentation system (Python 3)
Group: Development/Python3
Requires: %name
Requires: %prefx-web

%description -n %prefx-lore
Twisted is an event-based framework for internet applications.

Lore is a complete documentation system based on XHTML and can generate
documentation into other formats such as PDF, HTML.

%package -n %prefx-runner
Summary: Twisted Runner process management library and inetd replacement (Python 3)
Group: Development/Python3
Requires: %name

%description -n %prefx-runner
Twisted is an event-based framework for internet applications.

Twisted Runner contains code useful for persistent process management
with Python and Twisted, and has an almost full replacement for inetd.

%package -n %prefx-mail
Summary: A Twisted Mail library, server and client (Python 3)
Group: Development/Python3
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
Summary: Twisted web server, programmable in Python 3
Group: Development/Python3
%add_python3_req_skip Tkinter

%description -n %prefx-web
Twisted is an event-based framework for internet applications.

Twisted Web is a complete web server, aimed at hosting web
applications using Twisted and Python, but fully able to serve static
pages, also.

%package -n %prefx-conch
Summary: Twisted SSHv2 implementation (Python 3)
Group: Development/Python3
Requires: %name
Requires: python3-module-Crypto

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
Summary: GUI for Twisted Conch (Python 3)
Group: Development/Python3
Requires: %prefx-conch = %version-%release

%description -n %prefx-conch-gui
GUI for Twisted Conch

%package -n %prefx-names
Summary: A Twisted DNS implementation (Python 3)
Group: Development/Python3
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
Summary: Twisted Words contains Instant Messaging implementations (Python 3)
Group: Development/Python3
Requires: %name
%add_python3_req_skip java javax

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
Summary: Low-level networking transports and utilities (Python 3)
Group: Development/Python3
Requires: %name
%add_python3_req_skip eunuchs

%description -n %prefx-pair
Twisted is an event-based framework for internet applications.

Twisted Pair: The framework of your ethernet.
Low-level networking transports and utilities.

%prep
%setup -n %origname-%version

# Generate a brief README.zsh
awk '/^Zsh Notes:/,/^Have fun!/' twisted/python/zshcomp.py > README.zsh

%build
%python3_build

# README.ALT
#install -p -m 644 -D %SOURCE1 %buildroot/%_docdir/README.ALT-ru_RU.UTF-8
cp %SOURCE1 README.ALT-ru_RU.UTF-8

%install
%python3_install

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd

# cfsupport is support for MacOSX Core Foundations, so we can delete it
rm -rf %buildroot%python3_sitelibdir/twisted/internet/cfsupport

# iocpreactor is a win32 reactor, so we can delete it
rm -rf %buildroot%python3_sitelibdir/twisted/internet/iocpreactor

# Man pages
#mkdir -p %buildroot%_man1dir/
#cp -a doc/core/man/*.1 doc/lore/man/*.1 doc/mail/man/*.1 \
#	doc/conch/man/*.1 \
#	%buildroot%_man1dir/
rm -rf doc/core/man doc/lore/man doc/mail/man doc/conch/man \
	doc/words/man

# Zsh tab complete stub
#mkdir -p %buildroot%_datadir/zsh/Completion/Python
#sed 's#python -c#python -c#g' < twisted/python/_twisted_zsh_stub > _twisted_zsh_stub.MOD
#install -m 644 _twisted_zsh_stub.MOD %buildroot%_datadir/zsh/Completion/Python/_twisted_zsh_stub
#rm -Rf twisted/python/_twisted_zsh_stub

touch %buildroot%python3_sitelibdir/twisted/trial/__init__.py

%files
%doc LICENSE NEWS README
%doc README.ALT-ru_RU.UTF-8
%doc %python3_sitelibdir/twisted/topfiles
%_bindir/manhole3
%_bindir/tap2deb3
%_bindir/tap2rpm3
%_bindir/tapconvert3
#_bindir/mktap3
%_bindir/twistd3
%_bindir/pyhtmlizer3

#_man1dir/*
#exclude %_man1dir/lore.1*
#exclude %_man1dir/cftp.1*
#exclude %_man1dir/ckeygen.1*
#exclude %_man1dir/conch.1*
#exclude %_man1dir/tkconch.1*
#exclude %_man1dir/im.1*
#exclude %_man1dir/mailmail.1*

%python3_sitelibdir/Twisted*.egg-info
%dir %python3_sitelibdir/twisted/
%python3_sitelibdir/twisted/*.py*
%python3_sitelibdir/twisted/python/*.c
%python3_sitelibdir/twisted/python/__pycache__
%python3_sitelibdir/twisted/__pycache__
#python3_sitelibdir/twisted/protocols/_c_urlarg.c

%python3_sitelibdir/twisted/application/
%exclude %python3_sitelibdir/twisted/application/test
%python3_sitelibdir/twisted/cred/
%python3_sitelibdir/twisted/enterprise/
%python3_sitelibdir/twisted/internet/
%exclude %python3_sitelibdir/twisted/internet/test
%exclude %python3_sitelibdir/twisted/internet/pyuisupport.py*
%exclude %python3_sitelibdir/twisted/internet/wxreactor.py*
%exclude %python3_sitelibdir/twisted/internet/wxsupport.py*
%exclude %python3_sitelibdir/twisted/internet/gtk2reactor.py*
%exclude %python3_sitelibdir/twisted/internet/glib2reactor.py*
%exclude %python3_sitelibdir/twisted/internet/gtkreactor.py*
%exclude %python3_sitelibdir/twisted/internet/tksupport.py*

%dir %python3_sitelibdir/twisted/manhole/
%python3_sitelibdir/twisted/manhole/*.py*
%python3_sitelibdir/twisted/manhole/__pycache__
%exclude %python3_sitelibdir/twisted/manhole/gladereactor.py*
%exclude %python3_sitelibdir/twisted/manhole/_inspectro.py*

%python3_sitelibdir/twisted/persisted/
%exclude %python3_sitelibdir/twisted/persisted/test

%dir %python3_sitelibdir/twisted/plugins/
%python3_sitelibdir/twisted/plugins/*.py*
%python3_sitelibdir/twisted/plugins/__pycache__
%exclude %python3_sitelibdir/twisted/plugins/twisted_trial.py*
%exclude %python3_sitelibdir/twisted/plugins/twisted_news.py*
%exclude %python3_sitelibdir/twisted/plugins/twisted_lore.py*
%exclude %python3_sitelibdir/twisted/plugins/twisted_runner.py*
%exclude %python3_sitelibdir/twisted/plugins/twisted_mail.py*
%exclude %python3_sitelibdir/twisted/plugins/twisted_conch.py*
%exclude %python3_sitelibdir/twisted/plugins/twisted_words.py*
%exclude %python3_sitelibdir/twisted/plugins/twisted_web.py*
%exclude %python3_sitelibdir/twisted/plugins/twisted_names.py*

%dir %python3_sitelibdir/twisted/protocols/
%python3_sitelibdir/twisted/protocols/*.py*
%python3_sitelibdir/twisted/protocols/__pycache__
#python3_sitelibdir/twisted/protocols/*.so

%python3_sitelibdir/twisted/protocols/gps/
%python3_sitelibdir/twisted/protocols/mice/

%dir %python3_sitelibdir/twisted/python/
%python3_sitelibdir/twisted/python/*.py*
%python3_sitelibdir/twisted/python/*.so

%dir %python3_sitelibdir/twisted/python/zsh/
%python3_sitelibdir/twisted/python/zsh/README.txt
%python3_sitelibdir/twisted/python/zsh/_*

%python3_sitelibdir/twisted/scripts/
%exclude %python3_sitelibdir/twisted/scripts/test
%exclude %python3_sitelibdir/twisted/scripts/tkunzip.py*
%exclude %python3_sitelibdir/twisted/scripts/trial.py*

%dir %python3_sitelibdir/twisted/spread/
%python3_sitelibdir/twisted/spread/*.py*
%python3_sitelibdir/twisted/spread/__pycache__

%python3_sitelibdir/twisted/tap/


%files doc
%doc doc/core doc/fun doc/historic

%files gui
%python3_sitelibdir/twisted/internet/pyuisupport.py*
%python3_sitelibdir/twisted/internet/gtk2reactor.py*
%python3_sitelibdir/twisted/internet/glib2reactor.py*
%python3_sitelibdir/twisted/internet/gtkreactor.py*
%dir %python3_sitelibdir/twisted/manhole/ui
%python3_sitelibdir/twisted/manhole/ui/*
%exclude %python3_sitelibdir/twisted/manhole/ui/test
%python3_sitelibdir/twisted/manhole/*.glade
%exclude %python3_sitelibdir/twisted/manhole/inspectro.glade
%python3_sitelibdir/twisted/manhole/gladereactor.py*

%dir %python3_sitelibdir/twisted/spread/ui/
%python3_sitelibdir/twisted/spread/ui/*.py*
%python3_sitelibdir/twisted/spread/ui/__pycache__
%exclude %python3_sitelibdir/twisted/spread/ui/tkutil.py*
%exclude %python3_sitelibdir/twisted/spread/ui/tktree.py*
%python3_sitelibdir/twisted/spread/ui/*.glade

#files gui-wx
#python3_sitelibdir/twisted/internet/wxreactor.py*
#python3_sitelibdir/twisted/internet/wxsupport.py*

#files gui-gnome
#python3_sitelibdir/twisted/manhole/inspectro.glade
#python3_sitelibdir/twisted/manhole/_inspectro.py*

%files gui-tk
%python3_sitelibdir/twisted/internet/tksupport.py*
%python3_sitelibdir/twisted/spread/ui/tkutil.py*
%python3_sitelibdir/twisted/spread/ui/tktree.py*
%python3_sitelibdir/twisted/scripts/tkunzip.py*

%files zsh
%doc README.zsh
#_datadir/zsh/Completion/Python/_twisted_zsh_stub
#python3_sitelibdir/twisted/python/_twisted_zsh_stub
%python3_sitelibdir/twisted/python/twisted-completion.zsh

%files test
%_bindir/trial3
%python3_sitelibdir/twisted/test
%python3_sitelibdir/twisted/manhole/ui/test
%python3_sitelibdir/twisted/manhole/test
%python3_sitelibdir/twisted/python/test
%python3_sitelibdir/twisted/scripts/test
%python3_sitelibdir/twisted/internet/test
%python3_sitelibdir/twisted/protocols/test
%python3_sitelibdir/twisted/trial
%python3_sitelibdir/twisted/plugins/twisted_trial.py*
%python3_sitelibdir/twisted/scripts/trial.py*
%python3_sitelibdir/twisted/application/test
%python3_sitelibdir/twisted/news/test
%python3_sitelibdir/twisted/lore/test
%python3_sitelibdir/twisted/runner/test
%python3_sitelibdir/twisted/mail/test
%python3_sitelibdir/twisted/web/test
%python3_sitelibdir/twisted/conch/test
%python3_sitelibdir/twisted/names/test
%python3_sitelibdir/twisted/pair/test
%python3_sitelibdir/twisted/persisted/test

%files -n %prefx-news
%python3_sitelibdir/twisted/news/
%exclude %python3_sitelibdir/twisted/news/test
%python3_sitelibdir/twisted/plugins/twisted_news.py*

%files -n %prefx-lore
%doc doc/lore/*
%_bindir/lore3
#_man1dir/lore.1*
%python3_sitelibdir/twisted/lore/
%exclude %python3_sitelibdir/twisted/lore/test
%python3_sitelibdir/twisted/plugins/twisted_lore.py*

%files -n %prefx-runner
%python3_sitelibdir/twisted/runner/
%exclude %python3_sitelibdir/twisted/runner/test
%python3_sitelibdir/twisted/plugins/twisted_runner.py*

%files -n %prefx-mail
%doc doc/mail/*
%_bindir/mailmail3
%python3_sitelibdir/twisted/mail/
%exclude %python3_sitelibdir/twisted/mail/test
%python3_sitelibdir/twisted/plugins/twisted_mail.py*
#_man1dir/mailmail.1*

%files -n %prefx-web
%doc doc/web/*
%python3_sitelibdir/twisted/web
%python3_sitelibdir/twisted/plugins/twisted_web.py*
# There are no SOAPpy in ALT Linux Sisyphus - remove it support
%exclude %python3_sitelibdir/twisted/web/soap.py*
%exclude %python3_sitelibdir/twisted/web/test

%files -n %prefx-conch
%doc doc/conch/*
%_bindir/cftp3
%_bindir/ckeygen3
%_bindir/conch3
%_bindir/tkconch3
#_man1dir/cftp.1*
#_man1dir/ckeygen.1*
#_man1dir/conch.1*
#_man1dir/tkconch.1*
%python3_sitelibdir/twisted/conch/
%python3_sitelibdir/twisted/plugins/twisted_conch.py*
%exclude %python3_sitelibdir/twisted/conch/ui
%exclude %python3_sitelibdir/twisted/conch/scripts/tkconch.py
%exclude %python3_sitelibdir/twisted/conch/test

%files -n %prefx-conch-gui
%python3_sitelibdir/twisted/conch/ui
%python3_sitelibdir/twisted/conch/scripts/tkconch.py

%files -n %prefx-names
%doc doc/names/*
%python3_sitelibdir/twisted/names/
%exclude %python3_sitelibdir/twisted/names/test
%python3_sitelibdir/twisted/plugins/twisted_names.py*

%files -n %prefx-words
%doc doc/words/*
#_man1dir/im.1*
%python3_sitelibdir/twisted/words/
%exclude %python3_sitelibdir/twisted/words/test
%python3_sitelibdir/twisted/plugins/twisted_words.py*

%files -n %prefx-pair
%doc doc/pair/*
%python3_sitelibdir/twisted/pair/
%exclude %python3_sitelibdir/twisted/pair/test

%changelog
* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11.1.0-alt1.hg20120216
- Built for Python 3

