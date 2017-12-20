%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Config.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Sub/Delete.pm) perl(base.pm) perl(threads.pm) perl(threads/shared.pm) perl(Lexical/Sub.pm)
# END SourceDeps(oneline)
%define module_name constant-lexical
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.0003
Release: alt1
Summary: Perl pragma to declare lexical compile-time constants
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/S/SP/SPROUT/%{module_name}-%{version}.tar.gz
Patch: constant-lexical-2.0003-alt-fix-build.patch

%description
This module creates compile-time constants in the manner of.constant.pm, but makes them local to the enclosing scope.


%prep
%setup -q -n %{module_name}-%{version}

if [ %version == 2.0003 ]; then
%patch -p1
cp xs/*.xs .
fi

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/c*
%perl_vendor_autolib/c*

%changelog
* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 2.0003-alt1
- automated CPAN update

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 2.0001-alt2
- moved to Sisyphus as dependency

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.0001-alt1
- initial import by package builder

