%define module		HTTP-Lite
%define m_distro	HTTP-Lite
%define m_name		HTTP::Lite
#%define m_author_id	TJMATHER
Name: perl-%module
Version: 2.3
Release: alt1

Summary: HTTP::Lite - Lightweight HTTP implementation
Group: Development/Perl
License:	Artistic

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: http://search.cpan.org/dist/%m_distro/
Source: http://www.cpan.org/authors/id/A/AD/ADAMK/HTTP-Lite-2.3.tar.gz

BuildArch: noarch

%def_without test

# Automatically added by buildreq on Sun Feb 27 2005
BuildRequires: perl-devel

%description
HTTP::Lite is a stand-alone lightweight HTTP/1.1
    implementation for perl.  It is not intended to replace LWP,
    but rather is intended for use in situations where it is
    desirable to install the minimal number of modules to
    achieve HTTP support, or where LWP is not a good candidate
    due to CPU overhead, such as slower processors.

    HTTP::Lite is ideal for CGI (or mod_perl) programs or for
    bundling for redistribution with larger packages where only
    HTTP GET and POST functionality are necessary.

    HTTP::Lite supports basic POST and GET operations only.  As
    of 0.2.1, HTTP::Lite supports HTTP/1.1 and is compliant with
    the Host header, necessary for name based virtual hosting.
    Additionally, HTTP::Live now supports Proxies.

    If you require more functionality, such as FTP or HTTPS,
    please see libwwwperl (LWP).  LWP is a significantly better
    and more comprehensive package than HTTP::Lite, and should
    be used instead of HTTP::Lite whenever possible.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/HTTP/

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt2
- fix directory ownership violation

* Thu Aug 18 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- new version

* Sun Feb 27 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- first build for ALT Linux Sisyphus
