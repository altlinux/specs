# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
%define oldname axiom
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           ws-commons-axiom
Version:        1.2.12
Release:        alt2_5jpp7
Epoch:          0
Summary:        Axis Object Model
License:        ASL 2.0
Url:            http://ws.apache.org/commons/axiom/
Group:          Development/Java
# svn export http://svn.apache.org/repos/asf/webservices/commons/tags/axiom/1.2.12/ axiom-1.2.12
# tar caf axiom-1.2.12.tar.xz axiom-1.2.12
Source0:        %{oldname}-%{version}.tar.xz
# This patch makes several build changes:
# 1) Remove deps on a JAF implementation -- this is built into openjdk 7
# 2) Use the javamail and stax implementations already in Fedora
# 3) Remove maven plugins not present in Fedora, which do not impact the build process
# 4) Remove modules which require additional dependencies not yet in Fedora
Patch0:         axiom-build-fixes.patch
BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  junit
BuildRequires:  maven-local
BuildRequires:  apache-rat-plugin
BuildRequires:  bea-stax-api
BuildRequires:  javamail
BuildRequires:  apache-commons-logging
BuildRequires:  jaxen
BuildRequires:  jdepend
BuildRequires:  woodstox-core
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-jaxp-1.3-apis
BuildRequires:  xmlunit
Requires:       bea-stax-api
Requires:       xml-commons-jaxp-1.3-apis
Requires:       javamail >= 0:1.4
Requires:       apache-commons-logging
Requires:       jaxen
Requires:       woodstox-core
Requires:       xerces-j2
Requires:       jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
AXIOM stands for AXis Object Model (also known as OM - Object Model)
and refers to the XML info-set model that was initially developed for
Apache Axis2.

%package javadoc
Summary:        API Documentation for %{oldname}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -n %{oldname}-%{version} -q
%patch0 -p1
rm -rf modules/axiom-jaxen-testsuite/src/main/

# fix eol
%{__perl} -pi -e 's/\r$//g' README.txt NOTICE.txt RELEASE-NOTE.txt

%build
# Skipping tests for now due to many extra deps
mvn-rpmbuild -Dmaven.test.skip install

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/axiom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

install -m 644 target/%{oldname}*.jar \
           $RPM_BUILD_ROOT%{_javadir}/%{oldname}/%{oldname}.jar
install -pm 644 pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{oldname}-%{oldname}.pom
%add_maven_depmap JPP.%{oldname}-%{oldname}.pom %{oldname}/%{oldname}.jar
install -pm 644 modules/%{oldname}-parent/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{oldname}-parent.pom
%add_maven_depmap JPP.%{oldname}-parent.pom

for mod in axiom-api axiom-dom axiom-impl axiom-c14n; do
    install -m 644 modules/${mod}/target/${mod}-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{oldname}/${mod}.jar
    install -pm 644 modules/${mod}/pom.xml \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{oldname}-${mod}.pom
    %add_maven_depmap JPP.%{oldname}-${mod}.pom %{oldname}/${mod}.jar
done

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}
cp -rp target/apidocs $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}

%files
%doc *.txt
%{_javadir}/axiom/*.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{oldname}

%changelog
* Sat Aug 02 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.12-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.12-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.12-alt1_3jpp7
- new version

* Wed Mar 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.8-alt3_2jpp6
- fixed build with maven3

* Wed Jan 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.8-alt2_2jpp6
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.8-alt1_2jpp6
- new version

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.7-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.7-alt1_2jpp5
- converted from JPackage by jppimport script

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.4-alt1_1jpp1.7
- converted from JPackage by jppimport script

