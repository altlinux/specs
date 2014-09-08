Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             hawtjni
Version:          1.9
Release:          alt1_1jpp7
Summary:          Code generator that produces the JNI code
Group:            Development/Java
License:          ASL 2.0 and EPL and BSD
URL:              http://hawtjni.fusesource.org/

Source0:          https://github.com/fusesource/hawtjni/archive/hawtjni-project-%{version}.tar.gz
Patch0:           0001-Fix-shading-and-remove-unneeded-modules.patch
Patch1:           0002-Fix-xbean-compatibility.patch
Patch2:           0003-Remove-plexus-maven-plugin-dependency.patch
Patch3:           0004-Remove-eclipse-plugin.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-plugin-plugin
BuildRequires:    maven-surefire-report-plugin
BuildRequires:    maven-project-info-reports-plugin
BuildRequires:    maven-plugin-jxr
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-clean-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    plexus-containers-component-metadata
BuildRequires:    log4j
BuildRequires:    junit4
BuildRequires:    fusesource-pom
BuildRequires:    xbean
Source44: import.info

%description
HawtJNI is a code generator that produces the JNI code needed to
implement java native methods. It is based on the jnigen code generator
that is part of the SWT Tools project which is used to generate all the
JNI code which powers the eclipse platform.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package -n maven-hawtjni-plugin
Summary:          Use HawtJNI from a maven plugin
Group:            Development/Java
Requires:         hawtjni = %{?epoch:%epoch:}%{version}-%{release}

%description -n maven-%{name}-plugin
This package allows to use HawtJNI from a maven plugin.

%prep
%setup -q -n hawtjni-hawtjni-project-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Ready to replace patch0
# %pom_disable_module hawtjni-example
# %pom_disable_module hawtjni-website
# %pom_add_dep "org.apache.maven:maven-compat:3.0.3" maven-hawtjni-plugin/pom.xml
# %pom_remove_plugin ":maven-shade-plugin" hawtjni-generator/pom.xml

%mvn_package ":maven-hawtjni-plugin" maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc readme.md license.txt changelog.md

%files javadoc -f .mfiles-javadoc
%doc license.txt

%files -n maven-hawtjni-plugin -f .mfiles-maven-plugin
%doc license.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_1jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_4jpp7
- configure.ac template fixes for jansi-native

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_4jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt4_5jpp7
- fixed build

* Mon Apr 01 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt3_5jpp7
- fixed build with new junit

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_5jpp7
- fixed maven1 dependency

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_5jpp7
- fc update

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_4jpp7
- new fc release

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_3jpp7
- new version

* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_4jpp6
- fixed build:
  + changed objectweb-asm version in hawtjni-asm.patch to 3.3.1
  + added hawtjni-pom-alt.patch to fix shading

* Fri Feb 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_4jpp6
- new version

