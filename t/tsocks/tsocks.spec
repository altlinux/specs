%define		real_version	1.8beta5
Name:		tsocks
Version:	1.8
Release:	alt1
Summary:	Library for catching network connections, redirecting them on a SOCKS server
Group:		Security/Networking
License:	GPLv2+
URL:		http://tsocks.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{real_version}.tar
Patch0:		tsocks_remove_static_lib.patch
Patch1:		tsocks_fix_lib_path.patch
Patch2:		tsocks_script_validation_error.patch
Patch3:		tsocks_documentation_update.patch

%description
tsocks is designed for use in machines which are firewalled from the
Internet. It avoids the need to recompile applications like lynx or
telnet so they can use SOCKS to reach the Internet. It behaves much
like the SOCKSified TCP/IP stacks seen on other platforms.

tsocks is a library to allow transparent SOCKS proxying. It wraps the
normal connect() function. When a connection is attempted, it consults
the configuration file (which is defined at configure time but defaults
to /etc/tsocks.conf) and determines if the IP address specified is local.
If it is not, the library redirects the connection to a SOCKS server
specified in the configuration file. It then negotiates that connection
with the SOCKS server and passes the connection back to the calling
program.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING FAQ TODO tsocks.conf.simple.example tsocks.conf.complex.example
%{_bindir}/*
%{_libdir}/libtsocks*
%{_mandir}/man?/*

%changelog
* Fri Sep 24 2010 Mykola Grechukh <gns@altlinux.ru> 1.8-alt1
- built for ALT Linux

* Wed Jan  6 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 1.8-0.5.beta5
- Fix the library path problem more cleanly
- Fix bash script validation to handle the no argument case
- Change patch name to reflect guidelines
- Fix documentation to reflect patch modifications
- Remove INSTALL from packaged files

* Mon Dec 14 2009 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 1.8-0.4.beta5
- Fix the library path problem on x86_64 and ppc64
- Elaborate the summary and description fields

* Sat Dec  5 2009 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 1.8-0.3.beta5
- Fix as per the recommendations on bug #543566

* Thu Dec  3 2009 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 1.8-0.2.beta5
- Fix Source0 URL as per the guidelines

* Tue Dec  1 2009 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 1.8-0.1.beta5
- Initial build for Fedora
