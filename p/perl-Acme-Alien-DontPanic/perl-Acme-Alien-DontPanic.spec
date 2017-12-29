Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(autodie.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Acme-Alien-DontPanic
Version:        0.044
Release:        alt1_1
Summary:        Test module for Alien::Base
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Acme-Alien-DontPanic/
Source0:        http://www.cpan.org/authors/id/P/PL/PLICEASE/Acme-Alien-DontPanic-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(Alien/Base/ModuleBuild.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Use system dontpanic library instead of downloading it from the Internet at
# build time (it's forbidden in the build system).
BuildRequires:  pkgconfig(dontpanic)
# Dependecies for generated Build script
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Spec.pm)
# Run-time:
BuildRequires:  perl(Alien/Base.pm)
BuildRequires:  perl(parent.pm)
# Tests:
BuildRequires:  perl(Test2/V0.pm)
BuildRequires:  perl(Test/Alien.pm)
Requires:       perl(Alien/Base.pm) >= 1.010
# Generated code:
Requires:       perl(Data/Dumper.pm)
Requires:       perl(Module/Build.pm)
# The maning of the package is to dontpanic library is installed and
# application can build against it. Because we use system dontpanic library
# instead of bundling that one that had been dowloaded and compiled at build
# time, we nee to explicitly run-require developmental files of the library.
Requires:       pkgconfig(dontpanic)

# Remove under-specified dependencies

Source44: import.info
%filter_from_requires /^perl\\(Alien.Base.pm\\)$/d

%description
This Perl module is a toy module to test the efficacy of the Alien::Base system.

%prep
%setup -q -n Acme-Alien-DontPanic-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Fri Dec 29 2017 Igor Vlasenko <viy@altlinux.ru> 0.044-alt1_1
- to Sisyphus

