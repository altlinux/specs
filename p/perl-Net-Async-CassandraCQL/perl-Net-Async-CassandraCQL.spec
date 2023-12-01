## SPEC file for Perl module Net::Async::CassandraCQL

%define real_name Net-Async-CassandraCQL

Name: perl-Net-Async-CassandraCQL
Version: 0.12
Release: alt3

Summary: use Cassandra databases with IO::Async using CQL

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Net-Async-CassandraCQL/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Fri May 29 2015
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Compress-Snappy perl-Encode perl-Future perl-IO-Socket-IP perl-JSON-PP perl-Module-Metadata perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-Struct-Dumb perl-Sub-Exporter-Progressive perl-Test-Fatal perl-Test-Refcount perl-devel perl-parent perl-podlators
BuildRequires: perl-Compress-LZ4 perl-Devel-GlobalDestruction perl-Devel-Refcount perl-HTML-Parser perl-IO-Async perl-Module-Build perl-Protocol-CassandraCQL perl-Test-HexString perl-Test-Identity perl-Test-Pod perl(experimental.pm)
BuildRequires: perl-IO-Async-tests

# For 32bit platforms
BuildRequires: perl-Math-Int64
Requires:      perl(Math/Int64.pm)

%description
Perl module Net::Async::CassandraCQL allows use of the "CQL3"
interface of a Cassandra database.
It fully supports asynchronous operation via IO::Async, allowing
both direction queries and prepared statements to be managed
concurrently, if required. Alternatively, as the interface
is entirely based on Future objects, it can be operated
synchronously in a blocking fashion by simply awaiting each
individual operation by calling the "get" method.

It is based on Protocol::CassandraCQL, which more completely
documents the behaviours and limits of its ability to
communicate with Cassandra.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Net/Async/CassandraCQL*

%changelog
* Fri Dec 01 2023 Igor Vlasenko <viy@altlinux.org> 0.12-alt3
- NMU: fixed build with perl 5.38

* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt2
- add BR: perl-IO-Async-tests

* Fri May 29 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.12-alt1
- Initial build for ALT Linux Sisyphus
