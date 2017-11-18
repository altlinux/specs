BuildRequires: apache-parent
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          uima-parent-pom
Version:       10
Release:       alt2_3jpp8
Summary:       Apache UIMA Parent POM
License:       ASL 2.0
URL:           http://uima.apache.org/
Source0:       https://github.com/apache/uima-build/archive/parent-pom-%{version}.tar.gz
# uima-parent-pom package don't include the license file
# reported @ https://issues.apache.org/jira/browse/UIMA-3575
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local
BuildRequires: mvn(ant-contrib:ant-contrib)
BuildRequires: mvn(jakarta-regexp:jakarta-regexp)
BuildRequires: mvn(org.apache.ant:ant-apache-regexp)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)

BuildArch:     noarch
Source44: import.info

%description
UIMA (Unstructured Information Management Architecture).
UIMA promotes community development and reuse of annotators
that extract meta-data from unstructured information (text,
audio, video, etc.); it provides for externalized declaration of
type systems, component configuration, aggregation, and more,
supports scalablity, and provides tooling.

This package provides Parent for Apache UIMA Projects.

%prep
%setup -q -n uima-build-parent-pom-%{version}

%pom_xpath_remove pom:Embed-Dependency
%pom_xpath_remove pom:Embed-Directory
%pom_xpath_remove pom:Bundle-ClassPath
%pom_xpath_set pom:Include-Resource '{maven-resources}'
# Deprecated entry
%pom_xpath_remove pom:Bundle-RequiredExecutionEnvironment

%pom_remove_plugin org.apache.uima:uima-build-helper-maven-plugin
%pom_remove_plugin com.agilejava.docbkx:docbkx-maven-plugin
%pom_remove_plugin :maven-changes-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-remote-resources-plugin
%pom_remove_plugin :maven-javadoc-plugin

# unavailable deps org.apache.uima:uima-docbook-olink:zip:olink:1-SNAPSHOT
# https://svn.apache.org/repos/asf/uima/build/trunk/uima-docbook-olink/
%pom_xpath_remove "pom:profiles/pom:profile[pom:id = 'process-docbook']"
# Unavailable deps
%pom_xpath_remove "pom:profiles/pom:profile[pom:id = 'build-eclipse-update-subsite']"
%pom_xpath_remove "pom:profiles/pom:profile[pom:id = 'build distribution']"

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt README.txt

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.txt
%doc LICENSE-2.0.txt

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 10-alt2_3jpp8
- added BR: apache-parent for javapackages 5

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 10-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 10-alt1_2jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 8-alt1_8jpp8
- java 8 mass update

