# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-ear-plugin
Version:        2.7
Release:        alt1_1jpp7
Summary:        Maven EAR Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-ear-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

# plexus-container-default needs to be before plexus-plugin-api in the
# classpath as there is a duplication and incompatibility of classes
Patch0:         %{name}-plexus-dep.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven
BuildRequires: maven-plugin-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-archiver
BuildRequires: plexus-archiver
BuildRequires: plexus-container-default > 0:1.0-0.5.a9
BuildRequires: plexus-utils
BuildRequires: maven-shared-filtering
BuildRequires: maven-shared-verifier
BuildRequires: xmlunit
BuildRequires: junit

Requires:       maven
Requires:       jpackage-utils
Requires:       plexus-archiver
Requires:       plexus-container-default
Requires:       plexus-utils

Obsoletes: maven2-plugin-ear <= 0:2.0.8
Provides: maven2-plugin-ear = 0:%{version}-%{release}
Source44: import.info

%description
Generates a J2EE Enterprise Archive (EAR) file.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q 
%patch0 -p1

%build
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        install javadoc:aggregate

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_1jpp7
- complete build

