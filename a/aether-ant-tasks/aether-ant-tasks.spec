# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global vertag v20141111

Name:           aether-ant-tasks
Epoch:          1
Version:        1.0.1
Release:        alt1_4jpp8
Summary:        Ant tasks using Aether to resolve, install and deploy artifacts
Group:          Development/Other
BuildArch:      noarch

License:        EPL
URL:            http://www.eclipse.org/aether
Source0:        http://git.eclipse.org/c/aether/aether-ant.git/snapshot/%{name}-%{version}.%{vertag}.tar.bz2
Source5:        ant-classpath

Patch0001:      0001-Add-support-for-XMvn-workspace-reader.patch
# Forwarded upstream: http://bugs.eclipse.org/470696
Patch0002:      0002-Update-to-Maven-3.2.3.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-launcher)
BuildRequires:  mvn(org.apache.ant:ant-testutil)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider) >= 3.1.0
BuildRequires:  mvn(org.apache.maven:maven-settings-builder)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-connector-basic)
BuildRequires:  mvn(org.eclipse.aether:aether-impl)
BuildRequires:  mvn(org.eclipse.aether:aether-test-util)
BuildRequires:  mvn(org.eclipse.aether:aether-transport-classpath)
BuildRequires:  mvn(org.eclipse.aether:aether-transport-file)
BuildRequires:  mvn(org.eclipse.aether:aether-transport-http)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)

Requires:       ant
Source44: import.info

%description
The Aether Ant Tasks enable build scripts for Apache Ant 1.7+ to use Eclipse
Aether to resolve dependencies and install and deploy locally built artifacts.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}.%{vertag}
%patch0001 -p1
%patch0002 -p1

# Use junit since junit-dep is obselete and equivilent to junit since 4.11
sed -i -e 's@junit-dep@junit@g' pom.xml

%pom_remove_plugin ":maven-shade-plugin"
%pom_remove_plugin ":maven-enforcer-plugin"

%build
# Some tests require internet connectivity, so ignore failures
%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

install -d -m 755 %{buildroot}/%{_sysconfdir}/ant.d
install -p -m 644 %{SOURCE5} %{buildroot}/%{_sysconfdir}/ant.d/%{name}

%files -f .mfiles
%config(noreplace) %{_sysconfdir}/ant.d/%{name}
%doc README.md
%doc epl-v10.html notice.html

%files javadoc -f .mfiles-javadoc
%doc epl-v10.html notice.html

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1_4jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1_3jpp8
- new version

