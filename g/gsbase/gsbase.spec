Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-compat
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


Name:           gsbase
Version:        2.0.1
Release:        alt6_1jpp5
Epoch:          0
Summary:        GSBase
License:        Apache-style Software License
Group:          Development/Java
URL:            http://gsbase.sourceforge.net/
Source0:        %{name}-%{version}.tar.gz
# cvs -d:pserver:anonymous@gsbase.cvs.sourceforge.net:/cvsroot/gsbase login
# cvs -z3 -d:pserver:anonymous@gsbase.cvs.sourceforge.net:/cvsroot/gsbase export -r HEAD gsbase2
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        %{name}-%{version}-jpp-depmap.xml
Source5:        %{name}-%{version}.pom
Source6:        %{name}-build.xml

Patch0:         %{name}-maven.patch
Patch1:         %{name}-site-jsl.patch


%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: junit
BuildRequires: junitperf
%if %{with_maven}
BuildRequires: maven1 >= 0:1.1
BuildRequires: maven1-plugins-base
BuildRequires: maven1-plugin-changelog
BuildRequires: maven1-plugin-changes
BuildRequires: maven1-plugin-checkstyle
BuildRequires: maven1-plugin-developer-activity
BuildRequires: maven1-plugin-file-activity
BuildRequires: maven1-plugin-jdepend
BuildRequires: maven1-plugin-jxr
BuildRequires: maven1-plugin-license
BuildRequires: maven1-plugin-linkcheck
BuildRequires: maven1-plugin-pmd
BuildRequires: maven1-plugin-tasklist
BuildRequires: maven1-plugin-test
BuildRequires: maven1-plugin-xdoc
BuildRequires: saxon
BuildRequires: saxon-scripts
%endif
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires: junit
Requires: junitperf
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

%description
A collection of classes that are helpful 
when writing JUnit test cases. 


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %{with_maven}
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif

%prep
%setup -q 
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar" ); do
        mv $j $j.no
done
%patch0 -b .sav0
%patch1 -b .sav1
cp %{SOURCE6} build.xml

%build
%if %{with_maven}
export DEPCAT=$(pwd)/%{name}-%{version}-depcat.new.xml
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
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

export MAVEN_HOME_LOCAL=$(pwd)/.maven

maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5   -e \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=${MAVEN_HOME_LOCAL} \
        -Dmaven.test.error.ignore=true \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.xdoc.jsl=file://$(pwd)/xdocs/site.jsl \
        jar:jar javadoc:generate xdoc:transform
%else
export CLASSPATH=$(build-classpath \
junit \
junitperf \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
%endif

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap %{name} %{name} %{namedversion} JPP %{name}

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %{with_maven}
rm -rf target/docs/apidocs
cp -pr target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif

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

%files
%{_javadir}/*
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{subname}*-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%if %{with_maven}
%files manual
%doc %{_docdir}/%{name}-%{version}/*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt6_1jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt5_1jpp5
- use maven1

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt4_1jpp5
- selected java5 compiler explicitly

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt3_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_1jpp5
- converted from JPackage by jppimport script

