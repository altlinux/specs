Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global bootstrap 0
%global __jar_repack 0

%global main_pkg maven

Name:	    maven2
Version:	2.2.1
Release:	alt4_37jpp7
Summary:	Java project management and project comprehension tool

Group:		Development/Java
License:	ASL 2.0 and MIT and BSD
URL:		http://maven.apache.org

# export https://svn.apache.org/repos/asf/maven/maven-2/tags/maven-%{version}/ apache-maven-%{version}
# tar czvf %{name}-%{version}.tar.gz apache-maven-%{version}
Source0:	%{name}-%{version}.tar.gz


# 1xx for non-upstream/created sources
Source100:    %{name}-%{version}-settings.xml
Source103:    %{name}-%{version}-depmap.xml

Patch0:     %{name}-antbuild.patch
Patch2:     %{name}-%{version}-update-tests.patch
Patch3:     %{name}-%{version}-enable-bootstrap-repo.patch
Patch4:     %{name}-%{version}-unshade.patch
Patch5:     %{name}-%{version}-default-resolver-pool-size.patch
Patch6:     %{name}-%{version}-strip-jackrabbit-dep.patch
Patch7:     %{name}-%{version}-classworlds.patch


%if %{bootstrap}
BuildRequires: ant
%else
BuildRequires: apache-resource-bundles apache-jar-resource-bundle
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


BuildArch: noarch
Source44: import.info

Obsoletes:       maven2-plugin-jxr <= 0:2.0.4 
Obsoletes:       maven2-plugin-surefire <= 0:2.0.4 
Obsoletes:       maven2-plugin-surefire-report <= 0:2.0.4 
Obsoletes:       maven2-plugin-release <= 0:2.0.4 
Source45: maven3-jpp-script


%description
Apache Maven is a software project management and comprehension tool. Based on
the concept of a project object model (POM), Maven can manage a project's
build, reporting and documentation from a central piece of information.

%package -n maven-artifact
Group:          Development/Java
Summary:        Compatibility Maven artifact artifact
Requires:       jpackage-utils
Requires:       plexus-utils
Requires:       plexus-containers-container-default

%description -n maven-artifact
Maven artifact manager artifact

%package -n maven-artifact-manager
Group:          Development/Java
Summary:        Compatibility Maven artifact manager artifact
Requires:       jpackage-utils
Requires:       plexus-classworlds
Requires:       plexus-utils
Requires:       plexus-containers-container-default
Requires:       backport-util-concurrent
Requires:       maven-artifact = %{?epoch:%epoch:}%{version}-%{release}
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

%package -n maven-model
Group:          Development/Java
Summary:        Compatibility Maven model artifact
Requires:       jpackage-utils
Requires:       plexus-utils
# it was a tmp package during migration
Obsoletes:       maven-model22 < 0:%{version}-%{release}

%description -n maven-model
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
Requires:       plexus-containers-container-default

%description -n maven-plugin-registry
Maven plugin registry artifact

%package -n maven-profile
Group:          Development/Java
Summary:        Compatibility Maven profile artifact
Requires:       jpackage-utils
Requires:       maven-model = %{?epoch:%epoch:}%{version}-%{release}
Requires:       plexus-utils
Requires:       plexus-interpolation
Requires:       plexus-containers-container-default

%description -n maven-profile
Maven profile artifact

%package -n maven-project
Group:          Development/Java
Summary:        Compatibility Maven project artifact
Requires:       jpackage-utils
Requires:       maven-artifact-manager = %{?epoch:%epoch:}%{version}-%{release}
Requires:       maven-profile = %{?epoch:%epoch:}%{version}-%{release}
Requires:       maven-plugin-registry = %{?epoch:%epoch:}%{version}-%{release}
Requires:       maven-model = %{?epoch:%epoch:}%{version}-%{release}
Requires:       maven-settings = %{?epoch:%epoch:}%{version}-%{release}
Requires:       plexus-interpolation
Requires:       plexus-utils
Requires:       plexus-containers-container-default

%description -n maven-project
Maven project artifact

%package -n maven-settings
Group:          Development/Java
Summary:        Compatibility Maven settings artifact
Requires:       jpackage-utils
Requires:       maven-model = %{?epoch:%epoch:}%{version}-%{release}
Requires:       plexus-interpolation
Requires:       plexus-utils
Requires:       plexus-containers-container-default

%description -n maven-settings
Maven settings artifact

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

# disable parallel artifact resolution
%patch5 -p1 -b .parallel-artifacts-resolution

# remove unneeded jackrabbit dependency
%patch6 -p1 -b .strip-jackrabbit-dep

%patch7 -p1 -b .classworlds

for nobuild in apache-maven maven-artifact-test \
               maven-compat maven-core maven-plugin-api \
               maven-plugin-parameter-documenter maven-reporting \
               maven-script;do
    %pom_disable_module $nobuild
done

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
mvn-rpmbuild -X -Dmaven.local.debug=true -Dmaven.test.skip=true -P all-models -Dmaven.repo.local=$(pwd)/.m2 -Dmaven.local.depmap.file=%{SOURCE103} install
%endif

%install

# maven2 directory in /usr/share/java
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{main_pkg}
install -dm 755 $RPM_BUILD_ROOT%{_mavenpomdir}


# parts of maven2 now go into separate subpackages
for subdir in maven-artifact-manager maven-error-diagnostics \
              maven-monitor maven-plugin-registry \
              maven-profile maven-project maven-toolchain maven-plugin-descriptor ;do
     pushd $subdir
     install -m 644 target/$subdir-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{main_pkg}/$subdir.jar
     install -m 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{main_pkg}-$subdir.pom
     %add_maven_depmap JPP.%{main_pkg}-$subdir.pom %{main_pkg}/$subdir.jar -f $subdir
     popd
done

# these parts are compatibility versions which are available in
# maven-3.x as well. We default to maven-3, but if someone asks for
# 2.x we provide few compat versions
for subdir in \
  maven-artifact \
  maven-model \
  maven-settings;
do
     pushd $subdir
     install -m 644 target/$subdir-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{main_pkg}/$subdir.jar
     install -m 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{main_pkg}-$subdir.pom
     %add_maven_depmap JPP.%{main_pkg}-$subdir.pom %{main_pkg}/$subdir.jar -f $subdir -v "2.0.2,2.0.6,2.0.7,2.0.8"
     popd
done

# Items in %%{_bindir}
install -Dm 755 %{SOURCE45} $RPM_BUILD_ROOT%{_bindir}/mvn-jpp

%post
# clear the old links
[ -d %{_datadir}/%{name}/boot/ ] && find %{_datadir}/%{name}/boot/ -type l -exec rm -f '{}' \; ||:
[ -d %{_datadir}/%{name}/lib/ ] && find %{_datadir}/%{name}/lib/ -type l -exec rm -f '{}' \; ||:

%postun
# FIXME: This doesn't always remove the plugins dir. It seems that rpm doesn't
# honour the Requires(postun) as it should, causing maven to get uninstalled 
# before some plugins are
if [ -d %{_javadir}/%{name} ] ; then rmdir --ignore-fail-on-non-empty %{_javadir}/%{name} >& /dev/null; fi





%files -n maven-artifact
%{_mavendepmapfragdir}/%{name}-maven-artifact
%{_javadir}/%{main_pkg}/maven-artifact-2.*.jar
%{_mavenpomdir}/JPP.%{main_pkg}-maven-artifact-2.*.pom

%files -n maven-artifact-manager
%{_mavendepmapfragdir}/%{name}-maven-artifact-manager
%{_javadir}/%{main_pkg}/maven-artifact-manager.jar
%{_mavenpomdir}/JPP.%{main_pkg}-maven-artifact-manager.pom

%files -n maven-error-diagnostics
%{_mavendepmapfragdir}/%{name}-maven-error-diagnostics
%{_javadir}/%{main_pkg}/maven-error-diagnostics.jar
%{_mavenpomdir}/JPP.%{main_pkg}-maven-error-diagnostics.pom

%files -n maven-model
%{_mavendepmapfragdir}/%{name}-maven-model
%{_javadir}/%{main_pkg}/maven-model-*.jar
%{_mavenpomdir}/JPP.%{main_pkg}-maven-model-*.pom

%files -n maven-monitor
%{_mavendepmapfragdir}/%{name}-maven-monitor
%{_javadir}/%{main_pkg}/maven-monitor.jar
%{_mavenpomdir}/JPP.%{main_pkg}-maven-monitor.pom

%files -n maven-plugin-registry
%{_mavendepmapfragdir}/%{name}-maven-plugin-registry
%{_javadir}/%{main_pkg}/maven-plugin-registry.jar
%{_mavenpomdir}/JPP.%{main_pkg}-maven-plugin-registry.pom

%files -n maven-profile
%{_mavendepmapfragdir}/%{name}-maven-profile
%{_javadir}/%{main_pkg}/maven-profile.jar
%{_mavenpomdir}/JPP.%{main_pkg}-maven-profile.pom

%files -n maven-project
%{_mavendepmapfragdir}/%{name}-maven-project
%{_javadir}/%{main_pkg}/maven-project.jar
%{_mavenpomdir}/JPP.%{main_pkg}-maven-project.pom

%files -n maven-settings
%{_mavendepmapfragdir}/%{name}-maven-settings
%{_javadir}/%{main_pkg}/maven-settings-*.jar
%{_mavenpomdir}/JPP.%{main_pkg}-maven-settings-*.pom

%files -n maven-toolchain
%{_mavendepmapfragdir}/%{name}-maven-toolchain
%{_javadir}/%{main_pkg}/maven-toolchain.jar
%{_mavenpomdir}/JPP.%{main_pkg}-maven-toolchain.pom

%files -n maven-plugin-descriptor
%{_mavendepmapfragdir}/%{name}-maven-plugin-descriptor
%{_javadir}/%{main_pkg}/maven-plugin-descriptor.jar
%{_mavenpomdir}/JPP.%{main_pkg}-maven-plugin-descriptor.pom

%files 
%attr(0755,root,root) %{_bindir}/mvn-jpp



%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt4_37jpp7
- versioned provides

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt3_37jpp7
- update

* Fri Sep 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt3_32jpp7
- restored maven-model subpackage 

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt2_32jpp7
- fixed verbose post

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

