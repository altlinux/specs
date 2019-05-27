Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
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

%global reltag b6
%bcond_without  desktop

Name:           bsh
Version:        2.0
Release:        alt1_14.b6jpp8
Epoch:          0
Summary:        Lightweight Scripting for Java
URL:            http://www.beanshell.org/
# bundled asm is BSD
# bsf/src/bsh/util/BeanShellBSFEngine.java is public-domain
License:        ASL 2.0 and BSD and Public Domain
BuildArch:      noarch
# ./generate-tarball.sh
Source0:        %{name}-%{version}-%{reltag}.tar.gz
Source1:        %{name}-desktop.desktop
# Remove bundled jars which cannot be easily verified for licensing
# Remove code marked as SUN PROPRIETARY/CONFIDENTAIL
Source2:        generate-tarball.sh

BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  bsf
BuildRequires:  junit
BuildRequires:  javacc
BuildRequires:  glassfish-servlet-api
%if %{with desktop}
BuildRequires:  ImageMagick-tools
BuildRequires:  desktop-file-utils
%endif

Requires:       bsf
Requires:       jline
# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
Requires:       javapackages-tools


Provides:       %{name}-utils = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-utils < 0:2.0
Obsoletes:      %{name}-demo < 0:2.0

# bsh uses small subset of modified (shaded) classes from ancient version of
# objecweb-asm under asm directory
Provides:       bundled(objectweb-asm) = 1.3.6
Source44: import.info

%description
BeanShell is a small, free, embeddable, Java source interpreter with
object scripting language features, written in Java. BeanShell
executes standard Java statements and expressions, in addition to
obvious scripting commands and syntax. BeanShell supports scripted
objects as simple method closures like those in Perl and
JavaScript(tm). You can use BeanShell interactively for Java
experimentation and debugging or as a simple scripting engine for your
applications. In short: BeanShell is a dynamically interpreted Java,
plus some useful stuff. Another way to describe it is to say that in
many ways BeanShell is to Java as Tcl/Tk is to C: BeanShell is
embeddable - You can call BeanShell from your Java applications to
execute Java code dynamically at run-time or to provide scripting
extensibility for your applications. Alternatively, you can call your
Java applications and objects from BeanShell; working with Java
objects and APIs dynamically. Since BeanShell is written in Java and
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

%prep
%setup -q -n beanshell-%{version}%{reltag}

sed -i 's,org.apache.xalan.xslt.extensions.Redirect,http://xml.apache.org/xalan/redirect,' docs/manual/xsl/*.xsl

%mvn_alias :bsh bsh:bsh bsh:bsh-bsf org.beanshell:bsh

%mvn_file : %{name}

%build
mkdir lib
build-jar-repository lib bsf javacc junit glassfish-servlet-api

ant test dist

%install
%mvn_artifact pom.xml dist/%{name}-%{version}%{reltag}.jar

%mvn_install -J javadoc

%if %{with desktop}
# menu entry
desktop-file-install --mode=644 \
  --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
convert src/bsh/util/lib/icon.gif \
  %{buildroot}%{_datadir}/pixmaps/bsh.png
%endif

install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_datadir}/%{name}/webapps
install -m 644 dist/bshservlet.war %{buildroot}%{_datadir}/%{name}/webapps
install -m 644 dist/bshservlet-wbsh.war %{buildroot}%{_datadir}/%{name}/webapps

# scripts
install -d %{buildroot}%{_bindir}

%jpackage_script bsh.Interpreter "\${BSH_DEBUG:+-Ddebug=true}" jline.console.internal.ConsoleRunner %{name}:jline %{name} true
%jpackage_script bsh.Console "\${BSH_DEBUG:+-Ddebug=true}" "" bsh bsh-console true

echo '#!%{_bindir}/bsh' > %{buildroot}%{_bindir}/bshdoc
cat scripts/bshdoc.bsh >> %{buildroot}%{_bindir}/bshdoc

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE
%doc README.md src/Changes.html src/CodeMap.html docs/faq/faq.html
%attr(0755,root,root) %{_bindir}/%{name}*
%if %{with desktop}
%{_datadir}/applications/%{name}-desktop.desktop
%{_datadir}/pixmaps/%{name}.png
%endif
%{_datadir}/%{name}
%config(noreplace,missingok) /etc/java/%{name}.conf

%files manual
%doc docs/manual/html
%doc docs/manual/images/*.jpg
%doc docs/manual/images/*.gif
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_14.b6jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_9.b6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_8.b6jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_5.b6jpp8
- new version

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt6_35jpp8
- new fc release

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

