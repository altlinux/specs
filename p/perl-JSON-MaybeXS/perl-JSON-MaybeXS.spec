%define module_version 1.001000
%define module_name JSON-MaybeXS
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Cpanel/JSON/XS.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(JSON/PP.pm) perl(Test/More.pm) perl(Test/Without/Module.pm) perl(base.pm) perl(if.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.001000
Release: alt1
Summary: use L<Cpanel::JSON::XS> with a fallback to L<JSON::PP>
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/M/MS/MSTROUT/JSON-MaybeXS-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/J*

%changelog
* Sun Dec 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.001000-alt1
- automated CPAN update

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.000000-alt2
- moved to Sisyphus (for Catalyst-Runtime update)

* Mon Oct 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.000000-alt1
- initial import by package builder

