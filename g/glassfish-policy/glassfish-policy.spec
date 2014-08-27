Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
%global oname policy
Name:          glassfish-policy
Version:       2.3.1
Release:       alt1_3jpp7
Summary:       GlassFish WS-Policy implementation
License:       CDDL or GPLv2 with exceptions
URL:           http://policy.java.net/
# svn export https://svn.java.net/svn/policy~policy/tags/policy-2.3.1
# tar czf policy-2.3.1-src-svn.tar.gz policy-2.3.1
Source0:       %{oname}-%{version}-src-svn.tar.gz

BuildRequires: jvnet-parent

BuildRequires: bea-stax-api
BuildRequires: istack-commons
BuildRequires: txw2
BuildRequires: woodstox-core

# test deps
BuildRequires: junit

# BuildRequires: buildnumber-maven-plugin
BuildRequires: maven-local
BuildRequires: maven-antrun-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-surefire-provider-junit4
# BuildRequires: svn

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

%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-resources-plugin']" "<version>any</version>"
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='cobertura-maven-plugin']" "<version>any</version>"
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-jar-plugin']" "<version>any</version>"
%pom_xpath_inject "pom:reporting/pom:plugins/pom:plugin[pom:artifactId ='maven-javadoc-plugin']" "<version>any</version>"
%pom_xpath_inject "pom:reporting/pom:plugins/pom:plugin[pom:artifactId ='maven-surefire-report-plugin']" "<version>any</version>"
%pom_xpath_inject "pom:reporting/pom:plugins/pom:plugin[pom:artifactId ='maven-jxr-plugin']" "<version>any</version>"
%pom_xpath_inject "pom:reporting/pom:plugins/pom:plugin[pom:artifactId ='cobertura-maven-plugin']" "<version>any</version>"

sed -i 's/${artifactId}/${project.artifactId}/' pom.xml

iconv -f iso8859-1 -t utf-8 LICENSE.txt > LICENSE.txt.conv && mv -f LICENSE.txt.conv LICENSE.txt
sed -i 's/\r//' LICENSE.txt

%build

%mvn_file :%{oname} %{name}
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt Licenses/license-policy.html

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt Licenses/license-policy.html

%changelog
* Thu Aug 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_3jpp7
- new release

