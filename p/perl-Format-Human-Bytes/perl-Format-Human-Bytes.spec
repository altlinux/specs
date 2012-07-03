%define m_distro Format-Human-Bytes
Name: perl-Format-Human-Bytes
Version: 0.06
Release: alt1
Summary: Format::Human::Bytes - Format a bytecount and make it human readable

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: GPL
Url: http://search.cpan.org/~sewi/Format-Human-Bytes/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-Module-Install

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Format/Human/Bytes*
%doc Changes README 

%changelog
* Sun Sep 19 2010 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt1
- New version 0.06

* Sat Apr 10 2010 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt1
- New version 0.05

* Tue Jan 19 2010 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt1
- initial build
