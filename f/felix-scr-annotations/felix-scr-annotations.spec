Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global project   felix
%global bundle    org.apache.felix.scr.annotations
Name:          felix-scr-annotations
Version:       1.9.12
Release:       alt1_3jpp8
Summary:       Annotations for SCR
License:       ASL 2.0
URL:           http://felix.apache.org/
Source0:       http://www.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:felix-parent:pom:)
BuildRequires: mvn(org.apache.felix:org.apache.felix.scr.generator)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
# i dont know which package as missing this required...
BuildRequires: mvn(org.mockito:mockito-all)

BuildArch:     noarch
Source44: import.info

%description
Annotations for generating OSGi service descriptors.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%mvn_file :%{bundle} %{project}/%{bundle}

%build

# no test to run
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc changelog.txt
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.12-alt1_3jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.12-alt1_2jpp8
- unbootsrap build

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.6-alt1_4jpp7
- new release

