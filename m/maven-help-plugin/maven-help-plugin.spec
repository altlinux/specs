# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-help-plugin
Version:        2.2
Release:        alt1_8jpp8
Summary:        Plugin to to get relative information about a project or the system

Group:          Development/Other
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-help-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         maven3-api-fixes.patch
Patch1:         reduce-exception.patch
BuildArch: noarch

BuildRequires: plexus-utils
BuildRequires: ant
BuildRequires: junit-addons
BuildRequires: maven-local
BuildRequires: maven-install-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: xstream
BuildRequires: javapackages-tools rpm-build-java
BuildRequires: plexus-containers-component-metadata
BuildRequires: maven-plugin-tools-generators
Requires: ant
Requires: maven
Requires: javapackages-tools rpm-build-java
Requires: xstream
Requires: maven-plugin-tools-generators
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
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch0 -b .maven3-api-fixes
%patch1 -b .reduce-exception

# Use compatibility API
%pom_remove_dep org.apache.maven:maven-plugin-parameter-documenter
%pom_add_dep org.apache.maven:maven-compat

# Add missing test deps
%pom_add_dep net.sf.cglib:cglib:any:test

# In newer versions of maven-plugin-tools the PluginUtils.toText()
# static method was moved to GeneratorUtils class.
%pom_add_dep org.apache.maven.plugin-tools:maven-plugin-tools-generators
sed -i "s|PluginUtils.toText|org.apache.maven.tools.plugin.generator.GeneratorUtils.toText|" \
    src/main/java/org/apache/maven/plugins/help/DescribeMojo.java

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_8jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_7jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt5_11jpp7
- new release

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt5_8jpp7
- added maven-local BR:

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt4_8jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt4_7jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt3_7jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2_7jpp7
-  new release

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2_4jpp7
- fixed build with xpp3

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_4jpp7
- complete build

* Tue Mar 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

