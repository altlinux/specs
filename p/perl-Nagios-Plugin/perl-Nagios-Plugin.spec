%define _unpackaged_files_terminate_build 1
%define dist Nagios-Plugin
Name: perl-%dist
Version: 0.37
Release: alt1

Summary: A family of perl modules to streamline writing Nagios plugins
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/N/NI/NIERLEIN/Nagios-Plugin-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Apr 22 2011
BuildRequires: perl-Class-Accessor perl-Config-Tiny perl-Math-Calc-Units perl-Params-Validate perl-devel perl(Monitoring/Plugin/Functions.pm)

%description
Nagios::Plugin and its associated Nagios::Plugin::* modules are a
family of perl modules to streamline writing Nagios plugins. The main
end user modules are Nagios::Plugin, providing an object-oriented
interface to the entire Nagios::Plugin::* collection, and
Nagios::Plugin::Functions, providing a simpler functional interface to
a useful subset of the available functionality.

The purpose of the collection is to make it as simple as possible for
developers to create plugins that conform the Nagios Plugin guidelines
(http://nagiosplug.sourceforge.net/developer-guidelines.html).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Nagios

%changelog
* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- automated CPAN update

* Fri Apr 22 2011 Alexey Tourbin <at@altlinux.ru> 0.35-alt1
- 0.34 -> 0.35

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- automated CPAN update

* Mon Dec 22 2008 Dmitry V. Levin <ldv@altlinux.org> 0.30-alt1
- Updated to 0.30.

* Fri Sep 05 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.27-alt1
- 0.27

* Thu May 01 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.26-alt1
- first build for ALT Linux Sisyphus
