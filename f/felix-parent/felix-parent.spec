Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           felix-parent
Version:        2.1
Release:        alt1_9jpp8
Summary:        Parent POM file for Apache Felix Specs
License:        ASL 2.0
URL:            http://felix.apache.org/
Source0:        http://repo1.maven.org/maven2/org/apache/felix/felix-parent/%{version}/%{name}-%{version}-source-release.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mockito
BuildRequires:  maven-site-plugin
BuildRequires:  maven-release-plugin
Source44: import.info

%description
Parent POM file for Apache Felix Specs.

%prep
%setup -q -n felix-parent-%{version}
%mvn_alias : :felix
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin org.codehaus.mojo:ianal-maven-plugin
%pom_remove_plugin :apache-rat-plugin

# wagon ssh dependency unneeded
%pom_xpath_remove pom:extensions

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_9jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_8jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt5_11jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt5_8jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt4_8jpp7
- new release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt4_5jpp6
- use maven-plugin-build-helper

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt3_5jpp6
- fixed build with maven3

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt2_5jpp6
- new jpp release

* Wed Jun 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt2_3jpp6
- dropped mojo-maven2-* dependency

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_3jpp6
- fixed repolib

