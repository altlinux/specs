# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DateTime/Duration.pm) perl(DateTime/Infinite.pm) perl(Params/Validate.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Set
Version:        0.28
Release:        alt2_11
Summary:        Datetime sets and set math
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DateTime-Set/
Source0:        http://www.cpan.org/authors/id/F/FG/FGLOCK/DateTime-Set-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(DateTime.pm)
# introduces circular dependency
#BuildRequires:  perl(DateTime::Event::Recurrence)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Set/Infinite.pm)
BuildRequires:  perl(Test/More.pm)

%{echo 
%filter_from_requires /perl.Set.Infinite.pm. >= 0.5502/d

}

Source44: import.info


%description
DateTime::Set is a module for datetime sets. It can be used to handle two
different types of sets. The first is a fixed set of predefined datetime
objects. For example, if we wanted to create a set of datetimes containing
the birthdays of people in our family. The second type of set that it can
handle is one based on the idea of a recurrence, such as "every Wednesday",
or "noon on the 15th day of every month". This type of set can have fixed
starting and ending datetimes, but neither is required. So our "every
Wednesday set" could be "every Wednesday from the beginning of time until
the end of time", or "every Wednesday after 2003-03-05 until the end of
time", or "every Wednesday between 2003-03-05 and 2004-01-07".

%prep
%setup -q -n DateTime-Set-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
./Build test

%files
%doc Changes LICENSE README TODO
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.28-alt2_11
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1_11
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1_9
- fc import

