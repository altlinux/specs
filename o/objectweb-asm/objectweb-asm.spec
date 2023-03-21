Epoch: 0
Group: Development/Java
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           objectweb-asm
Version:        9.3
Release:        alt1_2jpp11
Summary:        Java bytecode manipulation and analysis framework
License:        BSD
URL:            https://asm.ow2.org/
BuildArch:      noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        parent.pom
Source2:        https://repo1.maven.org/maven2/org/ow2/asm/asm/%{version}/asm-%{version}.pom
Source3:        https://repo1.maven.org/maven2/org/ow2/asm/asm-analysis/%{version}/asm-analysis-%{version}.pom
Source4:        https://repo1.maven.org/maven2/org/ow2/asm/asm-commons/%{version}/asm-commons-%{version}.pom
Source5:        https://repo1.maven.org/maven2/org/ow2/asm/asm-test/%{version}/asm-test-%{version}.pom
Source6:        https://repo1.maven.org/maven2/org/ow2/asm/asm-tree/%{version}/asm-tree-%{version}.pom
Source7:        https://repo1.maven.org/maven2/org/ow2/asm/asm-util/%{version}/asm-util-%{version}.pom
# The source contains binary jars that cannot be verified for licensing and could be proprietary
Source9:        generate-tarball.sh

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
%endif

# Explicit javapackages-tools requires since asm-processor script uses
# /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Source44: import.info

%description
ASM is an all purpose Java bytecode manipulation and analysis
framework.  It can be used to modify existing classes or dynamically
generate classes, directly in binary form.  Provided common
transformations and analysis algorithms allow to easily assemble
custom complex transformations and code analysis tools.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q

# A custom parent pom to aggregate the build
cp -p %{SOURCE1} pom.xml

# Insert poms into modules
for pom in asm asm-analysis asm-commons asm-test asm-tree asm-util; do
  cp -p $RPM_SOURCE_DIR/${pom}-%{version}.pom $pom/pom.xml
  %pom_remove_parent $pom
done

# No need to ship the custom parent pom
%mvn_package :asm-aggregator __noinstall
# Don't ship the test framework to avoid runtime dep on junit
%mvn_package :asm-test __noinstall

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%jpackage_script org.objectweb.asm.xml.Processor "" "" %{name}/asm:%{name}/asm-attrs:%{name}/asm-util %{name}-processor true

%files -f .mfiles
%doc --no-dereference LICENSE.txt
%{_bindir}/%{name}-processor

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:9.3-alt1_2jpp11
- new version

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:9.2-alt1_3jpp11
- new version

* Fri May 27 2022 Igor Vlasenko <viy@altlinux.org> 0:9.1-alt1_3jpp11
- new version

* Thu Jun 03 2021 Igor Vlasenko <viy@altlinux.org> 0:8.0.1-alt1_1jpp8
- new version, use jvm8

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:7.0-alt1_4jpp8
- fc update

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 0:7.0-alt1_2jpp8
- new version

* Thu Jun 20 2019 Igor Vlasenko <viy@altlinux.ru> 0:6.2.1-alt1_1jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:6.1.1-alt1_1jpp8
- new version

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:6.0-alt1_1jpp8
- java update

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:5.1-alt1_8jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:5.1-alt1_7jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.1-alt1_4jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.4-alt1_2jpp8
- new version

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.3-alt1_2jpp8
- java 8 mass update

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_7jpp7
- new release

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_4jpp7
- update

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_4jpp6
- updated OSGi manifest to match version

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt4_4jpp6
- added pom groupid asm

* Sun Oct 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt3_4jpp6
- fixed poms

* Fri Sep 16 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt2_4jpp6
- removed asm2 pom provides

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt1_4jpp6
- new version

* Sat Feb 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_2jpp6
- added osgi manifest

* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt1_2jpp6
- new version

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt2_5jpp5
- added OSGi manifest

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_3jpp5
- converted from JPackage by jppimport script

* Mon Jan 28 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

