%define module		XML-XQL
%define m_distro	XML-XQL
%define m_name		XML::XQL
%define m_author_id	TJMATHER
Name: perl-%module
Version: 0.68
Release: alt2.1

Summary: A perl module for querying XML tree structures with XQL
Group: Development/Perl
License: Unknown

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: http://search.cpan.org/dist/%m_distro/
Source: http://www.cpan.org/modules/by-module/XML/%m_distro-%version.tar.bz2

BuildArch: noarch

# Automatically added by buildreq on Sat Sep 06 2008
BuildRequires: perl-Date-Manip perl-Parse-Yapp perl-XML-DOM perl-devel termutils

%description
This is a Perl extension that allows you to perform XQL queries on XML
object trees. Currently only the XML::DOM module is supported, but
other implementations, like XML::Grove, may soon follow.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/XML/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.68-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.68-alt2
- update buildreq, fix Source URL

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.68-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Oct 25 2004 Vitaly Lipatov <lav@altlinux.ru> 0.68-alt1
- first build for ALTLinux Sisyphus
