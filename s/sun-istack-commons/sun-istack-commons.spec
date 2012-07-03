BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2011, JPackage Project
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


Name:           sun-istack-commons
Version:        1.0
Release:	alt3_3jpp6
Epoch:          1
Summary:        Commons for JAXP, JAXB, SAAJ, and JAX-WS
License:        CDDL
Url:            https://istack-commons.dev.java.net
Source0:        sun-istack-commons-1.0.tar.gz
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r istack-commons-1_0 -d sun-istack-commons-1.0 istack-commons/istack-commons

Source1:        CDDLv1.0.html
Source2:        http://download.java.net/maven/2/com/sun/istack/istack-commons/1.0/istack-commons-1.0.pom

Group:          Development/Java
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  stax_1_0_api
BuildRequires:  jaf_1_1_api
BuildRequires:  junit
BuildRequires:  dom4j
%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires:  ant >= 0:1.7.1
Requires:  stax_1_0_api
Requires:  jaf_1_1_api
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info

%description
JAXP, JAXB, SAAJ, and JAX-WS projects are often used together 
by other projects (such as Mustang, Glassfish, and JWSDP to 
name a few.) But at the same time, they are released 
independently, and those technolgoies don't necessarily 
have dependencies between them. 
To promote code reuse between these projects, we host the 
common part in a separate project, so that when we ship 
individually, we can each carry istack-commons.jar, and when
we deliver together into another technology, we can reduce 
the footprint. 


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
# remove all binary libs
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
ln -sf $(build-classpath stax_1_0_api) runtime/lib/jsr173_1.0_api.jar
ln -sf $(build-classpath jaf_1_1_api) runtime/lib/activation.jar
ln -sf $(build-classpath junit) test/lib/junit.jar

ln -sf $(build-classpath dom4j) test/lib/dom4j.jar
%build
export CLASSPATH=$(build-classpath stax_1_0_api)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 dist javadoc

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 runtime/build/istack-commons-runtime.jar \
                $RPM_BUILD_ROOT%{_javadir}/%{name}/runtime-%{version}.jar
install -m 644 test/build/istack-commons-test.jar \
                $RPM_BUILD_ROOT%{_javadir}/%{name}/test-%{version}.jar
install -m 644 tools/build/istack-commons-tools.jar \
                $RPM_BUILD_ROOT%{_javadir}/%{name}/tools-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir}/%{name}
for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE2} \
          $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap com.sun.istack istack-commons %{version} JPP %{name}
install -m 644 runtime/pom.xml \
          $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-runtime.pom
%add_to_maven_depmap com.sun.istack commons-runtime %{version} JPP/%{name} runtime
install -m 644 tools/pom.xml \
          $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-tools.pom
%add_to_maven_depmap com.sun.istack commons-tools %{version} JPP/%{name} tools

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -pm 644 %{SOURCE1} \
           $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/CDDLv1.0.html

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%{_docdir}/%{name}-%{version}/CDDLv1.0.html
%{_javadir}/%{name}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%changelog
* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt3_3jpp6
- new jpp relase

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt3_2jpp5
- fixes for java6 support

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt2_2jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_2jpp5
- fixed repocop warnings

* Sun Oct 19 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_1jpp5
- jpackage 5.0

* Sat Jan 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:20070625-alt1_1jpp5.0
- first build

