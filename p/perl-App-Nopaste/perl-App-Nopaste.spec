Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(parent.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-App-Nopaste
Version:        1.007
Release:        alt1_1
Summary:        Easy access to any pastebin
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/App-Nopaste/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/App-Nopaste-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl
BuildRequires:  rpm-build-perl
BuildRequires:  sed
BuildRequires:  perl(CPAN/Meta/Requirements.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Runtime
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Class/Load.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Getopt/Long/Descriptive.pm)
BuildRequires:  perl(JSON.pm)
BuildRequires:  perl(JSON/MaybeXS.pm)
BuildRequires:  perl(Module/Metadata.pm)
BuildRequires:  perl(Module/Pluggable.pm)
BuildRequires:  perl(Module/Runtime.pm)
BuildRequires:  perl(Path/Tiny.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(URI/Escape.pm)
BuildRequires:  perl(WWW/Mechanize.pm)
BuildRequires:  perl(namespace/clean.pm)
# Tests only
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(LWP/Protocol.pm)
BuildRequires:  perl(Test/Deep.pm)
BuildRequires:  perl(Test/Fatal.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Trap.pm)
BuildRequires:  perl(version.pm)
# for ssh plugin
Requires:       /usr/bin/scp
Requires:       perl(Clipboard.pm)
Requires:       perl(Browser/Open.pm)
Requires:       perl(WWW/Pastebin/PastebinCom/Create.pm)
Requires:       perl(HTTP/Request/Common.pm)
Source44: import.info

%description
Pastebins (also known as nopaste sites) let you post text, usually code,
for public viewing. They're used a lot in IRC channels to show code that
would normally be too long to give directly in the channel (hence the
name nopaste).

%package -n nopaste
# needs to beat old nopaste-2835-3
Epoch:          1
License:        GPL+ or Artistic
Group:          Development/Other
Summary:        Access pastebins from the command line
Requires:       %{name} = 0:%{version}

%description -n nopaste
This application lets you post text to pastebins from the command line.

Pastebins (also known as nopaste sites) let you post text, usually code, for
public viewing. They're used a lot in IRC channels to show code that would
normally be too long to give directly in the channel (hence the name nopaste).


%prep
%setup -q -n App-Nopaste-%{version}
sed -i 's,^#!.*perl,#!%{__perl},' script/nopaste

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes CONTRIBUTING README
%doc LICENSE
%{perl_vendor_privlib}/App*

%files -n nopaste
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.007-alt1_1
- update to new release by fcimport

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.007-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.006-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_3
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_1
- update to new release by fcimport

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1
- automated CPAN update

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.002-alt1_1
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.001-alt1_1
- update to new release by fcimport

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.001-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1
- automated CPAN update

* Tue Jan 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.95-alt1
- automated CPAN update

* Wed Jan 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1
- automated CPAN update

* Tue Jan 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1
- automated CPAN update

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1
- uploaded to Sisyphus as Scalar-Does dependency

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.90-alt1_4
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.90-alt1_2
- update to new release by fcimport

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.90-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1_1
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1_1
- fc import

