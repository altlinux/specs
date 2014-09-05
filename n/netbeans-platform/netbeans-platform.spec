# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
%set_verify_elf_method fhs=relaxed
BuildRequires: /proc
BuildRequires: jpackage-compat
# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

%define nb_             netbeans
%define nb_major_ver    7.0
%define nb_minor_ver    1
%define nb_ver          %{nb_major_ver}.%{nb_minor_ver}

%define nb_release_time 201107282000
%define nb_home         %{_datadir}/%{nb_}
%define nb_dir          %{nb_home}/%{nb_major_ver}

%define nb_platform_ver  13
%define nb_platform      platform
%define nb_platform_dir  %{nb_home}/%{nb_platform}%{nb_platform_ver}
%define nb_platform_pkg  %{nb_}-platform
%define nb_platform_vpkg %{nb_}-%{nb_platform}%{nb_platform_ver}

%define nb_harness      harness
%define nb_harness_dir  %{nb_home}/%{nb_harness}
%define nb_harness_vpkg %{nb_}-%{nb_harness}

%define nb_javadoc      javadoc
%define nb_javadoc_dir  %{_javadocdir}/%{nb_}-%{nb_platform}

%define compiler_opt    -Dbuild.compiler.deprecation=false -Dbuild.compiler.debug=false
%define jdk_opt         -Dpermit.jdk6.builds=true -Dpermit.jdk7.builds=true
%define verify_opt      -Dverify.checkout=false
%define ant_nb_opt      %{ant} %{jdk_opt} %{compiler_opt} %{verify_opt}

%define nb_javadoc_site http://bits.netbeans.org/%{nb_ver}/javadoc

%define nbbuild_platform_dir nbbuild/netbeans/%{nb_platform}
%define nbbuild_harness_dir nbbuild/netbeans/%{nb_harness}

# Prevents use of autoupdate on the specified directory.
# %%{1} the directory being prevented for autoupdate.
%define noautoupdate()  echo > %{1}/.noautoupdate

# Creates the time stamp of the last modification for the NetBeans cluster.
# See:
# http://bits.netbeans.org/dev/javadoc/org-netbeans-bootstrap/overview-summary.html#java.io.File-.lastModified
# %%{1} the directory of the NetBeans cluster.
%define lastModified()  echo > %{1}/.lastModified

# Creates artifacts of the NetBeans cluster.
# %%{1} the directory of the NetBeans cluster.
%define nbCluster() %{expand:%%noautoupdate %{1}} ; %{expand:%%lastModified %{1}} ;

# Links the system JAR.
# %%{1} - the sys jar
# %%{2} - the symlink name/path (optional)
%global lnSys() \
  if [ -f %{1} ] ; then \
     %__ln_s -f %{*} ; \
  else \
    echo "%{1} doesn't exist." ; exit 1 ; \
  fi ;

# Removes all specified files, and creates the file rmFiles.lst.
# %%{1} - the iname value, e.g. "*.zip"
%global rmFiles() find . -type f \\( -iname %{1} \\) | \
                  tee -a ./rmFiles.lst | xargs -t %__rm -f ;

%global debug_package %{nil}

Name:         netbeans-platform
Epoch:        1
Version:      %{nb_ver}
Release:      alt1_9jpp7
Summary:      NetBeans Platform
Group:        Development/Java
License:      GPLv2 with exceptions or CDDL
URL:          http://platform.netbeans.org

Source0: http://download.netbeans.org/%{nb_}/%{version}/final/zip/%{nb_}-%{version}-%{nb_release_time}-platform-src.zip

# Avoids copying the external binaries
# (*.exe *.dll) from the o.n.bootstrup/build.xml
Patch0: remove-binaries-from-release.patch
# Avoid looking for non-linux jna bits
Patch1: remove-non-linux-jna-bits.patch
# Prevents from releasing zip files (swing-layout-1.0.4-doc.zip,
# swing-layout-1.0.4-src.zip) in the o.jdesktop.layout module
Patch2: remove-swing-layout-src.patch
# Do not copy non-linux jni libaries
Patch3: remove-non-linux-jni-libs.patch
# Build native libraries
Patch4: build-native-code.patch
# Fix path to native build dir
#Patch5: native-build-properties.patch
Patch5: fix-native-dir-paths.patch
# Fix paths and flags in jnilib native build
Patch6: jnilib-build-uniformly-across-archs.patch
# Do not special case so names
Patch7: do-not-name-sos-based-on-arch.patch
# Do not build windows cleaners
Patch8: no-windows-cleaners.patch
# Compatiblity with newer jna
Patch9: jna-structure-changes.patch
# Compatiblity with ant 1.9
Patch10: ant-1.9.patch

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: antlr3-java
BuildRequires: bindex >= 2.2
BuildRequires: felix-osgi-core >= 1.4.0
BuildRequires: felix-osgi-compendium >= 1.4.0
BuildRequires: felix-main >= 2.0.5
BuildRequires: felix-framework >= 2.0.5
BuildRequires: javahelp2 >= 2.0.05
BuildRequires: jna >= 3.0.9
BuildRequires: jna-contrib
BuildRequires: junit4 >= 4.5
BuildRequires: jakarta-oro >= 2.0.8
BuildRequires: jemmy >= 2.3.0.0
BuildRequires: swing-layout >= 1.0
BuildRequires: stringtemplate

Requires: jpackage-utils
Requires: junit4 >= 4.5
Requires: swing-layout >= 1.0
Requires: javahelp2 >= 2.0.05
Requires: jna >= 3.0.9
Requires: jna-contrib
Requires: felix-osgi-core >= 1.4.0
Requires: felix-osgi-compendium >= 1.4.0
Requires: felix-main >= 2.0.5
Requires: felix-framework >= 2.0.5

Provides: %{nb_platform_vpkg} = %{epoch}:%{version}-%{release}
Source44: import.info

# macos proxy detection code :(
#+ Requires: /usr/bin/grep
#+ Requires: /usr/sbin/scutil
%add_findreq_skiplist /usr/share/netbeans/platform*/lib/nbexec

%description
The NetBeans Platform is a generic framework for Swing applications.
It provides the services common to almost all large desktop
applications: window management, menus, settings and storage, update
management, file access, etc.

%package %{nb_javadoc}
Summary: Javadoc documentation for NetBeans Platform
Group: Development/Java
BuildArch: noarch

%description %{nb_javadoc}
NetBeans Platform is a set of modules, each providing
their own APIs and working together or in a standalone
mode. This package provides one master 
javadoc to all of them.

%package %{nb_harness}
Summary: Build harness for NetBeans Platform
Group: Development/Java

Requires: %{name} = %{epoch}:%{version}-%{release}

Requires: jpackage-utils

Requires: ant >= 1.7.0
Requires: bindex >= 2.2
Requires: cobertura >= 1.9.3
Requires: jakarta-oro >= 2.0.8
Requires: javahelp2 >= 2.0.05
Requires: jemmy >= 2.3.0.0

Provides:  %{nb_harness_vpkg} = %{epoch}:%{version}-%{release}

%description %{nb_harness}
Harness with build scripts and ant tasks for everyone who
build an application on top of NetBeans Platform

%prep
%setup -q -c

%rmFiles "*.jar"
%rmFiles "*.zip"
%rmFiles "*.exe"
%rmFiles "*.dll"
%rmFiles "*.so"
%rmFiles "binaries-list"

# To build the netbeans modules the system JARs will be used instead of pre-packaged ones
%lnSys %{_javadir}/javahelp2.jar     javahelp/external/jhall-2.0_05.jar
%lnSys %{_javadir}/jemmy.jar         jemmy/external/jemmy-2.3.0.0.jar
%lnSys %{_javadir}/jna.jar           libs.jna/external/jna-3.2.7.jar
mkdir -p libs.jna/external/linux-amd64
mkdir -p libs.jna/external/linux-i386
%lnSys %{_libdir}/jna/libjnidispatch.so libs.jna/external/linux-amd64/libjnidispatch.so
%lnSys %{_libdir}/jna/libjnidispatch.so libs.jna/external/linux-i386/libjnidispatch.so         

%lnSys %{_javadir}/junit4.jar        libs.junit4/external/junit-4.8.2.jar
%lnSys %{_javadir}/swing-layout.jar  o.jdesktop.layout/external/swing-layout-1.0.4.jar

pushd apisupport.harness/external
  %lnSys %{_javadir}/javahelp2.jar jsearch-2.0_05.jar
  %lnSys %{_javadir}/bindex.jar bindex-2.2.jar
popd
pushd core.nativeaccess/external
  #%lnSys %{_javadir}/jna.jar platform-3.2.7.jar
  %lnSys %{_javadir}/jna/platform.jar platform-3.2.7.jar 
popd
pushd libs.antlr3.devel/external
  %lnSys %{_javadir}/antlr3-runtime.jar antlr-3.1.3.jar
  %lnSys %{_javadir}/stringtemplate.jar stringtemplate-3.2.jar
popd
pushd libs.felix/external
  %lnSys %{_javadir}/felix/org.apache.felix.framework.jar felix-2.0.3.jar
  %lnSys %{_javadir}/felix/org.apache.felix.main.jar felix-main-2.0.2.jar
popd
pushd libs.osgi/external
  %lnSys %{_javadir}/felix/org.osgi.core.jar osgi.core-4.2.jar
  %lnSys %{_javadir}/felix/org.osgi.compendium.jar osgi.cmpn-4.2.jar
popd

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build

# build platform & harness
%ant_nb_opt -f nbbuild/build.xml build-platform

# build platform javadoc
%ant_nb_opt \
   -Dallmodules= \
   -Dcluster.config=platform \
   -Dconfig.javadoc.cluster=%{nb_platform} \
   -Dconfig.javadoc.netbeans=\
openide.util,openide.actions,openide.options,openide.awt,\
openide.dialogs,openide.nodes,openide.explorer,openide.filesystems,openide.modules,\
openide.text,openide.windows,openide.loaders,openide.io,queries,\
o.n.api.progress,settings,javahelp,openide.execution,\
sendopts,options.api,editor.mimelookup \
   -Djavadoc.docs.org-netbeans-api-java=%{nb_javadoc_site}/org-netbeans-api-java/ \
   -Djavadoc.docs.org-netbeans-modules-project-ant=%{nb_javadoc_site}/org-netbeans-modules-project-ant/ \
   -Djavadoc.docs.org-netbeans-modules-projectapi=%{nb_javadoc_site}/org-netbeans-modules-projectapi/ \
   -f nbbuild/build.xml build-javadoc

# clean up stub jars
%__rm -f %{nbbuild_platform_dir}/modules/ext/script-api.jar

%install
# install platform
%__mkdir_p %{buildroot}%{nb_platform_dir}
%__cp -pr nbbuild/netbeans/%{nb_platform}/* %{buildroot}%{nb_platform_dir}
%nbCluster %{buildroot}%{nb_platform_dir}

# linking the platform to the system JARs
pushd %{buildroot}%{nb_platform_dir}/modules/ext
  %lnSys %{_javadir}/felix/org.apache.felix.framework.jar felix-2.0.3.jar
  %lnSys %{_javadir}/felix/org.apache.felix.main.jar felix-main-2.0.2.jar
  %lnSys %{_javadir}/javahelp2.jar    jhall-2.0_05.jar
  %lnSys %{_javadir}/jna.jar          jna-3.2.7.jar
  %lnSys %{_javadir}/jna/platform.jar platform-3.2.7.jar
  %lnSys %{_javadir}/junit4.jar       junit-4.5.jar
  %lnSys %{_javadir}/felix/org.osgi.compendium.jar osgi.cmpn-4.2.jar
  %lnSys %{_javadir}/felix/org.osgi.core.jar osgi.core-4.2.jar
  %lnSys %{_javadir}/swing-layout.jar swing-layout-1.0.4.jar
popd
pushd %{buildroot}%{nb_platform_dir}/modules/lib
  %lnSys %{_libdir}/jna/libjnidispatch.so amd64/Linux/libjnidispatch.so
  %lnSys %{_libdir}/jna/libjnidispatch.so i386/Linux/libjnidispatch.so
popd

# link system jars to platform
%{__mkdir_p} %{buildroot}%{_javadir}/netbeans
%{__ln_s} %{nb_platform_dir}/modules/org-netbeans-swing-outline.jar \
  %{buildroot}%{_javadir}/netbeans/swing-outline.jar
%{__ln_s} %{nb_platform_dir}/modules/org-netbeans-swing-plaf.jar \
  %{buildroot}%{_javadir}/netbeans/swing-plaf.jar
%{__ln_s} %{nb_platform_dir}/modules/org-netbeans-swing-tabcontrol.jar \
  %{buildroot}%{_javadir}/netbeans/swing-tabcontrol.jar

# install harness
%__mkdir_p %{buildroot}%{nb_harness_dir}
%__cp -pr nbbuild/netbeans/%{nb_harness}/* %{buildroot}%{nb_harness_dir}
%nbCluster %{buildroot}%{nb_harness_dir}

# linking the harness to the system JARs
pushd %{buildroot}%{nb_harness_dir}
  pushd antlib
    %lnSys %{_javadir}/bindex.jar bindex-2.2.jar
    %lnSys %{_javadir}/javahelp2.jar jsearch-2.0_05.jar
  popd
  %lnSys %{_javadir}/jemmy.jar modules/ext/jemmy-2.3.0.0.jar
popd

# install javadoc
%__rm -rf  nbbuild/build/javadoc/*.zip
%__mkdir_p %{buildroot}%{nb_javadoc_dir}
%__cp -pr nbbuild/build/javadoc/* %{buildroot}%{nb_javadoc_dir}


%files
%doc nbbuild/licenses/CDDL-GPL-2-CP
%dir %{nb_home}/
%dir %{nb_platform_dir}/
%{nb_platform_dir}/config
%{nb_platform_dir}/core
%dir %{nb_platform_dir}/lib
%{nb_platform_dir}/lib/boot.jar
%attr(755, root, root) %{nb_platform_dir}/lib/nbexec
%{nb_platform_dir}/lib/org-openide-modules.jar
%{nb_platform_dir}/lib/org-openide-util.jar
%{nb_platform_dir}/lib/org-openide-util-lookup.jar
%{nb_platform_dir}/modules
%{nb_platform_dir}/update_tracking
%{nb_platform_dir}/VERSION.txt
%{nb_platform_dir}/.noautoupdate
%{nb_platform_dir}/.lastModified
%{_javadir}/netbeans/swing-outline.jar
%{_javadir}/netbeans/swing-plaf.jar
%{_javadir}/netbeans/swing-tabcontrol.jar

%files %{nb_harness}
%dir %{nb_harness_dir}/
%{nb_harness_dir}/antlib
%{nb_harness_dir}/config
%{nb_harness_dir}/etc
%{nb_harness_dir}/jnlp
%dir %{nb_harness_dir}/launchers
%attr(755, root, root) %{nb_harness_dir}/launchers/app.sh
%{nb_harness_dir}/modules
%{nb_harness_dir}/nbi
%{nb_harness_dir}/update_tracking
%doc %{nb_harness_dir}/README
%{nb_harness_dir}/build.xml
%{nb_harness_dir}/common.xml
%{nb_harness_dir}/jdk.xml
%{nb_harness_dir}/jnlp.xml
%{nb_harness_dir}/no-testcoverage.xml
%{nb_harness_dir}/osgi.xml
%{nb_harness_dir}/run.xml
%{nb_harness_dir}/suite.xml
%{nb_harness_dir}/tasks.jar
%{nb_harness_dir}/.noautoupdate
%{nb_harness_dir}/.lastModified

%files %{nb_javadoc}
%doc %{nb_javadoc_dir}/
%doc nbbuild/licenses/CDDL-GPL-2-CP

%changelog
* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 1:7.0.1-alt1_9jpp7
- new version

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1:7.0.1-alt1_6jpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1:6.9.1-alt2_3jpp6
- built with java 6

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 1:6.9.1-alt1_3jpp6
- update to new release by jppimport

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 6.9-alt1_4jpp6
- new version

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 6.8-alt1_2jpp6
- new version

* Thu Apr 30 2009 Igor Vlasenko <viy@altlinux.ru> 6.5-alt1_6jpp6
- new version

