Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: maven-local
# END SourceDeps(oneline)
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
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name maven
%bcond_with bootstrap

%global bundled_slf4j_version 1.7.30
%global apphomedir %{_datadir}/%{name}%{?maven_version_suffix}
%global confdir %{_sysconfdir}/%{name}%{?maven_version_suffix}

Name:           maven
Epoch:          1
Version:        3.6.3
Release:        alt5_10jpp11
Summary:        Java project management and project comprehension tool
# maven itself is ASL 2.0
# bundled slf4j is MIT
License:        ASL 2.0 and MIT
URL:            https://maven.apache.org/
BuildArch:      noarch

Source0:        https://archive.apache.org/dist/%{name}/%{name}-3/%{version}/source/apache-%{name}-%{version}-src.tar.gz
Source1:        maven-bash-completion
Source2:        mvn.1

Patch1:         0001-Adapt-mvn-script.patch
# Downstream-specific, avoids dependency on logback
# Used only when %%without logback is in effect
Patch2:         0002-Invoke-logback-via-reflection.patch
Patch3:         0003-Use-non-shaded-HTTP-wagon.patch
Patch4:         0004-Remove-dependency-on-powermock.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(com.google.inject:guice::no_aop:)
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(commons-jxpath:commons-jxpath)
BuildRequires:  mvn(javax.annotation:jsr250-api)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-connector-basic)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-impl)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-spi)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-transport-wagon)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-util)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-file)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.sonatype.plexus:plexus-cipher)
BuildRequires:  mvn(org.sonatype.plexus:plexus-sec-dispatcher)
BuildRequires:  mvn(org.xmlunit:xmlunit-core)
BuildRequires:  mvn(org.xmlunit:xmlunit-matchers)
%endif

# XXX
#BuildRequires:  mvn(org.slf4j:slf4j-simple::sources:) = %{bundled_slf4j_version}
%if %{without bootstrap}
BuildRequires:  mvn(org.slf4j:slf4j-simple::sources:)
%endif

Requires: %{name}-lib = %{epoch}:%{version}-%{release}
Source44: import.info
# maven-filesystem
Obsoletes: maven-filesystem < 0.02



%description
Maven is a software project management and comprehension tool. Based on the
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

%package lib
Group: Development/Java
Summary:        Core part of Maven
# If XMvn is part of the same RPM transaction then it should be
# installed first to avoid triggering rhbz#1014355.
Requires: xmvn-minimal

# Maven upstream uses patched version of SLF4J.  They unpack
# slf4j-simple-sources.jar, apply non-upstreamable, Maven-specific
# patch (using a script written in Groovy), compile and package as
# maven-slf4j-provider.jar, together with Maven-specific additions.
Provides:       bundled(slf4j) = %{bundled_slf4j_version}

%description lib
Core part of Apache Maven that can be used as a library.

%{?javadoc_package}

%prep
%setup -q -n apache-%{name}-%{version}

find -name '*.java' -exec sed -i 's/\r//' {} +
find -name 'pom.xml' -exec sed -i 's/\r//' {} +

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# not really used during build, but a precaution
find -name '*.jar' -not -path '*/test/*' -delete
find -name '*.class' -delete
find -name '*.bat' -delete

%pom_remove_dep -r :powermock-reflect

sed -i 's:\r::' apache-maven/src/conf/settings.xml

# Downloads dependency licenses from the Internet and aggregates them.
# We already ship the licenses in their respective packages.
rm apache-maven/src/main/appended-resources/META-INF/LICENSE.vm

# Disable plugins which are not useful for us
%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin
sed -i "
/buildNumber=/ {
  s/=.*/=Red Hat %{version}-%{release}/
  s/%{dist}$//
}
/timestamp=/ d
" `find -name build.properties`

%mvn_package :apache-maven __noinstall

%pom_change_dep :jansi :::runtime maven-embedder
%pom_remove_dep -r :logback-classic

%mvn_alias :maven-resolver-provider :maven-aether-provider

%pom_xpath_inject 'pom:build/pom:plugins' '
<plugin>
	<groupId>org.eclipse.sisu</groupId>
	<artifactId>sisu-maven-plugin</artifactId>
</plugin>' maven-model-builder/pom.xml

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dproject.build.sourceEncoding=UTF-8

mkdir m2home
(cd m2home
    tar --delay-directory-restore -xvf ../apache-maven/target/*tar.gz
)


%install
%mvn_install

export M2_HOME=$(pwd)/m2home/apache-maven-%{version}%{?ver_add}

install -d -m 755 %{buildroot}%{apphomedir}/conf
install -d -m 755 %{buildroot}%{confdir}
install -d -m 755 %{buildroot}%{_datadir}/bash-completion/completions/

cp -a $M2_HOME/{bin,lib,boot} %{buildroot}%{apphomedir}/
%if %{without bootstrap}
xmvn-subst -s -R %{buildroot} -s %{buildroot}%{apphomedir}
%endif

install -p -m 644 %{SOURCE2} %{buildroot}%{apphomedir}/bin/
gzip -9 %{buildroot}%{apphomedir}/bin/mvn.1
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/bash-completion/completions/mvn%{?maven_version_suffix}
mv $M2_HOME/bin/m2.conf %{buildroot}%{_sysconfdir}/m2%{?maven_version_suffix}.conf
ln -sf %{_sysconfdir}/m2%{?maven_version_suffix}.conf %{buildroot}%{apphomedir}/bin/m2.conf
mv $M2_HOME/conf/settings.xml %{buildroot}%{confdir}/
ln -sf %{confdir}/settings.xml %{buildroot}%{apphomedir}/conf/settings.xml
mv $M2_HOME/conf/logging %{buildroot}%{confdir}/
ln -sf %{confdir}/logging %{buildroot}%{apphomedir}/conf

# Ghosts for alternatives
install -d -m 755 %{buildroot}%{_bindir}/
install -d -m 755 %{buildroot}%{_mandir}/man1/
ln -s `relative %{apphomedir}/bin/mvn %{_bindir}/` %buildroot%{_bindir}/mvn
ln -s `relative %{apphomedir}/bin/mvnDebug %{_bindir}/` %buildroot%{_bindir}/mvnDebug
ln -s `relative %{apphomedir}/bin/mvn.1.gz %{_man1dir}/` %buildroot%{_man1dir}/mvn.1.gz

# Versioned commands and manpages
%if 0%{?maven_version_suffix:1}
ln -s %{apphomedir}/bin/mvn %{buildroot}%{_bindir}/mvn%{maven_version_suffix}
ln -s %{apphomedir}/bin/mvnDebug %{buildroot}%{_bindir}/mvnDebug%{maven_version_suffix}
ln -s %{apphomedir}/bin/mvn.1.gz %{buildroot}%{_mandir}/man1/mvn%{maven_version_suffix}.1.gz
ln -s %{apphomedir}/bin/mvnDebug.1.gz %{buildroot}%{_mandir}/man1/mvnDebug%{maven_version_suffix}.1.gz
%endif

# JDK bindings
install -d -m 755 %{buildroot}%{_javaconfdir}/
echo JAVA_HOME=%{_jvmlibdir}/java-1.8.0-openjdk >%{buildroot}%{_javaconfdir}/maven.conf-openjdk8
echo JAVA_HOME=%{_jvmlibdir}/java-11-openjdk >%{buildroot}%{_javaconfdir}/maven.conf-openjdk11

mkdir -p $RPM_BUILD_ROOT`dirname /etc/mavenrc`
touch $RPM_BUILD_ROOT/etc/mavenrc
# no %{name}-jdk-binding
rm -f %buildroot%{_javaconfdir}/maven.conf-openjdk*


%files lib -f .mfiles
%doc README.md
%doc --no-dereference LICENSE NOTICE
%{apphomedir}
%exclude %{apphomedir}/bin/mvn*
%dir %{confdir}
%dir %{confdir}/logging
%config(noreplace) %{_sysconfdir}/m2%{?maven_version_suffix}.conf
%config(noreplace) %{confdir}/settings.xml
%config(noreplace) %{confdir}/logging/simplelogger.properties

%files
%{apphomedir}/bin/mvn*
%{_bindir}/mvn
%{_bindir}/mvnDebug
%{_datadir}/bash-completion/completions/*
%{_mandir}/man1/mvn.1*
%if 0%{?maven_version_suffix:1}
%{_bindir}/mvn%{maven_version_suffix}
%{_bindir}/mvnDebug%{maven_version_suffix}
%{_mandir}/man1/mvn%{maven_version_suffix}.1*
%{_mandir}/man1/mvnDebug%{maven_version_suffix}.1*
%endif
%config(noreplace,missingok) /etc/mavenrc

%changelog
* Sun Jun 12 2022 Igor Vlasenko <viy@altlinux.org> 1:3.6.3-alt5_10jpp11
- maven-openjdkXX support

* Sat Jun 11 2022 Igor Vlasenko <viy@altlinux.org> 1:3.6.3-alt4_10jpp11
- update

* Wed Jun 08 2022 Igor Vlasenko <viy@altlinux.org> 1:3.6.3-alt4_9jpp11
- nobootstrap

* Tue Jun 07 2022 Igor Vlasenko <viy@altlinux.org> 1:3.6.3-alt3_9jpp11
- jarlink bootstrap for guava update

* Thu May 26 2022 Igor Vlasenko <viy@altlinux.org> 1:3.6.3-alt2_9jpp11
- support for new cdi-api
- added jarlink_bootstrap option

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 1:3.6.3-alt2_8jpp11
- fixed alternatives

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:3.6.3-alt1_8jpp11
- fc34 update

* Wed Jun 02 2021 Igor Vlasenko <viy@altlinux.org> 1:3.6.3-alt1_4jpp11
- new version

* Wed Jun 02 2021 Igor Vlasenko <viy@altlinux.org> 1:3.6.1-alt2_5jpp11
- fixed build with new modello

* Fri May 14 2021 Igor Vlasenko <viy@altlinux.org> 1:3.6.1-alt1_5jpp11
- new version

* Sun May 09 2021 Igor Vlasenko <viy@altlinux.org> 1:3.5.4-alt1_12jpp8
- update

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.5.4-alt1_10jpp8
- fixed build

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.5.4-alt1_7jpp8
- build with new mockito

* Wed Jun 19 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.5.4-alt1_4jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.5.3-alt1_1jpp8
- new version

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt1_5jpp8
- fc 28 update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt1_1jpp8
- new version

* Sun Nov 19 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.5.0-alt1_6jpp8
- new version

* Sun Oct 29 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.3.9-alt1_9jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3.9-alt1_6jpp8
- new fc release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3.9-alt1_4jpp8
- new version

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3.3-alt1_3jpp8
- java 8 mass update

* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.5-alt1_3jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.5-alt0.2jpp
- rebuild to add provides

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

