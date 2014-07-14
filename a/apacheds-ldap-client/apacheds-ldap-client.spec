BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          apacheds-ldap-client
Version:       0.1
Release:       alt2_2jpp7
Summary:       ApacheDS LDAP Client API
Group:         Development/Java
License:       ASL 2.0
Url:           http://directory.apache.org/
# svn export http://svn.apache.org/repos/asf/directory/clients/ldap/tags/0.1/ apacheds-ldap-client-0.1
# tar czf apacheds-ldap-client-0.1-src-svn.tar.gz apacheds-ldap-client-0.1
Source0:       apacheds-ldap-client-0.1-src-svn.tar.gz
# apacheds-ldap-client package don't include the license file
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt
# use the apacheds shared ldap apis
Patch0:        apacheds-ldap-client-0.1-api-LdapConnection.patch

BuildRequires: jpackage-utils
BuildRequires: directory-project

BuildRequires: apache-commons-pool
BuildRequires: apache-mina
BuildRequires: apacheds-shared

# test deps
BuildRequires: junit

BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      apache-commons-pool
Requires:      apache-mina
Requires:      apacheds-shared


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

This package contains the ApacheDS LDAP Client API.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p0
# cleanup
find . -name "*.jar" -delete
find . -name "*.class" -delete

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%build

mvn-rpmbuild install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}.pom
%add_maven_depmap JPP.%{name}.pom

mkdir -p %{buildroot}%{_javadir}/apacheds

for m in ldap-client-api; do
  install -m 644 ${m}/target/${m}-%{version}.jar %{buildroot}%{_javadir}/apacheds/${m}.jar
  install -pm 644 ${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.apacheds-${m}.pom
%add_maven_depmap JPP.apacheds-${m}.pom apacheds/${m}.jar
done

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/apacheds/*.jar
%{_mavenpomdir}/JPP.apacheds-*.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE-2.0.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE-2.0.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_2jpp7
- fc release

