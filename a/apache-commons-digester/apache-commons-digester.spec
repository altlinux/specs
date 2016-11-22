Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global short_name commons-digester

Name:          apache-%{short_name}
Version:       2.1
Release:       alt3_6jpp8
Summary:       XML to Java object mapping module
Group:         Development/Other
License:       ASL 2.0
URL:           http://commons.apache.org/digester/
Source0:       http://archive.apache.org/dist/commons/digester/source/%{short_name}-%{version}-src.tar.gz
BuildArch:     noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires: apache-commons-beanutils >= 1.8
BuildRequires: apache-commons-logging >= 1.1.1
BuildRequires: maven-local
Source44: import.info

%description
Many projects read XML configuration files to provide initialization of
various Java objects within the system. There are several ways of doing this,
and the Digester component was designed to provide a common implementation
that can be used in many different projects

%package javadoc
Summary:       API documentation for %{name}
Group:         Development/Java
BuildArch: noarch

%description javadoc
This package contains the %{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src

# Compatibility links
%mvn_alias "%{short_name}:%{short_name}" "org.apache.commons:%{short_name}"
%mvn_file :%{short_name} %{short_name} %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt3_6jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt3_5jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt3_14jpp7
- new release

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt3_11jpp7
- fc update

* Tue Mar 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt3_11jpp6
- bumped release to fix obsoletes

* Sat Jan 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt2_11jpp6
- fixed repolib version

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt1_11jpp6
- new version

