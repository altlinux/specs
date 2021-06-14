Group: Networking/WWW
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
%def_disable javaws
%def_enable moz_plugin
BuildRequires(pre): browser-plugins-npapi-devel
BuildRequires: bc

%set_compress_method none
%define oldname icedtea-web
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#can rust have debuginfo? Verify and fix! Likely issue in Makefile of itw.
%global debug_package %{nil}

# Version of java we run against
%define javaver 1.8.0
# Version of java we build by
%define buildjavaver 1.8.0

# Alternatives priority (rised by one number when jre bumped to 11 (as 11 < 18 :)
%define priority 110000
# jnlp prorocol gnome registry keys
%define gurlhandler   /desktop/gnome/url-handlers
%define jnlphandler   %{gurlhandler}/jnlp
%define jnlpshandler  %{gurlhandler}/jnlps

%define jredir      %{_jvmdir}/jre-%{javaver}-openjdk
%define sdkdir      %{_jvmdir}/java-%{buildjavaver}-openjdk

%define preffered_jre  java-%{javaver}-openjdk
%define preffered_jdk  java-%{buildjavaver}-openjdk-devel

Name:		mozilla-plugin-java-1.8.0-openjdk
Version:	2.0.0
Release:	alt2_pre.0.3.alpha16.patched1.3jpp8
Summary:	Additional Java components for OpenJDK - Java Web Start implementation

License:    LGPLv2+ and GPLv2 with exceptions
URL:        https://openwebstart.com/
Source0:    https://github.com/AdoptOpenJDK/IcedTea-Web/archive/%{oldname}-%{version}-alpha16.tar.gz
Patch0:     patchOutDunce.patch
Patch1:     launchersPhase.patch
# this should be upstreamed. In build tasks which lauches java are using runtime JRE, should beusing SDK, but there is no place where to set it
Patch2:     usePathJdkForDifferentBuildAndRuntimeJre.patch
Patch3:     altjava.patch

BuildRequires:  javapackages-tools
#for deprecated add_maven_depmap, see https://www.spinics.net/lists/fedora-devel/msg233211.html
BuildRequires:  javapackages-local
BuildRequires:  %{preffered_jdk}
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel libgio libgio-devel
BuildRequires:  dos2unix
BuildRequires:	rust
BuildRequires:	rust-cargo
BuildRequires:  junit
BuildRequires:  maven
BuildRequires:  hamcrest
BuildRequires:  libappstream-glib
BuildRequires:  tagsoup
BuildRequires:  maven-local
# have to remove them at the end, what is the result?
BuildRequires:  buildnumber-maven-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  exec-maven-plugin
BuildRequires:  hamcrest
BuildRequires:  hamcrest-core
BuildRequires:  rhino
BuildRequires:  IPAddress
BuildRequires:  maven-javadoc-plugin

# For functionality and the OpenJDK dirs
Requires:      %{preffered_jre}
Requires:      javapackages-tools
Requires:      rhino
Requires:      IPAddress

#maven fragments
Requires(post):      javapackages-tools
Requires(postun):    javapackages-tools

# When itw builds against it, it have to be also in runtime
Requires:      tagsoup

# Post requires alternatives to install tool alternatives.
# jnlp protocols support
Requires(post):   GConf libGConf
# Postun requires alternatives to uninstall tool alternatives.
# jnlp protocols support
Requires(postun):   GConf libGConf

# Standard JPackage plugin provides.
Provides: javaws = 1:%{javaver}
Provides: %{preffered_jre}-javaws = 1:%{version}
Source44: import.info

%define altname java-%{javaver}-openjdk
%define origin openjdk
%define label -itweb
%define javaws_ver      %{javaver}
%define sdkdir          java-%{javaver}-openjdk-%{javaver}.0.%{_arch}
# TODO: move here
#define mozilla_java_plugin_so %{_prefix}/lib/%{sdkdir}/IcedTeaPlugin.so
%define mozilla_java_plugin_so %{_libdir}/IcedTeaPlugin.so

# hack not to forget to rebuild this pkg with every new openjdk
# JAVACANDIDATE in alternatives below is release-dependent :(
%define _alt_javacandidate %(head -2 /etc/alternatives/packages.d/java-%{javaver}-openjdk-java-headless| tail -1 | awk '{print $3}')
%if "%{_alt_javacandidate}" != ""
Requires: %{_alt_javacandidate}
%endif
Provides: icedtea-web = %version-%release
Obsoletes: mozilla-plugin-java-1.7.0-openjdk < 1.5
Patch33: translation-desktop-files.patch
Source45: Messages_ru.properties

#BuildRequires: java-%javaver-%origin-devel

%description
The IcedTea-Web project provides a an implementation of Java Web Start
(originally based on the Netx project, now opensource part of OpenWebStart)
and a settings tool to manage deployment settings for the aforementioned 
Web Start implementations. 

%if_enabled javaws
%package -n %altname-javaws
Summary: Java Web Start
Group: Networking/Other
Requires: %name = %version-%release
Requires(post,preun): alternatives
# --- jpackage compatibility stuff starts here ---
Provides:       javaws = %{javaws_ver}
Obsoletes:      javaws-menu
#Obsoletes:      java-1.7.0-openjdk-javaws
#Obsoletes:      mozilla-plugin-java-1.7.0-openjdk
# --- jpackage compatibility stuff ends here ---
# due to the build specific
Requires: mozilla-plugin-%altname = %version-%release

%description -n %altname-javaws
Java Web Start is a deployment solution for Java-technology-based
applications. It is the plumbing between the computer and the Internet
that allows the user to launch and manage applications right off the
Web. Java Web Start provides easy, one-click activation of
applications, and guarantees that you are always running the latest
version of the application, eliminating complicated installation or
upgrade procedures.

This package provides the Java Web Start installation that is bundled
with %{name} J2SE Runtime Environment.
%endif # enabled javaws

%package javadoc
Group: Development/Java
Summary:    API documentation for IcedTea-Web
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch

%description javadoc
This package contains Javadocs for the IcedTea-Web project.


%package devel
Group: Development/Java
Summary:    pure sources for debugging IcedTea-Web
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch

%description devel
This package contains ziped sources of the IcedTea-Web project.

%prep
%setup -q -n IcedTea-Web-icedtea-web-2.0.0-alpha16
%patch0 -p1
dos2unix launchers/pom.xml
%patch1 -p0
%patch2 -p1
%patch3 -p1

%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-surefire-plugin
%pom_add_plugin org.apache.maven.plugins:maven-install-plugin:2.5.2
%pom_remove_dep junit:junit common/pom.xml
%pom_remove_dep org.hamcrest:hamcrest common/pom.xml

%pom_remove_dep org.hamcrest:hamcrest test-extensions/pom.xml
%pom_remove_dep net.jcip:jcip-annotations test-extensions/pom.xml
%pom_remove_dep com.github.stefanbirkner:system-rules test-extensions/pom.xml

%pom_remove_dep com.github.vatbub:mslinks core/pom.xml
%pom_remove_dep org.hamcrest:hamcrest integration/pom.xml
%pom_remove_dep com.github.tomakehurst:wiremock-jre8 integration/pom.xml
%pom_remove_dep com.github.stefanbirkner:system-rules integration/pom.xml

%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin common/pom.xml
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin core/pom.xml
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin test-extensions/pom.xml
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin xml-parser/pom.xml
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin pom.xml

rm -v core/src/main/java/net/sourceforge/jnlp/util/WindowsDesktopEntry.java
rm -r integration/src
%patch33 -p2
# not updated for 2.0 yet
#cp -f %SOURCE45 common/src/main/resources/net/adoptopenjdk/icedteaweb/i18n/Messages_ru.properties
#sed -i 's/en_US.UTF-8/en_US.UTF-8 ru_RU.UTF-8/' Makefile.am


%build
rm -rf launchers/build.log
#export JAVA_HOME=%{sdkdir}
SPLASH_TARGET_DIR=%{_datadir}/%{oldname} \
ITW_TARGET_DIR=%{_datadir}/%{oldname} \
BIN_TARGET_DIR=%{_libexecdir}/%{oldname} \
ETC_TARGET_DIR=%{_sysconfdir}/java/%{oldname} \
ITW_LIBS=DISTRIBUTION \
JRE=%{jredir} \
%mvn_build -- -Plaunchers -Dmaven.test.skip=true -Dmaven.javadoc.skip=true   || cat launchers/build.log
cat launchers/build.log

%install
#not installing all, itw is comlex maven project, wfrom which we need onlythe finall jar, without system deps
%mvn_artifact pom.xml launchers/target//usr/share/icedtea-web/javaws.jar

mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{oldname}
# build provides also .bat files, we do not want them
cp -v launchers/target/%{_libexecdir}/%{oldname}/javaws $RPM_BUILD_ROOT%{_libexecdir}/%{oldname}/
cp -v launchers/target/%{_libexecdir}/%{oldname}/itweb-settings $RPM_BUILD_ROOT%{_libexecdir}/%{oldname}/
cp -v launchers/target/%{_libexecdir}/%{oldname}/policyeditor $RPM_BUILD_ROOT%{_libexecdir}/%{oldname}/
cp -v launchers/target/%{_libexecdir}/%{oldname}/javaws.sh $RPM_BUILD_ROOT%{_libexecdir}/%{oldname}/
cp -v launchers/target/%{_libexecdir}/%{oldname}/itweb-settings.sh $RPM_BUILD_ROOT%{_libexecdir}/%{oldname}/
cp -v launchers/target/%{_libexecdir}/%{oldname}/policyeditor.sh $RPM_BUILD_ROOT%{_libexecdir}/%{oldname}/

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/java/%{oldname}/
cp -v launchers/target/%{_sysconfdir}/java/%{oldname}/itw-modularjdk.args $RPM_BUILD_ROOT%{_sysconfdir}/java/%{oldname}/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{oldname}
cp -v launchers/target/%{_datadir}/%{oldname}/* $RPM_BUILD_ROOT%{_datadir}/%{oldname}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/
cp -v launchers/target/extensions/bash_completion.d/* $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/
cp -r launchers/target/icedtea-web-docs/2.0.0-alpha16/man/* $RPM_BUILD_ROOT/%{_mandir}/
# rename javaws so it can coexists with other implementations
mv $RPM_BUILD_ROOT/%{_mandir}/man1/javaws.1 $RPM_BUILD_ROOT/%{_mandir}/man1/javaws.itweb.1
mv $RPM_BUILD_ROOT/%{_mandir}/cs/man1/javaws.1 $RPM_BUILD_ROOT/%{_mandir}/cs/man1/javaws.itweb.1
mv $RPM_BUILD_ROOT/%{_mandir}/de/man1/javaws.1 $RPM_BUILD_ROOT/%{_mandir}/de/man1/javaws.itweb.1
mv $RPM_BUILD_ROOT/%{_mandir}/pl/man1/javaws.1 $RPM_BUILD_ROOT/%{_mandir}/pl/man1/javaws.itweb.1

# Install desktop files.
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
desktop-file-install --vendor '' --dir $RPM_BUILD_ROOT%{_datadir}/applications launchers/target/extensions/xdesktop/javaws.desktop
desktop-file-install --vendor '' --dir $RPM_BUILD_ROOT%{_datadir}/applications launchers/target/extensions/xdesktop/itweb-settings.desktop
desktop-file-install --vendor '' --dir $RPM_BUILD_ROOT%{_datadir}/applications launchers/target/extensions/xdesktop/policyeditor.desktop
cp launchers/target/libs/javaws.png $RPM_BUILD_ROOT%{_datadir}/pixmaps

# install MetaInfo file for javaws
DESTDIR=%{buildroot} appstream-util install launchers/metadata/%{oldname}-javaws.appdata.xml

# maven fragments generation
mkdir -p $RPM_BUILD_ROOT%{_javadir}
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -s ../%{oldname}/javaws.jar %{oldname}.jar
popd
mkdir -p $RPM_BUILD_ROOT/%{_mavenpomdir}
cp pom.xml  $RPM_BUILD_ROOT/%{_mavenpomdir}/%{oldname}.pom

%mvn_artifact $RPM_BUILD_ROOT/%{_mavenpomdir}/%{oldname}.pom $RPM_BUILD_ROOT/%{_javadir}/%{oldname}.jar

%find_lang %{oldname} --all-name --with-man


##################################################
# --- alt linux specific, shared with openjdk ---#
##################################################
%if_enabled moz_plugin
# ControlPanel freedesktop.org menu entry
cat >> $RPM_BUILD_ROOT%{_desktopdir}/%{altname}-control-panel.desktop << EOF
[Desktop Entry]
Name=Java %javaver Plugin Control Panel
Comment=Java Control Panel
Exec=itweb-settings.itweb
Icon=java-%{javaver}
Terminal=false
Type=Application
Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
%endif

%if_enabled javaws
# javaws freedesktop.org menu entry
cat >> $RPM_BUILD_ROOT%{_desktopdir}/%{altname}-javaws.desktop << EOF
[Desktop Entry]
Name=Java Web Start (%{javaver})
Comment=Java Application Launcher
MimeType=application/x-java-jnlp-file;
Exec=javaws.itweb %%u
Icon=java-%{javaver}
Terminal=false
Type=Application
Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
%endif


JAVACANDIDATE=`head -2 /etc/alternatives/packages.d/java-%{javaver}-openjdk-java-headless| tail -1 | awk '{print $3}'`
[ -n "JAVACANDIDATE" ] || exit 1

install -d %buildroot%_altdir
%if_enabled moz_plugin
# Mozilla plugin alternative
%__cat <<EOF >%buildroot%_altdir/%altname-plugin
%browser_plugins_path/libjavaplugin_oji.so	%mozilla_java_plugin_so	%priority
EOF
%__cat <<EOF >>%buildroot%_altdir/%altname-plugin
%{_bindir}/ControlPanel	%_bindir/itweb-settings.itweb	$JAVACANDIDATE
%{_bindir}/jcontrol	%_bindir/itweb-settings.itweb	$JAVACANDIDATE
EOF
%endif

%if_enabled javaws
# Java Web Start alternative
cat <<EOF >%buildroot%_altdir/%altname-javaws
%_bindir/javaws	%_bindir/javaws.itweb	$JAVACANDIDATE
%_man1dir/javaws.1.gz	%_man1dir/javaws%label.1.gz	$JAVACANDIDATE
EOF
# ----- JPackage compatibility alternatives ------
%__cat <<EOF >>%buildroot%_altdir/%altname-javaws
%{_datadir}/javaws	%_bindir/javaws.itweb	$JAVACANDIDATE
EOF
# ----- end: JPackage compatibility alternatives ------
%endif	# enabled javaws

# hack (see #11383) to enshure that all man pages will be compressed
for i in $RPM_BUILD_ROOT%_man1dir/*.1; do
    [ -f $i ] && gzip -9 $i
done

##################################################
# - END alt linux specific, shared with openjdk -#
##################################################

%files -f %{oldname}.lang
%{_sysconfdir}/bash_completion.d/*
%config(noreplace) %{_sysconfdir}/java/%{oldname}/itw-modularjdk.args
%{_libexecdir}/%{oldname}/*
%{_datadir}/applications/*
%dir %{_datadir}/%{oldname}
%{_datadir}/%{oldname}/*.jar
%{_datadir}/java/%{oldname}.jar
%{_datadir}/maven-poms/%{oldname}.pom
%{_datadir}/%{oldname}/*.png
%{_datadir}/man/man1/*
%{_datadir}/pixmaps/*
%{_datadir}/appdata/*.xml
%doc README.md CONTRIBUTING.md
%doc --no-dereference LICENSE LICENCE_DETAILS.md
# alt linux specific
%_altdir/%altname-plugin
%{_desktopdir}/%{altname}-control-panel.desktop
# replace by local variants
%exclude %{_desktopdir}/itweb-settings.desktop
%if_enabled javaws
%exclude %{_desktopdir}/javaws.desktop
# separate javaws
%exclude %{_desktopdir}/%{altname}-javaws.desktop
%exclude %{_datadir}/pixmaps/javaws.png
%exclude %{_man1dir}/javaws.itweb.1.gz
%exclude %_bindir/javaws.itweb
%endif



%changelog
* Mon Jun 14 2021 Igor Vlasenko <viy@altlinux.org> 2.0.0-alt2_pre.0.3.alpha16.patched1.3jpp8
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.0.0-alt1_pre.2.alpha13.patched1jpp8
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1_3jpp8
- new version

* Tue Jun 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_2jpp8
- restored Ivan Razzhivin patches

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_1jpp8
- new version

* Wed Jan 09 2019 Ivan Razzhivin <underwit@altlinux.org> 1.7.1-alt5_6jpp8
- fix russian translation

* Fri Dec 07 2018 Ivan Razzhivin <underwit@altlinux.org> 1.7.1-alt4_6jpp8
- add russian translation to desktop files

* Thu Nov 15 2018 Ivan Razzhivin <underwit@altlinux.org> 1.7.1-alt3_6jpp8
- add russian translation

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt2_6jpp8
- fixed alternatives

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1_6jpp8
- fixed icons in desktop files

* Thu Jun 21 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1_5jpp8
- new version

* Sat Apr 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt3_1jpp8
- removed fedora-based alternative (closes: #32043)

* Fri Mar 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_1jpp8
- fixed requires

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_1jpp8
- new version

