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


Name:           sun-jaxb-1.0
Summary:        JAXB 1.0 API and Implementation
Url:            https://jaxb.dev.java.net/
Version:        1.0.6
Release:        alt3_2jpp5
Epoch:          0
License:        CDDL
Group:          Development/Java
BuildArch:      noarch
Source0:        jaxb-1.0.6.tar.gz
# cvs -d:pserver:guest@cvs.dev.java.net:/cvs export -r jaxb-1_0_6 -d jaxb-1.0.6 jaxb-sources

Source1:        sun-jaxb-1.0-api-build.xml
Source2:        xsom-20050414.tar.gz
# cvs -d:pserver:guest@cvs.dev.java.net:/cvs export -r scd -d xsom-20050415 jaxb2-sources/xsom

Source3:        jaxb-api-1.0.6.pom
Source4:        jaxb-impl-1.0.6.pom
Source5:        jaxb-libs-1.0.6.pom
Source6:        jaxb-xjc-1.0.6.pom


Patch0:         sun-jaxb-1.0-xjc-Options.patch
Patch1:         sun-jaxb-1.0-xjc-WhitespaceTransducer.patch
Patch2:         sun-jaxb-1.0-xjc-ConversionFinder.patch
Patch3:         sun-jaxb-1.0-xjc-ModelGroupBindingClassBinder.patch
Patch4:         sun-jaxb-1.0-xjc-DOMBinder.patch
Patch5:         sun-jaxb-1.0-xjc-DefaultClassBinder.patch
Patch6:         sun-jaxb-1.0-xjc-UnusedCustomizationChecker.patch
Patch7:         sun-jaxb-1.0-xjc-SimpleTypeBuilder.patch
Patch8:         sun-jaxb-1.0-xjc-FieldBuilder.patch
Patch9:         sun-jaxb-1.0-xjc-AGMFragmentBuilder.patch
Patch10:        sun-jaxb-1.0-xjc-TypeBuilder.patch
Patch11:        sun-jaxb-1.0-xjc-BIProperty.patch
Patch12:        sun-jaxb-1.0-build.patch
Patch13:        sun-jaxb-1.0-runtime-build.patch

BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-trax
BuildRequires: args4j10
BuildRequires: dom4j
BuildRequires: isorelax
BuildRequires: jing
BuildRequires: msv-msv
BuildRequires: msv-xsdlib
BuildRequires: nekohtml
BuildRequires: relaxngcc
BuildRequires: relaxngDatatype
BuildRequires: servlet_2_3_api
BuildRequires: xalan-j2
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: xml-commons-resolver11


%description
JAXB 1.0 API and Implementation

%package api
Summary:        JAXB 1.0 API from %{name}
Group:          Development/Java
Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4
Provides:       jaxb_api = 0:1.0
Provides:       jaxb_1_0_api = 0:%{version}-%{release}

%description api
%{summary}.

%package impl
Summary:        JAXB 1.0 RI from %{name}
Group:          Development/Java
Requires: %{name}-api = %{epoch}:%{version}-%{release}
Requires: dom4j
Requires: relaxngDatatype
Requires: xsdlib

%description impl
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
##%setup -q -n jaxb-ri-%{version}
%setup -q -n jaxb-%{version}
gzip -dc %{SOURCE2} | tar xf -
chmod -R go=u-w *
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
%patch6 -b .sav6
%patch7 -b .sav7
%patch8 -b .sav8
%patch9 -b .sav9
%patch10 -b .sav10
%patch11 -b .sav11
%patch12 -b .sav12
%patch13 -b .sav13


mkdir -p jaxb-api/src
pushd jaxb-api/src
unzip -qq ../../jaxb-ri/tools/lib/redist/jaxb-api-src.zip
popd
cp %{SOURCE1} jaxb-api/build.xml
mkdir -p jaxb-api/lib
ln -sf $(build-classpath dom4j) jaxb-api/lib

ln -sf $(build-classpath args4j10) jaxb-ri/tools/lib/args4j10.jar
ln -sf $(build-classpath isorelax) jaxb-ri/tools/lib/rebundle/isorelax.jar
ln -sf $(build-classpath msv-msv) jaxb-ri/tools/lib/rebundle/msv.jar
ln -sf $(build-classpath relaxngDatatype) jaxb-ri/tools/lib/redist/relaxngDatatype.jar
ln -sf $(build-classpath dom4j) jaxb-ri/tools/lib/util/dom4j.jar
ln -sf $(build-classpath servlet_2_3_api) jaxb-ri/tools/lib/util/servlet.jar
ln -sf $(build-classpath jing) jaxb-ri/tools/lib/util/jing.jar
ln -sf $(build-classpath nekohtml) jaxb-ri/tools/lib/util/nekohtml.jar
ln -sf $(build-classpath xsdlib) jaxb-ri/tools/lib/redist/xsdlib.jar
ln -sf $(build-classpath xml-commons-resolver11) jaxb-ri/tools/lib/rebundle/resolver.jar
#
ln -sf $(build-classpath relaxngcc) xsom-20050414/lib/relaxngcc.jar


%build

export CLASSPATH=
pushd jaxb-api
ant -Dbuild-classpath=first jar
popd
cp jaxb-api/jaxb-api.jar jaxb-ri/tools/lib/redist/jaxb-api.jar
export CLASSPATH=$(build-classpath relaxngDatatype)
pushd xsom-20050414
ant -Dbuild-classpath=first 
popd
cp xsom-20050414/build/xsom.jar jaxb-ri/tools/lib/rebundle/xsom.jar
pushd jaxb-ri/tools/lib/src/
  mkdir -p javadt/src
  pushd javadt
    pushd src
      unzip ../../relaxng.javadt.src.zip
    popd
    mkdir classes
    export CLASSPATH=$(build-classpath relaxngDatatype)
    $JAVA_HOME/bin/javac -d classes $(find src -name "*.java")
    $JAVA_HOME/bin/jar -cf relaxng-javadt.jar -C classes com
  popd
popd
cp jaxb-ri/tools/lib/src/javadt/relaxng-javadt.jar jaxb-ri/tools/lib/rebundle/relaxng.javadt.jar
export CLASSPATH=$(build-classpath xalan-j2-serializer relaxngcc)
pushd jaxb-ri
ant -Dxjc.docs=doc/api -Dbuild.sysclasspath=first dist javadoc
popd

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 jaxb-ri/dist/lib/jaxb-api.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-api-%{version}.jar
install -m 644 jaxb-ri/dist/lib/jaxb-impl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/impl-%{version}.jar
install -m 644 jaxb-ri/dist/lib/jaxb-libs.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/libs-%{version}.jar
install -m 644 jaxb-ri/dist/lib/jaxb-xjc.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xjc-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
touch $RPM_BUILD_ROOT%{_javadir}/jaxb_1_0_api.jar
touch $RPM_BUILD_ROOT%{_javadir}/jaxb_api.jar


install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-sun-jaxb-1.0-api.pom
%add_to_maven_depmap javax.xml.bind jaxb-api 1.0 JPP %{name}-api
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.sun-jaxb-1.0-impl.pom
%add_to_maven_depmap com.sun.xml jaxb-impl %{version} JPP/%{name} impl
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.sun-jaxb-1.0-libs.pom
%add_to_maven_depmap com.sun.xml jaxb-libs %{version} JPP/%{name} libs
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.sun-jaxb-1.0-xjc.pom
%add_to_maven_depmap com.sun.xml jaxb-xjc %{version} JPP/%{name} xjc

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/codemodel
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/impl
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xjc
cp -pr jaxb-ri/dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api
cp -pr jaxb-ri/docs/api/codemodel/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/codemodel
cp -pr jaxb-ri/runtime/doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/impl
cp -pr jaxb-ri/xjc/doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/impl
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxb_1_0_api_%{name}-api<<EOF
%{_javadir}/jaxb_1_0_api.jar	%{_javadir}/%{name}-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxb_api_%{name}-api<<EOF
%{_javadir}/jaxb_api.jar	%{_javadir}/%{name}-api.jar	10000
EOF

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files api
%_altdir/jaxb_api_%{name}-api
%_altdir/jaxb_1_0_api_%{name}-api
%{_javadir}/%{name}*.jar
%exclude %{_javadir}/jaxb_api.jar
%exclude %{_javadir}/jaxb_1_0_api.jar
%{_datadir}/maven2
%{_mavendepmapfragdir}

%files impl
%{_javadir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt3_2jpp5
- fixes for java6 support

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt2_2jpp5
- alternatives 0.4

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_2jpp5
- converted from JPackage by jppimport script

