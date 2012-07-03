Patch33: maven-assembly-plugin-2.2.2-alt-allow-empty-assembly-id.patch
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-assembly-plugin
Version:        2.2.2
Release:        alt2_4jpp7
Summary:        Maven Assembly Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-assembly-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch: noarch

Obsoletes: maven2-plugin-assembly <= 0:2.0.8
Provides:  maven2-plugin-assembly = 1:%{version}-%{release}

BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires:  ant
BuildRequires:  maven
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-doxia
BuildRequires:  maven-doxia-sitetools

BuildRequires: plexus-container-default
BuildRequires: plexus-utils
BuildRequires: plexus-active-collections
BuildRequires: plexus-containers-component-metadata
BuildRequires: plexus-io
BuildRequires: plexus-interpolation
BuildRequires: plexus-archiver

BuildRequires: maven-shared-file-management
BuildRequires: maven-shared-repository-builder
BuildRequires: maven-shared-filtering
BuildRequires: maven-shared-file-management
BuildRequires: maven-shared-io

BuildRequires: easymock
BuildRequires: jdom
BuildRequires: jaxen
BuildRequires: saxpath
BuildRequires: junit
BuildRequires: modello

Requires: easymock
Requires: jdom
Requires: jaxen
Requires: saxpath
Requires: plexus-container-default
Requires: plexus-utils
Requires: plexus-active-collections
Requires: plexus-containers-component-metadata
Requires: plexus-io
Requires: plexus-interpolation
Requires: plexus-archiver
Requires: maven-shared-repository-builder
Requires: maven-shared-filtering
Requires: maven-shared-file-management
Requires: maven-shared-io
Requires: jpackage-utils >= 0:1.7.2
Source44: import.info

%description
A Maven 2 plugin to create archives of your project's sources, classes, 
dependencies etc. from flexible assembly descriptors.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils >= 0:1.7.2
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch33 -p1

%build
# seems koji don't have easymockclassextension
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/
rm -rf target/site/api*

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt2_4jpp7
- maven2 compatibility: added
  maven-assembly-plugin-2.2.2-alt-allow-empty-assembly-id.patch

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt1_4jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

