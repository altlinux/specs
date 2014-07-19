# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             maven-filtering
Version:          1.0
Release:          alt2_9jpp7
Summary:          Shared component providing resource filtering
Group:            Development/Java
License:          ASL 2.0
URL:              http://maven.apache.org/shared/%{name}/index.html

Source0:          http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
# POM requires plexus-maven-plugin, which was replaced by 
# plexus-containers-component-metadata
Patch0:           %{name}-plexus.patch
  
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    plexus-build-api
BuildRequires:    plexus-containers-component-metadata
BuildRequires:    sisu

Requires:         jpackage-utils
Requires:         maven

Provides:         maven-shared-filtering = 1.0-99
Obsoletes:        maven-shared-filtering < 1.0-99 
Source44: import.info

%description
These Plexus components have been built from the filtering process/code in 
Maven Resources Plugin. The goal is to provide a shared component for all 
plugins that needs to filter resources.

%package javadoc
Group:            Development/Java
Summary:          Javadoc for %{name}
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1


%build
# Tests use a package that is no longer present in plexus-build-api (v0.0.7)
mvn-rpmbuild install javadoc:aggregate -Dmaven.test.skip

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}


%files
%doc DEPENDENCIES LICENSE NOTICE
%{_javadir}/*
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9jpp7
- new release

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_8jpp7
- full build

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

