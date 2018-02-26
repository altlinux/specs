Obsoletes: asm = 2.0-alt0.RC1
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

# tests need lots of: cpu, mem, time
%define tests %{?_with_tests:1}%{!?_with_tests:%{?_without_tests:0}%{!?_without_tests:%{?_tests:%{_tests}}%{!?_tests:0}}}


Name:           asm2
Version:        2.2.3
Release:        alt4_8jpp6
Epoch:          0
Summary:        Code manipulation tool to implement adaptable systems
License:        BSD
URL:            http://asm.objectweb.org/
Group:          Development/Java
Source0:        http://download.forge.objectweb.org/asm/asm-2.2.3.tar.gz
Source1:        http://asm.objectweb.org/current/asm-eng.pdf
Source2:        http://asm.objectweb.org/current/asm-transformations.pdf
Source3:        http://download.forge.objectweb.org/asm/asm-guide.pdf
Source4:        http://asm.objectweb.org/doc/faq.html
Source5:        asm-%{version}.pom
Source6:        asm-all-%{version}.pom
Source7:        asm-analysis-%{version}.pom
Source8:        asm-attrs-%{version}.pom
Source9:        asm-commons-%{version}.pom
Source10:       asm-parent-%{version}.pom
Source11:       asm-tree-%{version}.pom
Source12:       asm-util-%{version}.pom
Source13:       asm-xml-%{version}.pom
Patch0:         asm2-build_xml.patch
Patch1:         asm2-SerialVersionUIDAdder.patch
Patch2:         asm2-test-build_xml.patch
Patch3:         asm2-ALLPerfTest.patch
Patch4:         asm2-test-heap.patch
Patch5:         asm2-xml-no-classpath-in-manifest.patch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
%if %{tests}
BuildRequires:  ant-junit
BuildRequires:  asm2
BuildRequires:  bcel
BuildRequires:  ccl-util
BuildRequires:  cobertura
BuildRequires:  jakarta-oro
BuildRequires:  janino
BuildRequires:  javancss
BuildRequires:  javassist
BuildRequires:  log4j
%endif
BuildRequires:  objectweb-anttask
%if ! %{gcj_support}
BuildArch:      noarch
%endif

Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
%endif
Source44: import.info

%description
ASM is a Java bytecode manipulation framework. It can be 
used to dynamically generate stub classes or other proxy 
classes, directly in binary form, or to dynamically modify 
classes at load time, i.e., just before they are loaded into
the Java Virtual Machine.
ASM offers similar functionalities as BCEL or SERP, but is 
much smaller (33KB instead of 350KB for BCEL and 150KB for 
SERP) and faster than these tools (the overhead of a load 
time class transformation is of the order of 60%% with ASM, 
700%% or more with BCEL, and 1100%% or more with SERP). Indeed 
ASM was designed to be used in a dynamic way* and was 
therefore designed and implemented to be as small and 
as fast as possible.
(* ASM can of course be used in a static way too.)


%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    manual
%{summary}.

%package        demo
Summary:        Examples for %{name}
Group:          Development/Documentation
Requires:       %{name} = %{version}

%description    demo
%{summary}.

%prep
%setup -q -n asm-%{version}
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .
mkdir test/lib
%if %{tests}
pushd test/lib
ln -sf $(build-classpath asm2/asm2)
ln -sf $(build-classpath cobertura)
ln -sf $(build-classpath log4j)
ln -sf $(build-classpath jakarta-oro)
ln -sf $(build-classpath ccl-util) ccl.jar
ln -sf $(build-classpath javancss)
popd
%endif

%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p1

rm test/perf/org/objectweb/asm/SERPPerfTest.java
rm test/conform/adviceadapter2.xml

perl -pi -e 's/\r$//g' README.txt

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%if %{tests}
export CLASSPATH=$(build-classpath asm2/asm2 asm2/asm2-tree)
%endif
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
%if %{tests}
  -Dbcel.path=$(build-classpath bcel) \
  -Djanino.path=$(build-classpath janino) \
  -Djavassist.path=$(build-classpath javassist) \
%endif
  -Dobjectweb.ant.tasks.path=$(build-classpath objectweb-anttask) \
  jar \
  jdoc \
  examples \
%if %{tests}
  coverage \
  test \
  coverage.report \
  test.report \
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

for jar in output/dist/lib/*.jar; do
newjar=${jar/asm-/asm2-}
install -m 644 ${jar} \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/`basename ${newjar}`
done
install -m 644 output/dist/lib/all/asm-all-%{version}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-all-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

%add_to_maven_depmap asm asm-parent %{version} JPP asm2-parent
%add_to_maven_depmap asm2 asm-parent %{version} JPP asm2-parent
%add_to_maven_depmap asm asm-all %{version} JPP asm2-all
%add_to_maven_depmap asm2 asm-all %{version} JPP asm2-all
%add_to_maven_depmap asm asm-analysis %{version} JPP/asm2 asm2-analysis
%add_to_maven_depmap asm2 asm-analysis %{version} JPP/asm2 asm2-analysis
%add_to_maven_depmap asm asm-attrs %{version} JPP/asm2 asm2-attrs
%add_to_maven_depmap asm2 asm-attrs %{version} JPP/asm2 asm2-attrs
%add_to_maven_depmap asm asm-commons %{version} JPP/asm2 asm2-commons
%add_to_maven_depmap asm2 asm-commons %{version} JPP/asm2 asm2-commons
%add_to_maven_depmap asm asm-tree %{version} JPP/asm2 asm2-tree
%add_to_maven_depmap asm2 asm-tree %{version} JPP/asm2 asm2-tree
%add_to_maven_depmap asm asm-util %{version} JPP/asm2 asm2-util
%add_to_maven_depmap asm2 asm-util %{version} JPP/asm2 asm2-util
%add_to_maven_depmap asm asm-xml %{version} JPP/asm2 asm2-xml
%add_to_maven_depmap asm2 asm-xml %{version} JPP/asm2 asm2-xml
%add_to_maven_depmap asm asm %{version} JPP/asm2 asm2
%add_to_maven_depmap asm2 asm %{version} JPP/asm2 asm2

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-all.pom
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-analysis.pom
install -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-attrs.pom
install -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-commons.pom
install -m 644 %{SOURCE10} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
install -m 644 %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-tree.pom
install -m 644 %{SOURCE12} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-util.pom
install -m 644 %{SOURCE13} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-xml.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/dist/doc/javadoc/user/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
(cd $RPM_BUILD_ROOT%{_javadocdir} && ln -sf %{name}-%{version} %{name})

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr output/dist/examples $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc README.txt 
%dir %{_datadir}/%{name}-%{version}
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc faq.html
%doc *.pdf

%files demo
%{_datadir}/%{name}-%{version}/examples

%changelog
* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt4_8jpp6
- added versioned pom groupid asm2

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt3_8jpp6
- new jpp relase

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt3_7jpp5
- fixed docdir ownership

* Tue Sep 23 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt3_2jpp5
- fixed symlink

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt2_2jpp1.7
- updated to new jpackage release

* Tue Nov 27 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt2_1jpp1.7
- added link to parent pom

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Wed May 16 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_2jpp1.7
- fixed build with ant-1.7.0

* Thu Apr 28 2005 Vladimir Lettiev <crux@altlinux.ru> 2.0-alt0.RC1
- Initial release for ALT Linux Sisyphus

