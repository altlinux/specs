Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without  logback

%global bundled_slf4j_version 1.7.25

Name:           maven
Epoch:          1
Version:        3.5.2
Release:        alt1_1jpp8
Summary:        Java project management and project comprehension tool
License:        ASL 2.0
URL:            http://maven.apache.org/
BuildArch:      noarch

Source0:        http://archive.apache.org/dist/%{name}/%{name}-3/%{version}/source/apache-%{name}-%{version}-src.tar.gz
Source1:        maven-bash-completion
Source2:        mvn.1

Patch1:         0001-Adapt-mvn-script.patch
# Downstream-specific, avoids dependency on logback
# Used only when %%without logback is in effect
Patch2:         0002-Invoke-logback-via-reflection.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava)
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
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-connector-basic)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-impl)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-spi)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-transport-wagon)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-util)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-file)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http::shaded:)
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
BuildRequires:  mvn(xmlunit:xmlunit)

BuildRequires:  slf4j-sources = %{bundled_slf4j_version}

%if %{with logback}
BuildRequires:  mvn(ch.qos.logback:logback-classic)
%endif

Requires:       %{name}-lib = %{epoch}:%{version}-%{release}

# Theoretically Maven might be usable with just JRE, but typical Maven
# workflow requires full JDK, so we recommend it here.

# XMvn does generate auto-requires, but explicit requires are still
# needed because some symlinked JARs are not present in Maven POMs or
# their dependency scope prevents them from being added automatically
# by XMvn.  It would be possible to explicitly specify only
# dependencies which are not generated automatically, but adding
# everything seems to be easier.
Requires:       aopalliance
Requires:       apache-commons-cli
Requires:       apache-commons-codec
Requires:       apache-commons-io
Requires:       apache-commons-lang3
Requires:       apache-commons-logging
Requires:       atinject
Requires:       cdi-api
Requires:       geronimo-annotation
Requires:       google-guice
Requires:       guava
Requires:       hawtjni-runtime
Requires:       httpcomponents-client
Requires:       httpcomponents-core
Requires:       jansi
Requires:       jansi-native
Requires:       jcl-over-slf4j
Requires:       maven-resolver-api
Requires:       maven-resolver-connector-basic
Requires:       maven-resolver-impl
Requires:       maven-resolver-spi
Requires:       maven-resolver-transport-wagon
Requires:       maven-resolver-util
Requires:       maven-shared-utils
Requires:       maven-wagon-file
Requires:       maven-wagon-http
Requires:       maven-wagon-http-shared
Requires:       maven-wagon-provider-api
Requires:       plexus-cipher
Requires:       plexus-classworlds
Requires:       plexus-containers-component-annotations
Requires:       plexus-interpolation
Requires:       plexus-sec-dispatcher
Requires:       plexus-utils
Requires:       sisu-inject
Requires:       sisu-plexus
Requires:       slf4j
# maven-filesystem
Requires: maven-filesystem
BuildArch: noarch
Source44: import.info


%description
Maven is a software project management and comprehension tool. Based on the
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

%package        lib
Group: Development/Java
Summary:        Core part of Maven
# If XMvn is part of the same RPM transaction then it should be
# installed first to avoid triggering rhbz#1014355.

# Maven upstream uses patched version of SLF4J.  They unpack
# slf4j-simple-sources.jar, apply non-upstreamable, Maven-specific
# patch (using a script written in Groovy), compile and package as
# maven-slf4j-provider.jar, together with Maven-specific additions.
Provides:       bundled(slf4j) = %{bundled_slf4j_version}

%description    lib
Core part of Apache Maven that can be used as a library.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n apache-%{name}-%{version}

%patch1 -p1

# not really used during build, but a precaution
find -name '*.jar' -not -path '*/test/*' -delete
find -name '*.class' -delete
find -name '*.bat' -delete

sed -i 's:\r::' apache-maven/src/conf/settings.xml

# Downloads dependency licenses from the Internet and aggregates them.
# We already ship the licenses in their respective packages.
rm apache-maven/src/main/appended-resources/META-INF/LICENSE.vm

# Disable plugins which are not useful for us
%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin
sed -i "
/buildNumber=/ {
  s/=.*/=Red Hat %{version}-%{release}/
  s/%{dist}$//
}
/timestamp=/ d
" `find -name build.properties`

%mvn_package :apache-maven __noinstall

%if %{without logback}
%pom_remove_dep -r :logback-classic
%patch2 -p1
%endif

%mvn_alias :maven-resolver-provider :maven-aether-provider

%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

mkdir m2home
(cd m2home
    tar --delay-directory-restore -xvf ../apache-maven/target/*tar.gz
)


%install
%mvn_install

export M2_HOME=$(pwd)/m2home/apache-maven-%{version}%{?ver_add}

install -d -m 755 %{buildroot}%{_datadir}/%{name}/conf
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m 755 %{buildroot}%{_datadir}/bash-completion/completions
install -d -m 755 %{buildroot}%{_mandir}/man1

cp -a $M2_HOME/{bin,lib,boot} %{buildroot}%{_datadir}/%{name}/
xmvn-subst -R %{buildroot} -s %{buildroot}%{_datadir}/%{name}

# Transitive deps of wagon-http, missing because of unshading
build-jar-repository -s -p %{buildroot}%{_datadir}/%{name}/lib \
    commons-{codec,logging} httpcomponents/{httpclient,httpcore} maven-wagon/http-shared

# Transitive deps of cdi-api that should have been excluded
rm %{buildroot}%{_datadir}/%{name}/lib/jboss-interceptors*.jar
rm %{buildroot}%{_datadir}/%{name}/lib/javax.el-api*.jar

for cmd in mvn mvnDebug mvnyjp; do
    ln -s %{_datadir}/%{name}/bin/$cmd %{buildroot}%{_bindir}/$cmd
    echo ".so man1/mvn.1" >%{buildroot}%{_mandir}/man1/$cmd.1
done
install -p -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/bash-completion/completions/mvn
mv $M2_HOME/bin/m2.conf %{buildroot}%{_sysconfdir}
ln -sf %{_sysconfdir}/m2.conf %{buildroot}%{_datadir}/%{name}/bin/m2.conf
mv $M2_HOME/conf/settings.xml %{buildroot}%{_sysconfdir}/%{name}
ln -sf %{_sysconfdir}/%{name}/settings.xml %{buildroot}%{_datadir}/%{name}/conf/settings.xml
mv $M2_HOME/conf/logging %{buildroot}%{_sysconfdir}/%{name}
ln -sf %{_sysconfdir}/%{name}/logging %{buildroot}%{_datadir}/%{name}/conf
# maven-filesystem
rm -f %buildroot%_datadir/%{name}/repository-jni/JPP

mkdir -p $RPM_BUILD_ROOT`dirname /etc/mavenrc`
touch $RPM_BUILD_ROOT/etc/mavenrc

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/maven.conf`
touch $RPM_BUILD_ROOT/etc/java/maven.conf

ln -s maven-resolver-provider.jar $RPM_BUILD_ROOT%_javadir/maven/maven-aether-provider.jar

%pre 
# https://bugzilla.altlinux.org/show_bug.cgi?id=27807 (upgrade from maven1)
[ -d %_datadir/maven/repository/JPP ] && rm -rf %_datadir/maven/repository/JPP ||:


%files lib -f .mfiles
%doc LICENSE NOTICE README.md
%{_datadir}/%{name}
%dir %{_javadir}/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/logging
%config(noreplace) %{_sysconfdir}/m2.conf
%config(noreplace) %{_sysconfdir}/%{name}/settings.xml
%config(noreplace) %{_sysconfdir}/%{name}/logging/simplelogger.properties
%_javadir/maven/maven-aether-provider.jar

%files
%attr(0755,root,root) %{_bindir}/mvn*
%{_datadir}/bash-completion
%{_mandir}/man1/mvn*.1*
%config(noreplace,missingok) /etc/mavenrc
%config(noreplace,missingok) /etc/java/maven.conf

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
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

