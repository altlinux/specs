%define module_name Log-Agent

Name: perl-%module_name
Version: 0.307
Release: alt2.1

Summary: %module_name module for perl
License: Artistic
Group: Development/Perl

Url: %CPAN %module_name
Source: http://www.cpan.org/modules/by-module/Log/%module_name-%version.tar.gz

# Automatically added by buildreq on Fri May 21 2010 (-bi)
BuildRequires: perl-MailTools perl-devel sendmail-common

BuildArch: noarch

%description
Log::Agent is a general logging framework aimed at reusable modules. Instead
of having modules insist on using their own logging reporting (by hardwiring
calls to warn() or syslog()) which can conflict with the final application's
choice, one may use logwarn() for instance to emit a warning.

%prep
%setup -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Log*
%perl_vendor_privlib/auto/Log*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.307-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri May 21 2010 Victor Forsiuk <force@altlinux.org> 0.307-alt2
- This package is really noarch.

* Thu Jun 14 2007 Victor Forsyuk <force@altlinux.org> 0.307-alt1
- 0.307

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.306-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sun Nov 28 2004 Maxim Tkachenko <tma@altlinux.ru> 0.306-alt2
- rebuild for fix error

* Tue May 25 2004 Maxim Tkachenko <tma@altlinux.ru> 0.306-alt1
- build for AltLinux
