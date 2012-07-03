BuildRequires: /proc
BuildRequires: jpackage-compat

Name:          annox
Version:       0.5.0
Release:       alt1_2jpp7
Summary:       Java annotations in XML resources
Group:         Development/Java
License:       BSD
Url:           http://java.net/projects/annox
# svn export https://svn.java.net/svn/annox~svn/tags/0.5.0 annox-0.5.0
# tar czf annox-0.5.0-src-svn.tar.gz annox-0.5.0
Source0:       annox-0.5.0-src-svn.tar.gz
# from http://confluence.highsource.org/display/ANX/License
# annox package don't include the license file
# but annox developers allowed us to redistribute their
# work only if we include this notice. So we HAVE TO include these notices.
Source1:       annox-LICENSE
# remove
#    org.hibernate hibernate-search 3.0.0.GA
# change
#    groupId ant in org.apache.ant
#    artifactId ant-optional in ant
#    version 1.5.3-1 in 1.8.2
Patch0:        annox-0.5.0-fixbuild.patch

BuildRequires: jpackage-utils
BuildRequires: sonatype-oss-parent

BuildRequires: ant
BuildRequires: apache-commons-lang
BuildRequires: glassfish-jaxb
BuildRequires: junit

BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin

Requires:      apache-commons-lang
Requires:      glassfish-jaxb

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Annox is an open source project which allows you to
read arbitrary Java annotations from XML resources.
JAXB users may be interested in Annox annotation
reader for JAXB RI which allows you to define JAXB 
Java/XML mappings in XML resources (instead of
annotations).

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n annox-%{version}
find \( -name '*.jar' -o -name '*.class' -o -name '*.bat' \) -exec rm -f '{}' \;
%patch0 -p1
cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE
sed -i "s|<module>samples</module>|<!--module>samples</module-->|" pom.xml

%build
# unavailable deps for run test: org.hibernate hibernate-search 3.0.0.GA
mvn-rpmbuild -e \
  -Dmaven.test.skip=true \
  install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -pm 644 core/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-project.pom
%add_maven_depmap JPP-%{name}-project.pom
install -pm 644 core/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}*.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_2jpp7
- fc build

