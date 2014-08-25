Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
%global debug_package %{nil}

Name:           maven
Version:        3.0.5
Release:        alt1_3jpp7
Summary:        Java project management and project comprehension tool

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/
Source0:        http://archive.apache.org/dist/%{name}/%{name}-3/%{version}/source/apache-%{name}-%{version}-src.tar.gz
Source1:        maven-bash-completion
Source2:        mvn.1

# 2xx for created non-buildable sources
Source200:      %{name}-script

# Patch1XX could be upstreamed probably
Patch100:       0005-Use-generics-in-modello-generated-code.patch

BuildArch:      noarch

BuildRequires:  aether >= 1.13.1
BuildRequires:  aopalliance
BuildRequires: apache-resource-bundles apache-jar-resource-bundle
BuildRequires:  async-http-client
BuildRequires:  atinject
BuildRequires:  buildnumber-maven-plugin
BuildRequires:  cglib
BuildRequires:  google-guice >= 3.0
BuildRequires:  hamcrest
BuildRequires:  maven-local
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  objectweb-asm
BuildRequires:  plexus-containers-component-metadata >= 1.5.5
BuildRequires:  plexus-containers-container-default
BuildRequires:  sisu-inject-bean
BuildRequires:  sisu-inject-plexus
BuildRequires:  slf4j
BuildRequires:  xmlunit
%if 0%{?fedora}
BuildRequires:  animal-sniffer >= 1.6-5
%endif

# for noarch->arch change
Obsoletes:      %{name} < 0:%{version}-%{release}

# maven2 bin package no longer exists.
Obsoletes:      maven2 < 2.2.1-99
Provides:       maven2 = %{version}-%{release}
# maven-filesystem
Requires: maven-filesystem
BuildArch: noarch
Source44: import.info


%description
Maven is a software project management and comprehension tool. Based on the
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n apache-%{name}-%{version}%{?ver_add}
%patch100 -p1

# not really used during build, but a precaution
rm maven-ant-tasks-*.jar

# fix line endings
sed -i 's:\r::' *.txt

# fix for animal-sniffer (we don't generate 1.5 signatures)
sed -i 's:check-java-1.5-compat:check-java-1.6-compat:' pom.xml

rm -f apache-maven/src/bin/*.bat
sed -i 's:\r::' apache-maven/src/conf/settings.xml

# Update shell scripts to use unversioned classworlds
sed -i -e s:'-classpath "${M2_HOME}"/boot/plexus-classworlds-\*.jar':'-classpath "${M2_HOME}"/boot/plexus-classworlds.jar':g \
        apache-maven/src/bin/mvn*

# Disable animal-sniffer on RHEL
# Temporarily disabled for fedora to solve asm & asm4 clashing on classpath
#if [ %{?rhel} ]; then
%pom_remove_plugin :animal-sniffer-maven-plugin
#fi

%pom_add_dep org.codehaus.plexus:plexus-container-default maven-plugin-api
# Test dependencies
%pom_add_dep aopalliance:aopalliance:any:test maven-model-builder
%pom_add_dep cglib:cglib:any:test maven-model-builder

%build
# Put all JARs in standard location, but create symlinks in Maven lib
# directory so that Plexus Classworlds can find them.
%mvn_file ":{*}" %{name}/@1 %{_datadir}/%{name}/lib/@1

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
install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d
install -d -m 755 %{buildroot}%{_mandir}/man1

install -p -m 755 %{SOURCE200} %{buildroot}%{_bindir}/mvn
install -p -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}
mv $M2_HOME/bin/m2.conf %{buildroot}%{_sysconfdir}
ln -sf %{_sysconfdir}/m2.conf %{buildroot}%{_datadir}/%{name}/bin/m2.conf
mv $M2_HOME/conf/settings.xml %{buildroot}%{_sysconfdir}/%{name}
ln -sf %{_sysconfdir}/%{name}/settings.xml %{buildroot}%{_datadir}/%{name}/conf/settings.xml

cp -a $M2_HOME/bin/* %{buildroot}%{_datadir}/%{name}/bin

ln -sf $(build-classpath plexus/classworlds) \
    %{buildroot}%{_datadir}/%{name}/boot/plexus-classworlds.jar

(cd %{buildroot}%{_datadir}/%{name}/lib
    build-jar-repository -s -p . \
        aether/api \
        aether/connector-wagon \
        aether/impl \
        aether/spi \
        aether/util \
        aopalliance \
        atinject \
        cglib \
        commons-cli \
        google-guice \
        guava \
        maven-wagon/file \
        maven-wagon/http-lightweight \
        maven-wagon/http-shared \
        maven-wagon/provider-api \
        nekohtml \
        objectweb-asm \
        plexus/containers-component-annotations \
        plexus/interpolation \
        plexus/plexus-cipher \
        plexus/plexus-sec-dispatcher \
        plexus/utils \
        sisu/sisu-inject-bean \
        sisu/sisu-inject-plexus \
        slf4j/api \
        slf4j/nop \
        xbean/xbean-reflect \
)
# maven-filesystem
rm -f %buildroot%_datadir/%{name}/repository-jni/JPP

mkdir -p $RPM_BUILD_ROOT`dirname /etc/mavenrc`
touch $RPM_BUILD_ROOT/etc/mavenrc

%pre 
# https://bugzilla.altlinux.org/show_bug.cgi?id=27807 (upgrade from maven1)
[ -d %_datadir/maven/repository/JPP ] && rm -rf %_datadir/maven/repository/JPP ||:



%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.txt
%{_datadir}/%{name}
%{_bindir}/mvn
%dir %{_javadir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/m2.conf
%config(noreplace) %{_sysconfdir}/%{name}/settings.xml
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%{_mandir}/man1/mvn.1*
%config(noreplace,missingok) /etc/mavenrc

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.5-alt1_3jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.5-alt0.2jpp
- rebuild to add provides

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

