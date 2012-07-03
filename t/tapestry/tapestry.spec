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
%define java2 %{?_with_java2:1}%{!?_with_java2:%{?_without_java2:0}%{!?_without_java2:%{?_java2:%{_java2}}%{!?_java2:0}}}


Name:           tapestry
Version:        4.0.2
Release:        alt4_3jpp5
Epoch:          0
Summary:        Tapestry Framework
License:        ASL 2.0
Group:          Development/Java
URL:            http://tapestry.apache.org/
Source0:        tapestry-4.0.2.tar.gz
Source1:        hivemind-1.1.1.tar.gz
Patch0:         tapestry-hivemind-hivebuild-module.patch
Patch1:         tapestry-hivemind-hivebuild-module-properties.patch
Patch2:         tapestry-hivemind-hivebuild-properties.patch
Patch3:         tapestry-framework-build.patch
Patch4:         tapestry-portlet-build.patch
Patch5:         tapestry-contrib-build.patch
Patch6:         tapestry-annotations-build.patch
Patch7:         tapestry-examples-Workbench-build.patch
Patch8:         tapestry-examples-VlibBeans-build.patch
Patch9:         tapestry-examples-Vlib-build.patch
Patch10:        tapestry-PersistentPropertyDataEncoderTest.patch
Patch11:        tapestry-TestDataSqueezer.patch
Patch12:        tapestry-TestPortletRenderer.patch
Patch13:        tapestry-framework-build-java2.patch
Patch14:        tapestry-hivemind-hivebuild-module-java2.patch
Patch15:        tapestry-build-java2.patch

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif

%if ! %{java2}
%else
%endif
Requires: geronimo-ejb-2.1-api
Requires: hivemind = 0:1.1.1
Requires: hivemind-lib = 0:1.1.1
Requires: jakarta-commons-codec
Requires: jakarta-commons-fileupload
Requires: jakarta-commons-io
Requires: jakarta-commons-logging
Requires: jakarta-oro
Requires: javassist
Requires: ognl
Requires: portlet-1.0-api
Requires: servletapi4
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: ant-nodeps
BuildRequires: jpackage-utils >= 0:1.7
BuildRequires: cglib
BuildRequires: easymock
BuildRequires: easymock-classextension
BuildRequires: geronimo-ejb-2.1-api
BuildRequires: hivemind = 0:1.1.1
BuildRequires: hivemind-lib = 0:1.1.1
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-fileupload
BuildRequires: jakarta-commons-io
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-oro
BuildRequires: javassist
BuildRequires: jcharts
BuildRequires: jdom
BuildRequires: junit
BuildRequires: log4j
BuildRequires: ognl
BuildRequires: portlet-1.0-api
BuildRequires: servletapi4
BuildRequires: spring-all

%description
Tapestry is an open-source framework for creating dynamic, 
robust, highly scalable web applications in Java. Tapestry 
complements and builds upon the standard Java Servlet API, 
and so it works in any servlet container or application 
server. Tapestry divides a web application into a set of 
pages, each constructed from components. This provides a 
consistent structure, allowing the Tapestry framework to 
assume responsibility for key concerns such as URL 
construction and dispatch, persistent state storage on the 
client or on the server, user input validation, 
localization/internationalization, and exception reporting. 
Developing Tapestry applications involves creating HTML 
templates using plain HTML, and combining the templates 
with small amounts of Java code using (optional) XML 
descriptor files. In Tapestry, you create your application 
in terms of objects, and the methods and properties of those 
objects -- and specifically not in terms of URLs and query 
parameters. Tapestry brings true object oriented development 
to Java web applications. Tapestry is specifically designed 
to make creating new components very easy, as this is a 
routine approach when building applications. The distribution 
includes over fifty components, ranging from simple output 
components all the way up to complex data grids and tree 
navigators. Tapestry is architected to scale from tiny 
applications all the way up to massive applications consisting 
of hundreds of individual pages, developed by large, diverse 
teams. Tapestry easily integrates with any kind of backend, 
including J2EE, HiveMind and Spring.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if ! %{java2}
%package demo
Summary:        Examples for %{name}
Group:          Development/Documentation
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jcharts

%description demo
%{summary}.
%endif


%prep
%setup -q -n %{name}-%{version}
%setup -q -T -D -a 1 -c -n %{name}-%{version}

for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
%patch4 -b .sav
%patch5 -b .sav
%patch6 -b .sav
%patch7 -b .sav
%patch8 -b .sav
%patch9 -b .sav
%patch10 -b .sav
%patch11 -b .sav
%patch12 -b .sav
%if %{java2}
%patch13 -b .sav2

rm framework/src/test/org/apache/tapestry/coerce/StringToPropertySelectionModelConverterTest.java
rm framework/src/test/org/apache/tapestry/form/FormFixture.java
rm framework/src/test/org/apache/tapestry/link/DefaultLinkRendererTest.java

rm framework/src/test/org/apache/tapestry/event/ReportStatusEventTest.java
rm framework/src/test/org/apache/tapestry/form/AbstractFormComponentTest.java
rm framework/src/test/org/apache/tapestry/form/FormTest.java
rm framework/src/test/org/apache/tapestry/valid/FieldLabelTest.java

%patch14 -b .sav2

#rm -rf annotations
%patch15 -b .sav2
#rm -rf examples/Workbench
%endif
 
mkdir -p repository/JPP/jars
pushd repository/JPP/jars
ln -sf $(build-classpath commons-codec) commons-codec-.jar
ln -sf $(build-classpath commons-fileupload) commons-fileupload-.jar
ln -sf $(build-classpath commons-io) commons-io-.jar
ln -sf $(build-classpath commons-logging) commons-logging-.jar
ln -sf $(build-classpath hivemind) hivemind-.jar
ln -sf $(build-classpath hivemind-lib) hivemind-lib-.jar
ln -sf $(build-classpath oro) oro-.jar
ln -sf $(build-classpath javassist) javassist-.jar
ln -sf $(build-classpath servletapi4) servletapi-.jar
ln -sf $(build-classpath ognl) ognl-.jar
ln -sf $(build-classpath log4j) log4j-.jar
ln -sf $(build-classpath easymock) easymock-.jar
ln -sf $(build-classpath easymock-classextension) easymockclassextension-.jar
ln -sf $(build-classpath cglib-nodep) cglib-full-.jar
ln -sf $(build-classpath junit) junit-.jar
ln -sf $(build-classpath jdom) jdom-.jar
ln -sf $(build-classpath spring) spring-.jar
ln -sf $(build-classpath portlet-1.0-api) portlet-api-.jar
ln -sf $(build-classpath geronimo-ejb-2.1-api) geronimo-ejb-2.1-api-.jar
ln -sf $(build-classpath jcharts) jcharts-.jar
popd

rm ./framework/src/test/org/apache/tapestry/util/io/TestBinaryDumpOutputStream.java

sed -i -e s,JPEGEncoder13,JPEGEncoder,g `grep -rl org.jCharts.encoders.JPEGEncoder13 .`

%build
export CLASSPATH=
export OPT_JAR_LIST="`%{__cat} %{_sysconfdir}/ant.d/{junit,nodeps}`"
mkdir tmp
mkdir -p ext-package/lib
touch ext-package/download-warning-marker
%if ! %{java2}
%else
export JAVA_HOME=%{_jvmdir}/java-1.4.2
%endif
export RD=$(pwd)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dhivebuild.dir=${RD}/hivemind-1.1.1/hivebuild -Dscratch.dir=${RD}/tmp -Droot.dir=${RD} -Dhivebuild.skip-tests=true install run-reports
for d in framework contrib portlet; do
pushd $d
ant -Dhivebuild.dir=${RD}/hivemind-1.1.1/hivebuild -Dscratch.dir=${RD}/tmp -Droot.dir=${RD} javadoc
popd
done
%if ! %{java2}
pushd annotations
ant -Dhivebuild.dir=${RD}/hivemind-1.1.1/hivebuild -Dscratch.dir=${RD}/tmp -Droot.dir=${RD} javadoc
popd
%endif

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

install -m 644 target/%{name}-%{version}.jar \
                  $RPM_BUILD_ROOT%{_javadir}/%{name}/
%if ! %{java2}
install -m 644 target/%{name}-annotations-%{version}.jar \
                  $RPM_BUILD_ROOT%{_javadir}/%{name}/
%endif
install -m 644 target/%{name}-contrib-%{version}.jar \
                  $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -m 644 target/%{name}-portlet-%{version}.jar \
                  $RPM_BUILD_ROOT%{_javadir}/%{name}/
%if ! %{java2}
install -m 644 target/vlib/vlibbeans-%{version}.jar \
                  $RPM_BUILD_ROOT%{_javadir}/%{name}/
%endif
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

%if ! %{java2}
# apps
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -pm 644 target/workbench.war \
                  $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -pm 644 target/vlib/vlib.war \
                  $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -pm 644 target/vlib/vlib.ear \
                  $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
%endif

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/framework
cp -pr tmp/jakarta-tapestry/target/docs/tapestry/apidocs/* \
                  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/framework
%if ! %{java2}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/annotations
cp -pr tmp/jakarta-tapestry/target/docs/tapestry-annotations/apidocs/* \
                  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/annotations
%endif
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/contrib
cp -pr tmp/jakarta-tapestry/target/docs/tapestry-contrib/apidocs/* \
                  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/contrib
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/portlet
cp -pr tmp/jakarta-tapestry/target/docs/tapestry-portlet/apidocs/* \
                  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/portlet
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if ! %{java2}
# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/examples
cp -pr examples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/examples
%endif

# config
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/config
cp -pr config/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/config


%if %{gcj_support}
%{_bindir}/aot-compile-rpm \
    --exclude /usr/share/java/tapestry/tapestry-contrib-%{version}.jar \
%if ! %{java2}
    --exclude /usr/share/java/tapestry/vlibbeans-%{version}.jar \
    --exclude /usr/share/java/tapestry/tapestry-annotations-%{version}.jar \
    --exclude /usr/share/tapestry-%{version}/vlib.war \
    --exclude /usr/share/tapestry-%{version}/workbench.war \
    --exclude /usr/share/tapestry-%{version}/vlib.ear
%endif

%endif

%files
%{_javadir}/%{name}
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/config
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}*-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if ! %{java2}
%files demo
%{_datadir}/%{name}-%{version}/*.?ar
%{_datadir}/%{name}-%{version}/examples
%endif

%changelog
* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.0.2-alt4_3jpp5
- fixed build

* Sun Jan 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.0.2-alt3_3jpp5
- fixed build

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.0.2-alt2_3jpp5
- fixes for java6 support

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.0.2-alt1_3jpp5
- use default jpp profile

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.0.2-alt1_1jpp5.0
- converted from JPackage by jppimport script

