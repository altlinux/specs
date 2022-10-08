# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 1.3
%define module_name Math-Units
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.3
Release: alt2
Summary: Unit conversion
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/D/DM/DMUEY/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
The Math::Units module converts a numeric value in one unit of measurement
to some other unit.  The units must be compatible, i.e. length can not be
converted to volume.  If a conversion can not be made an exception is thrown.

A combination chaining and reduction algorithm is used to perform the most
direct unit conversion possible.  Units may be written in several different
styles.  An abbreviation table is used to convert from common long-form unit
names to the (more or less) standard abbreviations that the units module uses
internally.  All multiplicative unit conversions are cached so that future
conversions can be performed very quickly.

Too many units, prefixes and abbreviations are supported to list here.  See
the source code for a complete listing.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_privlib/M*

%changelog
* Sat Oct 08 2022 Igor Vlasenko <viy@altlinux.org> 1.3-alt2
- to Sisyphus as perl-Geo-Gpx dep

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1
- initial import by package builder

