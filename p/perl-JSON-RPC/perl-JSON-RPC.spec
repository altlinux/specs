%define module	JSON-RPC

Name: perl-JSON-RPC
Version: 1.06
Release: alt1

Summary: Perl implementation of JSON-RPC 1.1 protocol

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/JSON-RPC

Source0: %module-%version.tar
Patch0: %name-1.06-alt-use_lib.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses perl-devel

BuildRequires: perl-Module-Build perl-Class-Accessor-Lite perl-Plack perl-Router-Simple
# Automatically added by buildreq on Tue Sep 28 2010
BuildRequires: perl-CGI perl-JSON perl-Test-Pod perl-libwww
BuildRequires: apache2-mod_perl

%description
Perl module JSON::RPC - implementation of JSON-RPC 1.1 protocol.

JSON-RPC is a stateless and light-weight remote procedure call (RPC)
protocol for inter-networking applications over HTTP. It uses JSON
as the data format for of all facets of a remote procedure call,
including all application data carried in parameters.

%package Server-Apache2
Summary: JSON-RPC v1.1 mod_perl2 server
Group: Development/Perl
Requires: %name = %version-%release

%description Server-Apache2
Perl module JSON::RPC::Server::Apache2 - implementation of
JSON-RPC server for mod_perl2.

%prep
%setup -q -n %module-%version
%patch0 -p2

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc MANIFEST README.md Changes
%perl_vendor_privlib/JSON*
%exclude %perl_vendor_privlib/JSON/RPC/Legacy/Server/Apache2.pm

%files Server-Apache2
%perl_vendor_privlib/JSON/RPC/Legacy/Server/Apache2.pm


%changelog
* Mon Apr 23 2018 Grigory Ustinov <grenka@altlinux.org> 1.06-alt1
- Build new version.

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Sep 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.98-alt1
- Initial build for ALT Linux
