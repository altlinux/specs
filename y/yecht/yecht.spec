Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global commitversion 157cf13
%global dlversion 0.0.2-0-g157cf13
%global cluster jruby

Name:     yecht
Version:  1.0
Release:  alt1_3jpp8
Summary:  A YAML processor based on Syck
License:  MIT
URL:      http://github.com/%{cluster}/%{name}
Source0:  https://github.com/%{cluster}/%{name}/archive/%{name}-%{version}.zip
Patch0:   disable-jruby-dep.patch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires: maven-local
Requires: javapackages-tools rpm-build-java

BuildArch:      noarch
Source44: import.info

%description
Yecht is a Syck port, a YAML 1.0 processor for Ruby.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -n %{name}-%{name}-%{version}
%patch0

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_8jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_7jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_6jpp7
- new version

