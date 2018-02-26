BuildRequires: perl(Pod/Man.pm) perl(Config/General.pm) perl(Term/ReadLine.pm) perl(Term/Size.pm)
Name:           acheck-rules
Version:        0.3.1
Release:        alt2_5
Summary:        Rules for acheck

Group:          Text tools
License:        GPLv2+
URL:            http://packages.debian.org/etch/%{name}
Source0:        http://ftp.de.debian.org/debian/pool/main/a/acheck-rules/%{name}_%{version}.tar.gz
BuildRequires:  gettext
BuildArch:      noarch
Source44: import.info

%description
Rules for acheck.

%prep
%setup -q -n %{name}-%{version}


%build
#Empty build


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/acheck
cp -rp rules $RPM_BUILD_ROOT/%{_datadir}/acheck/
echo """
use Pod::Man;
my \$parser = Pod::Man->new(release => \$VERSION, section => 8);
\$parser->parse_from_file(\$ARGV[0], \$ARGV[1]);
""" > $RPM_BUILD_ROOT/pod2man.pl
perl $RPM_BUILD_ROOT/pod2man.pl man/acheck-rules.5.pod acheck-rules.5
perl $RPM_BUILD_ROOT/pod2man.pl man/acheck-rules.fr.5.pod acheck-rules.fr.5
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man5/
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man5/fr
install -p -m 644 acheck-rules.5 $RPM_BUILD_ROOT/%{_mandir}/man5/
install -p -m 644 acheck-rules.fr.5 $RPM_BUILD_ROOT/%{_mandir}/man5/fr/acheck-rules.5
rm -f $RPM_BUILD_ROOT/pod2man.pl

%files
%doc debian/changelog debian/copyright
%{_datadir}/acheck/rules/
%{_mandir}/man5/*.5*
%{_mandir}/man5/fr/*.5*


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_5
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_5
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_4
- initial release by fcimport

