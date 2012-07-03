%define oldname maven
%define movname maven1
%add_findreq_skiplist %_datadir/maven1/repository/javadoc/jars/*
%add_findreq_skiplist %_datadir/maven1/bin/*
BuildRequires: /proc
BuildRequires: jpackage-core
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


# If you need to omit BRs of foreign maven plugins
# which in turn require maven

%define bootstrap %{?_with_bootstrap:1}%{!?_with_bootstrap:%{?_without_bootstrap:0}%{!?_without_bootstrap:%{?_bootstrap:%{_bootstrap}}%{!?_bootstrap:0}}}

%define RHEL4 0
%define NONFREE 0

%define ver_jelly_tags 1.0.1

%define __os_install_post %{nil}

Name:           maven1
Version:        1.1
Release:        alt18_9jpp6
Epoch:          0
Summary:        Java project management and project comprehension tool

Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://maven.apache.org/

# svn export http://svn.apache.org/repos/asf/maven/maven-1/core/tags/maven-1.1/
Source0:        maven-1.1-src.tar.gz

# svn export http://svn.apache.org/repos/asf/maven/maven-1/plugins/trunk -r 565288 maven-plugins
Source2:        maven-plugins-r565288-src.tar.gz

Source3:        maven-1.1-build-maven-library
Source300:        maven-1.1-build-maven-library-build
Source4:        maven-1.1.script
Source5:        maven-jelly-tags-1.0.1-build.xml
Source6:        maven-1.1-MavenUtilsTest.java

# svn export http://svn.apache.org/repos/asf/maven/maven-1/plugins-sandbox/trunk -r 565288 maven-plugins-sandbox
Source7:        maven-plugins-sandbox-r565288-src.tar.gz

Source8:        maven-1.1-poms.tar.gz

Patch0:         maven-1.1-jpp.patch
# New:
Patch1:          maven-plugins-sandbox-r565288.patch
Patch2:          maven-plugins-r565288.patch
Patch3:          maven-1.1-DependencyVerifier.patch
Patch4:          maven-1.1-project-properties.patch
Patch5:          maven-project.patch
#Patch6:          maven-1.1-DefaultArtifactDeployer.patch
Patch7:          maven-1.1-plugins-project.patch
Patch8:          maven-1.1-RepositoryBuilder.patch
Patch9:          maven-1.1-ScmUtil.patch


#BuildArch:      noarch
Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0
BuildRequires: jpackage-utils >= 0:5.0.0

# !!! MM.MYSQL IS MISSING !!! -- mm.mysql-2.0.13-bin.jar (use mysql-connector-java)
# !!! MRJ TOOLKIT IS MISSING !!! -- MRJToolkitStubs-1.0.jar (omit abbot)
# !!! SAXPATH IS MISSING !!! -- saxpath-1.0-FCS.jar (use jaxen for this)

Summary:        The base maven package
Group:          Development/Java
BuildRequires: ant17
BuildRequires: ant17-junit
BuildRequires: ant17-nodeps
BuildRequires: ant17-trax
BuildRequires: xmlgraphics-batik
BuildRequires: bea-stax
BuildRequires: bea-stax-api
BuildRequires: dom4j >= 0:1.6.1
BuildRequires: forehead >= 0:1.0.b4
BuildRequires: hibernate2-tools
BuildRequires: jakarta-commons-beanutils16 >= 0:1.6.1
#BuildRequires:  jakarta-commons-betwixt
BuildRequires: jakarta-commons-cli10
BuildRequires: apache-commons-codec >= 0:1.2
BuildRequires: apache-commons-collections >= 0:3.1-1jpp
BuildRequires: jakarta-commons-graph >= 0:0.8.1
BuildRequires: jakarta-commons-httpclient >= 0:3.0
BuildRequires: apache-commons-io >= 0:1.2
BuildRequires: jakarta-commons-jelly >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-ant
BuildRequires: jakarta-commons-jelly-tags-define
BuildRequires: jakarta-commons-jelly-tags-interaction >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-util
BuildRequires: jakarta-commons-jelly-tags-xml
BuildRequires: apache-commons-jexl >= 0:1.0
BuildRequires: apache-commons-lang >= 0:2.0
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: jaxen >= 0:1.1
BuildRequires: jsch >= 0:0.1.27
BuildRequires: junit >= 0:3.8.2
BuildRequires: log4j >= 0:1.2.13
BuildRequires: maven-model >= 0:3.0.2
BuildRequires: maven-wagon >= 0:1.0-0.b2
BuildRequires: objectweb-asm
BuildRequires: plexus-classworlds
BuildRequires: plexus-containers-component-api
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-utils >= 0:1.0.3
BuildRequires: qname_1_1_api
BuildRequires: stax-utils
BuildRequires: werkz >= 1.0-0.b10.5jpp
BuildRequires: xerces-j2 >= 0:2.7.1
BuildRequires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
BuildRequires: xml-commons-resolver11
Requires: ant17
Requires: ant17-junit
Requires: ant17-nodeps
Requires: ant17-trax
Requires: dom4j >= 0:1.6.1
Requires: forehead >= 0:1.0.b4
Requires: jakarta-commons-beanutils16 >= 0:1.6.1
Requires: jakarta-commons-cli10
Requires: apache-commons-codec >= 0:1.2
Requires: apache-commons-collections >= 0:3.1-1jpp
Requires: jakarta-commons-graph >= 0:0.8.1
Requires: jakarta-commons-httpclient >= 0:3.0
Requires: apache-commons-io >= 0:1.2
Requires: jakarta-commons-jelly >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-ant
Requires: jakarta-commons-jelly-tags-define
Requires: jakarta-commons-jelly-tags-interaction >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-util
Requires: jakarta-commons-jelly-tags-xml
Requires: apache-commons-jexl >= 0:1.0
Requires: apache-commons-lang >= 0:2.0
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: jaxen >= 0:1.1
Requires: jsch >= 0:0.1.27
Requires: junit >= 0:3.8.2
Requires: log4j >= 0:1.2.13
Requires: maven-model >= 0:3.0.2
Requires: maven-wagon >= 0:1.0-0.b2
Requires: plexus-utils >= 1.0.3
Requires: stax-utils
Requires: werkz >= 1.0-0.b10.5jpp
Requires: xerces-j2 >= 0:2.7.1
Requires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Requires: xml-commons-resolver11

Requires(post): ant17
Requires(post): ant17-junit
Requires(post): ant17-nodeps
Requires(post): ant17-trax
Requires(post): dom4j >= 0:1.6.1
Requires(post): forehead >= 0:1.0.b4
Requires(post): jakarta-commons-beanutils16 >= 0:1.6.1
Requires(post): jakarta-commons-cli10
Requires(post): apache-commons-codec >= 0:1.2
Requires(post): apache-commons-collections >= 0:3.1-1jpp
Requires(post): jakarta-commons-graph >= 0:0.8.1
Requires(post): jakarta-commons-httpclient >= 0:3.0
Requires(post): apache-commons-io >= 0:1.2
Requires(post): jakarta-commons-jelly >= 0:1.0-5jpp
Requires(post): jakarta-commons-jelly-tags-ant
Requires(post): jakarta-commons-jelly-tags-define
Requires(post): jakarta-commons-jelly-tags-interaction >= 0:1.0-5jpp
Requires(post): jakarta-commons-jelly-tags-util
Requires(post): jakarta-commons-jelly-tags-xml
Requires(post): apache-commons-jexl >= 0:1.0
Requires(post): apache-commons-lang >= 0:2.0
Requires(post): jakarta-commons-logging >= 0:1.0.4
Requires(post): jaxen >= 0:1.1
Requires(post): log4j >= 0:1.2.13
Requires(post): maven-model >= 0:3.0.2
Requires(post): maven-wagon >= 0:1.0-0.b2
Requires(post): plexus-utils >= 1.0.3
Requires(post): werkz >= 1.0-0.b10.5jpp
Requires(post): xerces-j2 >= 0:2.7.1
Requires(post): xml-commons-jaxp-1.3-apis >= 0:1.3.03
Requires(post): xml-commons-resolver11

Provides: %movname = %{epoch}:%{version}-%{release}
Source44: import.info
Patch33: maven-1.1-plugin-checkstyle-alt-add-collections-dep.patch
Provides: %movname = %version-%release
Provides: %movname = 0:%version-%release
Obsoletes: maven1 < 1.1-alt14

# Begin sub package listings...

%package plugins-base
Summary:        Base plugins for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: dom4j >= 0:1.6.1
BuildRequires: isorelax
BuildRequires: forehead >= 0:1.0.b4
#BuildRequires:  jaf
BuildRequires: jakarta-commons-beanutils16 >= 0:1.6.1
BuildRequires: apache-commons-codec >= 0:1.2
BuildRequires: apache-commons-collections >= 0:3.1-1jpp
BuildRequires: jakarta-commons-jelly >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-ant >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-http >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-velocity >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
BuildRequires: apache-commons-jexl >= 0:1.0
BuildRequires: apache-commons-lang >= 0:2.0
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: jakarta-commons-net >= 0:1.4.1
BuildRequires: javacc3 >= 0:3.2
BuildRequires: jaxen >= 0:1.1
BuildRequires: jdom >= 0:1.0
BuildRequires: jline >= 0:0.9.5
BuildRequires: jsch >= 0:0.1.27
BuildRequires: junit >= 0:3.8.2
BuildRequires: maven-model >= 0:3.0.2
BuildRequires: maven-wagon >= 0:1.0-0.b2
BuildRequires: msv-msv
BuildRequires: msv-xsdlib
BuildRequires: plexus-utils >= 0:1.0.3
BuildRequires: relaxngDatatype
BuildRequires: velocity >= 0:1.5
BuildRequires: xerces-j2 >= 0:2.7.1
BuildRequires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
BuildRequires: xml-commons-resolver11
Requires: dom4j >= 0:1.6.1
Requires: isorelax
Requires: forehead >= 0:1.0.b4
Requires: jakarta-commons-beanutils16 >= 0:1.6.1
Requires: apache-commons-codec >= 0:1.2
Requires: apache-commons-collections >= 0:3.1-1jpp
Requires: jakarta-commons-jelly >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-ant >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-http >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-interaction >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-velocity >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Requires: apache-commons-jexl >= 0:1.0
Requires: apache-commons-lang >= 0:2.0
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: jakarta-commons-net >= 0:1.4.1
Requires: javacc3 >= 0:3.2
Requires: jaxen >= 0:1.1
Requires: jdom >= 0:1.0
Requires: jline >= 0:0.9.5
Requires: jsch >= 0:0.1.27
Requires: junit >= 0:3.8.2
Requires: maven-model >= 0:3.0.2
Requires: maven-wagon >= 0:1.0-0.b2
Requires: msv-msv
Requires: msv-xsdlib
Requires: plexus-utils >= 0:1.0.3
Requires: relaxngDatatype
Requires: velocity >= 0:1.5
Requires: xerces-j2 >= 0:2.7.1
Requires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Requires: xml-commons-resolver11
Provides: %movname-plugins-base = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-ant = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-artifact = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-clean = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-console = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-jar = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-java = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-javacc = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-javadoc = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-junit-report = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-plugin = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-pom = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugins-base < 1.1-alt14
BuildArch: noarch

%description plugins-base
%{summary}.

%if 0
%package plugin-abbot
Summary:        Optional abbot plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: abbot
BuildRequires: ant17
BuildRequires: ant17-junit
BuildRequires: gnu-regexp
BuildRequires: jakarta-commons-jelly-tags-xml
BuildRequires: jdom
BuildRequires: junit
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
Requires: abbot
Requires: ant17
Requires: gnu-regexp
Requires: jakarta-commons-jelly-tags-xml
Requires: jdom
Requires: junit
Requires: xerces-j2
Requires: xml-commons-jaxp-1.3-apis
Provides: %movname-plugin-abbot = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-abbot < 1.1-alt14
BuildArch: noarch

%description plugin-abbot
%{summary}.
%endif

%package plugin-announcement
Summary:        Optional announcement plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
BuildRequires: apache-commons-lang >= 0:2.0
BuildRequires: jakarta-commons-net >= 0:1.4.1
BuildRequires: junit >= 0:3.8.2
Requires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Requires: apache-commons-lang >= 0:2.0
Requires: jakarta-commons-net >= 0:1.4.1
Provides: %movname-plugin-announcement = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-announcement < 1.1-alt14
BuildArch: noarch

%description plugin-announcement
%{summary}.

%package plugin-antlr
Summary:        Optional antlr plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: antlr >= 0:2.7.6
BuildRequires: jakarta-commons-jelly-tags-antlr >= 0:1.0-5jpp
BuildRequires: apache-commons-lang >= 0:2.0
BuildRequires: junit >= 0:3.8.2
Requires: antlr >= 0:2.7.6
Requires: jakarta-commons-jelly-tags-antlr >= 0:1.0-5jpp
Requires: apache-commons-lang >= 0:2.0
Provides: %movname-plugin-antlr = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-antlr < 1.1-alt14
BuildArch: noarch

%description plugin-antlr
%{summary}.


%package plugin-appserver
Summary:        Optional appserver plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: ant17
BuildRequires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
Requires: ant17
Requires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
Provides: %movname-plugin-appserver = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-appserver < 1.1-alt14
BuildArch: noarch

%description plugin-appserver
%{summary}.

%if %{RHEL4}==0
%package plugin-aspectj
Summary:        Optional aspectj plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: aspectj >= 0:1.2.1
BuildRequires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
BuildRequires: junit >= 0:3.8.2
Requires: aspectj >= 0:1.2.1
Requires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
Requires: junit >= 0:3.8.2
Provides: %movname-plugin-aspectj = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-aspectj < 1.1-alt14
BuildArch: noarch

%description plugin-aspectj
%{summary}.
%endif

%if %{RHEL4}==0
%package plugin-aspectwerkz
Summary:        Optional aspectwerkz plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: ant17
BuildRequires: aspectwerkz >= 0:2.0
BuildRequires: bcel5.3
BuildRequires: dom4j >= 0:1.6.1
BuildRequires: gnu-trove >= 0:1.0.2
BuildRequires: apache-commons-jexl >= 0:1.0
BuildRequires: jrexx >= 0:1.1.1
BuildRequires: qdox161
BuildRequires: xerces-j2 >= 0:2.7.1
BuildRequires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
BuildRequires: xml-commons-resolver11
Requires: ant17
Requires: aspectwerkz >= 0:2.0
Requires: bcel5.3
Requires: dom4j >= 0:1.6.1
Requires: gnu-trove >= 0:1.0.2
Requires: apache-commons-jexl >= 0:1.0
Requires: jrexx >= 0:1.1.1
Requires: qdox161
Requires: xerces-j2 >= 0:2.7.1
Requires: xml-commons-jaxp-1.3-apis
Provides: %movname-plugin-aspectwerkz = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-aspectwerkz < 1.1-alt14
BuildArch: noarch

%description plugin-aspectwerkz
%{summary}.
%endif

%package plugin-cactus-jcoverage-integration
Summary:        Optional cactus jcoverage integration plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-cactus-jcoverage-integration = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-cactus-jcoverage-integration < 1.1-alt14
BuildArch: noarch

%description plugin-cactus-jcoverage-integration
%{summary}.

%package plugin-caller
Summary:        Optional caller plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-caller = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-caller < 1.1-alt14
BuildArch: noarch

%description plugin-caller
%{summary}.

%package plugin-castor
Summary:        Optional castor plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: castor0 >= 0:0.9.5
Requires: castor0 >= 0:0.9.5
Provides: %movname-plugin-castor = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-castor < 1.1-alt14
BuildArch: noarch

%description plugin-castor
%{summary}.

%if %{RHEL4}==0
%package plugin-changelog
Summary:        Optional changelog plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: ant17
BuildRequires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: junit >= 0:3.8.2
BuildRequires: javacvs-lib >= 0:3.6
BuildRequires: maven-model >= 0:3.0.2
BuildRequires: regexp >= 0:1.3
BuildRequires: xerces-j2 >= 0:2.7.1
BuildRequires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
BuildRequires: xml-commons-resolver11
Requires: ant17
Requires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: junit >= 0:3.8.2
Requires: javacvs-lib >= 3.6
Requires: maven-model >= 0:3.0.2
Requires: regexp >= 0:1.3
Requires: xerces-j2 >= 0:2.7.1
Requires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Requires: xml-commons-resolver11
Provides: %movname-plugin-changelog = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-changelog < 1.1-alt14
BuildArch: noarch

%description plugin-changelog
%{summary}.
%endif

%package plugin-changes
Summary:        Optional changes plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: dom4j >= 0:1.6.1
BuildRequires: apache-commons-io >= 0:1.2
BuildRequires: jaxen >= 0:1.1
BuildRequires: junit >= 0:3.8.2
BuildRequires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Requires: dom4j >= 0:1.6.1
Requires: apache-commons-io >= 0:1.2
Requires: jaxen >= 0:1.1
Requires: junit >= 0:3.8.2
Requires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Provides: %movname-plugin-changes = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-changes < 1.1-alt14
BuildArch: noarch

%description plugin-changes
%{summary}.

%package plugin-checkstyle
Summary:        Optional checkstyle plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: antlr >= 0:2.7.6
BuildRequires: checkstyle4 >= 0:4.4
BuildRequires: checkstyle4-optional >= 0:4.4
BuildRequires: jakarta-commons-beanutils >= 0:1.7.0
BuildRequires: junit >= 0:3.8.2
BuildRequires: regexp >= 0:1.3
Requires: antlr >= 0:2.7.6
Requires: checkstyle4 >= 0:4.4
Requires: checkstyle4-optional >= 0:4.4
Requires: jakarta-commons-beanutils >= 0:1.7.0
Requires: regexp >= 0:1.3
Provides: %movname-plugin-checkstyle = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-checkstyle < 1.1-alt14
BuildArch: noarch

%description plugin-checkstyle
%{summary}.

%package plugin-cruisecontrol
Summary:        Optional cruisecontrol plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
BuildRequires: junit >= 0:3.8.2
Requires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Provides: %movname-plugin-cruisecontrol = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-cruisecontrol < 1.1-alt14
BuildArch: noarch

%description plugin-cruisecontrol
%{summary}.

%package plugin-developer-activity
Summary:        Optional developer-activity plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
BuildRequires: junit >= 0:3.8.2
Requires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Provides: %movname-plugin-developer-activity = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-developer-activity < 1.1-alt14
BuildArch: noarch

%description plugin-developer-activity
%{summary}.

%if ! %{bootstrap}
%package plugin-dashboard
Summary:        Optional dashboard plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: sf-findbugs-maven-plugin
BuildRequires: sf-javancss-maven-plugin
Requires: sf-findbugs-maven-plugin
Requires: sf-javancss-maven-plugin
Provides: %movname-plugin-dashboard = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-dashboard < 1.1-alt14
BuildArch: noarch

%description plugin-dashboard
%{summary}.
%endif

%package plugin-dist
Summary:        Optional dist plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: apache-commons-lang >= 0:2.0
BuildRequires: junit >= 0:3.8.2
Requires: apache-commons-lang >= 0:2.0
Requires: junit >= 0:3.8.2
Provides: %movname-plugin-dist = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-dist < 1.1-alt14
BuildArch: noarch

%description plugin-dist
%{summary}.

%package plugin-docbook
Summary:        Optional docbook plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: xalan-j2 >= 0:2.4.1
Requires: xalan-j2 >= 0:2.4.1
Provides: %movname-plugin-docbook = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-docbook < 1.1-alt14
BuildArch: noarch

%description plugin-docbook
%{summary}.

%package plugin-ear
Summary:        Optional ear plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-jelly-tags-util >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
BuildRequires: jakarta-commons-logging >= 0:1.0.4
Requires: jakarta-commons-jelly-tags-util >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Requires: jakarta-commons-logging >= 0:1.0.4
Provides: %movname-plugin-ear = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-ear < 1.1-alt14
BuildArch: noarch

%description plugin-ear
%{summary}.

%package plugin-eclipse
Summary:        Optional eclipse plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-jelly >= 0:1.0-5jpp
BuildRequires: apache-commons-lang >= 0:2.0
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: junit >= 0:3.8.2
BuildRequires: maven-model >= 0:3.0.2
Requires: jakarta-commons-jelly >= 0:1.0-5jpp
Requires: apache-commons-lang >= 0:2.0
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: maven-model >= 0:3.0.2
Provides: %movname-plugin-eclipse = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-eclipse < 1.1-alt14
BuildArch: noarch

%description plugin-eclipse
%{summary}.

%package plugin-ejb
Summary:        Optional ejb plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: apache-commons-lang >= 0:2.0
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: junit >= 0:3.8.2
BuildRequires: maven-model >= 0:3.0.2
Requires: apache-commons-lang >= 0:2.0
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: maven-model >= 0:3.0.2
Provides: %movname-plugin-ejb = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-ejb < 1.1-alt14
BuildArch: noarch

%description plugin-ejb
%{summary}.

%package plugin-faq
Summary:        Optional faq plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-faq = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-faq < 1.1-alt14
BuildArch: noarch

%description plugin-faq
%{summary}.

%package plugin-file-activity
Summary:        Optional file-activity plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
BuildRequires: junit >= 0:3.8.2
Requires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Provides: %movname-plugin-file-activity = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-file-activity < 1.1-alt14
BuildArch: noarch

%description plugin-file-activity
%{summary}.

%if ! %{bootstrap}
%package plugin-genapp
Summary:        Optional genapp plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: bsf
BuildRequires: dom4j
BuildRequires: hivemind
BuildRequires: httpunit
BuildRequires: jakarta-cactus
BuildRequires: jakarta-commons-beanutils16
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-collections
#BuildRequires:  jakarta-commons-digester
BuildRequires: jakarta-commons-fileupload
BuildRequires: jakarta-commons-jelly-tags-interaction >= 0:1.0-5jpp
BuildRequires: apache-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-validator
BuildRequires: jakarta-oro
BuildRequires: jakarta-taglibs-standard
BuildRequires: javassist
BuildRequires: jboss4-j2ee
BuildRequires: jboss4-server
BuildRequires: jline >= 0:0.9.5
BuildRequires: jtidy
BuildRequires: junit >= 0:3.8.2
BuildRequires: ognl
#BuildRequires:  servletapi4
BuildRequires: servletapi5
BuildRequires: struts
BuildRequires: strutstestcase
BuildRequires: tapestry
BuildRequires: velocity
BuildRequires: velocity-tools >= 0:1.3
BuildRequires: xdoclet
BuildRequires: xdoclet-maven-plugin
BuildRequires: xjavadoc
Requires: jakarta-commons-jelly-tags-interaction >= 0:1.0-5jpp
Requires: jline >= 0:0.9.5
Provides: %movname-plugin-genapp = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-genapp < 1.1-alt14
BuildArch: noarch

%description plugin-genapp
%{summary}.
%endif

%package plugin-gump
Summary:        Optional gump plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-gump = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-gump < 1.1-alt14
BuildArch: noarch

%description plugin-gump
%{summary}.

%package plugin-html2xdoc
Summary:        Optional html2xdoc plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: dom4j >= 0:1.6.1
BuildRequires: jakarta-commons-jelly-tags-html >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: jaxen >= 0:1.1
BuildRequires: junit >= 0:3.8.2
BuildRequires: nekohtml >= 0:0.9.5
BuildRequires: xerces-j2 >= 0:2.7.1
BuildRequires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
BuildRequires: xml-commons-resolver11
Requires: dom4j >= 0:1.6.1
Requires: jakarta-commons-jelly-tags-html >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: jaxen >= 0:1.1
Requires: nekohtml >= 0:0.9.5
Requires: xerces-j2 >= 0:2.7.1
Requires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Requires: xml-commons-resolver11
Provides: %movname-plugin-html2xdoc = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-html2xdoc < 1.1-alt14
BuildArch: noarch

%description plugin-html2xdoc
%{summary}.

%package plugin-idea
Summary:        Optional idea plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-idea = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-idea < 1.1-alt14
BuildArch: noarch

%description plugin-idea
%{summary}.

%package plugin-itest
Summary:        Optional itest plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: junit >= 0:3.8.2
Requires: junit >= 0:3.8.2
Provides: %movname-plugin-itest = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-itest = 0:1.0-0.20060129.1jpp
Obsoletes: maven-plugin-itest < 1.1-alt14
BuildArch: noarch


%description plugin-itest
%{summary}.

%package plugin-j2ee
Summary:        Optional j2ee plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: dom4j >= 0:1.6.1
BuildRequires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: jaxen >= 0:1.1
BuildRequires: junit >= 0:3.8.2
BuildRequires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Requires: dom4j >= 0:1.6.1
Requires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: jaxen >= 0:1.1
Requires: junit >= 0:3.8.2
Requires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Provides: %movname-plugin-j2ee = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-j2ee < 1.1-alt14
BuildArch: noarch

%description plugin-j2ee
%{summary}.

%if %{RHEL4}==0
%package plugin-jalopy
Summary:        Optional jalopy plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jalopy >= 0:1.0-0.b11
#BuildRequires:  jalopy-ant >= 0:1.0-0.b11
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: jdom >= 0:1.0
#BuildRequires:  jext
BuildRequires: log4j >= 0:1.2.13
BuildRequires: jakarta-oro >= 0:2.0.8
BuildRequires: plexus-utils >= 0:1.0.3
BuildRequires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Requires: jalopy >= 0:1.0-0.b11
#Requires:  jalopy-ant >= 0:1.0-0.b11
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: jdom >= 0:1.0
#Requires:  jext
Requires: log4j >= 0:1.2.13
Requires: jakarta-oro >= 0:2.0.8
Requires: plexus-utils >= 0:1.0.3
Requires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Provides: %movname-plugin-jalopy = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-jalopy < 1.1-alt14
BuildArch: noarch

%description plugin-jalopy
%{summary}.
%endif

%package plugin-jboss
Summary:        Optional jboss plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-jboss = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-jboss < 1.1-alt14
BuildArch: noarch

%description plugin-jboss
%{summary}.

%package plugin-jbuilder
Summary:        Optional jbuilder plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Provides: %movname-plugin-jbuilder = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-jbuilder < 1.1-alt14
BuildArch: noarch

%description plugin-jbuilder
%{summary}.

%package plugin-jcoverage
Summary:        Optional jcoverage plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: bcel5.3
BuildRequires: gnu-getopt >= 0:1.0.12
BuildRequires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
BuildRequires: jcoverage >= 0:1.0.5
BuildRequires: junit >= 0:3.8.2
BuildRequires: log4j >= 0:1.2.13
BuildRequires: jakarta-oro >= 0:2.0.8
BuildRequires: velocity >= 0:1.5
BuildRequires: xerces-j2 >= 0:2.7.1
BuildRequires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
BuildRequires: xml-commons-resolver11
BuildRequires: xpp3 >= 0:1.1.3
Requires: bcel5.3
Requires: gnu-getopt >= 0:1.0.12
Requires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
Requires: jcoverage >= 0:1.0.5
Requires: junit >= 0:3.8.2
Requires: log4j >= 0:1.2.13
Requires: jakarta-oro >= 0:2.0.8
Requires: velocity >= 0:1.5
Requires: xerces-j2 >= 0:2.7.1
Requires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Requires: xml-commons-resolver11
Requires: xpp3 >= 0:1.1.3
Provides: %movname-plugin-jcoverage = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-jcoverage < 1.1-alt14
BuildArch: noarch

%description plugin-jcoverage
%{summary}.

%package plugin-jdee
Summary:        Optional jdee plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-jdee = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-jdee < 1.1-alt14
BuildArch: noarch

%description plugin-jdee
%{summary}.

%package plugin-jdepend
Summary:        Optional jdepend plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
BuildRequires: jdepend >= 0:2.9.1
BuildRequires: junit >= 0:3.8.2
BuildRequires: xerces-j2 >= 0:2.7.1
BuildRequires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
BuildRequires: xml-commons-resolver11
Requires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Requires: jdepend >= 0:2.9.1
Requires: xerces-j2 >= 0:2.7.1
Requires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Requires: xml-commons-resolver11
Provides: %movname-plugin-jdepend = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-jdepend < 1.1-alt14
BuildArch: noarch

%description plugin-jdepend
%{summary}.

%if %{RHEL4}==0
%package plugin-jdeveloper
Summary:        Optional jdeveloper plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jdepend22 >= 2.2-2jpp
Requires: jdepend22 >= 2.2-2jpp
Provides: %movname-plugin-jdeveloper = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-jdeveloper < 1.1-alt14
BuildArch: noarch

%description plugin-jdeveloper
%{summary}.
%endif

%if %{RHEL4}==0
%package plugin-jdiff
Summary:        Optional jdiff plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jdiff >= 0:1.0.10
BuildRequires: junit >= 0:3.8.2
BuildRequires: xerces-j2 >= 0:2.7.1
Requires: jdiff >= 0:1.0.10
Requires: xerces-j2 >= 0:2.7.1
Provides: %movname-plugin-jdiff = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-jdiff < 1.1-alt14
BuildArch: noarch

%description plugin-jdiff
%{summary}.
%endif

%package plugin-jellydoc
Summary:        Optional jellydoc plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: dom4j >= 0:1.6.1
BuildRequires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
BuildRequires: nekohtml >= 0:0.9.5
BuildRequires: xerces-j2 >= 0:2.7.1
BuildRequires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
BuildRequires: xml-commons-resolver11
Requires: dom4j >= 0:1.6.1
Requires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Requires: nekohtml >= 0:0.9.5
Requires: xerces-j2 >= 0:2.7.1
Requires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Requires: xml-commons-resolver11
Provides: %movname-plugin-jellydoc = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-jellydoc < 1.1-alt14
BuildArch: noarch

%description plugin-jellydoc
%{summary}.

%if %{RHEL4}==0
%package plugin-jetty
Summary:        Optional jetty plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: ant17
BuildRequires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
BuildRequires: jetty5
BuildRequires: tomcat5-jasper
BuildRequires: tomcat5-servlet-2.4-api
Requires: ant17
Requires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Requires: jetty5
Requires: tomcat5-jasper
Requires: tomcat5-servlet-2.4-api
Provides: %movname-plugin-jetty = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-jetty < 1.1-alt14
BuildArch: noarch

%description plugin-jetty
%{summary}.
%endif

%package plugin-jira
Summary:        Optional jira plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-httpclient >= 0:3.0
BuildRequires: apache-commons-codec >= 0:1.2
BuildRequires: jakarta-commons-jelly >= 0:1.0-5jpp
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: log4j >= 0:1.2.13
Requires: jakarta-commons-httpclient >= 0:3.0
Requires: apache-commons-codec >= 0:1.2
Requires: jakarta-commons-jelly >= 0:1.0-5jpp
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: log4j >= 0:1.2.13
Provides: %movname-plugin-jira = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-jira < 1.1-alt14
BuildArch: noarch

%description plugin-jira
%{summary}.

%package plugin-jnlp
Summary:        Optional jnlp plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-jnlp = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-jnlp < 1.1-alt14
BuildArch: noarch

%description plugin-jnlp
%{summary}.

%package plugin-junitdoclet
Summary:        Optional junitdoclet plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: junitdoclet-jdk14 >= 0:1.0.2
Requires: junitdoclet-jdk14 >= 0:1.0.2
Provides: %movname-plugin-junitdoclet = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-junitdoclet < 1.1-alt14
BuildArch: noarch

%description plugin-junitdoclet
%{summary}.

%package plugin-jxr
Summary:        Optional jxr plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: apache-commons-collections >= 0:3.1-1jpp
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: jakarta-oro >= 0:2.0.8
BuildRequires: junit >= 0:3.8.2
BuildRequires: maven-jxr >= 0:1.0
BuildRequires: plexus-utils >= 0:1.0.3
BuildRequires: velocity >= 0:1.5
Requires: apache-commons-collections >= 0:3.1-1jpp
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: jakarta-oro >= 0:2.0.8
Requires: maven-jxr >= 0:1.0
Requires: plexus-utils >= 0:1.0.3
Requires: velocity >= 0:1.5
Provides: %movname-plugin-jxr = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-jxr < 1.1-alt14
BuildArch: noarch

%description plugin-jxr
%{summary}.

%if %{RHEL4}==0
%package plugin-latex
Summary:        Optional latex plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: anttex >= 0.2-3jpp
BuildRequires: apache-commons-lang >= 0:2.0
Requires: anttex >= 0.2-3jpp
Requires: apache-commons-lang >= 0:2.0
Provides: %movname-plugin-latex = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-latex < 1.1-alt14
BuildArch: noarch

%description plugin-latex
%{summary}.
%endif

%if %{RHEL4}==0
%package plugin-latka
Summary:        Optional latka plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-httpclient >= 0:3.0
BuildRequires: jakarta-commons-jelly-tags-html >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
BuildRequires: jakarta-commons-latka >= 0:1.0
BuildRequires: jaxen >= 0:1.1
BuildRequires: jdom >= 0:1.0
BuildRequires: junit >= 0:3.8.2
BuildRequires: nekohtml >= 0:0.9.5
BuildRequires: regexp >= 0:1.3
BuildRequires: xalan-j2 >= 0:2.4.1
Requires: jakarta-commons-httpclient >= 0:3.0
Requires: jakarta-commons-jelly-tags-html >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Requires: jakarta-commons-latka >= 0:1.0
Requires: jaxen >= 0:1.1
Requires: jdom >= 0:1.0
Requires: junit >= 0:3.8.2
Requires: nekohtml >= 0:0.9.5
Requires: regexp >= 0:1.3
Requires: xalan-j2 >= 0:2.4.1
Provides: %movname-plugin-latka = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-latka < 1.1-alt14
BuildArch: noarch

%description plugin-latka
%{summary}.
%endif

%package plugin-license
Summary:        Optional license plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-license = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-license < 1.1-alt14
BuildArch: noarch

%description plugin-license
%{summary}.

%package plugin-linkcheck
Summary:        Optional linkcheck plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-beanutils >= 0:1.7.0
BuildRequires: apache-commons-codec >= 0:1.2
BuildRequires: apache-commons-collections >= 0:3.1-1jpp
BuildRequires: jakarta-commons-grant >= 0:1.0.b4
BuildRequires: jakarta-commons-httpclient >= 0:3.0
BuildRequires: jakarta-commons-jelly >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-ant >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
BuildRequires: apache-commons-lang >= 0:2.0
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: junit >= 0:3.8.2
BuildRequires: log4j >= 0:1.2.13
BuildRequires: maven-model >= 0:3.0.2
Requires: jakarta-commons-beanutils >= 0:1.7.0
Requires: apache-commons-codec >= 0:1.2
Requires: apache-commons-collections >= 0:3.1-1jpp
Requires: jakarta-commons-grant >= 0:1.0.b4
Requires: jakarta-commons-httpclient >= 0:3.0
Requires: jakarta-commons-jelly >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-ant >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Requires: apache-commons-lang >= 0:2.0
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: junit >= 0:3.8.2
Requires: log4j >= 0:1.2.13
Requires: maven-model >= 0:3.0.2
Provides: %movname-plugin-linkcheck = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-linkcheck < 1.1-alt14
BuildArch: noarch

%description plugin-linkcheck
%{summary}.

%package plugin-modello
Summary:        Optional modello plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: apache-jdo-2.0-api
BuildRequires: classworlds >= 0:1.1
BuildRequires: modello >= 0:1.0-0.a15
BuildRequires: plexus-container-default >= 0:1.0
BuildRequires: plexus-utils >= 0:1.0.3
BuildRequires: plexus-velocity >= 0:1.1.2
Requires: classworlds >= 0:1.1
Requires: modello >= 0:1.0-0.a15
Requires: plexus-container-default >= 0:1.0
Requires: plexus-utils >= 0:1.0.3
Requires: plexus-velocity >= 0:1.1.2
Provides: %movname-plugin-modello = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-modello < 1.1-alt14
BuildArch: noarch

%description plugin-modello
%{summary}.

%package plugin-multichanges
Summary:        Optional multichanges plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: junit >= 0:3.8.2
Requires: jakarta-commons-logging >= 0:1.0.4
Provides: %movname-plugin-multichanges = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-multichanges < 1.1-alt14
BuildArch: noarch

%description plugin-multichanges
%{summary}.

%package plugin-multiproject
Summary:        Optional multiproject plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-jelly-tags-velocity >= 0:1.0-5jpp
BuildRequires: maven-model >= 0:3.0.2
BuildRequires: velocity >= 0:1.5
Requires: jakarta-commons-jelly-tags-velocity >= 0:1.0-5jpp
BuildRequires: junit >= 0:3.8.2
Requires: maven-model >= 0:3.0.2
Requires: velocity >= 0:1.5
Provides: %movname-plugin-multiproject = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-multiproject < 1.1-alt14
BuildArch: noarch

%description plugin-multiproject
%{summary}.

%if %{RHEL4}==0
%package plugin-native
Summary:        Optional native plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: bcel5.3
BuildRequires: cpptasks >= 0:1.0
BuildRequires: junit >= 0:3.8.2
Requires: bcel5.3
Requires: cpptasks >= 0:1.0
Provides: %movname-plugin-native = %{epoch}:%{version}-%{release}
Obsoletes: pluginative < 1.1-alt14
BuildArch: noarch
#Provides: pluginative = %version-%release
#Provides: pluginative = 0:%version-%release

%description plugin-native
%{summary}.
%endif

%package plugin-nsis
Summary:        Optional nsis plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-nsis = %{epoch}:%{version}-%{release}
Obsoletes: pluginsis < 1.1-alt14
BuildArch: noarch
#Provides: pluginsis = %version-%release
#Provides: pluginsis = 0:%version-%release

%description plugin-nsis
%{summary}.

%if %{RHEL4}==0
%package plugin-pdf
Summary:        Optional pdf plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: excalibur-avalon-framework-api >= 0:4.3.1
BuildRequires: excalibur-avalon-framework-impl >= 0:4.3.1
BuildRequires: excalibur-avalon-logkit >= 0:2.2.1
BuildRequires: xmlgraphics-batik >= 0:1.6
BuildRequires: xmlgraphics-batik-rasterizer >= 0:1.6
BuildRequires: xmlgraphics-fop
BuildRequires: xalan-j2 >= 0:2.7.0
BuildRequires: xerces-j2 >= 0:2.7.1
BuildRequires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
BuildRequires: xml-commons-resolver11
Requires: excalibur-avalon-framework-api >= 0:4.3.1
Requires: excalibur-avalon-framework-impl >= 0:4.3.1
Requires: excalibur-avalon-logkit >= 0:2.2.1
Requires: xmlgraphics-batik >= 0:1.6
Requires: xmlgraphics-batik-rasterizer >= 0:1.6
Requires: xmlgraphics-fop
Requires: xalan-j2 >= 0:2.7.0
Requires: xerces-j2 >= 0:2.7.1
Requires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Requires: xml-commons-resolver11
Provides: %movname-plugin-pdf = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-pdf < 1.1-alt14
BuildArch: noarch

%description plugin-pdf
%{summary}.
%endif

%package plugin-pmd
Summary:        Optional pmd plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: backport-util-concurrent
BuildRequires: jaxen >= 0:1.1
BuildRequires: junit >= 0:3.8.2
BuildRequires: pmd >= 0:3.6
BuildRequires: asm2
Requires: backport-util-concurrent
Requires: jaxen >= 0:1.1
Requires: pmd >= 0:3.6
Requires: asm2
Provides: %movname-plugin-pmd = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-pmd < 1.1-alt14
BuildArch: noarch

%description plugin-pmd
%{summary}.

%package plugin-rar
Summary:        Optional rar plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-jelly-tags-util >= 0:1.0-5jpp
BuildRequires: jakarta-commons-logging
Requires: jakarta-commons-jelly-tags-util >= 0:1.0-5jpp
Provides: %movname-plugin-rar = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-rar < 1.1-alt14
BuildArch: noarch

%description plugin-rar
%{summary}.

%package plugin-release
Summary:        Optional release plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: dom4j >= 0:1.6.1
BuildRequires: apache-commons-io >= 0:1.2
BuildRequires: jakarta-commons-jelly >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-interaction >= 0:1.0-5jpp
BuildRequires: jaxen >= 0:1.1
BuildRequires: jline >= 0:0.9.5
BuildRequires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Requires: dom4j >= 0:1.6.1
Requires: apache-commons-io >= 0:1.2
Requires: jakarta-commons-jelly >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-interaction >= 0:1.0-5jpp
Requires: jaxen >= 0:1.1
Requires: jline >= 0:0.9.5
Requires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Provides: %movname-plugin-release = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-release < 1.1-alt14
BuildArch: noarch

%description plugin-release
%{summary}.

%package plugin-repository
Summary:        Optional repository plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-jelly-tags-util >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-util >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Provides: %movname-plugin-repository = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-repository < 1.1-alt14
BuildArch: noarch

%description plugin-repository
%{summary}.

%package plugin-scm
Summary:        Optional scm plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: classworlds >= 0:1.1
BuildRequires: dom4j >= 0:1.6.1
BuildRequires: apache-commons-io >= 0:1.2
BuildRequires: jakarta-commons-jelly >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-interaction >= 0:1.0-5jpp
BuildRequires: jaxen >= 0:1.1
BuildRequires: jline >= 0:0.9.5
BuildRequires: maven-scm >= 0:1.0
BuildRequires: plexus-container-default >= 0:1.0
BuildRequires: plexus-utils >= 0:1.0.3
Requires: classworlds >= 0:1.1
Requires: dom4j >= 0:1.6.1
Requires: apache-commons-io >= 0:1.2
Requires: jakarta-commons-jelly >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-interaction >= 0:1.0-5jpp
Requires: jaxen >= 0:1.1
Requires: jline >= 0:0.9.5
Requires: maven-scm >= 0:1.0
Requires: plexus-container-default >= 0:1.0
Requires: plexus-utils >= 0:1.0.3
Provides: %movname-plugin-scm = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-scm < 1.1-alt14
BuildArch: noarch

%description plugin-scm
%{summary}.

%package plugin-shell
Summary:        Optional shell plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-shell = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-shell < 1.1-alt14
BuildArch: noarch

%description plugin-shell
%{summary}.

%package plugin-site
Summary:        Optional site plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: ant17-commons-net
BuildRequires: apache-commons-lang >= 0:2.0
BuildRequires: jakarta-commons-net >= 0:1.4.1
BuildRequires: jakarta-oro >= 0:2.0.8
Requires: ant17-commons-net
Requires: apache-commons-lang >= 0:2.0
Requires: jakarta-commons-net >= 0:1.4.1
Requires: jakarta-oro >= 0:2.0.8
Provides: %movname-plugin-site = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-site < 1.1-alt14
BuildArch: noarch

%description plugin-site
%{summary}.

%package plugin-source
Summary:        Optional source plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-jelly >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-interaction >= 0:1.0-5jpp
BuildRequires: apache-commons-lang >= 0:2.0
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: jline >= 0:0.9.5
BuildRequires: junit >= 0:3.8.2
BuildRequires: maven-model >= 0:3.0.2
Requires: jakarta-commons-jelly >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-interaction >= 0:1.0-5jpp
Requires: apache-commons-lang >= 0:2.0
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: jline >= 0:0.9.5
Requires: maven-model >= 0:3.0.2
Provides: %movname-plugin-source = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-source < 1.1-alt14
BuildArch: noarch

%description plugin-source
%{summary}.

%package plugin-struts
Summary:        Optional struts plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-plugin-j2ee
BuildRequires: dom4j >= 0:1.6.1
BuildRequires: apache-commons-collections >= 0:3.1-1jpp
BuildRequires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
BuildRequires: apache-commons-lang >= 0:2.0
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: jaxen >= 0:1.1
BuildRequires: junit >= 0:3.8.2
BuildRequires: regexp >= 0:1.3
BuildRequires: xerces-j2 >= 0:2.7.1
BuildRequires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
BuildRequires: xml-commons-resolver11
Requires: dom4j >= 0:1.6.1
Requires: apache-commons-collections >= 0:3.1-1jpp
Requires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
Requires: apache-commons-lang >= 0:2.0
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: jaxen >= 0:1.1
Requires: junit >= 0:3.8.2
Requires: regexp >= 0:1.3
Requires: xerces-j2 >= 0:2.7.1
Requires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Requires: xml-commons-resolver11
Provides: %movname-plugin-struts = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-struts < 1.1-alt14
BuildArch: noarch

%description plugin-struts
%{summary}.

%package plugin-tasklist
Summary:        Optional tasklist plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-jelly >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-velocity >= 0:1.0-5jpp
BuildRequires: qdox161
BuildRequires: vdoclet >= 0:0.2
BuildRequires: velocity >= 0:1.5
Requires: jakarta-commons-jelly >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-velocity >= 0:1.0-5jpp
Requires: qdox161
Requires: vdoclet >= 0:0.2
Requires: velocity >= 0:1.5
Provides: %movname-plugin-tasklist = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-tasklist < 1.1-alt14
BuildArch: noarch

%description plugin-tasklist
%{summary}.

%package plugin-test
Summary:        Optional test plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: junit >= 0:3.8.2
BuildRequires: xerces-j2 >= 0:2.7.1
BuildRequires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
BuildRequires: xml-commons-resolver11
Requires: junit >= 0:3.8.2
Requires: xerces-j2 >= 0:2.7.1
Requires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Requires: xml-commons-resolver11
Provides: %movname-plugin-test = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-test < 1.1-alt14
BuildArch: noarch

%description plugin-test
%{summary}.

%if %{RHEL4}==0
%package plugin-tjdo
Summary:        Optional tjdo plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: tjdo >= 0:2.0
Requires: tjdo >= 0:2.0
Provides: %movname-plugin-tjdo = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-tjdo < 1.1-alt14
BuildArch: noarch

%description plugin-tjdo
%{summary}.
%endif

%package plugin-touchstone-partner
Summary:        Optional touchstone partner plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-touchstone-partner = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-touchstone-partner < 1.1-alt14
BuildArch: noarch

%description plugin-touchstone-partner
%{summary}.

%package plugin-touchstone
Summary:        Optional touchstone plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-touchstone = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-touchstone < 1.1-alt14
BuildArch: noarch

%description plugin-touchstone
%{summary}.

%if %{RHEL4}==0
%package plugin-uberjar
Summary:        Optional uberjar plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: classworlds >= 0:1.1
BuildRequires: jakarta-commons-jelly-tags-velocity >= 0:1.0-5jpp
BuildRequires: velocity >= 0:1.5
Requires: classworlds >= 0:1.1
Requires: jakarta-commons-jelly-tags-velocity >= 0:1.0-5jpp
Requires: velocity >= 0:1.5
Provides: %movname-plugin-uberjar = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-uberjar < 1.1-alt14
BuildArch: noarch

%description plugin-uberjar
%{summary}.
%endif

%if %{RHEL4}==0
%package plugin-vdoclet
Summary:        Optional vdoclet plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: excalibur-avalon-logkit >= 0:2.2.1
BuildRequires: apache-commons-collections >= 0:3.1-1jpp
BuildRequires: jakarta-commons-jelly >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-velocity >= 0:1.0-5jpp
BuildRequires: jakarta-oro >= 0:2.0.8
BuildRequires: qdox161
BuildRequires: vdoclet >= 0:0.2
BuildRequires: velocity >= 0:1.5
Requires: excalibur-avalon-logkit >= 0:2.2.1
Requires: apache-commons-collections >= 0:3.1-1jpp
Requires: jakarta-commons-jelly >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-velocity >= 0:1.0-5jpp
Requires: jakarta-oro >= 0:2.0.8
Requires: qdox161
Requires: vdoclet >= 0:0.2
Requires: velocity >= 0:1.5
Provides: %movname-plugin-vdoclet = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-vdoclet < 1.1-alt14
BuildArch: noarch

%description plugin-vdoclet
%{summary}.
%endif

%package plugin-war
Summary:        Optional war plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: apache-commons-lang >= 0:2.0
Requires: apache-commons-lang >= 0:2.0
Provides: %movname-plugin-war = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-war < 1.1-alt14
BuildArch: noarch

%description plugin-war
%{summary}.

%package plugin-webserver
Summary:        Optional webserver plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: ant17
BuildRequires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
Requires: ant17
Requires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
Provides: %movname-plugin-webserver = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-webserver < 1.1-alt14
BuildArch: noarch

%description plugin-webserver
%{summary}.

%package plugin-webstart
Summary:        Optional webstart plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %movname-plugin-webstart = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-webstart < 1.1-alt14
BuildArch: noarch

%description plugin-webstart
%{summary}.

%package plugin-wizard
Summary:        Optional wizard plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: jakarta-commons-jelly-tags-interaction >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-swing >= 0:1.0-5jpp
BuildRequires: jline >= 0:0.9.5
Requires: jakarta-commons-jelly-tags-interaction >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-swing >= 0:1.0-5jpp
Requires: jline >= 0:0.9.5
Provides: %movname-plugin-wizard = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-wizard < 1.1-alt14
BuildArch: noarch

%description plugin-wizard
%{summary}.

%package plugin-xdoc
Summary:        Optional xdoc plugin for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: dom4j >= 0:1.6.1
BuildRequires: forehead >= 0:1.0.b4
BuildRequires: jakarta-commons-jelly >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-fmt >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-velocity >= 0:1.0-5jpp
BuildRequires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
BuildRequires: apache-commons-lang >= 0:2.0
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: jaxen >= 0:1.1
BuildRequires: junit >= 0:3.8.2
BuildRequires: maven-model >= 0:3.0.2
BuildRequires: maven-scm >= 0:1.0
BuildRequires: velocity >= 0:1.5
BuildRequires: velocity-dvsl >= 0:1.0
BuildRequires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Requires: dom4j >= 0:1.6.1
Requires: forehead >= 0:1.0.b4
Requires: jakarta-commons-jelly >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-fmt >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-velocity >= 0:1.0-5jpp
Requires: jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
Requires: apache-commons-lang >= 0:2.0
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: jaxen >= 0:1.1
Requires: junit >= 0:3.8.2
Requires: maven-model >= 0:3.0.2
Requires: maven-scm >= 0:1.0
Requires: velocity >= 0:1.5
Requires: velocity-dvsl >= 0:1.0
Requires: xml-commons-jaxp-1.3-apis >= 0:1.3.03
Provides: %movname-plugin-xdoc = %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-xdoc < 1.1-alt14
BuildArch: noarch

%description plugin-xdoc
%{summary}.

# Disabled requirements

##BuildRequires:  clover >= 0:1.3.6
##BuildRequires:  java2html >= 0:1.2
##BuildRequires:  simian >= 0:1.9.1
##BuildRequires:  abbot

# Enabled requirements 

# (Even though commented out, this is the "global" pool of dependencies, it comes handy 
# when writing scripts to check dependencies)

##BuildRequires:  ant17
##BuildRequires:  ant17-commons-net >= 0:1.6.5
##BuildRequires:  ant17-junit
##BuildRequires:  antlr >= 0:2.7.6
##BuildRequires:  ant17-nodeps
##BuildRequires:  anttex >= 0.2-3jpp
##BuildRequires:  ant17-trax
##BuildRequires:  aspectj >= 0:1.2.1
##BuildRequires:  aspectwerkz >= 0:2.0
##BuildRequires:  batik >= 0:1.6
##BuildRequires:  batik-rasterizer >= 0:1.6
##BuildRequires:  bcel >= 0:5.1
##BuildRequires:  bsf
##BuildRequires:  castor0 >= 0:0.9.5
##BuildRequires:  checkstyle4 >= 0:4.4
##BuildRequires:  checkstyle4-optional >= 0:4.4
##BuildRequires:  classworlds >= 0:1.1
##BuildRequires:  cpptasks >= 0:1.0
##BuildRequires:  dom4j >= 0:1.6.1
##BuildRequires:  excalibur-avalon-framework-api >= 0:4.3.1
##BuildRequires:  excalibur-avalon-framework-impl >= 0:4.3.1
##BuildRequires:  excalibur-avalon-logkit >= 0:2.2.1
##BuildRequires:  fop >= 0:0.20.5
##BuildRequires:  fop < 0:0.93
##BuildRequires:  forehead >= 0:1.0.b4
##BuildRequires:  gnu-getopt >= 0:1.0.12
##BuildRequires:  gnu-regexp
##BuildRequires:  gnu-trove >= 0:1.0.2
##BuildRequires:  hivemind
##BuildRequires:  httpunit
##BuildRequires:  isorelax
##BuildRequires:  jaf
##BuildRequires:  jakarta-cactus
##BuildRequires:  jakarta-commons-beanutils >= 0:1.7.0
##BuildRequires:  jakarta-commons-beanutils16 >= 0:1.6.1
##BuildRequires:  jakarta-commons-cli10
##BuildRequires:  jakarta-commons-codec >= 0:1.2
##BuildRequires:  jakarta-commons-collections >= 0:3.1-1jpp
##BuildRequires:  jakarta-commons-digester
##BuildRequires:  jakarta-commons-fileupload
##BuildRequires:  jakarta-commons-grant >= 0:1.0.b4
##BuildRequires:  jakarta-commons-graph >= 0:0.8.1
##BuildRequires:  jakarta-commons-httpclient >= 0:3.0
##BuildRequires:  jakarta-commons-io >= 0:1.2
##BuildRequires:  jakarta-commons-jelly >= 0:1.0-5jpp
##BuildRequires:  jakarta-commons-jelly-tags-ant >= 0:1.0-5jpp
##BuildRequires:  jakarta-commons-jelly-tags-antlr >= 0:1.0-5jpp
##BuildRequires:  jakarta-commons-jelly-tags-define
##BuildRequires:  jakarta-commons-jelly-tags-fmt >= 0:1.0-5jpp
##BuildRequires:  jakarta-commons-jelly-tags-html >= 0:1.0-5jpp
##BuildRequires:  jakarta-commons-jelly-tags-interaction >= 0:1.0-5jpp
##BuildRequires:  jakarta-commons-jelly-tags-jsl >= 0:1.0-5jpp
##BuildRequires:  jakarta-commons-jelly-tags-log >= 0:1.0-5jpp
##BuildRequires:  jakarta-commons-jelly-tags-swing >= 0:1.0-5jpp
##BuildRequires:  jakarta-commons-jelly-tags-util >= 0:1.0-5jpp
##BuildRequires:  jakarta-commons-jelly-tags-velocity >= 0:1.0-5jpp
##BuildRequires:  jakarta-commons-jelly-tags-xml >= 0:1.0-5jpp
##BuildRequires:  jakarta-commons-jexl >= 0:1.0
##BuildRequires:  jakarta-commons-lang >= 0:2.0
##BuildRequires:  jakarta-commons-latka >= 0:1.0
##BuildRequires:  jakarta-commons-logging >= 0:1.0.4
##BuildRequires:  jakarta-commons-net >= 0:1.4.1
##BuildRequires:  jakarta-commons-validator
##BuildRequires:  jakarta-oro >= 0:2.0.8
##BuildRequires:  jakarta-taglibs-standard
##BuildRequires:  jalopy >= 0:1.0-0.b11
##BuildRequires:  jalopy-ant >= 0:1.0-0.b11
##BuildRequires:  javacc3 >= 0:3.2
##BuildRequires:  javacvs-lib >= 0:3.6
##BuildRequires:  javassist
##BuildRequires:  jaxen >= 0:1.1
##BuildRequires:  jboss4-j2ee
##BuildRequires:  jboss4-server
##BuildRequires:  jcoverage >= 0:1.0.5
##BuildRequires:  jdepend >= 0:2.9.1
##BuildRequires:  jdepend22 >= 2.2-2jpp
##BuildRequires:  jdiff >= 0:1.0.9
##BuildRequires:  jdom >= 0:1.0
##BuildRequires:  jetty5
##BuildRequires:  jext
##BuildRequires:  jline >= 0:0.9.5
##BuildRequires:  jpackage-utils >= 0:1.7.2
##BuildRequires:  jrexx >= 0:1.1.1
##BuildRequires:  jsch >= 0:0.1.27
##BuildRequires:  jtidy
##BuildRequires:  junit >= 0:3.8.2
##BuildRequires:  junitdoclet-jdk14 >= 0:1.0.2
##BuildRequires:  log4j >= 0:1.2.13
##BuildRequires:  maven-jxr >= 0:1.0
##BuildRequires:  maven-model >= 0:3.0.2
##BuildRequires:  maven-scm >= 0:1.0
##BuildRequires:  maven-wagon >= 0:1.0-0.b2
##BuildRequires:  modello >= 0:1.0-0.a8.6jpp
##BuildRequires:  msv-msv
##BuildRequires:  msv-xsdlib
##BuildRequires:  nekohtml >= 0:0.9.5
##BuildRequires:  ognl
##BuildRequires:  plexus-container-default >= 0:1.0
##BuildRequires:  plexus-utils >= 0:1.0.3
##BuildRequires:  plexus-velocity >= 0:1.1.2
##BuildRequires:  pmd >= 0:3.6
##BuildRequires:  qdox >= 0:1.6.1
##BuildRequires:  regexp >= 0:1.3
##BuildRequires:  relaxngDatatype
##BuildRequires:  servletapi4
##BuildRequires:  servletapi5
##BuildRequires:  struts
##BuildRequires:  strutstestcase
##BuildRequires:  tapestry
##BuildRequires:  tjdo >= 0:2.0
##BuildRequires:  tomcat5-jasper
##BuildRequires:  tomcat5-servlet-2.4-api
##BuildRequires:  vdoclet >= 0:0.2
##BuildRequires:  velocity >= 0:1.5
##BuildRequires:  velocity-dvsl >= 0:1.0
##BuildRequires:  velocity-tools >= 0:1.3
##BuildRequires:  werkz >= 1.0-0.b10.5jpp
##BuildRequires:  xalan-j2 >= 0:2.7.0
##BuildRequires:  xdoclet
##BuildRequires:  xdoclet-maven-plugin
##BuildRequires:  xerces-j2 >= 0:2.7.1
##BuildRequires:  xjavadoc
##BuildRequires:  xml-commons-jaxp-1.3-apis >= 0:1.3.03
##BuildRequires:  xml-commons-resolver11
##BuildRequires:  xpp3 >= 0:1.1.3


%description
Maven is a Java project management and project 
comprehension tool. Maven is based on the concept 
of a project object model (POM) in that all the 
artifacts produced by Maven are a result of 
consulting a well defined model for your project. 
Builds, documentation, source metrics, and source 
cross-references are all controlled by your POM. 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch
Obsoletes: maven-javadoc < 1.1-alt14

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch
Obsoletes: maven-manual < 1.1-alt14

%description    manual
%{summary}.


%prep
%setup -q -n %oldname-%version

# maven-jelly-tags now from main tarball

# here are the maven-plugins
(cd ..
rm -rf maven-plugins
gzip -dc %{SOURCE2} | tar -xf -
)
# here are the historical maven-plugins
(cd ..
rm -rf maven-plugins-sandbox
gzip -dc %{SOURCE7} | tar -xf -
)
cp %{SOURCE3} build-maven-library
chmod 755 build-maven-library
cp %{SOURCE300} build-maven-library-build
chmod 755 build-maven-library-build
#
cp %{SOURCE6} src/test/java/org/apache/maven/MavenUtilsTest.java
rm -rf ../maven-plugins/plugin/src/test/*

# here are the poms
gzip -dc %{SOURCE8} | tar -xf -

%patch0 -b .sav0
pushd ../maven-plugins-sandbox
%patch1 -b .sav1 -p2
popd
pushd ../maven-plugins
%patch2 -b .sav2 -p2
popd
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
#%patch6 -b .sav6
pushd ../maven-plugins
%patch7 -b .sav7 -p2
%patch8 -b .sav8 -p2
%patch9 -b .sav9 -p2
popd

%if %{bootstrap}
# dashboard needs sf-findbugs-maven-plugin and sf-javancss-maven-plugin
rm -rf ../maven-plugins/dashboard
rm maven-poms/maven-dashboard*
# also postpone genapp
rm -rf ../maven-plugins/genapp
rm maven-poms/maven-genapp*
%endif

# convenience move: jcoverage needed for dashboard
mv ../maven-plugins-sandbox/jcoverage ../maven-plugins

# Set up the exclusion list
%if %{RHEL4}==0
%if %{NONFREE}==1
(cd ../%{oldname}-%{version}
echo "maven.plugins.excludes = examples/**,touchstone/**,touchstone-partner/**,plugin-parent/**,itest/**,ashkelon/**,clover/**,simian/**,abbot/**,latka/**" >> project.properties
)
%else
(cd ../%{oldname}-%{version}
echo "maven.plugins.excludes = examples/**,touchstone/**,touchstone-partner/**,plugin-parent/**,itest/**,ashkelon/**,changelog/**,clover/**,simian/**,tjdo/**,uberjar/**,abbot/**,latka/**" >> project.properties
)
%endif
%else
(cd ../%{oldname}-%{version}
echo "maven.plugins.excludes = examples/**,touchstone/**,touchstone-partner/**,plugin-parent/**,itest/**,abbot/**,ashkelon/**,aspectj/**,aspectwerkz/**,changelog/**,clover/**,jalopy/**,jdeveloper/**,jdiff/**,jetty/**,latex/**,latka/**,native/**,pdf/**,simian/**,tjdo/**,uberjar/**,vdoclet/**" >> project.properties
)
%endif

# plexus-* have component-api.jar no more, use containers-container-default.jar instead.
sed -i 's,<jar>plexus/component-api.jar</jar>,<jar>plexus/containers-container-default.jar</jar>,' ../maven-plugins/scm/project.xml
sed -i 's,<jar>plexus/containers-component-api.jar</jar>,<jar>plexus/containers-container-default.jar</jar>,' ../maven-plugins/modello/project.xml
pushd ../maven-plugins
%patch33 -p2
popd

%build
mkdir -p home/lib/endorsed
export MAVEN_HOME=$(pwd)/home
./build-maven-library-build

mkdir -p repository/maven/jars
mkdir -p repository/maven/plugins
mkdir -p repository/JPP
mkdir -p repository/javadoc/jars
ln -s %{_javadir} repository/JPP/jars
mkdir -p repository/JPP/plugins
pushd repository/JPP/plugins
ln -sf /usr/share/java/maven1-plugins/maven-findbugs-plugin.jar
ln -sf /usr/share/java/maven1-plugins/maven-javancss-plugin.jar
mkdir xdoclet
pushd xdoclet
ln -sf /usr/share/java/xdoclet/maven-xdoclet-plugin.jar .
popd
popd
rm -rf ../maven-plugins/eclipse/src/plugin-test/maintest

mkdir -p repository/struts/tlds
pushd repository/struts/tlds
ln -sf /usr/share/struts/struts-bean.tld struts-bean-1.1.tld
ln -sf /usr/share/struts/struts-html.tld struts-html-1.1.tld
ln -sf /usr/share/struts/struts-logic.tld struts-logic-1.1.tld
popd

#Needed because in the bootstrap process the value for $JAVA_HOME is required for build to proceed.
#export JAVA_HOME=%{_jvmdir}/java-1.6.0
export JAVA_HOME=%{_jvmdir}/java

# jellydoc used to have a dependency on tools.jar, which has been removed since all standard 
# jdks have tools.jar available to them.

ln -s ${JAVA_HOME}/lib/tools.jar repository/javadoc/jars/tools.jar

cp %{SOURCE5} build.xml
export OPT_JAR_LIST="ant17-launcher ant17/ant17-junit junit"
export ANT_OPTS="-Xmx256m"

(
cd repository/maven/jars
ln -s ../../../home/plugins/maven-j2ee-plugin-1.6-SNAPSHOT.jar maven-j2ee-plugin.jar
ln -s ../../../home/plugins/maven-changes-plugin-1.7.jar
)
(
cd repository/maven/plugins
ln -s ../../../home/plugins/maven-jcoverage-plugin-1.1-SNAPSHOT.jar maven-jcoverage-plugin-1.0.9.jar
)

ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first
cp target/maven-jelly-tags-1.0.1.jar repository/maven/jars
(cd repository/maven/jars
ln -s maven-jelly-tags-1.0.1.jar maven-jelly-tags.jar
)

rm -rf ../maven-plugins/genapp/src/plugin-test/templatesTest/
rm -rf ../maven-plugins/modello/src/plugin-test/

export MAVEN_HOME=$(pwd)/home

export MAVEN_HOME_LOCAL=$(pwd)

echo "maven.get.jars.baseUrl = file:"$(pwd)/repository >> project.properties

ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
    -Dorg.xml.sax.driver=org.apache.xerces.parsers.SAXParser \
    -Dmaven.bootstrap.test.plugins=false \
    -f build-bootstrap.xml

# plugins
cd ../maven-plugins
$MAVEN_HOME/bin/maven -o -Dmaven.repo.remote=file:$MAVEN_HOME_LOCAL/repository

# plugins-sandbox
cd ../maven-plugins-sandbox
$MAVEN_HOME/bin/maven -o -Dmaven.repo.remote=file:$MAVEN_HOME_LOCAL/repository

cd ../%{oldname}-%{version}
$MAVEN_HOME/bin/maven -o javadoc:generate
$MAVEN_HOME/bin/maven -o xdoc:transform


# Maven build is done. Remove that J2EE plugin that we put in there for the struts plugin to build.
(
cd repository/maven/jars
rm -f maven-j2ee-plugin.jar
)

%install

# /usr/bin/maven
install -dm 755 $RPM_BUILD_ROOT%{_bindir}
install -pm 755 %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/maven

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

# maven.jar to _javadir
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 home/lib/maven.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
%add_to_maven_depmap %{oldname} %{oldname} %{version} JPP %{name}
install -pm 644 maven-poms/%{oldname}-%{version}.pom \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

install -pm 644 repository/maven/jars/maven-jelly-tags-1.0.1.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven1-jelly-tags-1.0.1.jar
ln -s maven1-jelly-tags-1.0.1.jar $RPM_BUILD_ROOT%{_javadir}/maven1-jelly-tags.jar
%add_to_maven_depmap %{oldname} %{oldname}-jelly-tags %{version} JPP %{name}-jelly-tags
install -pm 644 maven-poms/%{oldname}-jelly-tags-%{ver_jelly_tags}.pom \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-jelly-tags.pom

# maven.home
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
cp -p home/bin/* $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
cp -p build-maven-library $RPM_BUILD_ROOT%{_datadir}/%{name}/bin

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/lib

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins
cp -p home/plugins/*.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins
for p in maven-poms/maven-*-plugin*.pom; do
  b=$(basename $p);
  n=$(expr $b : '\(maven-.*-plugin\).*');
  v=$(expr $b : 'maven-.*-plugin-\(.*\)\.pom');
%add_to_maven_depmap %{oldname} $n $v JPP/maven1-plugins $n
  install -pm 644 $p \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.maven1-plugins-$n.pom
done
mv $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-junit-doclet-plugin.pom \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-junitdoclet-plugin.pom \

install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}-plugins
pushd $RPM_BUILD_ROOT%{_javadir}/%{name}-plugins
for j in $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/*.jar; do
        n=$(expr $(basename $j) : '\(maven-.*-plugin\).*\.jar')
        ln -sf %{_datadir}/%{name}/plugins/$(basename $j) $n.jar
done
popd

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/repository

# Main JPP repo
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/repository/JPP
ln -s %{_javadir} $RPM_BUILD_ROOT%{_datadir}/%{name}/repository/JPP/jars

# JVMJAR repo
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/repository/JPP-jvmjar
ln -s %{_jvmjardir} $RPM_BUILD_ROOT%{_datadir}/%{name}/repository/JPP-jvmjar/jars

# JNIJAR repo
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/repository/JPP-jnijar
ln -s %{_jnidir} $RPM_BUILD_ROOT%{_datadir}/%{name}/repository/JPP-jnijar/jars

cp -pr repository/maven $RPM_BUILD_ROOT%{_datadir}/%{name}/repository
cp -pr repository/javadoc $RPM_BUILD_ROOT%{_datadir}/%{name}/repository
ln -s maven $RPM_BUILD_ROOT%{_datadir}/%{name}/repository/maven1

# For backward compatibility, create a maven-1.0 symlink
ln -s %{_datadir}/%{name} $RPM_BUILD_ROOT%{_datadir}/%{name}-1.0

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf target/docs/apidocs

# manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# clean up saved files
find $RPM_BUILD_ROOT -name "*.sav?" -exec rm {} \;

#broken symlinks (jpp 5.0/6.0 to report)
#/usr/share/maven/repository/maven/jars/maven-changes-plugin-1.7.jar
#/usr/share/maven/repository/maven/plugins/maven-jcoverage-plugin-1.0.9.jar
pushd %buildroot/usr/share/%{name}
ln -sf ../../../plugins/maven-changes-plugin-1.7.jar repository/maven/jars/maven-changes-plugin-1.7.jar
ln -sf ../../../plugins/maven-jcoverage-plugin-1.1-SNAPSHOT.jar repository/maven/plugins/maven-jcoverage-plugin-1.0.9.jar
popd

mkdir -p $RPM_BUILD_ROOT`dirname /etc/mavenrc`
touch $RPM_BUILD_ROOT/etc/mavenrc

### Added or move manually
# moved from post
ln -s %{_javadir}/%{name}-plugins %buildroot%{_datadir}/%{name}/repository/JPP/plugins

# moved from post/killed %preun
export MAVEN_HOME=%buildroot%{_datadir}/%{name}
$MAVEN_HOME/bin/build-maven-library

# compat symlinks due to move
pushd %buildroot%{_datadir}/%{name}/lib
ln -sf maven1.jar maven.jar
popd
pushd %buildroot%{_datadir}/%{name}/repository/maven/jars
ln -s maven.jar maven1.jar
ln -s maven.jar maven1-1.1.jar
popd

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun
if [ -d %{_datadir}/%{name}/plugins ] ; then rmdir --ignore-fail-on-non-empty %{_datadir}/%{name}/plugins >& /dev/null; fi
if [ -d %{_datadir}/%{name} ] ; then rmdir --ignore-fail-on-non-empty %{_datadir}/%{name} >& /dev/null; fi

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_bindir}/maven
%{_javadir}/*.jar
%dir %{_javadir}/%{name}-plugins
%{_datadir}/%{name}/bin
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/repository
%{_datadir}/%{name}-1.0
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_datadir}/maven2/poms/JPP-%{name}-jelly-tags.pom
%{_mavendepmapfragdir}
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}
#%config(noreplace,missingok) /etc/mavenrc


%files plugins-base
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-ant-plugin*.jar
%{_javadir}/%{name}-plugins/maven-ant-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-ant-plugin.pom
%{_datadir}/%{name}/plugins/maven-artifact-plugin*.jar
%{_javadir}/%{name}-plugins/maven-artifact-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-artifact-plugin.pom
%{_datadir}/%{name}/plugins/maven-clean-plugin*.jar
%{_javadir}/%{name}-plugins/maven-clean-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-clean-plugin.pom
%{_datadir}/%{name}/plugins/maven-console-plugin*.jar
%{_javadir}/%{name}-plugins/maven-console-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-console-plugin.pom
%{_datadir}/%{name}/plugins/maven-jar-plugin*.jar
%{_javadir}/%{name}-plugins/maven-jar-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-jar-plugin.pom
%{_datadir}/%{name}/plugins/maven-java-plugin*.jar
%{_javadir}/%{name}-plugins/maven-java-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-java-plugin.pom
%{_datadir}/%{name}/plugins/maven-javacc-plugin*.jar
%{_javadir}/%{name}-plugins/maven-javacc-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-javacc-plugin.pom
%{_datadir}/%{name}/plugins/maven-javadoc-plugin*.jar
%{_javadir}/%{name}-plugins/maven-javadoc-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-javadoc-plugin.pom
%{_datadir}/%{name}/plugins/maven-junit-report-plugin*.jar
%{_javadir}/%{name}-plugins/maven-junit-report-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-junit-report-plugin.pom
%{_datadir}/%{name}/plugins/maven-plugin-plugin*.jar
%{_javadir}/%{name}-plugins/maven-plugin-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-plugin-plugin.pom
%{_datadir}/%{name}/plugins/maven-pom-plugin*.jar
%{_javadir}/%{name}-plugins/maven-pom-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-pom-plugin.pom

%if 0
%files plugin-abbot
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-abbot-plugin*.jar
%{_javadir}/%{name}-plugins/maven-abbot-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-abbot-plugin.pom
%endif

%files plugin-announcement
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-announcement-plugin*.jar
%{_javadir}/%{name}-plugins/maven-announcement-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-announcement-plugin.pom

%files plugin-antlr
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-antlr-plugin*.jar
%{_javadir}/%{name}-plugins/maven-antlr-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-antlr-plugin.pom

%files plugin-appserver
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-appserver-plugin*.jar
%{_javadir}/%{name}-plugins/maven-appserver-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-appserver-plugin.pom

%if %{RHEL4}==0
%files plugin-aspectj
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-aspectj-plugin*.jar
%{_javadir}/%{name}-plugins/maven-aspectj-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-aspectj-plugin.pom
%endif

%if %{RHEL4}==0
%files plugin-aspectwerkz
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-aspectwerkz-plugin*.jar
%{_javadir}/%{name}-plugins/maven-aspectwerkz-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-aspectwerkz-plugin.pom
%endif

%files plugin-cactus-jcoverage-integration
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-cactus-jcoverage-integration-plugin*.jar
%{_javadir}/%{name}-plugins/maven-cactus-jcoverage-integration-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-cactus-jcoverage-integration-plugin.pom

%files plugin-caller
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-caller-plugin*.jar
%{_javadir}/%{name}-plugins/maven-caller-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-caller-plugin.pom

%files plugin-castor
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-castor-plugin*.jar
%{_javadir}/%{name}-plugins/maven-castor-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-castor-plugin.pom

%if %{RHEL4}==0
%files plugin-changelog
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-changelog-plugin*.jar
%{_javadir}/%{name}-plugins/maven-changelog-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-changelog-plugin.pom
%endif

%files plugin-changes
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-changes-plugin*.jar
%{_javadir}/%{name}-plugins/maven-changes-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-changes-plugin.pom

%files plugin-checkstyle
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-checkstyle-plugin*.jar
%{_javadir}/%{name}-plugins/maven-checkstyle-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-checkstyle-plugin.pom

%files plugin-cruisecontrol
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-cruisecontrol-plugin*.jar
%{_javadir}/%{name}-plugins/maven-cruisecontrol-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-cruisecontrol-plugin.pom

%files plugin-developer-activity
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-developer-activity-plugin*.jar
%{_javadir}/%{name}-plugins/maven-developer-activity-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-developer-activity-plugin.pom

%if !%{bootstrap}
%files plugin-dashboard
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-dashboard-plugin*.jar
%{_javadir}/%{name}-plugins/maven-dashboard-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-dashboard-plugin.pom
%endif

%files plugin-dist
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-dist-plugin*.jar
%{_javadir}/%{name}-plugins/maven-dist-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-dist-plugin.pom

%files plugin-docbook
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-docbook-plugin*.jar
%{_javadir}/%{name}-plugins/maven-docbook-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-docbook-plugin.pom

%files plugin-ear
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-ear-plugin*.jar
%{_javadir}/%{name}-plugins/maven-ear-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-ear-plugin.pom

%files plugin-eclipse
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-eclipse-plugin*.jar
%{_javadir}/%{name}-plugins/maven-eclipse-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-eclipse-plugin.pom

%files plugin-ejb
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-ejb-plugin*.jar
%{_javadir}/%{name}-plugins/maven-ejb-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-ejb-plugin.pom

%files plugin-faq
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-faq-plugin*.jar
%{_javadir}/%{name}-plugins/maven-faq-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-faq-plugin.pom

%files plugin-file-activity
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-file-activity-plugin*.jar
%{_javadir}/%{name}-plugins/maven-file-activity-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-file-activity-plugin.pom

%if ! %{bootstrap}
%files plugin-genapp
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-genapp-plugin*.jar
%{_javadir}/%{name}-plugins/maven-genapp-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-genapp-plugin.pom
%endif

%files plugin-gump
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-gump-plugin*.jar
%{_javadir}/%{name}-plugins/maven-gump-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-gump-plugin.pom

%files plugin-html2xdoc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-html2xdoc-plugin*.jar
%{_javadir}/%{name}-plugins/maven-html2xdoc-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-html2xdoc-plugin.pom

%files plugin-idea
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-idea-plugin*.jar
%{_javadir}/%{name}-plugins/maven-idea-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-idea-plugin.pom

%files plugin-itest
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-itest-plugin*.jar
%{_javadir}/%{name}-plugins/maven-itest-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-itest-plugin.pom

%files plugin-j2ee
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-j2ee-plugin*.jar
%{_javadir}/%{name}-plugins/maven-j2ee-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-j2ee-plugin.pom

%if %{RHEL4}==0
%files plugin-jalopy
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-jalopy-plugin*.jar
%{_javadir}/%{name}-plugins/maven-jalopy-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-jalopy-plugin.pom
%endif

%files plugin-jboss
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-jboss-plugin*.jar
%{_javadir}/%{name}-plugins/maven-jboss-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-jboss-plugin.pom

%files plugin-jbuilder
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-jbuilder-plugin*.jar
%{_javadir}/%{name}-plugins/maven-jbuilder-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-jbuilder-plugin.pom

%files plugin-jcoverage
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-jcoverage-plugin*.jar
%{_javadir}/%{name}-plugins/maven-jcoverage-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-jcoverage-plugin.pom

%files plugin-jdee
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-jdee-plugin*.jar
%{_javadir}/%{name}-plugins/maven-jdee-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-jdee-plugin.pom

%files plugin-jdepend
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-jdepend-plugin*.jar
%{_javadir}/%{name}-plugins/maven-jdepend-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-jdepend-plugin.pom

%if %{RHEL4}==0
%files plugin-jdeveloper
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-jdeveloper-plugin*.jar
%{_javadir}/%{name}-plugins/maven-jdeveloper-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-jdeveloper-plugin.pom
%endif

%if %{RHEL4}==0
%files plugin-jdiff
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-jdiff-plugin*.jar
%{_javadir}/%{name}-plugins/maven-jdiff-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-jdiff-plugin.pom
%endif

%files plugin-jellydoc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-jellydoc-plugin*.jar
%{_javadir}/%{name}-plugins/maven-jellydoc-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-jellydoc-plugin.pom

%if %{RHEL4}==0
%files plugin-jetty
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-jetty-plugin*.jar
%{_javadir}/%{name}-plugins/maven-jetty-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-jetty-plugin.pom
%endif

%files plugin-jira
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-jira-plugin*.jar
%{_javadir}/%{name}-plugins/maven-jira-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-jira-plugin.pom

%files plugin-jnlp
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-jnlp-plugin*.jar
%{_javadir}/%{name}-plugins/maven-jnlp-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-jnlp-plugin.pom

%files plugin-junitdoclet
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-junitdoclet-plugin*.jar
%{_javadir}/%{name}-plugins/maven-junitdoclet-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-junitdoclet-plugin.pom

%files plugin-jxr
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-jxr-plugin*.jar
%{_javadir}/%{name}-plugins/maven-jxr-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-jxr-plugin.pom

%if %{RHEL4}==0
%files plugin-latex
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-latex-plugin*.jar
%{_javadir}/%{name}-plugins/maven-latex-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-latex-plugin.pom
%endif

%files plugin-latka
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-latka-plugin*.jar
%{_javadir}/%{name}-plugins/maven-latka-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-latka-plugin.pom

%files plugin-license
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-license-plugin*.jar
%{_javadir}/%{name}-plugins/maven-license-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-license-plugin.pom

%files plugin-linkcheck
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-linkcheck-plugin*.jar
%{_javadir}/%{name}-plugins/maven-linkcheck-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-linkcheck-plugin.pom

%files plugin-modello
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-modello-plugin*.jar
%{_javadir}/%{name}-plugins/maven-modello-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-modello-plugin.pom

%files plugin-multichanges
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-multichanges-plugin*.jar
%{_javadir}/%{name}-plugins/maven-multichanges-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-multichanges-plugin.pom

%files plugin-multiproject
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-multiproject-plugin*.jar
%{_javadir}/%{name}-plugins/maven-multiproject-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-multiproject-plugin.pom

%if %{RHEL4}==0
%files plugin-native
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-native-plugin*.jar
%{_javadir}/%{name}-plugins/maven-native-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-native-plugin.pom
%endif

%files plugin-nsis
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-nsis-plugin*.jar
%{_javadir}/%{name}-plugins/maven-nsis-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-nsis-plugin.pom

%if %{RHEL4}==0
%files plugin-pdf
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-pdf-plugin*.jar
%{_javadir}/%{name}-plugins/maven-pdf-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-pdf-plugin.pom
%endif

%files plugin-pmd
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-pmd-plugin*.jar
%{_javadir}/%{name}-plugins/maven-pmd-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-pmd-plugin.pom

%files plugin-rar
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-rar-plugin*.jar
%{_javadir}/%{name}-plugins/maven-rar-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-rar-plugin.pom

%files plugin-release
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-release-plugin*.jar
%{_javadir}/%{name}-plugins/maven-release-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-release-plugin.pom

%files plugin-repository
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-repository-plugin*.jar
%{_javadir}/%{name}-plugins/maven-repository-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-repository-plugin.pom

%files plugin-scm
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-scm-plugin*.jar
%{_javadir}/%{name}-plugins/maven-scm-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-scm-plugin.pom

%files plugin-shell
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-shell-plugin*.jar
%{_javadir}/%{name}-plugins/maven-shell-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-shell-plugin.pom

%files plugin-site
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-site-plugin*.jar
%{_javadir}/%{name}-plugins/maven-site-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-site-plugin.pom

%files plugin-source
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-source-plugin*.jar
%{_javadir}/%{name}-plugins/maven-source-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-source-plugin.pom

%files plugin-struts
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-struts-plugin*.jar
%{_javadir}/%{name}-plugins/maven-struts-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-struts-plugin.pom

%files plugin-tasklist
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-tasklist-plugin*.jar
%{_javadir}/%{name}-plugins/maven-tasklist-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-tasklist-plugin.pom

%files plugin-test
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-test-plugin*.jar
%{_javadir}/%{name}-plugins/maven-test-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-test-plugin.pom

%if %{RHEL4}==0
%files plugin-tjdo
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-tjdo-plugin*.jar
%{_javadir}/%{name}-plugins/maven-tjdo-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-tjdo-plugin.pom
%endif

%files plugin-touchstone-partner
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-touchstone-partner-plugin*.jar
%{_javadir}/%{name}-plugins/maven-touchstone-partner-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-touchstone-partner-plugin.pom

%files plugin-touchstone
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-touchstone-plugin*.jar
%{_javadir}/%{name}-plugins/maven-touchstone-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-touchstone-plugin.pom

%if %{RHEL4}==0
%files plugin-uberjar
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-uberjar-plugin*.jar
%{_javadir}/%{name}-plugins/maven-uberjar-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-uberjar-plugin.pom
%endif

%if %{RHEL4}==0
%files plugin-vdoclet
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-vdoclet-plugin*.jar
%{_javadir}/%{name}-plugins/maven-vdoclet-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-vdoclet-plugin.pom
%endif

%files plugin-war
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-war-plugin*.jar
%{_javadir}/%{name}-plugins/maven-war-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-war-plugin.pom

%files plugin-webserver
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-webserver-plugin*.jar
%{_javadir}/%{name}-plugins/maven-webserver-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-webserver-plugin.pom

%files plugin-webstart
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-webstart-plugin*.jar
%{_javadir}/%{name}-plugins/maven-webstart-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-webstart-plugin.pom

%files plugin-wizard
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-wizard-plugin*.jar
%{_javadir}/%{name}-plugins/maven-wizard-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-wizard-plugin.pom

%files plugin-xdoc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/maven-xdoc-plugin*.jar
%{_javadir}/%{name}-plugins/maven-xdoc-plugin.jar
%{_datadir}/maven2/poms/JPP.maven1-plugins-maven-xdoc-plugin.pom

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt18_9jpp6
- fixed build

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt17_9jpp6
- added compat symlinks

* Mon Mar 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt16_9jpp6
- moved to /usr/share/maven1 to avoid conflicts with maven3

* Sun Mar 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt15_9jpp6
- test build w/o noarch for #27053

* Mon Aug 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt14_9jpp6
- added Obsoletes: on maven subpackages

* Mon Aug 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt13_9jpp6
- renamed to maven1

* Mon Aug 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt12_9jpp6
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Sun Aug 28 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt12_9jpp6
- added maven 1 provides

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt11_9jpp6
- fixed build

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt10_9jpp6
- jpp 6 release

* Sun Dec 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt10_7jpp5
- fixed checkstyle plugin dependency

* Fri Sep 24 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt9_7jpp5
- rebuild with new maven-model; misc fixes for 2.0.8 upgrade

* Fri May 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt8_7jpp5
- java6 adaptation

* Wed Apr 01 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt7_7jpp5
- new jpp release

* Thu Mar 19 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt7_6jpp5
- fixed build

* Thu Nov 27 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt7_3jpp5
- fix for pmd that requires objectweb-asm = 3.0

* Tue Sep 23 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt6_3jpp5
- fixes for cli10

* Mon Apr 28 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt6_3jpp1.7
- Add jakarta-commons-jelly-tags-interaction (B)R

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt6_2jpp1.7
- updated to new jpackage release
- final version 1.1
- enabled eclipse plugin
- enabled dashboard plugin
- enabled aspectj plugin

* Sun Dec 16 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt6_0.beta3.2jpp1.7
- enabled jalopy plugin
- branch 4.0 compatible build

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt5_0.beta3.2jpp1.7
- enabled release, modello, tjdo plugins

* Tue Nov 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt4_0.beta3.2jpp1.7
- fixed misdependency on java-1.4.2-sun-devel with yes,nosymlinks instead of AutoReq: nosh

* Mon Nov 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_0.beta3.2jpp1.7
- fixed misdependency on java-1.4.2-sun-devel with yes,noshebang,noshell,nosymlink instead of AutoReq: nosh

* Fri Jul 20 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_0.beta3.2jpp1.7
- added requires for compatible environment:
  jakarta-commons-digester
  jakarta-commons-betwixt
  jakarta-commons-jelly-tags-interaction
  xml-commons-which

* Tue Jul 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_0.beta3.2jpp1.7
- converted from JPackage by jppimport script
- note: bootstrapped version
