Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%def_with repolib
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name: jcommon
Version: 1.0.23
Release: alt1_3jpp8
Summary: JFree Java utility classes
License: LGPLv2+
Group: System/Libraries
# Github: https://github.com/jfree/jcommon
# There are no tags which we can use to get sources. See:
#   https://github.com/jfree/jcommon/issues/1
# Source retrieved via:
#  bash getsources.sh 1ea10aa82e30e0d60f57e1c562281a3ac7dd5cdd 1.0.23
Source: %%{name}-%%{version}.tar.gz
URL: http://www.jfree.org/jcommon
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
Requires: javapackages-tools rpm-build-java
BuildArch: noarch
Source44: import.info

%description
JCommon is a collection of useful classes used by 
JFreeChart, JFreeReport and other projects.

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Documentation
Requires: %{name} = %{version}
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.


%description javadoc -l fr
Javadoc pour %{name}.

%prep
%setup -q
find . -name "*.jar" -exec rm -f {} \;
MVN_BUNDLE_PLUGIN_EXTRA_XML="<extensions>true</extensions>
        <configuration>
          <instructions>
            <Bundle-SymbolicName>org.jfree.jcommon</Bundle-SymbolicName>
            <Bundle-Vendor>Fedora Project</Bundle-Vendor>
            <Bundle-Version>%{version}</Bundle-Version>
            <!-- Do not autogenerate uses clauses in Manifests -->
            <_nouses>true</_nouses>
          </instructions>
        </configuration>"
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_add_plugin org.apache.felix:maven-bundle-plugin . "$MVN_BUNDLE_PLUGIN_EXTRA_XML"
# Change to packaging type bundle so as to be able to use it
# as an OSGi bundle.
%pom_xpath_set "pom:packaging" "bundle"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.23-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.23-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.18-alt1_3jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.18-alt1_2jpp7
- new release

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0.18-alt1_1jpp7
- fc update

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.17-alt1_4jpp7
- new version

* Wed Oct 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.16-alt2_2jpp6
- enabled repolib

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.16-alt1_2jpp6
- added pom

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.12-alt2_3jpp5
- new jpp release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.12-alt1_2jpp5
- converted from JPackage by jppimport script

* Fri Jun 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.9-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Tue Apr 26 2005 Eugene V. Horohorin <genix@altlinux.ru> 1.0.0-alt0.1pre2
- First build for ALTLinux
