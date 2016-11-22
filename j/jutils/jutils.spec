# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jutils
Version:        1.0.1
Release:        alt2_13.20110719svnjpp8
Summary:        Common utilities for the Java Gaming Interface

Group:          Development/Other
License:        BSD
URL:            http://java.net/projects/jutils
### upstream only provides subversion checkout
# tar creation instructions
# svn export -r30 https://svn.java.net/svn/jutils~svn/trunk jutils
# tar cfJ jutils-1.0.1.tar.xz jutils 
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  maven-local
Source44: import.info

%description
This is the utils project that contains useful shared functionality
for the other Java Games Initiative APIs.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}
sed -i 's/-SNAPSHOT//' pom.xml

%mvn_file : %{name}

%build
# Skip tests because they require an X display
%mvn_build -- -Dmaven.test.skip=true

%install
%mvn_install

%files -f .mfiles
%doc README.txt 

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_13.20110719svnjpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_12.20110719svnjpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_9.20110719svnjpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_7.20110719svnjpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_3.20110719svnjpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3.20110719svnjpp7
- initial build

