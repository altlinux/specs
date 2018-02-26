%define dist junoscript-perl
Name: perl-junoscript
Version: 6.4I0
Release: alt3

Summary: Perl modules for manage JunOS routers from Perl scripts
License: Juniper Networks
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Source1: junoscript-perl.README.alt

Patch1: junos-ssh.diff

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 12 2008
BuildRequires: perl-Date-Manip perl-IO-Tty perl-Parse-Yapp perl-XML-DOM perl-devel perl-libxml-perl

BuildRequires: perl-Net-SSLeay perl-Net-SSH-Perl

%description
Each Juniper Networks router running JUNOS Internet software release 4.3B2
or later supports the JUNOScript API. The JUNOScript API is an XML
application that Juniper Networks routers use to exchange information with
client applications. Telnet, SSH and SSL are supported.

%package examples
Summary: examples of using perl-junoscript
Group: Development/Perl

%description examples
Summary: examples of using perl-junoscript

%prep
%setup -q -n %dist-%version

%patch1 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%__cp %SOURCE1 $RPM_BUILD_DIR/%dist-%version/README.alt

%files
%doc	README CHANGES

%perl_vendor_privlib/JUNOS/*

%files examples
%doc examples/*
%doc README.alt

%changelog
* Wed Nov 17 2010 Sergey Y. Afonin <asy@altlinux.ru> 6.4I0-alt3
- removed macro %%perl_vendor_man3dir from spec
- removed Packager from spec
- applied patch from bug #63002 from CPAN

* Wed Nov 12 2008 Sergey Y. Afonin <asy@altlinux.ru> 6.4I0-alt2
- spec cleanup
- package examples

* Sun Jan 21 2007 Sergey Y. Afonin <asy@altlinux.ru> 6.4I0-alt1
- initial revision
