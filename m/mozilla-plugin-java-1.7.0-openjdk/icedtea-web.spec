# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ pkgconfig(x11) zlib-devel
# END SourceDeps(oneline)
%def_enable javaws
%def_enable moz_plugin

BuildRequires(pre): browser-plugins-npapi-devel
BuildRequires(pre): rpm-build-java
%set_compress_method none
%define oldname icedtea-web
BuildRequires: /proc
BuildRequires: jpackage-generic-compat

# We require at the least the first release java-1.6.0-openjdk 
# with IcedTea6 1.10
%define min_openjdk_version 1:1.6.0.0-60
%define multilib_arches ppc64 sparc64 x86_64

# Version of java
%define javaver 1.7.0

# Alternatives priority
%define priority 17000

%ifarch %{ix86}
%define archinstall i386
%endif
%ifarch x86_64
%define archinstall amd64
%endif
# 32 bit sparc, optimized for v9
%ifarch sparcv9
%define archinstall sparc
%endif
# 64 bit sparc
%ifarch sparc64
%define archinstall sparcv9
%endif

%ifarch %{multilib_arches}
%define javadir     %{_jvmdir}/java-%{javaver}-openjdk.%{_arch}
%define jredir      %{_jvmdir}/jre-%{javaver}-openjdk.%{_arch}
%define jre6dir     %{_jvmdir}/jre-1.6.0-openjdk.%{_arch}
%define javaplugin  libjavaplugin.so.%{_arch}
%else
%define javadir     %{_jvmdir}/java-%{javaver}-openjdk
%define jredir      %{_jvmdir}/jre-%{javaver}-openjdk
%define jre6dir     %{_jvmdir}/jre-1.6.0-openjdk
%define javaplugin  libjavaplugin.so
%endif

%define binsuffix      .itweb

Name:		mozilla-plugin-java-1.7.0-openjdk
Version:	1.1.4
Release:	alt2_4jpp7
Summary:	Additional Java components for OpenJDK

Group:      Development/Java
License:    LGPLv2+ and GPLv2 with exceptions
URL:        http://icedtea.classpath.org/wiki/IcedTea-Web
Source0:    http://icedtea.classpath.org/download/source/%{oldname}-%{version}.tar.gz
Patch0:     %{oldname}-%{version}-npapi-fix.patch

BuildRequires:  java-%{javaver}-openjdk-devel
BuildRequires:  desktop-file-utils
BuildRequires:  xulrunner-devel
BuildRequires:  libglib2-devel
BuildRequires:  libgtk+2-devel
BuildRequires:  xulrunner-devel

# For functionality and the OpenJDK dirs
Requires:      java-%{javaver}-openjdk

# For the mozilla plugin dir
Requires:       browser-plugins-npapi

# Post requires alternatives to install plugin alternative.
Requires(post):   alternatives

# Postun requires alternatives to uninstall plugin alternative.
Requires(postun): alternatives

# Standard JPackage plugin provides.
Provides: java-plugin = %{javaver}


# IcedTea is only built on these archs for now
ExclusiveArch: x86_64 %ix86
Source44: import.info

%define altname java-%{javaver}-openjdk
%define origin openjdk
%define label -itweb
%define javaws_ver      %{javaver}
%define sdkdir          java-%{javaver}-openjdk-%{javaver}.0.%{_arch}
# TODO: move here
#define mozilla_java_plugin_so %{_prefix}/lib/%{sdkdir}/IcedTeaPlugin.so
%define mozilla_java_plugin_so %{_libdir}/IcedTeaPlugin.so

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
#BuildRequires: java-%javaver-%origin-devel

%description
The IcedTea-Web project provides a Java web browser plugin, an implementation
of Java Web Start (originally based on the Netx project) and a settings tool to
manage deployment settings for the aforementioned plugin and Web Start
implementations. 

%package javadoc
Summary:    API documentation for IcedTea-Web
Group:      Development/Java
Requires:   jpackage-utils
BuildArch:  noarch

%description javadoc
This package contains Javadocs for the IcedTea-Web project.

%prep
%setup -q -n %{oldname}-%{version}

%patch0

%build
autoconf
./configure \
    --with-pkgversion=ALTLinux-%{release}-%{_arch} \
    --docdir=%{_datadir}/javadoc/%{oldname} \
    --with-jdk-home=%{javadir} \
    --with-jre-home=%{jredir} \
    --libdir=%{_libdir} \
    --program-suffix=%{binsuffix} \
    --prefix=%{_prefix}

make CXXFLAGS="$RPM_OPT_FLAGS"

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Move javaws man page to a more specific name
mv $RPM_BUILD_ROOT/%{_mandir}/man1/javaws.1 $RPM_BUILD_ROOT/%{_mandir}/man1/javaws-itweb.1

# Install desktop files.
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
cp javaws.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install --vendor ''\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications javaws.desktop
desktop-file-install --vendor ''\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications itweb-settings.desktop

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

%files
%{_prefix}/bin/*
%{_libdir}/IcedTeaPlugin.so
%{_datadir}/applications/*
%{_datadir}/icedtea-web
%{_datadir}/man/man1/*
%{_datadir}/pixmaps/*
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
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt2_4jpp7
- added security policy

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1_4jpp7
- Sisyphus release

