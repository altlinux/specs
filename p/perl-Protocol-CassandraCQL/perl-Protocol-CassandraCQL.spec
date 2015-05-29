## SPEC file for Perl module Protocol::CassandraCQL

%define real_name Protocol-CassandraCQL

Name: perl-Protocol-CassandraCQL
Version: 0.12
Release: alt2

Summary: wire protocol support functions for Cassandra CQL

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Protocol-CassandraCQL/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Fri May 29 2015
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-JSON-PP perl-Math-BigInt perl-Module-Metadata perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-Try-Tiny perl-devel perl-parent perl-podlators
BuildRequires: perl-Compress-Snappy perl-HTML-Parser perl-IO-Socket-IP perl-Module-Build perl-Sub-Name perl-Test-Fatal perl-Test-HexString perl-Test-Pod

# Only used on 32bit platforms, and missed by buildreq
BuildRequires: perl-Math-Int64
Requires:      perl(Math/Int64.pm)

%description
Perl module Protocol::CassandraCQL provides the basic constants
and other support functions required to communicate with 
a Cassandra database using `CQL'. It is not in itself a CQL
client; it simply provides the necessary support functions to
allow one to be written. It supports the additions added by
`CQL' version 2.

For a complete client, see instead Net::Async::CassandraCQL.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Protocol/CassandraCQL*

%changelog
* Fri May 29 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.12-alt2
- Initial build for ALT Linux Sisyphus
