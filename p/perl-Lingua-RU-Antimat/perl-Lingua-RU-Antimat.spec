%define module Lingua-RU-Antimat
%define m_distro Lingua-RU-Antimat
%define m_name Lingua::RU::Antimat
%define _enable_test 1

Name: perl-Lingua-RU-Antimat
Version: 1.01
Release: alt1.1

Summary: Lingua::RU::Antimat - Perl Module for removal Russian slang from chat, guestbooks, etc.

License: GPL
Group: Development/Perl
Url: http://www.tcen.ru/antimat

BuildArch: noarch
Source: Lingua-RU-Antimat.tar.bz2

# Automatically added by buildreq on Tue Mar 10 2009
BuildRequires: perl-Encode perl-devel

%description
Check Lingua::RU::Antimat web site at http://www.tcen.ru/antimat
There you will find Russian documentation, tutorial, etc.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README changesrus.txt changesrus_koi8.txt changesrus_utf-8.txt
%perl_vendor_privlib/Lingua/RU/*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Mar 10 2009 Grigory Milev <week@altlinux.ru> 1.01-alt1
- Initial build for ALT Linux
- added changes for work with utf-8
