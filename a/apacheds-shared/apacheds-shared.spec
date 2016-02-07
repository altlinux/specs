Epoch: 0
Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          apacheds-shared
Version:       0.9.19
Release:       alt3_9jpp8
Summary:       Shared APIs of Apache Directory Project
License:       ASL 2.0
Url:           http://directory.apache.org/
# svn export http://svn.apache.org/repos/asf/directory/shared/tags/0.9.19/ apacheds-shared-0.9.19
# tar czf  apacheds-shared-0.9.19-src-svn.tar.gz  apacheds-shared-0.9.19
Source0:       apacheds-shared-0.9.19-src-svn.tar.gz
# requires antlr 2.x and change org.apache.maven.plugins maven-antlr-plugin with org.codehaus.mojo antlr-maven-plugin
Patch0:        apacheds-shared-0.9.19-antlr-plugin.patch

BuildRequires: antlr
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-pool
BuildRequires: apache-mina apache-mina-mina-core
BuildRequires: directory-project
BuildRequires: dom4j
BuildRequires: log4j12
BuildRequires: slf4j
BuildRequires: xpp3
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
# test deps
BuildRequires: junit

BuildRequires: antlr-maven-plugin
BuildRequires: maven-local

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
Group: Development/Java
Summary:       Javadoc for %{name}
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

rm -r ldap-schema-manager/src/test/java/org/apache/directory/shared/ldap/schema/loader/ldif/SchemaManagerLoadTest.java

%mvn_file :shared-asn1 apacheds/shared-asn1
%mvn_file :shared-asn1-codec apacheds/shared-asn1-codec
%mvn_file :shared-cursor apacheds/shared-cursor
%mvn_file :shared-dsml-parser apacheds/shared-dsml-parser
%mvn_file :shared-i18n apacheds/shared-i18n
%mvn_file :shared-ldap apacheds/shared-ldap
%mvn_file :shared-ldap-constants apacheds/shared-ldap-constants
%mvn_file :shared-ldap-converter apacheds/shared-ldap-converter
%mvn_file :shared-ldap-jndi apacheds/shared-ldap-jndi
%mvn_file :shared-ldap-schema apacheds/shared-ldap-schema
%mvn_file :shared-ldap-schema-dao apacheds/shared-ldap-schema-dao
%mvn_file :shared-ldap-schema-loader apacheds/shared-ldap-schema-loader
%mvn_file :shared-ldap-schema-manager apacheds/shared-ldap-schema-manager
%mvn_file :shared-ldif apacheds/shared-ldif

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.txt
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.19-alt3_9jpp8
- java 8 mass update

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.9.19-alt3_3jpp7
- new release

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

