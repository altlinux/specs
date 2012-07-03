#         --- note from viy@altlinux: ---
# as an effort to build compatible portable java environment,
# the JPackage Project was chosen as a new base of ALT java subsystem.
# JPackage specs have the following disclaimer:
# ====================================================
# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
%define major 1.6
%define minor 0
%define oldorigin       sun
%define origin          sun
%define priority        1603
%define javaver         %major.%minor
%define buildver        26

%define jppname         java-%{javaver}-%{origin}
%define javaws_ver      %{javaver}

%define toplevel_dir    jdk%{javaver}_%{buildver}
%define distversion 6u%buildver

%define label -%{name}

%define sdklnk          java-%{javaver}-%{origin}
%define jrelnk          jre-%{javaver}-%{origin}
%define sdkdir          %{jppname}-%{version}
%define jredir          %{sdkdir}/jre
%define sdkbindir       %{_jvmdir}/%{sdklnk}/bin
%define sdklibdir       %{_jvmdir}/%{sdklnk}/lib
%define jrebindir       %{_jvmdir}/%{jrelnk}/bin
%define jvmjardir       %{_jvmjardir}/%{jppname}-%{version}

%define cgibindir       %{_var}/www/cgi-bin
# --- jpackage compatibility stuff ends here ---

%def_enable demo
%def_enable fonts
%def_enable accessibility
%def_disable alsa_subpackage
%def_enable jdbc_subpackage
%ifarch x86_64
%def_enable javaws
%def_enable moz_plugin
%def_disable moz_plugin_classic
%def_enable desktop
%else
%def_enable javaws
%def_enable moz_plugin
%def_enable moz_plugin_classic
%def_enable desktop
%endif
%def_with gcc32_abi

%ifarch x86_64
%define libarch	    amd64
%else
%define libarch	    i386
%endif

%ifarch x86_64
Provides: /usr/lib/jvm/jre/lib/%libarch/server/libjvm.so()(64bit)
Provides: /usr/lib/jvm/jre/lib/%libarch/server/libjvm.so(SUNWprivate_1.1)(64bit)
%else
Provides: /usr/lib/jvm/jre/lib/%libarch/server/libjvm.so()
Provides: /usr/lib/jvm/jre/lib/%libarch/server/libjvm.so(SUNWprivate_1.1)
Provides: /usr/lib/jvm/jre/lib/%libarch/client/libjvm.so()
Provides: /usr/lib/jvm/jre/lib/%libarch/client/libjvm.so(SUNWprivate_1.1)
%endif

%define fontdir		%_datadir/fonts/ttf/j2se-%origin
%define fontdir_oblique	%_datadir/fonts/ttf/j2se-%origin-oblique

%define mozplugin_gcc32_abi_dir %{_jvmdir}/%{sdkdir}/jre/plugin/%libarch/ns7
#define mozplugin_gcc29_abi_dir %{_jvmdir}/%{sdkdir}/jre/plugin/%libarch/ns7-gcc29
#define mozilla_java_plugin_so %mozplugin_gcc32_abi_dir/libjavaplugin_oji.so
%define mozilla_java_plugin_so %{_jvmdir}/%{sdkdir}/jre/lib/%libarch/libnpjp2.so

Name:           %jppname
Version:        %{javaver}.%{buildver}
Release:        alt4
Epoch:          0
Summary:        Java 2 Runtime Environment, Standard Edition
License:        Operating System Distributor License for Java version 1.1
Group:          System/Base
URL:            http://java.sun.com/j2se/%{javaver}
Packager:       Igor Yu. Vlasenko <viy@altlinux.org>

# --- jpackage compatibility stuff starts here ---
Provides:       jre-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}
Provides:       jre-%{origin} = %{epoch}:%{version}-%{release}
Provides:       jre-%{javaver}, java-%{javaver}, jre = %{epoch}:%{javaver}
Provides:       java-%{origin} = %{epoch}:%{version}-%{release}
Provides:       java = %{epoch}:%{javaver}
Provides:       jndi = %{epoch}:%{version}, jndi-ldap = %{epoch}:%{version}
Provides:       jndi-cos = %{epoch}:%{version}, jndi-rmi = %{epoch}:%{version}
Provides:       jndi-dns = %{epoch}:%{version}
Provides:       jaas = %{epoch}:%{version}
Provides:       jsse = %{epoch}:%{version}
Provides:       jce = %{epoch}:%{version}
Provides:       jdbc-stdext = %{epoch}:3.0, jdbc-stdext = %{epoch}:%{version}
Provides:       java-sasl = %{epoch}:%{version}
# --- jpackage compatibility stuff ends here ---

Requires: fonts-ttf-%name >= %version-%release
Requires: java-common
Requires: /proc
Requires(post,preun): alternatives >= 0.4

Source0: http://download.java.net/dlj/binaries/jdk-%distversion-dlj-linux-i586.bin
Source1: http://download.java.net/dlj/binaries/jdk-%distversion-dlj-linux-amd64.bin
Patch: visualvm-java-1.6.0-sun-alt-skip-autoreq.patch

ExclusiveArch: i586 x86_64

%ifarch x86_64
%define jdksource %SOURCE1
%else
%define jdksource %SOURCE0
%endif

# jpackage use perl -p -i -e, we use subst
# BuildPreReq: perl

BuildRequires(pre): browser-plugins-npapi-devel
BuildRequires(pre): rpm-build-java rpm-macros-alternatives
BuildRequires: libalsa
BuildRequires: libunixODBC
#BuildRequires: xorg-x11-devel
BuildRequires: libX11 libXext libXi libXp libXt libXtst libSM libICE
BuildRequires: libstdc++3.3
BuildRequires: /proc
BuildRequires: shared-mime-info >= 0.15-alt2
BuildRequires: desktop-file-utils
### against #16510; 
### found in plugin/i386/ns7/libjavaplugin_oji.so, but can be anywhere:
### yes, they doesn't link against stdc++!!!
Requires: libstdc++3.3

%set_compress_method none
%set_verify_elf_method none
%brp_strip_none %{_jvmdir}/%{jredir}/lib/%libarch/libJdbcOdbc.so
############## altlinux 3.0 compatibility stuff ##############
#add_findprov_lib_path %{_jvmdir}/%{jredir}/lib/%libarch
%ifnarch x86_64
#add_findprov_lib_path %{_jvmdir}/%{jredir}/lib/%libarch/client
%endif
# it is needed for those apps which links with libjvm.so
%add_findprov_lib_path %{_jvmdir}/%{jredir}/lib/%libarch/server
#add_findprov_lib_path %{_jvmdir}/%{jredir}/lib/%libarch/native_threads
#add_findprov_lib_path %{_jvmdir}/%{jredir}/lib/%libarch/headless
#add_findprov_lib_path %{_jvmdir}/%{jredir}/lib/%libarch/motif21
#add_findprov_lib_path %{_jvmdir}/%{jredir}/lib/%libarch/xawt
##Provides: libmawt.so
##Provides: libmawt.so(SUNWprivate_1.1)
##Provides: libmlib_image.so(VER_1.1)
#################################################################

%description
This package contains the Java Runtime Environment for %{name}.
Install this package if you need to run Java applications.

The Java Runtime Environment contains the Java virtual machine, 
runtime class libraries, and Java application launcher that are 
necessary to run programs written in the Java programming language. 
It is not a development environment and does not contain development 
tools such as compilers or debuggers.  For development tools, see the 
Java SDK, Standard Edition.

%package        devel
Summary:        Java 2 SDK, Standard Edition
Group:          Development/Java
Provides: /usr/bin/javac
Provides: jdk = %javaver
Requires: %name = %version-%release
Requires(post,preun): alternatives >= 0.4

# --- jpackage compatibility stuff starts here ---
Provides:       java-sdk-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}
Provides:       java-sdk-%{origin} = %{epoch}:%{version}-%{release}
Provides:       java-sdk-%{javaver}, java-sdk = %{epoch}:%{javaver}
Provides:       java-devel-%{origin} = %{epoch}:%{version}-%{release}
Provides:       java-%{javaver}-devel, java-devel = %{epoch}:%{javaver}
# --- jpackage compatibility stuff ends here ---

%ifarch x86_64
Provides: /usr/lib/jvm/java/jre/lib/%libarch/server/libjvm.so()(64bit)
Provides: /usr/lib/jvm/java/jre/lib/%libarch/server/libjvm.so(SUNWprivate_1.1)(64bit)
%else
Provides: /usr/lib/jvm/java/jre/lib/%libarch/server/libjvm.so()
Provides: /usr/lib/jvm/java/jre/lib/%libarch/server/libjvm.so(SUNWprivate_1.1)
Provides: /usr/lib/jvm/java/jre/lib/%libarch/client/libjvm.so()
Provides: /usr/lib/jvm/java/jre/lib/%libarch/client/libjvm.so(SUNWprivate_1.1)
%endif

%description    devel
The Java(tm) Development Kit (JDK(tm)) contains the software and tools that
developers need to compile, debug, and run applets and applications
written using the Java programming language.

Install this package if you need to develop and build Java applications.

%package source
Summary: Source files for the Java 2 SDK
Group: Development/Java

%description source
Java programming language source files for all classes that make up
the Java 2 core API.

%if_enabled demo
%package        demo
Summary:        Demo applets and programs for the Java 2 SDK
Group: Development/Java
AutoReqProv: no

%description    demo
This package contains demonstration files for %{name}.

These include examples, with source code, of programming for the Java 
platform that use Swing and other Java Foundation Classes, and the Java
Platform Debugger Architecture.
%endif

%if_enabled moz_plugin
%package -n mozilla-plugin-%name
Summary: Java Plug-In for Mozilla family browsers
Group: Networking/WWW
Provides: java2-plugin-mozilla = %javaver
Provides: j2se%major-%origin-plugin-mozilla
Obsoletes: j2se%major-%origin-plugin-mozilla
Provides: mozilla-plugin-j2se%major-%origin
Obsoletes: mozilla-plugin-j2se%major-%origin
Requires: %name = %version-%release
Requires: browser-plugins-npapi
Requires(post,preun): alternatives >= 0.4
# --- jpackage compatibility stuff starts here ---
Provides:       java-plugin = %{epoch}:%{javaver}, java-%{javaver}-plugin = %{epoch}:%{version}
Conflicts:      java-%{javaver}-ibm-plugin, java-%{javaver}-blackdown-plugin
Conflicts:      java-%{javaver}-bea-plugin
Obsoletes:      java-1.3.1-plugin, java-1.4.0-plugin, java-1.4.1-plugin, java-1.4.2-plugin
# --- jpackage compatibility stuff ends here ---

%description -n mozilla-plugin-%name
This package contains Java(TM) 2 Plug-In for Mozilla family web browsers.
%endif # enabled moz_plugin

%if_enabled alsa_subpackage
%package        alsa
Summary:        ALSA support for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}

%description    alsa
This package contains Advanced Linux Sound Architecture (ALSA) support
libraries for %{name}.
%endif # enabled alsa_subpackage

%if_enabled jdbc_subpackage
%package        jdbc
Summary:        Native library for JDBC support in Java
Group:          Development/Databases
Requires:       %name = %version-%release

%description    jdbc
This package contains the JDBC/ODBC bridge driver for %{name}.
%endif # enabled jdbc_subpackage

%if_enabled javaws
%package javaws
Summary: Java Web Start
Group: Networking/Other
Requires: %name = %version-%release
Requires(post,preun): alternatives >= 0.4
# --- jpackage compatibility stuff starts here ---
Provides:       javaws = %{epoch}:%{javaws_ver}
Obsoletes:      javaws-menu
# --- jpackage compatibility stuff ends here ---

%description javaws
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

%if_enabled desktop
%package -n java-%{oldorigin}-desktop
Summary: desktop resources for %{name}.
Group: Graphical desktop/Other
BuildArch: noarch

%description -n java-%{oldorigin}-desktop
Desktop resources, such as pixmaps, etc, for %{name},
that are shared between different versions of %{origin}
JVM.
%endif	# enabled desktop

%if_enabled accessibility
%package accessibility
Summary: Accessibility extensions for the %{origin} JVM.
Group: Accessibility
BuildRequires: java-access-bridge
Requires: java-access-bridge
BuildArch: noarch

%description    accessibility
This package contains accessibility extensions for %{name}.
%endif # enabled accessibility

%if_enabled fonts
%package -n fonts-ttf-%name
Summary: TrueType fonts for %{name}.
Group: System/Fonts/True type
BuildArch: noarch
BuildRequires: mkfontscale
Requires: fontconfig
Provides: java_%origin-fonts = %version-%release
Obsoletes: j2se-%origin-fonts
Obsoletes: j2se%major-%origin-fonts
Provides: fonts-ttf-j2se-%origin = %version-%release
Obsoletes: fonts-ttf-j2se-%origin < %version-%release
Obsoletes: fonts-ttf-java-1.4.2-sun, fonts-ttf-java-1.5.0-sun
# hack around apt (to remove when apt will be fixed)
Provides: /usr/share/fonts/ttf/j2se-sun
Provides: /usr/share/fonts/ttf/j2se-sun-oblique
# --- jpackage compatibility stuff starts here ---
Provides:       java-fonts = %{epoch}:%{javaver}, java-%{javaver}-fonts
Conflicts:      java-%{javaver}-ibm-fonts, java-%{javaver}-blackdown-fonts
Conflicts:      java-%{javaver}-bea-fonts
Obsoletes:      java-1.3.1-fonts, java-1.4.0-fonts, java-1.4.1-fonts, java-1.4.2-fonts, java-1.5.0-fonts
# --- jpackage compatibility stuff ends here ---

%description -n fonts-ttf-%name
This package contains the TrueType fonts for %{origin} JVMs.
%endif	# enabled fonts

%prep
#echo yes | MORE=10000 sh %jdksource
sh %jdksource --accept-license --unpack
%setup -T -D -n %{toplevel_dir}
# fix perms
chmod -R u+w *

%patch
cat >README.alt <<EOF
The Java 2 Runtime Environment and SDK, Standard Edition are distributed
within this and related packages as shown below:

%name		- Java 2 Runtime Environment, Standard Edition
			  (with notable omissions listed below).
%name-devel	- Java 2 SDK, Standard Edition.
%name-source	- Java 2 Standard Edition API source files.
%name-demo	- Java 2 SDK demo applets and programs.
%name-jdbc	- JDBC provider library using ODBC.
			  This library was excluded from the
			  %name package due to outstanding dependencies.
%name-javaws	- Java Web Start software that is bundled with
			  Java 2 Runtime Environment, Standard Edition
mozilla-plugin-%name	- Java 2 plug-in for Mozilla family browsers
fonts-ttf-%name		- The TrueType fonts in %fontdir
			  and %fontdir_oblique,
			  shared between various installations of
			  the Java 2 Runtime Environment.
java-%{origin}-desktop  - Java 2 desktop resources (pixmaps, etc)

See the README, LICENSE, COPYRIGHT, and THIRDPARTYLICENSEREADME.txt files
for copyright information, terms of use and redistribution covering contents
of these packages.

The packages should fullfill (most of) the requirements of JPackage 
policy (www.jpackage.org). There are some historical minor differences
which should not break the compatibility.
EOF
# # # TODO: # # # # # # # # # # # # #
# # current difference with jpackage
# man pages:
# pack200/unpack200 moved from devel -- good: that's a bug in jpackage
# devel: (no /var/www/cgi-bin...), 
# demo: 
# are in lib, should be in share/shortlink
# fonts:
# alt specific font links
# TODO(?): spring off the x11-related libraries

%if_enabled fonts
mkdir fontdoc
cat > fontdoc/README.alt <<EOF
The fonts contained in this package are part of the
Java 2 Runtime Environment, Standard Edition (J2SE).
This package is required by packages containing various versions
of J2SE.

See the LICENSE, COPYRIGHT, and THIRDPARTYLICENSEREADME.txt files
for copyright information, terms of use and redistribution covering contents
of this package.
EOF
%endif	# enabled fonts

%install
# .systemPrefs removed as they are not packaged in jpackage
#cp -a jre/.systemPrefs %buildroot%{_jvmdir}/%{jredir}
# ------------------------------------------

### jpackage ###

%if_enabled moz_plugin
## fix up ControlPanel APPHOME and bin locations
#%__subst 's|APPHOME=.*|APPHOME=%{_jvmdir}/%{jredir}|' jre/bin/ControlPanel
#%__subst 's|/usr/bin/||g' jre/bin/ControlPanel

# fix up (create new) HtmlConverter
cat > bin/HtmlConverter << EOF
%{jrebindir}/java -jar %{sdklibdir}/htmlconverter.jar $*
EOF

# fix up java-rmi.cgi PATH
[ -e bin/java-rmi.cgi ] && %__subst 's|PATH=.*|PATH=%{jrebindir}|' bin/java-rmi.cgi

# # install java-rmi-cgi
# install -D -m 755 bin/java-rmi.cgi $RPM_BUILD_ROOT%{cgibindir}/java-rmi-%{version}.cgi
%endif

# main files
install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
cp -a bin include lib src.zip $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}

# extensions handling
install -d -m 755 $RPM_BUILD_ROOT%{jvmjardir}
pushd $RPM_BUILD_ROOT%{jvmjardir}
   ln -s %{_jvmdir}/%{jredir}/lib/jsse.jar jsse-%{version}.jar
   ln -s %{_jvmdir}/%{jredir}/lib/jce.jar jce-%{version}.jar
   ln -s %{_jvmdir}/%{jredir}/lib/rt.jar jndi-%{version}.jar
   ln -s %{_jvmdir}/%{jredir}/lib/rt.jar jndi-ldap-%{version}.jar
   ln -s %{_jvmdir}/%{jredir}/lib/rt.jar jndi-cos-%{version}.jar
   ln -s %{_jvmdir}/%{jredir}/lib/rt.jar jndi-rmi-%{version}.jar
   ln -s %{_jvmdir}/%{jredir}/lib/rt.jar jaas-%{version}.jar
   ln -s %{_jvmdir}/%{jredir}/lib/rt.jar jdbc-stdext-%{version}.jar
   ln -s jdbc-stdext-%{version}.jar jdbc-stdext-3.0.jar
   ln -s %{_jvmdir}/%{jredir}/lib/rt.jar sasl-%{version}.jar
   # do we need version?; TODO: add provides to jvm?
   # disabled due to hardcored symlinks to jvm
   #ln -s %{_jvmdir}/%{jredir}/lib/rt.jar xml-commons-apis.jar
   for jar in *-%{version}.jar ; do
      if [ x%{version} != x%{javaver} ]; then
         ln -fs ${jar} $(echo $jar | sed "s|-%{version}.jar|-%{javaver}.jar|g")
      fi
      ln -fs ${jar} $(echo $jar | sed "s|-%{version}.jar|.jar|g")
   done
popd

# rest of the jre
cp -a jre/bin jre/lib $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}
%if_enabled javaws
cp -a jre/javaws $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}
%endif
%if_enabled moz_plugin
cp -a jre/plugin $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}
%endif
install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/endorsed

# jce policy file handling
install -d -m 755 $RPM_BUILD_ROOT%{_jvmprivdir}/%{name}/jce/vanilla
for file in local_policy.jar US_export_policy.jar; do
  mv $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security/$file \
    $RPM_BUILD_ROOT%{_jvmprivdir}/%{name}/jce/vanilla
  # for ghosts
  touch $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security/$file
done

# versionless symlinks
pushd $RPM_BUILD_ROOT%{_jvmdir}
ln -s %{jredir} %{jrelnk}
ln -s %{sdkdir} %{sdklnk}
popd

pushd $RPM_BUILD_ROOT%{_jvmjardir}
ln -s %{sdkdir} %{jrelnk}
ln -s %{sdkdir} %{sdklnk}
popd

# man pages
install -d -m 755 $RPM_BUILD_ROOT%{_man1dir}
for manpage in man/man1/*; do
  install -m 644 -p $manpage $RPM_BUILD_ROOT%{_man1dir}/`basename $manpage .1`%label.1
done

# demo
%if_enabled demo
cp -a demo sample %buildroot%{_jvmdir}/%{sdkdir}
%endif

#####################################
# ------- alt linux specific -------#
#####################################

mkinstall_java_fonts() {
local JRE_FONT_DIR=$1
local INSTALL_FONT_DIR=$2
%if_enabled fonts
install -d -m755 %buildroot$INSTALL_FONT_DIR
# move the fonts into a shared fonts directory
install -m 644 %buildroot%{_jvmdir}/%{jredir}/lib/$JRE_FONT_DIR/*.ttf %buildroot$INSTALL_FONT_DIR/
# symlink jre to common location (TODO: think of alternatives)
rm -rf %buildroot%{_jvmdir}/%{jredir}/lib/$JRE_FONT_DIR
ln -s `relative $INSTALL_FONT_DIR %{_jvmdir}/%{jredir}/lib/` %buildroot%{_jvmdir}/%{jredir}/lib/$JRE_FONT_DIR
install -d -m755 %buildroot%_sysconfdir/X11/fontpath.d/
FONTNAME=${INSTALL_FONT_DIR/\/usr\/share\/fonts\/ttf\//}
ln -s `relative $INSTALL_FONT_DIR %_sysconfdir/X11/fontpath.d/` %buildroot%_sysconfdir/X11/fontpath.d/ttf-$FONTNAME:pri=50
mkfontscale %buildroot$INSTALL_FONT_DIR
ln -s fonts.scale %buildroot$INSTALL_FONT_DIR/fonts.dir
%endif	# enabled fonts
}

mkinstall_java_fonts fonts %fontdir
mkinstall_java_fonts oblique-fonts %fontdir_oblique

# HACK around find-requires
%define __find_requires    $RPM_BUILD_ROOT/.find-requires
cat > $RPM_BUILD_ROOT/.find-requires <<EOF
#!/bin/sh
(/usr/lib/rpm/find-requires | grep -v %{_jvmdir}/%{sdkdir}) | grep -v /usr/bin/java || :
EOF
chmod 755 $RPM_BUILD_ROOT/.find-requires
# end HACK around find-requires

%if_enabled desktop
#install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/mime/packages/
install -d -m 755 $RPM_BUILD_ROOT{%_desktopdir,%_datadir/desktop-directories,/etc/xdg/menus/applications-merged}
mv $RPM_BUILD_ROOT%{_jvmdir}/%{jrelnk}/lib/desktop/icons $RPM_BUILD_ROOT%{_datadir}/
#mv $RPM_BUILD_ROOT%{_jvmdir}/%{jrelnk}/lib/desktop/mime/packages/* $RPM_BUILD_ROOT%{_datadir}/mime/packages/
#mv $RPM_BUILD_ROOT%{_jvmdir}/%{jrelnk}/lib/desktop/applications/%{oldorigin}-java.desktop $RPM_BUILD_ROOT%_desktopdir/
#mv $RPM_BUILD_ROOT%{_jvmdir}/%{jrelnk}/lib/desktop/applications/%{oldorigin}-javaws.desktop $RPM_BUILD_ROOT%_desktopdir/
%endif

%if_enabled moz_plugin
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 644 jre/plugin/desktop/%{origin}_java.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
install -d -m 755 $RPM_BUILD_ROOT%{_niconsdir}
ln -s %{_datadir}/pixmaps/%{name}.png $RPM_BUILD_ROOT%{_niconsdir}/%{name}.png
%endif

%if_enabled accessibility
cp %{_javadir}-ext/accessibility.properties $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/accessibility.properties
ln -s $(relative %{_javadir}-1.6.0/gnome-java-bridge.jar %{_jvmdir}/%{jredir}/lib/ext/gnome-java-bridge.jar) \
   $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/ext/gnome-java-bridge.jar
%endif

##################################################
# --- alt linux specific, shared with openjdk ---#
##################################################

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/applications
if [ -e $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/bin/jvisualvm ]; then
  cat >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-jvisualvm.desktop << EOF
[Desktop Entry]
Name=Java VisualVM (%{name})
Comment=Java Virtual Machine Monitoring, Troubleshooting, and Profiling Tool
Exec=%{_jvmdir}/%{sdkdir}/bin/jvisualvm
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;Profiling;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
fi

%if_enabled moz_plugin
# ControlPanel freedesktop.org menu entry
cat >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-control-panel.desktop << EOF
[Desktop Entry]
Name=Java Plugin Control Panel (%{name})
Comment=Java Control Panel
Exec=%{_jvmdir}/%{sdkdir}/bin/jcontrol
Icon=%{name}
Terminal=false
Type=Application
Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
%endif

%if_enabled javaws
# javaws freedesktop.org menu entry
cat >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-javaws.desktop << EOF
[Desktop Entry]
Name=Java Web Start (%{name})
Comment=Java Application Launcher
MimeType=application/x-java-jnlp-file;
Exec=%{_jvmdir}/%{jredir}/bin/javaws %%u
Icon=%{name}
Terminal=false
Type=Application
Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
%endif

# Install substitute rules for buildreq
echo java >j2se-buildreq-substitute
echo java-devel >j2se-devel-buildreq-substitute
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
install -m644 j2se-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name
install -m644 j2se-devel-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-devel

%__install -d %buildroot%_altdir

# J2SE alternative
%__cat <<EOF >%buildroot%_altdir/%name-java
%{_bindir}/java	%{_jvmdir}/%{jredir}/bin/java	%priority
%_man1dir/java.1.gz	%_man1dir/java%{label}.1.gz	%{_jvmdir}/%{jredir}/bin/java
EOF
# binaries and manuals
for i in keytool policytool servertool pack200 unpack200 \
orbd rmid rmiregistry tnameserv
do
  %__cat <<EOF >>%buildroot%_altdir/%name-java
%_bindir/$i	%{_jvmdir}/%{jredir}/bin/$i	%{_jvmdir}/%{jredir}/bin/java
%_man1dir/$i.1.gz	%_man1dir/${i}%{label}.1.gz	%{_jvmdir}/%{jredir}/bin/java
EOF
done

# ----- JPackage compatibility alternatives ------
%__cat <<EOF >>%buildroot%_altdir/%name-java
%{_jvmdir}/jre	%{_jvmdir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmjardir}/jre	%{_jvmjardir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmdir}/jre-%{origin}	%{_jvmdir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmjardir}/jre-%{origin}	%{_jvmjardir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmdir}/jre-%{javaver}	%{_jvmdir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmjardir}/jre-%{javaver}	%{_jvmjardir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
EOF
%if_enabled moz_plugin
%__cat <<EOF >>%buildroot%_altdir/%name-java
%{_bindir}/ControlPanel	%{_jvmdir}/%{jredir}/bin/ControlPanel	%{_jvmdir}/%{jredir}/bin/java
%{_bindir}/jcontrol	%{_jvmdir}/%{jredir}/bin/jcontrol	%{_jvmdir}/%{jredir}/bin/java
EOF
%endif
# JPackage specific: alternatives for security policy
%__cat <<EOF >>%buildroot%_altdir/%name-java
%{_jvmdir}/%{jrelnk}/lib/security/local_policy.jar	%{_jvmprivdir}/%{name}/jce/vanilla/local_policy.jar	%{priority}
%{_jvmdir}/%{jrelnk}/lib/security/US_export_policy.jar	%{_jvmprivdir}/%{name}/jce/vanilla/US_export_policy.jar	%{_jvmprivdir}/%{name}/jce/vanilla/local_policy.jar
EOF
# ----- end: JPackage compatibility alternatives ------


# Javac alternative
%__cat <<EOF >%buildroot%_altdir/%name-javac
%_bindir/javac	%{_jvmdir}/%{sdkdir}/bin/javac	%priority
%_man1dir/javac.1.gz	%_man1dir/javac%{label}.1.gz	%{_jvmdir}/%{sdkdir}/bin/javac
EOF

# binaries and manuals
for i in appletviewer extcheck idlj jar jarsigner javadoc javah javap jdb native2ascii rmic serialver apt jconsole jinfo jmap jps jsadebugd jstack jstat jstatd \
jhat jrunscript jvisualvm schemagen wsgen wsimport xjc
do
  if [ -e $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/bin/$i ]; then
  %__cat <<EOF >>%buildroot%_altdir/%name-javac
%_bindir/$i	%{_jvmdir}/%{sdkdir}/bin/$i	%{_jvmdir}/%{sdkdir}/bin/javac
%_man1dir/$i.1.gz	%_man1dir/${i}%{label}.1.gz	%{_jvmdir}/%{sdkdir}/bin/javac
EOF
  fi
done
# binaries w/o manuals
for i in HtmlConverter
do
  %__cat <<EOF >>%buildroot%_altdir/%name-javac
%_bindir/$i	%{_jvmdir}/%{sdkdir}/bin/$i	%{_jvmdir}/%{sdkdir}/bin/javac
EOF
done

# ----- JPackage compatibility alternatives ------
  %__cat <<EOF >>%buildroot%_altdir/%name-javac
%{_jvmdir}/java	%{_jvmdir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmjardir}/java	%{_jvmjardir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmdir}/java-%{origin}	%{_jvmdir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmjardir}/java-%{origin}	%{_jvmjardir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmdir}/java-%{javaver}	%{_jvmdir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmjardir}/java-%{javaver}	%{_jvmjardir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
EOF
# ----- end: JPackage compatibility alternatives ------

%if_enabled moz_plugin
# Mozilla plugin alternative
%__cat <<EOF >%buildroot%_altdir/%name-mozilla
%browser_plugins_path/libjavaplugin_oji.so	%mozilla_java_plugin_so	%priority
EOF
%endif	# enabled moz_plugin

%if_enabled javaws
# Java Web Start alternative
%__cat <<EOF >%buildroot%_altdir/%name-javaws
%_bindir/javaws	%{_jvmdir}/%{jredir}/bin/javaws	%{_jvmdir}/%{jredir}/bin/java
%_man1dir/javaws.1.gz	%_man1dir/javaws%label.1.gz	%{_jvmdir}/%{jredir}/bin/java
EOF
# ----- JPackage compatibility alternatives ------
%__cat <<EOF >>%buildroot%_altdir/%name-javaws
%{_datadir}/javaws	%{_jvmdir}/%{jredir}/bin/javaws	%{_jvmdir}/%{jredir}/bin/java
EOF
# ----- end: JPackage compatibility alternatives ------
%endif	# enabled javaws

# hack (see #11383) to enshure that all man pages will be compressed
for i in $RPM_BUILD_ROOT%_man1dir/*.1; do
    [ -f $i ] && gzip -9 $i
done

%post
%force_update_alternatives

##################################################
# - END alt linux specific, shared with openjdk -#
##################################################


%files
%doc jre/COPYRIGHT jre/LICENSE jre/README jre/Welcome.html
%doc jre/THIRDPARTYLICENSEREADME.txt
%doc README.alt
# jpackage links #
%{jvmjardir}
%{_jvmdir}/%{jrelnk}
%{_jvmjardir}/%{jrelnk}
# jpackage dirs
%{_jvmdir}/%{jredir}/lib/endorsed
%_altdir/%name-java
%_sysconfdir/buildreqs/packages/substitute.d/%name
%dir %{_jvmdir}/%{sdkdir}
%dir %{_jvmdir}/%{jredir}
%dir %{_jvmdir}/%{jredir}/lib
%dir %{_jvmdir}/%{jredir}/lib/management
%dir %{_jvmdir}/%{jredir}/lib/security
# .systemPrefs removed as they are not packaged in jpackage
#%{_jvmdir}/%{jredir}/.systemPrefs
%{_jvmdir}/%{jredir}/bin
%if_enabled javaws
%exclude %{_jvmdir}/%{jredir}/bin/javaws
%endif
%{_jvmdir}/%{jredir}/lib/%libarch
%if_enabled jdbc_subpackage
%exclude %{_jvmdir}/%{jredir}/lib/%libarch/libJdbcOdbc.so
%endif
%if_enabled alsa_subpackage
%exclude %{_jvmdir}/%{jredir}/lib/%libarch/libjsoundalsa.so
%endif
%{_jvmdir}/%{jredir}/lib/*.jar
%{_jvmdir}/%{jredir}/lib/*.txt
%{_jvmdir}/%{jredir}/lib/applet
%{_jvmdir}/%{jredir}/lib/audio
%{_jvmdir}/%{jredir}/lib/classlist
%{_jvmdir}/%{jredir}/lib/cmm
%{_jvmdir}/%{jredir}/lib/ext
%{_jvmdir}/%{jredir}/lib/fonts
%{_jvmdir}/%{jredir}/lib/im
%{_jvmdir}/%{jredir}/lib/images
%{_jvmdir}/%{jredir}/lib/servicetag
%if_enabled moz_plugin
# common between plugin and javaws (TODO: desktop)
%{_datadir}/pixmaps/%{name}.png
%{_niconsdir}/%{name}.png
%{_jvmdir}/%{jredir}/lib/locale
%exclude %{_jvmdir}/%{jredir}/lib/locale/*/LC_MESSAGES/sunw_java_plugin.mo
%exclude %{_jvmdir}/%{jredir}/lib/%libarch/libjavaplugin_jni.so
%exclude %{_jvmdir}/%{jredir}/lib/%libarch/libnpjp2.so
%exclude %{_jvmdir}/%{jredir}/lib/plugin.jar
%exclude %{_jvmdir}/%{jredir}/plugin
%if_enabled moz_plugin_classic
%exclude %{_jvmdir}/%{jredir}/lib/%libarch/libjavaplugin_nscp*.so
%endif
%endif
%{_jvmdir}/%{jredir}/lib/oblique-fonts
%{_jvmdir}/%{jredir}/lib/zi
%config(noreplace) %{_jvmdir}/%{jredir}/lib/*.properties
%config(noreplace) %{_jvmdir}/%{jredir}/lib/*.properties.??
%config(noreplace) %{_jvmdir}/%{jredir}/lib/fontconfig.bfc
%config(noreplace) %{_jvmdir}/%{jredir}/lib/fontconfig.properties.src
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/cacerts
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.policy
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.security
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/blacklist
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/trusted.libraries
%config(noreplace) %{_jvmdir}/%{jredir}/lib/management/*
%{_jvmdir}/%{jredir}/lib/fontconfig.*.bfc
%{_jvmdir}/%{jredir}/lib/fontconfig.*.properties.src
#%{_jvmdir}/%{jredir}/lib/security/*.jar
%{_jvmprivdir}/*
%ghost %{_jvmdir}/%{jredir}/lib/security/local_policy.jar
%ghost %{_jvmdir}/%{jredir}/lib/security/US_export_policy.jar
%_man1dir/java%label.1*
%_man1dir/keytool%label.1*
%_man1dir/orbd%label.1*
%_man1dir/policytool%label.1*
%_man1dir/rmid%label.1*
%_man1dir/rmiregistry%label.1*
%_man1dir/servertool%label.1*
%_man1dir/tnameserv%label.1*
%_man1dir/pack200%label.1*
%_man1dir/unpack200%label.1*
# new in 6
%{_jvmdir}/%{jredir}/lib/jexec
%{_jvmdir}/%{jredir}/lib/meta-index
%if_enabled accessibility
%exclude %{_jvmdir}/%{jredir}/lib/accessibility.properties
%exclude %{_jvmdir}/%{jredir}/lib/ext/gnome-java-bridge.jar
%endif

%if_enabled accessibility
%files accessibility
%{_jvmdir}/%{jredir}/lib/accessibility.properties
%{_jvmdir}/%{jredir}/lib/ext/gnome-java-bridge.jar
%endif

%files devel
%doc *README* LICENSE COPYRIGHT
# jpackage short links #
%{_jvmdir}/%{sdklnk}
%{_jvmjardir}/%{sdklnk}
%_altdir/%name-javac
%_sysconfdir/buildreqs/packages/substitute.d/%name-devel
%{_jvmdir}/%{sdkdir}/bin
%{_jvmdir}/%{sdkdir}/lib
%{_jvmdir}/%{sdkdir}/include
%_man1dir/appletviewer%label.1*
%_man1dir/extcheck%label.1*
%_man1dir/idlj%label.1*
%_man1dir/jar%label.1*
%_man1dir/jarsigner%label.1*
%_man1dir/javac%label.1*
%_man1dir/javadoc%label.1*
%_man1dir/javah%label.1*
%_man1dir/javap%label.1*
%_man1dir/jdb%label.1*
%_man1dir/native2ascii%label.1*
%_man1dir/rmic%label.1*
%_man1dir/serialver%label.1*
%_man1dir/apt%label.1*
%_man1dir/jconsole%label.1*
%_man1dir/jinfo%label.1*
%_man1dir/jmap%label.1*
%_man1dir/jps%label.1*
%_man1dir/jsadebugd%label.1*
%_man1dir/jstack%label.1*
%_man1dir/jstat%label.1*
%_man1dir/jstatd%label.1*
# new in 6
%_man1dir/jhat%label.1*
%_man1dir/jrunscript%label.1*
%_man1dir/jvisualvm%label.1*
%_man1dir/schemagen%label.1*
%_man1dir/wsgen%label.1*
%_man1dir/wsimport%label.1*
%_man1dir/xjc%label.1*
# new in 6
%{_datadir}/applications/%{name}-jvisualvm.desktop

%files source
%{_jvmdir}/%{sdkdir}/src.zip

%if_enabled demo
%files demo
#todo
#%dir %{_datadir}/%{name}
#%{_datadir}/%{name}/demo
%{_jvmdir}/%{sdkdir}/demo
%{_jvmdir}/%{sdkdir}/sample
%endif

%if_enabled moz_plugin
%files -n mozilla-plugin-%name
%_altdir/%name-mozilla
%dir %{_jvmdir}/%{jredir}/plugin
%dir %{_jvmdir}/%{jredir}/lib/%libarch
%{_jvmdir}/%{jredir}/lib/%libarch/libjavaplugin_jni.so
%{_jvmdir}/%{jredir}/lib/%libarch/libnpjp2.so
%dir %{_jvmdir}/%{jredir}/lib/locale
%dir %{_jvmdir}/%{jredir}/lib/locale/*
%dir %{_jvmdir}/%{jredir}/lib/locale/*/LC_MESSAGES
%{_jvmdir}/%{jredir}/lib/locale/*/LC_MESSAGES/sunw_java_plugin.mo
%{_jvmdir}/%{jredir}/lib/plugin.jar
%{_jvmdir}/%{jredir}/plugin/desktop
%{_datadir}/applications/%{name}-control-panel.desktop
%endif
%if_enabled moz_plugin_classic
%dir %{_jvmdir}/%{jredir}/plugin/%libarch
%{_jvmdir}/%{jredir}/lib/%libarch/libjavaplugin_nscp*.so
%mozplugin_gcc32_abi_dir
%endif

%if_enabled alsa_subpackage
%files alsa
%dir %{_jvmdir}/%{jredir}/lib/%libarch
%{_jvmdir}/%{jredir}/lib/%libarch/libjsoundalsa.so
%endif

%if_enabled jdbc_subpackage
%files jdbc
%dir %{_jvmdir}/%{jredir}/lib/%libarch
%{_jvmdir}/%{jredir}/lib/%libarch/libJdbcOdbc.so
%endif

%if_enabled desktop
%files -n java-%{oldorigin}-desktop
%{_datadir}/icons/*/*/*/*
#%{_datadir}/mime/packages/*.xml
#%_desktopdir/%{oldorigin}-java.desktop
#%_desktopdir/%{oldorigin}-javaws.desktop
%exclude %{_jvmdir}/%{jredir}/lib/desktop/applications/sun-java.desktop
%exclude %{_jvmdir}/%{jredir}/lib/desktop/applications/sun-javaws.desktop
%exclude %{_jvmdir}/%{jredir}/lib/desktop/applications/sun_java.desktop
%exclude %{_jvmdir}/%{jredir}/lib/desktop/mime/packages/x-java-archive.xml
%exclude %{_jvmdir}/%{jredir}/lib/desktop/mime/packages/x-java-jnlp-file.xml
%if_enabled moz_plugin
%exclude %{_niconsdir}/%{name}.png
%endif
%endif

%if_enabled javaws
%files javaws
%doc README.alt
%_altdir/%name-javaws
%{_jvmdir}/%{jredir}/bin/javaws
#%{_jvmdir}/%{jredir}/lib/javaws
%{_jvmdir}/%{jredir}/javaws
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/javaws.policy
%_man1dir/javaws%label.1*
%{_datadir}/applications/%{name}-javaws.desktop
# deploy.jar, javaws.jar: should be moved too
# new in 6
%{_jvmdir}/%{jredir}/lib/deploy
%endif

%if_enabled fonts
%files -n fonts-ttf-%name
%doc LICENSE COPYRIGHT
%doc fontdoc/README.alt
%_sysconfdir/X11/fontpath.d/*
%dir %fontdir
%fontdir/fonts.scale
%fontdir/fonts.dir
%fontdir/*.ttf
%dir %fontdir_oblique
%fontdir_oblique/fonts.scale
%fontdir_oblique/fonts.dir
%fontdir_oblique/*.ttf
%endif	# enabled fonts


%changelog
* Wed Feb 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.26-alt4
- proper u26; maintainance build for p6/t6 branch

* Sun Sep 18 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.26-alt3
- reverted to u17 due to https://bugs.eclipse.org/bugs/show_bug.cgi?id=346730

* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.26-alt2
- reverted to u23 due to http://bugs.sun.com/view_bug.do?bug_id=6302804

* Tue Jul 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.26-alt1
- new version

* Fri Mar 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.24-alt2
- removed java menu (merged with system menu).

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.24-alt1
- new version

* Tue Feb 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.23-alt2
- fixed java submenu (closes: #24533)

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.23-alt1
- new version

* Wed Oct 13 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.22-alt1
- new version

* Thu Aug 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.21-alt1
- new version

* Mon May 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.20-alt2
- tuning font dependencies

* Sat Apr 17 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.20-alt1
- new version

* Wed Apr 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.19-alt1
- new version

* Thu Jan 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.18-alt1
- new version

* Fri Dec 18 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.17-alt2
- fixed shared libjvm.so provides

* Sat Nov 07 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.17-alt1
- new version

* Thu Oct 08 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.16-alt2
- added shared libjvm.so provides

* Mon Oct 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.16-alt1
- new version

* Thu Jun 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.14-alt1
- new version

* Wed May 06 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.13-alt1
- new version

* Sat Feb 14 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.12-alt1
- new version
- x86_64 java plugin

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.11-alt2
- alternatives.prov friendly alternatives in jre
- removed xml-commons-apis provides

* Thu Dec 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.11-alt1
- new version

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.10-alt5
- added accessibility subpackage

* Sat Nov 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.10-alt4
- support for alternatives 0.4

* Mon Nov 17 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.10-alt3
- removed obsolete update_menu calls

* Sat Oct 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.10-alt2
- added explicit font Obsoletes: to help apt 

* Wed Oct 22 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.10-alt1
- new version

* Fri Aug 01 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.07-alt3
- fixed #16510. yes, they use, but doesn't link against stdc++ :(

* Fri Jul 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.07-alt2
- added jvisualvm desktop

* Tue Jul 22 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.07-alt1
- new version
- alsa subpackage is merged
- added jvisualvm

* Fri May 30 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.06-alt1
- new version

* Thu Apr 24 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.05-alt1
- new version
- javaws fixes

* Sat Oct 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.03-alt1
- new version
- built from dlj binaries
- use Operating System Distributor License for Java version 1.1

* Sat Sep 01 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.02-alt1
- new version
- alternatives cleanup
- applied new font policy
- added mime info
- added jre/lib/deploy/ffjcext.zip of firefox java console.
- TODO: install it.

* Fri Apr 27 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.01-alt2
- added dependency on libstdc++3.3

* Tue Apr 10 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.01-alt1.1
- x86_64 fixes

* Fri Apr 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.01-alt1
- 1.6.0 update 1

* Fri Apr 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0-alt0.6
- fixed by hands man page compression (for alternatives) (see #11383)
- x86_64 fixes

* Fri Mar 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0-alt0.5
- added desktop package for version-independent desktop resources
- todo: merge and fix .desktops, 
  remove plugin desktop resources from jre.

* Thu Mar 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0-alt0.4
- added hack around find-requires

* Thu Mar 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0-alt0.3
- added Provides: /usr/bin/javac to devel (at@ suggest)

* Sat Mar 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0-alt0.1
- initial version based on j2se1.5
  features of new version 6:
  * it does not have kinit, klist and ktab - removed
  * it has "early access" Apache Derby database (a pure Java relational database engine)
  - not packaged; TODO: package/notice in README
   TODO: db, jre/lib/desktop (looks like it should be in separate package)

