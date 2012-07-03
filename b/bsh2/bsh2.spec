# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2011, JPackage Project
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

%define orig_name bsh
%define Name      BeanShell2
%define fversion  2.1b5


Name:           bsh2
Version:        2.1
Release:        alt1_0.b5.1jpp6
Epoch:          0
Summary:        Lightweight Scripting for Java
License:        GPL
Url:            http://code.google.com/p/beanshell2/
Source0:        http://beanshell2.googlecode.com/files/bsh-2.1b5-src.zip
Source1:        beanshell-2.1b5.pom
Source2:        bsh-classpath-2.1b5.pom
Source3:        bsh-commands-2.1b5.pom
Source4:        bsh-core-2.1b5.pom
Source5:        bsh-reflect-2.1b5.pom
Source6:        bsh-util-2.1b5.pom
Source7:        bsh-bsf-2.1b5.pom
Source8:        bsh-classgen-2.1b5.pom
Patch0:         bsh2-faq-xsl.patch
Patch1:         bsh2-manual-xsl.patch

Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Requires:  jpackage-utils >= 0:1.7.5
Requires:  bsf
Requires:  servlet_2_4_api

BuildRequires:  ant
BuildRequires:  javacc3
BuildRequires:  junit4
BuildRequires:  bsf
BuildRequires:  servlet_2_4_api
BuildRequires:  bsf-javadoc
BuildRequires:  java-javadoc
BuildRequires:  jpackage-utils >= 0:1.7.5
Group:          Development/Java
%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%if ! %{gcj_support}
BuildArch:      noarch
%endif
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

%package bsf
Summary:        BSF support for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       bsf

%description bsf
BSF support for %{name}.

%package classgen
Summary:        ASM support for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description classgen
ASM support for %{name}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demos for %{name}
Group:          Development/Java
AutoReqProv:    no
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n %{Name}-%{fversion}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
mv tests/test-scripts/Data/addedCommand.jar.no tests/test-scripts/Data/addedCommand.jar
mv tests/test-scripts/Data/addclass.jar.no tests/test-scripts/Data/addclass.jar
%patch0 -b .sav0
%patch1 -b .sav1

%build
pushd lib
ln -sf $(build-classpath bsf)
ln -sf $(build-classpath javacc3) javacc.jar
ln -sf $(build-classpath junit4) junit-4.8.2.jar
ln -sf $(build-classpath servlet_2_4_api) servlet.jar
popd

# set VERSION
%__perl -p -i -e 's|VERSION =.*;|VERSION = "%{version}-%{release}";|' src/bsh/Interpreter.java

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=first \
    -Dbsf.javadoc=%{_javadocdir}/bsf \
    -Djava.javadoc=%{_javadocdir}/java \
    dist test
(cd docs/faq && %ant)
(cd docs/manual && %ant)

%install
%__rm -rf %{buildroot}

# jars
%__mkdir_p %{buildroot}%{_javadir}/%{name}
%__rm -f dist/%{orig_name}-%{fversion}-src.jar
for jar in dist/*.jar; do
  %__install -m 644 ${jar} %{buildroot}%{_javadir}/%{name}/`basename ${jar} -%{fversion}.jar`-%{version}.jar
done
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}*; do %__ln_s ${jar} ${jar/-%{version}/}; done)

%add_to_maven_depmap org.beanshell beanshell %{fversion} JPP/%{name} bsh
%add_to_maven_depmap org.beanshell bsh %{fversion} JPP/%{name} bsh
%add_to_maven_depmap org.beanshell bsh-classpath %{fversion} JPP/%{name} bsh-classpath
%add_to_maven_depmap org.beanshell bsh-commands %{fversion} JPP/%{name} bsh-commands
%add_to_maven_depmap org.beanshell bsh-core %{fversion} JPP/%{name} bsh-core
%add_to_maven_depmap org.beanshell bsh-reflect %{fversion} JPP/%{name} bsh-reflect
%add_to_maven_depmap org.beanshell bsh-util %{fversion} JPP/%{name} bsh-util
%add_to_maven_depmap org.beanshell bsh-bsf %{fversion} JPP/%{name} bsh-bsf
%add_to_maven_depmap org.beanshell bsh-classgen %{fversion} JPP/%{name} bsh-classgen

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-bsh.pom
install -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-bsh-classpath.pom
install -m 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-bsh-commands.pom
install -m 644 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-bsh-core.pom
install -m 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-bsh-reflect.pom
install -m 644 %{SOURCE6} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-bsh-util.pom
install -m 644 %{SOURCE7} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-bsh-bsf.pom
install -m 644 %{SOURCE8} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-bsh-classgen.pom

# manual
find docs -name ".cvswrappers" -exec %__rm -f {} \;
find docs -name "*.xml" -exec %__rm -f {} \;
find docs -name "*.xsl" -exec %__rm -f {} \;
find docs -name "*.log" -exec %__rm -f {} \;
(cd docs/manual && %__mv -f html/* .)
(cd docs/manual && %__rm -rf html)
(cd docs/manual && %__rm -rf xsl)

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -a javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && %__ln_s %{name}-%{version} %{name})

# demo
for i in `find tests -name "*.bsh"`; do
  %__perl -p -i -e 's,^\n?#!(/(usr/)?bin/java bsh\.Interpreter|/bin/sh),#!%{_bindir}/%{name},' $i
done

%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -a tests %{buildroot}%{_datadir}/%{name}

find %{buildroot}%{_datadir}/%{name} -type d \
  | sed 's|'%{buildroot}'|%dir |' >  %{name}-demo-%{version}.files
find %{buildroot}%{_datadir}/%{name} -type f -name "*.bsh" \
  | sed 's|'%{buildroot}'|%attr(0755,root,root) |'      >> %{name}-demo-%{version}.files
find %{buildroot}%{_datadir}/%{name} -type f ! -name "*.bsh" \
  | sed 's|'%{buildroot}'|%attr(0644,root,root) |'      >> %{name}-demo-%{version}.files

# bshservlet
%__mkdir_p %{buildroot}%{_datadir}/%{name}/bshservlet
(cd %{buildroot}%{_datadir}/%{name}/bshservlet
jar xf $RPM_BUILD_DIR/%{Name}-%{fversion}/dist/bshservlet.war
)

# bshservlet
%__mkdir_p %{buildroot}%{_datadir}/%{name}/bshservlet-wbsh
(cd %{buildroot}%{_datadir}/%{name}/bshservlet-wbsh
jar xf $RPM_BUILD_DIR/%{Name}-%{fversion}/dist/bshservlet-wbsh.war
)

# scripts
%__mkdir_p %{buildroot}%{_bindir}

%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
#
# %{name} script
# JPackage Project (http://jpackage.sourceforge.net)

# Source functions library
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
MAIN_CLASS=bsh.Interpreter
if [ -n "\$BSH_DEBUG" ]; then
  BASE_FLAGS=-Ddebug=true
fi

BASE_JARS="%{name}.jar"

#if [ -f /usr/lib/libJavaReadline.so ]; then
#  BASE_FLAGS="$BASE_FLAGS -Djava.library.path=/usr/lib"
#  BASE_FLAGS="\$BASE_FLAGS -Dbsh.console.readlinelib=GnuReadline"
#  BASE_JARS="\$BASE_JARS libreadline-java.jar"
#fi

# Set parameters
set_jvm
set_classpath \$BASE_JARS
set_flags \$BASE_FLAGS
set_options \$BASE_OPTIONS

# Let's start
run "\$@"
EOF

%__cat > %{buildroot}%{_bindir}/%{name}doc << EOF
#!/usr/bin/env %{_bindir}/%{name}
EOF
%__cat scripts/bshdoc.bsh >> %{buildroot}%{_bindir}/%{name}doc

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm \
--exclude %{_datadir}/%{name}/tests/test-scripts/Data/addedCommand.jar \
--exclude %{_datadir}/%{name}/tests/test-scripts/Data/addclass.jar

%endif

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/%{name}.conf

%files
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}doc
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{orig_name}-%{version}.jar
%{_javadir}/%{name}/%{orig_name}.jar
%{_javadir}/%{name}/%{orig_name}-classpath*.jar
%{_javadir}/%{name}/%{orig_name}-commands*.jar
%{_javadir}/%{name}/%{orig_name}-core*.jar
%{_javadir}/%{name}/%{orig_name}-reflect*.jar
%{_javadir}/%{name}/%{orig_name}-util*.jar
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/bshservlet
%{_datadir}/%{name}/bshservlet-wbsh
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/bsh-*%{version}.jar.*
%endif
%config(noreplace,missingok) /etc/%{name}.conf

%files bsf
%{_javadir}/%{name}/%{orig_name}-bsf*.jar

%files classgen
%{_javadir}/%{name}/%{orig_name}-classgen*.jar

%files manual
%doc docs/*

%files javadoc
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/*
%dir %{_javadocdir}/%{name}

%files demo -f %{name}-demo-%{version}.files

%changelog
* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_0.b5.1jpp6
- converted from JPackage by jppimport script

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt3_0.b5.1jpp5
- selected java5 compiler explicitly

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_0.b5.1jpp5
- new beta 5

* Thu Feb 28 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_0.b4.2jpp1.7
- fixed autoreq on /etc/bsh2.conf

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_0.b4.2jpp1.7
- updated to new jpackage release

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_0.b4.1jpp1.7
- updated to new jpackage release

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_0.b1.9jpp1.7
- converted from JPackage by jppimport script

* Tue Feb 21 2006 Eugene V. Horohorin <genix@altlinux.ru> 2.0-alt0.1b4
- new version compatible with j2se-1.5

* Tue Apr 26 2005 Eugene V. Horohorin <genix@altlinux.ru> 2.0-alt0.1b2
- First build for ALTLinux
