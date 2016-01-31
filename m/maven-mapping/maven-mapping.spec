Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-mapping
Version:        1.0
Release:        alt1_2jpp8
Summary:        Apache Maven Mapping
License:        ASL 2.0
URL:            http://maven.apache.org/shared/%{name}/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildRequires:  maven-local
BuildRequires:  maven-shared
Source44: import.info

%description
Maven shared component that implements file name mapping.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_2jpp8
- new version

