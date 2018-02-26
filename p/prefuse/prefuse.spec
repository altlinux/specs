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


Name:           prefuse
Version:        0.0
Release:        alt2_0.beta20071021.0jpp5
Epoch:          0
Summary:        Visualization Toolkit

Group:          Development/Java
License:        BSD
URL:            http://prefuse.org/
Source0:        http://prdownloads.sourceforge.net/prefuse/prefuse-beta-20071021.tar.bz2
Source1:        prefuse-beta-20071021.pom
Source2:        demos-beta-20071021.pom


%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: ant >= 0:1.6
BuildRequires: lucene1

Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description
Prefuse supports a rich set of features for data modeling, 
visualization, and interaction. It provides optimized data 
structures for tables, graphs, and trees, a host of layout 
and visual encoding techniques, and support for animation, 
dynamic queries, integrated search, and database connectivity. 
Prefuse is written in Java, using the Java 2D graphics library, 
and is easily integrated into Java Swing applications or web 
applets. 


%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.

%package        demo
Summary:        Examples for %{name}
Group:          Development/Documentation

%description    demo
%{summary}.

%prep
%setup -q -n %{name}-beta
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

rm ./src/prefuse/data/search/LuceneSearcher.java
rm ./src/prefuse/data/search/KeywordSearchTupleSet.java


%build
export CLASSPATH=$(build-classpath \
lucene1 \
)
CLASSPATH=build/prefuse/classes:$CLASSPATH

ant -Dbuild.sysclasspath=only -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 all api

%install

install -Dpm 644 build/%{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -Dpm 644 build/demos.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-demos-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

%add_to_maven_depmap org.prefuse %{name} %{version} JPP %{name}
%add_to_maven_depmap org.prefuse demos %{version} JPP %{name}-demos

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-demos.pom

#
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
#
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr demos/prefuse/demos $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%post
%update_maven_depmap
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%postun
%update_maven_depmap
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%doc license-prefuse.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}*%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files demo
%doc %{_datadir}/%{name}-%{version}

%changelog
* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.0-alt2_0.beta20071021.0jpp5
- fixed lucene classpath
- note: Lucene support is removed as source rely on lucene 1.4;

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.0-alt1_0.beta20071021.0jpp5
- fixed build

* Sat Nov 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.0-alt1_0.beta20071021.0jpp1.7
- new version;
- based on JPackage spec;
- note: removed Lucene support as source rely on lucene 1.4;

