# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Config.pm) perl(ExtUtils/MakeMaker.pm) perl(XSLoader.pm) perl(blib.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: gcc-c++
Name:           perl-ExtUtils-CppGuess
Version:        0.08
Release:        alt1
Summary:        Guess C++ compiler and flags
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/ExtUtils-CppGuess/
Source:        http://www.cpan.org/authors/id/E/ET/ETJ/ExtUtils-CppGuess-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Capture/Tiny.pm)
BuildRequires:  perl(ExtUtils/Manifest.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Fatal.pm)
BuildRequires:  perl(Exporter.pm)
Source44: import.info

%description
ExtUtils::CppGuess attempts to guess the system's C++ compiler that is
compatible with the C compiler that your perl was built with.

%prep
%setup -q -n ExtUtils-CppGuess-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
#%%{perl_vendor_privlib}/auto/*
%{perl_vendor_privlib}/ExtUtils*

%changelog
* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_7
- update to new release by fcimport

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_6
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Oct 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- initial import by package builder

