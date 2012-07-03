Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define gcj_support 0

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}


Name:           bcel
Version:        5.2
Release:        alt3_3jpp5
Epoch:          1
Summary:        Byte Code Engineering Library
License:        Apache Software License
Source0:        http://www.apache.org/dist/jakarta/%{name}/source/%{name}-%{version}-src.tar.gz
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        %{name}-%{version}-jpp-depmap.xml
Source5:        commons-build.tar.gz
Source6:        %{name}-%{version}-build.xml
Source7:        %{name}-%{version}.pom

Patch0:         %{name}-%{version}-project_properties.patch
URL:            http://jakarta.apache.org/%{name}/
Group:          Development/Java
Requires: regexp
BuildRequires: ant
%if %{with_maven}
BuildRequires: maven1 >= 0:1.1
BuildRequires: saxon
BuildRequires: saxon-scripts
BuildRequires: maven1-plugins-base
BuildRequires: maven1-plugin-changelog
BuildRequires: maven1-plugin-changes
BuildRequires: maven1-plugin-developer-activity
BuildRequires: maven1-plugin-jxr
BuildRequires: maven1-plugin-license
BuildRequires: maven1-plugin-pmd
BuildRequires: maven1-plugin-test
BuildRequires: maven1-plugin-xdoc
Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2
%endif
BuildRequires: regexp
BuildRequires: jpackage-utils >= 0:1.7.2
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
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

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Java

%description manual
%{summary}.

%prep

%setup -q
gzip -dc %{SOURCE5} | tar xf -
# remove all binary libs
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    %{__mv} $j ${j}.no
done
cp %{SOURCE6} build.xml
%patch0 -b .sav

%build
%if %{with_maven}
export DEPCAT="$(pwd)/%{name}-%{version}-depcat.new.xml"
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
        /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > %{name}-%{version}-depmap.new.xml

for p in $(find . -name project.xml); do
    pushd $(dirname $p)
        %{__cp} project.xml project.xml.orig
        /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} \
            map="%{SOURCE4}"
    popd
done

export MAVEN_HOME_LOCAL="$(pwd)/.maven"

maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=${MAVEN_HOME_LOCAL} \
        jar:jar javadoc:generate xdoc:transform
%else
ant -Dregexp.jar="file://$(build-classpath regexp)" jar javadoc
%endif

%install
# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__install} -m 0644 target/%{name}-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}-%{version}.jar
(
    cd %{buildroot}%{_javadir}
    for jar in *-%{version}*; do 
        %{__ln_s} ${jar} `echo $jar | %{__sed}  "s|-%{version}||g"`
    done
)
# depmap frags
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
%add_to_maven_depmap org.apache.bcel %{name} %{version} JPP %{name}
# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__install} -m 0644 %{SOURCE7} \
    %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/default_poms
%{__install} -m 0644 %{SOURCE7} \
    %{buildroot}%{_datadir}/maven2/default_poms/JPP-%{name}.pom

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%if %{with_maven}
%{__cp} -pr target/docs/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__rm} -rf target/docs/apidocs
%else
%{__cp} -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__rm} -rf docs/api
%endif
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} # ghost symlink

# manual
%{__mkdir_p} %{buildroot}%{_docdir}/%{name}-%{version}
%if %{with_maven}
%{__cp} -pr target/docs/* %{buildroot}%{_docdir}/%{name}-%{version}
%else
%{__cp} -pr docs/* %{buildroot}%{_docdir}/%{name}-%{version}
%endif
%{__cp} LICENSE.txt %{buildroot}%{_docdir}/%{name}-%{version}

%if %{gcj_support}
export CLASSPATH="$(build-classpath gnu-crypto)"
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
%{__rm} -f %{_javadocdir}/%{name}
%{__ln_s} %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    %{__rm} -f %{_javadocdir}/%{name}
fi

%post
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]; then
    %{_bindir}/rebuild-gcj-db
fi
%endif

%postun
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]; then
    %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt 
%{_javadir}/*
%if %{with_maven}
%{_datadir}/maven2/poms/*
%{_datadir}/maven2/default_poms/*
%endif
%{_mavendepmapfragdir}
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-*.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
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
