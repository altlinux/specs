Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          xmlenc
Version:       0.53
Release:       alt1_8jpp7
Summary:       Light-weight XML output library for Java
License:       BSD
#  http://xmlenc.sourceforge.net/
URL:           https://github.com/znerd/xmlenc/
Source0:       https://github.com/znerd/xmlenc/archive/%{name}-%{version}.tar.gz

BuildRequires: mvn(org.znerd:znerd-oss-parent)

# test deps
BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-surefire-provider-junit4
# required by enforcer-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components)
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

%build

%mvn_file : %{name}
%mvn_alias : "%{name}:%{name}"
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.txt COPYRIGHT.txt README.txt THANKS.txt

%files javadoc -f .mfiles-javadoc
%doc COPYRIGHT.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_8jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_4jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_10jpp7
- new version

