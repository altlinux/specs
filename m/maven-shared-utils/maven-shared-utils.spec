Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-shared-utils
Version:        0.4
Release:        alt1_2jpp7
Summary:        Maven shared utility classes
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-shared-utils
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
# Patching tests so that they are compatible with JUnit 4.11
# (upstream bug http://jira.codehaus.org/browse/MSHARED-285)
Patch0:         %{name}-tests.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  apache-commons-lang3
BuildRequires:  apache-rat
BuildRequires:  maven-shared
BuildRequires:  maven-shade-plugin
Source44: import.info

%description
This project aims to be a functional replacement for plexus-utils in Maven.

It is not a 100% API compatible replacement though but a replacement with
improvements: lots of methods got cleaned up, generics got added and we dropped
a lot of unused code.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch
    
%description javadoc
API documentation for %{name}.

%prep
%setup -q
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%patch0 -p1

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_2jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt0.2jpp
- rebuild to add provides

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

