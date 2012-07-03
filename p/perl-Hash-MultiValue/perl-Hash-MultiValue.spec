Name: perl-Hash-MultiValue
Version: 0.12
Release: alt1

Summary: Hash::MultiValue - Store multiple values per key
Group: Development/Perl
License: Perl

Url: %CPAN Hash-MultiValue
# cloned from git://github.com/miyagawa/Hash-MultiValue.git
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-threads perl-Module-Install perl-Test-Base perl-Module-Install-Repository perl-Module-Install-ReadmeFromPod perl-Module-Install-AuthorTests

%description
Hash::MultiValue is an object (and a plain hash reference) that may
contain multiple values per key, inspired by MultiDict of WebOb.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Hash/MultiValue*
%doc Changes README 

%changelog
* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- 0.12

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- initial build
