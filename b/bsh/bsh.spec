Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install ImageMagick-tools
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
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
Release:        alt6_34jpp8
Epoch:          0
Summary:        Lightweight Scripting for Java
License:        (SPL or LGPLv2+) and Public Domain
Source0:        %{name}-%{version}-src.tar.bz2
#cvs -d:pserver:anonymous@beanshell.cvs.sourceforge.net:/cvsroot/beanshell login
#cvs -z3 -d:pserver:anonymous@beanshell.cvs.sourceforge.net:/cvsroot/beanshell export -r rel_1_3_0_final BeanShell
#tar cjf bsh-1.3.0-src.tar.bz2 BeanShell
Source1:        bsh-1.3.0.pom
Source2:        bsh-bsf-1.3.0.pom
Source3:        %{name}-desktop.desktop

Patch0:         %{name}-build.patch
Patch1:         %{name}-xsl-fixes.patch
BuildRequires:  java-devel
BuildRequires:  ant bsf ImageMagick desktop-file-utils
BuildRequires:  servlet
Requires:       bsf
URL:            http://www.beanshell.org/
BuildArch:      noarch
Source44: import.info

%description
BeanShell is a small, free, embeddable, Java source interpreter with
object scripting language features, written in Java.  BeanShell
executes standard Java statements and expressions, in addition to
obvious scripting commands and syntax.  BeanShell supports scripted
objects as simple method closures like those in Perl and
JavaScript(tm).  You can use BeanShell interactively for Java
experimentation and debugging or as a simple scripting engine for your
applications.  In short: BeanShell is a dynamically interpreted Java,
plus some useful stuff.  Another way to describe it is to say that in
many ways BeanShell is to Java as Tcl/Tk is to C: BeanShell is
embeddable - You can call BeanShell from your Java applications to
execute Java code dynamically at run-time or to provide scripting
extensibility for your applications.  Alternatively, you can call your
Java applications and objects from BeanShell; working with Java
objects and APIs dynamically.  Since BeanShell is written in Java and
runs in the same space as your application, you can freely pass
references to "real live" objects into scripts and return them as
results.

%package manual
Group: Development/Java
Summary:        Manual for %{name}
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%package demo
Group: Development/Java
Summary:        Demo for %{name}
AutoReqProv:    no
Requires:       %{name} = %{epoch}:%{version}

%description demo
Demonstrations and samples for %{name}.

%package utils
Group: Development/Java
Summary:        %{name} utilities
Requires:       %{name} = %{epoch}:%{version}
Requires:       jline1
Provides:       %{name}-desktop = %{epoch}:%{version}-%{release}

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
ant="ant -Dant.build.javac.source=1.5"
$ant test dist
(cd docs/faq && $ant)
(cd docs/manual && $ant)

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
for mod in '' bsf classpath commands core reflect util; do
    install -p -m 644 dist/%{name}${mod:+-${mod}}-%{version}.jar \
             $RPM_BUILD_ROOT%{_javadir}/%{name}${mod:+-${mod}}.jar
done

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-bsf.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar -a org.beanshell:%{name}
%add_maven_depmap JPP-%{name}-bsf.pom %{name}-bsf.jar

# manual
find docs -name ".cvswrappers" -exec rm -f {} \;
find docs -name "*.xml" -exec rm -f {} \;
find docs -name "*.xsl" -exec rm -f {} \;
find docs -name "*.log" -exec rm -f {} \;
(cd docs/manual && mv html/* .)
(cd docs/manual && rm -rf html)
(cd docs/manual && rm -rf xsl)
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
# menu entry
desktop-file-install --mode=644 \
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

%jpackage_script bsh.Interpreter "\${BSH_DEBUG:+-Ddebug=true}" jline.ConsoleRunner %{name}:jline1/jline-1 %{name} true
%jpackage_script bsh.Console "\${BSH_DEBUG:+-Ddebug=true}" "" %{name} %{name}-console true

cat > $RPM_BUILD_ROOT%{_bindir}/%{name}doc << EOF
#!/usr/bin/env %{_bindir}/%{name}
EOF
cat scripts/bshdoc.bsh >> $RPM_BUILD_ROOT%{_bindir}/%{name}doc

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files -f .mfiles
%doc src/License.txt
%doc src/Changes.html src/README.txt
%{_javadir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/webapps
%config(noreplace,missingok) /etc/java/%{name}.conf

%files manual
%doc src/License.txt
%doc docs/*

%files javadoc
%doc src/License.txt
%{_javadocdir}/%{name}

%files demo
%doc tests/README.txt tests/Interactive/README
%{_datadir}/%{name}/*

%files utils
%attr(0755,root,root) %{_bindir}/%{name}*
%{_datadir}/applications/%{name}-desktop.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png

%changelog
* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt6_34jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt6_33jpp8
- new version

* Mon Jan 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt4_24jpp7
- new release

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

