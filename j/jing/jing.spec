Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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

%define cvsversion 20030619

Name:           jing
Version:        0.1
Release:        alt3_0.20030619.9jpp5
Epoch:          0
Summary:        Jing, a validator for RELAX NG implemented in Java

Group:          Development/Java
License:        Open Source
URL:            http://www.thaiopensource.com/relaxng/jing.html
Source0:        http://www.thaiopensource.com/download/jing-20030619.zip
Source1:        jing_build.xml
Source2:        jing-20030619.pom
Patch0:         jing-xerces2.patch
Patch1:         jing-ValidatorImpl.patch
Patch2:         jing-VerifierHandlerImpl.patch

%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: junit >= 0:3.8.1
BuildRequires: xalan-j2 >= 0:2.7.0
BuildRequires: xerces-j2 >= 0:2.9.0
BuildRequires: isorelax
BuildRequires: saxon
Requires: xalan-j2 >= 0:2.7.0
Requires: xerces-j2 >= 0:2.9.0
Requires: isorelax
Requires: saxon

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4

%description
This version of Jing implements: RELAX NG 1.0 Specification,
RELAX NG Compact Syntax, and parts of RELAX NG DTD Compatibility, 
specifically checking of ID/IDREF/IDREFS.
Jing also has experimental support for schema languages other 
than RELAX NG; specifically W3C XML Schema (based on Xerces-J);
Schematron; Namespace Routing Language.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -T -c -n %{name}-%{cvsversion}
(cd ..
unzip -q %{SOURCE0} )
cp %{SOURCE1} build.xml
mkdir src
( cd src
unzip -q ../src.zip )
find . -name "*.jar" -exec rm {} \;

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=$(build-classpath \
xalan-j2 \
xerces-j2 \
saxon \
isorelax)
CLASSPATH=$CLASSPATH:src/test-input:target/classes:target/test-classes
ant dist javadoc 

%install
install -Dpm 644 dist/lib/%{name}-%{cvsversion}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap thaiopensource %{name} %{version} JPP %{name}

install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

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
%{_javadir}/*.jar
%{_datadir}/maven2
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}


%changelog
* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt3_0.20030619.9jpp5
- fixes for java6 support

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt2_0.20030619.9jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_0.20030619.9jpp5
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_0.20030619.8jpp1.7
- converted from JPackage by jppimport script

