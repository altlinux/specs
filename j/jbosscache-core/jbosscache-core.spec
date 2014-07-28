# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:       jbosscache-core
Version:    3.2.8
Release:    alt1_7jpp7
Summary:    JBoss objects cache

Group:      Development/Java
License:    LGPLv2+
URL:        http://jboss.org/jbosscache
# svn export http://anonsvn.jboss.org/repos/jbosscache/core/tags/3.2.8.GA jbosscache-core-3.2.8
# tar cJf jbosscache-core-3.2.8.tar.xz jbosscache-core-3.2.8
Source0:    %{name}-%{version}.tar.xz
Patch0:     %{name}-jgroups212.patch

BuildRequires:  maven-local
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-surefire
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  jbosscache-common-parent
BuildRequires:  jdbm
BuildRequires:  c3p0
BuildRequires:  jcip-annotations
BuildRequires:  jgroups212
BuildRequires:  jpackage-utils
BuildRequires:  jboss-common-core
BuildRequires:  apache-commons-logging
BuildRequires:  jboss-transaction-1.1-api

Requires:       jpackage-utils
Requires:       jgroups212
Requires:       jboss-transaction-1.1-api
Requires:       jboss-common-core
Requires:       jdbm
Requires:       c3p0
Requires:       jcip-annotations
Requires:       apache-commons-logging

BuildArch:      noarch
Source44: import.info

%description
A library that caches frequently accessed Java objects in order to
dramatically improve the performance of applications.

%package javadoc
Summary:   Javadoc for %{name}
Group:     Development/Java
Requires:  jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
find . -name \*.jar -exec rm -f {} \;

# Remove optional dependencies
%pom_remove_dep com.sleepycat:je
%pom_remove_dep net.noderunner:amazon-s3

# Remove code for amazon-s3 and berkleydb-je dependencies
rm -rf src/main/java/org/jboss/cache/loader/{s3,bdbje}

# Fix JBoss transaction API dependency
sed -i -e "s|<groupId>org.jboss.javaee</groupId>|<groupId>org.jboss.spec.javax.transaction</groupId>|" \
    -e "s|<artifactId>jboss-transaction-api</artifactId>|<artifactId>jboss-transaction-api_1.1_spec</artifactId>|" \
    -e "s|<version>1.0.1.GA</version>|<version>1.0.1-SNAPSHOT</version>|" pom.xml

%patch0 -p1

%build
# Not running tests due to missing dependencies
mvn-rpmbuild install -Dmaven.test.skip=true \
    -Dproject.build.sourceEncoding=UTF-8 \
    javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%doc README-*.txt src/main/release/LICENSE-lgpl-2.1.txt src/main/release/README.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc src/main/release/LICENSE-lgpl-2.1.txt
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt1_7jpp7
- new release

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt1_5jpp7
- new fc release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt1_4jpp7
- new fc release

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt1_3jpp7
- new version

