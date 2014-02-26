# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(English.pm) perl(List/Util.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: gcc-c++
Name:           perl-Boost-Geometry-Utils
Version:        0.15
Release:        alt1_3
Summary:        Boost::Geometry::Utils Perl module
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Boost-Geometry-Utils/
Source0:        http://www.cpan.org/authors/id/A/AA/AAR/Boost-Geometry-Utils-%{version}.tar.gz
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/Typemaps/Default.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Module/Build/WithXSpp.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(XSLoader.pm)

 # Filters (not)shared c libs
Source44: import.info

%description
Boost::Geometry::Utils Perl module

%prep
%setup -q -n Boost-Geometry-Utils-%{version}

%build
perl Build.PL --install_path bindoc=%_man1dir installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc CHANGES LICENSE README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Boost*

%changelog
* Wed Feb 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_3
- moved to Sisyphus for Slic3r (by dd@ request)

