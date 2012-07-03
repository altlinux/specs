%define m_distro Email-Valid-Loose
Name: perl-Email-Valid-Loose
Version: 0.05
Release: alt1
Summary: Email::Valid::Loose - Email::Valid which allows dot before at mark

Group: Development/Perl
License: Perl
Url: %CPAN %m_distro

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-Email-Valid

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Email/Valid/Loose*
%doc Changes README 

%changelog
* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt1
- initial build
