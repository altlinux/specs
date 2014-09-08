Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          seam-parent
Version:       19
Release:       alt1_6jpp7
Summary:       The parent for Seam modules
License:       ASL 2.0
URL:           http://www.seamframework.org/
Source0:       https://github.com/seam/parent/archive/%{version}.tar.gz
# seam-parent package don't include the license file
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local
BuildArch:     noarch
Source44: import.info

%description
Parent for seamframework.org Projects.

%prep
%setup -q -n parent-%{version}

%pom_remove_dep junit:junit-dep
%pom_remove_dep org.jboss.arquillian.extension:arquillian-drone-bom
%pom_remove_dep org.jboss.arquillian:arquillian-bom
%pom_remove_dep org.apache.openwebbeans:openwebbeans

%pom_remove_plugin org.codehaus.mojo:emma-maven-plugin
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:jboss-maven-plugin
%pom_remove_plugin org.codehaus.mojo:selenium-maven-plugin
%pom_remove_plugin org.codehaus.mojo:tomcat-maven-plugin

%pom_remove_plugin org.jboss.arquillian.maven:arquillian-maven-plugin
%pom_remove_plugin org.mortbay.jetty:maven-jetty-plugin
%pom_remove_plugin org.sonatype.maven.plugin:emma4it-maven-plugin
%pom_remove_plugin org.sonatype.plugins:nexus-maven-plugin

%pom_remove_plugin org.jboss.maven.plugins:maven-jdocbook-plugin
%pom_remove_plugin org.glassfish:maven-embedded-glassfish-plugin
%pom_remove_plugin org.jboss.maven.plugins:maven-javadoc-plugin

sed -i "s|<artifactId>failsafe-maven-plugin|<artifactId>maven-failsafe-plugin|" pom.xml

# https://bugzilla.redhat.com/show_bug.cgi?id=837589
# org.codehaus.cargo:cargo-maven2-plugin

# ch.qos.cal10n.plugins:maven-cal10n-plugin

# removed modules used only for testing (unavailable example and test dependencies)
%pom_xpath_remove pom:modules
rm -r test settings.xml

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 19-alt1_6jpp7
- new release

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 19-alt1_4jpp7
- new release

