# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dumper.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Scalar/Util.pm) perl(Storable.pm) perl(Test/More.pm) perl(Time/HiRes.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_version 1.02
%define module_name Functional-Utility
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.02
Release: alt1
Summary: helper tools for light-weight functional programming.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/B/BE/BELDEN/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
Functional::Utility provides a small collection of utilities to make certain pieces
of functional programming a bit easier. Included are a few tools for controlling the
behavior of existing functions.

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README.md LICENSE
%perl_vendor_privlib/F*

%changelog
* Sat Oct 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- initial import by package builder

