Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global vertag Final

Name:           os-maven-plugin
Version:        1.2.3
Release:        alt1_6jpp8
Summary:        Maven plugin for generating platform-dependent properties
License:        ASL 2.0
URL:            https://github.com/trustin/os-maven-plugin/
BuildArch:      noarch

Source0:        https://github.com/trustin/%{name}/archive/%{name}-%{version}.Final.tar.gz

Patch0:         0001-Port-to-current-plexus-utils.patch
Patch1:         0002-Don-t-fail-on-unknown-arch.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info

%description
os-maven-plugin is a Maven extension/plugin that generates various
useful platform-dependent project properties normalized from
${os.name} and ${os.arch}.

${os.name} and ${os.arch} are often subtly different between JVM and
operating system versions or they sometimes contain machine-unfriendly
characters such as whitespaces. This plugin tries to remove such
fragmentation so that you can determine the current operating system
and architecture reliably.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}.%{vertag}

%patch0 -p1
%patch1 -p1

# Remove Eclipse plugin (not needed in Fedora)
%pom_remove_dep org.eclipse:ui
%pom_remove_plugin :maven-jar-plugin
find -name EclipseStartup.java -delete
find -name plugin.xml -delete

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%dir %{_mavenpomdir}/%{name}
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_6jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_5jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_4jpp8
- new version

