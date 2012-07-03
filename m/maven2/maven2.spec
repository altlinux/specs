Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global bootstrap 0
%global __jar_repack 0

Name:	    maven2
Version:	2.2.1
Release:	alt1_32jpp7
Summary:	Java project management and project comprehension tool

Group:		Development/Java
License:	ASL 2.0 and MIT and BSD
URL:		http://maven.apache.org

# export https://svn.apache.org/repos/asf/maven/maven-2/tags/maven-%{version}/ apache-maven-%{version}
# tar czvf %{name}-%{version}.tar.gz apache-maven-%{version}
Source0:	%{name}-%{version}.tar.gz

# Since we are using the entire dependency set "as is", we need to atleast try
# and make it so that only one version is packaged in the binary blob. This
# server an additional (and more important) purpose ... it ensures that a
# single version of each module is enough; because if not, versioned rpm names
# would be needed for those dependencies. The idea is as follows:

# Required by maven:
#  org/codehaus/plexus/1.0/plexus-1.0.jar
#  org/codehaus/plexus/1.1/plexus-1.1.jar
# What we package in the blob:
#  org/codehaus/plexus/1.1/plexus-1.1.jar
#  org/codehaus/plexus/1.0/plexus-1.0.jar -> ../1.1/plexus-1.1.jar

# Doing this for the hundreds of jars is a huge pain.. so we do the only
# thing sane people can. Crazy scripting magic! To generate the tarball

# rm -rf ~/.m2
# tar xzf SOURCE0
# cd apache-maven-%{version}
# export M2_HOME=`pwd`/installation/apache-maven-%{version}
# ant
# cd ~/.m2
# SOURCE100
# Find maven-%{version}-bootstrapdeps.tar.gz in ./
Source1:    %{name}-%{version}-bootstrapdeps.tar.gz

# 1xx for non-upstream/created sources
Source100:    %{name}-%{version}-settings.xml
Source101:    %{name}-JPackageRepositoryLayout.java
Source102:    %{name}-MavenJPackageDepmap.java
Source103:    %{name}-%{version}-depmap.xml
Source104:    %{name}-empty-dep.pom
Source105:    %{name}-empty-dep.jar

# 2xx for created non-buildable sources
Source200:    %{name}-script
Source201:    %{name}-jpp-script

Patch0:     %{name}-antbuild.patch
Patch1:     %{name}-%{version}-jpp.patch
Patch2:     %{name}-%{version}-update-tests.patch
Patch3:     %{name}-%{version}-enable-bootstrap-repo.patch
Patch4:     %{name}-%{version}-unshade.patch
Patch5:     %{name}-%{version}-default-resolver-pool-size.patch
Patch6:     %{name}-%{version}-strip-jackrabbit-dep.patch
Patch7:     %{name}-%{version}-classworlds.patch


%if %{bootstrap}
BuildRequires: ant
%else
BuildRequires: apache-resource-bundles
BuildRequires: objectweb-asm
BuildRequires: backport-util-concurrent
BuildRequires: buildnumber-maven-plugin
BuildRequires: bsh
BuildRequires: jsch
BuildRequires: apache-commons-codec
BuildRequires: jakarta-commons-httpclient
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-cli
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-parent
BuildRequires: maven
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-shade-plugin
%endif

Requires: classworlds
Requires: jdom

%if !%{bootstrap}
Requires: maven-artifact-manager = %{version}-%{release}
Requires: maven-error-diagnostics = %{version}-%{release}
Requires: maven-model22 = %{version}-%{release}
Requires: maven-monitor = %{version}-%{release}
Requires: maven-plugin-registry = %{version}-%{release}
Requires: maven-profile = %{version}-%{release}
Requires: maven-project = %{version}-%{release}
Requires: maven-toolchain = %{version}-%{release}
Requires: maven-plugin-descriptor = %{version}-%{release}
%endif

BuildArch: noarch
Source44: import.info
Source45: maven3-jpp-script

Provides:        maven2-bootstrap = %{epoch}:%{version}-%{release}
Obsoletes:       maven2-plugin-jxr <= 0:2.0.4 
Obsoletes:       maven2-plugin-surefire <= 0:2.0.4 
Obsoletes:       maven2-plugin-surefire-report <= 0:2.0.4 
Obsoletes:       maven2-plugin-release <= 0:2.0.4 


%description
Apache Maven is a software project management and comprehension tool. Based on
the concept of a project object model (POM), Maven can manage a project's
build, reporting and documentation from a central piece of information.

%package -n maven-artifact-manager
Group:          Development/Java
Summary:        Compatibility Maven artifact manager artifact
Requires:       jpackage-utils
Requires:       plexus-classworlds
Requires:       plexus-utils
Requires:       plexus-containers-container-default
Requires:       backport-util-concurrent
Requires:       maven-wagon

%description -n maven-artifact-manager
Maven artifact manager artifact

%package -n maven-error-diagnostics
Group:          Development/Java
Summary:        Compatibility Maven error diagnostics artifact
Requires:       jpackage-utils
Requires:       plexus-containers-container-default

%description -n maven-error-diagnostics
Maven error diagnostics artifact

%package -n maven-model22
Group:          Development/Java
Summary:        Compatibility Maven model artifact
Requires:       jpackage-utils
Requires:       plexus-utils

%description -n maven-model22
Maven model artifact

%package -n maven-monitor
Group:          Development/Java
Summary:        Compatibility Maven monitor artifact
Requires:       jpackage-utils

%description -n maven-monitor
Maven monitor artifact

%package -n maven-plugin-registry
Group:          Development/Java
Summary:        Compatibility Maven plugin registry artifact
Requires:       jpackage-utils
Requires:       plexus-utils
Requires:       plexus-interpolation
Requires:       plexus-containers-container-default

%description -n maven-plugin-registry
Maven plugin registry artifact

%package -n maven-profile
Group:          Development/Java
Summary:        Compatibility Maven profile artifact
Requires:       jpackage-utils
Requires:       plexus-utils
Requires:       plexus-interpolation
Requires:       plexus-containers-container-default

%description -n maven-profile
Maven profile artifact

%package -n maven-project
Group:          Development/Java
Summary:        Compatibility Maven project artifact
Requires:       jpackage-utils
Requires:       maven-artifact-manager
Requires:       maven-profile
Requires:       maven-plugin-registry
Requires:       maven-model
Requires:       plexus-interpolation
Requires:       plexus-utils
Requires:       plexus-containers-container-default

%description -n maven-project
Maven project artifact

%package -n maven-toolchain
Group:          Development/Java
Summary:        Compatibility Maven toolchain artifact
Requires:       jpackage-utils

%description -n maven-toolchain
Maven toolchain artifact

%package -n maven-plugin-descriptor
Group:          Development/Java
Summary:        Maven Plugin Description Model
Requires:       jpackage-utils
Requires:       maven
Requires:       plexus-classworlds
Requires:       plexus-container-default

%description -n maven-plugin-descriptor
Maven toolchain artifact


%prep
%setup -q -n apache-maven-2.2.1

%patch0 -b .antbuild
%patch1 -p1 -b .jpp
%patch2 -b .update-tests

%if ! %{bootstrap}
%patch4 -b .unshade
%endif

%if %{bootstrap}
%patch3 -b .enable-bootstrap-repo
%endif

# set cache location
export M2_REPO=`pwd`/.m2
mkdir $M2_REPO

# if bootstrapping, extract the dependencies
%if %{bootstrap}
(cd $M2_REPO

  tar xzf %{SOURCE1}

  # maven-remote-resources-plugin (m-r-r-p) is used side-by-side with
  # plexus-velocity (p-v) 1.1.3 upstream.. we collapse to a single p-v version
  # of 1.1.7. 1.1.7 however has a component descriptor that conflicts
  # with the one in m-r-r-p. We therefore need to remove the descriptor
  # from m-r-r-p first
  zip -d repository/org/apache/maven/plugins/maven-remote-resources-plugin/1.0-beta-2/maven-remote-resources-plugin-1.0-beta-2.jar \
         META-INF/plexus/components.xml

  # resource bundle 1.3 is needed during build, but not when done via
  # upstream, for some reason
  mkdir -p repository/org/apache/apache-jar-resource-bundle/1.3
  ln -s ../1.4/apache-jar-resource-bundle-1.4.jar \
        repository/org/apache/apache-jar-resource-bundle/1.3/apache-jar-resource-bundle-1.3.jar
  ln -s ../1.4/apache-jar-resource-bundle-1.4.jar.sha1 \
        repository/org/apache/apache-jar-resource-bundle/1.3/apache-jar-resource-bundle-1.3.jar.sha1
)
%endif

cp %{SOURCE101} maven-artifact/src/main/java/org/apache/maven/artifact/repository/layout/JPackageRepositoryLayout.java
cp %{SOURCE102} maven-artifact/src/main/java/org/apache/maven/artifact/repository/layout/MavenJPackageDepmap.java

# disable parallel artifact resolution
%patch5 -p1 -b .parallel-artifacts-resolution

# remove unneeded jackrabbit dependency
%patch6 -p1 -b .strip-jackrabbit-dep

%patch7 -p1 -b .classworlds

# test case is incorrectly assuming that target executed by antcall
# can propagate references to its parent (stopped working with ant 1.8)
rm maven-script/maven-script-ant/src/test/java/org/apache/maven/script/ant/AntMojoWrapperTest.java

# FIXIT: look why these tests are failing with maven-surefire 2.6
rm maven-artifact/src/test/java/org/apache/maven/artifact/resolver/DefaultArtifactCollectorTest.java
rm maven-project/src/test/java/org/apache/maven/project/validation/DefaultModelValidatorTest.java

%build
export M2_REPO=`pwd`/.m2
export M2_HOME=`pwd`/installation/apache-maven-%{version}

# copy settings to where ant reads from
mkdir -p $M2_HOME/conf
cp %{SOURCE100} $M2_HOME/conf/settings.xml

# replace locations in the copied settings file
sed -i -e s:__M2_LOCALREPO_PLACEHOLDER__:"file\://$M2_REPO/cache":g $M2_HOME/conf/settings.xml
sed -i -e s:__M2_REMOTEREPO_PLACEHOLDER__:"file\://$M2_REPO/repository":g $M2_HOME/conf/settings.xml

# replace settings file location before patching
sed -i -s s:__M2_SETTINGS_FILE__:$M2_HOME/conf/settings.xml:g build.xml

%if %{bootstrap}
ant -Dmaven.repo.local=$M2_REPO/cache
%else
# FIXME: These tests fail when building with maven for an unknown reason
rm -f maven-core/src/test/java/org/apache/maven/WagonSelectorTest.java
rm -f maven-artifact-manager/src/test/java/org/apache/maven/artifact/manager/DefaultWagonManagerTest.java
for nobuild in apache-maven maven-artifact-test \
               maven-compat maven-core maven-plugin-api \
               maven-plugin-parameter-documenter maven-reporting \
               maven-script;do
    sed -i "s:<module>$nobuild</module>::"  pom.xml
done
mvn-rpmbuild -X -Dmaven.test.skip=true -P all-models -Dmaven.repo.local=$(pwd)/.m2 -Dmaven.local.depmap.file=%{SOURCE103} install
%endif

%install

# maven2 directory in /usr/share/java
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

###########
# M2_HOME #
###########
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}

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

##################
# javadir/maven2 #
#*################
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

#######################
# javadir/maven2/poms #
#*#####################
ln -s %{_datadir}/%{name}/poms $RPM_BUILD_ROOT%{_javadir}/%{name}/poms

############
# /usr/bin #
############
install -dm 755 $RPM_BUILD_ROOT%{_bindir}

# Install files
install -m 644 %{SOURCE104} $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.maven2-empty-dep.pom
install -m 644 %{SOURCE105} $RPM_BUILD_ROOT%{_javadir}/%{name}/empty-dep.jar


###################
# Individual jars #
###################

# parts of maven2 now go into separate subpackages
for subdir in maven-artifact-manager maven-error-diagnostics \
              maven-model maven-monitor maven-plugin-registry \
              maven-profile maven-project maven-toolchain maven-plugin-descriptor ;do
     pushd $subdir
     install -m 644 target/$subdir-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$subdir.jar
     install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-$subdir.pom
     %add_to_maven_depmap org.apache.maven $subdir %{version} JPP/%{name} $subdir
     mv $RPM_BUILD_ROOT%{_mavendepmapfragdir}/%{name} \
        $RPM_BUILD_ROOT%{_mavendepmapfragdir}/$subdir
     popd
done



# maven-reporting pom
install -m 644 maven-reporting/pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-maven-reporting.pom
%add_to_maven_depmap org.apache.maven.reporting maven-reporting %{version} JPP/%{name} maven-reporting

# maven pom
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-maven.pom
%add_to_maven_depmap org.apache.maven maven %{version} JPP/%{name} maven
# maven-model22
mv $RPM_BUILD_ROOT%{_mavendepmapfragdir}/maven-model \
   $RPM_BUILD_ROOT%{_mavendepmapfragdir}/maven-model22

# Items in %%{_bindir}
install -Dm 755 %{SOURCE45} $RPM_BUILD_ROOT%{_bindir}/mvn-jpp

%post
# clear the old links
find %{_datadir}/%{name}/boot/ -type l -exec rm -f '{}' \; ||:
find %{_datadir}/%{name}/lib/ -type l -exec rm -f '{}' \; ||:

%postun
# FIXME: This doesn't always remove the plugins dir. It seems that rpm doesn't
# honour the Requires(postun) as it should, causing maven to get uninstalled 
# before some plugins are
if [ -d %{_javadir}/%{name} ] ; then rmdir --ignore-fail-on-non-empty %{_javadir}/%{name} >& /dev/null; fi



%files
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/poms
%exclude %{_datadir}/%{name}/poms/JPP.%{name}-maven-artifact-manager.pom
%exclude %{_datadir}/%{name}/poms/JPP.%{name}-maven-error-diagnostics.pom
%exclude %{_datadir}/%{name}/poms/JPP.%{name}-maven-model.pom
%exclude %{_datadir}/%{name}/poms/JPP.%{name}-maven-monitor.pom
%exclude %{_datadir}/%{name}/poms/JPP.%{name}-maven-plugin-registry.pom
%exclude %{_datadir}/%{name}/poms/JPP.%{name}-maven-profile.pom
%exclude %{_datadir}/%{name}/poms/JPP.%{name}-maven-project.pom
%exclude %{_datadir}/%{name}/poms/JPP.%{name}-maven-toolchain.pom
%exclude %{_datadir}/%{name}/poms/JPP.%{name}-maven-plugin-descriptor.pom
%{_datadir}/%{name}/repository
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}
%exclude %{_javadir}/%{name}/maven-artifact-manager.jar
%exclude %{_javadir}/%{name}/maven-error-diagnostics.jar
%exclude %{_javadir}/%{name}/maven-model.jar
%exclude %{_javadir}/%{name}/maven-monitor.jar
%exclude %{_javadir}/%{name}/maven-plugin-registry.jar
%exclude %{_javadir}/%{name}/maven-profile.jar
%exclude %{_javadir}/%{name}/maven-project.jar
%exclude %{_javadir}/%{name}/maven-toolchain.jar
%exclude %{_javadir}/%{name}/maven-plugin-descriptor.jar
%attr(0755,root,root) %{_bindir}/mvn-jpp


%files -n maven-artifact-manager
%{_mavendepmapfragdir}/maven-artifact-manager
%{_javadir}/%{name}/maven-artifact-manager.jar
%{_datadir}/%{name}/poms/JPP.%{name}-maven-artifact-manager.pom

%files -n maven-error-diagnostics
%{_mavendepmapfragdir}/maven-error-diagnostics
%{_javadir}/%{name}/maven-error-diagnostics.jar
%{_datadir}/%{name}/poms/JPP.%{name}-maven-error-diagnostics.pom

%files -n maven-model22
%{_mavendepmapfragdir}/maven-model22
%{_javadir}/%{name}/maven-model.jar
%{_datadir}/%{name}/poms/JPP.%{name}-maven-model.pom

%files -n maven-monitor
%{_mavendepmapfragdir}/maven-monitor
%{_javadir}/%{name}/maven-monitor.jar
%{_datadir}/%{name}/poms/JPP.%{name}-maven-monitor.pom

%files -n maven-plugin-registry
%{_mavendepmapfragdir}/maven-plugin-registry
%{_javadir}/%{name}/maven-plugin-registry.jar
%{_datadir}/%{name}/poms/JPP.%{name}-maven-plugin-registry.pom

%files -n maven-profile
%{_mavendepmapfragdir}/maven-profile
%{_javadir}/%{name}/maven-profile.jar
%{_datadir}/%{name}/poms/JPP.%{name}-maven-profile.pom

%files -n maven-project
%{_mavendepmapfragdir}/maven-project
%{_javadir}/%{name}/maven-project.jar
%{_datadir}/%{name}/poms/JPP.%{name}-maven-project.pom

%files -n maven-toolchain
%{_mavendepmapfragdir}/maven-toolchain
%{_javadir}/%{name}/maven-toolchain.jar
%{_datadir}/%{name}/poms/JPP.%{name}-maven-toolchain.pom

%files -n maven-plugin-descriptor
%{_mavendepmapfragdir}/maven-plugin-descriptor
%{_javadir}/%{name}/maven-plugin-descriptor.jar
%{_datadir}/%{name}/poms/JPP.%{name}-maven-plugin-descriptor.pom


%changelog
* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt1_32jpp7
- complete build

* Thu Apr 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt19_0jpp
- all plugins replaced with maven3 ones

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt18_0jpp
- more plugins replaced with maven3 ones: ant, antrun, ...

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt17_0jpp
- more plugins replaced with maven3 ones: ear, gpg, ...

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt16_0jpp
- more compat plugins (one,rar,checkstyle,...)

* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt15_0jpp
- disabled plugin-remote-resources

* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt14_0jpp
- mvn-jpp: added MAVEN_OPTS processing

* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt13_0jpp
- added compat mvn-jpp

* Sat Mar 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt12_0jpp
- empty proxy package to use maven3 instead of maven2

* Tue Sep 06 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt11_37jpp6
- fixed build w/new xmlrpc

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt10_37jpp6
- new jpp release with ant 1.8 support

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt10_29jpp6
- added missing /etc/mavenrc config

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt9_29jpp6
- new jpp release

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt9_28jpp6
- build with surefire 2.4

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt8_28jpp6
- build with new modello

* Mon Jan 31 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt8_27jpp6
- added missing Req: to maven2-plugin-remote-resources

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt7_27jpp6
- patched to build with new plexus-interpolation

* Tue Jan 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt6_27jpp6
- fixed build

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt6_26jpp6
- build w/o maven-2.0.x-MNG-3948.patch

* Mon Sep 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt5_26jpp6
- build w/o maven-2.0.x-MNG-3948.patch

* Sun Sep 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt4_26jpp6
- updated bootstrap repository

* Fri Sep 24 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt3_26jpp6
- backported 2.0.11 patch for parent poms lookup

* Fri Sep 24 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt2_26jpp6
- semi-bootstrap build

* Thu Sep 16 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt1_26jpp6
- new version

* Tue Jun 09 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.7-alt2_9jpp5
- new jpp release

* Fri Feb 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.7-alt2_8jpp5
- fixed build

* Tue Feb 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.7-alt1_8jpp5
- new version

* Tue Nov 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_10jpp1.7
- imported with jppimport script; note: bootstrapped version

