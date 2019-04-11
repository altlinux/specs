Group: Databases
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CGI.pm) perl(CGI/Carp.pm) perl(Encode.pm) perl(Module/Signature.pm) perl(Pod/Usage.pm) perl(charnames.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382

Name:           bucardo
Version:        5.5.0
Release:        alt1
Summary:        Postgres replication system for both multi-master and multi-slave operations
License:        BSD
URL:            http://bucardo.org/
Source0:        %name-%version.tar
Source1:        %name.service
BuildArch:      noarch

BuildRequires:  postgresql-perl

# Build
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)

# Runtime
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(Pod/PlainText.pm)
BuildRequires:  perl(Pod/Parser.pm)
BuildRequires:  perl(boolean.pm)
BuildRequires:  perl(open.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(DBD/Pg.pm)
BuildRequires:  perl(DBI.pm)
BuildRequires:  perl(DBIx/Safe.pm)
BuildRequires:  perl(Getopt/Long.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(Net/SMTP.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(sigtrap.pm)
BuildRequires:  perl(Sys/Hostname.pm)
BuildRequires:  perl(Sys/Syslog.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(Encode/Locale.pm)

# Extra
BuildRequires:  perl(MongoDB.pm)
BuildRequires:  perl(DBD/mysql.pm)
BuildRequires:  perl(Redis.pm)
BuildRequires:  perl(DBD/SQLite.pm)

# Tests only
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       postgresql-perl

Requires:  perl(MongoDB.pm)
Requires:  perl(DBD/mysql.pm)
Requires:  perl(Redis.pm)
Requires:  perl(DBD/SQLite.pm)

%description
Bucardo is an asynchronous PostgreSQL replication system, allowing for both
multi-master and multi-slave operations.It was developed at Backcountry.com
primarily by Greg Sabino Mullane of End Point Corporation.

%prep
%setup
# perl.req fails on -*-cperl-*-
sed -i -e 's,-- -\*-cperl-\*-,,' Bucardo.pm

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot} DESTINSTALLVENDORSHARE=%{buildroot}/%{_datadir}/%{name}
# removing packlist is required for building on fedora-epel
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
sed -i -e '1d;2i#!%{__perl}' %{name}
rm -f %{buildroot}/%{_bindir}/%{name}
install -p -d -m 0644 %buildroot/var/log/%name
install -Dp -m755 bucardo %{buildroot}/%{_sbindir}/%{name}
install -Dp -m644 %{name}.schema %{buildroot}/%{_datadir}/%{name}/%{name}.schema
install -pD -m 0644 %SOURCE1 %buildroot%systemd_unitdir/%name.service
# %{_fixperms} %{buildroot}/

%files
%doc --no-dereference LICENSE
%doc *.html Changes INSTALL README TODO
%dir /var/log/%name
%systemd_unitdir/%name.service
%{perl_vendor_privlib}/*
%{_sbindir}/%{name}
%{_datadir}/%{name}

%changelog
* Wed Apr 10 2019 Ilfat Aminov <aminov@altlinux.org> 5.5.0-alt1
- Build for Sisyphus/classic repo

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 5.4.1-alt1_11
- update to new release by fcimport

* Mon Dec 17 2018 Igor Vlasenko <viy@altlinux.ru> 5.4.1-alt1_10
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 5.4.1-alt1_7
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 5.4.1-alt1_6
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 5.4.1-alt1_5
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 5.4.1-alt1_4
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 5.4.1-alt1_3
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 4.5.0-alt3_8
- update to new release by fcimport

* Wed Aug 20 2014 Cronbuild Service <cronbuild@altlinux.org> 4.5.0-alt3_7
- rebuild to get rid of unmets

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.5.0-alt2_7
- update to new release by fcimport

* Tue Jan 29 2013 Cronbuild Service <cronbuild@altlinux.org> 4.5.0-alt2_3
- rebuild to get rid of unmets

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 4.5.0-alt1_3
- new release

* Thu Sep 04 2008 Mikhail Pokidko <pma@altlinux.org> 3.0.9-alt2
- sisyphus_check fixes

* Wed May 14 2008 Mikhail Pokidko <pma@altlinux.org> 3.0.9-alt1
- Initial ALT build
  + TODO: move .bucardorc to /etc/
