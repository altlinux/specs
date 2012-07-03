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

%define gcj_support 0

%define section   devel
%define base_name commons-betwixt

Name:           jakarta-commons-betwixt
Version:        1.0
Release:        alt1_0.alpha1.7jpp5
Epoch:          0
Summary:        Java bean to XML mapping library

Group:          Development/Java
License:        Apache Software License
URL:            http://jakarta.apache.org/commons/betwixt/
Source0:        http://archive.apache.org/dist/jakarta/commons/betwixt/source/commons-betwixt-1.0-alpha-1-src.tar.gz
Source1:        rss-0.91.dtd
Source2:        http://mirrors.ibiblio.org/pub/mirrors/maven2/commons-betwixt/commons-betwixt/1.0-alpha-1/commons-betwixt-1.0-alpha-1.pom
Patch0:         %{name}-crosslink.patch
Patch1:         %{name}-version.patch
Patch2:         commons-betwixt-rss-dtd.patch

%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit >= 0:1.6
BuildRequires: junit >= 0:3.8.1
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-digester >= 0:1.7
BuildRequires: jakarta-commons-collections >= 0:2.1
BuildRequires: jakarta-commons-beanutils >= 0:1.6.1
Requires: jakarta-commons-logging
Requires: jakarta-commons-digester >= 0:1.7
Requires: jakarta-commons-beanutils >= 0:1.6.1
Requires: jakarta-commons-collections >= 0:2.1
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
BuildRequires: jakarta-commons-logging-javadoc
BuildRequires: jakarta-commons-digester-javadoc >= 0:1.7
BuildRequires: jakarta-commons-beanutils-javadoc >= 0:1.6.1
BuildArch: noarch

%description    javadoc
%{summary}.


%prep
%setup -q -n %{base_name}-%{version}-alpha-1
%patch0 -p0
%patch1 -p0
%patch2 -p0
cp %{SOURCE1} .
cp %{SOURCE1} src/test/org/apache/commons/betwixt/xmlunit/

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=$(build-classpath commons-logging-api \
commons-logging \
commons-digester \
commons-digester-rss \
commons-collections \
commons-beanutils \
)
ant \
  -Dnoget=true \
  -Dbuild.sysclasspath=first \
  -Dj2se.javadoc=%{_javadocdir}/java \
  -Dcollections.javadoc=%{_javadocdir}/jakarta-commons-collections \
  -Dlogging.javadoc=%{_javadocdir}/jakarta-commons-logging \
  -Ddigester.javadoc=%{_javadocdir}/jakarta-commons-digester \
  -Dbeanutils.javadoc=%{_javadocdir}/jakarta-commons-beanutils \
  dist


%install

install -Dpm 644 target/%{base_name}-%{version}-alpha-1.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{base_name}-%{version}.jar
ln -s %{base_name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{base_name}.jar
%add_to_maven_depmap %{base_name} %{base_name} 1.0-alpha-1 JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt RELEASE-NOTES.txt
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}


%changelog
* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.alpha1.7jpp5
- new jpp release

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.alpha1.6jpp5
- fixed build w/java5

* Fri Apr 27 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.alpha1.6jpp1.7
- converted from JPackage by jppimport script

* Tue Dec 20 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt0.1.alpha1
- previous build was broken, switch to previous "stable" release

* Sun Dec 11 2005 Vladimir Lettiev <crux@altlinux.ru> 0.8-alt0.1
- Rebuild for ALT Linux Sisyphus
- Spec cleanup

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:1.0-0.alpha1.4jpp
- Rebuild with ant-1.6.2

* Fri Aug 06 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.alpha1.3jpp
- Void change

* Tue Jun 01 2004 Randy Watler <rwatler at finali.com> - 0:1.0-0.alpha1.2jpp
- Upgrade to Ant 1.6.X

* Sun Oct 12 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.0-0.alpha1.1jpp
- First build.
