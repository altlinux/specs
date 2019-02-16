Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 28
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora}
%bcond_with datanucleus_plugin
%endif

Name:          google-http-java-client
Version:       1.22.0
Release:       alt1_5jpp8
Summary:       Google HTTP Client Library for Java
License:       ASL 2.0
URL:           https://github.com/google/google-http-java-client/
Source0:       https://github.com/google/google-http-java-client/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.google.code.findbugs:findbugs)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.protobuf:protobuf-java)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(dom4j:dom4j)
BuildRequires: mvn(javax.jdo:jdo2-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(mysql:mysql-connector-java)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-checkstyle-plugin)
BuildRequires: mvn(org.codehaus.jackson:jackson-core-asl)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.datanucleus:datanucleus-core)
BuildRequires: mvn(org.datanucleus:datanucleus-api-jdo)
BuildRequires: mvn(org.datanucleus:datanucleus-rdbms)
%if %{with datanucleus_plugin}
BuildRequires: mvn(org.datanucleus:datanucleus-maven-plugin)
%endif
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(xpp3:xpp3)
BuildRequires: /usr/bin/protoc

# google-http-client/src/main/java/com/google/api/client/util/Base64.java
Provides:      bundled(apache-commons-codec) = 1.8

BuildArch:     noarch
Source44: import.info

%description
Google HTTP Client Library for Java. Functionality
that works on all supported Java platforms,
including Java 5 (or higher) desktop (SE) and
web (EE), Android, and Google App Engine.

%package findbugs
Group: Development/Java
Summary:       Google HTTP Client Findbugs plugin

%description findbugs
Google APIs Client Library Findbugs custom plugin.

%package gson
Group: Development/Java
Summary:       Google HTTP Client GSON extensions

%description gson
GSON extensions to the Google HTTP Client Library for Java.

%package jackson
Group: Development/Java
Summary:       Google HTTP Client Jackson extensions

%description jackson
Jackson extensions to the Google HTTP Client Library for Java.

%package jackson2
Group: Development/Java
Summary:      Google HTTP Client Jackson 2 extensions

%description jackson2
Jackson 2 extensions to the Google HTTP Client Library for Java.

%package jdo
Group: Development/Java
Summary:       Google HTTP Client JDO extensions

%description jdo
JDO extensions to the Google HTTP Client Library for Java.

%package parent
Group: Development/Java
Summary:       Google HTTP Client Parent POM

%description parent
Parent POM for the Google HTTP Client Library for Java.

%package protobuf
Group: Development/Java
Summary:       Google HTTP Client Protocol Buffer extensions

%description protobuf
Protocol Buffer extensions to the Google HTTP Client Library for Java.

%package test
Group: Development/Java
Summary:       Google HTTP Client Test support

%description test
Shared classes used for testing of artifacts in the
Google HTTP Client Library for Java.

%package xml
Group: Development/Java
Summary:       Google HTTP Client XML extensions

%description xml
XML extensions to the Google HTTP Client Library for Java.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin
%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :findbugs-maven-plugin
%pom_remove_plugin -r :maven-deploy-plugin

%pom_remove_plugin :maven-release-plugin

%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:executions"

# kr.motd.maven:os-maven-plugin:1.4.0.Final
%pom_xpath_remove -r "pom:build/pom:extensions"

%pom_disable_module google-http-client-assembly
%pom_disable_module google-http-client-appengine
%pom_disable_module google-http-client-android
%pom_disable_module samples/dailymotion-simple-cmdline-sample
%pom_disable_module samples/googleplus-simple-cmdline-sample

%pom_change_dep -r :guava-jdk5 :guava

%pom_xpath_remove "pom:dependency[pom:groupId='commons-codec']/pom:scope" google-http-client

# Disable bundle of commons-codec & guava
%pom_remove_plugin org.sonatype.plugins:jarjar-maven-plugin google-http-client
%pom_remove_plugin :maven-antrun-plugin google-http-client

%pom_remove_dep com.google.android:android google-http-client

%if %{without datanucleus_plugin}
%pom_remove_plugin :maven-datanucleus-plugin
%pom_remove_plugin :maven-datanucleus-plugin google-http-client-jdo
%else
# Generate: ENHANCED (PersistenceCapable) : com.google.api.client.extensions.jdo.JdoDataStoreFactory$JdoValue
# Upgrade datanucleus-maven-plugin refs
%pom_xpath_set "pom:plugins/pom:plugin[pom:groupId='org.datanucleus']/pom:artifactId" datanucleus-maven-plugin
%pom_xpath_set "pom:plugins/pom:plugin[pom:groupId='org.datanucleus']/pom:artifactId" datanucleus-maven-plugin google-http-client-jdo
# Fix datanucleus-maven-plugin runtime deps
# Error: Could not find or load main class org.datanucleus.enhancer.DataNucleusEnhancer
%pom_xpath_inject "pom:plugins/pom:plugin[pom:groupId='org.datanucleus']" "
<dependencies>
    <dependency>
      <groupId>org.datanucleus</groupId>
      <artifactId>datanucleus-core</artifactId>
      <version>3.2.9</version>
    </dependency>
    <dependency>
      <groupId>org.datanucleus</groupId>
      <artifactId>datanucleus-api-jdo</artifactId>
      <version>3.2.6</version>
    </dependency>
</dependencies>" google-http-client-jdo
%endif

# com.google.protobuf.tools:maven-protoc-plugin:0.4.2
%pom_remove_plugin com.google.protobuf.tools:maven-protoc-plugin google-http-client-protobuf
%pom_add_plugin org.codehaus.mojo:build-helper-maven-plugin:1.5 google-http-client-protobuf "
<executions>
   <execution>
      <id>add-test-source</id>
      <phase>generate-test-sources</phase>
      <goals>
         <goal>add-test-source</goal>
      </goals>
      <configuration>
         <sources>
            <source>target/generated-test-sources</source>
         </sources>
      </configuration>
   </execution>
</executions>"
%pom_add_plugin org.apache.maven.plugins:maven-antrun-plugin:1.8 google-http-client-protobuf '
<executions>
  <execution>
     <id>generate-sources</id>
     <phase>generate-sources</phase>
     <configuration>
       <target>
         <mkdir dir="target/generated-test-sources"/>
         <exec failonerror="true" executable="protoc">
            <arg value="--java_out=target/generated-test-sources"/>
            <arg value="src/test/proto/simple_proto.proto"/>
         </exec>
       </target>
     </configuration>
     <goals>
       <goal>run</goal>
     </goals>
  </execution>
</executions>'

# Disable default-jar execution of maven-jar-plugin, which is causing
# problems with version 3.0.0 of the plugin.
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions" "
<execution>
 <id>default-jar</id>
 <phase>skip</phase>
</execution>" google-http-client-jdo

# UnknownHostException: www.test.url: Name or service not known
rm -r google-http-client/src/test/java/com/google/api/client/http/apache/ApacheHttpTransportTest.java
# UrlEncodedContentTest.testWriteTo:47->subtestWriteTo:54 expected:<[username=un&password=password123%%3B%%7B%%7D]>
# but was:<[password=password123%%3B%%7B%%7D&username=un]>
#rm -r google-http-client/src/test/java/com/google/api/client/http/UrlEncodedContentTest.java

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-google-http-client
%doc README.md
%doc --no-dereference LICENSE

%files findbugs -f .mfiles-google-http-client-findbugs
%files gson -f .mfiles-google-http-client-gson
%files jackson -f .mfiles-google-http-client-jackson
%files jackson2 -f .mfiles-google-http-client-jackson2
%files jdo -f .mfiles-google-http-client-jdo
%files parent -f .mfiles-google-http-client-parent
%files protobuf -f .mfiles-google-http-client-protobuf
%files test -f .mfiles-google-http-client-test
%files xml -f .mfiles-google-http-client-xml

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.22.0-alt1_5jpp8
- fc29 update

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.22.0-alt1_4jpp8
- new version

