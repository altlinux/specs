# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DateTime/Span.pm) perl(DateTime/SpanSet.pm) perl(Params/Validate.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Event-Recurrence
Version:        0.16
Release:        alt2_17
Summary:        DateTime::Set extension for create basic recurrence sets
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DateTime-Event-Recurrence/
Source0:        http://www.cpan.org/authors/id/F/FG/FGLOCK/DateTime-Event-Recurrence-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Class/ISA.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Set.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
This module provides convenience methods that let you easily create
DateTime::Set objects for various recurrences, such as "once a month" or
"every day". You can also create more complicated recurrences, such as
"every Monday, Wednesday and Thursday at 10:00 AM and 2:00 PM".

%prep
%setup -q -n DateTime-Event-Recurrence-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
make test

%files
%doc Changes CREDITS LICENSE README TODO
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_17
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_17
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_15
- fc import

