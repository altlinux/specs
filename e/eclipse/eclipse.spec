%define _enable_debug 1
BuildRequires: java-javadoc ant-jai ant-junit4 ant-junit
AutoReqProv: yes,nopython
BuildRequires: xorg-proto-devel libGLU-devel
BuildRequires: java-devel-openjdk
Requires: dbus
BuildRequires: ant-optional
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
Epoch:  1

%global eclipse_major   4
%global eclipse_minor   2
%global eclipse_majmin  %{eclipse_major}.%{eclipse_minor}
%global eclipse_micro   0
%global initialize      1
%global download_url    http://download.eclipse.org/technology/linuxtools/eclipse-build/4.2.x/
%global eb_sha1         8b7060063e10f73e00056a9766d33fc43f043f4b
%global build_id        I20120608-1400
%global eclipse_version %{eclipse_majmin}.%{eclipse_micro}
%global emf_version     2.8.0

# FIXME:  update java packaging guidelines for this.  See
# fedora-devel-java-list discussion in September 2008.
#
# Prevent brp-java-repack-jars from being run.
%define __jar_repack 0

Summary:        An open, extensible IDE
Name:           eclipse
Version:        %{eclipse_version}
Release:        alt7_7jpp7
License:        EPL
Group:          Editors
URL:            http://www.eclipse.org/
Source0:        %{download_url}eclipse-build-%{eb_sha1}.tar.xz
Source1:        %{download_url}eclipse-%{eclipse_version}-%{build_id}-src.tar.bz2
Source4:        macros.%{name}
Source5:        http://repo1.maven.org/maven2/org/eclipse/osgi/org.eclipse.osgi/3.6.0.v20100517/org.eclipse.osgi-3.6.0.v20100517.pom
# Fetched from http://repo1.maven.org/maven2/org/eclipse/osgi/org.eclipse.osgi.services/3.2.100.v20100503/org.eclipse.osgi.services-3.2.100.v20100503.pom
# Patched to remove fake parent
Source6:        org.eclipse.osgi.services-3.2.100.v20100503.pom
Source7:        http://repo1.maven.org/maven2/org/eclipse/equinox/http/servlet/1.0.0-v20070606/servlet-1.0.0-v20070606.pom
Source8:        org.eclipse.jdt.core-3.8.0.v_C03.pom
Patch0:         lucene-3.6-compile.patch
Patch73:	eclipse-3.7.0-alt-dependencies.patch
Patch74:	fix-libwebkitgtk-1.11.91-compatibility.patch
Patch75:    swt-gtk-combo.patch

BuildRequires:  ant >= 1.8.3
BuildRequires:  rsync
BuildRequires:  jpackage-utils >= 0:1.5 make gcc
BuildRequires:  gtk2-devel
BuildRequires:  glib2-devel
BuildRequires:  libGConf-devel
BuildRequires:  gcc-c++
BuildRequires:  libnspr-devel
BuildRequires:  libXtst-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libcairo >= 1.0
BuildRequires:  unzip
BuildRequires:  desktop-file-utils
BuildRequires:  java-javadoc >= 1:1.7.0
BuildRequires:  libXt-devel
BuildRequires:  webkitgtk-devel
BuildRequires:  geronimo-annotation >= 1.0-7

BuildRequires: icu4j-eclipse >= 1:4.4.2.2-11
BuildRequires: tomcat-lib >= 7.0.25-3
BuildRequires: ant-antlr ant-apache-bcel ant-apache-log4j ant-apache-oro ant-apache-regexp ant-apache-resolver ant-commons-logging ant-apache-bsf ant-commons-net
BuildRequires: ant-javamail ant-jdepend ant-junit ant-junit4 ant-swing ant-jsch ant-testutil ant-apache-xalan2 ant-jmf
BuildRequires: ant-scripts
BuildRequires: jsch >= 0:0.1.46-2
BuildRequires: apache-commons-el >= 1.0-22
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-codec >= 1.6-2
BuildRequires: jakarta-commons-httpclient >= 1:3.1-7
BuildRequires: felix-gogo-command >= 0.12
BuildRequires: felix-gogo-shell >= 0.10.0-3
BuildRequires: jetty >= 8.1.0-1
BuildRequires: lucene >= 2.9.4-8
BuildRequires: lucene-contrib >= 2.9.4-8
BuildRequires: junit4 >= 4.10-5
BuildRequires: hamcrest >= 0:1.1-11
BuildRequires: sat4j >= 2.3.0-1
BuildRequires: objectweb-asm >= 3.3.1-1
BuildRequires: zip
BuildRequires: sac >= 1.3-12
BuildRequires: batik >= 1.8
BuildRequires: xml-commons-apis 
BuildRequires: atinject >= 1-6

%if 0%{?rhel} >= 6
ExclusiveArch: %{ix86} x86_64
%endif
Source44: import.info
Patch33: eclipse-3.7.0-alt-as-needed-statically-link-xpcomglue.patch
Patch34: eclipse-3.7.0-alt-libgnomeproxy-gcc-as-needed.patch
Patch35: eclipse-3.7.0-alt-swt-linux-as-needed.patch
Patch41: eclipse-4.2.0-alt-swt-enable-depercated-glib2-headers.patch
Source45: fix_share_symlinks_to_libdir.pl

%description
The Eclipse platform is designed for building integrated development
environments (IDEs), server-side applications, desktop applications, and
everything in between.

%package     swt
Version:        %{eclipse_version}
Summary:        SWT Library for GTK+-2.0
Group:          Editors
# %{_libdir}/java directory owned by jpackage-utils
Requires:       jpackage-utils
Requires:       gtk2
Requires:       webkitgtk

%description swt
SWT Library for GTK+-2.0.

%package      equinox-osgi
Group: Editors
Version:        %{eclipse_version}
Summary:        Eclipse OSGi - Equinox
Requires:       jpackage-utils

%description  equinox-osgi
Eclipse OSGi - Equinox

%package        rcp
Version:        %{eclipse_version}
Summary:        Eclipse Rich Client Platform
Group:          Development/Java
Requires:       eclipse-swt = %{epoch}:%{eclipse_version}-%{release}
Requires:       eclipse-equinox-osgi = %{epoch}:%{eclipse_version}-%{release}
Requires:       icu4j-eclipse >= 1:4.4.2.2-11
#Requires:       %{name}-emf-core >= %{epoch}:%{emf_version}-%{release}
Provides:       osgi(system.bundle) = %{epoch}:%{eclipse_version}
Provides:	osgi(org.eclipse.core.runtime) = %version
Provides:	osgi(org.eclipse.equinox.ds) = %version

%description    rcp
Eclipse Rich Client Platform

%package        platform
AutoReqProv: yes,nopython
Version:        %{eclipse_version}
Summary:        Eclipse platform common files
Group:          Editors
Requires:   eclipse-rcp = %{epoch}:%{eclipse_version}-%{release}
Requires: ant-antlr ant-apache-bcel ant-apache-log4j ant-apache-oro ant-apache-regexp ant-apache-resolver ant-commons-logging ant-apache-bsf ant-commons-net
Requires: ant-javamail ant-jdepend ant-junit ant-swing ant-jsch ant-testutil ant-apache-xalan2 ant-jmf
Requires: ant-scripts
Requires: apache-commons-el >= 1.0-23
Requires: apache-commons-logging
Requires: apache-commons-codec >= 1.6-2
Requires: jakarta-commons-httpclient >= 1:3.1-7
Requires: tomcat-lib >= 7.0.25-3
Requires: felix-gogo-command >= 0.12
Requires: felix-gogo-shell >= 0.10.0-3
Requires: jetty >= 8.1.0-1
Requires: jsch >= 0.1.46-2
Requires: lucene >= 2.9.4-8
Requires: lucene-contrib >= 2.9.4-8
Requires: sat4j >= 2.3.0-1
Requires: sac >= 1.3-12
Requires: xml-commons-apis
Requires: batik >= 1.8
Requires: atinject >= 1-6
Requires: geronimo-annotation >= 1.0-7
Provides: eclipse-cvs-client = 1:%{eclipse_version}-%{release}
Obsoletes: eclipse-cvs-client < 1:3.3.2-20
#Package eclipse-platform has broken dep on osgi(org.apache.el)
#Reinst eclipse-emf-core Failed early because of osgi(org.w3c.css.sac)
Provides: osgi(org.apache.el) = 1.0
Provides: osgi(org.w3c.css.sac) = 1.3.0
Provides: osgi(org.eclipse.equinox.p2.core) = 2.0.100
Provides: osgi(org.eclipse.equinox.p2.engine) = 2.0.0
Provides: osgi(org.eclipse.equinox.p2.metadata) = 2.1.0
Provides: osgi(org.eclipse.equinox.p2.repository) = 2.1.0


%description    platform
The Eclipse Platform is the base of all IDE plugins.  This does not include the
Java Development Tools or the Plugin Development Environment.


%package        jdt
Version:        %{eclipse_version}
Summary:        Eclipse Java Development Tools
Group:          Editors
Requires:       eclipse-platform = %{epoch}:%{eclipse_version}-%{release}
Requires:       eclipse-cvs-client = %{epoch}:%{eclipse_version}-%{release}
Requires:       junit4 >= 4.10-5
Requires:       jakarta-commons-httpclient >= 1:3.1-7
Requires:       hamcrest >= 0:1.1-11
Requires:       java-javadoc >= 1:1.7.0


%description    jdt
Eclipse Java Development Tools.  This package is required to use Eclipse for
developing software written in the Java programming language.

%package        pde
Version:        %{eclipse_version}
Summary:        Eclipse Plugin Development Environment
Group:          Editors
Provides:       eclipse = %{epoch}:%{eclipse_version}-%{release}
Provides:       eclipse-sdk = %{epoch}:%{eclipse_version}-%{release}
Requires:       eclipse-platform = %{epoch}:%{eclipse_version}-%{release}
Requires:       eclipse-jdt = %{epoch}:%{eclipse_version}-%{release}
Requires:       objectweb-asm >= 3.3.1-1
# For PDE Build wrapper script + creating jars
Requires:       zip
Requires:       bash
Provides:       %{name}-pde-runtime = 1:%{eclipse_version}-%{release}
Obsoletes:      %{name}-pde-runtime < 1:3.3.2-20

%description    pde
Eclipse Plugin Development Environment.  This package is required for
developing Eclipse plugins.

%prep
export JAVA_HOME=%{java_home}
%setup -q -n eclipse-build-%{eb_sha1}
cp %{SOURCE1} .
# Add new patches
%patch74 -p2
# Apply patches
ant applyPatches
%patch0
pushd build/eclipse-%{eclipse_version}-%{build_id}-src
%patch75 -p2

sed -i -e "s|\[2.9.0,3.0.0)|\[2.9.0,4.0.0)|g" plugins/org.eclipse.help.base/META-INF/MANIFEST.MF

# Use our system-installed javadocs, reference only what we built, and
# don't like to osgi.org docs (FIXME:  maybe we should package them?)
sed -i -e "s|http://download.oracle.com/javase/1.5.0/docs/api|%{_datadir}/javadoc/java|" \
   -e "/osgi\.org/d" \
   -e "s|-breakiterator|;../org.eclipse.equinox.util/@dot\n;../org.eclipse.ecf.filetransfer_3.0.0.v20090302-0803.jar\n;../org.eclipse.ecf_3.0.0.v20090302-0803.jar\n-breakiterator|" \
    plugins/org.eclipse.platform.doc.isv/platformOptions.txt
sed -i -e "s|http://download.oracle.com/javase/1.5.0/docs/api|%{_datadir}/javadoc/java|" \
   -e "s/win32.win32.x86/gtk.linux.%{eclipse_arch}/" \
   plugins/org.eclipse.jdt.doc.isv/jdtOptions.txt
sed -i -e "s|http://download.oracle.com/javase/6/docs/api|%{_datadir}/javadoc/java|" \
   -e "/osgi\.org/d" \
   plugins/org.eclipse.jdt.doc.isv/jdtOptions.txt
sed -i -e "s|http://download.oracle.com/javase/1.4.2/docs/api|%{_datadir}/javadoc/java|" \
   -e "s/motif.linux.x86/gtk.linux.%{eclipse_arch}/" \
   -e "/osgi\.org/d" \
   plugins/org.eclipse.pde.doc.user/pdeOptions.txt \
   plugins/org.eclipse.pde.doc.user/pdeOptions.txt
sed -i -e "s|http://download.oracle.com/javase/1.5.0/docs/api|%{_datadir}/javadoc/java|" \
   plugins/org.eclipse.pde.doc.user/pdeOptions.txt \
   plugins/org.eclipse.pde.doc.user/pdeOptions.txt

#fix for glib 2.31 not allowing include of anything else but glib
sed -i -e "s|#include <glib/gslist.h>||g" plugins/org.eclipse.core.net/natives/unix/gnomeproxy.c

# make sure there are no jars left
JARS=""
for j in $(find -name \*.jar); do
  if [ ! -L $j ]; then
    JARS="$JARS `echo $j`"
  fi
done
if [ ! -z "$JARS" ]; then
    echo "These jars should be deleted and symlinked to system jars: $JARS"
   #FIXME: enable  exit 1
fi

popd
pushd build/eclipse-%version-*
%patch33 -p2
%patch34 -p2
%patch35 -p2
%patch41 -p2
popd
%patch73 -p0

%build
export CXX='g++ -Dchar16_t="unsigned short int"'
export JAVA_HOME=%{java_home}
ant provision.cvs

%install
export JAVA_HOME=%{java_home}
ant -DdestDir=$RPM_BUILD_ROOT -Dprefix=/usr -Dmultilib=true installSDKinDropins

# We don't need icon.xpm
# https://bugs.eclipse.org/292472
rm -f $RPM_BUILD_ROOT/%{_libdir}/%{name}/icon.xpm

# Some directories we need
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/java
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
# Create file listings for the extracted shared libraries
echo -n "" > %{_builddir}/%{buildsubdir}/%{name}-platform.install;
for id in `ls configuration/org.eclipse.osgi/bundles`; do
  if [ "Xconfiguration" = $(echo X`find configuration/org.eclipse.osgi/bundles/$id -name libswt\*.so` | sed "s:/.*::") ]; then
    echo "%verify(not mtime) %{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles/$id" > %{_builddir}/%{buildsubdir}/%{name}-swt.install;
  else
    echo "%verify(not mtime) %{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles/$id" >> %{_builddir}/%{buildsubdir}/%{name}-platform.install;
  fi
done
popd

# Remove state files
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}/configuration/org.eclipse.osgi/
    rm -rf .bundledata* .lazy* .manager .state*
popd

# Symlinks to the SWT JNI shared libraries in %%{_libdir}/eclipse
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
for lib in $(find configuration -name libswt\*.so); do
  ln -s $lib `basename $lib`
done
popd

# Temporary fix until https://bugs.eclipse.org/294877 is resolved
sed -i "s|-Xms40m|-Xms128m|g" $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
sed -i "s|-Xmx384m|-Xmx512m|g" $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-Dorg.eclipse.swt.browser.UseWebKitGTK=true" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-Dhelp.lucene.tokenizer=standard" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/eclipse/core/internal/dtree/DataTreeNode,forwardDeltaWith" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/eclipse/jdt/internal/compiler/lookup/ParameterizedMethodBinding,<init>" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/eclipse/cdt/internal/core/dom/parser/cpp/semantics/CPPTemplates,instantiateTemplate" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/eclipse/cdt/internal/core/pdom/dom/cpp/PDOMCPPLinkage,addBinding" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/python/pydev/editor/codecompletion/revisited/PythonPathHelper,isValidSourceFile" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/python/pydev/ui/filetypes/FileTypesPreferencesPage,getDottedValidSourceFiles" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini

# Prevent running master Eclipse in a shared configuration
echo "-preventMasterEclipseLaunch" | cat - $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini > /tmp/out && mv -f /tmp/out $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini

# Deploy installation debug config
echo -e "org.eclipse.equinox.p2.core/debug=true" >  $RPM_BUILD_ROOT%{_libdir}/%{name}/.options
echo -e "org.eclipse.equinox.p2.core/reconciler=true" >>  $RPM_BUILD_ROOT%{_libdir}/%{name}/.options

# SWT JAR symlink in libdir
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
ln -s ../%{name}/swt.jar ../java/swt.jar
popd

# OSGI JAR symlinks in javadir and maven depmaps
pushd $RPM_BUILD_ROOT%{_javadir}/eclipse
ln -s ../../../../%{_libdir}/%{name}/plugins/org.eclipse.osgi_*.jar osgi.jar
popd
install -m 0644 %{SOURCE5} $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.eclipse-osgi.pom
%add_maven_depmap JPP.eclipse-osgi.pom %{name}/osgi.jar -a "org.eclipse:osgi,org.eclipse.tycho:org.eclipse.osgi" -f equinox-osgi

pushd $RPM_BUILD_ROOT%{_javadir}/eclipse
ln -s ../../../../%{_libdir}/%{name}/plugins/org.eclipse.osgi.services_*.jar osgi.services.jar
popd
install -m 0644 %{SOURCE6} $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.eclipse-osgi.services.pom
%add_maven_depmap JPP.eclipse-osgi.services.pom %{name}/osgi.services.jar -a "org.eclipse.osgi:services" -f equinox-osgi

pushd $RPM_BUILD_ROOT%{_javadir}/eclipse
ln -s ../../../../%{_libdir}/%{name}/plugins/org.eclipse.osgi.util_*.jar osgi.util.jar
popd

pushd $RPM_BUILD_ROOT%{_javadir}/eclipse
ln -s ../../../../%{_libdir}/%{name}/plugins/org.eclipse.equinox.http.servlet_*.jar equinox.http.servlet.jar
popd
install -m 0644 %{SOURCE7} $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.eclipse-equinox.http.servlet.pom
%add_maven_depmap JPP.eclipse-equinox.http.servlet.pom %{name}/equinox.http.servlet.jar -a "org.eclipse.equinox.http:servlet" -f platform

pushd $RPM_BUILD_ROOT%{_javadir}/eclipse
ln -s ../../../../%{_libdir}/%{name}/plugins/org.eclipse.jdt.core_*.jar jdt.core.jar
popd
install -m 0644 %{SOURCE8} $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.eclipse-jdt.core.pom
%add_maven_depmap JPP.eclipse-jdt.core.pom %{name}/jdt.core.jar -a "org.eclipse:jdt.core,org.eclipse.tycho:org.eclipse.jdt.core"  -f jdt
# A sanity check.
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

# Create a script that can be used to make a symlink tree of the
# eclipse platform.
cp -p pdebuild/eclipse-copy-platform.sh copy-platform

mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts
mv copy-platform $RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts
copyPlatform=$RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts/copy-platform

# Install the PDE Build wrapper script.
install -p -D -m0755 pdebuild/eclipse-pdebuild.sh \
  $RPM_BUILD_ROOT%{_bindir}/%{name}-pdebuild
PDEBUILDVERSION=$(ls $RPM_BUILD_ROOT%{_libdir}/%{name}/dropins/sdk/plugins \
  | grep org.eclipse.pde.build_ | \
  sed 's/org.eclipse.pde.build_//')
sed -i "s/@PDEBUILDVERSION@/$PDEBUILDVERSION/g" \
  $RPM_BUILD_ROOT%{_bindir}/%{name}-pdebuild

# Install eclipse macros file
mkdir $RPM_BUILD_ROOT%{_sysconfdir}/rpm/

# Remove the junit library duplicated by pdebuild.
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/dropins/jdt/plugins/org.junit_4.10.0.v4_10_0_v20120426-0900.jar
chmod 755 $RPM_BUILD_ROOT%{_bindir}/*
# check for undefined symbols
if find %buildroot%_libdir/eclipse -type f -name '*.so' -print0 \
 | xargs -0 ldd -r 2>&1 \
 | grep -v SUNWprivate \
 | grep 'undefined symbol'; then
    echo "JPP robo-check for undefined symbols failed."
    exit 1;
fi
# fix /usr/share symlinks to _libdir
perl %{SOURCE45} %buildroot
touch %buildroot/etc/eclipse.ini

%if %{initialize}
%files swt -f %{name}-swt.install
%else
%files swt
%endif
/etc/eclipse.ini
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%if %{initialize}
%{_libdir}/%{name}/libswt-*.so
%dir %{_libdir}/%{name}/configuration
%dir %{_libdir}/%{name}/configuration/org.eclipse.osgi
%dir %{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles
%endif
%{_libdir}/%{name}/notice.html
%{_libdir}/%{name}/eclipse.ini
%{_libdir}/%{name}/.options
%{_libdir}/%{name}/epl-v10.html
%{_libdir}/%{name}/plugins/org.eclipse.swt_*
%{_libdir}/%{name}/plugins/org.eclipse.swt.gtk.linux.*
%{_libdir}/%{name}/swt-gtk*.jar
%{_libdir}/%{name}/swt.jar
%{_libdir}/java/swt.jar

%files rcp
%dir %{_libdir}/%{name}/features
%dir %{_datadir}/%{name}
%dir %{_libdir}/%{name}/configuration
%{_libdir}/%{name}/configuration/config.ini
%{_libdir}/%{name}/configuration/org.eclipse.equinox.simpleconfigurator/bundles.info
%dir %{_libdir}/%{name}/configuration/org.eclipse.equinox.simpleconfigurator
%{_libdir}/%{name}/readme
%{_libdir}/%{name}/features/org.eclipse.rcp_*
%{_libdir}/%{name}/features/org.eclipse.e4.rcp_*
%{_libdir}/%{name}/plugins/com.ibm.icu_*
%{_libdir}/%{name}/plugins/javax.inject_1.0.0.v20091030.jar
%{_libdir}/%{name}/plugins/javax.xml_1.3.4.v200806030440.jar
%{_libdir}/%{name}/plugins/org.apache.batik.css_*
%{_libdir}/%{name}/plugins/org.apache.batik.util.gui_*
%{_libdir}/%{name}/plugins/org.apache.batik.util_*
%{_libdir}/%{name}/plugins/org.apache.geronimo.specs.geronimo-annotation_1.1_spec_*
%{_libdir}/%{name}/plugins/org.eclipse.core.commands_*
%{_libdir}/%{name}/plugins/org.eclipse.core.contenttype_*
%{_libdir}/%{name}/plugins/org.eclipse.core.databinding_*
%{_libdir}/%{name}/plugins/org.eclipse.core.databinding.beans_*
%{_libdir}/%{name}/plugins/org.eclipse.core.databinding.observable_*
%{_libdir}/%{name}/plugins/org.eclipse.core.databinding.property_*
%{_libdir}/%{name}/plugins/org.eclipse.core.expressions_*
%{_libdir}/%{name}/plugins/org.eclipse.core.jobs_*
%{_libdir}/%{name}/plugins/org.eclipse.core.runtime_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.app_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.bidi_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.console_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.common_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.launcher_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.launcher.gtk.linux.*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.preferences_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.registry_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.util_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.core.commands_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.core.contexts_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.core.di.extensions_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.core.di_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.core.services_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.bindings_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.css.core_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.css.swt.theme_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.css.swt_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.di_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.model.workbench_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.services_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.widgets_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.workbench.addons.swt_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.workbench.renderers.swt_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.workbench.swt_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.workbench3_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.workbench_*
%{_libdir}/%{name}/plugins/org.eclipse.help_*
%{_libdir}/%{name}/plugins/org.eclipse.jface_*
%{_libdir}/%{name}/plugins/org.eclipse.jface.databinding_*
%{_libdir}/%{name}/plugins/org.eclipse.rcp_*
%{_libdir}/%{name}/plugins/org.eclipse.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.views_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.workbench_*
%{_libdir}/%{name}/plugins/org.eclipse.update.configurator_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.simpleconfigurator_*
%{_libdir}/%{name}/plugins/org.w3c.css.sac_*
%{_libdir}/%{name}/plugins/org.w3c.dom.svg_*
%dir %_libdir/eclipse/configuration/org.eclipse.osgi
# duplicates of swt
%exclude %_libdir/eclipse/configuration/org.eclipse.osgi/bundles/*/*/.cp/libswt-*.so

%if %{initialize}
%files platform -f %{name}-platform.install
%else
%files platform
%endif
%attr(0755,root,root) %{_bindir}/%{name}
%{_libdir}/%{name}/.eclipseproduct
%config %{_libdir}/%{name}/eclipse.ini
%config %{_sysconfdir}/eclipse.ini
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/*/*/apps/*
%{_libdir}/%{name}/eclipse
%dir %{_libdir}/%{name}/dropins
%dir %{_datadir}/%{name}/dropins
%{_libdir}/%{name}/features/org.eclipse.platform_*
%{_libdir}/%{name}/features/org.eclipse.e4.rcp_*
%{_libdir}/%{name}/plugins/com.jcraft.jsch_*
%{_libdir}/%{name}/plugins/org.eclipse.jdt.core_*
%{_libdir}/%{name}/plugins/javax.servlet_*
%{_libdir}/%{name}/plugins/javax.servlet.jsp_*
%{_libdir}/%{name}/plugins/javax.el_*
%{_libdir}/%{name}/plugins/javax.inject_1.0.0.v20091030.jar
%{_libdir}/%{name}/plugins/javax.xml_1.3.4.v200806030440.jar
%{_libdir}/%{name}/plugins/org.apache.tomcat_*
%{_libdir}/%{name}/plugins/org.apache.juli_*
%{_libdir}/%{name}/plugins/org.apache.el_*
%{_libdir}/%{name}/plugins/org.apache.ant_*
%{_libdir}/%{name}/plugins/org.apache.batik.css_*
%{_libdir}/%{name}/plugins/org.apache.batik.util.gui_*
%{_libdir}/%{name}/plugins/org.apache.batik.util_*
%{_libdir}/%{name}/plugins/org.apache.commons.codec_*
%{_libdir}/%{name}/plugins/org.apache.commons.el_*
%{_libdir}/%{name}/plugins/org.apache.commons.httpclient_*
%{_libdir}/%{name}/plugins/org.apache.commons.logging_*
%{_libdir}/%{name}/plugins/org.apache.felix.gogo.command_*
%{_libdir}/%{name}/plugins/org.apache.felix.gogo.runtime_*
%{_libdir}/%{name}/plugins/org.apache.felix.gogo.shell_*
%{_libdir}/%{name}/plugins/org.apache.geronimo.specs.geronimo-annotation_1.1_spec_*
%{_libdir}/%{name}/plugins/org.apache.lucene.core_*
%{_libdir}/%{name}/plugins/org.apache.lucene.analysis_*
%{_libdir}/%{name}/plugins/org.eclipse.ant.core_*
%{_libdir}/%{name}/plugins/org.eclipse.compare_*
%{_libdir}/%{name}/plugins/org.eclipse.compare.core_*
%{_libdir}/%{name}/plugins/org.eclipse.core.externaltools_*
%{_libdir}/%{name}/plugins/org.eclipse.core.filebuffers_*
%{_libdir}/%{name}/plugins/org.eclipse.core.filesystem_*
%{_libdir}/%{name}/plugins/org.eclipse.core.filesystem.linux.*
%{_libdir}/%{name}/plugins/org.eclipse.core.net_*
%{_libdir}/%{name}/plugins/org.eclipse.core.net.linux.*
%{_libdir}/%{name}/plugins/org.eclipse.core.resources_*
%{_libdir}/%{name}/plugins/org.eclipse.core.runtime.compatibility_*
%{_libdir}/%{name}/plugins/org.eclipse.core.runtime.compatibility.registry_*
%{_libdir}/%{name}/plugins/org.eclipse.core.variables_*
%{_libdir}/%{name}/plugins/org.eclipse.debug.core_*
%{_libdir}/%{name}/plugins/org.eclipse.debug.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.ds_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.event_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.http.jetty_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.http.registry_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.http.servlet_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.jsp.jasper_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.jsp.jasper.registry_*
%{_libdir}/%{name}/plugins/org.eclipse.help.base_*
%{_libdir}/%{name}/plugins/org.eclipse.help.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.help.webapp_*
%{_libdir}/%{name}/plugins/org.eclipse.jface.text_*
%{_libdir}/%{name}/plugins/org.eclipse.jsch.core_*
%{_libdir}/%{name}/plugins/org.eclipse.jsch.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.ltk.core.refactoring_*
%{_libdir}/%{name}/plugins/org.eclipse.ltk.ui.refactoring_*
%{_libdir}/%{name}/plugins/org.eclipse.osgi.services_*
%{_libdir}/%{name}/plugins/org.eclipse.osgi.util_*
%{_libdir}/%{name}/plugins/org.eclipse.platform_*
%{_libdir}/%{name}/plugins/org.eclipse.platform.doc.user_*
%{_libdir}/%{name}/plugins/org.eclipse.search_*
%{_libdir}/%{name}/plugins/org.eclipse.team.core_*
%{_libdir}/%{name}/plugins/org.eclipse.team.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.text_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.browser_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.cheatsheets_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.console_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.editors_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.externaltools_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.forms_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.ide_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.ide.application_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.intro_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.intro.universal_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.navigator_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.navigator.resources_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.net_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.views_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.views.properties.tabbed_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.workbench.texteditor_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.core.commands_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.core.contexts_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.core.di.extensions_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.core.di_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.core.services_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.bindings_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.css.core_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.css.swt.theme_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.css.swt_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.di_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.model.workbench_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.services_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.widgets_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.workbench.addons.swt_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.workbench.renderers.swt_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.workbench.swt_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.workbench3_*
%{_libdir}/%{name}/plugins/org.eclipse.e4.ui.workbench_*
%{_libdir}/%{name}/plugins/org.eclipse.jetty.util_*
%{_libdir}/%{name}/plugins/org.eclipse.jetty.server_*
%{_libdir}/%{name}/plugins/org.eclipse.jetty.http_*
%{_libdir}/%{name}/plugins/org.eclipse.jetty.continuation_*
%{_libdir}/%{name}/plugins/org.eclipse.jetty.io_*
%{_libdir}/%{name}/plugins/org.eclipse.jetty.security_*
%{_libdir}/%{name}/plugins/org.eclipse.jetty.servlet_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.initializer_*
%{_libdir}/%{name}/plugins/org.eclipse.team.cvs.core_*
%{_libdir}/%{name}/plugins/org.eclipse.cvs_*
%{_libdir}/%{name}/plugins/org.eclipse.team.cvs.ssh2_*
%{_libdir}/%{name}/plugins/org.eclipse.team.cvs.ui_*
%{_libdir}/%{name}/features/org.eclipse.cvs_*
%{_libdir}/%{name}/features/org.eclipse.help_*
%{_libdir}/%{name}/plugins/org.apache.jasper_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.frameworkadmin_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.frameworkadmin.equinox_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.simpleconfigurator.manipulator_*
%{_libdir}/%{name}/features/org.eclipse.equinox.p2.core.feature_*
%{_libdir}/%{name}/features/org.eclipse.equinox.p2.extras.feature_*
%{_libdir}/%{name}/features/org.eclipse.equinox.p2.rcp.feature_*
%{_libdir}/%{name}/features/org.eclipse.equinox.p2.user.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.director_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.core_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.engine_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.jarprocessor_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.metadata_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.metadata.repository_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.artifact.repository_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.touchpoint.eclipse_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.touchpoint.natives_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.console_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.ql_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.operations_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.transport.ecf_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.ui.importexport_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.ui.sdk_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.ui.sdk.scheduler_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.updatechecker_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.garbagecollector_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.directorywatcher_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.publisher_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.publisher.eclipse_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.repository_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.repository.tools_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.reconciler.dropins_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.updatesite_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.security_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.security.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.extensionlocation_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.director.app_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.provider.filetransfer_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.provider.filetransfer.httpclient_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.provider.filetransfer.httpclient.ssl_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.provider.filetransfer.ssl_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.ssl_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.filetransfer_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.identity_*
%{_libdir}/%{name}/plugins/org.sat4j.core_*
%{_libdir}/%{name}/plugins/org.sat4j.pb_*
%{_libdir}/%{name}/plugins/org.w3c.css.sac_*
%{_libdir}/%{name}/plugins/org.w3c.dom.svg_*
%{_libdir}/%{name}/plugins/org.eclipse.emf.common_*
%{_libdir}/%{name}/plugins/org.eclipse.emf.ecore.change_*
%{_libdir}/%{name}/plugins/org.eclipse.emf.ecore.xmi_*
%{_libdir}/%{name}/plugins/org.eclipse.emf.ecore_*
%{_libdir}/%{name}/features/org.eclipse.emf.common_*
%{_libdir}/%{name}/features/org.eclipse.emf.ecore_*

# Put this in -platform since we're putting the p2 stuff here
%{_libdir}/%{name}/artifacts.xml
# FIXME: should we ship content.xml for the platform?
#%%{_libdir}/%%{name}/metadata
%{_libdir}/%{name}/p2
%{_javadir}/%{name}/equinox.http.servlet.jar
%{_mavenpomdir}/JPP.%{name}-equinox.http.servlet.pom
%{_mavendepmapfragdir}/%{name}-platform

%files jdt
%attr(0755,root,root) %{_bindir}/efj
%{_libdir}/%{name}/dropins/jdt
%{_javadir}/%{name}/jdt.core.jar
%{_mavenpomdir}/JPP.%{name}-jdt.core.pom
%{_mavendepmapfragdir}/%{name}-jdt

%files pde
%{_bindir}/%{name}-pdebuild
%{_libdir}/%{name}/buildscripts
%{_libdir}/%{name}/dropins/sdk

%files equinox-osgi
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/osgi.jar
%{_javadir}/%{name}/osgi.services.jar
%{_javadir}/%{name}/osgi.util.jar
%{_libdir}/%{name}/plugins/org.eclipse.osgi_*
%{_libdir}/%{name}/plugins/org.eclipse.osgi.services_*
%{_libdir}/%{name}/plugins/org.eclipse.osgi.util_*
%{_mavenpomdir}/JPP.%{name}-osgi*.pom
%{_mavendepmapfragdir}/%{name}-equinox-osgi

%changelog
* Fri Jan 03 2014 Paul Wolneykien <manowar@altlinux.ru> 1:4.2.0-alt7_7jpp7
- Fix the Eclipse bug #383189 (patch).

* Sat Jul 27 2013 Paul Wolneykien <manowar@altlinux.ru> 1:4.2.0-alt6_7jpp7
- Fix the WebKitGTK crash in libsoup (patch).

* Fri Apr 19 2013 Igor Vlasenko <viy@altlinux.ru> 1:4.2.0-alt5_7jpp7
- fixed build

* Sat Sep 29 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.2.0-alt4_7jpp7
- build with lucene3

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.2.0-alt3_7jpp7
- fixed geronimo-*api dependencies

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.2.0-alt2_7jpp7
- restored internal emf

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.2.0-alt1_8jpp7
- use external emf-core

* Tue Aug 21 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.2.0-alt1_7jpp7
- new version

* Tue Oct 18 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.7.0-alt3_3jpp6
- bumped release for t6 update

* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.7.0-alt2_3jpp6
- fixed jdt bin permissions

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.7.0-alt1_3jpp6
- update to new release by jppimport

* Thu Apr 28 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.6.2-alt1_2jpp6
- new version

* Tue Apr 05 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.6.1-alt2_6.1jpp6
- BR: cleanup

* Sun Feb 27 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.6.1-alt1_6.1jpp6
- new version

* Fri Dec 17 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt4_2jpp6
- dropped wide dependency on xulrunner (closes: #23263)

* Sat Dec 11 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt3_2jpp6
- fixed linkage of swt-atk

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt2_2jpp6
- bugfix release

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt1_2jpp6
- new version

* Thu Feb 18 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.5.1-alt2_28jpp6
- removed auto python deps

* Sat Feb 06 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.5.1-alt1_28jpp6
- build with xulrunner 192

* Tue Jan 26 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.5.1-alt1_21jpp6
- new version

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.4.1-alt7_5jpp6.1
- Rebuilt with python 2.6

* Thu Mar 19 2009 Igor Vlasenko <viy@altlinux.ru> 1:3.4.1-alt7_5jpp6
- obsoletes ecj again
- eclipse-ecj now has no osgi provides

* Sun Feb 22 2009 Igor Vlasenko <viy@altlinux.ru> 1:3.4.1-alt6_5jpp6
- no more obsoletes ecj
- brand new splash screen (Stanislav Yadykin artwork)

* Thu Jan 15 2009 Igor Vlasenko <viy@altlinux.ru> 1:3.4.1-alt5_5jpp6
- bugfixs; use icu4j, properly conflicts mozilla

* Tue Jan 13 2009 Igor Vlasenko <viy@altlinux.ru> 1:3.4.1-alt4_5jpp6
- first 3.4.x production build

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 1:3.4.1-alt3_5jpp6
- disabled osgi requires on ecj

* Thu Dec 25 2008 Igor Vlasenko <viy@altlinux.ru> 1:3.4.1-alt2_5jpp6
- new version

* Mon Dec 22 2008 Igor Vlasenko <viy@altlinux.ru> 1:3.4.1-alt1_5jpp6
- new version

* Sat Aug 09 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.3.2-alt2_12jpp6
- obsoletes ecj; ecj,cvs,jdt made noarches.

* Sun Jul 27 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.3.2-alt1_12jpp6
- new version

* Mon Apr 14 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.3.0-alt7_31jpp5.0
- build in debug mode (no stripping yet).
- fixed help browser

* Sat Mar 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.3.0-alt7_30jpp5.0
- build in debug mode (no stripping yet).
- rebuild with fresh tomcat5 build

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.3.0-alt6_30jpp5.0
- build in debug mode (no stripping yet).
- fixed lucene issues

* Thu Dec 20 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.3.0-alt5_30jpp5.0
- based on 3.3.0-30; build in debug mode (no stripping yet).
- work towards help browser; help search now works;
- added extra ant tasks

* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.3.0-alt4_30jpp5.0
- based on 3.3.0-30; build in debug mode (no stripping yet).
- help browser does not work
- fixed explicit requires

* Fri Dec 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.3.0-alt3_30jpp5.0
- based on 3.3.0-30; build in debug mode (no stripping yet).
- help browser does not work
- added explicit requires; removed conflict with mozilla (no more present in repo).

* Thu Dec 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.3.0-alt2_30jpp5.0
- based on 3.3.0-30; build in debug mode (no stripping yet).
- embedded firefox bug is still present

* Tue Dec 11 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.3.0-alt2_11jpp5.0
- based on 3.3.0-11; build in debug mode (no stripping yet).
- embedded firefox bug is still present

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.3.0-alt2_5jpp5.0
- based on 3.3.0-5; build in debug mode (no stripping yet).
- fixed double free on exit bug

* Wed Nov 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.3.0-alt1_5jpp5.0
- build for ALTLinux; based on 3.3.0-5
- build in debug mode (no stripping yet). fixed build on ix86

* Tue Nov 20 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.3.0-alt1_5jpp1.7
- build for ALTLinux; based on 3.3.0-5
- build in debug mode (no stripping yet).

* Sun Dec 18 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.1.1-alt2
- Corrected XSLT in eclipse-list-feature-plugins.xsl
- Patch2: merged Patch3 in; use pkg-config to get Gecko flags

* Wed Oct 05 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.1.1-alt1
- 3.1.1
- Updated Patch4 from Eclipse bug #106527
- Reordered application of patches to occur after any source unpacking,
  original or not
- Updated Patch0
- Use get_version instead of homegrown macros
- Use the Ant XSLT task instead of xsltproc
- Joined swt-cairo up to swt, as GTK+ is now dependant on Cairo anyway
- Do insertBuildId target to provide build tags

* Sat Aug 27 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.1-alt2
- Rebuilt with new cairo
- Patch4: Port to the new Cairo API from Eclipse bug #106527

* Mon Aug 01 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.1-alt1
- Updated to 3.1
- Brought SWT back under the source RPM umbrella, albeit in externalized form
- Support x86_64 build
- Added eclipse-rcp and eclipse-rcp-source packages
- Added eclipse-common to hold installation directories
  and serve as the dependency root
- Added desktop entry (bug #6441)

* Sun Jan 09 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.0.1-alt1
- Updated to 3.0.1
- Externalized SWT and third-party JARs
- Restructured packages to meet changed feature layout

* Fri Apr 04 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.1-alt1
- Initial release
- Major above-platform features ripped out to be subpackages
- The native module depending on GNOME is a subpackage too
