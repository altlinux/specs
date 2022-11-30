# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(Test/Warn.pm)
# END SourceDeps(oneline)
%define module_name Graphics-Toolkit-Color
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.00
Release: alt1.1
Summary: color palette creation tool
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/L/LI/LICHTKIND/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
Each object has 7 attributes, which are its RGB and HSL values and if possible a name.
This is because humans access colors on hardware level (eye) in RGB,
on cognition level in HSL (brain) and on cultural level (language) with names. 
Having easy access to all three and some color math should enable you to get the color
palette you desire quickly and with no additional dependencies.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README.md Changes README CONTRIBUTING
%perl_vendor_privlib/G*

%changelog
* Wed Nov 30 2022 Igor Vlasenko <viy@altlinux.org> 1.00-alt1.1
- to Sisyphus as perl-Chart dep

* Thu Oct 06 2022 Igor Vlasenko <viy@altlinux.org> 1.00-alt1
- initial import by package builder

