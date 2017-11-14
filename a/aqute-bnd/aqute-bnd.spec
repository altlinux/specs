Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without ant_tasks
%if 0%{?fedora}
%bcond_without maven_plugin
%endif

Name:           aqute-bnd
Version:        3.3.0
Release:        alt1_7jpp8
Summary:        BND Tool
License:        ASL 2.0
URL:            http://bnd.bndtools.org/
BuildArch:      noarch

Source0:        %{version}.REL.tar.gz
# removes bundled jars from upstream tarball
# run as:
# ./repack-tarball.sh
Source1:        repack-tarball.sh

Source2:        parent.pom
Source3:        https://repo1.maven.org/maven2/biz/aQute/bnd/aQute.libg/%{version}/aQute.libg-%{version}.pom
Source4:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd/%{version}/biz.aQute.bnd-%{version}.pom
Source5:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/%{version}/biz.aQute.bndlib-%{version}.pom
Source6:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd.annotation/%{version}/biz.aQute.bnd.annotation-%{version}.pom

Patch0:         0001-Port-to-Java-8.patch
Patch1:         0002-Disable-removed-commands.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.osgi:osgi.annotation)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
%if %{with ant_tasks}
BuildRequires:  mvn(org.apache.ant:ant)
%endif
%if %{with maven_plugin}
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
%endif
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

%if %{with maven_plugin}
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
%setup -q -n bnd-%{version}.REL

rm gradlew*

%patch0 -p1
%patch1 -p1

# the commands pull in more dependencies than we want (felix-resolver, jetty)
rm biz.aQute.bnd/src/aQute/bnd/main/{RemoteCommand,ResolveCommand}.java

sed 's/@VERSION@/%{version}/' %SOURCE2 > pom.xml
sed -i 's|${Bundle-Version}|%{version}|' biz.aQute.bndlib/src/aQute/bnd/osgi/bnd.info

%if %{without ant_tasks}
rm -rf biz.aQute.bnd/src/aQute/bnd/ant
%endif

%if %{without maven_plugin}
%pom_disable_module maven
%endif

# libg
pushd aQute.libg
cp -p %{SOURCE3} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}
%pom_add_dep org.osgi:osgi.cmpn
%pom_add_dep org.slf4j:slf4j-api
popd

# bndlib.annotations
pushd biz.aQute.bnd.annotation
cp -p %{SOURCE6} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}
popd

# bndlib
pushd biz.aQute.bndlib
cp -p %{SOURCE5} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}

%pom_add_dep org.osgi:osgi.annotation
%pom_add_dep org.osgi:osgi.core
%pom_add_dep org.osgi:osgi.cmpn
%pom_add_dep org.slf4j:slf4j-api
%pom_add_dep biz.aQute.bnd:aQute.libg:%{version}
%pom_add_dep biz.aQute.bnd:biz.aQute.bnd.annotation:%{version}
popd

# bnd
pushd biz.aQute.bnd
cp -p %{SOURCE4} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}

%pom_add_dep biz.aQute.bnd:biz.aQute.bndlib:%{version}
%pom_add_dep biz.aQute.bnd:aQute.libg:%{version}
%pom_add_dep biz.aQute.bnd:biz.aQute.bnd.annotation:%{version}
%if %{with ant_tasks}
%pom_add_dep org.apache.ant:ant
%endif
%pom_add_dep org.osgi:osgi.annotation
%pom_add_dep org.osgi:osgi.core
%pom_add_dep org.osgi:osgi.cmpn
%pom_add_dep org.slf4j:slf4j-api

%pom_add_dep org.slf4j:slf4j-simple:runtime
popd

# maven-plugins

# Unavailable reactor dependency - org.osgi.impl.bundle.repoindex.cli
%pom_disable_module bnd-indexer-maven-plugin maven
# Requires unbuilt parts of bnd
%pom_disable_module bnd-export-maven-plugin maven
# Integration tests require Internet access
%pom_remove_plugin -r :maven-invoker-plugin maven


%mvn_alias biz.aQute.bnd:biz.aQute.bnd :bnd biz.aQute:bnd
%mvn_alias biz.aQute.bnd:biz.aQute.bndlib :bndlib biz.aQute:bndlib

%mvn_package biz.aQute.bnd:biz.aQute.bndlib bndlib
%mvn_package biz.aQute.bnd:biz.aQute.bnd.annotation bndlib
%mvn_package biz.aQute.bnd:aQute.libg bndlib
%mvn_package biz.aQute.bnd:bnd-maven-plugin maven
%mvn_package biz.aQute.bnd:bnd-baseline-maven-plugin maven
%mvn_package biz.aQute.bnd:parent __noinstall
%mvn_package biz.aQute.bnd:bnd-plugin-parent __noinstall

%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%if %{with ant_tasks}
install -d -m 755 %{buildroot}%{_sysconfdir}/ant.d
echo "aqute-bnd slf4j/api slf4j/simple osgi-annotation osgi-core osgi-compendium" >%{buildroot}%{_sysconfdir}/ant.d/%{name}
%endif

%jpackage_script aQute.bnd.main.bnd "" "" aqute-bnd:slf4j/slf4j-api:slf4j/slf4j-simple:osgi-annotation:osgi-core:osgi-compendium bnd 1

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files -f .mfiles
%doc LICENSE
%{_bindir}/bnd
%if %{with ant_tasks}
%config(noreplace) %{_sysconfdir}/ant.d/*
%endif
%config(noreplace,missingok) /etc/java/%{name}.conf

%files -n aqute-bndlib -f .mfiles-bndlib
%doc LICENSE

%if %{with maven_plugin}
%files -n bnd-maven-plugin -f .mfiles-maven
%endif

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
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

