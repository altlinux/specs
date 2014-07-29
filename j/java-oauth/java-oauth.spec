# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global oname oauth
Name:          java-oauth
Version:       20100601
Release:       alt2_5jpp7
Summary:       An open protocol to allow API authentication
Group:         Development/Java
License:       ASL 2.0
Url:           http://code.google.com/p/oauth/
# svn export http://oauth.googlecode.com/svn/code/java oauth-20100601
# find oauth-20100601 -name "*.bat" -delete
# find oauth-20100601 -name "*.class" -delete
# find oauth-20100601 -name "*.jar" -delete
# tar czf oauth-20100601-clean-src-svn.tar.gz oauth-20100601
Source0:       oauth-20100601-clean-src-svn.tar.gz

# remove unavailable test deps org.mortbay.jetty jetty-embedded 6.1.11
# unavailable deps disable this modules: core-old example test

# x test
# org.mortbay.jetty jetty-embedded 6.1.11

# x oauth-example-desktop
# org.codehaus.mojo appassembler-maven-plugin
# org.mortbay.jetty jetty-embedded 6.1.11

# x oauth-example-provider oauth-example-consumer
# org.mortbay.jetty jetty-maven-plugin

Patch0:        oauth-20100601-poms.patch
BuildRequires: jpackage-utils

BuildRequires: httpcomponents-client
BuildRequires: jakarta-commons-httpclient
BuildRequires: tomcat-servlet-3.0-api

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin

Requires:      httpcomponents-client
Requires:      jakarta-commons-httpclient
Requires:      tomcat-servlet-3.0-api

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
An open protocol to allow API authentication
in a simple and standard method from desktop and
web applications.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1

%build
# unavailable test deps
mvn-rpmbuild -Dmaven.test.skip=true -Dproject.build.sourceEncoding=UTF-8 install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}/%{oname}
install -pm 644 core/commons/target/%{oname}-%{version}.jar %{buildroot}%{_javadir}/%{oname}/%{oname}.jar
install -pm 644 core/consumer/target/%{oname}-consumer-%{version}.jar %{buildroot}%{_javadir}/%{oname}/%{oname}-consumer.jar
install -pm 644 core/httpclient3/target/%{oname}-httpclient3-%{version}.jar %{buildroot}%{_javadir}/%{oname}/%{oname}-httpclient3.jar
install -pm 644 core/httpclient4/target/%{oname}-httpclient4-%{version}.jar %{buildroot}%{_javadir}/%{oname}/%{oname}-httpclient4.jar
install -pm 644 core/provider/target/%{oname}-provider-%{version}.jar %{buildroot}%{_javadir}/%{oname}/%{oname}-provider.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{oname}-parent.pom
install -pm 644 core/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{oname}-core-parent.pom
install -pm 644 core/commons/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{oname}-%{oname}.pom
install -pm 644 core/consumer/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{oname}-%{oname}-consumer.pom
install -pm 644 core/httpclient3/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{oname}-%{oname}-httpclient3.pom
install -pm 644 core/httpclient4/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{oname}-%{oname}-httpclient4.pom
install -pm 644 core/provider/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{oname}-%{oname}-provider.pom

%add_maven_depmap JPP.%{oname}-parent.pom
%add_maven_depmap JPP.%{oname}-core-parent.pom
%add_maven_depmap JPP.%{oname}-%{oname}.pom %{oname}/%{oname}.jar
%add_maven_depmap JPP.%{oname}-%{oname}-consumer.pom %{oname}/%{oname}-consumer.jar
%add_maven_depmap JPP.%{oname}-%{oname}-httpclient3.pom %{oname}/%{oname}-httpclient3.jar
%add_maven_depmap JPP.%{oname}-%{oname}-httpclient4.pom %{oname}/%{oname}-httpclient4.jar
%add_maven_depmap JPP.%{oname}-%{oname}-provider.pom %{oname}/%{oname}-provider.jar

mv %{buildroot}%{_mavendepmapfragdir}/%{name} %{buildroot}%{_mavendepmapfragdir}/%{oname}

mkdir -p %{buildroot}%{_javadocdir}/%{oname}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{oname}

%files
%{_javadir}/%{oname}/%{oname}*.jar
%{_mavenpomdir}/JPP.%{oname}*.pom
%{_mavendepmapfragdir}/%{oname}
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/%{oname}
%doc LICENSE.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 20100601-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 20100601-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 20100601-alt1_3jpp7
- new version

