# BEGIN SourceDeps(oneline):
BuildRequires: perl(MIME/Base64.pm) perl(SOAP/Lite.pm) perl(SOAP/Test.pm) perl(SOAP/Transport/HTTP.pm) perl(SOAP/Transport/POP3.pm) perl(SOAP/Transport/TCP.pm) perl(Test.pm)
# END SourceDeps(oneline)
%define module_version 0.717
%define module_name XMLRPC-Lite
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel

Name: perl-%module_name
Version: 0.717
Release: alt1
Summary: client and server implementation of XML-RPC protocol
Group: Development/Perl
License: unknown
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/P/PH/PHRED/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
XMLRPC::Lite is a Perl modules which provides a simple nterface to the
XML-RPC protocol both on client and server side. Based on SOAP::Lite module,
it gives you access to all features and transports available in that module.

See t/26-xmlrpc.t for client examples and examples/XMLRPC/* for server
implementations.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/A*
%perl_vendor_privlib/X*

%changelog
* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.717-alt1
- initial import by package builder

