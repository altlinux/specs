%define version 2.5.0
%define release alt2.2
%setup_python_module twisted

Name:           %{packagename}
Version:        %{version}
Release: %{release}

Summary:        Twisted is an event-based framework for internet applications

Group:          Development/Python
License:        MIT
URL:            http://www.twistedmatrix.com
Packager: Sergey Alembekov <rt@altlinux.ru>


Requires:       python-module-twisted-core
Requires:       python-module-twisted-conch
Requires:       python-module-twisted-lore
Requires:       python-module-twisted-mail
Requires:       python-module-twisted-names
Requires:       python-module-twisted-news
Requires:       python-module-twisted-runner
Requires:       python-module-twisted-web
Requires:       python-module-twisted-words
Requires:	python-modules-tkinter python-module-wx python-module-pygtk python-module-PyQt4
Obsoletes:      pythom-module-twisted < 2.5.0
Provides:       twisted = %{version}-%{release}
BuildArch: noarch

%description
Twisted is an event-based framework for internet applications.  It includes a
web server, a telnet server, a chat server, a news server, a generic client 
and server for remote object access, and APIs for creating new protocols and
services. Twisted supports integration of the Tk, GTK+, Qt or wxPython event
loop with its main event loop. The Win32 event loop is also supported, as is
basic support for running servers on top of Jython.
Installing this package brings all Twisted sub-packages into your system.

%prep


%build

#%install

%clean


%files

%changelog
* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt2.2
- Removed requirement on python-module-pygnome (ALT #27188)

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.0-alt2.1.1.1
- Rebuild with Python-2.7

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt2.1.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.5.0-alt2.1
- Rebuilt with python-2.5.

* Thu Nov 08 2007 Sergey Alembekov <rt@altlinux.ru> 2.5.0-alt2
- adding requires for scripts using gtk, qt4, tkinter, wx and gnome modules

* Fri Mar 30 2007 Sergey Alembekov <rt@altlinux.ru> 2.5.0-alt1
- new version

* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.0-alt1.1
- Rebuilt with python-2.4.

* Fri Dec 31 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- first build for ALT Linux Sisyphus
