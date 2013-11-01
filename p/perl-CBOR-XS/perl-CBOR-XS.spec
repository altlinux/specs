# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Types/Serialiser.pm) perl(XSLoader.pm) perl(common/sense.pm)
# END SourceDeps(oneline)
%define module_version 0.08
%define module_name CBOR-XS
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.08
Release: alt1
Summary: unknown
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/ML/MLEHMANN/%module_name-%module_version.tar.gz

%description
WARNING! This module is very new, and not very well tested (that's up to
you to do). Furthermore, details of the implementation might change freely
before version 1.0. And lastly, the object serialisation protocol depends
on a pending IANA assignment, and until that assignment is official, this
implementation is not interoperable with other implementations (even
future versions of this module) until the assignment is done.

You are still invited to try out CBOR, and this module.

This module converts Perl data structures to the Concise Binary Object
Representation (CBOR) and vice versa. CBOR is a fast binary serialisation
format that aims to use a superset of the JSON data model, i.e. when you
can represent something in JSON, you should be able to represent it in
CBOR.

In short, CBOR is a faster and very compact binary alternative to JSON,
with the added ability of supporting serialisation of Perl objects. (JSON
often compresses better than CBOR though, so if you plan to compress the
data later you might want to compare both formats first).

To give you a general idea about speed, with texts in the megabyte range,
`CBOR::XS' usually encodes roughly twice as fast as the Storable manpage or
the JSON::XS manpage and decodes about 15%%-30%% faster than those. The shorter the
data, the worse the Storable manpage performs in comparison.

As for compactness, `CBOR::XS' encoded data structures are usually about
20%% smaller than the same data encoded as (compact) JSON or the Storable manpage.

The primary goal of this module is to be *correct* and the secondary goal
is to be *fast*. To reach the latter goal it was written in C.

See MAPPING, below, on how CBOR::XS maps perl values to CBOR values and
vice versa.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes COPYING
%perl_vendor_archlib/C*
%perl_vendor_autolib/*

%changelog
* Fri Nov 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- initial import by package builder

