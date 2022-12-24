%define module_name App-Packager
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(PAR.pm) perl(Test/More.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.430.1
Release: alt2
Summary: Abstraction for Packagers
Group: Development/Perl
License: perl
Url: %CPAN %module_name
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/J/JV/JV/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
App::Packager provides an abstract interface to a number of common
packagers, trying to catch as much common behaviour as possible.

The main purpose is to have uniform access to application specific
resources.

Supported packagers are PAR::Packer, Cava::Packager and unpackaged. In
the latter case, the packager functions are emulated via
Cava::Packager which provides fallback for unpackaged use.

For example:

    use App::Packager;
    print "My packager is: ", App::Packager::Packager(), "\n";
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/A*

%changelog
* Sat Dec 24 2022 Ilya Mashkin <oddity@altlinux.ru> 1.430.1-alt2
- Build for Sisyphus

* Fri Oct 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.430.1-alt1
- updated by package builder

* Sat Jul 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.430-alt1
- regenerated from template by package builder

* Wed May 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.420-alt1
- initial import by package builder

