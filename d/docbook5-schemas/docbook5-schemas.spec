BuildRequires: xml-utils
Name: docbook5-schemas
Version: 5.0
Release: alt2_6
Group: Text tools

Summary: Norman Walsh's schemas (DTD, Relax NG, W3C schema) for Docbook 5.X

License: Freely redistributable without restriction
URL: http://www.oasis-open.org/docbook/

Provides: docbook5-dtd = %{version}-%{release}
Provides: docbook5-rng = %{version}-%{release}
Provides: docbook5-sch = %{version}-%{release}
Provides: docbook5-xsd = %{version}-%{release}

Requires(post): libxml2 >= 2.4.8
Requires(postun): libxml2 >= 2.4.8
Requires: xml-common >= 0.6.3-24
BuildRequires: unzip
BuildRequires: libxml2 >= 2.4.8

BuildArch: noarch

Source0:  http://www.docbook.org/xml/%{version}/docbook-%{version}.zip
Source44: import.info

%description
Docbook 5.X is a complete rewrite of Docbook in RELAX NG and not compatible
with previous Docbook versions. This package contains Relax NG , DTD and W3C
schema for Docbook 5.X. Syntax of those schemas is XML-compliant and is
developed by the OASIS consortium.

%prep
%setup -q -n docbook-5.0


%build
CATALOG=docbook-5.xml
%{_bindir}/xmlcatalog --create --noout $CATALOG
for v in 5.0
do
  # DTD
  %{_bindir}/xmlcatalog --noout --add "public" \
     "-//OASIS//DTD DocBook XML ${v}//EN" \
     "file://%{_datadir}/xml/docbook5/schema/dtd/${v}/docbook.dtd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "system" \
     "http://www.oasis-open.org/docbook/xml/${v}/dtd/docbook.dtd" \
     "file://%{_datadir}/xml/docbook5/schema/dtd/${v}/docbook.dtd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "system" \
     "http://docbook.org/xml/${v}/dtd/docbook.dtd" \
     "file://%{_datadir}/xml/docbook5/schema/dtd/${v}/docbook.dtd" ${CATALOG}
  # RNG
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/rng/docbook.rng" \
     "file://%{_datadir}/xml/docbook5/schema/rng/${v}/docbook.rng" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/rng/docbook.rng" \
     "file://%{_datadir}/xml/docbook5/schema/rng/${v}/docbook.rng" ${CATALOG}
  # RNG+XInclude
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/rng/docbookxi.rng" \
     "file://%{_datadir}/xml/docbook5/schema/rng/${v}/docbookxi.rng" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/rng/docbookxi.rng" \
     "file://%{_datadir}/xml/docbook5/schema/rng/${v}/docbookxi.rng" ${CATALOG}
  # RNC
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/rnc/docbook.rnc" \
     "file://%{_datadir}/xml/docbook5/schema/rng/${v}/docbook.rnc" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/rng/docbook.rnc" \
     "file://%{_datadir}/xml/docbook5/schema/rng/${v}/docbook.rnc" ${CATALOG}
  # RNC+XInclude
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/rnc/docbookxi.rnc" \
     "file://%{_datadir}/xml/docbook5/schema/rng/${v}/docbookxi.rnc" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/rng/docbookxi.rnc" \
     "file://%{_datadir}/xml/docbook5/schema/rng/${v}/docbookxi.rnc" ${CATALOG}
  # XSD
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/xsd/docbook.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/docbook.xsd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/xsd/docbook.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/docbook.xsd" ${CATALOG}
  # XSD + XInclude
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/xsd/docbookxi.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/docbookxi.xsd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/xsd/docbookxi.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/docbookxi.xsd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/xsd/xi.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/xi.xsd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/xsd/xi.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/xi.xsd" ${CATALOG}
  # XLink + XML
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/xsd/xlink.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/xlink.xsd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/xsd/xlink.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/xlink.xsd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/xsd/xml.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/xml.xsd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/xsd/xml.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/xml.xsd" ${CATALOG}
  # Schematron
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/sch/docbook.sch" \
     "file://%{_datadir}/xml/docbook5/schema/sch/${v}/docbook.sch" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/sch/docbook.sch" \
     "file://%{_datadir}/xml/docbook5/schema/sch/${v}/docbook.sch" ${CATALOG}
done
# ---------------------
# Build XML catalog files for each Schema
for v in 5.0
do
  for s in dtd rng sch xsd; do
   cat=${s}/catalog.xml
   %{_bindir}/xmlcatalog --noout --create ${cat}
   case $s in
    dtd)
     %{_bindir}/xmlcatalog --noout --add "public" \
       "-//OASIS//DTD DocBook XML ${v}//EN" \
       "docbook.dtd" ${cat}
     %{_bindir}/xmlcatalog --noout --add "system" \
       "http://www.oasis-open.org/docbook/xml/${v}/dtd/docbook.dtd" \
       "docbook.dtd" ${cat}
     ;;
    sch)
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/docbook.${s}" \
       "docbook.${s}" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/docbook.${s}" \
       "docbook.${s}" ${cat}
     ;;
    rng)
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/docbook.${s}" \
       "docbook.${s}" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/docbook.${s}" \
       "docbook.${s}" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/docbookxi.${s}" \
       "docbookxi.${s}" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/docbookxi.${s}" \
       "docbookxi.${s}" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/docbook.rnc" \
       "docbook.rnc" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/docbook.rnc" \
       "docbook.rnc" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/docbookxi.rnc" \
       "docbookxi.rnc" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/docbookxi.rnc" \
       "docbookxi.rnc" ${cat}
     ;;
    xsd)
     # http://www.oasis-open.org/docbook/xml/5.0/xsd/docbookxi.xsd
     # http://www.oasis-open.org/docbook/xml/5.0/xsd/xlink.xsd
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/docbook.${s}" \
       "docbook.${s}" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/docbook.${s}" \
       "docbook.${s}" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/docbookxi.${s}" \
       "docbookxi.${s}" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/docbookxi.${s}" \
       "docbookxi.${s}" ${cat}
     # XLink + XML:
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/xlink.xsd" \
       "xlink.xsd" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/xlink.xsd" \
       "xlink.xsd" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/xml.xsd" \
       "xml.xsd" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/xml.xsd" \
       "xml.xsd" ${cat}
     ;;
   esac
  done
done

%install
DOCBOOK5DIR=$RPM_BUILD_ROOT%{_datadir}/xml/docbook5
for v in 5.0
do
mkdir -p ${DOCBOOK5DIR}/schema/dtd/$v
mkdir -p ${DOCBOOK5DIR}/schema/rng/$v
mkdir -p ${DOCBOOK5DIR}/schema/sch/$v
mkdir -p ${DOCBOOK5DIR}/schema/xsd/$v
install -m644 dtd/* ${DOCBOOK5DIR}/schema/dtd/$v
install -m644 rng/* ${DOCBOOK5DIR}/schema/rng/$v
install -m644 sch/* ${DOCBOOK5DIR}/schema/sch/$v
install -m644 xsd/* ${DOCBOOK5DIR}/schema/xsd/$v
done
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m755 tools/db4-entities.pl $RPM_BUILD_ROOT%{_bindir}
mkdir -p ${DOCBOOK5DIR}/stylesheet/upgrade
install -m644 tools/db4-upgrade.xsl ${DOCBOOK5DIR}/stylesheet/upgrade

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xml
install -m644 docbook-5.xml $RPM_BUILD_ROOT%{_sysconfdir}/xml/docbook-5.xml

%post
ROOTCATALOG=%{_sysconfdir}/xml/catalog
if [ -w $ROOTCATALOG ]
then
  for v in 5.0
  do
  %{_bindir}/xmlcatalog --noout --add "delegatePublic" \
    "-//OASIS//DTD DocBook XML ${v}//EN" \
    "file://%{_datadir}/xml/docbook5/schema/dtd/${v}/catalog.xml" \
    $ROOTCATALOG
  %{_bindir}/xmlcatalog --noout --add "delegateSystem" \
    "http://docbook.org/xml/${v}/dtd/" \
    "file://%{_datadir}/xml/docbook5/schema/dtd/${v}/catalog.xml" \
    $ROOTCATALOG
  %{_bindir}/xmlcatalog --noout --add "delegateURI" \
    "http://docbook.org/xml/${v}/dtd/" \
    "file://%{_datadir}/xml/docbook5/schema/dtd/${v}/catalog.xml" \
    $ROOTCATALOG
  %{_bindir}/xmlcatalog --noout --add "delegateURI" \
    "http://docbook.org/xml/${v}/rng/"  \
    "file://%{_datadir}/xml/docbook5/schema/rng/${v}/catalog.xml" \
    $ROOTCATALOG
  %{_bindir}/xmlcatalog --noout --add "delegateURI" \
    "http://docbook.org/xml/${v}/sch/"  \
    "file://%{_datadir}/xml/docbook5/schema/sch/${v}/catalog.xml" \
    $ROOTCATALOG
  %{_bindir}/xmlcatalog --noout --add "delegateURI" \
    "http://docbook.org/xml/${v}/xsd/"  \
    "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/catalog.xml" \
    $ROOTCATALOG
   done
fi

%postun
if [ "$1" = 0 ]; then
  ROOTCATALOG=%{_sysconfdir}/xml/catalog
  if [ -w $ROOTCATALOG ]
  then
    for v in 5.0
    do
       %{_bindir}/xmlcatalog --noout --del \
       "file://%{_datadir}/xml/docbook5/schema/dtd/${v}/catalog.xml" \
       $ROOTCATALOG
       %{_bindir}/xmlcatalog --noout --del \
       "file://%{_datadir}/xml/docbook5/schema/rng/${v}/catalog.xml" \
       $ROOTCATALOG
       %{_bindir}/xmlcatalog --noout --del \
       "file://%{_datadir}/xml/docbook5/schema/sch/${v}/catalog.xml" \
       $ROOTCATALOG
       %{_bindir}/xmlcatalog --noout --del \
       "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/catalog.xml" \
       $ROOTCATALOG
     done
  fi
fi

%files
%doc docs/* README ChangeLog
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xml/docbook-5.xml
%dir %{_datadir}/xml/docbook5/
%dir %{_datadir}/xml/docbook5/schema
%dir %{_datadir}/xml/docbook5/schema/dtd
%dir %{_datadir}/xml/docbook5/schema/rng
%dir %{_datadir}/xml/docbook5/schema/sch
%dir %{_datadir}/xml/docbook5/schema/xsd
%dir %{_datadir}/xml/docbook5/stylesheet
%dir %{_datadir}/xml/docbook5/stylesheet/upgrade
# Docbook5.0
%{_datadir}/xml/docbook5/schema/dtd/%{version}
%{_datadir}/xml/docbook5/schema/rng/%{version}
%{_datadir}/xml/docbook5/schema/sch/%{version}
%{_datadir}/xml/docbook5/schema/xsd/%{version}
%{_datadir}/xml/docbook5/stylesheet/upgrade/db4-upgrade.xsl
%{_bindir}/db4-entities.pl

%ChangeLog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 5.0-alt2_6
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 5.0-alt1_6
- update to new release by fcimport

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 5.0-alt1_5
- initial release by fcimport

