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
%define major 1.5
%define minor 0
%define oldorigin       sun
%define origin          sun
%define priority        1503
%define javaver         %major.%minor
%define buildver        22

%define jppname         java-%{javaver}-%{origin}
%define javaws_ver      %{javaver}

%define toplevel_dir    jdk%{javaver}_%{buildver}
%define distversion	5.0u%{buildver}

%define label -%{name}

Name:           %jppname
Version:        %{javaver}.%{buildver}
Release:        alt6
Epoch:          0
Summary:        Java 2 Runtime Environment, Standard Edition
License:        Operating System Distributor License for Java version 1.1
Group:          System/Base
URL:            http://java.sun.com/j2se/%{javaver}
Packager:       Igor Yu. Vlasenko <viy@altlinux.org>

%def_enable headless
%def_enable demo
%def_disable fonts
%def_disable jvmjardir
%def_disable accessibility
%def_disable alsa_subpackage
%def_enable jdbc_subpackage
%def_disable control_panel
%ifarch x86_64
%def_disable javaws
%def_disable moz_plugin
%def_disable desktop
%else
%def_disable javaws
%def_disable moz_plugin
%def_disable desktop
%endif
%def_with gcc32_abi

%define sdklnk          java-%{javaver}-%{origin}
%define jrelnk          jre-%{javaver}-%{origin}
%define sdkdir          %{jppname}-%{version}
%define jredir          %{sdkdir}/jre
%define sdkbindir       %{_jvmdir}/%{sdklnk}/bin
%define sdklibdir       %{_jvmdir}/%{sdklnk}/lib
%define jrebindir       %{_jvmdir}/%{jrelnk}/bin
%if_enabled jvmjardir
%define jvmjardir       %{_jvmjardir}/%{jppname}-%{version}
%endif

%define cgibindir       %{_var}/www/cgi-bin
# --- jpackage compatibility stuff ends here ---

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

%if_with gcc32_abi
%define mozplugindir %{_jvmdir}/%{sdkdir}/jre/plugin/%libarch/ns7
%else
%define mozplugindir %{_jvmdir}/%{sdkdir}/jre/plugin/%libarch/ns7-gcc29
%endif
%define mozilla_java_plugin_so %mozplugindir/libjavaplugin_oji.so

# --- jpackage compatibility stuff starts here ---
Provides:       jre-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}
Provides:       jre-%{origin} = %{epoch}:%{version}-%{release}
Provides:       jre-%{javaver}, java-%{javaver}, jre = %{epoch}:%{javaver}
Provides:       java-%{origin} = %{epoch}:%{version}-%{release}
Provides:       java = %{epoch}:%{javaver}
%if_disabled headless
Provides:       jndi = %{epoch}:%{version}, jndi-ldap = %{epoch}:%{version}
Provides:       jndi-cos = %{epoch}:%{version}, jndi-rmi = %{epoch}:%{version}
Provides:       jndi-dns = %{epoch}:%{version}
Provides:       jaas = %{epoch}:%{version}
Provides:       jsse = %{epoch}:%{version}
Provides:       jce = %{epoch}:%{version}
Provides:       jdbc-stdext = %{epoch}:3.0, jdbc-stdext = %{epoch}:%{version}
Provides:       java-sasl = %{epoch}:%{version}
%endif
# --- jpackage compatibility stuff ends here ---

Obsoletes: j2se%major-%origin

%if_enabled headless
Requires: %{name}-headless = %{?epoch:%epoch:}%version-%release
%endif
Requires: fonts-ttf-java-%{origin} >= %version-%release
Requires: java-common
Requires: /proc
Requires(post,preun): alternatives >= 0.4

Source0: http://download.java.net/dlj/binaries/jdk-%distversion-dlj-linux-i586.bin
Source1: http://download.java.net/dlj/binaries/jdk-%distversion-dlj-linux-amd64.bin

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
BuildRequires: /proc
BuildRequires: shared-mime-info >= 0.15-alt2
BuildRequires: desktop-file-utils
### against #16510; 
### found in plugin/i386/ns7/libjavaplugin_oji.so, but can be anywhere:
### yes, they doesn't link against stdc++!!!
Requires: libstdc++3.3

%set_compress_method none
%set_verify_elf_method none
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


%if_enabled headless
%package        headless
Summary:        Java Runtime Environment, without audio and video support
Group:          Development/Java
Requires: fonts-ttf-java-%{origin} >= %version-%release
Requires(post,preun): alternatives >= 0.4

# --- fedora compatibility stuff starts here ---
Provides:       jre-%{javaver}-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides:       jre-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides:       jre-%{javaver}-headless = %{epoch}:%{version}-%{release}
Provides:       java-%{javaver}-headless = %{epoch}:%{version}-%{release}
Provides:       jre-headless = %{javaver}
Provides:       java-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides:       java-headless = %{epoch}:%{javaver}
# --- fedora compatibility stuff ends here ---

# --- jpackage compatibility stuff starts here ---
Provides:       jndi = %{epoch}:%{version}, jndi-ldap = %{epoch}:%{version}
Provides:       jndi-cos = %{epoch}:%{version}, jndi-rmi = %{epoch}:%{version}
Provides:       jndi-dns = %{epoch}:%{version}
Provides:       jaas = %{epoch}:%{version}
Provides:       jsse = %{epoch}:%{version}
Provides:       jce = %{epoch}:%{version}
Provides:       jdbc-stdext = %{epoch}:4.1, jdbc-stdext = %{epoch}:%{version}
Provides:       java-sasl = %{epoch}:%{version}
# --- jpackage compatibility stuff ends here ---

%description    headless
This package contains the Java Runtime Environment for %{name}
without audio and video support.
Install this package if you need to run Java applications
in server mode.

For audio and video support install the %{name} package.

The Java Runtime Environment contains the Java virtual machine, 
runtime class libraries, and Java application launcher that are 
necessary to run programs written in the Java programming language. 
It is not a development environment and does not contain development 
tools such as compilers or debuggers.  For development tools, see the 
Java SDK, Standard Edition.
%endif

%package        devel
Summary:        Java 2 SDK, Standard Edition
Group:          Development/Java
Provides: /usr/bin/javac
Provides: jdk = %javaver
Requires: %name = %{?epoch:%epoch:}%version-%release
Requires(post,preun): alternatives >= 0.4
Obsoletes: jdk-%origin j2sdk-%origin
# --------- rename stuff ------------------
Provides:       j2se%major-%origin-devel = %{version}
Obsoletes:      j2se%major-%origin-devel < 1.5.0.12
# -----------------------------------------

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
Obsoletes: j2se%major-%origin-source

%description source
Java programming language source files for all classes that make up
the Java 2 core API.

%if_enabled demo
%package        demo
Summary:        Demo applets and programs for the Java 2 SDK
Group: Development/Java
AutoReqProv: no
Obsoletes:      j2se%major-%origin-demo

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
Requires: %name = %{?epoch:%epoch:}%version-%release
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
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description    alsa
This package contains Advanced Linux Sound Architecture (ALSA) support
libraries for %{name}.
%endif # enabled alsa_subpackage

%if_enabled jdbc_subpackage
%package        jdbc
Summary:        Native library for JDBC support in Java
Group:          Development/Databases
Requires:       %name = %{?epoch:%epoch:}%version-%release

%description    jdbc
This package contains the JDBC/ODBC bridge driver for %{name}.
%endif # enabled jdbc_subpackage

%if_enabled javaws
%package javaws
Summary: Java Web Start
Group: Networking/Other
Requires: %name = %{?epoch:%epoch:}%version-%release
Requires(post,preun): alternatives >= 0.4
# --- jpackage compatibility stuff starts here ---
Provides:       javaws = %{epoch}:%{javaws_ver}
Obsoletes:      javaws-menu
# --- jpackage compatibility stuff ends here ---
Obsoletes:      j2se%major-%origin-javaws

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
Provides: fonts-ttf-java-%{origin} = %version
Provides: fonts-ttf-j2se-%origin = %version-%release
Obsoletes: fonts-ttf-j2se-%origin < %version-%release
Obsoletes: fonts-ttf-java-1.4.2-sun
# hack around apt (to remove when apt will be fixed)
Provides: /usr/share/fonts/ttf/j2se-sun
Provides: /usr/share/fonts/ttf/j2se-sun-oblique
# --- jpackage compatibility stuff starts here ---
Provides:       java-fonts = %{epoch}:%{javaver}, java-%{javaver}-fonts
Conflicts:      java-%{javaver}-ibm-fonts, java-%{javaver}-blackdown-fonts
Conflicts:      java-%{javaver}-bea-fonts
Obsoletes:      java-1.3.1-fonts, java-1.4.0-fonts, java-1.4.1-fonts, java-1.4.2-fonts
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

%if_enabled control_panel
# fix up ControlPanel APPHOME and bin locations
sed -i 's|APPHOME=.*|APPHOME=%{_jvmdir}/%{jredir}|' jre/bin/ControlPanel
sed -i 's|/usr/bin/||g' jre/bin/ControlPanel
# 1.6.0 compat symlink
ln -s ControlPanel jre/bin/jcontrol

# fix up (create new) HtmlConverter
cat > bin/HtmlConverter << EOF
%{jrebindir}/java -jar %{sdklibdir}/htmlconverter.jar $*
EOF
%endif

%if_enabled moz_plugin
# fix up java-rmi.cgi PATH
sed -i 's|PATH=.*|PATH=%{jrebindir}|' bin/java-rmi.cgi

# # install java-rmi-cgi
# install -D -m 755 bin/java-rmi.cgi $RPM_BUILD_ROOT%{cgibindir}/java-rmi-%{version}.cgi
%endif

# main files
install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
cp -a bin include lib src.zip $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}

%if_enabled jvmjardir
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
%endif

# rest of the jre
cp -a jre/bin jre/lib $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}
%if_enabled javaws
cp -a jre/javaws $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}
%endif
%if_enabled moz_plugin
cp -a jre/plugin $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}
%endif
install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/endorsed

# versionless symlinks
pushd $RPM_BUILD_ROOT%{_jvmdir}
ln -s %{jredir} %{jrelnk}
ln -s %{sdkdir} %{sdklnk}
popd

%if_enabled jvmjardir
pushd $RPM_BUILD_ROOT%{_jvmjardir}
ln -s %{sdkdir} %{jrelnk}
ln -s %{sdkdir} %{sdklnk}
popd
%endif

# man pages
install -d -m 755 $RPM_BUILD_ROOT%{_man1dir}
for manpage in man/man1/*; do
  install -m 644 -p $manpage $RPM_BUILD_ROOT%{_man1dir}/`basename $manpage .1`%label.1
done

# demo
%if_enabled demo
cp -a demo sample %buildroot%{_jvmdir}/%{sdkdir}
%endif

# Remove unpackaged files
%if_with gcc32_abi
rm -f %buildroot%{_jvmdir}/%{jredir}/lib/%libarch/*_gcc29.so
rm -rf %buildroot%{_jvmdir}/%{jredir}/plugin/%libarch/*-gcc29
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

%if_enabled control_panel
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

%if_enabled control_panel
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
echo java-headless >j2se-headless-buildreq-substitute
echo java-devel >j2se-devel-buildreq-substitute
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
install -m644 j2se-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name
install -m644 j2se-headless-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-headless
install -m644 j2se-devel-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-devel

install -d %buildroot%_altdir

# J2SE alternative
cat <<EOF >%buildroot%_altdir/%name-java
%{_bindir}/java	%{_jvmdir}/%{jredir}/bin/java	%priority
%_man1dir/java.1.gz	%_man1dir/java%{label}.1.gz	%{_jvmdir}/%{jredir}/bin/java
EOF
# binaries and manuals
for i in keytool policytool servertool pack200 unpack200 \
orbd rmid rmiregistry tnameserv
do
  cat <<EOF >>%buildroot%_altdir/%name-java
%_bindir/$i	%{_jvmdir}/%{jredir}/bin/$i	%{_jvmdir}/%{jredir}/bin/java
%_man1dir/$i.1.gz	%_man1dir/${i}%{label}.1.gz	%{_jvmdir}/%{jredir}/bin/java
EOF
done

%if_enabled control_panel
cat <<EOF >>%buildroot%_altdir/%name-java
%{_bindir}/ControlPanel	%{_jvmdir}/%{jredir}/bin/ControlPanel	%{_jvmdir}/%{jredir}/bin/java
%{_bindir}/jcontrol	%{_jvmdir}/%{jredir}/bin/jcontrol	%{_jvmdir}/%{jredir}/bin/java
EOF
%endif
# ----- JPackage compatibility alternatives ------
cat <<EOF >>%buildroot%_altdir/%name-java
%{_jvmdir}/jre	%{_jvmdir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmdir}/jre-%{origin}	%{_jvmdir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmdir}/jre-%{javaver}	%{_jvmdir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
%if_enabled jvmjardir
%{_jvmjardir}/jre	%{_jvmjardir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmjardir}/jre-%{origin}	%{_jvmjardir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmjardir}/jre-%{javaver}	%{_jvmjardir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
%endif
EOF
# ----- end: JPackage compatibility alternatives ------


# Javac alternative
cat <<EOF >%buildroot%_altdir/%name-javac
%_bindir/javac	%{_jvmdir}/%{sdkdir}/bin/javac	%priority
%_man1dir/javac.1.gz	%_man1dir/javac%{label}.1.gz	%{_jvmdir}/%{sdkdir}/bin/javac
EOF

# binaries and manuals
for i in appletviewer extcheck idlj jar jarsigner javadoc javah javap jdb native2ascii rmic serialver apt jconsole jinfo jmap jps jsadebugd jstack jstat jstatd
do
  if [ -e $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/bin/$i ]; then
  cat <<EOF >>%buildroot%_altdir/%name-javac
%_bindir/$i	%{_jvmdir}/%{sdkdir}/bin/$i	%{_jvmdir}/%{sdkdir}/bin/javac
%_man1dir/$i.1.gz	%_man1dir/${i}%{label}.1.gz	%{_jvmdir}/%{sdkdir}/bin/javac
EOF
  fi
done
# binaries w/o manuals
for i in HtmlConverter
do
  cat <<EOF >>%buildroot%_altdir/%name-javac
%_bindir/$i	%{_jvmdir}/%{sdkdir}/bin/$i	%{_jvmdir}/%{sdkdir}/bin/javac
EOF
done

# ----- JPackage compatibility alternatives ------
  cat <<EOF >>%buildroot%_altdir/%name-javac
%{_jvmdir}/java	%{_jvmdir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmdir}/java-%{origin}	%{_jvmdir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmdir}/java-%{javaver}	%{_jvmdir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
%if_enabled jvmjardir
%{_jvmjardir}/java	%{_jvmjardir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmjardir}/java-%{origin}	%{_jvmjardir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmjardir}/java-%{javaver}	%{_jvmjardir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
%endif
EOF
# ----- end: JPackage compatibility alternatives ------


%if_enabled moz_plugin
# Mozilla plugin alternative
cat <<EOF >%buildroot%_altdir/%name-mozilla
%browser_plugins_path/libjavaplugin_oji.so	%mozilla_java_plugin_so	%priority
EOF
%endif	# enabled moz_plugin

%if_enabled javaws
# Java Web Start alternative
cat <<EOF >%buildroot%_altdir/%name-javaws
%_bindir/javaws	%{_jvmdir}/%{jredir}/bin/javaws	%{_jvmdir}/%{jredir}/bin/java
%_man1dir/javaws.1.gz	%_man1dir/javaws%label.1.gz	%{_jvmdir}/%{jredir}/bin/java
EOF
# ----- JPackage compatibility alternatives ------
cat <<EOF >>%buildroot%_altdir/%name-javaws
%{_datadir}/javaws	%{_jvmdir}/%{jredir}/bin/javaws	%{_jvmdir}/%{jredir}/bin/java
EOF
# ----- end: JPackage compatibility alternatives ------
%endif	# enabled javaws

# hack (see #11383) to enshure that all man pages will be compressed
for i in $RPM_BUILD_ROOT%_man1dir/*.1; do
    [ -f $i ] && gzip -9 $i
done

%if_enabled headless
%post headless
%else
%post
%endif
%force_update_alternatives

##################################################
# - END alt linux specific, shared with openjdk -#
##################################################


%files
%if_enabled control_panel
# common between plugin and javaws (TODO: desktop)
%{_datadir}/pixmaps/%{name}.png
%{_niconsdir}/%{name}.png
%endif
%if_enabled headless
%{_jvmdir}/%{jredir}/bin/policytool
%{_jvmdir}/%{jredir}/lib/%libarch/awt_robot
%{_jvmdir}/%{jredir}/lib/%libarch/libjsoundalsa.so
%{_jvmdir}/%{jredir}/lib/%libarch/motif21/libmawt.so
%{_jvmdir}/%{jredir}/lib/%libarch/xawt/libmawt.so

%files headless
%exclude %{_jvmdir}/%{jredir}/bin/policytool
%exclude %{_jvmdir}/%{jredir}/lib/%libarch/awt_robot
%exclude %{_jvmdir}/%{jredir}/lib/%libarch/libjsoundalsa.so
%exclude %{_jvmdir}/%{jredir}/lib/%libarch/motif21/libmawt.so
%exclude %{_jvmdir}/%{jredir}/lib/%libarch/xawt/libmawt.so
%_sysconfdir/buildreqs/packages/substitute.d/%name-headless
%endif
%doc jre/CHANGES jre/COPYRIGHT jre/LICENSE jre/README jre/Welcome.html
%doc jre/THIRDPARTYLICENSEREADME.txt
%doc README.alt
# jpackage links #
%{_jvmdir}/%{jrelnk}
%if_enabled jvmjardir
%{jvmjardir}
%{_jvmjardir}/%{jrelnk}
%endif
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
%{_jvmdir}/%{jredir}/lib/locale
%exclude %{_jvmdir}/%{jredir}/lib/locale/*/LC_MESSAGES/sunw_java_plugin.mo
%exclude %{_jvmdir}/%{jredir}/lib/%libarch/libjavaplugin_jni.so
%exclude %{_jvmdir}/%{jredir}/lib/%libarch/libjavaplugin_nscp*.so
%exclude %{_jvmdir}/%{jredir}/lib/plugin.jar
%exclude %{_jvmdir}/%{jredir}/plugin
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
%config(noreplace) %{_jvmdir}/%{jredir}/lib/management/*
%{_jvmdir}/%{jredir}/lib/fontconfig.*.bfc
%{_jvmdir}/%{jredir}/lib/fontconfig.*.properties.src
#%{_jvmdir}/%{jredir}/lib/security/*.jar
%{_jvmdir}/%{jredir}/lib/security/local_policy.jar
%{_jvmdir}/%{jredir}/lib/security/US_export_policy.jar
%_man1dir/java%label.1*
%_man1dir/keytool%label.1*
%_man1dir/kinit%label.1*
%_man1dir/klist%label.1*
%_man1dir/ktab%label.1*
%_man1dir/orbd%label.1*
%_man1dir/policytool%label.1*
%_man1dir/rmid%label.1*
%_man1dir/rmiregistry%label.1*
%_man1dir/servertool%label.1*
%_man1dir/tnameserv%label.1*
%_man1dir/pack200%label.1*
%_man1dir/unpack200%label.1*
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
%if_enabled jvmjardir
%{_jvmjardir}/%{sdklnk}
%endif
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
%mozplugindir
%dir %{_jvmdir}/%{jredir}/plugin
%dir %{_jvmdir}/%{jredir}/plugin/%libarch
%dir %{_jvmdir}/%{jredir}/lib/%libarch
%{_jvmdir}/%{jredir}/lib/%libarch/libjavaplugin_jni.so
%{_jvmdir}/%{jredir}/lib/%libarch/libjavaplugin_nscp*.so
%dir %{_jvmdir}/%{jredir}/lib/locale
%dir %{_jvmdir}/%{jredir}/lib/locale/*
%dir %{_jvmdir}/%{jredir}/lib/locale/*/LC_MESSAGES
%{_jvmdir}/%{jredir}/lib/locale/*/LC_MESSAGES/sunw_java_plugin.mo
%{_jvmdir}/%{jredir}/lib/plugin.jar
%{_jvmdir}/%{jredir}/plugin/desktop
%{_datadir}/applications/%{name}-control-panel.desktop
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
%if_enabled control_panel
%exclude %{_niconsdir}/%{name}.png
%endif
%endif

%if_enabled javaws
%files javaws
%doc README.alt
%_altdir/%name-javaws
%{_jvmdir}/%{jredir}/bin/javaws
%{_jvmdir}/%{jredir}/lib/javaws
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
* Tue Nov 28 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.22-alt6
- removed obsolete exports in jvmjardir
- removed obsolete security policy alternatives in _jvmprivdir
- better font sharing

* Sat Oct 10 2015 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.22-alt5
- added headless subpackage

* Tue Aug 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.22-alt4
- added epoch to strict Requires

* Wed Feb 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.22-alt3
- maintainance release - synced specs

* Fri Dec 18 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.22-alt2
- fixed shared libjvm.so provides

* Sat Nov 07 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.22-alt1
- new version

* Thu Oct 08 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.21-alt2
- added shared libjvm.so provides

* Mon Oct 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.21-alt1
- new version

* Wed Jul 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.19-alt1
- new version

* Wed May 06 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.18-alt1
- new version

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.17-alt3
- alternatives.prov friendly alternatives in jre

* Thu Dec 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.17-alt2
- disabled xml-commons-apis.jar symlink

* Thu Dec 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.17-alt1
- new version

* Sat Nov 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.16-alt3
- support for alternatives 0.4

* Mon Nov 17 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.16-alt2
- removed obsolete update_menu calls

* Tue Jul 22 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.16-alt1
- new version
- disabled alsa subpackage (libalsa is a neglectable dependency)

* Thu Apr 24 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.15-alt1
- new version
- javaws fixes (#14236)

* Sat Oct 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.13-alt1
- new version
- built from dlj binaries
- use Operating System Distributor License for Java version 1.1

* Fri Sep 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.12-alt1.1
- ldd crashes in verify_elf; added hack around

* Sat Sep 01 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.12-alt1
- new version
- renamed to java-version-origin
- alternatives cleanup
- applied new font policy
- added jre/lib/deploy/ffjcext.zip of firefox java console.
- TODO: install it.

* Thu Mar 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.11-alt5
- added Provides: /usr/bin/javac to devel (at@ suggest)
- fixed man pages compression

* Sat Mar 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.11-alt4
- add_findprov_lib_path %{_jvmdir}/%{jredir}/lib/%libarch/server
  for apps that links with libjvm.so 

* Thu Mar 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.11-alt3
- changed buildreq provides from j2se{,-devel} to java{,-devel}
- removed old profile scripts (they are handled in java-common)

* Wed Mar 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.11-alt2.2
- removed symlink at previous JVM location (/usr/lib/j2se1.5-sun)
  as caused upgrade troubles and used nowhere.

* Tue Mar 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.11-alt2.1
- fix for x86_64 

* Tue Mar 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0.11-alt2
- merged jpackage spec
- set priority 1503 (according to jpackage)
- added .desktop files
- added epoch: 0
- spawned alsa supbackage
- moved plugin-specific stuff to mozilla-plugin
- changed j2se layout in filesystem to /usr/lib/jvm;
  old locations are provided as symlinks 
  (to be compatible with both JPackage and old ALT).
- a bundle of 'Provides:' added to be JPackage compatible;
- added new JPackage compatible alternatives;
- removed support for ns4_plugin -- this jre does not have it;
- removed profile symlinks from /etc/profile.d 
  (see #9766; java_home finder should be implemented there)

* Wed Jan 31 2007 Igor Vlasenko <viy@altlinux.ru> 1.5.0_11-alt1
- Release 1.5.0_11

* Wed Oct 04 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.0_09-alt1
- Release 1.5.0_09

* Sun Aug 27 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.0_08-alt1
- Release 1.5.0_08

* Tue Jun 20 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.0_07-alt1
- Release 1.5.0_07

* Thu Mar 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.0_06-alt2
- Relaxed ELF symbols check
- Added soname dependencies to BuildRequires
- Made sure JAVA_HOME is in /usr/lib independently of the architecture
- Moved demo and source back to %%java_home
- Renamed the fonts package to respect the latest policy
- Moved oblique-fonts to the fonts package

* Sun Feb 19 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.0_06-alt1
- 1.5.0_06
- Fixed filelist error for x86_64
- Sync with j2se1.4-sun-1.4.2_09-alt1:
- Provide the old name for mozilla-plugin-%%name

* Sun Oct 30 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.0_05-alt1
- 1.5.0_05
- Sync with j2se1.4-sun-1.4.2_09-alt1:
- Renamed subpackage %%name-plugin-mozilla to mozilla-plugin-%%name [bug 8114]
- Moved the mozilla plugin alternative symlink to browser-plugins-npapi
  [bug 7461]
- Use macros from browser-plugins-npapi-devel
- Added the bundled desktop files to the JRE package
- Resolved filelist conflict between j2se1.5-sun and j2se1.5-sun-javaws

* Wed Aug 03 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.0_04-alt3
- Corrected build for x86_64

* Thu Jul 28 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.0_04-alt2
- Updated to 1.5.0_04
- Merged x86_64 changes made by Anton Kachalov
- Moved the Mozilla plugin to browser-plugins-npapi

* Sat Feb 05 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.0_01-alt1
- New upstream release
- Synced with j2se1.4-sun changes

* Wed Oct 13 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.0-alt3
- Disabled dependency search for demo to eliminate bogus dependencies

* Thu Oct 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.0-alt2
- Corrected slave records in alternatives

* Fri Oct 01 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.0-alt1
- Updated to the 1.5.0 release
- New alternatives format
- Require /proc

* Sun Mar 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.0-alt0.1.beta1
- Updated to 1.5.0 beta 1
- Conditionally disable fonts
- Minor fix in javaws launcher

* Mon Dec 22 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2_03-alt1
- Bugfix upstream release

* Fri Dec 19 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2_02-alt3
- Added /usr/sbin/update-alternatives to install-time dependencies

* Wed Dec 03 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2_02-alt2
- Fixed filelist bug

* Wed Nov 12 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2_02-alt1
- New upstream release
- Relaxed TEXTREL check on ELF files
- Added some files that were reported as unlisted

* Thu Oct 23 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2_01-alt2
- Added locations of binary libraries to %%_findprov_lib_path

* Sat Oct 04 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2_01-alt1
- New upstream release

* Sun Jul 13 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2-alt1
- J2SE 1.4.2
- Reformed fonts package into j2se-sun-fonts, shared between various
  J2SE installations
- javaws subpackage for the bundled Java Web Start
- Added kinit, klist and ktab manpages to the filelist.
  The tools themselves will not be symlinked to /usr/bin
  due to conflicts with the krb5-workstation package
- Created README.alt describing package layout specifics,
  as required by the J2SE license

* Tue Mar 18 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1_02-alt1
- 1.4.1_02

* Tue Jan 14 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1_01-alt5
- Added Requires: to devel subpackage for the main package

* Thu Dec 26 2002 AEN <aen@altlinux.ru> 1.4.1_01-alt4
- added Provides: java_sun-fonts to fonts package

* Mon Nov 18 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1_01-alt3
- The j2se package does not provide /usr/bin/java, instead it requires
  java-common
- Moved profile scripts to /usr/lib/j2se1.4-sun

* Wed Nov 13 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1_01-alt2
- The j2se package provides /usr/bin/java
- Target profile scripts moved out of /etc/profile.d to /usr/share/j2se1.4-sun

* Tue Nov 12 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1_01-alt1
- Renamed to j2se1.4-sun
- Renamed subpackages: src to source, odbc to jdbc
- Added fonts subpackage, using fontconfig
- Moved demo and source to /usr/share/j2se1.4-sun
- Provide /usr/lib/jdk as an alternatives-driven link, for seamless upgrades
  from obsolete JDK packages to j2se1.4-sun-devel

* Tue Jun 18 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.0_01-alt1
- Renamed to j2sdk-sun
- Arch is now i586
- Eliminated chdirs in the install script
- Included JRE README and license in the file list

* Sat Mar 30 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.0-alt2
- Bumped to alt2. Thanks, Ivan, you did all the work.
- Added orbd and servertool to executable symlinks
- spec cleanup

* Sat Mar  2 2002 Ivan Zakharyaschev <imz@altlinux.ru> 1.4.0-alt1imz
- 1.4.0
- NOT DONE: Sun Inc. changed the name from jdk to j2sdk; we change it, too: it sounds
  logical (1.4.0 is the version of Java2);
- 4 entries in %%files changed:
  + include-old dropped;
  + jre/lib/tzmappings files replaced by zi/ subdirectory;
  + jre/lib/jvm.cfg moved into i386/ subdirectory;
  + src.jar -> src.zip;
- using ns610 instead of ns600 plugin for Mozilla; now the version
  of Java2 environment is appended to the plugin libraries --
  modify scriplets accordingly;

* Sat Jun 16 2001 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.1-alt2
- corrected generation of the filelist

* Sat Jun 16 2001 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.1-alt1
- 1.3.1
- config(noreplace) on configuration files
- odbc subpackage

* Fri May 04 2001 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.0_02-alt3
- Omit version in install directory name to make upgrades painless
- Fixed uninstallation scripts

* Sat Apr 28 2001 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.0_02-alt2
- Unbundled plugins because they cast excessive dependencies
- update-alternatives for plugins

* Fri Apr 27 2001 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.0_02-alt1
- Updated version
- New distribution
- Renamed to jdk-sun to leave room for jdk-ibm or others

* Sun Dec 10 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3-1mdk_mhz
- initial package
