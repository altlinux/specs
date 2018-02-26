Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define gcj_support %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_witho_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gport:0}}}

%define base_name commons-betwixt

Name:           jakarta-%{base_name}0
Version:        0.8
Release:        alt2_2jpp5
Epoch:          0
Summary:        Java bean to XML mapping library

Group:          Development/Java
License:        Apache Software License
URL:            http://jakarta.apache.org/commons/betwixt/
Source0:        commons-betwixt-0.8-src.tar.gz
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/commons-betwixt/commons-betwixt/0.8/commons-betwixt-0.8.pom
Patch0:         commons-betwixt-0.8-build_xml.patch


%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit >= 0:1.6
BuildRequires: junit
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-digester
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-beanutils
Requires: jakarta-commons-logging
Requires: jakarta-commons-digester
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-collections
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

%description
The Betwixt library provides an XML introspection mechanism for
mapping beans to XML in a flexible way. It is implemented using an
XMLIntrospector and XMLBeanInfo classes which are similar to the
standard Introspector and BeanInfo from the Java Beans specification.
Betwixt provides a way of turning beans into XML as well as
automatically generating digester rules in a way that can be
customized on a per type manner in the same way that the BeanInfo
mechanism can be used to customize the default introspection on a java
object.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildRequires: java-javadoc jakarta-commons-collections-javadoc >= 0:2.1
BuildRequires: jakarta-commons-logging-javadoc >= 0:1.0.2
BuildRequires: jakarta-commons-digester-javadoc >= 0:1.5
BuildRequires: jakarta-commons-beanutils-javadoc >= 0:1.6.1

%description    javadoc
%{summary}.


%prep
%setup -q -n %{base_name}-%{version}-src
%patch0 -b .sav
rm src/test/org/apache/commons/betwixt/TestRSSRoundTrip.java

%build
export LANG=en_US.ISO8859-1
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=$(build-classpath jakarta-commons-logging-api \
jakarta-commons-logging jakarta-commons-digester jakarta-commons-collections \
jakarta-commons-beanutils \
)
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dnoget=true \
  -Dbuild.sysclasspath=first \
  -Dj2se.javadoc=%{_javadocdir}/java \
  -Dcollections.javadoc=%{_javadocdir}/jakarta-commons-collections \
  -Dlogging.javadoc=%{_javadocdir}/jakarta-commons-logging \
  -Ddigester.javadoc=%{_javadocdir}/jakarta-commons-digester \
  -Dbeanutils.javadoc=%{_javadocdir}/jakarta-commons-beanutils \
  test dist


%install
install -Dpm 644 dist/%{base_name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in jakarta-*; do \
ln -sf ${jar} ${jar/jakarta-/}; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

%add_to_maven_depmap %{base_name} %{base_name} %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr RELEASE-NOTES.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%doc %{_docdir}/%{name}-%{version}/RELEASE-NOTES.txt
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.8-alt2_2jpp5
- fixed build with java 7

* Tue May 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.8-alt1_2jpp5
- fixed docdir ownership

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.8-alt1_1jpp5
- fixed build w/java5

* Mon Jul 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.8-alt1_1jpp1.7
- converted from JPackage by jppimport script

