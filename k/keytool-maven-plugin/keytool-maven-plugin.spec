BuildRequires: maven-project
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat mojo-parent maven-plugin-plugin

%global group_id  org.codehaus.mojo

Name:             keytool-maven-plugin
Version:          1.0
Release:          alt7_18jpp8
Summary:          A plugin that wraps the keytool program and allows to manipulate keystores
License:          MIT and ASL 2.0
Group:            Development/Other
# http://mojo.codehaus.org/keytool-maven-plugin/
URL:              http://mojo.codehaus.org/%{name}/
# svn export http://svn.codehaus.org/mojo/tags/keytool-maven-plugin-1.0/ keytool-maven-plugin-1.0
# tar caf keytool-maven-plugin-1.0.tar.xz keytool-maven-plugin-1.0
Source0:          %{name}-%{version}.tar.xz
Source1:          LICENSE-ASL

BuildArch:        noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    maven-local

Requires: javapackages-tools
Requires:         maven
Requires:         plexus-utils
Requires:         apache-commons-lang
Source44: import.info

%description
A plugin that wraps the keytool program bundled with Sun's Java SDK.
It provides the capability to manipulate keys and keystores
with the goals "keytool:genkey" and "keytool:clean".

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

# fixing licenses
mv LICENSE.txt LICENSE-MIT
cp %{SOURCE1} LICENSE-ASL

# junit dependency was removed in Plexus 1.6
%pom_add_dep junit:junit::test

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-MIT LICENSE-ASL

%files javadoc -f .mfiles-javadoc
%doc LICENSE-MIT LICENSE-ASL

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt7_18jpp8
- fixed build with new maven-reporting-impl

* Tue Nov 07 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt6_18jpp8
- fixed build

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5_18jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5_17jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5_12jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5_10jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5_7jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_7jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_7jpp7
- fixed build

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_7jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6jpp7
- new fc release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5jpp7
- complete build

