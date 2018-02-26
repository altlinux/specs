Name: perl-Lingua-JA-Regular-Unicode
Version: 0.07
Release: alt1

Summary: Lingua::JA::Regular::Unicode - convert japanese chars
Group: Development/Perl
License: Perl

Url: %CPAN Lingua-JA-Regular-Unicode
# Cloned from git://github.com/tokuhirom/p5-lingua-ja-regular-unicode.git
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-Module-Build perl-Test-Base perl-Test-Perl-Critic

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Lingua/JA/Regular/Unicode*
%doc Changes LICENSE

%changelog
* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt1
- 0.07

* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt1
- initial build
