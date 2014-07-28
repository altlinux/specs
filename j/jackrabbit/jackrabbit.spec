Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          jackrabbit
Version:       2.4.2
Release:       alt2_6jpp7
Summary:       Implementation of the Content Repository for Java Technology API
Group:         Development/Java
License:       ASL 2.0
URL:           http://jackrabbit.apache.org/
Source0:       http://archive.apache.org/dist/%{name}/%{version}/%{name}-%{version}-src.zip
# force tomcat6-servlet-2.5-api apis use
Source1:       jackrabbit-depmap
# build fix for servlet 2.5
Patch0:        0001-Conform-to-newer-servlet-API.patch
# build fix for servlet 3.0
Patch1:        jackrabbit-2.4.2-servlet30.patch

BuildArch:     noarch

BuildRequires: jpackage-utils
# main deps
# javax.servlet:servlet-api:2.3
BuildRequires: tomcat-servlet-3.0-api
#BuildRequires: mvn(biz.aQute:bndlib)
#BuildRequires: mvn(commons-httpclient:commons-httpclient)
#BuildRequires: mvn(org.slf4j:slf4j-api)
#BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
# test deps
#BuildRequires: junit
#BuildRequires: mvn(ch.qos.logback:logback-classic)

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin

Requires:      jpackage-utills
Source44: import.info

%description
The Apache Jackrabbit content repository is a fully conforming implementation 
of the Content Repository for Java Technology API (JCR, specified in JSR 170 
and 283).

A content repository is a hierarchical content store with support for 
structured and unstructured content, full text search, versioning, 
transactions, observation, and more.

%package webdav
Summary:       Jackrabbit WebDAV Library
Group:         Development/Java
Requires:      jpackage-utils

%description webdav
This is the WebDAV Library component of the Apache Jackrabbit project. This 
component provides interfaces and common utility classes used for building a 
WebDAV server or client.

%package webdav-javadoc
Summary:       Javadoc for %{name}-webdav
Group:         Development/Java
Requires:      jpackage-utils

%description webdav-javadoc
This package contains the API documentation for %{name}-webdav.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# maven-local load in classpath wrong library. also using the file depmap
%pom_remove_dep javax.servlet:servlet-api %{name}-webdav
%pom_xpath_inject "pom:dependencies" "
  <dependency>
    <groupId>javax.servlet</groupId>
    <artifactId>servlet-api</artifactId>
    <version>any</version>
    <scope>system</scope>
    <systemPath>$(build-classpath tomcat-servlet-3.0-api)</systemPath>
  </dependency>" %{name}-webdav
    
%build

cd %{name}-webdav
mvn-rpmbuild -Dmaven.test.skip=true package javadoc:aggregate
#  -Dmaven.local.depmap.file="%%{SOURCE1}"

%install
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}

install -pm 644 %{name}-webdav/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-webdav.pom
install -pm 644 %{name}-webdav/target/%{name}-webdav-%{version}.jar %{buildroot}%{_javadir}/%{name}-webdav.jar
cp -rp %{name}-webdav/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}-webdav

%add_maven_depmap JPP-%{name}-webdav.pom %{name}-webdav.jar -f webdav

# We don't install the parent POM. Rempove reference to it, so that mvn-rpmbuild works
awk '/<parent>/ {skip=1} {if (!skip) print} /<\/parent>/ {skip=0}' %{name}-webdav/pom.xml \
 >%{buildroot}%{_mavenpomdir}/JPP-%{name}-webdav.pom
touch -r %{name}-webdav/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-webdav.pom

%files webdav
%{_javadir}/%{name}-webdav.jar
%{_mavendepmapfragdir}/%{name}-webdav
%{_mavenpomdir}/JPP-%{name}-webdav.pom
%doc NOTICE.txt LICENSE.txt
%doc %{name}-webdav/README.txt

%files webdav-javadoc
%{_javadocdir}/%{name}-webdav
%doc NOTICE.txt LICENSE.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4.2-alt2_6jpp7
- new release

* Tue Jul 15 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4.2-alt2_2jpp7
- fixed build

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4.2-alt1_2jpp7
- new version

* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt7_2jpp6
- dropped felix-maven2 dependency

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt6_2jpp6
- fixed build with maven3

* Sat Feb 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt5_2jpp6
- fixed build

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt4_2jpp6
- built with compat lucene24

* Fri Mar 18 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt3_2jpp6
- fixed build with new javacc5

* Sun Feb 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt2_2jpp6
- fixed build with new javacc3

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt1_2jpp6
- new version

