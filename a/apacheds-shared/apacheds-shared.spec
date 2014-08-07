Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          apacheds-shared
Version:       0.9.19
Release:       alt3_1jpp7
Summary:       Shared APIs of Apache Directory Project
Group:         Development/Java
License:       ASL 2.0
Url:           http://directory.apache.org/
# svn export http://svn.apache.org/repos/asf/directory/shared/tags/0.9.19/ apacheds-shared-0.9.19
# tar czf  apacheds-shared-0.9.19-src-svn.tar.gz  apacheds-shared-0.9.19
Source0:       apacheds-shared-0.9.19-src-svn.tar.gz
# requires antlr 2.x and change org.apache.maven.plugins maven-antlr-plugin with org.codehaus.mojo antlr-maven-plugin
Patch0:        apacheds-shared-0.9.19-antlr-plugin.patch

BuildRequires: jpackage-utils
BuildRequires: directory-project

BuildRequires: antlr
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-pool
BuildRequires: apache-mina
BuildRequires: dom4j
BuildRequires: log4j
BuildRequires: slf4j
BuildRequires: xpp3

# test deps
BuildRequires: junit

BuildRequires: antlr-maven-plugin
BuildRequires: maven-local
BuildRequires: maven-antrun-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      antlr
Requires:      apache-commons-collections
Requires:      apache-commons-io
Requires:      apache-commons-lang
Requires:      apache-commons-pool
Requires:      apache-mina
Requires:      dom4j
Requires:      log4j
Requires:      slf4j
Requires:      xpp3

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
ApacheDS is an extensible and embeddable directory server
entirely written in Java, which has been certified LDAPv3
compatible by the Open Group. Besides LDAP it supports
Kerberos 5 and the Change Password Protocol. It has been
designed to introduce triggers, stored procedures, queues and
views to the world of LDAP which has lacked these rich
constructs. 

This package contains the shared APIs of the
Apache Directory Project.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n apacheds-shared-%{version}
%patch0 -p1
# cleanup
find . -name "*.jar" -delete
find . -name "*.class" -delete

sed -i "s|<module>all</module>|<!--module>all</module-->|" pom.xml
# fix wrong permissions
chmod 644 README.txt

%build

mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-parent.pom

mkdir -p %{buildroot}%{_javadir}/apacheds

install -m 644 ldap-convert/target/shared-ldap-converter-%{version}.jar %{buildroot}%{_javadir}/apacheds/shared-ldap-converter.jar
install -pm 644 ldap-convert/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-ldap-converter.pom
%add_maven_depmap JPP.%{name}-ldap-converter.pom apacheds/shared-ldap-converter.jar

install -m 644 ldap-ldif/target/shared-ldif-%{version}.jar %{buildroot}%{_javadir}/apacheds/shared-ldif.jar
install -pm 644 ldap-ldif/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-ldif.pom
%add_maven_depmap JPP.%{name}-ldif.pom apacheds/shared-ldif.jar

for m in asn1 \
  asn1-codec \
  cursor \
  dsml-parser \
  i18n \
  ldap \
  ldap-constants \
  ldap-jndi \
  ldap-schema \
  ldap-schema-dao \
  ldap-schema-loader \
  ldap-schema-manager; do
  install -m 644 ${m}/target/shared-${m}-%{version}.jar %{buildroot}%{_javadir}/apacheds/shared-${m}.jar
  install -pm 644 ${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
%add_maven_depmap JPP.%{name}-${m}.pom apacheds/shared-${m}.jar
done

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/apacheds/shared-*.jar
%{_mavenpomdir}/JPP.%{name}-*.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE NOTICE README.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.9.19-alt3_1jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.9.19-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.19-alt1_1jpp7
- fc release

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.12-alt5_2jpp6
- fixed build with java 7

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.12-alt4_2jpp6
- use maven2-plugin-shade

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.12-alt3_2jpp6
- fixed build

* Fri Oct 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.12-alt2_2jpp6
- removed junit embedded in bouncycastle

* Sat Sep 25 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.12-alt1_2jpp6.1
- fixed build with maven 2.0.8

* Thu Sep 16 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.12-alt1_2jpp6
- new version

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5.5-alt2_2jpp5
- explicit selection of java5 compiler

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5.5-alt1_2jpp5
- converted from JPackage by jppimport script

* Thu Jan 17 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5.3-alt1_2jpp1.7
- converted from JPackage by jppimport script

