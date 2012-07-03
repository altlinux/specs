%define module WWW-Google-PageRank

Name: perl-%module
Version: 0.17
Release: alt1

Summary: Perl module to query google pagerank of page
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/WWW/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Jul 21 2011
BuildRequires: perl-devel perl-libwww

%description
This package contains Perl module assigned for querying PageRank of web page
in Google.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/WWW

%changelog
* Mon Jan 09 2012 Victor Forsiuk <force@altlinux.org> 0.17-alt1
- 0.17

* Thu Jul 21 2011 Victor Forsiuk <force@altlinux.org> 0.16-alt1
- 0.16

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Feb 12 2010 Victor Forsiuk <force@altlinux.org> 0.15-alt1
- 0.15

* Fri Jun 20 2008 Victor Forsyuk <force@altlinux.org> 0.14-alt1
- Initial build.
