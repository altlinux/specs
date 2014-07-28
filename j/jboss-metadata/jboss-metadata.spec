Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-metadata
%define version 7.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name: jboss-metadata
Version: 7.0.1
Release: alt2_5jpp7
Summary: JBoss Metadata
Group: Development/Java
License: LGPLv2+
URL: https://github.com/jboss/metadata

# git clone git://github.com/jboss/metadata.git
# cd metadata/ && git archive --format=tar --prefix=jboss-metadata-7.0.1.Final/ 7.0.1.Final | xz > jboss-metadata-7.0.1.Final.tar.xz
Source0: %{name}-%{namedversion}.tar.xz

# Remove the dependency on jaxb-api:
Patch0: %{name}-pom.patch

# Fix the FSF address in the copy of the license file that we are going to
# include in the packages:
Patch1: %{name}-fix-fsf-address.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: jboss-parent
BuildRequires: jboss-logging
BuildRequires: hibernate-jpa-2.0-api
BuildRequires: jboss-ejb-3.1-api
BuildRequires: jboss-ejb3-ext-api
BuildRequires: jboss-interceptors-1.1-api
BuildRequires: jboss-annotations-1.1-api
BuildRequires: dos2unix

Requires: jboss-annotations-1.1-api
Requires: jboss-interceptors-1.1-api
Requires: jpackage-utils
Requires: jboss-logging
Requires: hibernate-jpa-2.0-api
Requires: jboss-ejb-3.1-api
Requires: jboss-ejb3-ext-api >= 2.0.0-0.1.beta2
Source44: import.info


%description
This package contains JBoss Metadata for JBoss AS 7.


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.


%prep

# Unpack and patch the sources:
%setup -q -n %{name}-%{namedversion}
%patch0 -p1
%patch1 -p1

# Fix the line ending in the license file:
dos2unix common/LICENSE.txt


%build
# We don't have packaged all test dependencies (jboss-test for example):
mvn-rpmbuild \
  -Dmaven.test.skip=true \
  install \
  javadoc:aggregate


%install

# Create the directories:
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_mavendepmapfragdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}

# Jar and POM files:
for module in common ejb web ear appclient; do
  install -pm 644 ${module}/target/%{name}-${module}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${module}.jar
  install -pm 644 ${module}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-${module}.pom
  %add_maven_depmap JPP.%{name}-%{name}-${module}.pom %{name}/%{name}-${module}.jar
done

# Parent POM file:
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom
%add_maven_depmap JPP.%{name}-%{name}-parent.pom

# Javadoc files:
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files
%{_javadir}/%{name}
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc common/LICENSE.txt


%files javadoc
%{_javadocdir}/%{name}
%doc common/LICENSE.txt


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:7.0.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:7.0.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:7.0.1-alt1_3jpp7
- new version

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt2_0jpp6
- fixed build with java 7

* Wed Feb 09 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_0jpp6
- new version

