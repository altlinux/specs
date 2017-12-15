%define module_name CBOR-XS
%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Canary/Stability.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Math/BigFloat.pm) perl(Math/BigInt.pm) perl(Math/BigRat.pm) perl(Time/Piece.pm) perl(Types/Serialiser.pm) perl(URI.pm) perl(XSLoader.pm) perl(common/sense.pm)
# END SourceDeps(oneline)
Epoch: 2
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.7
Release: alt2.1
Summary: Concise Binary Object Representation (CBOR, RFC7049)
Group: Development/Perl
License: GPL-3
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/M/ML/MLEHMANN/%{module_name}-%{version}.tar.gz

%description
This module converts Perl data structures to the Concise Binary Object
Representation (CBOR) and vice versa. CBOR is a fast binary serialisation
format that aims to use an (almost) superset of the JSON data model, i.e.
when you can represent something useful in JSON, you should be able to
represent it in CBOR.

In short, CBOR is a faster and quite compact binary alternative to JSON,
with the added ability of supporting serialisation of Perl objects. (JSON
often compresses better than CBOR though, so if you plan to compress the
data later and speed is less important you might want to compare both
formats first).

To give you a general idea about speed, with texts in the megabyte range,
`CBOR::XS' usually encodes roughly twice as fast as the Storable manpage or
the JSON::XS manpage and decodes about 15%%%%-30%%%% faster than those. The shorter the
data, the worse the Storable manpage performs in comparison.

Regarding compactness, `CBOR::XS'-encoded data structures are usually
about 20%%%% smaller than the same data encoded as (compact) JSON or
the Storable manpage.

In addition to the core CBOR data format, this module implements a
number of extensions, to support cyclic and shared data structures
(see `allow_sharing' and `allow_cycles'), string deduplication (see
`pack_strings') and scalar references (always enabled).

The primary goal of this module is to be *correct* and the secondary goal
is to be *fast*. To reach the latter goal it was written in C.

See MAPPING, below, on how CBOR::XS maps perl values to CBOR values and
vice versa.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes COPYING README
%perl_vendor_archlib/C*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2:1.7-alt2.1
- rebuild with new perl 5.26.1

* Sat Oct 28 2017 Igor Vlasenko <viy@altlinux.ru> 2:1.7-alt2
- updated summary

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 2:1.7-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2:1.6-alt1.1
- rebuild with new perl 5.24.1

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 2:1.6-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 2:1.5-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.41-alt1
- new version

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.3-alt1.1
- rebuild with new perl 5.22.0

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.3-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1.1
- rebuild with new perl 5.20.1

* Thu Dec 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Tue Dec 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- automated CPAN update

* Fri Nov 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- initial import by package builder

