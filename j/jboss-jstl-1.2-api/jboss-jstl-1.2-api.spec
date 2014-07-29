# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jstl-1.2-api
%define version 1.0.3
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name: jboss-jstl-1.2-api
Version: 1.0.3
Release: alt2_6jpp7
Summary: JSP Standard Template Library 1.2 API
Group: Development/Java
License: CDDL or GPLv2 with exceptions
URL: http://www.jboss.org

# git clone git://github.com/jboss/jboss-jstl-api_spec.git jboss-jstl-1.2-api
# cd jboss-jstl-1.2-api/ && git archive --format=tar --prefix=jboss-jstl-1.2-api-1.0.3.Final/ jboss-jstl-api_1.2_spec-1.0.3.Final | xz > jboss-jstl-1.2-api-1.0.3.Final.tar.xz
Source0: %{name}-%{namedversion}.tar.xz

# Fix the FSF address in the license file:
Patch0: %{name}-fix-fsf-address.patch

BuildRequires: jboss-parent
BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: jboss-el-2.2-api
BuildRequires: jboss-servlet-3.0-api
BuildRequires: jboss-jsp-2.2-api
BuildRequires: xalan-j2

Requires: jpackage-utils
Requires: jboss-el-2.2-api
Requires: jboss-servlet-3.0-api
Requires: jboss-jsp-2.2-api
Requires: xalan-j2

BuildArch: noarch
Source44: import.info


%description
Java Server Pages Standard Template Library 1.2 API.


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
install -pm 644 target/jboss-jstl-api_1.2_spec-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Dependencies map:
%add_maven_depmap JPP-%{name}.pom %{name}.jar

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
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_4jpp7
- new version

