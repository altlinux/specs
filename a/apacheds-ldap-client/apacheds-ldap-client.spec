Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          apacheds-ldap-client
Version:       0.1
Release:       alt2_10jpp8
Summary:       ApacheDS LDAP Client API
License:       ASL 2.0
Url:           http://directory.apache.org/
# svn export http://svn.apache.org/repos/asf/directory/clients/ldap/tags/0.1/ apacheds-ldap-client-0.1
# tar czf apacheds-ldap-client-0.1-src-svn.tar.gz apacheds-ldap-client-0.1
Source0:       apacheds-ldap-client-0.1-src-svn.tar.gz
# apacheds-ldap-client package don't include the license file
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt
# use the apacheds shared ldap apis
Patch0:        apacheds-ldap-client-0.1-api-LdapConnection.patch

BuildRequires: apache-commons-pool
BuildRequires: apache-mina
BuildRequires: apacheds-shared
BuildRequires: directory-project
BuildRequires: junit
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

This package contains the ApacheDS LDAP Client API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
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

%mvn_file :ldap-client-api apacheds/ldap-client-api

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_10jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_2jpp7
- fc release

