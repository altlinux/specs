BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support
#def_with readline
%bcond_with readline
%bcond_without servlet
%bcond_without repolib

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


%define repodir %{_javadir}/repository.jboss.com/beanshell/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define Name BeanShell
%define fversion 1.3.0

Name:           bsh
Version:        1.3.0
Release:	alt3_15jpp6
Epoch:          0
Summary:        Lightweight Scripting for Java
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.beanshell.org/
Source0:        %{name}-%{fversion}-src.tar.bz2
Source1:        bsh-1.3.0.pom
Source2:        bsh-bsf-1.3.0.pom
Source3:        bsh-component-info.xml
Patch0:         %{name}-build.patch
Patch1:         %{name}-readline.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: bsf
Requires: jpackage-utils
BuildRequires: ant
BuildRequires: ant-trax
BuildRequires: bsf
BuildRequires: jpackage-utils
%if %with servlet
BuildRequires: servlet_2_5_api
%endif
%if %with readline
BuildRequires: libreadline-java
%endif
Buildarch:      noarch
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
Buildarch:      noarch
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

%if %with repolib
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

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
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: /usr/bin/env

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n BeanShell
%patch0 -p1
%if %with readline
%patch1 -p1
%endif
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}
# remove all CVS files
%{_bindir}/find -type d -name CVS | %{_bindir}/xargs -t %{__rm} -r
%{_bindir}/find -type f -name .cvsignore | %{_bindir}/xargs -t %{__rm}
%{__mkdir_p} lib
%if %with servlet
pushd lib
ln -sf $(build-classpath servlet_2_5_api) servlet.jar
popd
%else
%{__rm} -r src/bsh/servlet
%endif

%build
export CLASSPATH=$(build-classpath bsf)
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/trax`
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  dist
%if %without servlet
%{__rm} -r src/bsh/servlet
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dexclude-servlet='bsh/servlet/*' compile
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dexclude-servlet='bsh/servlet/*' jarall
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dexclude-servlet='bsh/servlet/*' javadoc
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dexclude-servlet='bsh/servlet/*' bshdoc
%else
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  dist
%endif
(cd docs/faq && %{ant})
(cd docs/manual && %{ant})

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
install -p -m 644 dist/%{name}-bsf-%{version}.jar %{buildroot}%{_javadir}/%{name}-bsf-%{version}.jar
install -p -m 644 dist/%{name}-classpath-%{version}.jar %{buildroot}%{_javadir}/%{name}-classpath-%{version}.jar
install -p -m 644 dist/%{name}-commands-%{version}.jar %{buildroot}%{_javadir}/%{name}-commands-%{version}.jar
install -p -m 644 dist/%{name}-core-%{version}.jar %{buildroot}%{_javadir}/%{name}-core-%{version}.jar
install -p -m 644 dist/%{name}-reflect-%{version}.jar %{buildroot}%{_javadir}/%{name}-reflect-%{version}.jar
install -p -m 644 dist/%{name}-util-%{version}.jar %{buildroot}%{_javadir}/%{name}-util-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}.pom
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-bsf.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
%add_to_maven_depmap %{name} %{name}-bsf %{version} JPP %{name}-bsf

# manual
# FIXME: (dwalluck): breaks -bi --short-circuit
find docs -name ".cvswrappers" -exec rm -f {} \;
find docs -name "*.xml" -exec rm -f {} \;
find docs -name "*.xsl" -exec rm -f {} \;
find docs -name "*.log" -exec rm -f {} \;
(cd docs/manual && mv html/* . || :)
(cd docs/manual && rm -rf html)
(cd docs/manual && rm -rf xsl)

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

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

install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -pr tests %{buildroot}%{_datadir}/%{name}

install -d -m 755 %{buildroot}%{_datadir}/%{name}/webapps
install -p -m 644 dist/bshservlet.war %{buildroot}%{_datadir}/%{name}/webapps
install -p -m 644 dist/bshservlet-wbsh.war %{buildroot}%{_datadir}/%{name}/webapps

# scripts
install -d %{buildroot}%{_bindir}

cat > %{buildroot}%{_bindir}/%{name} << EOF
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

%if %with readline
if [ -f %{libdir}/libJavaReadline.so ]; then
  BASE_FLAGS="$BASE_FLAGS -Djava.library.path=%{libdir}"
  BASE_FLAGS="\$BASE_FLAGS -Dbsh.console.readlinelib=GnuReadline"
  BASE_JARS="\$BASE_JARS libreadline-java.jar"
fi
%endif

# Set parameters
set_jvm
set_classpath \$BASE_JARS
set_flags \$BASE_FLAGS
set_options \$BASE_OPTIONS

# Let's start
run "\$@"
EOF

cat > %{buildroot}%{_bindir}/%{name}doc << EOF
#!/usr/bin/env %{_bindir}/%{name}
EOF
cat scripts/bshdoc.bsh >> %{buildroot}%{_bindir}/%{name}doc

%if %{gcj_support}
%{_bindir}/aot-compile-rpm \
   --exclude %{_datadir}/%{name}/webapps/bshservlet.war \
   --exclude %{_datadir}/%{name}/webapps/bshservlet-wbsh.war
%endif

%if %with repolib
install -d -m 755 %{buildroot}%{repodir}
install -d -m 755 %{buildroot}%{repodirlib}
install -p -m 644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}-brew/g' %{buildroot}%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
install -d -m 755 %{buildroot}%{repodirsrc}
install -p -m 644 %{PATCH0} %{buildroot}%{repodirsrc}
%if %with readline
install -p -m 644 %{PATCH1} %{buildroot}%{repodirsrc}
%endif
install -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
install -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
install -p -m 644 %{SOURCE2} %{buildroot}%{repodirsrc}
cp -p %{buildroot}%{_javadir}/%{name}.jar %{buildroot}%{repodirlib}/bsh.jar
cp -p %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}.pom %{buildroot}%{repodirlib}/bsh.pom
cp -p %{buildroot}%{_javadir}/%{name}-bsf.jar %{buildroot}%{repodirlib}/bsh-bsf.jar
cp -p %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-bsf.pom %{buildroot}%{repodirlib}/bsh-bsf.pom
%endif

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/%{name}.conf

%files
%doc src/Changes.html src/License.txt src/README.txt
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}doc
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-bsf-%{version}.jar
%{_javadir}/%{name}-bsf.jar
%{_javadir}/%{name}-classpath-%{version}.jar
%{_javadir}/%{name}-classpath.jar
%{_javadir}/%{name}-commands-%{version}.jar
%{_javadir}/%{name}-commands.jar
%{_javadir}/%{name}-core-%{version}.jar
%{_javadir}/%{name}-core.jar
%{_javadir}/%{name}-reflect-%{version}.jar
%{_javadir}/%{name}-reflect.jar
%{_javadir}/%{name}-util-%{version}.jar
%{_javadir}/%{name}-util.jar
%{_datadir}/maven2/poms/JPP.%{name}-bsf.pom
%{_datadir}/maven2/poms/JPP.%{name}.pom
%{_mavendepmapfragdir}/%{name}
%dir %{_datadir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif
%config(noreplace,missingok) /etc/%{name}.conf

%files manual
%doc docs/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%doc tests/README.txt tests/Interactive/README
%{_datadir}/%{name}/*

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
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

