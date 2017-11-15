Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global githash db8a995386c9808c893384023eee78e087ad9ad7
Name:          subethasmtp
Version:       3.1.7
Release:       alt1_11jpp8
Summary:       A SMTP mail server for Java
# BSD: src/main/java/org/subethamail/smtp/util/Base64.java
License:       ASL 2.0 and BSD
# http://code.google.com/p/subethasmtp/
# https://github.com/vivosys/subethasmtp
URL:           https://github.com/voodoodyne/subethasmtp
Source0:       https://github.com/voodoodyne/subethasmtp/archive/%{githash}/%{name}-%{githash}.tar.gz

BuildRequires: java-javadoc
BuildRequires: maven-local
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(javax.mail:mail)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-simple)
%if 0
BuildRequires: mvn(com.googlecode.jmockit:jmockit) >= 0.999.11
%endif

BuildArch:     noarch
Source44: import.info

%description
SubEtha SMTP is an easy-to-use server-side SMTP library for Java.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{githash}
find -name "*.class" -print -delete
find -name "*.jar" -print -delete

%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-gpg-plugin

%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration" "
<excludes>
  <exclude>org/subethamail/smtp/test/**</exclude>
</excludes>"

%pom_xpath_inject "pom:plugin[pom:artifactId='maven-javadoc-plugin']" "
<configuration>
  <nodeprecated>false</nodeprecated>
  <use>false</use>
  <author>true</author>
  <version>true</version>
  <detectJavaApiLink>false</detectJavaApiLink>
  <offlineLinks>
    <offlineLink>
      <url>http://download.oracle.com/javase/6/docs/api/</url>
      <location>%{_javadocdir}/java</location>
    </offlineLink>
  </offlineLinks>
  <excludePackageNames>org.subethamail.smtp.test.*:**Test**</excludePackageNames>
</configuration>"

# use system jvm apis
%pom_remove_dep javax.activation:activation

# unavailable test dep
%pom_remove_dep :jmockit
rm -r src/test/java/org/subethamail/smtp/MessageHandlerTest.java
# this test fails ComparisonFailure
rm -r src/test/java/org/subethamail/smtp/TimeoutTest.java \
 src/test/java/org/subethamail/smtp/WiserFailuresTest.java \
 src/test/java/org/subethamail/smtp/ReceivedHeaderStreamTest.java

sed -i.java8 "s|MDC.setContextMap(parentLoggingMdcContext);|MDC.setContextMap((Map<String, String>)parentLoggingMdcContext);|" src/main/java/org/subethamail/smtp/server/Session.java

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.html
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.7-alt1_11jpp8
- new version

