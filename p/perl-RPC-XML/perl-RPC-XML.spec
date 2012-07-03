## SPEC file for Perl module RPC::XML
## Used in ikiwiki

%define version    0.74
%define release    alt1

Name: perl-RPC-XML
Version: %version
Release: %release

Summary: an implementation of XML-RPC

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/~rjray/RPC-XML/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name RPC-XML
Source: %real_name-%version.tar

BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Apr 23 2011
BuildRequires: apache-mod_perl-base perl-CGI perl-HTTP-Daemon perl-XML-LibXML perl-XML-Parser perl-podlators

%description
Perl module RPC::XML is an implementation of XML-RPC. The module
provides classes for sample client and server implementations, 
a server designed as an Apache location-handler, and a suite of 
data-manipulation classes that are used by them.

%package -n perl-Apache-RPC-Server
Summary: a subclass of RPC::XML::Server tuned for mod_perl
Group: Development/Perl
Requires: %name = %version-%release

%description -n perl-Apache-RPC-Server
Perl module Apache::RPC::Server module is a subclassing
of RPC::XML::Server that is tuned and designed for use
within Apache with mod_perl.

%prep
%setup  -n %real_name-%version

# Ugly patch to obtain build system dependant server name for tests
HOST=`awk '/^127.0.0.1/ {print $2;}' /etc/hosts`
%__subst "s/localhost\([':]\)/$HOST\1/g" t/40_server.t

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README README.apache2 ChangeLog
%dir %perl_vendor_privlib/RPC
%perl_vendor_privlib/RPC/XML*
%dir %perl_vendor_privlib/auto/RPC
%perl_vendor_privlib/auto/RPC/XML*

%_bindir/make_method
%_man1dir/make_method*

%files -n perl-Apache-RPC-Server
%perl_vendor_privlib/Apache/RPC*


%changelog
* Sat Apr 23 2011 Alexey Tourbin <at@altlinux.ru> 0.74-alt1
- New version 0.74

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Oct 10 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.73-alt1
- New version 0.73 (Closes: 22725)
- Moving mod_perl specific modules into subpackage

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.69-alt1
- New version 0.69

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.64-alt1
- New version 0.64

* Mon Apr 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.60-alt1
- New version 0.60
  - Multiple bugfixes and improvements

* Sat Feb 23 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.59-alt1
- Initial build for ALT Linux Sisyphus

* Mon Feb 18 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.59-alt0.1
- Initial build
