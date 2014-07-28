Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          ehcache-core
Version:       2.6.0
Release:       alt2_5jpp7
Summary:       Easy Hibernate Cache
Group:         Development/Java
License:       ASL 2.0
URL:           http://ehcache.org/
# svn export http://svn.terracotta.org/svn/ehcache/tags/ehcache-core-2.6.0
# find ehcache-core-2.6.0 -name '*.jar' -delete
# ehcache-core-2.6.0/tools/maven-ant-tasks-2.0.7.jar
# find ehcache-core-2.6.0 -name '*.class' -delete
# tar czf ehcache-core-2.6.0-clean-src-svn.tar.gz ehcache-core-2.6.0
Source0:       %{name}-%{version}-clean-src-svn.tar.gz
# force use tomcat 7.x apis
Source1:       %{name}-%{version}-depmap
# remove gmaven-plugin maven-checkstyle-plugin
# fix java.vendor
# add servlet-api version
Patch0:        %{name}-%{version}-pom.patch
# Don't use buildnumber-plugin, because jna is required (and currently broken)
Patch1:        %{name}-%{version}-disable-buildnumber-plugin.patch
# circular deps
# org.hibernate hibernate-ehcache 3.3.2.GA
# unavailable deps
# net.sf.hibernate hibernate
Patch2:        %{name}-%{version}-remove-unavailable-test-deps.patch

BuildRequires: ehcache-parent
BuildRequires: jpackage-utils

BuildRequires: geronimo-jta
BuildRequires: hibernate3 >= 3.6.10-7
BuildRequires: ehcache-sizeof-agent
BuildRequires: slf4j
BuildRequires: tomcat-servlet-3.0-api

# TODO test
#BuildRequires: apache-commons-logging
#BuildRequires: mvn(org.hibernate:hibernate-ehcache)
#BuildRequires: bsh
#BuildRequires: btm
#BuildRequires: derby
#BuildRequires: dom4j
#BuildRequires: hamcrest12
#BuildRequires: javassist
#BuildRequires: junit4
#BuildRequires: mockito
#BuildRequires: xsom

BuildRequires: maven-local
BuildRequires: maven-assembly-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: rmic-maven-plugin
BuildRequires: xml-maven-plugin
BuildRequires: plexus-resources

Requires:      ehcache-sizeof-agent
Requires:      geronimo-jta
Requires:      hibernate3 >= 3.6.10-7
Requires:      slf4j
Requires:      tomcat-servlet-3.0-api

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Ehcache is a pure Java, in-process cache.

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
%patch1 -p0
%patch2 -p0

# Make sure we require version '3' of Hibernate
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:groupId = 'org.hibernate']/pom:version"
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:groupId = 'org.hibernate']" "<version>3</version>"
%build

# tests skipped. cause: missing dependencies
mvn-rpmbuild -Dmaven.local.depmap.file="%{SOURCE1}" -Dmaven.test.skip=true install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc src/assemble/EHCACHE-CORE-LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc src/assemble/EHCACHE-CORE-LICENSE.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt1_2jpp7
- new version

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_1jpp6
- new version

