%define origname TwistedCore
%define major 17.5

%def_with python3

%define prefx python-module-twisted
%define prefx3 python3-module-twisted
Name: %prefx-core
Version: %major.0
Release: alt2.1
%setup_python_module twisted-core
Summary: An asynchronous networking framework written in Python

Group: Development/Python
License: MIT
Url: http://twistedmatrix.com/trac/wiki/TwistedCore

# Source-url: https://twistedmatrix.com/Releases/Twisted/%major/Twisted-%version.tar.bz2
Source: %name-%version.tar
Source1: README.ALT-ru_RU.UTF-8

BuildRequires: python-devel python-modules-compiler python-module-setuptools
BuildPreReq: python-module-zope.interface python-module-incremental
BuildRequires: python-module-pydoctor
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-zope.interface python3-module-incremental
%endif

Requires: %prefx-logger = %EVR
Obsoletes: %prefx-lore <= %EVR
Provides: %prefx-lore = %EVR
%py_provides lore
Requires: python-module-OpenSSL

Conflicts: %name-core < %version-%release

%add_python_req_skip AppKit Carbon Foundation GDK PAM cfsupport
%add_python_req_skip kqsyscall msvcrt pythoncom pywintypes win32api
%add_python_req_skip win32com win32event win32file win32gui win32pipe
%add_python_req_skip win32process win32security win32con CFNetwork
%add_python_req_skip CoreFoundation distutils
%if_with python3
%add_python3_req_skip AppKit Carbon Foundation GDK PAM cfsupport
%add_python3_req_skip kqsyscall msvcrt pythoncom pywintypes win32api
%add_python3_req_skip win32com win32event win32file win32gui win32pipe
%add_python3_req_skip win32process win32security win32con CFNetwork
%add_python3_req_skip CoreFoundation
%endif

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
Provides: python-module-twisted-core-gui-gnome = %version-%release
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

%package -n %prefx-positioning
Summary: The Twisted positioning framework.
Group: Development/Python
Requires: %name

%description -n %prefx-positioning
Twisted is an event-based framework for internet applications.

The Twisted positioning framework.

%package -n %prefx-logger
Summary: Classes and functions to do granular logging
Group: Development/Python
Requires: %name

%description -n %prefx-logger
Twisted is an event-based framework for internet applications.

This package contains classes and functions to do granular logging.

%if_with python3
%package -n %prefx3-core
Summary: An asynchronous networking framework written in Python 3
Group: Development/Python3
Requires: python3-module-OpenSSL

%description -n %prefx3-core
An extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

It is expected that one day the project will expanded to the point
that the framework will seamlessly integrate with mail, web, DNS,
netnews, IRC, RDBMSs, desktop environments, and your toaster.

%package -n %prefx3-core-gui
Summary: GUI for Twisted Core (Python 3)
Group: Development/Python3
Requires: python3-module-twisted-core = %version-%release
####add_python_req_skip pyui wx wxPython gtk Tkinter gnome tkFileDialog tkMessageBox tkSimpleDialog
%add_python3_req_skip pyui gtk

%description -n %prefx3-core-gui
GUI for Twisted Core

%package -n %prefx3-core-gui-wx
Summary: GUI for Twisted Core (wxWidgets) (Python 3)
Group: Development/Python3
Requires: python3-module-twisted-core-gui = %version-%release

%description -n %prefx3-core-gui-wx
GUI for Twisted Core (wxWidgets)

%package -n %prefx3-core-gui-tk
Summary: GUI for Twisted Core (TK) (Python 3)
Group: Development/Python3
Requires: python3-module-twisted-core-gui = %version-%release

%description -n %prefx3-core-gui-tk
GUI for Twisted Core (TK)

%package -n %prefx3-core-gui-gnome
Summary: GUI for Twisted Core (Gnome) (Python 3)
Group: Development/Python3
Requires: python3-module-twisted-core-gui = %version-%release

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

%package -n %prefx3-core-test
Summary: Unit tests for Twisted Core (Python 3)
Group: Development/Python3
Requires: python3-module-twisted-core = %version-%release
%add_python3_req_skip idonotexist
AutoReqProv: nopython
Obsoletes: %prefx3-news-tests
Obsoletes: %prefx3-lore-tests
Obsoletes: %prefx3-runner-tests
Obsoletes: %prefx3-mail-tests
Obsoletes: %prefx3-web-tests
Obsoletes: %prefx3-conch-tests
Obsoletes: %prefx3-names-tests
Obsoletes: %prefx3-words-tests

%description -n %prefx3-core-test
Unit tests for Twisted Core.

%package -n %prefx3-news
Summary: Twisted News is an NNTP server and programming library (Python 3)
Group: Development/Python3
Requires: %prefx3-core
Requires: %prefx3-mail

%description -n %prefx3-news
Twisted is an event-based framework for internet applications.

Twisted News is an NNTP protocol (Usenet) programming library. The
library contains server and client protocol implementations. A simple
NNTP server is also provided.

%package -n %prefx3-lore
Summary: Twisted documentation system (Python 3)
Group: Development/Python3
Requires: %prefx3-core
Requires: %prefx3-web

%description -n %prefx3-lore
Twisted is an event-based framework for internet applications.

Lore is a complete documentation system based on XHTML and can generate
documentation into other formats such as PDF, HTML.

%package -n %prefx3-runner
Summary: Twisted Runner process management library and inetd replacement (Python 3)
Group: Development/Python3
Requires: %prefx3-core

%description -n %prefx3-runner
Twisted is an event-based framework for internet applications.

Twisted Runner contains code useful for persistent process management
with Python and Twisted, and has an almost full replacement for inetd.

%package -n %prefx3-mail
Summary: A Twisted Mail library, server and client (Python 3)
Group: Development/Python3
Requires: %prefx3-core
Requires: %prefx3-names

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
Requires: python3-module-Crypto

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
Requires: %prefx3-core

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
Requires: %prefx3-core
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
Requires: %prefx3-core

%description -n %prefx3-positioning
Twisted is an event-based framework for internet applications.

The Twisted positioning framework.

%package -n %prefx3-logger
Summary: Classes and functions to do granular logging (Python 3)
Group: Development/Python3
Requires: %prefx3-core

%description -n %prefx3-logger
Twisted is an event-based framework for internet applications.

This package contains classes and functions to do granular logging.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

# README.ALT
cp %SOURCE1 README.ALT-ru_RU.UTF-8

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}.py3
done
popd
%endif

%python_install

# cfsupport is support for MacOSX Core Foundations, so we can delete it
rm -rf %buildroot%python_sitelibdir/twisted/internet/cfsupport
rm -rf %buildroot%python3_sitelibdir/twisted/internet/cfsupport

# iocpreactor is a win32 reactor, so we can delete it
rm -rf %buildroot%python_sitelibdir/twisted/internet/iocpreactor
rm -rf %buildroot%python3_sitelibdir/twisted/internet/iocpreactor

# Man pages
mkdir -p %buildroot%_man1dir/
cp -a docs/core/man/*.1 docs/mail/man/*.1 \
	docs/conch/man/*.1 \
	%buildroot%_man1dir/
%if_with python3
pushd %buildroot%_man1dir
for i in *.1 ; do
	cp $i ${i%%.1}.py3.1
done
popd
%endif

rm -rf docs/core/man docs/lore/man docs/mail/man docs/conch/man \
	docs/words/man

touch %buildroot%python_sitelibdir/twisted/trial/__init__.py
touch %buildroot%python3_sitelibdir/twisted/trial/__init__.py

%check


%files
%doc LICENSE NEWS.rst README.rst
%doc README.ALT-ru_RU.UTF-8
%_bindir/twist
%_bindir/twistd
%_bindir/pyhtmlizer
%if_with python3
%exclude %_bindir/*.py3
%endif

%_man1dir/*
%exclude %_man1dir/cftp.1*
%exclude %_man1dir/ckeygen.1*
%exclude %_man1dir/conch.1*
%exclude %_man1dir/tkconch.1*
%exclude %_man1dir/mailmail.1*
%if_with python3
%exclude  %_man1dir/*.py3.1*
%endif

%python_sitelibdir/Twisted*.egg-info
%dir %python_sitelibdir/twisted/
%python_sitelibdir/twisted/*.py*
%python_sitelibdir/twisted/python/*.c
%python_sitelibdir/twisted/python/_pydoctortemplates/

%python_sitelibdir/twisted/application/
%exclude %python_sitelibdir/twisted/application/test
%python_sitelibdir/twisted/cred/
%python_sitelibdir/twisted/_threads/
%exclude %python_sitelibdir/twisted/_threads/test/
%python_sitelibdir/twisted/enterprise/
%python_sitelibdir/twisted/internet/
%exclude %python_sitelibdir/twisted/internet/test
%exclude %python_sitelibdir/twisted/internet/pyuisupport.py*
%exclude %python_sitelibdir/twisted/internet/wxreactor.py*
%exclude %python_sitelibdir/twisted/internet/wxsupport.py*
%exclude %python_sitelibdir/twisted/internet/gtk2reactor.py*
%exclude %python_sitelibdir/twisted/internet/glib2reactor.py*
%exclude %python_sitelibdir/twisted/internet/tksupport.py*

%python_sitelibdir/twisted/persisted/
%exclude %python_sitelibdir/twisted/persisted/test

%dir %python_sitelibdir/twisted/plugins/
%python_sitelibdir/twisted/plugins/*.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_trial.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_news.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_runner.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_mail.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_conch.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_words.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_web.py*
%exclude %python_sitelibdir/twisted/plugins/twisted_names.py*

%dir %python_sitelibdir/twisted/protocols/
%python_sitelibdir/twisted/protocols/*.py*

%python_sitelibdir/twisted/protocols/mice/
%python_sitelibdir/twisted/protocols/haproxy/
%exclude %python_sitelibdir/twisted/protocols/haproxy/test/

%dir %python_sitelibdir/twisted/python/
%python_sitelibdir/twisted/python/*.py*
%python_sitelibdir/twisted/python/*.so


%python_sitelibdir/twisted/scripts/
%exclude %python_sitelibdir/twisted/scripts/test
%exclude %python_sitelibdir/twisted/scripts/trial.py*

%dir %python_sitelibdir/twisted/spread/
%python_sitelibdir/twisted/spread/*.py*

%python_sitelibdir/twisted/tap/


%files doc
%doc docs/core

%files gui
%python_sitelibdir/twisted/internet/pyuisupport.py*
%python_sitelibdir/twisted/internet/gtk2reactor.py*
%python_sitelibdir/twisted/internet/glib2reactor.py*

%files gui-wx
%python_sitelibdir/twisted/internet/wxreactor.py*
%python_sitelibdir/twisted/internet/wxsupport.py*

%files gui-tk
%python_sitelibdir/twisted/internet/tksupport.py*

%files zsh
%python_sitelibdir/twisted/python/twisted-completion.zsh

%files test
%_bindir/trial
%python_sitelibdir/twisted/test
%python_sitelibdir/twisted/python/test
%python_sitelibdir/twisted/scripts/test
%python_sitelibdir/twisted/internet/test
%python_sitelibdir/twisted/protocols/test
%python_sitelibdir/twisted/protocols/haproxy/test
%python_sitelibdir/twisted/trial
%python_sitelibdir/twisted/plugins/twisted_trial.py*
%python_sitelibdir/twisted/scripts/trial.py*
%python_sitelibdir/twisted/application/test
%python_sitelibdir/twisted/news/test
%python_sitelibdir/twisted/runner/test
%python_sitelibdir/twisted/mail/test
%python_sitelibdir/twisted/web/test
%python_sitelibdir/twisted/conch/test
%python_sitelibdir/twisted/names/test
%python_sitelibdir/twisted/pair/test
%python_sitelibdir/twisted/_threads/test
%python_sitelibdir/twisted/persisted/test
%python_sitelibdir/twisted/positioning/test
%python_sitelibdir/twisted/spread/test
%python_sitelibdir/twisted/logger/test

%files -n %prefx-news
%python_sitelibdir/twisted/news/
%exclude %python_sitelibdir/twisted/news/test
%python_sitelibdir/twisted/plugins/twisted_news.py*

%files -n %prefx-runner
%python_sitelibdir/twisted/runner/
%exclude %python_sitelibdir/twisted/runner/test
%python_sitelibdir/twisted/plugins/twisted_runner.py*

%files -n %prefx-mail
%doc docs/mail/*
%_bindir/mailmail
%python_sitelibdir/twisted/mail/
%exclude %python_sitelibdir/twisted/mail/test
%python_sitelibdir/twisted/plugins/twisted_mail.py*
%_man1dir/mailmail.1*

%files -n %prefx-web
%doc docs/web/*
%python_sitelibdir/twisted/web
%python_sitelibdir/twisted/plugins/twisted_web.py*
# There are no SOAPpy in ALT Linux Sisyphus - remove it support
%exclude %python_sitelibdir/twisted/web/soap.py*
%exclude %python_sitelibdir/twisted/web/test

%files -n %prefx-conch
%doc docs/conch/*
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
%doc docs/names/*
%python_sitelibdir/twisted/names/
%exclude %python_sitelibdir/twisted/names/test
%python_sitelibdir/twisted/plugins/twisted_names.py*

%files -n %prefx-words
%doc docs/words/*
%python_sitelibdir/twisted/words/
%exclude %python_sitelibdir/twisted/words/test
%python_sitelibdir/twisted/plugins/twisted_words.py*

%files -n %prefx-pair
%doc docs/pair/*
%python_sitelibdir/twisted/pair/
%exclude %python_sitelibdir/twisted/pair/test

%files -n %prefx-positioning
%python_sitelibdir/twisted/positioning/
%exclude %python_sitelibdir/twisted/positioning/test

%files -n %prefx-logger
%python_sitelibdir/twisted/logger/
%exclude %python_sitelibdir/twisted/logger/test

%if_with python3
%files -n %prefx3-core
%doc LICENSE NEWS.rst README.rst
%doc README.ALT-ru_RU.UTF-8
%_bindir/twist.py3
%_bindir/twistd.py3
%_bindir/pyhtmlizer.py3

%_man1dir/*.py3.1.*
%exclude %_man1dir/cftp.py3.1*
%exclude %_man1dir/ckeygen.py3.1*
%exclude %_man1dir/conch.py3.1*
%exclude %_man1dir/tkconch.py3.1*
%exclude %_man1dir/mailmail.py3.1*

%python3_sitelibdir/Twisted*.egg-info
%dir %python3_sitelibdir/twisted/
%python3_sitelibdir/twisted/*.py*
%python3_sitelibdir/twisted/python/*.c
%python3_sitelibdir/twisted/python/_pydoctortemplates/

%python3_sitelibdir/twisted/application/
%exclude %python3_sitelibdir/twisted/application/test
%python3_sitelibdir/twisted/cred/
%python3_sitelibdir/twisted/_threads/
%exclude %python3_sitelibdir/twisted/_threads/test/
%python3_sitelibdir/twisted/enterprise/
%python3_sitelibdir/twisted/internet/
%exclude %python3_sitelibdir/twisted/internet/test
#exclude %python3_sitelibdir/twisted/internet/pyuisupport.py*
%exclude %python3_sitelibdir/twisted/internet/wxreactor.py*
%exclude %python3_sitelibdir/twisted/internet/wxsupport.py*
#exclude %python3_sitelibdir/twisted/internet/gtk2reactor.py*
#exclude %python3_sitelibdir/twisted/internet/glib2reactor.py*
#exclude %python3_sitelibdir/twisted/internet/tksupport.py*

%python3_sitelibdir/twisted/persisted/
%exclude %python3_sitelibdir/twisted/persisted/test

%dir %python3_sitelibdir/twisted/plugins/
%python3_sitelibdir/twisted/plugins/*.py*
%exclude %python3_sitelibdir/twisted/plugins/twisted_trial.py*
#exclude %python3_sitelibdir/twisted/plugins/twisted_news.py*
#exclude %python3_sitelibdir/twisted/plugins/twisted_runner.py*
#exclude %python3_sitelibdir/twisted/plugins/twisted_mail.py*
%exclude %python3_sitelibdir/twisted/plugins/twisted_conch.py*
#exclude %python3_sitelibdir/twisted/plugins/twisted_words.py*
%exclude %python3_sitelibdir/twisted/plugins/twisted_web.py*
#exclude %python3_sitelibdir/twisted/plugins/twisted_names.py*

%dir %python3_sitelibdir/twisted/protocols/
%python3_sitelibdir/twisted/protocols/*.py*

#python3_sitelibdir/twisted/protocols/mice/
%python3_sitelibdir/twisted/protocols/haproxy/
%exclude %python3_sitelibdir/twisted/protocols/haproxy/test/

%dir %python3_sitelibdir/twisted/python/
%python3_sitelibdir/twisted/python/*.py*
#python3_sitelibdir/twisted/python/*.so


%python3_sitelibdir/twisted/scripts/
%exclude %python3_sitelibdir/twisted/scripts/test
%exclude %python3_sitelibdir/twisted/scripts/trial.py*

%dir %python3_sitelibdir/twisted/spread/
%python3_sitelibdir/twisted/spread/*.py*

%python3_sitelibdir/twisted/tap/

%files -n %prefx3-core-doc
%doc docs/core

%files -n %prefx3-core-gui
#python3_sitelibdir/twisted/internet/pyuisupport.py*
#python3_sitelibdir/twisted/internet/gtk2reactor.py*
#python3_sitelibdir/twisted/internet/glib2reactor.py*

%files -n %prefx3-core-gui-wx
%python3_sitelibdir/twisted/internet/wxreactor.py*
%python3_sitelibdir/twisted/internet/wxsupport.py*

%files -n %prefx3-core-gui-tk
#python3_sitelibdir/twisted/internet/tksupport.py*

%files -n %prefx3-core-zsh
%python3_sitelibdir/twisted/python/twisted-completion.zsh

%files -n %prefx3-core-test
%_bindir/trial.py3
%python3_sitelibdir/twisted/test
%python3_sitelibdir/twisted/python/test
%python3_sitelibdir/twisted/scripts/test
%python3_sitelibdir/twisted/internet/test
%python3_sitelibdir/twisted/protocols/test
%python3_sitelibdir/twisted/protocols/haproxy/test
%python3_sitelibdir/twisted/trial
%python3_sitelibdir/twisted/plugins/twisted_trial.py*
%python3_sitelibdir/twisted/scripts/trial.py*
%python3_sitelibdir/twisted/application/test
#python3_sitelibdir/twisted/news/test
%python3_sitelibdir/twisted/runner/test
#python3_sitelibdir/twisted/mail/test
%python3_sitelibdir/twisted/web/test
%python3_sitelibdir/twisted/conch/test
%python3_sitelibdir/twisted/names/test
%python3_sitelibdir/twisted/pair/test
%python3_sitelibdir/twisted/_threads/test
%python3_sitelibdir/twisted/persisted/test
%python3_sitelibdir/twisted/positioning/test
%python3_sitelibdir/twisted/spread/test
%python3_sitelibdir/twisted/logger/test

%files -n %prefx3-news
#python3_sitelibdir/twisted/news/
#exclude %python3_sitelibdir/twisted/news/test
#python3_sitelibdir/twisted/plugins/twisted_news.py*

%files -n %prefx3-runner
%python3_sitelibdir/twisted/runner/
%exclude %python3_sitelibdir/twisted/runner/test
#python3_sitelibdir/twisted/plugins/twisted_runner.py*

%files -n %prefx3-mail
%doc docs/mail/*
#_bindir/mailmail.py3
%python3_sitelibdir/twisted/mail/
%exclude %python3_sitelibdir/twisted/mail/test
#python3_sitelibdir/twisted/plugins/twisted_mail.py*
#_man1dir/mailmail.py3.1*

%files -n %prefx3-web
%doc docs/web/*
%python3_sitelibdir/twisted/web
%python3_sitelibdir/twisted/plugins/twisted_web.py*
# There are no SOAPpy in ALT Linux Sisyphus - remove it support
#exclude %python3_sitelibdir/twisted/web/soap.py*
%exclude %python3_sitelibdir/twisted/web/test

%files -n %prefx3-conch
%doc docs/conch/*
%_bindir/cftp.py3
%_bindir/ckeygen.py3
%_bindir/conch.py3
%_bindir/tkconch.py3
%_man1dir/cftp.py3.1*
%_man1dir/ckeygen.py3.1*
%_man1dir/conch.py3.1*
%_man1dir/tkconch.py3.1*
%python3_sitelibdir/twisted/conch/
%python3_sitelibdir/twisted/plugins/twisted_conch.py*
%exclude %python3_sitelibdir/twisted/conch/ui
%exclude %python3_sitelibdir/twisted/conch/scripts/tkconch.py
%exclude %python3_sitelibdir/twisted/conch/test

%files -n %prefx3-conch-gui
%python3_sitelibdir/twisted/conch/ui
%python3_sitelibdir/twisted/conch/scripts/tkconch.py

%files -n %prefx3-names
%doc docs/names/*
%python3_sitelibdir/twisted/names/
%exclude %python3_sitelibdir/twisted/names/test
#python3_sitelibdir/twisted/plugins/twisted_names.py*

%files -n %prefx3-words
%doc docs/words/*
%python3_sitelibdir/twisted/words/
%exclude %python3_sitelibdir/twisted/words/test
#python3_sitelibdir/twisted/plugins/twisted_words.py*

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
%endif

%changelog
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

