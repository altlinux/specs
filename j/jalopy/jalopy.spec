Packager: Igor Vlasenko <viy@altlinux.ru>
%def_without eclipse
BuildRequires: ant-trax
BuildRequires: docbook-style-xsl docbook-dtds
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2005, JPackage Project
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

#%define jeditplugdir %{_datadir}/jedit/jars
%define eclipseplugdir %{_datadir}/eclipse/plugins
%define eclipsejalodir %{eclipseplugdir}/de.hunsicker.jalopy.plugin.eclipse

Summary:        Java Source Code Formatter Beautifier Pretty Printer
Name:           jalopy
Version:        1.0
Release:        alt3_0.b11.1jpp5
Epoch:          0
Group:          Development/Java
License:        BSD
URL:            http://jalopy.sourceforge.net/
BuildArch:      noarch
Source0:        http://download.sourceforge.net/jalopy/jalopy-1.0b11.src.tar.gz
Source1:        %{name}.jalopy.script
Source2:        %{name}-settings.sh
Source3:        %{name}-settings.desktop
# Converted from main/src/resources/Preferences16.gif
Source4:        %{name}-settings.png
Patch0:         %{name}-eclipse-nover.patch
Patch1:         %{name}-docfix.patch
Patch2:         %{name}-%{version}b11-noclasspath.patch
Patch3:         %{name}-%{version}b11-eclipse-build_xml.patch
Patch4:         %{name}-jdom-Convention.patch

BuildRequires: ant >= 0:1.6
BuildRequires: ant-trax
BuildRequires: jakarta-oro
BuildRequires: log4j
BuildRequires: jdom
BuildRequires: junit
BuildRequires: gnu-getopt
BuildRequires: saxon
#BuildRequires:  jedit >= 0:4.1, jedit-messageview >= 0:0.1.0
#BuildRequires: eclipse-platform >= 0:3.1
BuildRequires: docbook-xsl-saxon
BuildRequires: jpackage-utils >= 0:1.6
# This one's named the same on many distros and is located in same place...
BuildRequires: docbook-style-xsl
BuildRequires: /usr/bin/perl
Requires: log4j
Requires: jdom
Requires: jakarta-oro

%description
Jalopy is a source code formatter for the Sun Java programming
language. It layouts any valid Java source code according to some
widely configurable rules; to meet a certain coding style without
putting a formatting burden on individual developers.
With Jalopy you will be able to transform any foreign coding style to
your own preferences, without any browbeating or bloodletting.

%package        console
Group:          Development/Java
Summary:        Jalopy console plugin
Requires: %{name} = %{epoch}:%{version}-%{release} gnu.getopt

%description    console
Jalopy console plugin.

%package     	ant
Group:          Development/Java
Summary:        Jalopy plugin for Ant
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: ant >= 0:1.6
Obsoletes:      ant-%{name}
Provides:       ant-%{name}

%description ant
Jalopy plugin for Ant.

#%package     jedit
#Group:          Software Development/Quality Assurance
#Summary:        Jalopy plugin for jEdit
#Requires:       %{name} = %{epoch}:%{version}-%{release}
#Requires:       jedit >= 0:4.1, jedit-messageview >= 0:0.1.0
#Obsoletes:      jedit-%{name}
#Provides:       jedit-%{name}

#%description jedit
#Jalopy plugin for jEdit.

%if_with eclipse
%package        eclipse
Group:          Development/Java
Summary:        Jalopy plugin for Eclipse
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: eclipse-platform >= 0:3.1
Obsoletes:      eclipse-%{name}
Provides:       eclipse-%{name}
%endif #eclipse

%if_with eclipse
%description eclipse
Jalopy plugin for Eclipse.
%endif #eclipse

%package        manual
Group:          Development/Java
Summary:        Manual for %{name}

%description    manual
Documentation for %{name}.

%package        javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}

%description    javadoc
Javadoc for %{name}.


%prep
%setup -q -c
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
# Jalopy has a custom antlr, need to use it.
rm -f `find -type f -name "*.jar" -a ! -name "antlr-*"`
#for j in $(find . -name "*.jar"); do
#	mv $j $j.no
#done
# Fix path to DocBook XSL's.  For some reason, a "-DDIR.DOCBOOK.XSL" does
# not seem to work.
perl -pi -e \
  's|^(DIR\.DOCBOOK\.XSL\s*=).*|$1 %{_datadir}/xml/docbook/xsl-stylesheets|' \
  build/build.properties


%build

# core jars
export CLASSPATH=$(build-classpath ant oro log4j jdom junit gnu.getopt saxon \
docbook-xsl-saxon)

# jedit plugin jars
#export CLASSPATH=$CLASSPATH:$(build-classpath jedit):\
#%{jeditplugdir}/MessageView.jar

# eclipse plugin jars
#CLASSPATH=$CLASSPATH:$(find %{_datadir}/eclipse/plugins -name "org.eclipse.core.runtime_3.3.*.jar")
#CLASSPATH=$CLASSPATH:$(find %{_datadir}/eclipse/plugins -name "org.eclipse.core.resources_3.3.*.jar")
#CLASSPATH=$CLASSPATH:$(find %{_datadir}/eclipse/plugins -name "org.eclipse.text_3.3.*.jar")
#CLASSPATH=$CLASSPATH:$(find %{_datadir}/eclipse/plugins -name "org.eclipse.jface.text_3.3.*.jar")
#CLASSPATH=$CLASSPATH:$(find %{_datadir}/eclipse/plugins -name "org.eclipse.jface_3.3.*.jar")
#CLASSPATH=$CLASSPATH:$(find %{_datadir}/eclipse/plugins -name "org.eclipse.ui.workbench_3.3.*.jar")
#CLASSPATH=$CLASSPATH:$(find %{_datadir}/eclipse/plugins -name "org.eclipse.ui.workbench.texteditor_3.3.*.jar")
#CLASSPATH=$CLASSPATH:$(find %{_datadir}/eclipse/plugins -name "org.eclipse.swt.gtk.*_3.3.*.jar")
#CLASSPATH=$CLASSPATH:$(find %{_datadir}/eclipse/plugins -name "org.eclipse.ui.ide_3.3.*.jar")
#CLASSPATH=$CLASSPATH:$(find %{_datadir}/eclipse/plugins -name "org.eclipse.jdt.core_3.3.*.jar")
#CLASSPATH=$CLASSPATH:$(find %{_datadir}/eclipse/plugins -name "org.eclipse.osgi_3.3.*.jar")
#CLASSPATH=$CLASSPATH:$(build-classpath \
#eclipse/org.eclipse.core.runtime/runtime \
#eclipse/org.eclipse.core.resources/resources \
#eclipse/org.eclipse.text/text \
#eclipse/org.eclipse.jface.text/jfacetext \
#eclipse/org.eclipse.jface/jface \
#eclipse/org.eclipse.ui.workbench/workbench \
#eclipse/org.eclipse.ui.workbench.texteditor/texteditor \
#eclipse/org.eclipse.swt.gtk/swt \
#eclipse/org.eclipse.ui.ide/ide \
#eclipse/org.eclipse.jdt.core/jdtcore \
#eclipse/org.eclipse.osgi/osgi \
#)

cd build

# The Xalan that comes with J2SE 1.4 is buggy, and fails to build the docs.
# Since we're using Saxon anyway, let's force it.
export ANT_OPTS=\
"-Djavax.xml.transform.TransformerFactory=\
com.icl.saxon.TransformerFactoryImpl -Xmx256m"

# Use the locally installed DocBook 4.2 DTD if available.  The build will
# work without this as well, if a net connection is available (but will be
# slow as hell).  With Ant 1.6, could use the external catalog support of
# xmlcatalog.
DOCBOOK_42_DTD=\
`ls -1 %{_datadir}/xml/docbook/dtd/4.2*/docbookx.dtd 2>/dev/null || :`

ant -Dant.build.javac.source=1.3 -Dant.build.javac.target=1.3 \
  -Dbuild.sysclasspath=first \
  -DDIR.DOCBOOK.DTD=$DOCBOOK_42_DTD \
  build-jar-main \
  build-jar-console \
  build-jar-ant \
   \
  build-docu

#  build-jar-jedit \


%install

# jar
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p tmp~/build/jars/jalopy-1*.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
cp -p tmp~/build/jars/jalopy-ant-*.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-ant-%{version}.jar
cp -p tmp~/build/jars/jalopy-console-*.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-console-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# jedit plugin jars
#mkdir -p $RPM_BUILD_ROOT%{jeditplugdir}
#cp -p tmp~/build/jars/jalopy-jedit-*.jar \
#  $RPM_BUILD_ROOT%{jeditplugdir}/JalopyPlugin.jar
#ln -s %{_javadir}/{jalopy,log4j,oro,jdom}.jar \
#  $RPM_BUILD_ROOT%{jeditplugdir}

# eclipse plugin
#mkdir -p $RPM_BUILD_ROOT%{eclipsejalodir}
#cp -p tmp~/build/jars/jalopy-eclipse-*.jar \
##  $RPM_BUILD_ROOT%{eclipsejalodir}/jalopy-eclipse.jar
#cp -p tmp~/eclipse/de.hunsicker.jalopy.plugin.eclipse*/{about.html,plugin.*} \
#  $RPM_BUILD_ROOT%{eclipsejalodir}
#ln -s %{_javadir}/{jalopy,log4j,oro,jdom}.jar $RPM_BUILD_ROOT%{eclipsejalodir}

# scripts
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}-settings

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr tmp~/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# combine docs with manual, fix javadoc link
mv tmp~/docs/site/* tmp~/docs/manual/
ln -s %{_javadocdir}/%{name}-%{version} tmp~/docs/manual/api

# freedesktop.org meny entry
install -Dpm 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/applications/jpackage-%{name}-settings.desktop
install -Dpm 644 %{SOURCE4} \
  $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}-settings.png

mkdir -p $RPM_BUILD_ROOT/%_liconsdir
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
mkdir -p $RPM_BUILD_ROOT/%_niconsdir
ln -s $(relative $RPM_BUILD_ROOT/usr/share/pixmaps/%{name}-settings.png $RPM_BUILD_ROOT/%_niconsdir/) $RPM_BUILD_ROOT/%_niconsdir/
ln -s $(relative $RPM_BUILD_ROOT/usr/share/pixmaps/%{name}-settings.png $RPM_BUILD_ROOT/%_liconsdir/) $RPM_BUILD_ROOT/%_liconsdir/
ln -s $(relative $RPM_BUILD_ROOT/usr/share/pixmaps/%{name}-settings.png $RPM_BUILD_ROOT/%_miconsdir/) $RPM_BUILD_ROOT/%_miconsdir/


%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}


%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/%{name}-settings
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/applications/*%{name}-settings.desktop
%{_datadir}/pixmaps/%{name}-settings.png

%_liconsdir/*
%_miconsdir/*
%_niconsdir/*

%files console
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/%{name}
%{_javadir}/%{name}-console*

%files ant
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-ant*

#%files jedit
#%defattr(0644,root,root,0755)
#%{jeditplugdir}/*

%if_with eclipse
%files eclipse
%defattr(0644,root,root,0755)
%{eclipsejalodir}
%endif #eclipse

%files manual
%defattr(0644,root,root,0755)
%doc --no-dereference tmp~/docs/manual/*

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}


%changelog
* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b11.1jpp5
- fixed build in jpp 5.0

* Tue Mar 11 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.b11.1jpp1.7
- passed repocop tests

* Sun Nov 25 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b11.1jpp1.7
- converted from JPackage by jppimport script

