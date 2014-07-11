# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
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

Name:           bsh
Version:        1.3.0
Release:        alt4_20jpp7
Epoch:          0
Summary:        Lightweight Scripting for Java
License:        SPL or LGPLv2+
Source0:        %{name}-%{version}-src.tar.bz2
#cvs -d:pserver:anonymous@beanshell.cvs.sourceforge.net:/cvsroot/beanshell login
#cvs -z3 -d:pserver:anonymous@beanshell.cvs.sourceforge.net:/cvsroot/beanshell export -r rel_1_3_0_final BeanShell
#tar cjf bsh-1.3.0-src.tar.bz2 BeanShell
Source1:        bsh-1.3.0.pom
Source2:        bsh-bsf-1.3.0.pom
Source3:        %{name}-desktop.desktop

Patch0:         %{name}-build.patch
Patch1:         %{name}-xsl-fixes.patch
BuildRequires:  ant bsf ant-trax ImageMagick desktop-file-utils
BuildRequires:  servlet
Requires:       bsf
Requires:       jpackage-utils >= 0:1.7.5-3.9
URL:            http://www.beanshell.org/
Group:          Development/Java
BuildArch:      noarch
Source44: import.info

%description
BeanShell is a small, free, embeddable, Java source interpreter with
object scripting language features, written in Java. BeanShell executes
standard Java statements and expressions, in addition to obvious
scripting commands and syntax. BeanShell supports scripted objects as
simple method closures like those in Perl and JavaScript(tm).
You can use BeanShell interactively for Java experimentation and
debugging or as a simple scripting engine for your applications. In
short: BeanShell is a dynamically interpreted Java, plus some useful
stuff. Another way to describe it is to say that in many ways BeanShell
is to Java as Tcl/Tk is to C: BeanShell is embeddable - You can call
BeanShell from your Java applications to execute Java code dynamically
at run-time or to provide scripting extensibility for your applications.
Alternatively, you can call your Java applications and objects from
BeanShell; working with Java objects and APIs dynamically. Since
BeanShell is written in Java and runs in the same space as your
application, you can freely pass references to "real live" objects into
scripts and return them as results.

%package manual
Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demo for %{name}
Group:          Development/Java
AutoReqProv:    no
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       /usr/bin/env

%description demo
Demonstrations and samples for %{name}.

%package utils
Summary:        %{name} utilities
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jline
Provides:       %{name}-desktop = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-desktop < 0:1.3.0-17
# So that yum will pull this in on base package upgrades from < 0:1.3.0-17
# (bsh and bshdoc scripts moved here in -17):
Obsoletes:      %{name} < 0:1.3.0-17

%description utils
%{name} utilities.

%prep
%setup -q -n BeanShell
%patch0 -p1
%patch1 -p1
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
# remove all CVS files
for dir in `find . -type d -name CVS`; do rm -rf $dir; done
for file in `find . -type f -name .cvsignore`; do rm -rf $file; done
# fix rpmlint spurious-executable-perm warnings
for i in backbutton forwardbutton homebutton remoteconsole upbutton; do
    chmod 644 docs/images/$i.gif
done

%build
mkdir -p lib
pushd lib
ln -sf $(build-classpath bsf)
ln -sf $(build-classpath servlet)
popd
ant="ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5"
$ant dist
%ifnarch ppc64 s390x
(cd docs/faq && $ant)
(cd docs/manual && $ant)
%endif

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{name}-%{version}.jar \
             $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 dist/%{name}-bsf-%{version}.jar \
             $RPM_BUILD_ROOT%{_javadir}/%{name}-bsf-%{version}.jar
install -m 644 dist/%{name}-classpath-%{version}.jar \
             $RPM_BUILD_ROOT%{_javadir}/%{name}-classpath-%{version}.jar
install -m 644 dist/%{name}-commands-%{version}.jar \
             $RPM_BUILD_ROOT%{_javadir}/%{name}-commands-%{version}.jar
install -m 644 dist/%{name}-core-%{version}.jar \
             $RPM_BUILD_ROOT%{_javadir}/%{name}-core-%{version}.jar
install -m 644 dist/%{name}-reflect-%{version}.jar \
             $RPM_BUILD_ROOT%{_javadir}/%{name}-reflect-%{version}.jar
install -m 644 dist/%{name}-util-%{version}.jar \
             $RPM_BUILD_ROOT%{_javadir}/%{name}-util-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
%add_to_maven_depmap %{name} %{name}-bsf %{version} JPP %{name}-bsf

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-bsf.pom

# manual
find docs -name ".cvswrappers" -exec rm -f {} \;
find docs -name "*.xml" -exec rm -f {} \;
find docs -name "*.xsl" -exec rm -f {} \;
find docs -name "*.log" -exec rm -f {} \;
%ifnarch ppc64 s390x
(cd docs/manual && mv html/* .)
(cd docs/manual && rm -rf html)
(cd docs/manual && rm -rf xsl)
%endif
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
# menu entry
desktop-file-install --vendor=fedora --mode=644 \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE3}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
convert src/bsh/util/lib/icon.gif \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/bsh.png

# demo
for i in `find tests -name \*.bsh`; do
  perl -p -i -e 's,^\n?#!(/(usr/)?bin/java bsh\.Interpreter|/bin/sh),#!/usr/bin/env %{_bindir}/%{name},' $i
  if head -1 $i | grep '#!/usr/bin/env %{_bindir}/%{name}' >/dev/null; then
    chmod 755 $i
  fi
done
chmod 755 tests/Template
cat > one << EOF
#!/bin/sh

EOF
cat tests/Interactive/reload/one >> one
cat one > tests/Interactive/reload/one
rm one
cat > two << EOF
#!/bin/sh

EOF
cat tests/Interactive/reload/two >> two
cat two > tests/Interactive/reload/two
rm two
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr tests $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/webapps
install -m 644 dist/bshservlet.war $RPM_BUILD_ROOT%{_datadir}/%{name}/webapps
install -m 644 dist/bshservlet-wbsh.war $RPM_BUILD_ROOT%{_datadir}/%{name}/webapps

# scripts
install -d $RPM_BUILD_ROOT%{_bindir}

function bsh_script() {
    local jars=%{name}.jar runclass=
    if [ $2 = jline.ConsoleRunner ] ; then
        jars="$jars jline.jar"
        runclass=bsh.Interpreter
    fi
cat > $RPM_BUILD_ROOT%{_bindir}/$1 << EOF
#!/bin/sh
#
# $1 script
# JPackage Project (http://jpackage.sourceforge.net)

# Source functions library
_prefer_jre=true
. %{_datadir}/java-utils/java-functions

# Source system prefs
if [ -f %{_sysconfdir}/%{name}.conf ] ; then
  . %{_sysconfdir}/%{name}.conf
fi

# Source user prefs
if [ -f \$HOME/.%{name}rc ] ; then
  . \$HOME/.%{name}rc
fi

# Configuration
MAIN_CLASS=$2
if [ -n "\$BSH_DEBUG" ]; then
  BASE_FLAGS=-Ddebug=true
fi

BASE_JARS="$jars"

# Set parameters
set_jvm
set_classpath \$BASE_JARS
set_flags \$BASE_FLAGS
set_options \$BASE_OPTIONS

# Let's start
run $runclass "\$@"
EOF
}

bsh_script bsh jline.ConsoleRunner
bsh_script bsh-desktop bsh.Console

cat > $RPM_BUILD_ROOT%{_bindir}/%{name}doc << EOF
#!/usr/bin/env %{_bindir}/%{name}
EOF
cat scripts/bshdoc.bsh >> $RPM_BUILD_ROOT%{_bindir}/%{name}doc

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/%{name}.conf

%files
%doc src/Changes.html src/License.txt src/README.txt
%{_javadir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/webapps
%{_mavenpomdir}/*
%{_mavendepmapfragdir}
%config(noreplace,missingok) /etc/%{name}.conf

%ifnarch ppc64 s390x
%files manual
%doc docs/*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%doc tests/README.txt tests/Interactive/README
%{_datadir}/%{name}/*

%files utils
%attr(0755,root,root) %{_bindir}/%{name}*
%{_datadir}/applications/*%{name}-desktop.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png

%changelog
* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt4_20jpp7
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt3_20jpp7
- fc update

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt3_15jpp6
- new jpp release

* Tue Mar 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt3_13jpp5
- fixed bug in component-info.xml in repolib

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt2_13jpp5
- new jpackage release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt2_11jpp5
- converted from JPackage by jppimport script

* Tue Oct 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_11jpp1.7
- updated to new jpackage release

* Tue May 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_10jpp1.7
- converted from JPackage by jppimport script

