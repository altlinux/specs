Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          properties-maven-plugin
Version:       1.0.0
Release:       alt1_2jpp8
Summary:       Properties Maven Plugin
License:       ASL 2.0
URL:           http://www.mojohaus.org/properties-maven-plugin/
Source0:       https://github.com/mojohaus/properties-maven-plugin/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch:     noarch
Source44: import.info

%description
The Properties Maven Plugin is here to make life a little easier when dealing
with properties. It provides goals to read and write properties from files.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# use maven 3.x apis
%pom_xpath_set pom:properties/pom:maven.api.version 3.0.3
%pom_change_dep :maven-project :maven-core:'${maven.api.version}'

%pom_remove_plugin :plexus-maven-plugin
%pom_add_plugin org.codehaus.plexus:plexus-component-metadata:1.5.5 . '
<executions>
 <execution>
  <goals>
   <goal>generate-metadata</goal>
  </goals>
 </execution>
</executions>'

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.11.alpha2jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.10.alpha2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.6.alpha2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.4.alpha2jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.2.alpha2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.2.alpha2jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.2.alpha2jpp7
- new version

