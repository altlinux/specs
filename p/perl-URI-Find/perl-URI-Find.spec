Name: perl-URI-Find
Version: 20160806
Release: alt1

Summary: URI::Find - Find URIs in arbitrary text
License: Perl
Group: Development/Perl

Url: %CPAN URI-Find
# Cloned from git://github.com/schwern/uri-find.git
Source: %name-%version.tar

BuildRequires: perl-devel perl-Module-Build perl-URI
BuildArch: noarch

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/urifind
%_man1dir/urifind.*
%perl_vendor_privlib/URI/Find*
%doc TODO Changes README 

%changelog
* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 20160806-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 20140709-alt1
- automated CPAN update

* Mon Oct 01 2012 Vladimir Lettiev <crux@altlinux.ru> 20111103-alt1
- 20100505 -> 20111103

* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 20100505-alt1
- initial build
