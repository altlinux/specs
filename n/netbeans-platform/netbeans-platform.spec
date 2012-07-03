%set_verify_elf_method fhs=relaxed
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# one of the sources is a zip file
BuildRequires: unzip
BuildRequires: gcc-c++
# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

%define nb_             netbeans
%define nb_major_ver    6.9
%define nb_bugfix_ver   1
%define nb_ver          %{nb_major_ver}.%{nb_bugfix_ver}

%define nb_release_time 201007282301
%define nb_home         %{_datadir}/%{nb_}
%define nb_dir          %{nb_home}/%{nb_major_ver}

%define nb_platform_ver 12
%define nb_platform     platform
%define nb_platform_dir %{nb_home}/%{nb_platform}%{nb_platform_ver}
%define nb_platform_vpkg %{nb_}-%{nb_platform}%{nb_platform_ver}

%define nb_harness      harness
%define nb_harness_dir  %{nb_home}/%{nb_harness}

%define nb_javadoc      javadoc
%define nb_javadoc_dir  %{_javadocdir}/%{nb_}-%{nb_platform}

%define compiler_opt    -Dbuild.compiler.deprecation=false -Dbuild.compiler.debug=false
%define jdk_opt         -Dpermit.jdk6.builds=true
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
%global lnSysJAR() \
  if [ -f %{_javadir}/%{1} ] ; then \
     %__ln_s -f %{_javadir}/%{*} ; \
  else \
    echo "%{1} doesn't exist." ; exit 1 ; \
  fi ;

# Removes all specified files, and creates the file rmFiles.lst.
# %%{1} - the iname value, e.g. "*.zip"
%global rmFiles() find . -type f \\( -iname %{1} \\) | \
                  tee -a ./rmFiles.lst | xargs -t %__rm -f ;

Name:         netbeans-platform
Epoch:        1
Version:      %{nb_ver}
Release:      alt2_3jpp6
Summary:      NetBeans Platform {nb_ver}
Group:        Development/Java
License:      GPLv2 with exceptions or CDDL
URL:          http://platform.netbeans.org

Source0: http://download.netbeans.org/%{nb_}/%{version}/final/zip/%{nb_}-%{version}-%{nb_release_time}-platform-src.zip

# Avoids copying the external binaries
# (*.exe *.dll) from the o.n.bootstrup/build.xml
Patch0: %{name}-6.9~release_external.patch
# Prevents from releasing zip files (swing-layout-1.0.4-doc.zip,
# swing-layout-1.0.4-src.zip) in the o.jdesktop.layout module
Patch1: %{name}-6.9~properties.patch
# Avoids copying the external binaries in nbi module
Patch2: %{name}-6.9~nbi.patch
# Avoids spam in the log if the -XX:+HeapDumpOnOutOfMemoryError option is not supported by the JVM
# http://netbeans.org/bugzilla/show_bug.cgi?id=188283
Patch3: %{name}-6.9~launcher.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: ant >= 1.7.0
BuildRequires: ant-junit >= 1.7.0
BuildRequires: ant-nodeps >= 1.7.0
BuildRequires: ant-trax >= 1.7.0
BuildRequires: junit4 >= 4.5
BuildRequires: swing-layout >= 1.0
BuildRequires: javahelp2 >= 2.0.05
BuildRequires: jna >= 3.0.9
BuildRequires: cobertura >= 1.9.3
BuildRequires: objectweb-asm >= 3.0
BuildRequires: log4j >= 1.2.9
BuildRequires: jakarta-oro >= 2.0.8
BuildRequires: jemmy >= 2.3.0.0
BuildRequires: felix-osgi-core >= 1.4.0
BuildRequires: felix-osgi-compendium >= 1.4.0
BuildRequires: felix-main >= 2.0.5
BuildRequires: felix-framework >= 2.0.5
BuildRequires: bindex >= 2.2

Requires: jpackage-utils
Requires: junit4 >= 4.5
Requires: swing-layout >= 1.0
Requires: javahelp2 >= 2.0.05
Requires: jna >= 3.0.9
Requires: felix-osgi-core >= 1.4.0
Requires: felix-osgi-compendium >= 1.4.0
Requires: felix-main >= 2.0.5
Requires: felix-framework >= 2.0.5

Provides: %{nb_platform_vpkg} = %{version}-%{release}
Source44: import.info

# macos proxy detection code :(
#+ Requires: /usr/bin/grep
#+ Requires: /usr/sbin/scutil
%add_findreq_skiplist /usr/share/netbeans/platform*/lib/nbexec

%description
The NetBeans Platform, version %{nb_platform_ver}, is a generic framework 
for Swing applications. It provides the services common to almost all 
large desktop applications: window management, menus, settings and 
storage, update management, file access, etc.

%package %{nb_javadoc}
Summary: Javadoc documentation for NetBeans Platform %{nb_platform_ver}
Group: Development/Java
%description %{nb_javadoc}
NetBeans Platform is a set of modules, each providing
their own APIs and working together or in a standalone
mode. This package provides one master 
javadoc to all of them.

%package %{nb_harness}
Summary: Build harness for NetBeans Platform %{nb_platform_ver}
Group: Development/Java
Requires: jpackage-utils
Requires: ant >= 1.7.0
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: javahelp2 >= 2.0.05
Requires: cobertura >= 1.9.3
Requires: objectweb-asm >= 3.0
Requires: log4j >= 1.2.9
Requires: jakarta-oro >= 2.0.8
Requires: jemmy >= 2.3.0.0
Requires: bindex >= 2.2
%description %{nb_harness}
Harness with build scripts and ant tasks for everyone who
build an application on top of NetBeans Platform

%prep
%setup -q -c

%rmFiles "*.jar"
%rmFiles "*.zip"
%rmFiles "*.exe"
%rmFiles "*.dll"
%rmFiles "binaries-list"

# To build the netbeans modules the system JARs will be used instead of pre-packaged ones
%lnSysJAR javahelp2.jar     javahelp/external/jh-2.0_05.jar
%lnSysJAR jemmy.jar         jemmy/external/jemmy-2.3.0.0.jar
%lnSysJAR jna.jar           libs.jna/external/jna-3.0.9.jar
%lnSysJAR junit4.jar        libs.junit4/external/junit-4.5.jar
%lnSysJAR swing-layout.jar  o.jdesktop.layout/external/swing-layout-1.0.4.jar

pushd apisupport.harness/external
  %lnSysJAR javahelp2.jar jsearch-2.0_05.jar
  %lnSysJAR bindex.jar bindex-2.2.jar
popd
pushd apisupport.tc.cobertura/external
  %lnSysJAR objectweb-asm/asm-all.jar asm-3.0.jar
  %lnSysJAR objectweb-asm/asm-all.jar asm-tree-3.0.jar
  %lnSysJAR cobertura.jar cobertura-1.9.3.jar
  %lnSysJAR oro.jar       jakarta-oro-2.0.8.jar
  %lnSysJAR log4j.jar     log4j-1.2.9.jar
popd
pushd libs.felix/external
  %lnSysJAR felix/org.apache.felix.framework.jar felix-2.0.3.jar
  %lnSysJAR felix/org.apache.felix.main.jar felix-main-2.0.2.jar
popd
pushd libs.osgi/external
  %lnSysJAR felix/org.osgi.core.jar osgi.core-4.2.jar
  %lnSysJAR felix/org.osgi.compendium.jar osgi.cmpn-4.2.jar
popd

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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
  %lnSysJAR felix/org.apache.felix.framework.jar felix-2.0.3.jar
  %lnSysJAR felix/org.apache.felix.main.jar felix-main-2.0.2.jar
  %lnSysJAR javahelp2.jar    jh-2.0_05.jar
  %lnSysJAR jna.jar          jna-3.0.9.jar
  %lnSysJAR junit4.jar       junit-4.5.jar
  %lnSysJAR felix/org.osgi.compendium.jar osgi.cmpn-4.2.jar
  %lnSysJAR felix/org.osgi.core.jar osgi.core-4.2.jar
  %lnSysJAR swing-layout.jar swing-layout-1.0.4.jar
popd

# install harness
%__mkdir_p %{buildroot}%{nb_harness_dir}
%__cp -pr nbbuild/netbeans/%{nb_harness}/* %{buildroot}%{nb_harness_dir}
%nbCluster %{buildroot}%{nb_harness_dir}

# linking the harness to the system JARs
pushd %{buildroot}%{nb_harness_dir}
  pushd antlib
    %lnSysJAR bindex.jar bindex-2.2.jar
    %lnSysJAR javahelp2.jar jsearch-2.0_05.jar
  popd
  %lnSysJAR jemmy.jar modules/ext/jemmy-2.3.0.0.jar
  pushd testcoverage/cobertura
    %lnSysJAR cobertura.jar cobertura-1.9.3.jar
    pushd lib
      %lnSysJAR objectweb-asm/asm-all.jar asm-3.0.jar
      %lnSysJAR objectweb-asm/asm-all.jar asm-tree-3.0.jar
      %lnSysJAR oro.jar       jakarta-oro-2.0.8.jar
      %lnSysJAR log4j.jar     log4j-1.2.9.jar
    popd
  popd
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
%{nb_harness_dir}/testcoverage
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
%{nb_harness_dir}/testcoverage-suite.xml
%{nb_harness_dir}/testcoverage.xml
%{nb_harness_dir}/.noautoupdate
%{nb_harness_dir}/.lastModified

%files %{nb_javadoc}
%doc %{nb_javadoc_dir}/
%doc nbbuild/licenses/CDDL-GPL-2-CP

%changelog
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

