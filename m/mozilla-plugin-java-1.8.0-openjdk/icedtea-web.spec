# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install gcc-c++
# END SourceDeps(oneline)
%def_enable javaws
%def_enable moz_plugin
BuildRequires(pre): browser-plugins-npapi-devel
%set_compress_method none
%filter_from_requires /^java-headless/d
%define oldname icedtea-web
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# Version of java
%define javaver 1.8.0

# Alternatives priority
%define priority 18000

%define javadir     %{_jvmdir}/java-openjdk
%define jredir      %{_jvmdir}/jre-openjdk
%define javaplugin  libjavaplugin.so.%{_arch}

%define binsuffix      .itweb

Name:		mozilla-plugin-java-1.8.0-openjdk
Version:	1.6.2
Release:	alt2_1jpp8
Summary:	Additional Java components for OpenJDK - Java browser plug-in and Web Start implementation

Group:      Networking/WWW
License:    LGPLv2+ and GPLv2 with exceptions
URL:        http://icedtea.classpath.org/wiki/IcedTea-Web
Source0:    http://icedtea.classpath.org/download/source/%{oldname}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  java-%{javaver}-openjdk-devel
BuildRequires:  desktop-file-utils
BuildRequires:  xulrunner-devel
BuildRequires:  glib2-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  xulrunner-devel
BuildRequires:  junit
BuildRequires:  hamcrest
BuildRequires:  libappstream-glib
# new in 1.5 to have  clean up for malformed XMLs
BuildRequires:  tagsoup
# rhino is used as JS evaluator in testtime
BuildRequires:      rhino

# For functionality and the OpenJDK dirs
Requires:      java-%{javaver}-openjdk
#maven fragments

# For the mozilla plugin dir
Requires:       browser-plugins-npapi

# When itw builds against it, it have to be also in runtime
Requires:      tagsoup

# rhino is used as JS evaluator in runtime
Requires:      rhino

# Post requires alternatives to install plugin alternative.

# Postun requires alternatives to uninstall plugin alternative.

# Standard JPackage plugin provides.
Provides: java-plugin = 1:%{javaver}
Provides: javaws = 1:%{javaver}

Provides:   java-%{javaver}-openjdk-plugin = 1:%{version}
Source44: import.info

%define altname java-%{javaver}-openjdk
%define origin openjdk
%define label -itweb
%define javaws_ver      %{javaver}
%define sdkdir          java-%{javaver}-openjdk-%{javaver}.0.%{_arch}
# TODO: move here
#define mozilla_java_plugin_so %{_prefix}/lib/%{sdkdir}/IcedTeaPlugin.so
%define mozilla_java_plugin_so %{_libdir}/IcedTeaPlugin.so
Provides: icedtea-web = %version-%release
Obsoletes: mozilla-plugin-java-1.7.0-openjdk < 1.5
#BuildRequires: java-%javaver-%origin-devel

%description
The IcedTea-Web project provides a Java web browser plugin, an implementation
of Java Web Start (originally based on the Netx project) and a settings tool to
manage deployment settings for the aforementioned plugin and Web Start
implementations. 

%if_enabled javaws
%package -n %altname-javaws
Summary: Java Web Start
Group: Networking/Other
Requires: %name = %version-%release
Requires(post,preun): alternatives
# --- jpackage compatibility stuff starts here ---
Provides:       javaws = %{javaws_ver}
Obsoletes:      javaws-menu
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
Summary:    API documentation for IcedTea-Web
Group:      Development/Java
Requires:   %{name} = %{version}
BuildArch:  noarch

%description javadoc
This package contains Javadocs for the IcedTea-Web project.

%prep
%setup -n %{oldname}-%{version} -q

%build
autoreconf -vfi
CXXFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS" \
%configure \
    --with-pkgversion=ALTLinux-%{release}-%{_arch} \
    --docdir=%{_datadir}/javadoc/%{oldname} \
    --with-jdk-home=%{javadir} \
    --with-jre-home=%{jredir} \
    --libdir=%{_libdir} \
    --program-suffix=%{binsuffix} \
    --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# icedteaweb-completion is currently not handled by make nor make install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/
cp icedteaweb-completion $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/

# Move javaws man page to a more specific name
mv $RPM_BUILD_ROOT/%{_mandir}/man1/javaws.1 $RPM_BUILD_ROOT/%{_mandir}/man1/javaws-itweb.1

# Install desktop files.
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
desktop-file-install --vendor ''\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications javaws.desktop
desktop-file-install --vendor ''\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications itweb-settings.desktop
desktop-file-install --vendor ''\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications policyeditor.desktop

# install MetaInfo file for firefox
DESTDIR=%{buildroot} appstream-util install metadata/%{oldname}.metainfo.xml
# install MetaInfo file for javaws
DESTDIR=%{buildroot} appstream-util install metadata/%{oldname}-javaws.appdata.xml

# maven fragments generation
mkdir -p $RPM_BUILD_ROOT%{_javadir}
pushd $RPM_BUILD_ROOT%{_javadir}
ln -s ../%{oldname}/netx.jar %{oldname}.jar
ln -s ../%{oldname}/plugin.jar %{oldname}-plugin.jar
popd
mkdir -p $RPM_BUILD_ROOT/%{_mavenpomdir}
cp  metadata/%{oldname}.pom  $RPM_BUILD_ROOT/%{_mavenpomdir}/%{oldname}.pom
cp metadata/%{oldname}-plugin.pom  $RPM_BUILD_ROOT/%{_mavenpomdir}/%{oldname}-plugin.pom

%add_maven_depmap %{oldname}.pom %{oldname}.jar
%add_maven_depmap %{oldname}-plugin.pom %{oldname}-plugin.jar
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/%{javaplugin}_icedtea-web<<EOF
%{_libdir}/mozilla/plugins/libjavaplugin.so	%{_libdir}/IcedTeaPlugin.so	%{priority}
%{_bindir}/javaws	%{_prefix}/bin/javaws%{binsuffix}	%{_libdir}/IcedTeaPlugin.so
%{_mandir}/man1/javaws.1.gz	%{_mandir}/man1/javaws-itweb.1.gz	%{_libdir}/IcedTeaPlugin.so
EOF

install -d -m 755 %buildroot/etc/icedtea-web
cat > %buildroot/etc/icedtea-web/javaws.policy << EOF
// Based on Oracle JDK policy file
grant codeBase "file:/usr/share/icedtea-web/netx.jar" {
    permission java.security.AllPermission;
};
EOF
sed -e 's,^JAVA_ARGS=,JAVA_ARGS="-Djava.security.policy=/etc/icedtea-web/javaws.policy",' \
%buildroot%_bindir/javaws.itweb


##################################################
# --- alt linux specific, shared with openjdk ---#
##################################################
%if_enabled moz_plugin
# ControlPanel freedesktop.org menu entry
cat >> $RPM_BUILD_ROOT%{_desktopdir}/%{altname}-control-panel.desktop << EOF
[Desktop Entry]
Name=Java Plugin Control Panel (%{name})
Comment=Java Control Panel
Exec=itweb-settings.itweb
Icon=%{name}
Terminal=false
Type=Application
Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
%endif

%if_enabled javaws
# javaws freedesktop.org menu entry
cat >> $RPM_BUILD_ROOT%{_desktopdir}/%{altname}-javaws.desktop << EOF
[Desktop Entry]
Name=Java Web Start (%{name})
Comment=Java Application Launcher
MimeType=application/x-java-jnlp-file;
Exec=javaws.itweb %%u
Icon=%{name}
Terminal=false
Type=Application
Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
%endif


JAVACANDIDATE=`head -2 /etc/alternatives/packages.d/java-%{javaver}-openjdk-java| tail -1 | awk '{print $3}'`

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



%check
make check
appstream-util validate $RPM_BUILD_ROOT/%{_datadir}/appdata/*.xml || :

%files -f .mfiles
%_altdir/%{javaplugin}_icedtea-web
%{_sysconfdir}/bash_completion.d/icedteaweb-completion
%{_prefix}/bin/*
%{_libdir}/IcedTeaPlugin.so
%{_datadir}/applications/*
%{_datadir}/%{oldname}
%{_datadir}/man/man1/*
%{_datadir}/man/cs/man1/*
%{_datadir}/man/de/man1/*
%{_datadir}/man/pl/man1/*
%{_datadir}/pixmaps/*
%{_datadir}/appdata/*.xml
%doc NEWS README COPYING
# alt linux specific
%_altdir/%altname-plugin
%{_desktopdir}/%{altname}-control-panel.desktop
# replace by local variants
%exclude %{_desktopdir}/javaws.desktop
%exclude %{_desktopdir}/itweb-settings.desktop
# separate javaws
%exclude %{_desktopdir}/%{altname}-javaws.desktop
%exclude %{_datadir}/pixmaps/javaws.png
%exclude %{_man1dir}/javaws-itweb.1.gz
%exclude %_bindir/javaws.itweb
# security policy
%dir /etc/icedtea-web
/etc/icedtea-web/javaws.policy

%files javadoc
%{_datadir}/javadoc/%{oldname}
%doc COPYING

%files -n %altname-javaws
#
%_altdir/%altname-javaws
%{_desktopdir}/%{altname}-javaws.desktop
%{_datadir}/pixmaps/javaws.png
%{_man1dir}/javaws-itweb.1.gz
%_bindir/javaws.itweb


%changelog
* Fri Mar 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_1jpp8
- fixed requires

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_1jpp8
- new version

