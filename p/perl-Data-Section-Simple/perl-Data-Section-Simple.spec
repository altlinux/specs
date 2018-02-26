Name: perl-Data-Section-Simple
Version: 0.03
Release: alt1
Summary: Data::Section::Simple - Read data from __DATA__

Group: Development/Perl
License: Perl
Url: %CPAN Data-Section-Simple

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-Test-Requires perl-Module-Install perl-Module-Install-ReadmeFromPod perl-Module-Install-Repository

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Data/Section/Simple.pm
%doc Changes README 

%changelog
* Sun Dec 04 2011 Vladimir Lettiev <crux@altlinux.ru> 0.03-alt1
- New version 0.03

* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1
- initial build
