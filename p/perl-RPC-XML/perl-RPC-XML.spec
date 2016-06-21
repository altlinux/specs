## SPEC file for Perl module RPC::XML
## Used in ikiwiki

Name: perl-RPC-XML
Version: 0.80
Release: alt1

Summary: an implementation of XML-RPC

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/RPC-XML/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name RPC-XML
Source: %real_name-%version.tar

BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Jun 06 2015
# optimized out: perl-Class-Factory-Util perl-Class-Singleton perl-Compress-Raw-Zlib perl-DateTime perl-DateTime-Format-Builder perl-DateTime-Format-Strptime perl-DateTime-Locale perl-DateTime-TimeZone perl-Devel-Symdump perl-Encode perl-Exporter-Tiny perl-HTTP-Date perl-HTTP-Message perl-IO-Compress perl-IO-Socket-IP perl-LWP-MediaTypes perl-List-MoreUtils perl-Module-Implementation perl-Module-Runtime perl-Net-HTTP perl-Params-Validate perl-Pod-Escapes perl-Pod-Simple perl-Socket6 perl-Try-Tiny perl-URI perl-XML-Parser perl-devel perl-libwww perl-parent
BuildRequires: apache-mod_perl-base perl-CGI perl-DateTime-Format-ISO8601 perl-HTTP-Daemon perl-IO-Socket-INET6 perl-Module-Load perl-Net-Server perl-Sub-Name perl-XML-LibXML perl-podlators

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

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
sed -e "s/localhost\([':]\)/$HOST\1/g" -i t/40_server.t

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README README.apache2 ChangeLog
%exclude /.perl.req
%perl_vendor_privlib/RPC

%_bindir/make_method
%_man1dir/make_method*

%files -n perl-Apache-RPC-Server
%perl_vendor_privlib/Apache


%changelog
* Tue Jun 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.80-alt1
- New version

* Sat Jun 06 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.79-alt1
- New version

* Sun Aug 31 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.78-alt1
- New version

* Thu Oct 18 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.77-alt1
- New version

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
