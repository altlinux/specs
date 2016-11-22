Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global short_name      commons-cli

Name:             apache-%{short_name}
Version:          1.3.1
Release:          alt1_3jpp8
Summary:          Command Line Interface Library for Java
Group:            Development/Other
License:          ASL 2.0
URL:              http://commons.apache.org/cli/
Source0:          http://www.apache.org/dist/commons/cli/source/%{short_name}-%{version}-src.tar.gz
# workaround for https://issues.apache.org/jira/browse/CLI-253
Patch0:           CLI-253-workaround.patch
BuildArch:        noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    maven-local
BuildRequires:    jacoco-maven-plugin

Requires: javapackages-tools rpm-build-java
Source44: import.info
Obsoletes: jakarta-%{short_name} < 1:%{version}-%{release}
Conflicts: jakarta-%{short_name} < 1:%{version}-%{release}
Provides: jakarta-commons-cli = %version

%description
The CLI library provides a simple and easy to use API for working with the 
command line arguments and options.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src

%patch0 -p1

# Compatibility links
%mvn_alias "%{short_name}:%{short_name}" "org.apache.commons:%{short_name}"
%mvn_file :commons-cli %{short_name} %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.md RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_2jpp8
- java 8 mass update

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sun Sep 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_9jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_7jpp7
- fc update

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_6jpp6
- add obsoletes

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_6jpp6
- fixed repolib

