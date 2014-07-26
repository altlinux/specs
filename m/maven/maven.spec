Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
%global debug_package %{nil}

Name:           maven
Version:        3.0.4
Release:        alt6_21.3jpp7
Summary:        Java project management and project comprehension tool

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/
# Source URL is for testing only, final version will be in different place:
# http://www.apache.org/dyn/closer.cgi/maven/source/apache-%{name}-%{version}-src.tar.gz
Source0:        http://www.apache.org/dist//maven/source/apache-%{name}-%{version}-src.tar.gz
Source1:        maven-bash-completion
Source2:        mvn.1

# custom resolver java files
# source: git clone git://fedorapeople.org/~sochotni/maven-javadir-resolver/
Source100:      JavadirWorkspaceReader.java
Source101:      MavenJPackageDepmap.java

# empty files for resolving to nothing
Source104:    %{name}-empty-dep.pom
Source105:    %{name}-empty-dep.jar

# 2xx for created non-buildable sources
Source200:    %{name}-script
Source201:    %{name}-script-local
Source202:    %{name}-script-rpmbuild

# Other included files
Source250:    repo-metadata.tar.xz

# Patch1XX could be upstreamed probably
Patch100:       0005-Use-generics-in-modello-generated-code.patch
Patch101:       0006-Make-compiler-plugin-default-to-source-1.5.patch

# Patch15X are already upstream
Patch150:         0001-Add-plugin-api-deps.patch
Patch151:         0003-Use-utf-8-source-encoding.patch
# Patch2XX for non-upstreamable patches
Patch200:       0002-Use-custom-resolver.patch
Patch201:       0004-Fix-text-scope-skipping-with-maven.test.skip.patch

BuildArch:      noarch

BuildRequires:  aether >= 1.13.1
BuildRequires:  aopalliance
BuildRequires:  apache-commons-parent
BuildRequires:  async-http-client
BuildRequires:  atinject
BuildRequires:  buildnumber-maven-plugin
BuildRequires:  cglib
BuildRequires:  google-guice >= 3.0
BuildRequires:  hamcrest
BuildRequires:  maven
BuildRequires:  maven2-common-poms
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-parent
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  mojo-parent
BuildRequires:  objectweb-asm
BuildRequires:  plexus-containers-component-metadata >= 1.5.5
BuildRequires:  plexus-containers-container-default
BuildRequires:  sisu >= 2.1.1-2
BuildRequires:  slf4j
BuildRequires:  sonatype-oss-parent
BuildRequires:  xmlunit
%if 0%{?fedora}
BuildRequires:  animal-sniffer >= 1.6-5
%endif

Requires:       aether >= 1.13.1
Requires:       apache-commons-cli
Requires:       apache-commons-parent
Requires:       async-http-client
Requires:       atinject
Requires:       google-guice >= 3.0
Requires:       guava
Requires:       hamcrest
Requires:       hamcrest
Requires:       maven2-common-poms
Requires:       maven-parent
Requires:       maven-wagon
Requires:       mojo-parent
Requires:       nekohtml
Requires:       plexus-cipher
Requires:       plexus-classworlds >= 2.4
Requires:       plexus-containers-component-annotations
Requires:       plexus-containers-container-default
Requires:       plexus-interpolation
Requires:       plexus-sec-dispatcher
Requires:       plexus-utils
Requires:       sisu >= 2.1.1-2
Requires:       sonatype-oss-parent
Requires:       tar
Requires:       xbean
Requires:       xerces-j2
%if 0%{?fedora}
Requires:       animal-sniffer >= 1.6-5
%endif


# for noarch->arch change
Obsoletes:      %{name} < 0:%{version}-%{release}

# maven2 bin package no longer exists. Replace it
# these should be around until F20
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
Requires:       jpackage-utils
BuildArch:      noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n apache-%{name}-%{version}%{?ver_add}
%patch150 -p1
%patch151 -p1
%patch200 -p1
%patch201 -p1
%patch100 -p1
%patch101 -p1

# get custom resolver in place
mkdir -p maven-aether-provider/src/main/java/org/apache/maven/artifact/resolver \
         maven-aether-provider/src/main/java/org/apache/maven/artifact/repository

cp %{SOURCE100} maven-aether-provider/src/main/java/org/apache/maven/artifact/resolver
cp %{SOURCE101} maven-aether-provider/src/main/java/org/apache/maven/artifact/repository

# by adding our things this has become compile dep
sed -i 's:<scope>runtime</scope>::' maven-core/pom.xml

# not really used during build, but a precaution
rm maven-ant-tasks-*.jar

# fix line endings
sed -i 's:\r::' *.txt

# fix for animal-sniffer (we don't generate 1.5 signatures)
sed -i 's:check-java-1.5-compat:check-java-1.6-compat:' pom.xml

pushd apache-maven
rm src/bin/*bat
sed -i 's:\r::' src/conf/settings.xml

# Update shell scripts to use unversioned classworlds
sed -i -e s:'-classpath "${M2_HOME}"/boot/plexus-classworlds-\*.jar':'-classpath "${M2_HOME}"/boot/plexus-classworlds.jar':g \
        src/bin/mvn*
popd

# Disable animal-sniffer on RHEL
# Temporarily disabled for fedora to solve asm & asm4 clashing on classpath
#if [ %{?rhel} ]; then
%pom_remove_plugin :animal-sniffer-maven-plugin
#fi

%pom_add_dep aopalliance:aopalliance:any:test maven-model-builder
%pom_add_dep cglib:cglib:any:test maven-model-builder

%build
mvn-rpmbuild -e install javadoc:aggregate

mkdir m2home
(cd m2home
tar --delay-directory-restore -xvf ../apache-maven/target/*tar.gz
chmod -R +rwX apache-%{name}-%{version}%{?ver_add}
chmod -x apache-%{name}-%{version}%{?ver_add}/conf/settings.xml
)


%install
export M2_HOME=$(pwd)/m2home/apache-maven-%{version}%{?ver_add}

# maven2 directory in /usr/share/java
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

# put global m2 config into /etc and symlink it later
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}
mv $M2_HOME/bin/m2.conf $RPM_BUILD_ROOT%{_sysconfdir}/

###########
# M2_HOME #
###########
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}

#################
# Repo metadata #
#################
install -m 755 %{SOURCE250} $RPM_BUILD_ROOT%{_datadir}/%{name}/


###############
# M2_HOME/bin #
###############
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
cp -a $M2_HOME/bin/* $RPM_BUILD_ROOT%{_datadir}/%{name}/bin

ln -sf %{_sysconfdir}/m2.conf $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/m2.conf


################
# M2_HOME/boot #
################
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/boot

# this dangling symlink will be filled in by Requires
(cd $RPM_BUILD_ROOT%{_datadir}/%{name}/boot
  ln -sf `build-classpath plexus/classworlds` plexus-classworlds.jar
)


################
# M2_HOME/conf #
################
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/conf
cp -a $M2_HOME/conf/* $RPM_BUILD_ROOT%{_datadir}/%{name}/conf/

###############
# M2_HOME/lib #
###############
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/lib

# jdom is needed for our custom resolving code only
(cd $RPM_BUILD_ROOT%{_datadir}/%{name}/lib

  build-jar-repository -s -p . aether/api aether/connector-wagon aether/impl aether/spi aether/util \
                               commons-cli guava google-guice nekohtml plexus/plexus-cipher \
                               plexus/containers-component-annotations  \
                               plexus/interpolation plexus/plexus-sec-dispatcher plexus/utils \
                               sisu/sisu-inject-bean sisu/sisu-inject-plexus maven-wagon/file \
                               maven-wagon/http-lightweight maven-wagon/http-shared maven-wagon/provider-api \
                               xbean/xbean-reflect xerces-j2 atinject aopalliance cglib \
                               slf4j/api slf4j/nop objectweb-asm
  # dependency of our resolver
  mkdir ext/
  build-jar-repository -s -p ext/ xml-commons-apis
)

################
# M2_HOME/poms #
#*##############
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/poms

########################
# /etc/maven/fragments #
########################
install -dm 755 $RPM_BUILD_ROOT/%{_sysconfdir}/maven/fragments

##############################
# /usr/share/java repository #
##############################
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/repository
ln -s %{_javadir} $RPM_BUILD_ROOT%{_datadir}/%{name}/repository/JPP

##############################
# /usr/share/java-jni repository #
##############################
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/repository-java-jni
ln -s %{_javajnidir} $RPM_BUILD_ROOT%{_datadir}/%{name}/repository-java-jni/JPP

##############################
# _libdir/java repository #
##############################
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/repository-jni
# create symlink in post, remove in preun so we can stay noarch

##################
# javadir/maven #
#*################
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

#######################
# javadir/maven/poms #
#*#####################
ln -s %{_datadir}/%{name}/poms $RPM_BUILD_ROOT%{_javadir}/%{name}/poms

# for our custom resolver to remove dependencies we need empty jar and
# pom file
install -m 644 %{SOURCE104} $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.maven-empty-dep.pom
install -m 644 %{SOURCE105} $RPM_BUILD_ROOT%{_javadir}/%{name}/empty-dep.jar

############
# /usr/bin #
############
install -dm 755 $RPM_BUILD_ROOT%{_bindir}

# Wrappers
cp -af %{SOURCE200} $RPM_BUILD_ROOT%{_bindir}/mvn
cp -af %{SOURCE201} $RPM_BUILD_ROOT%{_bindir}/mvn-local
cp -af %{SOURCE202} $RPM_BUILD_ROOT%{_bindir}/mvn-rpmbuild

###################
# Individual jars #
###################

for module in maven-aether-provider maven-artifact maven-compat \
              maven-core maven-embedder maven-model \
              maven-model-builder maven-plugin-api \
              maven-repository-metadata  maven-settings \
              maven-settings-builder;do

    pushd $module
    install -m 644 target/$module-%{version}%{?ver_add}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$module.jar
    ln -s %{_javadir}/%{name}/$module.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/$module.jar
    install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-$module.pom
    %add_to_maven_depmap org.apache.maven $module %{version} JPP/%{name} $module
    popd
done

# maven pom
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-maven.pom
%add_to_maven_depmap org.apache.maven maven %{version} JPP/%{name} maven

# javadocs
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Install bash-completion
install -Dm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}

# Manual page
install -dm 755 $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1
gzip -9 $RPM_BUILD_ROOT%{_mandir}/man1/*
# maven-filesystem
rm -f %buildroot%_datadir/%{name}/repository-jni/JPP

mkdir -p $RPM_BUILD_ROOT`dirname /etc/mavenrc`
touch $RPM_BUILD_ROOT/etc/mavenrc

%pre 
# https://bugzilla.altlinux.org/show_bug.cgi?id=27807 (upgrade from maven1)
[ -d %_datadir/maven/repository/JPP ] && rm -rf %_datadir/maven/repository/JPP ||:


%files
%doc LICENSE.txt NOTICE.txt README.txt
%attr(0755,root,root) %{_bindir}/mvn
%attr(0755,root,root) %{_bindir}/mvn-local
%attr(0755,root,root) %{_bindir}/mvn-rpmbuild
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%attr(0755,root,root) %{_datadir}/%{name}/bin/mvn
%attr(0755,root,root) %{_datadir}/%{name}/bin/mvnyjp
%attr(0755,root,root) %{_datadir}/%{name}/bin/mvnDebug
%{_datadir}/%{name}/bin/*.conf
%config(noreplace) %{_sysconfdir}/m2.conf
%{_datadir}/%{name}/boot
%{_datadir}/%{name}/conf
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/poms
%{_datadir}/%{name}/repository
%{_datadir}/%{name}/repository-jni
%{_datadir}/%{name}/repository-java-jni
%config %{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}
%{_datadir}/%{name}/repo-metadata.tar.xz
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%{_mandir}/man1/mvn.1*
%config(noreplace,missingok) /etc/mavenrc

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}


%changelog
* Sat Jul 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt6_21.3jpp7
- update

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt5_21jpp7
- non-bootstrap build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

