%define m_distro Eval-Context
Name: perl-Eval-Context
Version: 0.09.11
Release: alt1
Summary: Eval::Context perl module

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~nkh/Eval-Context/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-Term-Size perl-Test-Output perl-Directory-Scratch-Structured perl-Test-Block perl-Test-Exception perl-Module-Build perl-Test-NoWarnings perl-Test-Warn perl-Text-Diff perl-Data-Compare perl-Data-TreeDumper

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Eval/Context*
%doc Changes README 

%changelog
* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.09.11-alt1
- initial build
