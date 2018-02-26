%define module  Event-ExecFlow

Name: perl-%module
Version: 0.64
Release: alt1

Summary: Event::ExecFlow - High level API for event-based execution flow control  
License: GPL/Artistic
Group: Development/Perl

Url: http://www.exit1.org/Event-ExecFlow/ 
Source: %module-%version.tar.gz

BuildRequires: perl-devel perl-libintl perl-AnyEvent

Packager: Ilya Mashkin <oddity@altlinux.ru>

%description
Event::ExecFlow provides a ligh level API for defining complex flow
controls with asynchronous execution of external programs.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%dir %perl_vendor_privlib/Event/ExecFlow
%perl_vendor_privlib/Event*
%_bindir/*

%changelog
* Sat May 15 2010 Ilya Mashkin <oddity@altlinux.ru> 0.64-alt1
- 0.64

* Tue May 27 2008 L.A. Kostis <lakostis@altlinux.ru> 0.63-alt1
- 0.63.

* Sun Feb 18 2007 L.A. Kostis <lakostis@altlinux.ru> 0.62-alt1.2
- add missing dir.

* Sun Feb 18 2007 L.A. Kostis <lakostis@altlinux.ru> 0.62-alt1.1
- add execflow.

* Fri Feb 16 2007 L.A. Kostis <lakostis@altlinux.ru> 0.62-alt1
- initial release.

