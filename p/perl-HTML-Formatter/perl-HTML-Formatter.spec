%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Data/Dumper.pm) perl(Encode.pm) perl(Encode/CN.pm) perl(Encode/JP.pm) perl(Encode/KR.pm) perl(Encode/TW.pm) perl(English.pm) perl(File/Slurper.pm) perl(File/Spec.pm) perl(Font/Metrics/Courier.pm) perl(Font/Metrics/CourierBold.pm) perl(Font/Metrics/CourierBoldOblique.pm) perl(Font/Metrics/CourierOblique.pm) perl(Font/Metrics/Helvetica.pm) perl(Font/Metrics/HelveticaBold.pm) perl(Font/Metrics/HelveticaBoldOblique.pm) perl(Font/Metrics/HelveticaOblique.pm) perl(Font/Metrics/TimesBold.pm) perl(Font/Metrics/TimesBoldItalic.pm) perl(Font/Metrics/TimesItalic.pm) perl(Font/Metrics/TimesRoman.pm) perl(HTML/Element.pm) perl(HTML/TreeBuilder.pm) perl(IO/File.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Module/Build.pm) perl(Pod/Wordlist.pm) perl(Scalar/Util.pm) perl(Test/CPAN/Meta.pm) perl(Test/Warnings.pm)
BuildRequires: perl(Test/EOL.pm) perl(Test/More.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl(Test/Spelling.pm) perl(Test/Synopsis.pm) perl(base.pm) perl(blib.pm) perl(bytes.pm) perl(integer.pm) perl(parent.pm) perl(strict.pm) perl(utf8.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_version 2.16
%define module_name HTML-Formatter
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.16
Release: alt1
Summary: Base class for HTML formatters
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/HTML-Formatter

Source: http://www.cpan.org/authors/id/N/NI/NIGELM/HTML-Formatter-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_privlib/H*

%changelog
* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 2.16-alt1
- automated CPAN update

* Thu Feb 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.14-alt2
- to Sisyphus

* Fri Oct 23 2015 Igor Vlasenko <viy@altlinux.ru> 2.14-alt1
- initial import by package builder

