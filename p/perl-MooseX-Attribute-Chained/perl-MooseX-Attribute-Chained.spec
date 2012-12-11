# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Moose/Meta/Method/Accessor.pm) perl(Moose/Role.pm) perl(Moose/Util.pm) perl(Scalar/Util.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-MooseX-Attribute-Chained
Version:        1.0.1
Release:        alt3_3
Summary:        Attribute that returns the instance to allow for chaining
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/MooseX-Attribute-Chained/
Source0:        http://www.cpan.org/authors/id/P/PE/PERLER/MooseX-Attribute-Chained-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Script.pm)
BuildRequires:  perl(Try/Tiny.pm)
# for release testing, but they mostly fail
#BuildRequires:  perl(Pod::Coverage::TrustPod)
#BuildRequires:  perl(Test::HasVersion)
#BuildRequires:  perl(Test::Kwalitee)
#BuildRequires:  perl(Test::MinimumVersion)
#BuildRequires:  perl(Test::Pod)
#BuildRequires:  perl(Test::Pod::Coverage)
#BuildRequires:  perl(Test::Portability::Files)

# renamed from perl-MooseX-ChainedAccessors in January 2012
# no explicit provides necessary as this package still contains the old classes
# and rpm automatically detects them
Obsoletes:      perl-MooseX-ChainedAccessors <= 0.02-3.fc17


Source44: import.info

%description
MooseX::Attribute::Chained is a Moose Trait which allows for method
chaining on accessors by returning $self on write/set operations.

%prep
%setup -q -n MooseX-Attribute-Chained-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;


%check
./Build test

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_3
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_3
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_1
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1
- fc import

