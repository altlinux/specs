%define _unpackaged_files_terminate_build 1
Epoch: 1
%define dist JSON-PP
Name: perl-%dist
Version: 2.97000
Release: alt1

Summary: JSON::XS compatible pure-Perl module
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/I/IS/ISHIGAKI/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 28 2011
BuildRequires: perl-Math-BigInt perl-Tie-IxHash perl-devel perl(Encode.pm) perl(Pod/Man.pm)

%description
JSON::PP was inculded in JSON distribution (CPAN module).
It comes to be a perl core module in Perl 5.14.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/JSON
%_bindir/json_pp
%_man1dir/json_pp*

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.97000-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.94-alt1.1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.27400-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 2.27300-alt1
- automated CPAN update

* Sat Oct 19 2013 Igor Vlasenko <viy@altlinux.ru> 2.27203-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.27202-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.27200-alt1
- automated CPAN update

* Thu Apr 28 2011 Alexey Tourbin <at@altlinux.ru> 2.27105-alt1
- initial revision
