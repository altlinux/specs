Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global oname policy
Name:          glassfish-policy
Version:       2.5
Release:       alt1_5jpp8
Summary:       GlassFish WS-Policy implementation
License:       CDDL or GPLv2 with exceptions
URL:           http://policy.java.net/
# svn export https://svn.java.net/svn/policy~policy/tags/policy-2.5
# tar cJf policy-2.5.tar.xz policy-2.5
Source0:       %{oname}-%{version}.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(com.sun.istack:istack-commons-buildtools)
BuildRequires: mvn(com.sun.istack:istack-commons-runtime)
BuildRequires: mvn(com.sun.xml.txw2:txw2)
BuildRequires: mvn(javax.xml.stream:stax-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.codehaus.woodstox:woodstox-core-asl)
#BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
#BuildRequires: mvn(org.apache.maven.plugins:maven-deploy-plugin)

BuildArch:     noarch
Source44: import.info

%description
The policy project provides the WS-Policy implementation
for Project Metro.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}
find -name '*.jar' -delete
find -name '*.class' -delete

%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.glassfish.build:gfnexus-maven-plugin
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-deploy-plugin


sed -i 's/${artifactId}/${project.artifactId}/' pom.xml

iconv -f iso8859-1 -t utf-8 LICENSE.txt > LICENSE.txt.conv && mv -f LICENSE.txt.conv LICENSE.txt
sed -i 's/\r//' LICENSE.txt

%mvn_file :%{oname} %{name}

%build
# https://github.com/FasterXML/woodstox/issues/10
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt Licenses/license-policy.html

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt Licenses/license-policy.html

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_5jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_4jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_3jpp8
- java 8 mass update

* Thu Aug 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_3jpp7
- new release

