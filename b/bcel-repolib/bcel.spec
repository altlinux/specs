Packager: Igor Vlasenko <viy@altlinux.ru>
%define oldname bcel
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

%bcond_with bootstrap
%bcond_with maven
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/apache-bcel/5.1-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0


Name:           bcel-repolib
Version:        5.1
Release:        alt2_16jpp5
Epoch:          1
Summary:        Byte Code Engineering Library
License:        ASL 2.0
URL:            http://jakarta.apache.org/%{oldname}/
Group:          Development/Java
# svn -q export https://svn.apache.org/repos/asf/jakarta/bcel/tags/BCEL_5_1
Source0:        bcel-5.1-src.tar.gz
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        bcel-5.1-jpp-depmap.xml
Source5:        bcel-jakarta-site2.tar.gz
Source6:        bcel-5.1-component-info.xml
Source7:        bcel-%{version}.pom
Patch0:         bcel-5.1-build.patch
Patch1:         bcel-5.1-project_xml.patch
Requires: regexp
BuildRequires: ant
BuildRequires: regexp
BuildRequires: jpackage-utils >= 0:1.6
%if %with maven
BuildRequires: maven >= 0:1.1
BuildRequires: saxon
BuildRequires: saxon-scripts
%endif
%if %without bootstrap
BuildRequires: jdom
BuildRequires: velocity
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-lang
BuildRequires: excalibur-avalon-logkit
BuildRequires: werken.xpath
%endif
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif

%description
The Byte Code Engineering Library (formerly known as JavaClass) is
intended to give users a convenient possibility to analyze, create, and
manipulate (binary) Java class files (those ending with .class). Classes
are represented by objects which contain all the symbolic information of
the given class: methods, fields and byte code instructions, in
particular.  Such objects can be read from an existing file, be
transformed by a program (e.g. a class loader at run-time) and dumped to
a file again. An even more interesting application is the creation of
classes from scratch at run-time. The Byte Code Engineering Library
(BCEL) may be also useful if you want to learn about the Java Virtual
Machine (JVM) and the format of Java .class files.  BCEL is already
being used successfully in several projects such as compilers,
optimizers, obfuscators and analysis tools, the most popular probably
being the Xalan XSLT processor at Apache.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{oldname}
Group:          Development/Documentation

Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{oldname}.

%package manual
Summary:        Manual for %{oldname}
Group:          Development/Java
BuildArch: noarch

%description manual
Documentation for %{oldname}.

%package demo
Summary:        Examples for %{oldname}
Group:          Development/Java

%description demo
%{summary}.

%prep
%setup -q -n BCEL_5_1
%setup -q -T -D -a 5 -n BCEL_5_1
%patch0 -p1
%patch1 -p0
%{_bindir}/find . -name "*.jar" | %{_bindir}/xargs -t %{__rm}

%if %without bootstrap
%{__mkdir_p} jakarta-site2/lib
pushd jakarta-site2/lib/
  %{_bindir}/build-jar-repository -s -p . jdom
  %{_bindir}/build-jar-repository -s -p . velocity
  %{_bindir}/build-jar-repository -s -p . commons-collections
  %{_bindir}/build-jar-repository -s -p . excalibur/avalon-logkit
  %{_bindir}/build-jar-repository -s -p . werken.xpath
  %{_bindir}/build-jar-repository -s -p . commons-lang
popd
%endif

pushd lib
  %{__ln_s} $(build-classpath regexp) Regex.jar
popd

# very broken build
%{__perl} -p -i -e 's| depends=\"examples\"||g;' build.xml
/bin/touch manifest.txt

# fix file-not-utf8
%{__mv} docs/verifier/JustIce.lyx docs/verifier/JustIce.lyx.orig
%{_bindir}/iconv -f iso-8859-1 -t utf-8 -o docs/verifier/JustIce.lyx docs/verifier/JustIce.lyx.orig
%{__rm} docs/verifier/JustIce.lyx.orig

%build
%if %with maven
export DEPCAT=$(pwd)/bcel-5.1-depcat.new.xml
/bin/echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
/bin/echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
      %{_bindir}/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
/bin/echo >> $DEPCAT
/bin/echo '</depset>' >> $DEPCAT
%{_bindir}/saxon $DEPCAT %{SOURCE2} > bcel-5.1-depmap.new.xml

for p in $(find . -name project.xml); do
    pushd $(dirname $p)
      %{__cp} -p project.xml project.xml.orig
      %{_bindir}/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

export MAVEN_HOME_LOCAL=$(pwd)/.maven
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=${MAVEN_HOME_LOCAL} \
        jar:jar javadoc:generate xdoc:transform
%else
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.dest=build/classes -Dbuild.dir=build \
        -Ddocs.src=xdocs -Djakarta.site2=jakarta-site2 -Djdom.jar=jdom.jar \
        compile jar apidocs xdocs
%endif

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}

%if %with maven
%{__install} -p -m 0644 target/%{oldname}-%{version}.jar %{buildroot}%{_javadir}/%{oldname}-%{version}.jar
%else
%{__install} -p -m 0644 build/%{oldname}.jar %{buildroot}%{_javadir}/%{oldname}-%{version}.jar
%endif

(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# depmap frags
%add_to_maven_depmap %{oldname} %{oldname} %{version} JPP %{oldname}
%add_to_maven_depmap org.apache.bcel %{oldname} %{version} JPP %{oldname}

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__install} -p -m 0644 %{SOURCE7} %{buildroot}%{_datadir}/maven2/poms/JPP-%{oldname}.pom

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{oldname}-%{version}
%{__ln_s} %{oldname}-%{version} %{buildroot}%{_javadocdir}/%{oldname}

%if %with maven
%{__cp} -pr target/docs/apidocs/* %{buildroot}%{_javadocdir}/%{oldname}
# FIXME: (dwalluck): breaks -bi --short-circuit
%{__rm} -rf target/docs/apidocs
%else
%{__cp} -pr docs/api/* %{buildroot}%{_javadocdir}/%{oldname}
# FIXME: (dwalluck): breaks -bi --short-circuit
%{__rm} -rf docs/api
%endif

# samples
%{__mkdir_p} %{buildroot}%{_datadir}/%{oldname}-%{version}
%{__cp} -pr examples/* %{buildroot}%{_datadir}/%{oldname}-%{version}

# manual
%{__mkdir_p} %{buildroot}%{_docdir}/%{oldname}-%{version}

%if %with maven
%{__cp} -pr target/docs/* %{buildroot}%{_docdir}/%{oldname}-%{version}
%else
%{__cp} -pr docs/* %{buildroot}%{_docdir}/%{oldname}-%{version}
%endif

%if %with repolib
%{__install} -d -m 755 %{buildroot}%{repodir}
%{__install} -d -m 755 %{buildroot}%{repodirlib}
%{__install} -p -m 644 %{SOURCE6} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{oldname}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 755 %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE2} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE3} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE4} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE5} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE7} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH1} %{buildroot}%{repodirsrc}
cp -p %{buildroot}%{_javadir}/%{oldname}-%{version}.jar %{buildroot}%{repodirlib}/bcel.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
%if %with repolib

%files
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 1:5.1-alt2_16jpp5
- fixed build with moved maven1

* Fri Aug 21 2009 Igor Vlasenko <viy@altlinux.ru> 1:5.1-alt1_16jpp5
- repolib

* Sat May 02 2009 Igor Vlasenko <viy@altlinux.ru> 1:5.2-alt1_3jpp5
- reverted to 5.2

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 1:5.1-alt1_16jpp5
- downgrade to match 5.0; added repolib

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.2-alt2_3jpp1.7
- updated to new jpackage release

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:5.2-alt2_2jpp1.7
- updated to new jpackage release

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:5.2-alt2_1jpp1.7
- fixed [Bug 11852] Misprint in package description

* Mon Jul 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:5.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 5.1-alt3
- added jpackage compatible symlinks
- rebuild with java-1.4

* Sun Feb 26 2006 Mikhail Zabaluev <mhz@altlinux.ru> 5.1-alt2
- Patch0: disambiguated use of the Deprecated class to build with JDK 1.5
- Updated Patch1: fixes to build with JDK 1.5
- Use macros from rpm-build-java

* Thu Sep 11 2003 Mikhail Zabaluev <mhz@altlinux.ru> 5.1-alt1
- New version
- Patch0 gone upstream
- Removed doc package due to absence of the docs in the source tarball
- Fix the build.xml crack [Patch1]

* Wed Nov 20 2002 Mikhail Zabaluev <mhz@altlinux.ru> 5.0-alt1
- Adopted from JPackage
