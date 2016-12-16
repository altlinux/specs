Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           exec-maven-plugin
Version:        1.5.0
Release:        alt1_1jpp8
Summary:        Exec Maven Plugin

License:        ASL 2.0
URL:            http://mojo.codehaus.org/exec-maven-plugin
Source0:        http://repo1.maven.org/maven2/org/codehaus/mojo/exec-maven-plugin/%{version}/exec-maven-plugin-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.maven:maven-artifact:2.2.1)
BuildRequires:  mvn(org.apache.maven:maven-artifact-manager)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model:2.2.1)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven:maven-toolchain)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

Obsoletes:      maven-plugin-exec < %{version}-%{release}
Provides:       maven-plugin-exec = %{version}-%{release}
Source44: import.info

%description
A plugin to allow execution of system and Java programs.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n exec-maven-plugin-%{version}

sed -i 's/\r$//' LICENSE.txt
find . -name *.jar -delete

%pom_remove_plugin :animal-sniffer-maven-plugin

%build
# tests are disabled, see: rhbz#1095077
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_3jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_2jpp8
- new version

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt4_10jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt4_3jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_3jpp7
- new version

