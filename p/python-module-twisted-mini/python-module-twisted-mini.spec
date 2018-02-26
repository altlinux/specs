%define version 2.5.0
%define release alt3
%setup_python_module twisted-mini

Name:           %{packagename}
Version:        %{version}
Release: %{release}.1

Summary:        Twisted is an event-based framework for internet applications

Group:          Development/Python
License:        MIT
URL:            http://www.twistedmatrix.com
Packager:	Sergey Alembekov <rt@altlinux.ru>


Requires:       python-module-twisted-core
Requires:       python-module-twisted-conch
Requires:       python-module-twisted-lore
Requires:       python-module-twisted-mail
Requires:       python-module-twisted-names
Requires:       python-module-twisted-news
Requires:       python-module-twisted-runner
Requires:       python-module-twisted-web
Requires:       python-module-twisted-words

Obsoletes:      pythom-module-twisted < 2.5.0
Conflicts:	python-module-twisted
Provides:       twisted = %{version}-%{release}
BuildArch: noarch

%description
Twisted is an event-based framework for internet applications.  It includes a
web server, a telnet server, a chat server, a news server, a generic client 
and server for remote object access, and APIs for creating new protocols and
services. 
Installing this package brings Twisted sub-packages into your system except 
GUI-libraries wich is requieres Tkinter, gtk, gt4, wx. This package is usefull
for the servers where GUI-libraries are needless.

%prep


%build

#%install

%clean


%files

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.0-alt3.1
- Rebuild with Python-2.7

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt3
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.5.0-alt2.1
- Rebuilt with python-2.5.

* Fri Mar 30 2007 Sergey Alembekov <rt@altlinux.ru> 2.5.0-alt2
- firs build.
