# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: xhtml2fo-style-xsl
Version: 20051222
Release: alt1_12
Group: Text tools

Summary: Antenna House, Inc. XHTML to XSL:FO stylesheets
License: Copyright only
URL: http://www.antennahouse.com/XSLsample/XSLsample.htm

Requires(pre): xhtml1-dtds
Requires(pre): xml-common >= 0.6.3
#Requires(post): libxml2
#Requires(postun): libxml2


BuildArch: noarch
Source0: http://www.antennahouse.com/XSLsample/sample-xsl-xhtml2fo.zip
Source1: AntennaHouse-COPYRIGHT
Source44: import.info

%description
These XSL stylesheets allow you to transform any XHTML document to FO.
With a XSL:FO processor you could create PDF versions of XHTML documents.


%prep
%setup -q -c -n %{name}-%{version} -T -b 0
%__cp %{SOURCE1} .
%build


%install
%__rm -Rf $RPM_BUILD_ROOT
%__mkdir -p $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT/usr/share/sgml/xhtml1/xhtml2fo-stylesheets
%__mkdir -p $DESTDIR
%__cp *xsl $DESTDIR/

%files
%doc AntennaHouse-COPYRIGHT
/usr/share/sgml/xhtml1/xhtml2fo-stylesheets


%post
CATALOG=%{_sysconfdir}/xml/catalog
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://www.antennahouse.com/XSLsample/sample-xsl-xhtml2fo/xhtml2fo.xsl" \
 "file:///usr/share/sgml/xhtml1/xhtml2fo-stylesheets/xhtml2fo.xsl" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://www.antennahouse.com/XSLsample/sample-xsl-xhtml2fo/xhtml2fo.xsl" \
 "file:///usr/share/sgml/xhtml1/xhtml2fo-stylesheets/xhtml2fo.xsl" $CATALOG

%postun
if [ "$1" = 0 ]; then
  CATALOG=%{_sysconfdir}/xml/catalog
  %{_bindir}/xmlcatalog --noout --del \
  "file://%{_datadir}/sgml/xhtml1/xhtml2fo-stylesheets/xhtml2fo.xsl" $CATALOG
fi


%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20051222-alt1_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20051222-alt1_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 20051222-alt1_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20051222-alt1_9
- update to new release by fcimport

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 20051222-alt1_8
- initial fc import

