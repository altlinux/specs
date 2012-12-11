# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DBI.pm) perl(Date/Manip.pm) perl(DateTime/Duration.pm) perl(DateTime/Format/Builder.pm) perl(DateTime/LeapSecond.pm) perl(Test/NoWarnings.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-Epoch
Version:        0.13
Release:        alt2_4
Summary:        Convert DateTimes to/from epoch seconds
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DateTime-Format-Epoch/
Source0:        http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-Epoch-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(Math/BigInt.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Params/Validate.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
Requires:       perl(DateTime.pm) >= 0.31
Requires:       perl(Math/BigInt.pm) >= 1.66


Source44: import.info

%description
This module can convert a DateTime object (or any object that can be
converted to a DateTime object) to the number of seconds since a given
epoch. It can also do the reverse.

%prep
%setup -q -n DateTime-Format-Epoch-%{version}

# replace CRLF
find -type f -print0 | xargs -0 sed -i 's/\r$//'

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;


%check
./Build test

%files
%doc Changes LICENSE README TODO
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_4
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_4
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_2
- fc import

