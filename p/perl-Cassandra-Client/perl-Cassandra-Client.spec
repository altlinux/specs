## SPEC file for Perl module Cassandra::Client

%define real_name Cassandra-Client

Name: perl-Cassandra-Client
Version: 0.08
Release: alt1

Summary: Perl interface to Cassandra's native protocol

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Cassandra-Client/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Sep 18 2016
# optimized out: perl perl-AnyEvent perl-Data-OptList perl-Encode perl-Params-Util perl-Sub-Exporter perl-Sub-Install perl-devel python-base python-modules python3
BuildRequires: perl-Clone perl-Compress-LZ4 perl-Compress-Snappy perl-Promises perl-Ref-Util

%description
Perl module Cassandra::Client is a library providing access to
the Cassandra database, through the native protocol. Both
synchronous and asynchronous querying is supported, through
various common calling styles.

%prep
%setup -q -n %real_name-%version

%build
rm -f t/03-types.t
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Cassandra/Client*

%changelog
* Sun Nov 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.08-alt1
- New version

* Sun Sep 18 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.05-alt1
- Initial build for ALT Linux Sisyphus
