BuildRequires: maven-enforcer-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jsf-2.1-api
%define version 2.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name: jboss-jsf-2.1-api
Version: 2.0.2
Release: alt3_3jpp7
Summary: JavaServer Faces 2.1 API
Group: Development/Java
License: CDDL or GPLv2 with exceptions
URL: http://www.jboss.org

# git clone git://github.com/jboss/jboss-jsf-api_spec.git jboss-jsf-2.1-api
# cd jboss-jsf-2.1-api/ && git archive --format=tar --prefix=jboss-jsf-2.1-api-2.0.2.Final/ jboss-jsf-api_2.1_spec-2.0.2.Final | xz > jboss-jsf-2.1-api-2.0.2.Final.tar.xz
Source0: %{name}-%{namedversion}.tar.xz

# Fix the FSF address in the license file:
Patch0: %{name}-fix-fsf-address.patch

BuildRequires: jboss-parent
BuildRequires: jpackage-utils
BuildRequires: geronimo-validation
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: objenesis
BuildRequires: jboss-el-2.2-api
BuildRequires: jboss-jsp-2.2-api
BuildRequires: jboss-jstl-1.2-api

Requires: jpackage-utils
Requires: jboss-jsp-2.2-api
Requires: jboss-jstl-1.2-api
Requires: jboss-el-2.2-api
Requires: geronimo-validation

BuildArch:noarch
Source44: import.info


%description
JavaServer(tm) Faces API classes based on Version 2.1 of Specification.


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc	
This package contains the API documentation for %{name}.


%prep

# Unpack the sources:
%setup -q -n %{name}-%{namedversion}


# Apply the patches:
%patch0 -p1


%build
mvn-rpmbuild install javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 target/jboss-jsf-api_2.1_spec-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Dependencies map:
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "javax.faces:jsf-api"

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE
%doc README


%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE
%doc README


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt3_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_3jpp7
- new version

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_3jpp7
- new version

