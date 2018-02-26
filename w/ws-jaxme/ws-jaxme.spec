Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: jakarta-commons-codec
Requires: jakarta-commons-codec
Requires: xmldb-api-sdk
BuildRequires: xmldb-api-sdk
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

%define base_name jaxme

Name:           ws-jaxme
Version:        0.5.2
Release:        alt2_1jpp5
Epoch:          0
Summary:        Open source implementation of JAXB

Group:          Development/Java
License:        Apache Software License
URL:            http://ws.apache.org/jaxme/
Source0:        ws-jaxme-0.5.2-src.tar.gz
# svn export https://svn.apache.org/repos/asf/webservices/jaxme/tags/R0_5_2/ ws-jaxme-0.5.2

Source1:        ws-jaxme-0.5-docs.tar.gz
# generated docs with forrest-0.5.1
Source2:        jaxme2-0.5.2.pom
Source3:        jaxme2-rt-0.5.2.pom
Source4:        jaxmeapi-0.5.2.pom
Source5:        jaxmejs-0.5.2.pom
Source6:        jaxmepm-0.5.2.pom
Source7:        jaxmexs-0.5.2.pom

Patch0:         ws-jaxme-ant-scripts.patch

# ws-jaxme 0.5.1 fedora
Source11:        ws-jaxme-bind-MANIFEST.MF
Patch3:         ws-jaxme-jdk16.patch
Patch5:         ws-jaxme-use-commons-codec.patch


%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: ant >= 0:1.6
BuildRequires: antlr
BuildRequires: junit
BuildRequires: hsqldb
BuildRequires: log4j
BuildRequires: xmldb-api
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis

Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2

Requires: ant
Requires: antlr
Requires: log4j
Requires: xml-commons-jaxp-1.3-apis
Requires: xmldb-api


%description
A Java/XML binding compiler takes as input a schema 
description (in most cases an XML schema, but it may 
be a DTD, a RelaxNG schema, a Java class inspected 
via reflection, or a database schema). The output is 
a set of Java classes:
* A Java bean class matching the schema description. 
  (If the schema was obtained via Java reflection, 
  the original Java bean class.)
* Read a conforming XML document and convert it into 
  the equivalent Java bean.
* Vice versa, marshal the Java bean back into the 
  original XML document.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description    manual
%{summary}.

%prep
%setup -q -n %{name}-%{version}
for j in $(find . -name "*.jar"); do
      mv $j $j.no
done
mkdir -p build/docs/build/site
pushd build/docs/build/site
tar xzf %{SOURCE1}
popd

%patch0 -b .sav
#%patch3 -p1
%patch5 -b .sav

subst 's,<pathelement location="\${preqs}/ant.jar"/>,<pathelement location="${preqs}/ant.jar"/><pathelement location="${preqs}/commons-codec.jar"/>,' ant/jm.xml

%build
build-jar-repository -s -p prerequisites \
ant \
antlr \
junit \
log4j \
xerces-j2 \
xml-commons-jaxp-1.3-apis \
xmldb-api \
hsqldb \
commons-codec

ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 all 
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 javadoc

mkdir -p META-INF
cp -p %{SOURCE11} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u dist/jaxmeapi-%{version}.jar META-INF/MANIFEST.MF

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{base_name}
for jar in dist/*.jar; do
   install -m 644 ${jar} $RPM_BUILD_ROOT%{_javadir}/%{base_name}/
done
(cd $RPM_BUILD_ROOT%{_javadir}/%{base_name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{base_name} && for jar in *.jar; do ln -sf ${jar} ws-${jar}; done)

%add_to_maven_depmap org.apache.ws.jaxme jaxme2 %{version} JPP/jaxme jaxme2
%add_to_maven_depmap org.apache.ws.jaxme jaxme2-rt %{version} JPP/jaxme jaxme2-rt
%add_to_maven_depmap org.apache.ws.jaxme jaxmeapi %{version} JPP/jaxme jaxmeapi
%add_to_maven_depmap org.apache.ws.jaxme jaxmejs %{version} JPP/jaxme jaxmejs
%add_to_maven_depmap org.apache.ws.jaxme jaxmepm %{version} JPP/jaxme jaxmepm
%add_to_maven_depmap org.apache.ws.jaxme jaxmexs %{version} JPP/jaxme jaxmexs

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jaxme-jaxme2.pom
install -pm 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jaxme-jaxme2-rt.pom
install -pm 644 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jaxme-jaxmeapi.pom
install -pm 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jaxme-jaxmejs.pom
install -pm 644 %{SOURCE6} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jaxme-jaxmepm.pom
install -pm 644 %{SOURCE7} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jaxme-jaxmexs.pom

#javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/src/documentation/content/apidocs $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf build/docs/build/site/apidocs

#manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr build/docs/build/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p LICENSE $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

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
%doc %{_docdir}/%{name}-%{version}/LICENSE
%{_javadir}/%{base_name}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/jaxme*%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}


%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Fri May 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt2_1jpp5
- explicitly selected java5 compiler

* Mon Jan 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt1_1jpp5
- added OSGi provides

* Tue Oct 23 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Sun May 06 2007 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2
- added JPackage compatible symlinks

* Sat Apr 23 2005 Vladimir Lettiev <crux@altlinux.ru> 0.3.1-alt1
- Initial build for ALT Linux Sisyphus

