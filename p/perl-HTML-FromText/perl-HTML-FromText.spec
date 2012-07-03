%define module		HTML-FromText
%define m_distro	HTML-FromText
%define m_name		HTML::FromText
#%define m_author_id	TJMATHER
Name: perl-%module
Version: 2.05
Release: alt3.1

Summary: A perl module for HTML::FromText
Group: Development/Perl
License: Artistic/GPL v1

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: http://search.cpan.org/dist/%m_distro/
Source: http://search.cpan.org/CPAN/authors/id/C/CW/CWEST/%m_distro-%version.tar.bz2
Patch: %name.patch

BuildArch: noarch

# Automatically added by buildreq on Sun Feb 27 2005
BuildRequires: perl-Email-Find perl-Exporter-Lite perl-HTML-Parser perl-Pod-Escapes perl-Pod-Simple perl-Test-Pod perl-devel

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
HTML::FromText converts text to HTML.

%prep
%setup -q -n %m_distro-%version
%patch -p1

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README Changes
%_bindir/*
%perl_vendor_privlib/HTML/
%_man1dir/*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.05-alt3.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.05-alt3
- fix directory ownership violation

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 2.05-alt2
- add fix from Alexey Tourbin <at@>

* Sun Feb 27 2005 Vitaly Lipatov <lav@altlinux.ru> 2.05-alt1
- first build for ALT Linux Sisyphus
