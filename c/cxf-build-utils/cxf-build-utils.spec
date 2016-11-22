# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             cxf-build-utils
Version:          2.6.0
Release:          alt1_3jpp8
Summary:          Apache CXF Build Utils
Group:            Development/Other
License:          ASL 2.0
URL:              http://cxf.apache.org/build-utils.html

# svn export http://svn.apache.org/repos/asf/cxf/build-utils/tags/cxf-build-utils-2.6.0/ cxf-build-utils-2.6.0
# tar cafJ cxf-build-utils-2.6.0.tar.xz cxf-build-utils-2.6.0
Source0:          cxf-build-utils-%{version}.tar.xz

# PMD support in Fedora
Patch0:           0001-Support-for-PMD-from-Fedora.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-shade-plugin
BuildRequires:    glassfish-fastinfoset
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    pmd
Source44: import.info

%description
The Apache CXF Build Utils contains common utilities and configuration files
that are used by multiple versions of the CXF builds.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n cxf-build-utils-%{version}
%patch0 -p1

%pom_remove_dep net.sourceforge.pmd:pmd buildtools/pom.xml
%pom_add_dep net.sourceforge.pmd:pmd-java buildtools/pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_3jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_2jpp8
- new version

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt5_6jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt5_4jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt4_4jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt3_4jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_4jpp7
- new version

