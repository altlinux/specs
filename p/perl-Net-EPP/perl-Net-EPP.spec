%define module Net-EPP

Name: perl-%module
Version: 0.18
Release: alt1

Summary: Perl interface to EPP
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/G/GB/GBROWN/Net-EPP-%version.tar.gz

# Automatically added by buildreq on Sun Jul 17 2011
BuildRequires: perl-Digest-SHA perl-IO-Socket-SSL perl-XML-LibXML perl-devel

BuildArch: noarch

%description
This package offers a number of Perl modules which implement various EPP-related
functions.

%prep
%setup -n %module-%version

%build
find lib/Net/EPP -type f -name '*.pm' -print0 |xargs -r0 chmod -x
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net

%changelog
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
