# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name hibernate-validator
%define version 4.2.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name: hibernate-validator
Version: 4.2.0
Release: alt2_8jpp7
Summary: Bean Validation (JSR 303) Reference Implementation

Group: Development/Java
License: ASL 2.0 

URL: http://www.hibernate.org/subprojects/validator.html

# git clone git://github.com/hibernate/hibernate-validator
# cd hibernate-validator/ && git archive --format=tar --prefix=hibernate-validator-4.2.0.Final/ 4.2.0.Final | xz > hibernate-validator-4.2.0.Final.tar.xz
Source0: hibernate-validator-4.2.0.Final.tar.xz

# Remove the jdocbook plugin as it is not available in the distribution:
Patch0: %{name}-remove-jdocbook-plugin.patch

# Use maven-jaxb2-plugin (already packaged) to avoid adding packaging
# jaxb2-maven-plugin:
Patch1: %{name}-use-maven-jaxb2-plugin.patch         

# Don't generate test reports:
Patch2: %{name}-dont-generate-test-reports.patch

# Remove the shade plugin:
Patch3: %{name}-remove-shade-plugin.patch

# Remove the wagon webdav extension:
Patch4: %{name}-remove-wagon-webdav-extension.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: jsoup
BuildRequires: jtype
BuildRequires: joda-time
BuildRequires: geronimo-validation
BuildRequires: maven-injection-plugin
BuildRequires: hibernate-jpa-2.0-api
BuildRequires: maven-jaxb2-plugin
BuildRequires: dos2unix

Requires: hibernate-jpa-2.0-api
Requires: jpackage-utils
Requires: geronimo-validation
Requires: jsoup
Requires: jtype
Requires: joda-time
Requires: slf4j
Source44: import.info


%description
Bean Validation (JSR 303) Reference Implementation


%package javadoc
Summary: API docs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
Reference implementation of JSR 303 - Bean Validation. Bean Validation defines
a metadata model and API for JavaBean validation. The default metadata source
is annotations, with the ability to override and extend the meta-data through
the use of XML validation descriptors.


%prep
%setup -q -n hibernate-validator-%{namedversion}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1


%build

# Rrunning tests requires hibernate proper, so skip for now:
mvn-rpmbuild \
  -Dmaven.test.skip=true \
  -pl hibernate-validator \
  install \
  javadoc:javadoc

# Fix the line endings:
dos2unix readme.txt


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 hibernate-validator/target/%{name}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml  %{buildroot}%{_mavenpomdir}/JPP-%{name}-parent.pom
install -pm 644 %{name}/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp %{name}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# Dependencies map:
%add_maven_depmap JPP-%{name}-parent.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%{_mavenpomdir}/JPP-%{name}-parent.pom
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar
%doc license.txt
%doc readme.txt
%doc changelog.txt


%files javadoc
%{_javadocdir}/%{name}
%doc license.txt


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt2_8jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1_5jpp7
- new version

