Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          shibboleth-java-support
Version:       7.1.1
Release:       alt1_5jpp8
Summary:       Java Support for Shibboleth projects
License:       ASL 2.0 and BSD
URL:           http://shibboleth.net/
# git clone git://git.shibboleth.net/java-support
# (cd java-support/ && git archive --format=tar --prefix=shibboleth-java-support-7.1.1/ 7.1.1 | xz > ../shibboleth-java-support-7.1.1.tar.xz)
Source0:       %{name}-%{version}.tar.xz
Patch0:        shibboleth-java-support-7.1.1-port-to-servlet-3.1.patch

BuildRequires: maven-local
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(ch.qos.logback:logback-core)
BuildRequires: mvn(com.beust:jcommander)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(joda-time:joda-time)
BuildRequires: mvn(net.shibboleth:parent-v3:pom:)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.apache.httpcomponents:httpclient-cache)
BuildRequires: mvn(org.apache.velocity:velocity)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires: mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-test)
# test deps listed in net.shibboleth:parent-v3:pom:
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.slf4j:jul-to-slf4j)
BuildRequires: mvn(org.slf4j:log4j-over-slf4j)
BuildRequires: mvn(org.testng:testng)
BuildRequires: mvn(xmlunit:xmlunit)

BuildArch:     noarch
Source44: import.info

%description
Java Support for Shibboleth projects.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

# Use web connection
# UnknownHostException: buildvm-19.phx2.fedoraproject.org: buildvm-19.phx2.fedoraproject.org: unknown error
rm src/test/java/net/shibboleth/utilities/java/support/net/IPRangeTest.java
# AssertionError only on koji builders
rm src/test/java/net/shibboleth/utilities/java/support/collection/LazyMapTest.java \
 src/test/java/net/shibboleth/utilities/java/support/collection/ClassToInstanceMultiMapTest.java \
 src/test/java/net/shibboleth/utilities/java/support/httpclient/IdleConectionSweeperTest.java

%mvn_file : %{name} java-support
%mvn_package :java-support::tests:

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc doc/RELEASE-NOTES.txt
%doc doc/LICENSE.txt doc/NOTICE.txt doc/OWASP-LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc doc/LICENSE.txt doc/NOTICE.txt doc/OWASP-LICENSE.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 7.1.1-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 7.1.1-alt1_4jpp8
- new jpp release

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.1-alt1_3jpp8
- new version

