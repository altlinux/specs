Group: Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Note to self: like is with the HTML 2.0 and 3.2 DTDs, HTML 4.0 and 4.01
# have the same public id to their ENTITIES files.  They are not exactly the
# same in 4.0 and 4.01, but the changes are in comments only, so no need
# use a hardcoded system id.  Well, until something installs another, and
# incompatible set of entities using the same public id anyway...

%define date     19991224

Name:            html401-dtds
Version:         4.01
Release:         alt1_%{date}.12.22
Summary:         HTML 4.01 document type definitions

# W3C Software License for DTDs etc:
# http://www.w3.org/Consortium/Legal/IPR-FAQ-20000620#DTD
License:         W3C
URL:             http://www.w3.org/TR/1999/REC-html401-%{date}/
# Source0 generated with Source99, see comments in the script
Source0:         %{name}-%{date}.tar.bz2
Source99:        %{name}-prepare-tarball.sh
Patch0:          %{name}-catalog.patch

BuildArch:       noarch
Requires:        xml-common sgml-common
Requires(post):  /usr/bin/install-catalog
Requires(preun): /usr/bin/install-catalog
Source44: import.info

%description
This package provides the three HTML 4.01 DTDs (strict, frameset, and
transitional).  The DTDs are required for processing HTML 4.01
document instances using SGML tools such as OpenSP, OpenJade, or
SGMLSpm.


%prep
%setup -q -n %{name}
%patch0  -p1


%build


%install

install -dm 0755 %{buildroot}%{_datadir}/sgml/html/4.01
install -pm 0644 *.dtd *.cat *.ent *.decl %{buildroot}%{_datadir}/sgml/html/4.01

install -dm 0755 %{buildroot}%{_sysconfdir}/sgml
touch %{buildroot}%{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc
ln -s %{name}-%{version}-%{release}.soc %{buildroot}%{_sysconfdir}/sgml/%{name}.soc
for rpm404_ghost in %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done



%post
/usr/bin/install-catalog --add \
  %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
  %{_datadir}/sgml/html/4.01/HTML4.cat >/dev/null

%preun
/usr/bin/install-catalog --remove \
  %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
  %{_datadir}/sgml/html/4.01/HTML4.cat >/dev/null || :


%files
%ghost %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc
%{_sysconfdir}/sgml/%{name}.soc
%{_datadir}/sgml/html/


%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 4.01-alt1_19991224.12.22
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 4.01-alt1_19991224.12.9
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 4.01-alt1_19991224.12.8
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 4.01-alt1_19991224.12.7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 4.01-alt1_19991224.12.6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.01-alt1_19991224.12.5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 4.01-alt1_19991224.12.4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 4.01-alt1_19991224.12.3
- update to new release by fcimport

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.01-alt1_19991224.12.2
- initial fc import

