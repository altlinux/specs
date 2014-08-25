Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-plugin-testing
Version:        2.1
Release:        alt1_7jpp7
Summary:        Maven Plugin Testing
License:        ASL 2.0
URL:            http://maven.apache.org/plugin-testing/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugin-testing/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch: noarch

BuildRequires: easymock2
BuildRequires: junit
BuildRequires: maven-local
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: plexus-containers-component-metadata
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-shared-reporting-impl
Source44: import.info
#BuildRequires: maven-test-tools

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
BuildRequires: maven-surefire-provider-junit4
Obsoletes: maven-shared-plugin-testing-harness <= 0:1.2
Provides: maven-shared-plugin-testing-harness = 1:%{version}-%{release}

%description harness
The Maven Plugin Testing Harness provides mechanisms to manage tests on Mojo.

%package tools
Group: Development/Java
Summary: Maven Plugin Testing Tools
Obsoletes: maven-shared-plugin-testing-tools <= 0:%{version}-%{release}
Provides: maven-shared-plugin-testing-tools = 1:%{version}-%{release}

%description tools
A set of useful tools to help the Maven Plugin testing.

%package -n maven-test-tools
Group: Development/Java
Summary: Maven Testing Tool
Obsoletes: maven-shared-test-tools <= 0:%{version}-%{release}
Provides: maven-shared-test-tools = 1:%{version}-%{release}

%description -n maven-test-tools
Framework to test Maven Plugins with Easymock objects.

%prep
%setup -q

%build
%mvn_alias : org.apache.maven.shared:
# Tests are skipped due to some test failures most probably caused by issues 
# with our plexus container
%mvn_build -f -s

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

