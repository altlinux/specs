Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 23
Name:           jfreechart
Version:        1.0.19
Release:        alt1_4jpp8
Summary:        Java chart library

Group:          Development/Java
License:        LGPLv2+
URL:            http://www.jfree.org/jfreechart/
Source0:        http://download.sourceforge.net/sourceforge/jfreechart/%{name}-%{version}.zip
Patch0:         build_swt_encoding_fix.patch

BuildRequires:  maven-local
BuildRequires:  maven-plugin-bundle
BuildRequires:  mvn(org.jfree:jcommon) >= 1.0.23
BuildRequires:  servlet >= 2.5
%if 0%{?fedora}
BuildRequires:  eclipse-swt
%endif

BuildArch:      noarch
Source44: import.info

%description
JFreeChart is a free 100% Java chart library that makes it easy for
developers to display professional quality charts in their applications.

%if 0%{?fedora}
%package swt
Summary:        Swt extension for jfreechart
Group:          Development/Java
Requires:       %{name} = %{version}
Requires:       eclipse-swt jpackage-utils

%description swt
Experimental swt extension for jfreechart.
%endif

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.



%description javadoc -l fr
Javadoc pour %{name}.

%prep
%setup -q
# Erase prebuilt files
find \( -name '*.jar' -o -name '*.class' \) -exec rm -f '{}' \;
%patch0 -p2

MVN_BUNDLE_PLUGIN_EXTRA_XML="<extensions>true</extensions>
        <configuration>
          <instructions>
            <Bundle-SymbolicName>org.jfree.jfreechart</Bundle-SymbolicName>
            <Bundle-Vendor>Fedora Project</Bundle-Vendor>
            <Bundle-Version>%{version}</Bundle-Version>
            <!-- Do not autogenerate uses clauses in Manifests -->
            <Import-Package>
              !javax.servlet,
              !javax.servlet.http,
              *
            </Import-Package>
            <_nouses>true</_nouses>
          </instructions>
        </configuration>"
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-jxr-plugin
%pom_remove_plugin :maven-javadoc-plugin

%pom_add_plugin org.apache.felix:maven-bundle-plugin . "$MVN_BUNDLE_PLUGIN_EXTRA_XML"
%pom_add_plugin org.apache.maven.plugins:maven-javadoc-plugin . "<configuration><excludePackageNames>org.jfree.chart.fx*</excludePackageNames></configuration>"
# Change to packaging type bundle so as to be able to use it
# as an OSGi bundle.
%pom_xpath_set "pom:packaging" "bundle"

%build
# Ignore failing test: SegmentedTimelineTest
%mvn_build -- -Dmaven.test.failure.ignore=true

%if 0%{?fedora}
# /usr/lib/java/swt.jar is an arch independent path to swt
ant -f ant/build-swt.xml \
        -Dswt.jar=%_jnidir/swt.jar \
        -Djcommon.jar=$(build-classpath jcommon) \
        -Djfreechart.jar=target/jfreechart-%{version}.jar
%endif

%install
%mvn_install

%if 0%{?fedora}
install -m 644 lib/swtgraphics2d.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}/swtgraphics2d.jar
install -m 644 lib/jfreechart-%{version}-swt.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-swt.jar
%endif

%files -f .mfiles
%doc ChangeLog NEWS README.txt

%if 0%{?fedora}
%files swt
%{_javadir}/%{name}/swtgraphics2d*.jar
%{_javadir}/%{name}/%{name}-swt*.jar
%endif

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.19-alt1_4jpp8
- fixed build

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.19-alt1_3jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt3_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt3_9jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt3_3jpp7
- new fc release

* Sat Sep 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt3_2jpp7
- added jpp compat symlink

* Sat Sep 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt2_2jpp7
- added jfreechart:jfreechart depmap

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt1_2jpp7
- new version

* Wed Jan 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt3_3jpp6
- fixed repolib dep on jcommon

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt2_3jpp6
- new jpp relase

* Wed Oct 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt2_2jpp6
- fixed jcommon version in repolib

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt1_2jpp6
- added pom

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.9-alt2_4jpp5
- new jpp release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.9-alt1_2jpp5
- converted from JPackage by jppimport script

* Tue Oct 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.5-alt1_1jpp1.7
- updated to new jpackage release

* Tue Apr 26 2005 Eugene V. Horohorin <genix@altlinux.ru> 1.0.0-alt0.1pre2
- First build for ALTLinux
