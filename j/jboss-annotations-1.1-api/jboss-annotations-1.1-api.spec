BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-annotations-1.1-api
%define version 1.0.1
%global namedreltag .20120212git76e1a2
%global namedversion %{version}%{?namedreltag}

Name: jboss-annotations-1.1-api
Version: 1.0.1
Release: alt2_0.3.20120212git76e1a2jpp7
Summary: Common Annotations 1.1 API
Group: Development/Java
License: CDDL or GPLv2 with exceptions
URL: http://www.jboss.org

# git clone git://github.com/jboss/jboss-annotations-api_spec.git jboss-annotations-1.1-api
# cd jboss-annotations-1.1-api
# git archive --format=tar --prefix=jboss-annotations-1.1-api-1.0.1/ 76e1a2c85e025342710a29cd9dfff109d730a483 | xz > jboss-annotations-1.1-api-1.0.1.20120212git76e1a2.tar.xz
Source0: %{name}-%{namedversion}.tar.xz

BuildRequires: jboss-specs-parent
BuildRequires: jpackage-utils
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin

Requires: jpackage-utils
BuildArch: noarch
Source44: import.info


%description
This package contains Common Annotations 1.1 API.


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc	
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}


%build
mvn-rpmbuild install javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 target/jboss-annotations-api_1.1_spec-%{version}-SNAPSHOT.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/.

# Dependencies map:
%add_maven_depmap JPP-%{name}.pom %{name}.jar

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
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_0.3.20120212git76e1a2jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_0.3.20120212git76e1a2jpp7
- new version

