%define _unpackaged_files_terminate_build 1
%define module Net-EPP

Name: perl-%module
Version: 0.26
Release: alt1

Summary: Perl interface to EPP
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/G/GB/GBROWN/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Sun Jul 17 2011
BuildRequires: perl-Digest-SHA perl-IO-Socket-SSL perl-XML-LibXML perl-devel

BuildArch: noarch

%description
This package offers a number of Perl modules which implement various EPP-related
functions.

%prep
%setup -q -n %{module}-%{version}
find lib/Net/EPP -type f -name '*.pm' -print0 |xargs -r0 chmod -x

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md
%perl_vendor_privlib/Net

%changelog
* Mon Oct 30 2023 Igor Vlasenko <viy@altlinux.org> 0.26-alt1
- automated CPAN update

* Sun May 21 2023 Igor Vlasenko <viy@altlinux.org> 0.25-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.21_1-alt1
- automated CPAN update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Sun Jul 17 2011 Victor Forsiuk <force@altlinux.org> 0.18-alt1
- 0.18

* Sun Apr 10 2011 Victor Forsiuk <force@altlinux.org> 0.17-alt1
- 0.17

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jun 15 2010 Victor Forsiuk <force@altlinux.org> 0.15-alt1
- 0.15

* Fri Jan 22 2010 Victor Forsyuk <force@altlinux.org> 0.13-alt1
- 0.13

* Tue Aug 18 2009 Victor Forsyuk <force@altlinux.org> 0.12-alt1
- Initial build.
