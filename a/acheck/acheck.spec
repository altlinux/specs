# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Config/General.pm) perl(Exporter.pm) perl(File/Spec/Functions.pm) perl(IO/File.pm) perl(Term/ANSIColor.pm) perl(Term/ReadLine.pm) perl(Term/Size.pm) perl-podlators
# END SourceDeps(oneline)
Name:           acheck
Version:        0.5.4
Release:        alt1_0
Summary:        Check common localisation mistakes

Group:          Text tools
License:        GPLv2+
URL:            http://packages.debian.org/etch/%{name}
Source0:        http://ftp.de.debian.org/debian/pool/main/a/acheck/%{name}_%{version}.tar
BuildRequires:  gettext
BuildRequires:  /usr/bin/pod2man
BuildArch:      noarch
Requires:       perl(Text/Aspell.pm) perl(Config/General.pm) perl(Term/Size.pm) perl(Locale/gettext.pm)
Requires:       perl(Locale/PO.pm) perl(Term/ReadLine/Gnu.pm) perl(Term/UI.pm) %{name}-rules
Source44: import.info


%description
Any text file checker, is a tool designed to help both
translators and reviewers checking and fixing common localisation
mistakes according to file format. Rules can be defined to add new
checks.

%prep
%setup -q -n acheck-%{version}

%build
#Empty build


%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
install -p -m 755 %{name} $RPM_BUILD_ROOT/%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{perl_vendor_privlib}/ACheck/
install -p -m 644 Common.pm FileType.pm Parser.pm \
 $RPM_BUILD_ROOT%{perl_vendor_privlib}/ACheck/
cd po;make;cd ..

/usr/bin/pod2man man/acheck.1.pod acheck.1
/usr/bin/pod2man man/acheck.5.pod acheck.5
/usr/bin/pod2man man/acheck.fr.1.pod acheck.fr.1
/usr/bin/pod2man man/acheck.fr.5.pod acheck.fr.5

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1/
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man5/
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1/fr
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man5/fr

install -p -m 644 acheck.1 $RPM_BUILD_ROOT/%{_mandir}/man1/
install -p -m 644 acheck.5 $RPM_BUILD_ROOT/%{_mandir}/man5/
install -p -m 644 acheck.fr.1 $RPM_BUILD_ROOT/%{_mandir}/man1/fr/acheck.1
install -p -m 644 acheck.fr.5 $RPM_BUILD_ROOT/%{_mandir}/man5/fr/acheck.5

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/locale/fr/LC_MESSAGES/ \
 $RPM_BUILD_ROOT/%{_datadir}/locale/pl/LC_MESSAGES/ \
 $RPM_BUILD_ROOT/%{_datadir}/locale/sv/LC_MESSAGES/
install -p -m 644 po/fr.mo $RPM_BUILD_ROOT/%{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo
install -p -m 644 po/pl.mo $RPM_BUILD_ROOT/%{_datadir}/locale/pl/LC_MESSAGES/%{name}.mo
install -p -m 644 po/sv.mo $RPM_BUILD_ROOT/%{_datadir}/locale/sv/LC_MESSAGES/%{name}.mo


%files
%doc debian/changelog debian/copyright
%doc bash_completion.d
%{_bindir}/%{name}
%{perl_vendor_privlib}/*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man1/fr/*.1*
%{_mandir}/man5/fr/*.5*
%{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/pl/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/sv/LC_MESSAGES/%{name}.mo

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt1_0
- manual update from debian

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_11
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_10
- update to new release by fcimport

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_6
- update to new release by fcimport

* Mon Oct 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_5
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_4
- initial release by fcimport

