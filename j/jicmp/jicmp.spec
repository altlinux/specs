Name: jicmp
Version: 1.2.1
Release: alt1
License: GPL
Group: Databases
Summary: Java interface to ICMP (ping)
Source: %name-%version.tar.gz
URL: http://www.opennms.org/
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

# Automatically added by buildreq on Sat Mar 29 2008
BuildRequires: /proc jpackage-1.6-compat

%define arch_arg --with-jvm-arch=32
%ifarch x86_64
%define arch_arg --with-jvm-arch=64
%endif

%description
JICMP is a Java interface to the ICMP protocol (ping), originally written as a part of OpenNMS

%prep
%setup -n %name-%version

%build
%autoreconf
%configure %arch_arg
make

%install
%makeinstall_std

%files
%attr(755,root,root) %_libdir/libjicmp*
%attr(644,root,root) %_datadir/java/*.jar

%changelog
* Sat Dec 31 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.1-alt1
- 1.2.1

* Thu May 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.11-alt1
- 1.0.11

* Tue Jul 14 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.10-alt1
- 1.0.10

* Sat Nov 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.8-alt2
- Remmove depricated ldconfig call in post

* Sun Aug 03 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.8-alt1
- 1.0.8

* Fri Mar 21 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.7-alt1
- 1.0.7

* Sat Nov 24 2007 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.0.6-alt1
- initial build
