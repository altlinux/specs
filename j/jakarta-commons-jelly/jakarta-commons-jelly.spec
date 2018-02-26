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

# If you want to build tags-jaxme, 
# give rpmbuild option '--with jaxme'

%define without_jaxme %{!?_with_jaxme:1}%{?_with_jaxme:0}
%define with_jaxme %{?_with_jaxme:1}%{!?_with_jaxme:0}


%define base_name commons-jelly
%define jakarta_version 1.0

Name:           jakarta-%{base_name}
Version:        %{jakarta_version}
Release:        alt10_7jpp6
Epoch:          0
Summary:        Jelly Scripting Engine
Group:          Development/Java
License:        Apache Software License
URL:            http://jakarta.apache.org/commons/jelly/
Source0:        commons-jelly-1.0-src.tar.gz
Source1:        jelly-tags-231113.tar.gz
# Exported revision 231113.
# svn export http://svn.apache.org/repos/asf/jakarta/commons/proper/jelly/tags/commons-jelly-1.0/jelly-tags
Source2:        commons-jelly-tags-xml-1.1.tar.gz
Source3:        commons-jelly-tags-jmx-build.xml
Patch0:         commons-jelly-tags-xml-build_xml.patch
Patch1:         commons-jelly-tags-jsl-suite_jelly.patch
Patch2:         commons-jelly-tags-jsl-example_jelly.patch
Patch3:         commons-jelly-tags-jetty-HttpContextTag.patch
Patch4:         commons-jelly-tags-jetty-JettyHttpServerTag.patch
Patch5:         commons-jelly-tags-jetty-SecurityHandlerTag.patch
Patch6:         commons-jelly-tags-jetty-build_xml.patch
Patch7:         commons-jelly-tags-sql-DataSourceWrapper.patch
Patch8:         commons-jelly-tags-xmlunit-AssertDocumentsEqualTag.patch
# Jelly build and test BuildRequires
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant17 >= 0:1.7.1
BuildRequires:  ant17-junit
BuildRequires:  junit
BuildRequires:  xmlunit
# Jelly general BuildRequires
BuildRequires:  dom4j >= 0:1.6.1
BuildRequires:  apache-commons-jexl >= 0:1.0
BuildRequires:  jakarta-commons-beanutils16
BuildRequires:  apache-commons-cli
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-discovery
BuildRequires:  apache-commons-lang
BuildRequires:  apache-commons-logging
BuildRequires:  jakarta-taglibs-standard
BuildRequires:  jaxen >= 0:1.1-0.b7
BuildRequires:  forehead
BuildRequires:  servlet_2_4_api
#BuildRequires:  xerces-j2
# Jelly taglibs individual BuildRequires
## for tags-ant, tags-fmt and tags-jsl
BuildRequires:  jakarta-commons-grant
## for tags-antlr
BuildRequires:  antlr
## for tags-avalon
BuildRequires:  excalibur-avalon-framework-api
## for tags-beanshell and tags-fmt
BuildRequires:  bsh
## for tags-beanshell
BuildRequires:  libreadline-java
## for tags-betwixt
BuildRequires:  apache-commons-betwixt
BuildRequires:  apache-commons-digester
## for tags-bsf
BuildRequires:  bsf
## for tags-email
BuildRequires:  jaf_1_0_2_api
BuildRequires:  javamail_1_3_1_api
## for tags-html
BuildRequires:  nekohtml
## for tags-http, tags-jetty and tags-soap
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-httpclient
## for tags-interaction
BuildRequires:  jline
%if %{with_jaxme}
## for tags-jaxme
BuildRequires:  ws-jaxme
%endif
## for tags-jetty
BuildRequires:  jetty5
BuildRequires:  servlet_2_4_api
## for tags-jms
BuildRequires:  jakarta-commons-messenger
BuildRequires:  jms_1_1_api
## for tags-jmx
BuildRequires:  mx4j
## for tags-junit
#BuildRequires: junit # already required as general test tool
## for tags-ojb
BuildRequires:  db-ojb
## for tags-quartz
BuildRequires:  log4j
BuildRequires:  quartz
## for tags-soap
BuildRequires:  axis
## for tags-sql
BuildRequires:  hsqldb
## for tags-validate
BuildRequires:  isorelax
BuildRequires:  msv-msv
BuildRequires:  relaxngDatatype
## for tags-velocity
BuildRequires:  velocity14
%if %{with_jaxme}
## for tags-xmlunit and unit tests of tags-jaxme
BuildRequires:  xmlunit
%endif
# Jelly general runtime requirements
Requires:  dom4j >= 0:1.6.1
Requires:  apache-commons-jexl >= 0:1.0
Requires:  jakarta-commons-beanutils16
Requires:  apache-commons-cli
Requires:  apache-commons-collections
Requires:  apache-commons-discovery
Requires:  apache-commons-lang
Requires:  apache-commons-logging
Requires:  jakarta-taglibs-standard
Requires:  jaxen >= 0:1.1-0.b7
Requires:  forehead
Requires:  servlet_2_4_api
%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info
Patch33: commons-jelly-1.0-alt-velocity-fix-incorrect-logsystem.patch

%description
Jelly is a Java and XML based scripting engine. 
Jelly combines the best ideas from JSTL, Velocity, 
DVSL, Ant and Cocoon all together in a simple
yet powerful scripting engine.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}. Includes javadocs for all jelly-tags

%package tags-ant
Summary:        Ant tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-util = %{epoch}:%{version}-%{release}
Requires:       jakarta-commons-grant

%description    tags-ant
%{summary}.

%package tags-antlr
Summary:        Antlr tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       antlr

%description    tags-antlr
%{summary}.

%package tags-avalon
Summary:        Avalon tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       excalibur-avalon-framework-api

%description    tags-avalon
%{summary}.

%package tags-bean
Summary:        Bean tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-log = %{epoch}:%{version}-%{release}

%description    tags-bean
%{summary}.

%package tags-beanshell
Summary:        BSH tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       bsh
Requires:       libreadline-java

%description    tags-beanshell
%{summary}.

%package tags-betwixt
Summary:        Betwixt tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-log = %{epoch}:%{version}-%{release}
Requires:       apache-commons-betwixt
Requires:       apache-commons-digester

%description    tags-betwixt
%{summary}.

%package tags-bsf
Summary:        BSF tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       bsf

%description    tags-bsf
%{summary}.

%package tags-define
Summary:        Define tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-dynabean = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-log = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-xml = %{epoch}:%{version}-%{release}

%description    tags-define
%{summary}.

%package tags-dynabean
Summary:        Dynabean tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    tags-dynabean
%{summary}.

%package tags-email
Summary:        Email tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jaf_1_0_2_api
Requires:       javamail_1_3_1_api

%description    tags-email
%{summary}.

%package tags-fmt
Summary:        Formatting tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-ant = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-beanshell = %{epoch}:%{version}-%{release}
Requires:       bsh
Requires:       jakarta-commons-grant

%description    tags-fmt
%{summary}.

%package tags-html
Summary:        HTML tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-jsl = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-log = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-xml = %{epoch}:%{version}-%{release}
Requires:       nekohtml

%description    tags-html
%{summary}.

%package tags-http
Summary:        HTTP tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-define = %{epoch}:%{version}-%{release}
Requires:       apache-commons-codec
Requires:       apache-commons-httpclient

%description    tags-http
%{summary}.

%package tags-interaction
Summary:        Interaction tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    tags-interaction
%{summary}.

%if %{with_jaxme}
%package tags-jaxme
Summary:        JaxME tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       ws-jaxme

%description    tags-jaxme
%{summary}.
%endif

%package tags-jetty
Summary:        Jetty tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-http = %{epoch}:%{version}-%{release}
Requires:       jakarta-commons-codec
Requires:       jakarta-commons-httpclient
Requires:       jetty5
Requires:       servlet_2_4_api

%description    tags-jetty
%{summary}.

%package tags-jms
Summary:        JMS tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jakarta-commons-messenger
Requires:       jms_1_1_api

%description    tags-jms
%{summary}.

%package tags-jmx
Summary:        JMX tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-bean = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-log = %{epoch}:%{version}-%{release}
Requires:       mx4j

%description    tags-jmx
%{summary}.

%package tags-jsl
Summary:        JSL tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-ant = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-log = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-xml = %{epoch}:%{version}-%{release}
Requires:       jakarta-commons-grant

%description    tags-jsl
%{summary}.

%package tags-junit
Summary:        JUnit tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       junit

%description    tags-junit
%{summary}.

%package tags-log
Summary:        Logging tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    tags-log
%{summary}.

%package tags-ojb
Summary:        OJB tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       db-ojb

%description    tags-ojb
%{summary}.

%package tags-quartz
Summary:        Quartz tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       log4j
Requires:       quartz

%description    tags-quartz
%{summary}.

%package tags-soap
Summary:        Soap tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       axis
Requires:       apache-commons-codec
Requires:       apache-commons-httpclient

%description    tags-soap
%{summary}.

%package tags-sql
Summary:        SQL tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       hsqldb

%description    tags-sql
%{summary}.

%package tags-swing
Summary:        Swing tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    tags-swing
%{summary}.

%package tags-threads
Summary:        Threads tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    tags-threads
%{summary}.

%package tags-util
Summary:        Utility tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    tags-util
%{summary}.

%package tags-validate
Summary:        XML Schema validation tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       isorelax
Requires:       msv-msv
Requires:       msv-xsdlib
Requires:       relaxngDatatype

%description    tags-validate
%{summary}.

%package tags-velocity
Summary:        Velocity tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       velocity14

%description    tags-velocity
%{summary}.

%package tags-xml
Summary:        Xml tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    tags-xml
%{summary}.

%package tags-xmlunit
Summary:        Xmlunit tags for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-tags-xml = %{epoch}:%{version}-%{release}
Requires:       xmlunit

%description    tags-xmlunit
%{summary}.


%prep
%setup -q -n %{base_name}-%{version}-src
# optionally inhibit tests to save time
#for b in `find . -name build.xml`; do
#    sed -e 's/ depends="compile,test"/ depends="compile"/' $b > tempf
#    cp tempf $b
#done
gzip -dc %{SOURCE1} | tar xf -
# won't run in headless environments
rm -f jelly-tags/swing/src/test/org/apache/commons/jelly/swing/TestSwingTags.java
# maven generated build.xml missing in cvs
cp %{SOURCE3} jelly-tags/jmx/build.xml
(cd jelly-tags/xml
rm -rf *
gzip -dc %{SOURCE2} | tar xf -
)
cat >> build.properties << EOBP
servletapi.jar=file:$(build-classpath servlet_2_4_api)
commons-cli.jar=file:$(build-classpath commons-cli)
commons-lang.jar=file:$(build-classpath commons-lang)
commons-discovery.jar=file:$(build-classpath commons-discovery)
forehead.jar=file:$(build-classpath forehead)
jstl.jar=file:$(build-classpath taglibs-standard)
junit.jar=file:$(build-classpath junit)
commons-jexl.jar=file:$(build-classpath commons-jexl)
#xml-apis.jar=file:$(build-classpath xml-commons-apis)
commons-beanutils.jar=file:$(build-classpath commons-beanutils16)
commons-collections.jar=file:$(build-classpath commons-collections)
commons-logging.jar=file:$(build-classpath commons-logging)
dom4j.jar=file:$(build-classpath dom4j)
jaxen.jar=file:$(build-classpath jaxen)
#xerces.jar=file:$(build-classpath xerces-j2)
EOBP

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2

%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5

%patch6 -b .sav6
%patch7 -b .sav7
%patch8 -b .sav8
%patch33 -p0

%build
export OPT_JAR_LIST="ant17/ant17-junit junit"
export CLASSPATH=$(build-classpath taglibs-core)
ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first dist
pushd jelly-tags
  pushd junit
cat >> build.properties << EOBP
commons-cli.jar=file:$(build-classpath commons-cli)
junit.jar=file:$(build-classpath junit)
commons-jexl.jar=file:$(build-classpath commons-jexl)
#xml-apis.jar=file:$(build-classpath xml-commons-apis)
commons-beanutils.jar=file:$(build-classpath commons-beanutils16)
commons-collections.jar=file:$(build-classpath commons-collections)
commons-logging.jar=file:$(build-classpath commons-logging)
dom4j.jar=file:$(build-classpath dom4j)
jaxen.jar=file:$(build-classpath jaxen)
#xerces.jar=file:$(build-classpath xerces-j2)
commons-jelly.jar=file:$(pwd)/../../target/commons-jelly-1.0.jar
EOBP
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 dist
  popd
  pushd util
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-jexl commons-lang commons-logging dom4j jaxen)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd log
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-collections commons-beanutils16 commons-jexl commons-logging dom4j jaxen)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd xml
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-jexl commons-logging dom4j jaxen)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd ant
cat >> build.properties << EOBP
ant.jar=file:$(build-classpath ant17)
ant-launcher.jar=file:$(build-classpath ant17-launcher)
ant-junit.jar=file:$(build-classpath ant17/ant17-junit)
commons-jelly-tags-junit.jar=file:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
commons-jelly-tags-util.jar=file:$(pwd)/../util/target/commons-jelly-tags-util-1.0-SNAPSHOT.jar
commons-cli.jar=file:$(build-classpath commons-cli)
#xml-apis.jar=file:$(build-classpath xml-commons-apis)
commons-beanutils.jar=file:$(build-classpath commons-beanutils16)
commons-collections.jar=file:$(build-classpath commons-collections)
commons-jexl.jar=file:$(build-classpath commons-jexl)
commons-jelly.jar=file:$(pwd)/../../target/commons-jelly-1.0.jar
commons-logging.jar=file:$(build-classpath commons-logging)
dom4j.jar=file:$(build-classpath dom4j)
jaxen.jar=file:$(build-classpath jaxen)
#xerces.jar=file:$(build-classpath xerces-j2)
EOBP
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../util/target/commons-jelly-tags-util-1.0-SNAPSHOT.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-jexl commons-logging dom4j jaxen )
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd antlr
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath antlr)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd avalon
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath excalibur/avalon-framework-api dom4j jaxen)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd bean
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../log/target/commons-jelly-tags-log-1.0-SNAPSHOT.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-jexl commons-logging dom4j jaxen)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd beanshell
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-jexl commons-logging bsh dom4j jaxen)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd betwixt
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../log/target/commons-jelly-tags-log-1.0-SNAPSHOT.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-betwixt commons-collections commons-digester commons-jexl commons-logging dom4j jaxen)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd bsf
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-logging bsf)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd dynabean
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-jexl commons-logging dom4j jaxen)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd define
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../log/target/commons-jelly-tags-log-1.0-SNAPSHOT.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../xml/target/commons-jelly-tags-xml-1.0-SNAPSHOT.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../dynabean/target/commons-jelly-tags-dynabean-1.0-SNAPSHOT.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-jexl commons-logging dom4j jaxen)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd email
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-logging jaf javamail)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd fmt
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../ant/target/commons-jelly-tags-ant-1.1-SNAPSHOT.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-jexl commons-logging dom4j jaxen)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd jsl
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../xml/target/commons-jelly-tags-xml-1.0-SNAPSHOT.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../log/target/commons-jelly-tags-log-1.0-SNAPSHOT.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../ant/target/commons-jelly-tags-ant-1.1-SNAPSHOT.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-jexl commons-logging dom4j jaxen)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd html
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../xml/target/commons-jelly-tags-xml-1.0-SNAPSHOT.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-jexl commons-logging dom4j jaxen nekohtml)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd http
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-codec commons-httpclient)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd interaction
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-logging jline)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd jetty
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../http/target/commons-jelly-tags-http-1.0-SNAPSHOT.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-codec commons-httpclient commons-jexl commons-logging jetty5 dom4j jaxen servlet_2_4_api)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd jms
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-logging commons-messenger jms)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd jmx
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../bean/target/commons-jelly-tags-bean-1.0-SNAPSHOT.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-logging mx4j/mx4j-jmx dom4j jaxen)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd ojb
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-lang db-ojb/db-ojb)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd quartz
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath quartz)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd soap
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath axis/axis axis/jaxrpc commons-codec commons-httpclient)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd sql
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-jexl commons-logging dom4j jaxen)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd swing
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-jexl commons-lang commons-logging dom4j jaxen)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd threads
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-jexl commons-logging dom4j jaxen)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd validate
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-jexl commons-logging dom4j jaxen isorelax msv-msv msv-xsdlib relaxngDatatype)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd velocity
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-collections velocity)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
  pushd xmlunit
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../xml/target/commons-jelly-tags-xml-1.0-SNAPSHOT.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-jexl commons-logging xmlunit dom4j jaxen)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
%if %{with_jaxme}
  pushd jaxme
rm -rf src/test/*
    export CLASSPATH=$(pwd)/../../target/commons-jelly-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../junit/target/commons-jelly-tags-junit-1.0.jar
    CLASSPATH=$CLASSPATH:$(pwd)/../xmlunit/target/commons-jelly-tags-xmlunit-1.0-SNAPSHOT.jar
    CLASSPATH=$CLASSPATH:$(build-classpath commons-beanutils16 commons-collections commons-jexl commons-logging jaxme/jaxme2 jaxme/jaxmeapi jaxme/jaxmejs jaxme/jaxmexs dom4j jaxen xmlunit)
    CLASSPATH=$CLASSPATH:target/classes:target/test-classes
    ant17  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist
  popd
%endif
popd

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/jelly-tags
install -pm 644 target/%{base_name}-%{jakarta_version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

install -pm 644 jelly-tags/ant/target/commons-jelly-tags-ant-1.1-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-ant-%{version}.jar
install -pm 644 jelly-tags/antlr/target/commons-jelly-tags-antlr-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-antlr-%{version}.jar
install -pm 644 jelly-tags/avalon/target/commons-jelly-tags-avalon-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-avalon-%{version}.jar
install -pm 644 jelly-tags/bean/target/commons-jelly-tags-bean-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-bean-%{version}.jar
install -pm 644 jelly-tags/beanshell/target/commons-jelly-tags-beanshell-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-beanshell-%{version}.jar
install -pm 644 jelly-tags/betwixt/target/commons-jelly-tags-betwixt-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-betwixt-%{version}.jar
install -pm 644 jelly-tags/bsf/target/commons-jelly-tags-bsf-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-bsf-%{version}.jar
install -pm 644 jelly-tags/define/target/commons-jelly-tags-define-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-define-%{version}.jar
install -pm 644 jelly-tags/dynabean/target/commons-jelly-tags-dynabean-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-dynabean-%{version}.jar
install -pm 644 jelly-tags/email/target/commons-jelly-tags-email-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-email-%{version}.jar
install -pm 644 jelly-tags/fmt/target/commons-jelly-tags-fmt-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-fmt-%{version}.jar
install -pm 644 jelly-tags/html/target/commons-jelly-tags-html-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-html-%{version}.jar
install -pm 644 jelly-tags/http/target/commons-jelly-tags-http-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-http-%{version}.jar
install -pm 644 jelly-tags/interaction/target/commons-jelly-tags-interaction-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-interaction-%{version}.jar
%if %{with_jaxme}
install -pm 644 jelly-tags/jaxme/target/commons-jelly-tags-jaxme-0.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-jaxme-%{version}.jar
%endif
install -pm 644 jelly-tags/jetty/target/commons-jelly-tags-jetty-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-jetty-%{version}.jar
install -pm 644 jelly-tags/jms/target/commons-jelly-tags-jms-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-jms-%{version}.jar
install -pm 644 jelly-tags/jmx/target/commons-jelly-tags-jmx-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-jmx-%{version}.jar
install -pm 644 jelly-tags/jsl/target/commons-jelly-tags-jsl-1.1-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-jsl-%{version}.jar
install -pm 644 jelly-tags/junit/target/commons-jelly-tags-junit-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-junit-%{version}.jar
install -pm 644 jelly-tags/log/target/commons-jelly-tags-log-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-log-%{version}.jar
install -pm 644 jelly-tags/ojb/target/commons-jelly-tags-ojb-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-ojb-%{version}.jar
install -pm 644 jelly-tags/quartz/target/commons-jelly-tags-quartz-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-quartz-%{version}.jar
install -pm 644 jelly-tags/soap/target/commons-jelly-tags-soap-1.1-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-soap-%{version}.jar
install -pm 644 jelly-tags/sql/target/commons-jelly-tags-sql-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-sql-%{version}.jar
install -pm 644 jelly-tags/swing/target/commons-jelly-tags-swing-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-swing-%{version}.jar
install -pm 644 jelly-tags/threads/target/commons-jelly-tags-threads-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-threads-%{version}.jar
install -pm 644 jelly-tags/util/target/commons-jelly-tags-util-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-util-%{version}.jar
install -pm 644 jelly-tags/validate/target/commons-jelly-tags-validate-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-validate-%{version}.jar
install -pm 644 jelly-tags/velocity/target/commons-jelly-tags-velocity-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-velocity-%{version}.jar
install -pm 644 jelly-tags/xml/target/commons-jelly-tags-xml-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-xml-%{version}.jar
install -pm 644 jelly-tags/xmlunit/target/commons-jelly-tags-xmlunit-1.0-SNAPSHOT.jar \
      $RPM_BUILD_ROOT%{_javadir}/jelly-tags/%{name}-tags-xmlunit-%{version}.jar

%if %{with_jaxme}
export taglibs="ant antlr avalon bean beanshell betwixt bsf define dynabean email fmt html http interaction jaxme jetty jms jmx jsl junit log ojb quartz soap sql swing threads util validate velocity xml xmlunit"
%else
export taglibs="ant antlr avalon bean beanshell betwixt bsf define dynabean email fmt html http interaction jetty jms jmx jsl junit log ojb quartz soap sql swing threads util validate velocity xml xmlunit"
%endif

(
cd $RPM_BUILD_ROOT%{_javadir} 
for tag in ${taglibs}; do
  ln -sf jelly-tags/%{name}-tags-${tag}-%{version}.jar %{name}-tags-${tag}.jar
done
for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done
for jar in jakarta-*.jar; do ln -sf ${jar} `echo $jar| sed "s|jakarta-||g"`; done
cd jelly-tags
for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done
for jar in jakarta-*.jar; do ln -sf ${jar} `echo $jar| sed "s|jakarta-||g"`; done
)

#javadoc dirs
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jelly-tags
for tag in ${taglibs}; do
  install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jelly-tags/${tag}
done

#javadoc files
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
for tag in ${taglibs}; do
  cp -pr jelly-tags/${tag}/dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jelly-tags/${tag}
done

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt
%{_javadir}/jakarta-commons-jelly-1.0.jar
%{_javadir}/jakarta-commons-jelly.jar
%{_javadir}/commons-jelly-1.0.jar
%{_javadir}/commons-jelly.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files    tags-ant
%{_javadir}/jakarta-commons-jelly-tags-ant.jar
%{_javadir}/commons-jelly-tags-ant.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-ant-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-ant.jar
%{_javadir}/jelly-tags/commons-jelly-tags-ant-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-ant.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-ant-%{version}.jar.*
%endif

%files    tags-antlr
%{_javadir}/jakarta-commons-jelly-tags-antlr.jar
%{_javadir}/commons-jelly-tags-antlr.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-antlr-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-antlr.jar
%{_javadir}/jelly-tags/commons-jelly-tags-antlr-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-antlr.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-antlr-%{version}.jar.*
%endif

%files    tags-avalon
%{_javadir}/jakarta-commons-jelly-tags-avalon.jar
%{_javadir}/commons-jelly-tags-avalon.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-avalon-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-avalon.jar
%{_javadir}/jelly-tags/commons-jelly-tags-avalon-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-avalon.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-avalon-%{version}.jar.*
%endif

%files    tags-bean
%{_javadir}/jakarta-commons-jelly-tags-bean.jar
%{_javadir}/commons-jelly-tags-bean.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-bean-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-bean.jar
%{_javadir}/jelly-tags/commons-jelly-tags-bean-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-bean.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-bean-%{version}.jar.*
%endif

%files    tags-beanshell
%{_javadir}/jakarta-commons-jelly-tags-beanshell.jar
%{_javadir}/commons-jelly-tags-beanshell.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-beanshell-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-beanshell.jar
%{_javadir}/jelly-tags/commons-jelly-tags-beanshell-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-beanshell.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-beanshell-%{version}.jar.*
%endif

%files    tags-betwixt
%{_javadir}/jakarta-commons-jelly-tags-betwixt.jar
%{_javadir}/commons-jelly-tags-betwixt.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-betwixt-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-betwixt.jar
%{_javadir}/jelly-tags/commons-jelly-tags-betwixt-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-betwixt.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-betwixt-%{version}.jar.*
%endif

%files    tags-bsf
%{_javadir}/jakarta-commons-jelly-tags-bsf.jar
%{_javadir}/commons-jelly-tags-bsf.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-bsf-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-bsf.jar
%{_javadir}/jelly-tags/commons-jelly-tags-bsf-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-bsf.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-bsf-%{version}.jar.*
%endif

%files    tags-define
%{_javadir}/jakarta-commons-jelly-tags-define.jar
%{_javadir}/commons-jelly-tags-define.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-define-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-define.jar
%{_javadir}/jelly-tags/commons-jelly-tags-define-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-define.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-define-%{version}.jar.*
%endif

%files    tags-dynabean
%{_javadir}/jakarta-commons-jelly-tags-dynabean.jar
%{_javadir}/commons-jelly-tags-dynabean.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-dynabean-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-dynabean.jar
%{_javadir}/jelly-tags/commons-jelly-tags-dynabean-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-dynabean.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-dynabean-%{version}.jar.*
%endif

%files    tags-email
%{_javadir}/jakarta-commons-jelly-tags-email.jar
%{_javadir}/commons-jelly-tags-email.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-email-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-email.jar
%{_javadir}/jelly-tags/commons-jelly-tags-email-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-email.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-email-%{version}.jar.*
%endif

%files    tags-fmt
%{_javadir}/jakarta-commons-jelly-tags-fmt.jar
%{_javadir}/commons-jelly-tags-fmt.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-fmt-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-fmt.jar
%{_javadir}/jelly-tags/commons-jelly-tags-fmt-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-fmt.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-fmt-%{version}.jar.*
%endif

%files    tags-html
%{_javadir}/jakarta-commons-jelly-tags-html.jar
%{_javadir}/commons-jelly-tags-html.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-html-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-html.jar
%{_javadir}/jelly-tags/commons-jelly-tags-html-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-html.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-html-%{version}.jar.*
%endif

%files    tags-http
%{_javadir}/jakarta-commons-jelly-tags-http.jar
%{_javadir}/commons-jelly-tags-http.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-http-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-http.jar
%{_javadir}/jelly-tags/commons-jelly-tags-http-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-http.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-http-%{version}.jar.*
%endif

%files    tags-interaction
%{_javadir}/jakarta-commons-jelly-tags-interaction.jar
%{_javadir}/commons-jelly-tags-interaction.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-interaction-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-interaction.jar
%{_javadir}/jelly-tags/commons-jelly-tags-interaction-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-interaction.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-interaction-%{version}.jar.*
%endif

%if %{with_jaxme}
%files    tags-jaxme
%{_javadir}/jakarta-commons-jelly-tags-jaxme.jar
%{_javadir}/commons-jelly-tags-jaxme.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-jaxme-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-jaxme.jar
%{_javadir}/jelly-tags/commons-jelly-tags-jaxme-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-jaxme.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-jaxme-%{version}.jar.*
%endif
%endif

%files    tags-jetty
%{_javadir}/jakarta-commons-jelly-tags-jetty.jar
%{_javadir}/commons-jelly-tags-jetty.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-jetty-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-jetty.jar
%{_javadir}/jelly-tags/commons-jelly-tags-jetty-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-jetty.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-jetty-%{version}.jar.*
%endif

%files    tags-jms
%{_javadir}/jakarta-commons-jelly-tags-jms.jar
%{_javadir}/commons-jelly-tags-jms.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-jms-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-jms.jar
%{_javadir}/jelly-tags/commons-jelly-tags-jms-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-jms.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-jms-%{version}.jar.*
%endif

%files    tags-jmx
%{_javadir}/jakarta-commons-jelly-tags-jmx.jar
%{_javadir}/commons-jelly-tags-jmx.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-jmx-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-jmx.jar
%{_javadir}/jelly-tags/commons-jelly-tags-jmx-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-jmx.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-jmx-%{version}.jar.*
%endif

%files    tags-jsl
%{_javadir}/jakarta-commons-jelly-tags-jsl.jar
%{_javadir}/commons-jelly-tags-jsl.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-jsl-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-jsl.jar
%{_javadir}/jelly-tags/commons-jelly-tags-jsl-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-jsl.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-jsl-%{version}.jar.*
%endif

%files    tags-junit
%{_javadir}/jakarta-commons-jelly-tags-junit.jar
%{_javadir}/commons-jelly-tags-junit.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-junit-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-junit.jar
%{_javadir}/jelly-tags/commons-jelly-tags-junit-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-junit.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-junit-%{version}.jar.*
%endif

%files    tags-log
%{_javadir}/jakarta-commons-jelly-tags-log.jar
%{_javadir}/commons-jelly-tags-log.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-log-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-log.jar
%{_javadir}/jelly-tags/commons-jelly-tags-log-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-log.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-log-%{version}.jar.*
%endif

%files    tags-ojb
%{_javadir}/jakarta-commons-jelly-tags-ojb.jar
%{_javadir}/commons-jelly-tags-ojb.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-ojb-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-ojb.jar
%{_javadir}/jelly-tags/commons-jelly-tags-ojb-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-ojb.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-ojb-%{version}.jar.*
%endif

%files    tags-quartz
%{_javadir}/jakarta-commons-jelly-tags-quartz.jar
%{_javadir}/commons-jelly-tags-quartz.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-quartz-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-quartz.jar
%{_javadir}/jelly-tags/commons-jelly-tags-quartz-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-quartz.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-quartz-%{version}.jar.*
%endif

%files    tags-soap
%{_javadir}/jakarta-commons-jelly-tags-soap.jar
%{_javadir}/commons-jelly-tags-soap.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-soap-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-soap.jar
%{_javadir}/jelly-tags/commons-jelly-tags-soap-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-soap.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-soap-%{version}.jar.*
%endif

%files    tags-sql
%{_javadir}/jakarta-commons-jelly-tags-sql.jar
%{_javadir}/commons-jelly-tags-sql.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-sql-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-sql.jar
%{_javadir}/jelly-tags/commons-jelly-tags-sql-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-sql.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-sql-%{version}.jar.*
%endif

%files    tags-swing
%{_javadir}/jakarta-commons-jelly-tags-swing.jar
%{_javadir}/commons-jelly-tags-swing.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-swing-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-swing.jar
%{_javadir}/jelly-tags/commons-jelly-tags-swing-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-swing.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-swing-%{version}.jar.*
%endif

%files    tags-threads
%{_javadir}/jakarta-commons-jelly-tags-threads.jar
%{_javadir}/commons-jelly-tags-threads.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-threads-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-threads.jar
%{_javadir}/jelly-tags/commons-jelly-tags-threads-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-threads.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-threads-%{version}.jar.*
%endif

%files    tags-util
%{_javadir}/jakarta-commons-jelly-tags-util.jar
%{_javadir}/commons-jelly-tags-util.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-util-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-util.jar
%{_javadir}/jelly-tags/commons-jelly-tags-util-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-util.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-util-%{version}.jar.*
%endif

%files    tags-validate
%{_javadir}/jakarta-commons-jelly-tags-validate.jar
%{_javadir}/commons-jelly-tags-validate.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-validate-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-validate.jar
%{_javadir}/jelly-tags/commons-jelly-tags-validate-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-validate.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-validate-%{version}.jar.*
%endif

%files    tags-velocity
%{_javadir}/jakarta-commons-jelly-tags-velocity.jar
%{_javadir}/commons-jelly-tags-velocity.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-velocity-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-velocity.jar
%{_javadir}/jelly-tags/commons-jelly-tags-velocity-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-velocity.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-velocity-%{version}.jar.*
%endif

%files    tags-xml
%{_javadir}/jakarta-commons-jelly-tags-xml.jar
%{_javadir}/commons-jelly-tags-xml.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-xml-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-xml.jar
%{_javadir}/jelly-tags/commons-jelly-tags-xml-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-xml.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-xml-%{version}.jar.*
%endif

%files    tags-xmlunit
%{_javadir}/jakarta-commons-jelly-tags-xmlunit.jar
%{_javadir}/commons-jelly-tags-xmlunit.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-xmlunit-1.0.jar
%{_javadir}/jelly-tags/jakarta-commons-jelly-tags-xmlunit.jar
%{_javadir}/jelly-tags/commons-jelly-tags-xmlunit-1.0.jar
%{_javadir}/jelly-tags/commons-jelly-tags-xmlunit.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tags-xmlunit-%{version}.jar.*
%endif


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt10_7jpp6
- fixed build with java7

* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt9_7jpp6
- new jpp release

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt9_6jpp5
- build with ant17

* Fri Dec 17 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt8_6jpp5
- patched velocity tag 

* Wed Dec 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_6jpp5
- fixed build

* Wed Oct 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6_6jpp5
- fixed build

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_6jpp5
- selected java5 compiler explicitly

* Sat Feb 28 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_6jpp5
- jpp5 release

* Fri Nov 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_5jpp1.7
- converted from JPackage by jppimport script

* Fri Aug 31 2007 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4
- rebuild with taglibs-standard jstl

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3
- added jpackage compat. symlink

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2
- resurrected from orphaned;
- added jpackage compat links

* Sat Jul 02 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt1
- Final release
- update servletapi dependency to servletapi5
- changed rpmgroup for javadoc package

* Wed May 04 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt0.1
- Initial release for ALTLinux Sisyphus
- svn snapshot 20050504

