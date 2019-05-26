Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-plugin-testing
Version:        3.3.0
Release:        alt1_14jpp8
Summary:        Maven Plugin Testing
License:        ASL 2.0
URL:            http://maven.apache.org/plugin-testing/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugin-testing/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch0:         0001-Port-to-plexus-utils-3.0.21.patch
Patch1:         0002-Port-to-current-maven-artifact.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-invoker)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-file)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.easymock:easymock)
Source44: import.info

%description
The Maven Plugin Testing contains the necessary modules
to be able to test Maven Plugins.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package harness
Group: Development/Java
Summary: Maven Plugin Testing Mechanism
Obsoletes: maven-shared-plugin-testing-harness <= 0:1.2

%description harness
The Maven Plugin Testing Harness provides mechanisms to manage tests on Mojo.

%package tools
Group: Development/Java
Summary: Maven Plugin Testing Tools
Obsoletes: maven-shared-plugin-testing-tools <= 0:%{version}-%{release}

%description tools
A set of useful tools to help the Maven Plugin testing.

%package -n maven-test-tools
Group: Development/Java
Summary: Maven Testing Tool
Obsoletes: maven-shared-test-tools <= 0:%{version}-%{release}

%description -n maven-test-tools
Framework to test Maven Plugins with Easymock objects.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin

sed -i -e "s/MockControl/IMocksControl/g" maven-test-tools/src/main/java/org/apache/maven/shared/tools/easymock/MockManager.java

# needs network for some reason
rm maven-plugin-testing-tools/src/test/java/org/apache/maven/shared/test/plugin/ProjectToolTest.java

%mvn_alias : org.apache.maven.shared:

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}
%doc LICENSE NOTICE
%files harness -f .mfiles-%{name}-harness
%files tools -f .mfiles-%{name}-tools
%files -n maven-test-tools -f .mfiles-maven-test-tools
%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_14jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_12jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_10jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_9jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_7jpp8
- new fc release

* Fri Dec 09 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_6jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_3jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_7jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_4.alpha1jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_4.alpha1jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_4.alpha1jpp7
- new fc release

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_3.alpha1jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

