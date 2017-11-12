Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          xmlenc
Version:       0.53
Release:       alt1_15jpp8
Summary:       Light-weight XML output library for Java
License:       BSD
#  http://xmlenc.sourceforge.net/
URL:           https://github.com/znerd/xmlenc/
Source0:       https://github.com/znerd/xmlenc/archive/%{name}-%{version}.tar.gz

BuildRequires: mvn(org.znerd:znerd-oss-parent:pom:)
# test deps
BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
# required by enforcer-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildArch:     noarch
Source44: import.info

%description
This library is a fast stream-based XML output library for Java. 
Main design goals are performance, simplicity and pureness. 

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}

%prep
%setup -q -n %{name}-%{name}-%{version}

find . -name "*.class" -delete
find . -name ".*" -delete
find . -name "*.jar" -type f -delete

%mvn_file : %{name}
%mvn_alias : "%{name}:%{name}"

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.txt README.txt THANKS.txt
%doc COPYRIGHT.txt

%files javadoc -f .mfiles-javadoc
%doc COPYRIGHT.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_15jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_14jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_13jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_12jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_8jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_4jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_10jpp7
- new version

