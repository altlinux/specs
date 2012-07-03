BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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

%define jaxbver  2.1

Name:           sun-jaxb-2.1-impl
Version:        2.1.13
Release:        alt2_1jpp6
Epoch:          0
Summary:        JAXB Reference Implementation
License:        CDDL
Url:            https://jaxb2-sources.dev.java.net/
Source0:        sun-jaxb-2.1-impl-2.1.13.tgz
# svn export https://svn.java.net/svn/jaxb~version2/tags/jaxb-2_1_13-tag sun-jaxb-2.1-impl-2.1.13
# tar czf ../SOURCES/sun-jaxb-2.1-impl-2.1.13.tgz sun-jaxb-2.1-impl-2.1.13/

Source1:        http://download.java.net/maven/2/com/sun/xml/bind/jaxb-impl/2.1.13/jaxb-impl-2.1.13.pom
Source2:        http://download.java.net/maven/2/com/sun/xml/bind/jaxb-xjc/2.1.13/jaxb-xjc-2.1.13.pom
# Patch to use original xml-commons-resolver11 (?)
Patch0:         sun-jaxb-2.1-impl-Options.patch
Patch1:         sun-jaxb-2.1-impl-nbproject-build-impl.patch
Patch2:         sun-jaxb-2.1-impl-scripts.patch

Group:          Development/Java
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  antlr
BuildRequires:  args4j10
BuildRequires:  dom4j
BuildRequires:  isorelax
BuildRequires:  jaf_1_1_api
BuildRequires:  jakarta-commons-jelly
BuildRequires:  jakarta-commons-jelly-tags-util
BuildRequires:  javamail_1_4_api
BuildRequires:  javatools-package-rename-task
BuildRequires:  jing >= 0:0.1-0.20030619.9jpp
BuildRequires:  jsp_2_1_api
BuildRequires:  msv-msv
BuildRequires:  msv-xsdlib
BuildRequires:  relaxngcc
BuildRequires:  relaxngDatatype
BuildRequires:  rngom
BuildRequires:  servlet_2_5_api
BuildRequires:  stax_1_0_api
BuildRequires:  stax-ex >= 0:1.2
BuildRequires:  sun-codemodel
BuildRequires:  sun-dtdparser
BuildRequires:  sun-fi >= 0:1.2.2
BuildRequires:  sun-htmlmacro
BuildRequires:  sun-istack-commons >= 1:1.0
BuildRequires:  sun-jaxb-1.0-impl
BuildRequires:  sun-jaxb-2.1-api
BuildRequires:  sun-txw2
BuildRequires:  sun-txw2-compiler
BuildRequires:  sun-xsom
BuildRequires:  xml-commons-resolver11

Requires:  ant
Requires:  antlr
Requires:  dom4j
Requires:  isorelax
Requires:  jaf_1_1_api
Requires:  javamail_1_4_api
Requires:  jsp_2_1_api
Requires:  msv-msv
Requires:  relaxngDatatype
Requires:  servlet_2_5_api
Requires:  stax_1_0_api
Requires:  stax-ex >= 0:1.2
Requires:  sun-fi >= 0:1.2.2
Requires:  sun-jaxb-2.1-api
%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info

%description
The Java Architecture for XML Binding (JAXB) 2.1
Reference Implementation from Sun.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

# jaxb-ri/tools/lib/util/istack-commons-test.jar.no
# jaxb-ri/tools/lib/util/xercesImpl.jar.no
# jaxb-ri/tools/lib/util/ant-trax.jar.no
# jaxb-ri/tools/lib/util/ant-junit.jar.no
# jaxb-ri/tools/lib/util/maven-repository-importer.jar.no
# jaxb-ri/tools/lib/util/ant.jar.no
# jaxb-ri/tools/lib/util/ant-contrib-0.6.jar.no
# jaxb-ri/tools/lib/util/ant-launcher.jar.no
# jaxb-ri/tools/lib/util/ant-fsget.jar.no
# jaxb-ri/tools/lib/src/jsr173_1.0_src.jar.no
# jaxb-ri/tools/lib/src/jsr173_1.0_javadoc.jar.no

pushd jaxb-ri
mv tools/lib/util/sfx4j-1.0.jar.no tools/lib/util/sfx4j-1.0.jar
#

#mv tools/lib/util/dom4j.jar.no tools/lib/util/dom4j.jar
ln -sf $(build-classpath dom4j) tools/lib/util/dom4j.jar

#mv tools/lib/util/sjsxp.jar.no tools/lib/util/sjsxp.jar
ln -sf $(build-classpath sjsxp) tools/lib/util/sjsxp.jar

#mv tools/lib/util/bnd-0.0.249.jar.no tools/lib/util/bnd-0.0.249.jar
ln -sf $(build-classpath aqute-bndlib) tools/lib/util/bnd-0.0.249.jar

#mv tools/lib/util/jing.jar.no tools/lib/util/jing.jar
ln -sf $(build-classpath jing) tools/lib/util/jing.jar

#mv tools/lib/rebundle/runtime2/txw2.jar.no tools/lib/rebundle/runtime2/txw2.jar
ln -sf $(build-classpath sun-txw2) tools/lib/rebundle/runtime2/txw2.jar

###
mv tools/lib/util/txwc2.jar.no tools/lib/util/txwc2.jar
#ln -sf $(build-classpath sun-txwc2) tools/lib/util/txwc2.jar

#mv tools/htmlmacro/htmlmacro.jar.no tools/htmlmacro/htmlmacro.jar
ln -sf $(build-classpath sun-htmlmacro) tools/htmlmacro/htmlmacro.jar

#mv tools/htmlmacro/commons-jelly-tags-util-1.1.1.jar.no tools/htmlmacro/commons-jelly-tags-util-1.1.1.jar
ln -sf $(build-classpath jelly-tags/commons-jelly-tags-util) tools/htmlmacro/commons-jelly-tags-util-1.1.1.jar

#mv tools/lib/rebundle/compiler/dtd-parser-1.0.jar.no tools/lib/rebundle/compiler/dtd-parser-1.0.jar
ln -sf $(build-classpath sun-dtdparser) tools/lib/rebundle/compiler/dtd-parser-1.0.jar

###
#mv tools/lib/rebundle/compiler/resolver.jar.no tools/lib/rebundle/compiler/resolver.jar
ln -sf $(build-classpath xml-commons-resolver12) tools/lib/rebundle/compiler/resolver.jar

#mv tools/lib/util/stax-ex.jar.no tools/lib/util/stax-ex.jar
ln -sf $(build-classpath stax-ex) tools/lib/util/stax-ex.jar

#mv tools/lib/util/args4j-1.0-RC.jar.no tools/lib/util/args4j-1.0-RC.jar
ln -sf $(build-classpath args4j10) tools/lib/util/args4j-1.0-RC.jar

#mv tools/lib/util/package-rename-task.jar.no tools/lib/util/package-rename-task.jar
ln -sf $(build-classpath javatools-package-rename-task) tools/lib/util/package-rename-task.jar

#mv tools/lib/rebundle/compiler/rngom.jar.no tools/lib/rebundle/compiler/rngom.jar
ln -sf $(build-classpath rngom) tools/lib/rebundle/compiler/rngom.jar

#mv tools/lib/rebundle/compiler/codemodel.jar.no tools/lib/rebundle/compiler/codemodel.jar
ln -sf $(build-classpath sun-codemodel) tools/lib/rebundle/compiler/codemodel.jar

#mv tools/lib/util/codemodel-annotation-compiler.jar.no tools/lib/util/codemodel-annotation-compiler.jar
ln -sf $(build-classpath sun-codemodel-annotation-compiler) tools/lib/util/codemodel-annotation-compiler.jar

#mv tools/lib/rebundle/compiler/istack-commons-tools.jar.no tools/lib/rebundle/compiler/istack-commons-tools.jar
ln -sf $(build-classpath sun-istack-commons/tools) tools/lib/rebundle/compiler/istack-commons-tools.jar

#mv tools/lib/rebundle/runtime2/istack-commons-runtime.jar.no tools/lib/rebundle/runtime2/istack-commons-runtime.jar
ln -sf $(build-classpath sun-istack-commons/runtime) tools/lib/rebundle/runtime2/istack-commons-runtime.jar

###
mv tools/lib/rebundle/compiler/xsom.jar.no tools/lib/rebundle/compiler/xsom.jar
#ln -sf $(build-classpath sun-xsom/xsom) tools/lib/rebundle/compiler/xsom.jar

#mv tools/lib/util/FastInfoset.jar.no tools/lib/util/FastInfoset.jar
ln -sf $(build-classpath sun-fi) tools/lib/util/FastInfoset.jar

#mv tools/lib/redist/jsr173_1.0_api.jar.no tools/lib/redist/jsr173_1.0_api.jar
ln -sf $(build-classpath stax_1_0_api) tools/lib/redist/jsr173_1.0_api.jar

#mv tools/lib/redist/jaxb-api.jar.no tools/lib/redist/jaxb-api.jar
ln -sf $(build-classpath jaxb_2_1_api) tools/lib/redist/jaxb-api.jar

#mv tools/lib/rebundle/runtime/relaxngDatatype.jar.no tools/lib/rebundle/runtime/relaxngDatatype.jar
ln -sf $(build-classpath relaxngDatatype) tools/lib/rebundle/runtime/relaxngDatatype.jar

#mv tools/lib/rebundle/compiler/relaxngDatatype.jar.no tools/lib/rebundle/compiler/relaxngDatatype.jar
ln -sf $(build-classpath relaxngDatatype) tools/lib/rebundle/compiler/relaxngDatatype.jar

#mv tools/lib/rebundle/runtime/isorelax.jar.no tools/lib/rebundle/runtime/isorelax.jar
ln -sf $(build-classpath isorelax) tools/lib/rebundle/runtime/isorelax.jar

#mv tools/lib/rebundle/runtime/msv.jar.no tools/lib/rebundle/runtime/msv.jar
ln -sf $(build-classpath msv-msv) tools/lib/rebundle/runtime/msv.jar

#mv tools/lib/rebundle/runtime/xsdlib.jar.no tools/lib/rebundle/runtime/xsdlib.jar
ln -sf $(build-classpath xsdlib) tools/lib/rebundle/runtime/xsdlib.jar

#mv tools/lib/redist/activation.jar.no tools/lib/redist/activation.jar
ln -sf $(build-classpath jaf_1_1_api) tools/lib/redist/activation.jar

#mv tools/lib/util/relaxngcc.jar.no tools/lib/util/relaxngcc.jar
ln -sf $(build-classpath relaxngcc) tools/lib/util/relaxngcc.jar

#mv tools/compiler10/jaxb1-xjc.jar.no tools/compiler10/jaxb1-xjc.jar
ln -sf $(build-classpath sun-jaxb-1.0/xjc.jar) tools/compiler10/jaxb1-xjc.jar


%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2

popd

%build
cd jaxb-ri
mkdir -p tools/installer/build/classes
export OPT_JAR_LIST="ant-launcher"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 dist javadoc

export CLASSPATH=$(build-classpath \
antlr \
javamail_1_4_api \
jsp_2_1_api \
servlet_2_5_api \
)
CLASSPATH=$CLASSPATH:$(pwd)/dist/lib/jaxb-xjc.jar
CLASSPATH=$CLASSPATH:$(pwd)/dist/lib/jaxb1-impl.jar

pushd tools

pushd jing-rnc-driver
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar
popd

pushd pretty-printer
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar
popd

pushd taglets
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar
popd

pushd webapp-commons
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar
popd

pushd xmllint
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar
popd

popd

%install
cd jaxb-ri

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/sun-jaxb-2.1-tools
install -m 644 dist/lib/jaxb-impl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 dist/lib/jaxb-xjc.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-xjc-%{version}.jar
%add_to_maven_depmap com.sun.xml.bind jaxb-impl %{version} JPP %{name}
%add_to_maven_depmap com.sun.xml.bind jaxb-xjc %{version} JPP %{name}-xjc

install -m 644 tools/jing-rnc-driver/build/jing-rnc-driver.jar $RPM_BUILD_ROOT%{_javadir}/sun-jaxb-2.1-tools/jing-rnc-driver-%{version}.jar
install -m 644 tools/pretty-printer/build/pretty-printer.jar $RPM_BUILD_ROOT%{_javadir}/sun-jaxb-2.1-tools/pretty-printer-%{version}.jar
install -m 644 tools/taglets/build/taglets.jar $RPM_BUILD_ROOT%{_javadir}/sun-jaxb-2.1-tools/taglets-%{version}.jar
install -m 644 tools/xmllint/build/xmllint.jar $RPM_BUILD_ROOT%{_javadir}/sun-jaxb-2.1-tools/xmllint-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/sun-jaxb-2.1-tools && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
touch $RPM_BUILD_ROOT%{_javadir}/jaxb_2_1_impl.jar
touch $RPM_BUILD_ROOT%{_javadir}/jaxb_impl.jar

# home
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
ln -s %{_javadir}/jaf_1_1_api.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/activation.jar
ln -s %{_javadir}/jaxb_2_1_api.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/jaxb-api.jar
ln -s %{_javadir}/stax_1_0_api.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/jsr173_1.0_api.jar
ln -s %{_javadir}/sun-jaxb-2.1-impl.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/jaxb-impl.jar
ln -s %{_javadir}/sun-jaxb-2.1-impl-xjc.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/jaxb-xjc.jar

# scripts
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 dist/bin/schemagen.sh $RPM_BUILD_ROOT%{_bindir}/sun-jaxb-schemagen
install -m 755 dist/bin/xjc.sh $RPM_BUILD_ROOT%{_bindir}/sun-jaxb-xjc

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-xjc.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#cp -pr dist/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 644 *.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

## samples
#install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
#cp -pr dist/samples $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxb_2_1_impl_sun-jaxb-2.1-impl<<EOF
%{_javadir}/jaxb_2_1_impl.jar	%{_javadir}/%{name}.jar	20100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxb_impl_sun-jaxb-2.1-impl<<EOF
%{_javadir}/jaxb_impl.jar	%{_javadir}/%{name}.jar	20100
EOF

%files
%_altdir/jaxb_impl_sun-jaxb-2.1-impl
%_altdir/jaxb_2_1_impl_sun-jaxb-2.1-impl
%{_docdir}/%{name}-%{version}/*.txt
%{_javadir}/%{name}*.jar
%{_javadir}/sun-jaxb-2.1-tools
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
%exclude %{_javadir}/jaxb_2_1_impl.jar
%exclude %{_javadir}/jaxb_impl.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.13-alt2_1jpp6
- use java6 build

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.13-alt1_1jpp6
- new jpp relase

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.1.6-alt4_1jpp5
- selected java5 compiler explicitly

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.6-alt3_1jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.6-alt2_1jpp5
- alternatives 0.4

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.6-alt1_1jpp5
- converted from JPackage by jppimport script

