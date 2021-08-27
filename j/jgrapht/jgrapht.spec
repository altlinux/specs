%define _unpackaged_files_terminate_build 1

%define oname jgrapht

Name:    jgrapht
Epoch:   1
Version: 1.0.1
Release: alt1_jpp11
Summary: A free Java graph library that provides mathematical graph objs and algorithms
License: LGPLv2+
Group:   Development/Java
URL:     http://jgrapht.sourceforge.net/

BuildArch: noarch

# http://downloads.sourceforge.net/project/jgrapht/JGraphT/Version%%200.8.1/jgrapht-%{version}.tar.gz
Source: %oname-%version.tar

Patch1: %oname-%version-alt-build-core.patch

BuildRequires: rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-default
#BuildRequires: java-devel >= 1.6
BuildRequires: javapackages-local
BuildRequires: maven-local
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

%description
JGraphT is a free Java graph library that provides mathematical graph-theory 
objects and algorithms.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{oname}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{oname}.

%prep
%setup -n %oname-%version
%patch1 -p2

%pom_remove_plugin :maven-shade-plugin jgrapht-demo/pom.xml
%pom_remove_plugin :maven-shade-plugin jgrapht-ext/pom.xml
%pom_remove_plugin :maven-shade-plugin jgrapht-touchgraph/pom.xml

%build
%mvn_build --skip-tests -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc CONTRIBUTING.md CONTRIBUTORS.md HISTORY.md README.md
%doc license-EPL.txt license-LGPL.txt

%files javadoc -f .mfiles-javadoc
%doc CONTRIBUTING.md CONTRIBUTORS.md HISTORY.md README.md
%doc license-EPL.txt license-LGPL.txt

%changelog
* Fri Aug 27 2021 Igor Vlasenko <viy@altlinux.org> 1:1.0.1-alt1_jpp11
- java11 build

* Fri Nov 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.0.1-alt1
- Updated to version 1.0.1.

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_16jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_15jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_14jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_13jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_12jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_6jpp7
- new release

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_5jpp7
- fc update

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.8.2-alt1_1jpp6
- new version

