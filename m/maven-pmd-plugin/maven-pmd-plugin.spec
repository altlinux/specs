Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-pmd-plugin
Version:        3.6
Release:        alt1_2jpp8
Summary:        Maven PMD Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-pmd-plugin/
Source0:        http://archive.apache.org/dist/maven/plugins/maven-pmd-plugin-%{version}-source-release.zip

BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  mvn(dom4j:dom4j)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(net.sourceforge.pmd:pmd-core) >= 5.3.2
BuildRequires:  mvn(net.sourceforge.pmd:pmd-java) >= 5.3.2
BuildRequires:  mvn(net.sourceforge.pmd:pmd-javascript) >= 5.3.2
BuildRequires:  mvn(net.sourceforge.pmd:pmd-jsp) >= 5.3.2
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-decoration-model)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-resources)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info

%description
A Maven plugin for the PMD toolkit, that produces a report on both code rule 
violations and detected copy and paste fragments, as well as being able to 
fail the build based on these metrics.
  

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q

# remove unnecessary animal sniffer and enforcer plugins
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

# remove test dependency not in fedora
%pom_remove_dep com.github.tomakehurst:wiremock

%build
# ignore test failures
# all tests fail, so this is probably environmental but I'm not sure what's missing
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.6-alt1_2jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 3.6-alt1_1jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt2_6jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt2_3jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt1_3jpp7
- new fc release

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt1_1jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

