# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             jbosgi-parent
Version:          1.0.22
Release:          alt2_5jpp7
Summary:          JBossOSGi Parent
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/
Source0:          https://raw.github.com/jbosgi/jbosgi-parent/%{version}/pom.xml

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin

Requires:         jpackage-utils
Requires:         maven
Source44: import.info

%description
This package contains the JBossOSGi Parent

%prep
cp %{SOURCE0} .

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom -a "org.jboss.osgi:jboss-osgi-parent"

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.22-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.22-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.22-alt1_3jpp7
- new version

