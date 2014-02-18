# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(ExtUtils/ParseXS.pm) perl(ExtUtils/Typemaps.pm) perl(File/Basename.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Module-Build-WithXSpp
Version:        0.14
Release:        alt1_1
Summary:        XS++ enhanced flavor of Module::Build
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Module-Build-WithXSpp/
Source0:        http://www.cpan.org/authors/id/S/SM/SMUELLER/Module-Build-WithXSpp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/CppGuess.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(ExtUtils/CppGuess.pm) >= 0.04
Requires:       perl(ExtUtils/ParseXS.pm) >= 2.220.500
Requires:       perl(ExtUtils/Typemaps.pm) >= 1.00
Requires:       perl(ExtUtils/XSpp.pm) >= 0.11
Requires:       perl(File/Basename.pm)
Requires:       perl(File/Spec.pm)
Requires:       perl(Module/Build.pm) >= 0.26

# Filtering unversioned requires


Source44: import.info
%filter_from_requires /^perl\\(Module.Build.pm\\)$/d
%filter_from_requires /^perl\\(ExtUtils.CppGuess.pm\\)$/d

%description
This subclass of Module::Build adds some tools and processes to make it
easier to use for wrapping C++ using XS++ (ExtUtils::XSpp).

%prep
%setup -q -n Module-Build-WithXSpp-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_1
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- initial import by package builder

