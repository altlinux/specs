BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             weld-parent
Version:          17
Release:          alt2_4jpp7
Summary:          Parent POM for Weld
Group:            Development/Java
License:          ASL 2.0
URL:              http://seamframework.org/Weld

Source0:          http://repo1.maven.org/maven2/org/jboss/weld/%{name}/%{version}/%{name}-%{version}.pom

# Removed accessing remote repos
Patch0:           weld-parent-%{version}-pom.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-enforcer-plugin

Requires:         jpackage-utils
Requires:         maven
Source44: import.info

%description
Parent POM for Weld

%prep
cp %{SOURCE0} pom.xml

%patch0 -p0

%build
mvn-rpmbuild install

%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 17-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 17-alt1_4jpp7
- new version

