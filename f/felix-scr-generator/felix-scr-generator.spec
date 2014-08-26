Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
%global project   felix
%global bundle    org.apache.felix.scr.generator
Name:          felix-scr-generator
Version:       1.8.2
Release:       alt1_1jpp7
Summary:       Descriptor Generator Implementation
License:       ASL 2.0
URL:           http://felix.apache.org/
Source0:       http://www.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildRequires: mvn(org.apache.felix:felix-parent)

BuildRequires: mvn(org.osgi:org.osgi.compendium)
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(org.ow2.asm:asm-all)

# Test deps
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.easymock:easymock)
BuildRequires: mvn(org.mockito:mockito-all)
%if 0
# Circular deps
BuildRequires: mvn(org.apache.felix:org.apache.felix.scr.annotations)
%endif

BuildRequires: maven-local
BuildRequires: maven-remote-resources-plugin
BuildRequires: maven-site-plugin

BuildArch:     noarch
Source44: import.info

%description
Provides the implementation to generate Declarative Services and Metatype
Service descriptors from Java 5 Annotations and/or JavaDoc tags.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%build

%mvn_file :%{bundle} %{project}/%{bundle}
# tests skipped for circular dependency with org.apache.felix:org.apache.felix.scr.annotations
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE changelog.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1_1jpp7
- new release

