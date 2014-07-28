# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             opensaml-java-parent
Version:          4
Release:          alt1_3jpp7
Summary:          OpenSAML Java Parent
Group:            Development/Java
License:          ASL 2.0
URL:              http://www.jboss.org/jbossws
Source0:          https://build.shibboleth.net/nexus/content/groups/public/net/shibboleth/parent/%{version}/parent-%{version}.pom
Source1:          LICENSE-2.0.txt

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-clean-plugin
BuildRequires:    maven-dependency-plugin

Requires:         jpackage-utils
Source44: import.info

%description
This package contains the OpenSAML Java Parent

%prep
cp %{SOURCE1} .

%build
mvn-rpmbuild -f %{SOURCE0} install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

# POM
install -pm 644 %{SOURCE0} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE-2.0.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4-alt1_3jpp7
- new release

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 4-alt1_1jpp7
- fc update

