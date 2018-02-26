%define dist Text-TabularDisplay

Name: perl-%dist
Version: 1.30
Release: alt1

Summary: Text::TabularDisplay - display text in formatted table output
License: GPLv2+
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DA/DARREN/%dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 01 2012
BuildRequires: perl-devel

%description
Text::TabularDisplay simplifies displaying textual data in a table. The
output is identical to the columnar display of query results in the
mysql text monitor.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc examples
%perl_vendor_privlib/Text

%changelog
* Sun Apr 01 2012 Victor Forsiuk <force@altlinux.org> 1.30-alt1
- 1.30

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Jul 11 2007 Victor Forsyuk <force@altlinux.org> 1.22-alt1
- 1.22

* Thu Aug 25 2005 Alexey Morozov <morozov@altlinux.org> 1.20-alt1
- Initial build for ALT Linux
