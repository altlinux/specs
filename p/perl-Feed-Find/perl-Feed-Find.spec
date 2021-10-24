%define _unpackaged_files_terminate_build 1
%define dist Feed-Find
Name: perl-%dist
Version: 0.12
Release: alt1

Summary: Syndication feed auto-discovery
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/D/DA/DAVECROSS/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Class-ErrorHandler perl-Filter perl-Pod-Escapes perl-devel perl-libwww

%description
Feed::Find implements feed auto-discovery for finding syndication feeds,
given a URI. It (currently) passes all of the auto-discovery tests at
http://diveintomark.org/tests/client/autodiscovery/.

Feed::Find will discover the following feed formats: RSS 0.91, RSS 1.0,
RSS 2.0, and Atom.

%prep
%setup -q -n %{dist}-%{version}

%ifdef __BTE
# requires network
rm t/01-find.t
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Feed

%changelog
* Sun Oct 24 2021 Igor Vlasenko <viy@altlinux.org> 0.12-alt1
- automated CPAN update

* Thu Jun 17 2021 Igor Vlasenko <viy@altlinux.org> 0.11-alt1
- automated CPAN update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0.09-alt1
- automated CPAN update

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.07-alt2
- disabled build depndency on perl-Module-Install

* Sat Apr 23 2011 Alexey Tourbin <at@altlinux.ru> 0.07-alt1
- 0.06 -> 0.07

* Sat Sep 10 2005 Alexey Tourbin <at@altlinux.ru> 0.06-alt1
- 0.05 -> 0.06

* Sun Aug 21 2005 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- initial revision (for XML::Feed)
