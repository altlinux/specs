Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global base_name       pool
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          1.6
Release:          alt2_12jpp8
Summary:          Apache Commons Pool Package
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:        noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    maven-local
Source44: import.info

%description
The goal of Pool package is it to create and maintain an object (instance)
pooling package to be distributed under the ASF license. The package should
support a variety of pool implementations, but encourage support of an
interface that makes these implementations interchangeable.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src

%mvn_alias : org.apache.commons:%{short_name}
%mvn_file : %{name} %{short_name}

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.txt LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp7
- new version

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt3_6jpp6
- fixed build

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt2_6jpp6
- fixed build with maven3

* Thu Feb 24 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt1_6jpp6
- new version

