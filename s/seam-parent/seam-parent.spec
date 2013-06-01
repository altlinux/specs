# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          seam-parent
Version:       19
Release:       alt1_4jpp7
Summary:       The parent for Seam modules
Group:         Development/Java
License:       ASL 2.0
URL:           http://www.seamframework.org/
# git clone git://github.com/seam/parent.git seam-parent-19
# (cd seam-parent-19/ && git archive --format=tar --prefix=seam-parent-19/ 19 | xz > ../seam-parent-19.tar.xz)
Source0:       %{name}-%{version}.tar.xz
# seam-parent package don't include the license file
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: jpackage-utils

BuildRequires: maven-local

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Parent for seamframework.org Projects.

%prep
%setup -q

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
# Nothing to do
%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom

%check
mvn-rpmbuild verify

%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE-2.0.txt

%changelog
* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 19-alt1_4jpp7
- new release

