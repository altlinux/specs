Epoch: 0
Group: Development/Java
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

%if %{without bootstrap} && !0%{?rhel}
%bcond_without bnd_maven_plugin
%else
%bcond_with bnd_maven_plugin
%endif

Name:           aqute-bnd
Version:        6.2.0
Release:        alt1_2jpp11
Summary:        BND Tool
# Part of jpm is under BSD, but jpm is not included in binary RPM
License:        ASL 2.0 or EPL-2.0
URL:            https://bnd.bndtools.org/
BuildArch:      noarch

Source0:        %{name}-%{version}.tar.gz
# removes bundled jars from upstream tarball
# run as:
# ./generate-tarball.sh
Source1:        generate-tarball.sh

Source2:        parent.pom
Source3:        https://repo1.maven.org/maven2/biz/aQute/bnd/aQute.libg/%{version}/aQute.libg-%{version}.pom
Source4:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd/%{version}/biz.aQute.bnd-%{version}.pom
Source5:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/%{version}/biz.aQute.bndlib-%{version}.pom
Source6:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd.annotation/%{version}/biz.aQute.bnd.annotation-%{version}.pom
Source7:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd.ant/%{version}/biz.aQute.bnd.ant-%{version}.pom
Source8:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd.util/%{version}/biz.aQute.bnd.util-%{version}.pom

Patch1:         0001-Disable-removed-commands.patch
Patch2:         0002-Port-to-OSGI-7.0.0.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.junit:junit-bom:pom:)
BuildRequires:  mvn(org.osgi:osgi.annotation)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
%endif
%if %{with bnd_maven_plugin}
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-mapping)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
%endif

# Explicit javapackages-tools requires since bnd script uses
# /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Source44: import.info

%description
The bnd tool helps you create and diagnose OSGi bundles.
The key functions are:
- Show the manifest and JAR contents of a bundle
- Wrap a JAR so that it becomes a bundle
- Create a Bundle from a specification and a class path
- Verify the validity of the manifest entries
The tool is capable of acting as:
- Command line tool
- File format
- Directives
- Use of macros

%package -n aqute-bndlib
Group: Development/Java
Summary:        BND library

%description -n aqute-bndlib
%{summary}.

%if %{with bnd_maven_plugin}
%package -n bnd-maven-plugin
Group: Development/Java
Summary:        BND Maven plugin

%description -n bnd-maven-plugin
%{summary}.
%endif

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q

%patch1 -p1
%patch2 -p1

# the commands pull in more dependencies than we want (felix-resolver, jetty)
rm biz.aQute.bnd/src/aQute/bnd/main/{ExportReportCommand,MbrCommand,RemoteCommand,ReporterLogger,ResolveCommand,Shell}.java

sed 's/@VERSION@/%{version}/' %SOURCE2 > pom.xml
sed -i 's|${Bundle-Version}|%{version}|' biz.aQute.bndlib/src/aQute/bnd/osgi/bnd.info

%if %{without bnd_maven_plugin}
%pom_disable_module maven
%endif

# libg
pushd aQute.libg
cp -p %{SOURCE3} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}
%pom_add_dep org.osgi:osgi.cmpn
popd

# bnd.annotation
pushd biz.aQute.bnd.annotation
cp -p %{SOURCE6} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}
%pom_add_dep org.osgi:osgi.core
%pom_add_dep org.osgi:osgi.cmpn
popd

# bndlib
pushd biz.aQute.bndlib
cp -p %{SOURCE5} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}
%pom_add_dep org.osgi:osgi.cmpn
%pom_add_dep biz.aQute.bnd:aQute.libg:%{version}
%pom_add_dep biz.aQute.bnd:biz.aQute.bnd.annotation:%{version}
popd

# bnd.ant
pushd biz.aQute.bnd.ant
cp -p %{SOURCE7} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}
popd

# bnd
cp -r biz.aQute.bnd.exporters/src/aQute/bnd/exporter biz.aQute.bnd/src/aQute/bnd/
pushd biz.aQute.bnd
cp -p %{SOURCE4} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}
%pom_remove_dep :biz.aQute.resolve
%pom_remove_dep :biz.aQute.repository
%pom_remove_dep :biz.aQute.bnd.exporters
%pom_remove_dep :biz.aQute.bnd.reporter
%pom_remove_dep :biz.aQute.remote.api
%pom_remove_dep :snakeyaml
%pom_remove_dep :jline
%pom_remove_dep org.osgi:org.osgi.service.coordinator
%pom_remove_dep org.osgi:org.osgi.service.resolver
popd

# bnd.util
pushd biz.aQute.bnd.util
cp -p %{SOURCE8} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}
%pom_add_dep biz.aQute.bnd:aQute.libg:%{version}
popd

%pom_remove_dep -r org.osgi:org.osgi.dto
%pom_remove_dep -r org.osgi:org.osgi.framework
%pom_remove_dep -r org.osgi:org.osgi.namespace.contract
%pom_remove_dep -r org.osgi:org.osgi.namespace.extender
%pom_remove_dep -r org.osgi:org.osgi.namespace.implementation
%pom_remove_dep -r org.osgi:org.osgi.namespace.service
%pom_remove_dep -r org.osgi:org.osgi.resource
%pom_remove_dep -r org.osgi:org.osgi.service.log
%pom_remove_dep -r org.osgi:org.osgi.service.repository
%pom_remove_dep -r org.osgi:org.osgi.service.serviceloader
%pom_remove_dep -r org.osgi:org.osgi.util.function
%pom_remove_dep -r org.osgi:org.osgi.util.promise
%pom_remove_dep -r org.osgi:org.osgi.util.tracker

%pom_xpath_remove -r pom:project/pom:dependencies/pom:dependency/pom:scope

# maven-plugins
cp -r biz.aQute.bnd.maven/src/aQute/bnd/maven/lib/configuration maven/bnd-maven-plugin/src/main/java/aQute/bnd/maven/lib
cp -r biz.aQute.bnd.maven/src/aQute/bnd/maven/lib/executions maven/bnd-maven-plugin/src/main/java/aQute/bnd/maven/lib
pushd maven
%pom_remove_dep -r :biz.aQute.bnd.maven
# Unavailable reactor dependency - org.osgi.impl.bundle.repoindex.cli
%pom_disable_module bnd-indexer-maven-plugin
# Requires unbuilt parts of bnd
%pom_disable_module bnd-export-maven-plugin
%pom_disable_module bnd-reporter-maven-plugin
%pom_disable_module bnd-resolver-maven-plugin
%pom_disable_module bnd-run-maven-plugin
%pom_disable_module bnd-testing-maven-plugin
# Integration tests require Internet access
%pom_remove_plugin -r :maven-invoker-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_remove_plugin -r :flatten-maven-plugin
popd

%mvn_alias biz.aQute.bnd:biz.aQute.bnd :bnd biz.aQute:bnd
%mvn_alias biz.aQute.bnd:biz.aQute.bndlib :bndlib biz.aQute:bndlib

%mvn_package biz.aQute.bnd:biz.aQute.bndlib bndlib
%mvn_package biz.aQute.bnd:biz.aQute.bnd.annotation bndlib
%mvn_package biz.aQute.bnd:aQute.libg bndlib
%mvn_package biz.aQute.bnd:parent __noinstall
%mvn_package biz.aQute.bnd:bnd-plugin-parent __noinstall
%if %{with bnd_maven_plugin}
%mvn_package biz.aQute.bnd:bnd-maven-plugin maven
%mvn_package biz.aQute.bnd:bnd-baseline-maven-plugin maven
%endif

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

install -d -m 755 %{buildroot}%{_sysconfdir}/ant.d
echo "aqute-bnd slf4j/api slf4j/simple osgi-annotation osgi-core osgi-compendium" >%{buildroot}%{_sysconfdir}/ant.d/%{name}

%jpackage_script aQute.bnd.main.bnd "" "" aqute-bnd:slf4j/slf4j-api:slf4j/slf4j-simple:osgi-annotation:osgi-core:osgi-compendium bnd 1

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files -f .mfiles
%doc --no-dereference LICENSE
%{_bindir}/bnd
%config(noreplace) %{_sysconfdir}/ant.d/*
%config(noreplace,missingok) /etc/java/%{name}.conf

%files -n aqute-bndlib -f .mfiles-bndlib
%doc --no-dereference LICENSE

%if %{with bnd_maven_plugin}
%files -n bnd-maven-plugin -f .mfiles-maven
%endif

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:6.2.0-alt1_2jpp11
- new version

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:5.2.0-alt1_9jpp11
- update

* Wed Jun 08 2022 Igor Vlasenko <viy@altlinux.org> 0:5.2.0-alt1_5jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:4.3.1-alt1_4jpp11
- fc34 update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:4.3.1-alt1_1jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.5.0-alt1_8jpp8
- fc update

* Mon Jul 15 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.5.0-alt1_6jpp8
- fixed build with osgi-compendium-7

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.5.0-alt1_5jpp8
- new version

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.5.0-alt1_2jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.5.0-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.3.0-alt1_7jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.3.0-alt1_6jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt2_3jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt2_2jpp8
- new versio

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt0.2jpp
- removed compatibility symlink

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt2_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt2_8jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt1_7jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

