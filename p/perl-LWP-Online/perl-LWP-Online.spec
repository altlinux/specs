%define m_distro LWP-Online
Name: perl-LWP-Online
Version: 1.08
Release: alt1
Summary: LWP::Online - Does your process have access to the web

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~adamk/LWP-Online/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-libwww perl-URI

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/LWP/Online*
%doc Changes README 

%changelog
* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Thu Jan 28 2010 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt1
- initial build
