Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven
Version:        3.3.9
Release:        alt1_6jpp8
Summary:        Java project management and project comprehension tool
License:        ASL 2.0
URL:            http://maven.apache.org/
BuildArch:      noarch

Source0:        http://archive.apache.org/dist/%{name}/%{name}-3/%{version}/source/apache-%{name}-%{version}-src.tar.gz
Source1:        maven-bash-completion
Source2:        mvn.1
Source200:      %{name}-script

Patch0:         0001-Force-SLF4J-SimpleLogger-re-initialization.patch

BuildRequires:  maven-local

BuildRequires:  aether-api >= 1:0
BuildRequires:  aether-connector-basic >= 1:0
BuildRequires:  aether-impl >= 1:0
BuildRequires:  aether-spi >= 1:0
BuildRequires:  aether-util >= 1:0
BuildRequires:  aether-transport-wagon >= 1:0
BuildRequires:  aopalliance
BuildRequires:  apache-commons-cli
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang
BuildRequires:  apache-commons-lang3
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-jxpath
BuildRequires:  apache-commons-logging
BuildRequires:  apache-resource-bundles
BuildRequires:  atinject
BuildRequires:  buildnumber-maven-plugin
BuildRequires:  cglib
BuildRequires:  easymock3
BuildRequires:  google-guice >= 3.1.6
BuildRequires:  hamcrest
BuildRequires:  httpcomponents-core
BuildRequires:  httpcomponents-client
BuildRequires:  jsoup
BuildRequires:  jsr-305
BuildRequires:  junit
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-parent
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-wagon-file
BuildRequires:  maven-wagon-http
BuildRequires:  maven-wagon-http-shared
BuildRequires:  maven-wagon-provider-api
BuildRequires:  objectweb-asm
BuildRequires:  plexus-cipher
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-containers-component-metadata >= 1.5.5
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-sec-dispatcher
BuildRequires:  plexus-utils >= 3.0.10
BuildRequires:  sisu-inject >= 1:0.1
BuildRequires:  sisu-plexus >= 1:0.1
BuildRequires:  sisu-mojos
BuildRequires:  slf4j
BuildRequires:  xmlunit
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)

Requires:       %{name}-lib = %{version}

# Theoretically Maven might be usable with just JRE, but typical Maven
# workflow requires full JDK, so we recommend it here.

# XMvn does generate auto-requires, but explicit requires are still
# needed because some symlinked JARs are not present in Maven POMs or
# their dependency scope prevents them from being added automatically
# by XMvn.  It would be possible to explicitly specify only
# dependencies which are not generated automatically, but adding
# everything seems to be easier.
Requires:       aether-api
Requires:       aether-connector-basic
Requires:       aether-impl
Requires:       aether-spi
Requires:       aether-transport-wagon
Requires:       aether-util
Requires:       aopalliance
Requires:       apache-commons-cli
Requires:       apache-commons-io
Requires:       apache-commons-lang
Requires:       apache-commons-lang3
Requires:       apache-commons-codec
Requires:       apache-commons-logging
Requires:       atinject
Requires:       google-guice
Requires:       guava
Requires:       httpcomponents-client
Requires:       httpcomponents-core
Requires:       jsoup
Requires:       jsr-305
Requires:       maven-wagon-file
Requires:       maven-wagon-http
Requires:       maven-wagon-http-shared
Requires:       maven-wagon-provider-api
Requires:       objectweb-asm
Requires:       plexus-cipher
Requires:       plexus-classworlds
Requires:       plexus-containers-component-annotations
Requires:       plexus-interpolation
Requires:       plexus-sec-dispatcher
Requires:       plexus-utils
Requires:       sisu-inject
Requires:       sisu-plexus
Requires:       slf4j

# Temporary fix for broken sisu
Requires:       cdi-api
BuildRequires:  cdi-api
# maven-filesystem
Requires: maven-filesystem
BuildArch: noarch
Source44: import.info


%description
Maven is a software project management and comprehension tool. Based on the
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

%package        lib
Summary:        Core part of Maven
Group:          Development/Java
# If XMvn is part of the same RPM transaction then it should be
# installed first to avoid triggering rhbz#1014355.

%description    lib
Core part of Apache Maven that can be used as a library.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n apache-%{name}-%{version}%{?ver_add}
%patch0 -p1

# not really used during build, but a precaution
rm maven-ant-tasks-*.jar

# Use Eclipse Sisu plugin
sed -i s/org.sonatype.plugins/org.eclipse.sisu/ maven-core/pom.xml

# fix for animal-sniffer (we don't generate 1.5 signatures)
sed -i 's:check-java-1.5-compat:check-java-1.6-compat:' pom.xml

rm -f apache-maven/src/bin/*.bat
sed -i 's:\r::' apache-maven/src/conf/settings.xml

# Update shell scripts to use unversioned classworlds
sed -i -e s:'-classpath "${M2_HOME}"/boot/plexus-classworlds-\*.jar':'-classpath "${M2_HOME}"/boot/plexus-classworlds.jar':g \
        apache-maven/src/bin/mvn*

# Disable QA plugins which are not useful for us
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :apache-rat-plugin

# logback is not really needed by maven in typical use cases, so set
# its scope to provided
%pom_xpath_inject "pom:dependency[pom:artifactId='logback-classic']" "<scope>provided</scope>" maven-embedder

%mvn_package :apache-maven __noinstall


%build
# Put all JARs in standard location, but create symlinks in Maven lib
# directory so that Plexus Classworlds can find them.
%mvn_file ":{*}:jar:" %{name}/@1 %{_datadir}/%{name}/lib/@1

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

mkdir m2home
(cd m2home
    tar --delay-directory-restore -xvf ../apache-maven/target/*tar.gz
    chmod -R +rwX apache-%{name}-%{version}%{?ver_add}
    chmod -x apache-%{name}-%{version}%{?ver_add}/conf/settings.xml
)


%install
%mvn_install

export M2_HOME=$(pwd)/m2home/apache-maven-%{version}%{?ver_add}

install -d -m 755 %{buildroot}%{_datadir}/%{name}/bin
install -d -m 755 %{buildroot}%{_datadir}/%{name}/conf
install -d -m 755 %{buildroot}%{_datadir}/%{name}/boot
install -d -m 755 %{buildroot}%{_datadir}/%{name}/lib/ext
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m 755 %{buildroot}%{_datadir}/bash-completion/completions
install -d -m 755 %{buildroot}%{_mandir}/man1

for cmd in mvnDebug mvnyjp; do
    sed s/@@CMD@@/$cmd/ %{SOURCE200} >%{buildroot}%{_bindir}/$cmd
    echo ".so man1/mvn.1" >%{buildroot}%{_mandir}/man1/$cmd.1
done
sed s/@@CMD@@/mvn/ %{SOURCE200} >%{buildroot}%{_datadir}/%{name}/bin/mvn-script
ln -sf %{_datadir}/%{name}/bin/mvn-script %{buildroot}%{_bindir}/mvn
install -p -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/bash-completion/completions/mvn
mv $M2_HOME/bin/m2.conf %{buildroot}%{_sysconfdir}
ln -sf %{_sysconfdir}/m2.conf %{buildroot}%{_datadir}/%{name}/bin/m2.conf
mv $M2_HOME/conf/settings.xml %{buildroot}%{_sysconfdir}/%{name}
ln -sf %{_sysconfdir}/%{name}/settings.xml %{buildroot}%{_datadir}/%{name}/conf/settings.xml
mv $M2_HOME/conf/logging %{buildroot}%{_sysconfdir}/%{name}
ln -sf %{_sysconfdir}/%{name}/logging %{buildroot}%{_datadir}/%{name}/conf

cp -a $M2_HOME/bin/* %{buildroot}%{_datadir}/%{name}/bin

ln -sf $(build-classpath plexus/classworlds) \
    %{buildroot}%{_datadir}/%{name}/boot/plexus-classworlds.jar

(cd %{buildroot}%{_datadir}/%{name}/lib
    build-jar-repository -s -p . \
        aether/aether-api \
        aether/aether-connector-basic \
        aether/aether-impl \
        aether/aether-spi \
        aether/aether-transport-wagon \
        aether/aether-util \
        aopalliance \
        cdi-api \
        commons-cli \
        commons-io \
        commons-lang \
        commons-lang3 \
        guava \
        atinject \
        jsoup/jsoup \
        jsr-305 \
        org.eclipse.sisu.inject \
        org.eclipse.sisu.plexus \
        plexus/plexus-cipher \
        plexus/containers-component-annotations \
        plexus/interpolation \
        plexus/plexus-sec-dispatcher \
        plexus/utils \
        google-guice-no_aop \
        slf4j/api \
        slf4j/simple \
        maven-wagon/file \
        maven-wagon/http-shaded \
        maven-wagon/http-shared \
        maven-wagon/provider-api \
        \
        httpcomponents/httpclient \
        httpcomponents/httpcore \
        commons-logging \
        commons-codec \
        objectweb-asm/asm \
)
# maven-filesystem
rm -f %buildroot%_datadir/%{name}/repository-jni/JPP

mkdir -p $RPM_BUILD_ROOT`dirname /etc/mavenrc`
touch $RPM_BUILD_ROOT/etc/mavenrc

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/maven.conf`
touch $RPM_BUILD_ROOT/etc/java/maven.conf

%pre 
# https://bugzilla.altlinux.org/show_bug.cgi?id=27807 (upgrade from maven1)
[ -d %_datadir/maven/repository/JPP ] && rm -rf %_datadir/maven/repository/JPP ||:



%files lib -f .mfiles
%doc LICENSE NOTICE README.md
%{_datadir}/%{name}
%attr(0755,root,root) %{_datadir}/%{name}/bin/mvn-script
%dir %{_javadir}/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/logging
%config(noreplace) %{_sysconfdir}/m2.conf
%config(noreplace) %{_sysconfdir}/%{name}/settings.xml
%config(noreplace) %{_sysconfdir}/%{name}/logging/simplelogger.properties

%files
%attr(0755,root,root) %{_bindir}/mvn*
%{_datadir}/bash-completion/completions/mvn
%{_mandir}/man1/mvn*.1*
%config(noreplace,missingok) /etc/mavenrc
%config(noreplace,missingok) /etc/java/maven.conf

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
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

