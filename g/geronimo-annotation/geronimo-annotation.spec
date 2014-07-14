BuildRequires: /proc
BuildRequires: jpackage-compat
%global spec_ver 1.1
%global spec_name geronimo-annotation_%{spec_ver}_spec

Name:             geronimo-annotation
Version:          1.0
Release:          alt2_9jpp7
Summary:          Java EE: Annotation API v1.1
Group:            Development/Java
License:          ASL 2.0
URL:              http://geronimo.apache.org/

Source0:          http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{spec_name}/%{version}/%{spec_name}-%{version}-source-release.tar.gz
Patch1:           use_parent_pom.patch
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    geronimo-parent-poms
BuildRequires:    maven-resources-plugin

Requires:         jpackage-utils

Provides:         annotation_api = %{spec_ver}
Source44: import.info

%description
This package defines the common annotations.

%package javadoc
Group:            Development/Java
Summary:          Javadoc for %{name}
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{spec_name}-%{version}
sed -i 's/\r//' LICENSE NOTICE
%patch1 -p0

%build
mvn-rpmbuild  install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{spec_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/annotation.jar

# poms
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.apache.geronimo.specs:geronimo-annotation_1.0_spec,javax.annotation:jsr250-api"


# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%doc LICENSE NOTICE
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_9jpp7
- new version

