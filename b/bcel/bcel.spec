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

Name:           bcel
Version:        5.2
Release:        alt4_15jpp7
Epoch:          1
Summary:        Byte Code Engineering Library
License:        ASL 2.0
Source0:        %{name}-%{version}-src.tar.gz
#svn export https://svn.apache.org/repos/asf/jakarta/bcel/tags/BCEL_5_2
#tar czvf bcel-5.2-src.tar.gz BCEL_5_2
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        %{name}-%{version}-jpp-depmap.xml
#Source5:        commons-build.tar.gz
Source5:        bcel-jakarta-site2.tar.gz
Source6:        %{name}-%{version}-build.xml
Source7:        %{name}-%{version}.pom
Source8:        %{name}-MANIFEST.MF

Patch0:         %{name}-%{version}-project_properties.patch
URL:            http://jakarta.apache.org/%{name}/
Group:          Development/Java
Requires:       regexp
BuildRequires:  zip
BuildRequires:  ant
BuildRequires:  jdom
BuildRequires:  velocity
BuildRequires:  jakarta-commons-collections
BuildRequires:  apache-commons-lang
BuildRequires:  avalon-logkit
BuildRequires:  werken-xpath
BuildRequires:  regexp
BuildRequires:  jpackage-utils >= 0:1.7.2
BuildArch:      noarch
Source44: import.info

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

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n BCEL_5_2
gzip -dc %{SOURCE5} | tar xf -
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
mkdir jakarta-site2/lib
pushd jakarta-site2/lib/
  build-jar-repository -s -p . jdom
  build-jar-repository -s -p . velocity
  build-jar-repository -s -p . commons-collections
  build-jar-repository -s -p . commons-lang
  build-jar-repository -s -p . avalon-logkit
  build-jar-repository -s -p . werken-xpath
popd
cp %{SOURCE6} build.xml
%patch0 -b .sav

# fix wrong-file-end-of-line-encoding
sed -i 's/\r//' docs/verifier/V_API_SD.eps docs/eps/classloader.fig

%build
#ant -Dregexp.jar="file://$(build-classpath regexp)" jar javadoc
ant     -Dbuild.dest=build/classes -Dbuild.dir=build -Ddocs.dest=docs \
        -Ddocs.src=xdocs -Djakarta.site2=jakarta-site2 -Djdom.jar=jdom.jar \
        -Dregexp.jar="file://$(build-classpath regexp)" \
        jar javadoc xdocs

%install
# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE8} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u target/%{name}-%{version}.jar META-INF/MANIFEST.MF

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__install} -m 0644 target/%{name}-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}.jar

# pom
%{__mkdir_p} %{buildroot}%{_mavenpomdir}
%{__install} -m 0644 %{SOURCE7} \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# depmap frags
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a org.apache.bcel:%{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}
%{__cp} -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}
%{__rm} -rf dist/docs/api

# manual
%{__mkdir_p} %{buildroot}%{_docdir}/%{name}-%{version}
%{__cp} -pr docs/* %{buildroot}%{_docdir}/%{name}-%{version}
%{__cp} LICENSE.txt %{buildroot}%{_docdir}/%{name}-%{version}
%{__cp} NOTICE.txt %{buildroot}%{_docdir}/%{name}-%{version}

%files
%doc %{_docdir}/%{name}-%{version}
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:5.2-alt4_15jpp7
- new release

* Fri Mar 15 2013 Igor Vlasenko <viy@altlinux.ru> 1:5.2-alt4_13jpp7
- fc update

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1:5.2-alt4_3jpp5
- build with saxon6-scripts

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 1:5.2-alt3_3jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 1:5.2-alt2_3jpp5
- use maven1

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
