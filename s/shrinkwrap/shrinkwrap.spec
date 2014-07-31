# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name shrinkwrap
%define version 1.0.0
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
Name:          shrinkwrap
Version:       1.0.0
Release:       alt2_5jpp7
Summary:       A simple mechanism to assemble Java archives
Group:         Development/Java
License:       ASL 2.0
Url:           http://www.jboss.org/shrinkwrap/
# git clone git://github.com/shrinkwrap/shrinkwrap.git shrinkwrap-1.0.0
# cd shrinkwrap-1.0.0 && git archive --format=tar --prefix=shrinkwrap-1.0.0/ 1.0.0 | xz > ../shrinkwrap-1.0.0.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz
# shrinkwrap package don't include the license file
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: jboss-parent
BuildRequires: jpackage-utils

BuildRequires: apiviz
BuildRequires: junit

BuildRequires: maven-local
BuildRequires: maven-checkstyle-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

# required by enforcer-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components)

Requires:      junit

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Shrinkwrap provides a simple mechanism to assemble archives
like JARs, WARs, and EARs with a friendly, fluent API.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

#sed -i "s|<module>dist</module>|<!--module>dist</module-->|" pom.xml
%pom_disable_module dist
cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%build

export JAVA5_HOME=%{_jvmdir}/java
export JAVA_HOME=$JAVA5_HOME
mvn-rpmbuild install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}/%{name}
install -pm 644 api/target/%{name}-api-%{namedversion}-tests.jar %{buildroot}%{_javadir}/%{name}/api-tests.jar
install -pm 644 api/target/%{name}-api-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/api.jar
install -pm 644 build-resources/target/%{name}-build-resources-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/build-resources.jar
install -pm 644 impl-base/target/%{name}-impl-base-%{namedversion}-tests.jar %{buildroot}%{_javadir}/%{name}/impl-base-tests.jar
install -pm 644 impl-base/target/%{name}-impl-base-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/impl-base.jar
install -pm 644 spi/target/%{name}-spi-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/spi.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-parent.pom
install -pm 644 bom/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-bom.pom
%add_maven_depmap JPP.%{name}-bom.pom
install -pm 644 depchain/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-depchain.pom
%add_maven_depmap JPP.%{name}-depchain.pom
install -pm 644 api/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-api.pom
%add_maven_depmap JPP.%{name}-api.pom %{name}/api.jar
install -pm 644 build-resources/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-build-resources.pom
%add_maven_depmap JPP.%{name}-build-resources.pom %{name}/build-resources.jar
install -pm 644 impl-base/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-impl-base.pom
%add_maven_depmap JPP.%{name}-impl-base.pom %{name}/impl-base.jar
install -pm 644 spi/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-spi.pom
%add_maven_depmap JPP.%{name}-spi.pom %{name}/spi.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -r target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}/*.jar
%{_mavenpomdir}/JPP.%{name}-*.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE-2.0.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE-2.0.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp7
- new version

