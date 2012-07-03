BuildRequires: /proc
BuildRequires: jpackage-compat
# one of the sources is a zip file
BuildRequires: unzip
# Copyright (c) 2000-2009, JPackage Project
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

%define gcj_support 0


Name:           clirr
Summary:        Binary and Source Compatibility Check
Url:            http://clirr.sourceforge.net/
Version:        0.6
Release:        alt5_6jpp6
Epoch:          0
License:        LGPL
Group:          Development/Java
Source0:        http://prdownloads.sourceforge.net/clirr/clirr-0.6-src.zip

Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        clirr-0.6-jpp-depmap.xml
Source5:        clirr-core-0.6.pom
Source6:        clirr-maven-0.6.pom

Patch0:         clirr-0.6-maven-plugin-project_xml.patch
# patch to bcel-5.2
Patch1:         clirr-0.6-BcelJavaType.patch
Patch2:         clirr-0.6-maven-maven_xml.patch
#Patch3:         clirr-0.6-core-project_xml.patch

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant >= 0:1.7.1
BuildRequires: junit
BuildRequires: saxon
BuildRequires: saxon-scripts
BuildRequires: maven1 >= 0:1.1
BuildRequires: maven1-plugins-base
BuildRequires: maven1-plugin-changes
BuildRequires: maven1-plugin-developer-activity
BuildRequires: maven1-plugin-file-activity
BuildRequires: maven1-plugin-jdepend
BuildRequires: maven1-plugin-jxr
BuildRequires: maven1-plugin-license
BuildRequires: maven1-plugin-linkcheck
BuildRequires: maven1-plugin-multiproject
BuildRequires: maven1-plugin-tasklist
BuildRequires: maven1-plugin-test
BuildRequires: maven1-plugin-xdoc
BuildRequires: maven-model
BuildRequires: sf-javaapp-maven-plugin
BuildRequires: bcel5.3
BuildRequires: apache-commons-cli
BuildRequires: jakarta-commons-jelly
BuildRequires: apache-commons-lang
#
Requires: bcel5.3
Requires: apache-commons-cli
Requires: jakarta-commons-jelly
Requires: apache-commons-lang
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0
Source44: import.info

%description
Clirr is a tool that checks Java libraries for binary and 
source compatibility with older releases. Basically you 
give it two sets of jar files and Clirr dumps out a list 
of changes in the public api. The Clirr Ant task can be 
configured to break the build if it detects incompatible 
api changes. In a continuous integration process Clirr 
can automatically prevent accidental introduction of 
binary or source compatibility problems.

%package maven-plugin
Summary:        Maven plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}
Requires: maven1 >= 0:1.1
Requires: maven-model
Requires: sf-javaapp-maven-plugin

%description maven-plugin
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if 0
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif

%prep
%setup -q -n %{name}-%{version}
chmod -R go=u-w *
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
#%patch3 -b .sav3

if [ ! -f %{SOURCE4} ]; then
export DEPCAT=$(pwd)/clirr-0.6-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > clirr-0.6-depmap.new.xml
fi

%build
export LANG=C
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

MAVEN_HOME_LOCAL=$(pwd)/.maven
maven -Dmaven.compile.target=1.4 -Dmaven.javadoc.source=1.4  -Dmaven.repo.remote=file:/usr/share/maven1/repository \
      -Dmaven.home.local=${MAVEN_HOME_LOCAL} \
      -Dmaven.javadoc.source=1.4 \
      -Dgoal=jar:jar,dist,javadoc:generate \
      multiproject:goal

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 core/target/%{name}-core-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-core-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# plugin
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven1/plugins
install -m 644 \
    maven/target/%{name}-maven-%{version}.jar \
    $RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-clirr-plugin-%{version}.jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/maven1-plugins
pushd $RPM_BUILD_ROOT%{_javadir}/maven1-plugins
ln -sf \
    %{_datadir}/maven1/plugins/maven-clirr-plugin-%{version}.jar \
    maven-clirr-plugin.jar
popd

%add_to_maven_depmap %{name} %{name}-core %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE5} \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-clirr-core.pom
install -m 644 %{SOURCE6} \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-clirr-maven.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core
cp -pr core/target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core
rm -rf core/target/docs/apidocs
#install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven
#cp -pr maven/target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven
#rm -rf maven/target/docs/apidocs
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
%if 0
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/core
cp -pr core/target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/core
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/maven
cp -pr maven/target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/maven
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

mkdir -p $RPM_BUILD_ROOT%_bindir/
cat > $RPM_BUILD_ROOT%_bindir/%name <<'EOF'
#!/bin/sh
# 
# Clirr startup script
#
# JPackage Project <http://www.jpackage.org/>

# Source functions library
if [ -f /usr/share/java-utils/java-functions ] ; then 
  . /usr/share/java-utils/java-functions
else
  echo "Can't find functions library, aborting"
  exit 1
fi

# Configuration
MAIN_CLASS=net.sf.clirr.cli.Clirr
BASE_JARS="bcel commons-cli commons-lang clirr-core"

# Set parameters
set_jvm
set_classpath $BASE_JARS
set_flags $BASE_FLAGS
set_options $BASE_OPTIONS

# Let's start
run "$@"
EOF

chmod 755 $RPM_BUILD_ROOT%_bindir/%name

%files
%doc LICENSE.txt
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-core-%{version}.jar.*
%endif
%exclude %_javadir/maven1-plugins*
%_bindir/%name

%files maven-plugin
%doc LICENSE.txt
%{_datadir}/maven1/plugins/maven-clirr-plugin*.jar
%{_javadir}/maven1-plugins/maven-clirr-plugin.jar
%{_datadir}/maven2/poms/JPP-clirr-maven.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/maven-%{name}-plugin-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%if 0
%files manual
%{_docdir}/%{name}-%{version}
%endif

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt5_6jpp6
- fixed build with moved maven1

* Mon Aug 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt4_6jpp6
- maven1 translation

* Sat Oct 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt3_6jpp6
- new jpp release

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt3_3jpp5
- fixed build with java 5

* Wed Feb 13 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt2_3jpp1.7
- misc fixes; added launch script

* Sun Nov 25 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt2_2jpp1.7
-excluded maven plugin from clirr

* Wed Nov 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt1_2jpp1.7
- converted from JPackage by jppimport script

