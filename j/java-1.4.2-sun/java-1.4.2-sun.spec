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
%define major 1.4
%define minor 2
%define origin          sun
%define priority        1423
%define javaver         %major.%minor
%define buildver        17

%define jppname         java-%{javaver}-%{origin}
%define javaws_ver      %{javaver}

%define toplevel_dir    j2sdk%{javaver}_%{buildver}
%define distversion 1_4_2_%{buildver}

%define altname  j2se%major-%origin
%define label -%{jppname}

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

%def_enable fonts
%ifarch x86_64
%def_disable javaws
%def_disable moz_plugin
%else
%def_enable javaws
%def_enable moz_plugin
%endif
%def_with gcc32_abi

%ifarch x86_64
%define libarch	    amd64
%else
%define libarch	    i386
%endif

%define fontdir		%_datadir/fonts/ttf/j2se-%origin

%if_with gcc32_abi
%define mozplugindir %{_jvmdir}/%{sdkdir}/jre/plugin/%libarch/ns610-gcc32
%else
%define mozplugindir %{_jvmdir}/%{sdkdir}/jre/plugin/%libarch/ns610
%endif

# --- jpackage compatibility stuff starts here ---
#if jpackage-utils stuff (to remove ufter upgrade)
%define _jvmdir	%{_prefix}/lib/jvm
%define _jvmjardir	%{_prefix}/lib/jvm-exports
%define _jvmprivdir	%{_prefix}/lib/jvm-private
%define _javadir        %{_datadir}/java
%define _jnidir        %{_prefix}/lib/java
#else
#Requires:       jpackage-utils >= 0:1.5.38
#BuildRequires:  jpackage-utils >= 0:1.5.38
Conflicts:      kaffe
#endif
#-----

Name:           %jppname
Version:        %{javaver}.%{buildver}
Release:        alt3
Epoch:          0
Summary:        Java 2 Runtime Environment, Standard Edition
License:        Sun Binary Code License
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
#Provides:       java-sasl = %{epoch}:%{version}
# --- jpackage compatibility stuff ends here ---

Provides: j2se = %javaver
Provides: jre = %javaver, java2 = %javaver
Obsoletes: %altname


Requires: fonts-ttf-j2se-%origin >= %version-%release
Requires: java-common
Requires: /proc
Requires(post,preun): alternatives >= 0.4

Source0: j2sdk-%distversion-linux-i586.bin

ExclusiveArch: i586 

%ifarch x86_64
%else
%define jdksource %SOURCE0
%endif

# jpackage use perl -p -i -e, we use subst
# BuildPreReq: perl

BuildPreReq: browser-plugins-npapi-devel
BuildRequires: libalsa
BuildRequires: libunixODBC
#BuildRequires: xorg-x11-devel
BuildRequires: libX11 libXext libXi libXp libXt libXtst libSM libICE


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

%package        devel
Summary:        Java 2 SDK, Standard Edition
Group:          Development/Java
Provides: j2se-devel = %javaver
Provides: /usr/bin/javac
Provides: jdk = %javaver, j2sdk = %javaver
Requires: %name = %version-%release
Requires(post,preun): alternatives >= 0.4
Obsoletes: jdk-%origin j2sdk-%origin
Obsoletes: %altname-devel

# --- jpackage compatibility stuff starts here ---
Provides:       java-sdk-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}
Provides:       java-sdk-%{origin} = %{epoch}:%{version}-%{release}
Provides:       java-sdk-%{javaver}, java-sdk = %{epoch}:%{javaver}
Provides:       java-devel-%{origin} = %{epoch}:%{version}-%{release}
Provides:       java-%{javaver}-devel, java-devel = %{epoch}:%{javaver}
# --- jpackage compatibility stuff ends here ---

%description    devel
The Java(tm) Development Kit (JDK(tm)) contains the software and tools that
developers need to compile, debug, and run applets and applications
written using the Java programming language.

Install this package if you need to develop and build Java applications.

%package source
Summary: Source files for the Java 2 SDK
Group: Development/Java
Obsoletes: %altname-source

%description source
Java programming language source files for all classes that make up
the Java 2 core API.

%package        demo
Summary:        Demo applets and programs for the Java 2 SDK
Group: Development/Java
AutoReqProv: no
Obsoletes:      %altname-demo

%description    demo
This package contains demonstration files for %{name}.

These include examples, with source code, of programming for the Java 
platform that use Swing and other Java Foundation Classes, and the Java
Platform Debugger Architecture.

%if_enabled moz_plugin
%package -n mozilla-plugin-%altname
Summary: Java Plug-In for Mozilla family browsers
Group: Networking/WWW
Provides: java2-plugin-mozilla = %javaver
Provides: %altname-plugin-mozilla
Obsoletes: %altname-plugin-mozilla
Requires: %name = %version-%release
Requires: browser-plugins-npapi
Requires(post,preun): alternatives >= 0.4
# --- jpackage compatibility stuff starts here ---
Provides:       java-plugin = %{epoch}:%{javaver}, java-%{javaver}-plugin = %{epoch}:%{version}
Conflicts:      java-%{javaver}-ibm-plugin, java-%{javaver}-blackdown-plugin
Conflicts:      java-%{javaver}-bea-plugin
Obsoletes:      java-1.3.1-plugin, java-1.4.0-plugin, java-1.4.1-plugin
# --- jpackage compatibility stuff ends here ---

%description -n mozilla-plugin-%altname
This package contains Java(TM) 2 Plug-In for Mozilla family web browsers.
%endif # enabled moz_plugin

%package        alsa
Summary:        ALSA support for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Obsoletes:      %altname-alsa

%description    alsa
This package contains Advanced Linux Sound Architecture (ALSA) support
libraries for %{name}.

%package        jdbc
Summary:        Native library for JDBC support in Java
Group:          Development/Databases
Provides:       j2se-jdbc = %javaver
Requires:       %name = %version-%release
Obsoletes:      %altname-jdbc

%description    jdbc
This package contains the JDBC/ODBC bridge driver for %{name}.

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
Obsoletes:      %altname-javaws

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

%if_enabled fonts
%package -n fonts-ttf-%jppname
Summary: TrueType fonts for Java 2 Standard Edition
Group: System/Fonts/True type
BuildRequires: mkfontscale
Requires: fontconfig
Provides: java_%origin-fonts = %version-%release
Obsoletes: j2se-%origin-fonts
Obsoletes: %altname-fonts
Provides: fonts-ttf-j2se-%origin = %version-%release
Obsoletes: fonts-ttf-j2se-%origin < %version-%release
# --- jpackage compatibility stuff starts here ---
Provides:       java-fonts = %{epoch}:%{javaver}, java-%{javaver}-fonts
Conflicts:      java-%{javaver}-ibm-fonts, java-%{javaver}-blackdown-fonts
Conflicts:      java-%{javaver}-bea-fonts
Obsoletes:      java-1.3.1-fonts, java-1.4.0-fonts, java-1.4.1-fonts
# --- jpackage compatibility stuff ends here ---

%description -n fonts-ttf-%jppname
This package contains the TrueType fonts for %{origin} JVMs.
%endif	# enabled fonts

%prep
MORE=10000 sh %jdksource <<EOF
yes
EOF
%setup -T -D -n %{toplevel_dir}
# fix perms
chmod -R u+w *

echo java >j2se-buildreq-substitute
echo java-devel >j2se-devel-buildreq-substitute

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
mozilla-plugin-%altname	- Java 2 plug-in for Mozilla family browsers
fonts-ttf-%jppname		- The TrueType fonts in %fontdir
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

%if_enabled moz_plugin
# fix up ControlPanel APPHOME and bin locations
%__subst 's|APPHOME=.*|APPHOME=%{_jvmdir}/%{jredir}|' jre/bin/ControlPanel
%__subst 's|/usr/bin/||g' jre/bin/ControlPanel

# fix up (create new) HtmlConverter
cat > bin/HtmlConverter << EOF
%{jrebindir}/java -jar %{sdklibdir}/htmlconverter.jar $*
EOF

# fix up java-rmi.cgi PATH
%__subst 's|PATH=.*|PATH=%{jrebindir}|' bin/java-rmi.cgi

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
install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/endorsed

# jce policy file handling
install -d -m 755 $RPM_BUILD_ROOT%{_jvmprivdir}/%{jppname}/jce/vanilla
for file in local_policy.jar US_export_policy.jar; do
  mv $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security/$file \
    $RPM_BUILD_ROOT%{_jvmprivdir}/%{jppname}/jce/vanilla
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

%if_enabled moz_plugin
# ControlPanel freedesktop.org menu entry
%__subst 's|INSTALL_DIR/JRE_NAME_VERSION|%{_jvmdir}/%{jredir}|g' jre/plugin/desktop/sun_java.desktop
%__subst 's|Name=.*|Name=Java Plugin Control Panel \(%{name}\)|' jre/plugin/desktop/sun_java.desktop
%__subst 's|Icon=.*|Icon=%{name}.png|' jre/plugin/desktop/sun_java.desktop
%__subst 's|Categories=.*|Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Sun-Java-%javaver;|' jre/plugin/desktop/sun_java.desktop

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
install -m 644 jre/plugin/desktop/sun_java.desktop  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-control-panel.desktop
install -m 644 jre/plugin/desktop/sun_java.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

cp -a jre/plugin $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}

# javaws freedesktop.org menu entry
cat >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-javaws.desktop << EOF
[Desktop Entry]
Name=Java Web Start (%{name})
Comment=Java Application Launcher
MimeType=application/x-java-jnlp-file
Exec=%{_jvmdir}/%{jredir}/javaws/javaws %%u
Icon=%{name}
Terminal=false
Type=Application
Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Sun-Java-%javaver;
EOF
%endif

# man pages
install -d -m 755 $RPM_BUILD_ROOT%{_man1dir}
for manpage in man/man1/*; do
  install -m 644 -p $manpage $RPM_BUILD_ROOT%{_man1dir}/`basename $manpage .1`%label.1
done

# demo
# install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{jppname}
# cp -a demo $RPM_BUILD_ROOT%{_datadir}/%{jppname}
install -d -m755 %buildroot%{_jvmdir}/%{sdkdir}
cp -a demo %buildroot%{_jvmdir}/%{sdkdir}


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

# Install substitute rules for buildreq
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
install -m644 j2se-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name
install -m644 j2se-devel-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-devel

%__install -d %buildroot%_altdir

# J2SE alternative
%__cat <<EOF >%buildroot%_altdir/%altname-j2se
%{_bindir}/java	%{jrebindir}/java	%priority
%_man1dir/java.1.gz	%_man1dir/java%{label}.1.gz	%{jrebindir}/java
EOF
# binaries and manuals
for i in keytool policytool servertool \
orbd rmid rmiregistry tnameserv
do
  %__cat <<EOF >>%buildroot%_altdir/%altname-j2se
%_bindir/$i	%{_jvmdir}/%{jredir}/bin/$i	%{jrebindir}/java
%_man1dir/$i.1.gz	%_man1dir/${i}%{label}.1.gz	%{jrebindir}/java
EOF
done

# ----- JPackage compatibility alternatives ------
%__cat <<EOF >>%buildroot%_altdir/%altname-j2se
%{_jvmdir}/jre	%{_jvmdir}/%{jrelnk}	%{jrebindir}/java
%{_jvmjardir}/jre	%{_jvmjardir}/%{jrelnk}	%{jrebindir}/java
%{_jvmdir}/jre-%{origin}	%{_jvmdir}/%{jrelnk}	%{jrebindir}/java
%{_jvmjardir}/jre-%{origin}	%{_jvmjardir}/%{jrelnk}	%{jrebindir}/java
%{_jvmdir}/jre-%{javaver}	%{_jvmdir}/%{jrelnk}	%{jrebindir}/java
%{_jvmjardir}/jre-%{javaver}	%{_jvmjardir}/%{jrelnk}	%{jrebindir}/java
EOF
%if_enabled moz_plugin
%__cat <<EOF >>%buildroot%_altdir/%altname-j2se
%{_bindir}/ControlPanel	%{jrebindir}/ControlPanel	%{jrebindir}/java
EOF
%endif
# JPackage specific: alternatives for security policy
%__cat <<EOF >>%buildroot%_altdir/%altname-j2se
%{_jvmdir}/%{jrelnk}/lib/security/local_policy.jar	%{_jvmprivdir}/%{jppname}/jce/vanilla/local_policy.jar	%{priority}
%{_jvmdir}/%{jrelnk}/lib/security/US_export_policy.jar	%{_jvmprivdir}/%{jppname}/jce/vanilla/US_export_policy.jar	%{_jvmprivdir}/%{jppname}/jce/vanilla/local_policy.jar
EOF
# ----- end: JPackage compatibility alternatives ------


# Javac alternative
%__cat <<EOF >%buildroot%_altdir/%altname-javac
%_bindir/javac	%{_jvmdir}/%{sdkdir}/bin/javac	%priority
%_prefix/lib/jdk	%{_jvmdir}/%{sdkdir}	%{_jvmdir}/%{sdkdir}/bin/javac
%_man1dir/javac.1.gz	%_man1dir/javac%{label}.1.gz	%{_jvmdir}/%{sdkdir}/bin/javac
EOF

# binaries and manuals
for i in appletviewer extcheck idlj jar jarsigner javadoc javah javap jdb native2ascii rmic serialver
do
  %__cat <<EOF >>%buildroot%_altdir/%altname-javac
%_bindir/$i	%{_jvmdir}/%{sdkdir}/bin/$i	%{_jvmdir}/%{sdkdir}/bin/javac
%_man1dir/$i.1.gz	%_man1dir/${i}%{label}.1.gz	%{_jvmdir}/%{sdkdir}/bin/javac
EOF
done
# binaries w/o manuals
for i in HtmlConverter jmap
do
  %__cat <<EOF >>%buildroot%_altdir/%altname-javac
%_bindir/$i	%{_jvmdir}/%{sdkdir}/bin/$i	%{_jvmdir}/%{sdkdir}/bin/javac
EOF
done

# ----- JPackage compatibility alternatives ------
  %__cat <<EOF >>%buildroot%_altdir/%altname-javac
%_prefix/lib/j2se	%{_jvmdir}/%{sdkdir}	%{_jvmdir}/%{sdkdir}/bin/javac
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
%__cat <<EOF >%buildroot%_altdir/%altname-mozilla
%browser_plugins_path/libjavaplugin_oji.so	%mozplugindir/libjavaplugin_oji.so	%priority
EOF
%endif	# enabled moz_plugin

%if_enabled javaws
# Java Web Start alternative
%__cat <<EOF >%buildroot%_altdir/%altname-javaws
%_bindir/javaws	%{_jvmdir}/%{jredir}/javaws/javaws	%{jrebindir}/java
%_man1dir/javaws.1.gz	%_man1dir/javaws%label.1.gz	%{jrebindir}/java
EOF
# ----- JPackage compatibility alternatives ------
%__cat <<EOF >>%buildroot%_altdir/%altname-javaws
%{_datadir}/javaws	%{_jvmdir}/%{jredir}/javaws/javaws	%{jrebindir}/java
EOF
# ----- end: JPackage compatibility alternatives ------
%endif	# enabled javaws

# Remove unpackaged files
%if_with gcc32_abi
%__rm -f %buildroot%{_jvmdir}/%{jredir}/lib/%libarch/*_gcc29.so
%__rm -rf %buildroot%{_jvmdir}/%{jredir}/plugin/%libarch/*-gcc29
%endif

%if_enabled moz_plugin
install -d -m 755 $RPM_BUILD_ROOT%{_niconsdir}
ln -s %{_datadir}/pixmaps/%{name}.png $RPM_BUILD_ROOT%{_niconsdir}/%{name}.png
%endif

# hack (see #11383) to enshure that all man pages will be compressed
for i in $RPM_BUILD_ROOT%_man1dir/*.1; do
    [ -f $i ] && gzip -9 $i
done

# HACK around find-requires
%define __find_requires    $RPM_BUILD_ROOT/.find-requires
cat > $RPM_BUILD_ROOT/.find-requires <<EOF
#!/bin/sh
(/usr/lib/rpm/find-requires | grep -v %{_jvmdir}/%{sdkdir}) | grep -v /usr/bin/java || :
EOF
chmod 755 $RPM_BUILD_ROOT/.find-requires
# end HACK around find-requires


%post
# ----- JPackage stuff ------
if [ -d %{_jvmdir}/%{jrelnk}/lib/security ]; then
  # Need to remove the old jars in order to support upgrading, ugly :(
  # update-alternatives fails silently if the link targets exist as files.
  rm -f %{_jvmdir}/%{jrelnk}/lib/security/{local,US_export}_policy.jar
fi

# %ifnarch x86_64
# if [ -f %{_sysconfdir}/mime.types ]; then
#    %__subst 's|application/x-java-jnlp-file.*||g' %{_sysconfdir}/mailcap.bak 2>/dev/null
#    echo "type=application/x-java-jnlp-file; description=\"Java Web Start\"; exts=\"jnlp\"" >> %{_sysconfdir}/mailcap 2>/dev/null

#    %__subst 's|application/x-java-jnlp-file.*||g' %{_sysconfdir}/mime.types 2>/dev/null
#    echo "application/x-java-jnlp-file      jnlp" >> %{_sysconfdir}/mime.types 2>/dev/null
# fi
# %endif
# ----- JPackage stuff ------


%pre
[ -L %{_jvmdir}/%{jredir}/lib/fonts ] || %__rm -rf %{_jvmdir}/%{jredir}/lib/fonts

%if_enabled fonts
%post -n fonts-ttf-%jppname
%_bindir/fc-cache %fontdir ||:

%triggerpostun -n fonts-ttf-%jppname -- j2se1.3-sun-fonts j2se1.4-sun-fonts j2se1.4-blackdown-fonts
# Recreate the cache removed by the font uninstall scripts
%_bindir/fc-cache %fontdir ||:

%postun -n fonts-ttf-%jppname
if [ "$1" = "0" ]; then
    %_bindir/fc-cache --system-only ||:
fi
%endif	# enabled fonts

%files
%doc jre/CHANGES jre/COPYRIGHT jre/LICENSE jre/README jre/Welcome.html
%doc jre/THIRDPARTYLICENSEREADME.txt
%doc README.alt
# jpackage links #
%{jvmjardir}
%{_jvmdir}/%{jrelnk}
%{_jvmjardir}/%{jrelnk}
# jpackage dirs
%{_jvmdir}/%{jredir}/lib/endorsed
%_altdir/%altname-j2se
%_sysconfdir/buildreqs/packages/substitute.d/%name
%dir %{_jvmdir}/%{sdkdir}
%dir %{_jvmdir}/%{jredir}
%dir %{_jvmdir}/%{jredir}/lib
%dir %{_jvmdir}/%{jredir}/lib/security
# .systemPrefs removed as they are not packaged in jpackage
#%{_jvmdir}/%{jredir}/.systemPrefs
%{_jvmdir}/%{jredir}/bin
%if_enabled javaws
#%exclude %{_jvmdir}/%{jredir}/bin/javaws
%endif
%{_jvmdir}/%{jredir}/lib/%libarch
%exclude %{_jvmdir}/%{jredir}/lib/%libarch/libJdbcOdbc.so
%exclude %{_jvmdir}/%{jredir}/lib/%libarch/libjsoundalsa.so
%{_jvmdir}/%{jredir}/lib/*.jar
%{_jvmdir}/%{jredir}/lib/*.txt
%{_jvmdir}/%{jredir}/lib/applet
%{_jvmdir}/%{jredir}/lib/audio
#%{_jvmdir}/%{jredir}/lib/classlist
%{_jvmdir}/%{jredir}/lib/cmm
%{_jvmdir}/%{jredir}/lib/ext
%{_jvmdir}/%{jredir}/lib/fonts
%{_jvmdir}/%{jredir}/lib/im
%{_jvmdir}/%{jredir}/lib/images
%if_enabled moz_plugin
# common between plugin and javaws (TODO: desktop)
%{_datadir}/pixmaps/%{name}.png
%{_niconsdir}/%{name}.png
%{_jvmdir}/%{jredir}/lib/locale
%exclude %{_jvmdir}/%{jredir}/lib/locale/*/LC_MESSAGES/sunw_java_plugin.mo
%exclude %{_jvmdir}/%{jredir}/lib/%libarch/libjavaplugin_jni.so
#exclude %{_jvmdir}/%{jredir}/lib/%libarch/libjavaplugin_nscp*.so
%exclude %{_jvmdir}/%{jredir}/lib/plugin.jar
%exclude %{_jvmdir}/%{jredir}/plugin
%endif
%{_jvmdir}/%{jredir}/lib/zi
%config(noreplace) %{_jvmdir}/%{jredir}/lib/*.properties
%config(noreplace) %{_jvmdir}/%{jredir}/lib/*.properties.??
#%config(noreplace) %{_jvmdir}/%{jredir}/lib/fontconfig.bfc
#%config(noreplace) %{_jvmdir}/%{jredir}/lib/fontconfig.properties.src
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/cacerts
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.policy
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.security
#%config(noreplace) %{_jvmdir}/%{jredir}/lib/management/*
#%{_jvmdir}/%{jredir}/lib/fontconfig.*.bfc
#%{_jvmdir}/%{jredir}/lib/fontconfig.*.properties.src
#%{_jvmdir}/%{jredir}/lib/security/*.jar
%{_jvmprivdir}/*
%ghost %{_jvmdir}/%{jredir}/lib/security/local_policy.jar
%ghost %{_jvmdir}/%{jredir}/lib/security/US_export_policy.jar
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

%files devel
%doc *README* LICENSE COPYRIGHT
# jpackage short links #
%{_jvmdir}/%{sdklnk}
%{_jvmjardir}/%{sdklnk}
%_altdir/%altname-javac
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

%files source
%{_jvmdir}/%{sdkdir}/src.zip

%files demo
#todo
#%dir %{_datadir}/%{jppname}
#%{_datadir}/%{jppname}/demo
%{_jvmdir}/%{sdkdir}/demo

%if_enabled moz_plugin
%files -n mozilla-plugin-%altname
%doc jre/ControlPanel.html
%_altdir/%altname-mozilla
%mozplugindir
%dir %{_jvmdir}/%{jredir}/plugin
%dir %{_jvmdir}/%{jredir}/plugin/%libarch
%{_jvmdir}/%{jredir}/lib/%libarch/libjavaplugin_jni.so
#%{_jvmdir}/%{jredir}/lib/%libarch/libjavaplugin_nscp*.so
%{_jvmdir}/%{jredir}/lib/locale/*/LC_MESSAGES/sunw_java_plugin.mo
%{_jvmdir}/%{jredir}/lib/plugin.jar
%{_jvmdir}/%{jredir}/plugin/desktop
%{_datadir}/applications/%{name}-control-panel.desktop
%endif

%files alsa
%{_jvmdir}/%{jredir}/lib/%libarch/libjsoundalsa.so

%files jdbc
%{_jvmdir}/%{jredir}/lib/%libarch/libJdbcOdbc.so

%if_enabled javaws
%files javaws
%doc README.alt
%_altdir/%altname-javaws
%dir %{_jvmdir}/%{jredir}/javaws
%{_jvmdir}/%{jredir}/javaws/javaws
%{_jvmdir}/%{jredir}/javaws/javawsbin
%{_jvmdir}/%{jredir}/javaws/*.jar
%{_jvmdir}/%{jredir}/javaws/*.gif
%doc %{_jvmdir}/%{jredir}/javaws/*.html
%{_jvmdir}/%{jredir}/javaws/resources
%config(noreplace) %{_jvmdir}/%{jredir}/javaws/javaws.policy
#%config(noreplace) %{_jvmdir}/%{jredir}/javaws/cacerts
%_man1dir/javaws%label.1*
%{_datadir}/applications/%{name}-javaws.desktop
%endif

%if_enabled fonts
%files -n fonts-ttf-%jppname
%doc LICENSE COPYRIGHT
%doc fontdoc/README.alt
%_sysconfdir/X11/fontpath.d/*
%dir %fontdir
%fontdir/fonts.scale
%fontdir/fonts.dir
%fontdir/*.ttf
%endif	# enabled fonts


%changelog
* Sun Oct 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2.17-alt3
- rebuild to repair requires

* Mon Nov 17 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2.17-alt2
- removed obsolete update_menu calls

* Wed Apr 16 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2.17-alt1
- new version

* Sat Oct 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2.16-alt1
- new version
- fonts package renamed to be stored in Sisyphus as separate package

* Sat Sep 01 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2.14-alt1
- new version
- renamed to java-1.4.2-sun
- cleaned up alternatives
- applied new font policy

* Thu Mar 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2.13-alt5
- added Provides: /usr/bin/javac to devel (at@ suggest)
- desktop fixes

* Sat Mar 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2.13-alt4
- add_findprov_lib_path %{_jvmdir}/%{jredir}/lib/%libarch/server
  for apps that links with libjvm.so 

* Thu Mar 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2.13-alt3
- chenged buildreq provides from j2se{,-devel} to java{,-devel}
- removed old profile scripts (they are handled in java-common)

* Tue Mar 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2.13-alt2
- merged jpackage spec
- set priority 1423 (according to jpackage)
- added .desktop files
- added epoch: 0
- spawned alsa supbackage
- moved plugin-specific stuff to mozilla-plugin
- changed j2se layout in filesystem to /usr/lib/jvm;
  old locations are provided as symlinks 
  (to be compatible with both JPackage and old ALT).
- a bundle of 'Provides:' added to be JPackage compatible;
- added new JPackage compatible alternatives;
- removed support for ns4_plugin.
- removed profile symlinks from /etc/profile.d (see #9766)

* Tue Feb 06 2007 Igor Vlasenko <viy@altlinux.ru> 1.4.2_13-alt1
- new version 1.4.2_13

* Thu Feb 23 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.4.2_10-alt2
- Updated to new style library provides.

* Wed Nov 30 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2_10-alt1
- 1.4.2_10
- Provide the old name for mozilla-plugin-%name

* Sat Oct 29 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2_09-alt1
- 1.4.2_09
- Renamed subpackage %name-plugin-mozilla to mozilla-plugin-%name [bug 8114]
- Use macros from browser-plugins-npapi-devel
- Added the bundled desktop files to the JRE package

* Mon Jul 25 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2_08-alt2
- Moved the mozilla plugins alternative symlink to browser-plugins-npapi
  [bug 7461]

* Sat Jun 25 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2_08-alt1
- Updated to 1.4.2_08

* Thu Nov 25 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2_06-alt1
- New upstream release and a security fix
- Moved to the new alternatives scheme
- Stop using generated filelist for native libraries, use %%exclude instead

* Sat Aug 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2_05-alt2
- Require /proc

* Sat Jul 03 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2_05-alt1
- New upstream release

* Wed Jun 16 2004 Stanislav Ievlev <inger@altlinux.org> 1.4.2_04-alt2.1
- NMU: move to new alternatives scheme

* Sat Mar 13 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2_04-alt2
- Added jvm.jprof.txt and jvm.jcov.txt to the JRE file list
- Conditionally-disabled fonts, enabled by default

* Wed Mar 10 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2_04-alt1
- Bugfix upstream release

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
