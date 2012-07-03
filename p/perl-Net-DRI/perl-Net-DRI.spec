%define module Net-DRI
%def_without test

Name: perl-%module
Version: 0.96
Release: alt1.1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: A Perl library to access Domain Name Registries/Registrars
License: GPLv2+
Group: Development/Perl

#Url: %CPAN %module
Url: http://www.dotandco.com/services/software/Net-DRI/
#Source: http://www.cpan.org/modules/by-module/Net/%module-%version.tar.gz
Source: http://www.dotandco.com/services/software/Net-DRI/Net-DRI-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 08 2010
BuildRequires: perl-Class-Accessor-Chained perl-DateTime-Format-ISO8601 perl-Email-Valid perl-IO-Compress-Zlib perl-IO-Socket-SSL perl-Log-Agent perl-SOAP-Lite perl-SOAP-WSDL perl-Sub-Name perl-Term-ReadLine-Gnu perl-UNIVERSAL-require perl-XML-LibXML

%description
DRI stands for Domain Registration Interface and aims to be, for domain name
registries/registrars/resellers what Perl DBI is for databases.

Net::DRI offers a uniform API to access services. It can be used by registrars
to access registries. It can be used by clients to access registrars and/or
resellers. It can be used by anonyone to do whois or DAS queries.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 0.96-alt1
- 0.96

* Mon Aug 17 2009 Victor Forsyuk <force@altlinux.org> 0.95-alt1
- 0.95
- Use upstream site in Url and Source instead of CPAN.

* Tue Dec 30 2008 Victor Forsyuk <force@altlinux.org> 0.92-alt1
- 0.92

* Wed Aug 13 2008 Victor Forsyuk <force@altlinux.org> 0.91-alt1
- Initial build.
