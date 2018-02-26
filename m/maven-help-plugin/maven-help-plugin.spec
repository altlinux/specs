BuildRequires: xpp3-minimal
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-help-plugin
Version:        2.1.1
Release:        alt2_4jpp7
Summary:        Plugin to to get relative information about a project or the system

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-help-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         add-compat.patch
Patch1:         reduce-exception.patch

BuildArch: noarch

BuildRequires: plexus-utils
BuildRequires: ant
BuildRequires: maven
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: xstream
BuildRequires: jpackage-utils
Requires: ant
Requires: maven
Requires: jpackage-utils
Requires: xstream

Obsoletes: maven2-plugin-help < 0:%{version}-%{release}
Provides: maven2-plugin-help = 0:%{version}-%{release}
Source44: import.info

%description
The Maven Help Plugin is used to get relative information about a project
 or the system. It can be used to get a description of a particular plugin, 
including the plugin's mojos with their parameters and component requirements,
the effective POM and effective settings of the current build, 
and the profiles applied to the current project being built.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q 
%patch0
%patch1

%build
# no junit-addons, skip test
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2_4jpp7
- fixed build with xpp3

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_4jpp7
- complete build

* Tue Mar 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

