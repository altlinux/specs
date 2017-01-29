## SPEC file for Perl module DBD::Cassandra

%define real_name DBD-Cassandra

Name: perl-DBD-Cassandra
Version: 0.53
Release: alt1

Summary: DBD database driver for Cassandra's CQL3

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/DBD-Cassandra/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Sep 18 2016
# optimized out: perl perl-Clone perl-Data-OptList perl-Encode perl-Params-Util perl-Pod-Escapes perl-Pod-Simple perl-Promises perl-Ref-Util perl-Sub-Exporter perl-Sub-Install perl-devel python-base python-modules python3
BuildRequires: perl-Cassandra-Client perl-Compress-LZ4 perl-Compress-Snappy perl-DBI perl-Test-Pod

%description
Perl module DBD::Cassandra aids developers in connecting to
Apache Cassandra via the familiar DBI interfaces. The current
implementation is very incomplete, though later releases will
hopefully implement the full CQL3 language.

Right now this module is entirely written in Perl. Performance
is not very good, so this might become XS some day.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/DBD/Cassandra*

%changelog
* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.53-alt1
- New version

* Sun Sep 18 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.51-alt1
- New version

* Sat Mar 19 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.25-alt1
- New version

* Sat Feb 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.24-alt1
- New version

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.23-alt1
- New version

* Mon Sep 28 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.21-alt1
- New version

* Sat Sep 05 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.16-alt1
- New version

* Tue Aug 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.15-alt1
- New version

* Fri May 29 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.14-alt1
- Initial build for ALT Linux Sisyphus
