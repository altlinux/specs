%define _unpackaged_files_terminate_build 1
## SPEC file for Perl module Cassandra::Client

%define real_name Cassandra-Client

Name: perl-Cassandra-Client
Version: 0.19
Release: alt1

Summary: Perl interface to Cassandra's native protocol

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Cassandra-Client/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Aug 09 2020
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel perl perl-AnyEvent perl-CPAN-Meta-Requirements perl-Encode perl-JSON-PP perl-Net-SSLeay perl-PadWalker perl-Parse-CPAN-Meta perl-Socket6 perl-Sub-Exporter-Progressive perl-Sub-Uplevel perl-devel perl-parent python-modules python2-base python3 python3-base python3-dev ruby ruby-stdlibs sh4
BuildRequires: perl-AnyEvent-XSPromises perl-CPAN-Meta perl-Clone perl-Compress-LZ4 perl-Compress-Snappy perl-Devel-Cycle perl-Devel-GlobalDestruction perl-EV perl-IO-Socket-INET6 perl-Ref-Util perl-Ref-Util-XS perl-Sub-Current perl-Test-Exception

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
%perl_vendor_archlib/Cassandra/Client*
%perl_vendor_autolib/Cassandra/Client*

%changelog
* Sat Dec 03 2022 Nikolay A. Fetisov <naf@altlinux.org> 0.19-alt1
- New version

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.18-alt1
- New version

* Sun Aug 09 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.17-alt1
- New version

* Wed Feb 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- new version

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.2
- rebuild with new perl 5.28.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1
- rebuild with new perl 5.26.1

* Sat Dec 09 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.14-alt1
- New version

* Sat Jul 15 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.13-alt1
- New version

* Tue Jul 04 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.12-alt1
- New version

* Sun Jun 18 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.11-alt1
- New version

* Tue Feb 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.10-alt1
- New version

* Sat Jan 21 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.09-alt1
- New version

* Sun Nov 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.08-alt1
- New version

* Sun Sep 18 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.05-alt1
- Initial build for ALT Linux Sisyphus
