Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(parent.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-App-Nopaste
Version:        1.013
Release:        alt1_1
Summary:        Easy access to any pastebin
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/App-Nopaste
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/App-Nopaste-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
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
Group: Development/Other
# needs to beat old nopaste-2835-3
Epoch:          1
License:        GPL+ or Artistic
Summary:        Access pastebins from the command line
Requires:       %{name} = 0:%{version}-%{release}

%description -n nopaste
This application lets you post text to pastebins from the command line.

Pastebins (also known as nopaste sites) let you post text, usually code, for
public viewing. They're used a lot in IRC channels to show code that would
normally be too long to give directly in the channel (hence the name nopaste).


%prep
%setup -q -n App-Nopaste-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes CONTRIBUTING README
%doc --no-dereference LICENSE
%{perl_vendor_privlib}/App*

%files -n nopaste
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.013-alt1_1
- update to new release by fcimport

* Wed Jul 31 2019 Igor Vlasenko <viy@altlinux.ru> 1.013-alt1
- automated CPAN update

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1_1
- update to new release by fcimport

* Sun Jul 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.011-alt1_1
- update to new release by fcimport

* Wed Aug 30 2017 Igor Vlasenko <viy@altlinux.ru> 1.011-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.010-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.009-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.008-alt1
- automated CPAN update

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

