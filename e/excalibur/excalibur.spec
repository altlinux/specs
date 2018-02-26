BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support
#def_with jdk6
%bcond_without jdk6
%bcond_without maven
%bcond_without repolib

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


%define rsvn r508111
%define rdate 15022007
%define main_version 1.0
%define components_version 2.2.1
%define containerkit_version 2.2.1
%define cornerstone_version 2.2.1
%define excalidep_version 2.2.1
%define fortress_version 1.3.1
%define framework_version 4.3.1

Name:           excalibur
Version:        1.0
Release:        alt8_0.r508111.16jpp6
Epoch:          1
Summary:        Excalibur IOC Frameworks, Containers, Components
License:        ASL 2.0
Group:          Development/Java
URL:            http://excalibur.apache.org/
Source0:        http://www.apache.org/dist/excalibur/releases/200702/excalibur-src-r508111-15022007.tar.gz
Source2:        excalibur-1.0-build-files.tar.gz
Source3:        excalibur-settings.xml
Source4:        excalibur-1.0-jpp-depmap.xml
Source100:      excalibur-avalon-framework-component-info.xml
Source101:      excalibur-avalon-logkit-component-info.xml
# FIXME: patch out maven-gpg-plugin processing
Patch0:         excalibur-r508111-00-pom_xml.patch
#### # add saxon-aelfred to dependencies:
Patch1:         excalibur-components-xmlutil-pom.patch
#### Patch1:         excalibur-r508111-components-xmlutil-01-pom_xml.patch
# add concurrent to dependencies:
Patch2:         excalibur-r508111-fortress-container-impl-02-pom_xml.patch
# set testFailureIgnore to true FIXME:
Patch3:         excalibur-r508111-deprecated-component-test-03-pom_xml.patch
Patch4:         excalibur-r508111-fortress-examples-04-pom_xml.patch
Patch5:         excalibur-r508111-fortress-platform-05-script.patch
Patch6:         excalibur-r508111-fortress-platform-06-wrapper_conf.patch
Patch7:         excalibur-containerkit-logkit-DefaultDataSource.patch
Patch8:         excalibur-components-xmlutil-Saxon8ProcessorImpl.patch
Patch9:         excalibur-r508111-maven-compile-target.patch
Patch10:        excalibur-r508111-components-xmlutil-project-xml.patch
Patch11:        excalibur-qdox.patch
BuildRequires:  commons-parent
BuildRequires:  geronimo-genesis >= 0:1.1
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-junit
BuildRequires:  hsqldb
BuildRequires:  junit
BuildRequires:  jmock
%if %{with_maven}
BuildRequires:  maven2 >= 2.0.7
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-eclipse
BuildRequires:  maven2-plugin-idea
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven-release
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit
%if 0
BuildRequires:  avalon-framework
%endif
%endif
BuildRequires:  bcel
#BuildRequires: javamail_1_3_1_api
BuildRequires:  geronimo-javamail-1.3.1-api
BuildRequires:  concurrent
BuildRequires:  d-haven-event
BuildRequires:  d-haven-mpool
#BuildRequires: jms_1_1_api
BuildRequires:  geronimo-jms-1.1-api
BuildRequires:  jakarta-commons-beanutils
BuildRequires:  jakarta-commons-collections
BuildRequires:  jakarta-commons-httpclient
BuildRequires:  jakarta-commons-logging
BuildRequires:  jakarta-commons-vfs
BuildRequires:  jaxen
BuildRequires:  jisp2
BuildRequires:  jtidy
BuildRequires:  junitperf
BuildRequires:  log4j >= 0:1.2.13
BuildRequires:  qdox161
BuildRequires:  saxon8
BuildRequires:  saxon8-xpath
#### BuildRequires:  saxon
#### BuildRequires:  saxon7
#### BuildRequires:  saxon-aelfred
BuildRequires:  servlet_2_3_api
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-jaxp-1.3-apis
BuildRequires:  xml-commons-resolver11
BuildRequires:  xom

%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif

Requires(post):    jpackage-utils >= 0:1.7.4
Requires(postun):  jpackage-utils >= 0:1.7.4
Source44: import.info


%description
Excalibur is a platform for component and container applications 
built on key design patterns such as Inversion of Control and 
Separation of Concerns available for the Java platform. You 
can use Excalibur to build any number of other applications 
from desktop centric Swing apps to complicated servers. The 
Avalon Framework (the core of Excalibur) is often used as the 
"underpinning" of a larger application or platform. Such 
applications include Apache Cocoon, Apache James, and the 
Keel Framework.
Excalibur is not part of the J2EE stack. While Excalibur can 
be used in developing J2EE applications and even used to build 
a J2EE server, the platform is not part of J2EE or a J2EE 
application server. Excalibur is much simpler and does not 
include many J2EE specifications out of the box. That said, 
you might write a J2EE application which embeds Excalibur 
(such as in a servlet) or you may embed a J2EE server in a 
larger Excalibur-based container.
The Excalibur platform is the following:
* A core framework for component programming (The Avalon Framework)
* An IoC container called Fortress
* A set of container utilities called ContainerKit
* A component library called Cornerstone
When working with Excalibur you may use one or all of these. 

%package avalon-framework
Summary:        Excalibur Avalon Framework Monolithic
Group:          Development/Java
Version:        %{framework_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-logkit = %{epoch}:%{containerkit_version}-%{release}
Requires:       jakarta-commons-logging
Requires:       log4j >= 0:1.2.13

%description avalon-framework
%{summary}.

%if %with repolib
%package avalon-framework-repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java
Version:        %{framework_version}

%description avalon-framework-repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package avalon-framework-api
Summary:        Excalibur Avalon Framework API
Group:          Development/Java
Version:        %{framework_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-logkit = %{epoch}:%{containerkit_version}-%{release}

%description avalon-framework-api
%{summary}.

%package avalon-framework-impl
Summary:        Excalibur Avalon Framework Implementation
Group:          Development/Java
Version:        %{framework_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-logkit = %{epoch}:%{containerkit_version}-%{release}
Requires:       jakarta-commons-logging
Requires:       log4j >= 0:1.2.13

%description avalon-framework-impl
%{summary}.

%package avalon-logkit
Summary:        Excalibur Avalon LogKit
Group:          Development/Java
Version:        %{containerkit_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       jms_1_1_api
#Requires:      geronimo-jms-1.1-api
Requires:       javamail_1_3_1_api
#Requires:      geronimo-javamail-1.3.1-api
Requires:       log4j >= 0:1.2.13
Requires:       servlet

%description avalon-logkit
%{summary}.

%if %with repolib
%package avalon-logkit-repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java
Version:        %{containerkit_version}

%description avalon-logkit-repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package cornerstone-connection-api
Summary:        Excalibur Cornerstone Connection API
Group:          Development/Java
Version:        %{cornerstone_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-thread-api = %{epoch}:%{components_version}-%{release}

%description cornerstone-connection-api
%{summary}.

%package cornerstone-connection-impl
Summary:        Excalibur Cornerstone Connection Implementation
Group:          Development/Java
Version:        %{cornerstone_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-cornerstone-connection-api = %{epoch}:%{cornerstone_version}-%{release}
Requires:       %{name}-cornerstone-sockets-api = %{epoch}:%{cornerstone_version}-%{release}
Requires:       %{name}-cornerstone-threads-api = %{epoch}:%{cornerstone_version}-%{release}
Requires:       %{name}-datasource = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-pool-api = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-pool-impl = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-thread-api = %{epoch}:%{components_version}-%{release}
Requires:       jakarta-commons-logging
Requires:       xerces-j2
Requires:       xml-commons-jaxp-1.3-apis

%description cornerstone-connection-impl
%{summary}.

%package cornerstone-datasources-api
Summary:        Excalibur Cornerstone Datasources API
Group:          Development/Java
Version:        %{cornerstone_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}

%description cornerstone-datasources-api
%{summary}.

%package cornerstone-datasources-impl
Summary:        Excalibur Cornerstone Datasources Implementation
Group:          Development/Java
Version:        %{cornerstone_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-pool-api = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-pool-impl = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-datasource = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-cornerstone-datasources-api = %{epoch}:%{cornerstone_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       xerces-j2
Requires:       xml-commons-jaxp-1.3-apis

%description cornerstone-datasources-impl
%{summary}.

%package cornerstone-scheduler-api
Summary:        Excalibur Cornerstone Scheduler API
Group:          Development/Java
Version:        %{cornerstone_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       xerces-j2
Requires:       xml-commons-jaxp-1.3-apis

%description cornerstone-scheduler-api
%{summary}.

%package cornerstone-scheduler-impl
Summary:        Excalibur Cornerstone Scheduler Implementation
Group:          Development/Java
Version:        %{cornerstone_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-cornerstone-scheduler-api = %{epoch}:%{cornerstone_version}-%{release}
Requires:       %{name}-cornerstone-threads-api = %{epoch}:%{cornerstone_version}-%{release}
Requires:       %{name}-thread-api = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       xerces-j2
Requires:       xml-commons-jaxp-1.3-apis

%description cornerstone-scheduler-impl
%{summary}.

%package cornerstone-sockets-api
Summary:        Excalibur Cornerstone Sockets API
Group:          Development/Java
Version:        %{cornerstone_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}

%description cornerstone-sockets-api
%{summary}.

%package cornerstone-sockets-impl
Summary:        Excalibur Cornerstone Sockets Implementation
Group:          Development/Java
Version:        %{cornerstone_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-cornerstone-sockets-api = %{epoch}:%{cornerstone_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       xerces-j2
Requires:       xml-commons-jaxp-1.3-apis

%description cornerstone-sockets-impl
%{summary}.

%package cornerstone-store-api
Summary:        Excalibur Cornerstone Store API
Group:          Development/Java
Version:        %{cornerstone_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}

%description cornerstone-store-api
%{summary}.

%package cornerstone-store-impl
Summary:        Excalibur Cornerstone Store Implementation
Group:          Development/Java
Version:        %{cornerstone_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-cornerstone-store-api = %{epoch}:%{cornerstone_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       xerces-j2
Requires:       xml-commons-jaxp-1.3-apis

%description cornerstone-store-impl
%{summary}.

%package cornerstone-threads-api
Summary:        Excalibur Cornerstone Threads API
Group:          Development/Java
Version:        %{cornerstone_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-thread-api = %{epoch}:%{components_version}-%{release}

%description cornerstone-threads-api
%{summary}.

%package cornerstone-threads-impl
Summary:        Excalibur Cornerstone Threads Implementation
Group:          Development/Java
Version:        %{cornerstone_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-cornerstone-threads-api = %{epoch}:%{cornerstone_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-pool-api = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-pool-impl = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-thread-api = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-thread-impl = %{epoch}:%{components_version}-%{release}
Requires:       concurrent
Requires:       jakarta-commons-collections

%description cornerstone-threads-impl
%{summary}.

%package component
Summary:        Excalibur Component Component (deprecated)
Group:          Development/Java
Version:        %{excalidep_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-logger = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-avalon-logkit = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-pool-api = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-pool-impl = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-pool-instrumented = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-instrument-api = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-instrument-mgr-api = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-instrument-mgr-impl = %{epoch}:%{containerkit_version}-%{release}
Requires:       jakarta-commons-collections
Requires:       log4j
Requires:       servlet

%description component
%{summary}.

%package datasource
Summary:        Excalibur Datasource Component
Group:          Development/Java
Version:        %{components_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-testcase = %{epoch}:%{excalidep_version}-%{release}
Requires:       %{name}-pool-api = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-pool-impl = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-pool-instrumented = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-instrument-api = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-logger = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-avalon-logkit = %{epoch}:%{containerkit_version}-%{release}
Requires:       concurrent
Requires:       hsqldb

%description datasource
%{summary}.

%package event-api
Summary:        Excalibur Event Component API (deprecated)
Group:          Development/Java
Version:        %{excalidep_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}

%description event-api
%{summary}.

%package event-impl
Summary:        Excalibur Event Component Implementation (deprecated)
Group:          Development/Java
Version:        %{excalidep_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-event-api = %{epoch}:%{excalidep_version}-%{release}
Requires:       %{name}-logger = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-avalon-logkit = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-pool-api = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-pool-impl = %{epoch}:%{components_version}-%{release}
Requires:       concurrent
Requires:       jakarta-commons-collections

%description event-impl
%{summary}.

%package fortress-bean
Summary:        Excalibur Fortress Bean
Group:          Development/Java
Version:        %{fortress_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-fortress-container-api = %{epoch}:%{fortress_version}-%{release}
Requires:       %{name}-fortress-container-impl = %{epoch}:%{fortress_version}-%{release}
Requires:       %{name}-logger = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-avalon-logkit = %{epoch}:%{containerkit_version}-%{release}
Requires:       junit

%description fortress-bean
%{summary}.

%package fortress-container-api
Summary:        Excalibur Fortress Container API
Group:          Development/Java
Version:        %{fortress_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       d-haven-event

%description fortress-container-api
%{summary}.

%package fortress-container-impl
Summary:        Excalibur Fortress Container Implementation
Group:          Development/Java
Version:        %{fortress_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-fortress-container-api = %{epoch}:%{fortress_version}-%{release}
Requires:       %{name}-logger = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-avalon-logkit = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-instrument-api = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-instrument-mgr-api = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-instrument-mgr-impl = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-lifecycle-api = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-lifecycle-impl = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-sourceresolve = %{epoch}:%{components_version}-%{release}
Requires:       bcel
Requires:       concurrent
Requires:       d-haven-event
Requires:       d-haven-mpool
Requires:       jakarta-commons-beanutils
Requires:       jakarta-commons-collections

%description fortress-container-impl
%{summary}.

%package fortress-examples
Summary:        Excalibur Fortress Examples
Group:          Development/Java
Version:        %{fortress_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-logger = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-instrument-api = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-lifecycle-api = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-lifecycle-impl = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-fortress-container-api = %{epoch}:%{fortress_version}-%{release}
Requires:       %{name}-fortress-container-impl = %{epoch}:%{fortress_version}-%{release}
Requires:       servlet

%description fortress-examples
%{summary}.

%package fortress-meta
Summary:        Excalibur Fortress Metadata
Group:          Development/Java
Version:        %{fortress_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-fortress-container-api = %{epoch}:%{fortress_version}-%{release}
Requires:       ant
Requires:       qdox161

%description fortress-meta
%{summary}.

%package fortress-migration
Summary:        Excalibur Fortress Migration
Group:          Development/Java
Version:        %{fortress_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-fortress-container-api = %{epoch}:%{fortress_version}-%{release}
Requires:       %{name}-fortress-container-impl = %{epoch}:%{fortress_version}-%{release}

%description fortress-migration
%{summary}.

%package fortress-platform
Summary:        Excalibur Fortress Platform
Group:          Development/Java
Version:        %{fortress_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-fortress-container-impl = %{epoch}:%{fortress_version}-%{release}
Requires:       tanukiwrapper

%description fortress-platform
%{summary}.

%package fortress-testcase
Summary:        Excalibur Fortress Testcase
Group:          Development/Java
Version:        %{fortress_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-fortress-container-api = %{epoch}:%{fortress_version}-%{release}
Requires:       %{name}-fortress-container-impl = %{epoch}:%{fortress_version}-%{release}
Requires:       junit

%description fortress-testcase
%{summary}.

%package instrument-api
Summary:        Excalibur Instrument API
Group:          Development/Java
Version:        %{containerkit_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}

%description instrument-api
%{summary}.

%package instrument-client
Summary:        Excalibur Instrument Client
Group:          Development/Java
Version:        %{containerkit_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}

%description instrument-client
%{summary}.

%package instrument-mgr-api
Summary:        Excalibur Instrument Manager API
Group:          Development/Java
Version:        %{containerkit_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-instrument-api = %{epoch}:%{containerkit_version}-%{release}
Requires:       xml-commons-jaxp-1.3-apis

%description instrument-mgr-api
%{summary}.

%package instrument-mgr-http
Summary:        Excalibur Instrument Manager HTTP Access
Group:          Development/Java
Version:        %{containerkit_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-instrument-api = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-instrument-mgr-api = %{epoch}:%{containerkit_version}-%{release}
Requires:       xml-commons-jaxp-1.3-apis

%description instrument-mgr-http
%{summary}.

%package instrument-mgr-impl
Summary:        Excalibur Instrument Manager Implementation
Group:          Development/Java
Version:        %{containerkit_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-instrument-api = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-instrument-mgr-api = %{epoch}:%{containerkit_version}-%{release}
Requires:       xml-commons-jaxp-1.3-apis

%description instrument-mgr-impl
%{summary}.

%package lifecycle-api
Summary:        Excalibur Lifecycle API
Group:          Development/Java
Version:        %{containerkit_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}

%description lifecycle-api
%{summary}.

%package lifecycle-impl
Summary:        Excalibur Lifecycle Implementation
Group:          Development/Java
Version:        %{containerkit_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-lifecycle-api = %{epoch}:%{containerkit_version}-%{release}

%description lifecycle-impl
%{summary}.

%package logger
Summary:        Excalibur Logger
Group:          Development/Java
Version:        %{containerkit_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-logkit = %{epoch}:%{containerkit_version}-%{release}
Requires:       jms_1_1_api
#Requires:      geronimo-jms-1.1-api
Requires:       javamail_1_3_1_api
#Requires:      geronimo-javamail-1.3.1-api
Requires:       log4j
Requires:       servlet
Requires:       xml-commons-jaxp-1.3-apis

%description logger
%{summary}.

%package monitor
Summary:        Excalibur Monitor
Group:          Development/Java
Version:        %{components_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-sourceresolve = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-avalon-logkit = %{epoch}:%{containerkit_version}-%{release}
Requires:       log4j

%description monitor
%{summary}.

%package pool-api
Summary:        Excalibur Pool API
Group:          Development/Java
Version:        %{components_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}

%description pool-api
%{summary}.

%package pool-impl
Summary:        Excalibur Pool Implementation
Group:          Development/Java
Version:        %{components_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-pool-api = %{epoch}:%{components_version}-%{release}
Requires:       concurrent
Requires:       jakarta-commons-collections

%description pool-impl
%{summary}.

%package pool-instrumented
Summary:        Excalibur Pool Instrumented
Group:          Development/Java
Version:        %{components_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-instrument-api = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-pool-api = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-fortress-container-api = %{epoch}:%{fortress_version}-%{release}
Requires:       concurrent
Requires:       jakarta-commons-collections
Requires:       jakarta-commons-logging

%description pool-instrumented
%{summary}.

%package sourceresolve
Summary:        Excalibur Sourceresolve
Group:          Development/Java
Version:        %{components_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       jakarta-commons-httpclient
Requires:       jakarta-commons-logging
Requires:       jakarta-commons-vfs

%description sourceresolve
%{summary}.

%package store
Summary:        Excalibur Store
Group:          Development/Java
Version:        %{components_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-instrument-api = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-fortress-container-api = %{epoch}:%{fortress_version}-%{release}
Requires:       concurrent
Requires:       jisp2

%description store
%{summary}.

%package testcase
Summary:        Excalibur Testcase (deprecated)
Group:          Development/Java
Version:        %{excalidep_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-component = %{epoch}:%{excalidep_version}-%{release}
Requires:       %{name}-logger = %{epoch}:%{containerkit_version}-%{release}
Requires:       %{name}-avalon-logkit = %{epoch}:%{containerkit_version}-%{release}
Requires:       junit
Requires:       log4j

%description testcase
%{summary}.

%package thread-api
Summary:        Excalibur Thread API
Group:          Development/Java
Version:        %{components_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}

%description thread-api
%{summary}.

%package thread-impl
Summary:        Excalibur Thread Implementation
Group:          Development/Java
Version:        %{components_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-thread-api = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-pool-api = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-pool-impl = %{epoch}:%{components_version}-%{release}

%description thread-impl
%{summary}.

%package thread-instrumented
Summary:        Excalibur Thread Instrumented
Group:          Development/Java
Version:        %{components_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-avalon-framework-impl = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-thread-api = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-thread-impl = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-pool-api = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-pool-impl = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-pool-instrumented = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-instrument-api = %{epoch}:%{containerkit_version}-%{release}

%description thread-instrumented
%{summary}.

%package xmlutil
Summary:        Excalibur XML Utilities
Group:          Development/Java
Version:        %{components_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-avalon-framework-api = %{epoch}:%{framework_version}-%{release}
Requires:       %{name}-pool-api = %{epoch}:%{components_version}-%{release}
#### Requires:       saxon
Requires:       %{name}-sourceresolve = %{epoch}:%{components_version}-%{release}
Requires:       %{name}-store = %{epoch}:%{components_version}-%{release}
Requires:       jaxen
Requires:       jtidy
#### Requires:       saxon-aelfred
#### Requires:       saxon7
Requires:       saxon8
Requires:       saxon8-xpath
Requires:       xalan-j2
Requires:       xerces-j2
Requires:       xml-commons-jaxp-1.3-apis
Requires:       xml-commons-resolver11

%description xmlutil
%{summary}.

%if %{with_maven}
%package maven-fortress-plugin
Summary:        Excalibur Fortress Maven2 Plugin
Group:          Development/Java
Version:        %{fortress_version}
Requires:       %{name} = %{epoch}:%{main_version}-%{release}
Requires:       %{name}-fortress-meta = %{epoch}:%{fortress_version}-%{release}
Requires:       maven2

%description maven-fortress-plugin
%{summary}.
%endif

%package avalon-framework-api-javadoc
Summary:        Javadoc for avalon-framework-api
Group:          Development/Documentation
Version:        %{framework_version}

%description avalon-framework-api-javadoc
%{summary}.

%package avalon-framework-impl-javadoc
Summary:        Javadoc for avalon-framework-impl
Group:          Development/Documentation
Version:        %{framework_version}

%description avalon-framework-impl-javadoc
%{summary}.

%package avalon-logkit-javadoc
Summary:        Javadoc for avalon-logkit
Group:          Development/Documentation
Version:        %{containerkit_version}

%description avalon-logkit-javadoc
%{summary}.

%package cornerstone-connection-api-javadoc
Summary:        Javadoc for cornerstone-connection-api
Group:          Development/Documentation
Version:        %{cornerstone_version}

%description cornerstone-connection-api-javadoc
%{summary}.

%package cornerstone-connection-impl-javadoc
Summary:        Javadoc for cornerstone-connection-impl
Group:          Development/Documentation
Version:        %{cornerstone_version}

%description cornerstone-connection-impl-javadoc
%{summary}.

%package cornerstone-datasources-api-javadoc
Summary:        Javadoc for cornerstone-datasources-api
Group:          Development/Documentation
Version:        %{cornerstone_version}

%description cornerstone-datasources-api-javadoc
%{summary}.

%package cornerstone-datasources-impl-javadoc
Summary:        Javadoc for cornerstone-datasources-impl
Group:          Development/Documentation
Version:        %{cornerstone_version}

%description cornerstone-datasources-impl-javadoc
%{summary}.

%package cornerstone-scheduler-api-javadoc
Summary:        Javadoc for cornerstone-scheduler-api
Group:          Development/Documentation
Version:        %{cornerstone_version}

%description cornerstone-scheduler-api-javadoc
%{summary}.

%package cornerstone-scheduler-impl-javadoc
Summary:        Javadoc for cornerstone-scheduler-impl
Group:          Development/Documentation
Version:        %{cornerstone_version}

%description cornerstone-scheduler-impl-javadoc
%{summary}.

%package cornerstone-sockets-api-javadoc
Summary:        Javadoc for cornerstone-sockets-api
Group:          Development/Documentation
Version:        %{cornerstone_version}

%description cornerstone-sockets-api-javadoc
%{summary}.

%package cornerstone-sockets-impl-javadoc
Summary:        Javadoc for cornerstone-sockets-impl
Group:          Development/Documentation
Version:        %{cornerstone_version}

%description cornerstone-sockets-impl-javadoc
%{summary}.

%package cornerstone-store-api-javadoc
Summary:        Javadoc for cornerstone-store-api
Group:          Development/Documentation
Version:        %{cornerstone_version}

%description cornerstone-store-api-javadoc
%{summary}.

%package cornerstone-store-impl-javadoc
Summary:        Javadoc for cornerstone-store-impl
Group:          Development/Documentation
Version:        %{cornerstone_version}

%description cornerstone-store-impl-javadoc
%{summary}.

%package cornerstone-threads-api-javadoc
Summary:        Javadoc for cornerstone-threads-api
Group:          Development/Documentation
Version:        %{cornerstone_version}

%description cornerstone-threads-api-javadoc
%{summary}.

%package cornerstone-threads-impl-javadoc
Summary:        Javadoc for cornerstone-threads-impl
Group:          Development/Documentation
Version:        %{cornerstone_version}

%description cornerstone-threads-impl-javadoc
%{summary}.

%package component-javadoc
Summary:        Javadoc for component
Group:          Development/Documentation
Version:        %{excalidep_version}

%description component-javadoc
%{summary}.

%package datasource-javadoc
Summary:        Javadoc for datasource
Group:          Development/Documentation
Version:        %{components_version}

%description datasource-javadoc
%{summary}.

%package event-api-javadoc
Summary:        Javadoc for event-api
Group:          Development/Documentation
Version:        %{excalidep_version}

%description event-api-javadoc
%{summary}.

%package event-impl-javadoc
Summary:        Javadoc for event-impl
Group:          Development/Documentation
Version:        %{excalidep_version}

%description event-impl-javadoc
%{summary}.

%package fortress-bean-javadoc
Summary:        Javadoc for fortress-bean
Group:          Development/Documentation
Version:        %{fortress_version}

%description fortress-bean-javadoc
%{summary}.

%package fortress-container-api-javadoc
Summary:        Javadoc for fortress-container-api
Group:          Development/Documentation
Version:        %{fortress_version}

%description fortress-container-api-javadoc
%{summary}.

%package fortress-container-impl-javadoc
Summary:        Javadoc for fortress-container-impl
Group:          Development/Documentation
Version:        %{fortress_version}

%description fortress-container-impl-javadoc
%{summary}.

%package fortress-examples-javadoc
Summary:        Javadoc for fortress-examples
Group:          Development/Documentation
Version:        %{fortress_version}

%description fortress-examples-javadoc
%{summary}.

%package fortress-meta-javadoc
Summary:        Javadoc for fortress-meta
Group:          Development/Documentation
Version:        %{fortress_version}

%description fortress-meta-javadoc
%{summary}.

%package fortress-migration-javadoc
Summary:        Javadoc for fortress-migration
Group:          Development/Documentation
Version:        %{fortress_version}

%description fortress-migration-javadoc
%{summary}.

%package fortress-testcase-javadoc
Summary:        Javadoc for fortress-testcase
Group:          Development/Documentation
Version:        %{fortress_version}

%description fortress-testcase-javadoc
%{summary}.

%package instrument-api-javadoc
Summary:        Javadoc for instrument-api
Group:          Development/Documentation
Version:        %{containerkit_version}

%description instrument-api-javadoc
%{summary}.

%package instrument-client-javadoc
Summary:        Javadoc for instrument-client
Group:          Development/Documentation
Version:        %{containerkit_version}

%description instrument-client-javadoc
%{summary}.

%package instrument-mgr-api-javadoc
Summary:        Javadoc for instrument-mgr-api
Group:          Development/Documentation
Version:        %{containerkit_version}

%description instrument-mgr-api-javadoc
%{summary}.

%package instrument-mgr-http-javadoc
Summary:        Javadoc for instrument-mgr-http
Group:          Development/Documentation
Version:        %{containerkit_version}

%description instrument-mgr-http-javadoc
%{summary}.

%package instrument-mgr-impl-javadoc
Summary:        Javadoc for instrument-mgr-impl
Group:          Development/Documentation
Version:        %{containerkit_version}

%description instrument-mgr-impl-javadoc
%{summary}.

%package lifecycle-api-javadoc
Summary:        Javadoc for lifecycle-api
Group:          Development/Documentation
Version:        %{containerkit_version}

%description lifecycle-api-javadoc
%{summary}.

%package lifecycle-impl-javadoc
Summary:        Javadoc for lifecycle-impl
Group:          Development/Documentation
Version:        %{containerkit_version}

%description lifecycle-impl-javadoc
%{summary}.

%package logger-javadoc
Summary:        Javadoc for logger
Group:          Development/Documentation
Version:        %{containerkit_version}

%description logger-javadoc
%{summary}.

%package monitor-javadoc
Summary:        Javadoc for monitor
Group:          Development/Documentation
Version:        %{components_version}

%description monitor-javadoc
%{summary}.

%package pool-api-javadoc
Summary:        Javadoc for pool-api
Group:          Development/Documentation
Version:        %{components_version}

%description pool-api-javadoc
%{summary}.

%package pool-impl-javadoc
Summary:        Javadoc for pool-impl
Group:          Development/Documentation
Version:        %{components_version}

%description pool-impl-javadoc
%{summary}.

%package pool-instrumented-javadoc
Summary:        Javadoc for pool-instrumented
Group:          Development/Documentation
Version:        %{components_version}

%description pool-instrumented-javadoc
%{summary}.

%package sourceresolve-javadoc
Summary:        Javadoc for sourceresolve
Group:          Development/Documentation
Version:        %{components_version}

%description sourceresolve-javadoc
%{summary}.

%package store-javadoc
Summary:        Javadoc for store
Group:          Development/Documentation
Version:        %{components_version}

%description store-javadoc
%{summary}.

%package testcase-javadoc
Summary:        Javadoc for testcase
Group:          Development/Documentation
Version:        %{excalidep_version}

%description testcase-javadoc
%{summary}.

%package thread-api-javadoc
Summary:        Javadoc for thread-api
Group:          Development/Documentation
Version:        %{components_version}

%description thread-api-javadoc
%{summary}.

%package thread-impl-javadoc
Summary:        Javadoc for thread-impl
Group:          Development/Documentation
Version:        %{components_version}

%description thread-impl-javadoc
%{summary}.

%package thread-instrumented-javadoc
Summary:        Javadoc for thread-instrumented
Group:          Development/Documentation
Version:        %{components_version}

%description thread-instrumented-javadoc
%{summary}.

%package xmlutil-javadoc
Summary:        Javadoc for xmlutil
Group:          Development/Documentation
Version:        %{components_version}

%description xmlutil-javadoc
%{summary}.

%if %{with_maven}
%package maven-fortress-plugin-javadoc
Summary:        Javadoc for maven-fortress-plugin
Group:          Development/Documentation
Version:        %{fortress_version}

%description maven-fortress-plugin-javadoc
%{summary}.
%endif

%prep
%setup -q -n %{name}-src-%{rsvn}-%{rdate}
%setup -q -n %{name}-src-%{rsvn}-%{rdate} -T -D -a 2
cp -p %{SOURCE3} settings.xml
find . -name "*.jar" | xargs -t rm

rm components/xmlutil/src/java/org/apache/excalibur/xml/xpath/Saxon6ProcessorImpl.java  
mv components/xmlutil/src/java/org/apache/excalibur/xml/xpath/Saxon7ProcessorImpl.java \
   components/xmlutil/src/java/org/apache/excalibur/xml/xpath/Saxon8ProcessorImpl.java

## patch out maven-gpg-plugin processing FIXME
%patch0 -p0 -b .sav00
%patch1 -p0 -b .sav01
# add saxon-aelfred to dependencies
%if 0
%patch1 -p0 -b .sav01
%endif
# add concurrent to dependencies
%patch2 -p0 -b .sav02
# set testFailureIgnore to true
%patch3 -p0 -b .sav03
#
%patch4 -p0 -b .sav04
#
%patch5 -p0 -b .sav05
#
%patch6 -p0 -b .sav06
%if %with jdk6
%patch7 -p0 -b .sav07
%endif
%patch8 -p0 -b .sav08
%patch9 -p0 -b .sav09
%patch10 -p0 -b .sav10
%patch11 -p0 -b .sav11

%if %with maven
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP
%endif

%build
%if %with maven
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

export LANG=en_US.UTF-8
export CLASSPATH=$(build-classpath xalan-j2-serializer)

mkdir testDir

export MAVEN_OPTS="-Xmx384m -XX:PermSize=256m -XX:MaxPermSize=512m"
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Dmaven2.jpp.mode=true \
        -Dmaven.test.failure.ignore=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE4} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dtest.db.driver=org.hsqldb.jdbcDriver \
        -Dtest.db.jdbc=jdbc:hsqldb:mem:dbtest \
        -Dtest.db.user=sa \
        -Dtest.db.pword="" \
        -Dtest.db.run="true" \
        install javadoc:javadoc
%else
export EXCALIBUR_BASEDIR=$(pwd)
pushd containerkit/logkit
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$(build-classpath \
log4j \
servlet_2_3_api \
javamail_1_3_1_api \
jms_1_1_api \
junit \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd framework/api
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logkit/target/avalon-logkit-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd framework/impl
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$(build-classpath \
commons-logging \
jmock \
junit \
log4j \
)
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logkit/target/avalon-logkit-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd containerkit/logger
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logkit/target/avalon-logkit-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
log4j \
servlet_2_3_api \
javamail_1_3_1_api \
jms_1_1_api \
xml-commons-jaxp-1.3-apis \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd containerkit/lifecycle/api
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd containerkit/lifecycle/impl
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/lifecycle/api/target/excalibur-lifecycle-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd containerkit/instrument/api
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
junit \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd containerkit/instrument/client
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd containerkit/instrument/mgr-api
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/api/target/excalibur-instrument-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
xml-commons-jaxp-1.3-apis \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd containerkit/instrument/mgr-http
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/api/target/excalibur-instrument-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/mgr-api/target/excalibur-instrument-mgr-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
xml-commons-jaxp-1.3-apis \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd containerkit/instrument/mgr-impl
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/api/target/excalibur-instrument-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/mgr-api/target/excalibur-instrument-mgr-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
junit \
xml-commons-jaxp-1.3-apis \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd fortress/container-api
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
d-haven-event \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd fortress/meta
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/fortress/container-api/target/excalibur-fortress-container-api-%{fortress_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
qdox161 \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd fortress/plugin
popd

pushd components/sourceresolve
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
commons-vfs \
commons-httpclient \
commons-logging \
junit \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd components/pool/api
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd components/pool/impl
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/api/target/excalibur-pool-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
commons-collections \
concurrent \
junitperf \
junit \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd components/pool/instrumented
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/api/target/excalibur-instrument-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/api/target/excalibur-pool-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/fortress/container-api/target/excalibur-fortress-container-api-%{fortress_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
commons-collections \
commons-logging \
concurrent \
junitperf \
junit \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd deprecated/component
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logger/target/excalibur-logger-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logkit/target/avalon-logkit-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/api/target/excalibur-pool-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/impl/target/excalibur-pool-impl-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/instrumented/target/excalibur-pool-instrumented-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/api/target/excalibur-instrument-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/mgr-api/target/excalibur-instrument-mgr-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/mgr-impl/target/excalibur-instrument-mgr-impl-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
commons-collections \
junit \
log4j \
servlet_2_3_api \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd deprecated/testcase
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/deprecated/component/target/excalibur-component-%{excalidep_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logger/target/excalibur-logger-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logkit/target/avalon-logkit-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
junit \
log4j \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd components/store
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/api/target/excalibur-instrument-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/fortress/container-api/target/excalibur-fortress-container-api-%{fortress_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
concurrent \
jisp2 \
junit \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd components/xmlutil
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/api/target/excalibur-pool-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/sourceresolve/target/excalibur-sourceresolve-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/store/target/excalibur-store-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/deprecated/testcase/target/excalibur-testcase-%{excalidep_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
jaxen \
jtidy \
junit \
saxon8 \
saxon8-xpath \
xalan-j2 \
xerces-j2 \
xml-commons-jaxp-1.3-apis \
xml-commons-resolver11 \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd components/thread/api
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd components/thread/impl
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/thread/api/target/excalibur-thread-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/api/target/excalibur-pool-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/impl/target/excalibur-pool-impl-%{components_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
junit \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd components/thread/instrumented
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/thread/api/target/excalibur-thread-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/thread/impl/target/excalibur-thread-impl-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/api/target/excalibur-pool-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/impl/target/excalibur-pool-impl-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/instrumented/target/excalibur-pool-instrumented-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/api/target/excalibur-instrument-api-%{containerkit_version}.jar

CLASSPATH=$CLASSPATH:$(build-classpath \
junit \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd components/monitor
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/sourceresolve/target/excalibur-sourceresolve-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/deprecated/testcase/target/excalibur-testcase-%{excalidep_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logkit/target/avalon-logkit-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
commons-collections \
log4j \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd components/datasource
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/deprecated/testcase/target/excalibur-testcase-%{excalidep_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/api/target/excalibur-pool-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/impl/target/excalibur-pool-impl-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/instrumented/target/excalibur-pool-instrumented-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/api/target/excalibur-instrument-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logger/target/excalibur-logger-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logkit/target/avalon-logkit-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
concurrent \
hsqldb \
junit \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd fortress/container-impl
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/fortress/container-api/target/excalibur-fortress-container-api-%{fortress_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logger/target/excalibur-logger-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logkit/target/avalon-logkit-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/api/target/excalibur-instrument-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/mgr-api/target/excalibur-instrument-mgr-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/mgr-impl/target/excalibur-instrument-mgr-impl-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/lifecycle/api/target/excalibur-lifecycle-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/lifecycle/impl/target/excalibur-lifecycle-impl-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/sourceresolve/target/excalibur-sourceresolve-%{components_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
bcel \
commons-collections \
commons-beanutils \
concurrent \
d-haven-event \
d-haven-mpool \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd fortress/container-test
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/api/target/excalibur-instrument-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/mgr-api/target/excalibur-instrument-mgr-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/mgr-impl/target/excalibur-instrument-mgr-impl-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/lifecycle/api/target/excalibur-lifecycle-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/lifecycle/impl/target/excalibur-lifecycle-impl-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logger/target/excalibur-logger-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/fortress/container-api/target/excalibur-fortress-container-api-%{fortress_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/fortress/container-impl/target/excalibur-fortress-container-impl-%{fortress_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/fortress/meta/target/excalibur-fortress-meta-%{fortress_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
d-haven-event \
d-haven-mpool \
junit \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

# no java sources here
pushd fortress/platform
popd

pushd fortress/examples
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logger/target/excalibur-logger-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/instrument/api/target/excalibur-instrument-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/lifecycle/api/target/excalibur-lifecycle-api-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/lifecycle/impl/target/excalibur-lifecycle-impl-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/fortress/container-api/target/excalibur-fortress-container-api-%{fortress_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/fortress/container-impl/target/excalibur-fortress-container-impl-%{fortress_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
servlet_2_3_api \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd fortress/testcase
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/fortress/container-api/target/excalibur-fortress-container-api-%{fortress_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/fortress/container-impl/target/excalibur-fortress-container-impl-%{fortress_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
junit \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd fortress/migration
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/fortress/container-api/target/excalibur-fortress-container-api-%{fortress_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/fortress/container-impl/target/excalibur-fortress-container-impl-%{fortress_version}.jar
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd fortress/bean
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/fortress/container-api/target/excalibur-fortress-container-api-%{fortress_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/fortress/container-impl/target/excalibur-fortress-container-impl-%{fortress_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/fortress/testcase/target/excalibur-fortress-testcase-%{fortress_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logger/target/excalibur-logger-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logkit/target/avalon-logkit-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
junit \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd deprecated/event/api
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd deprecated/event/impl
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/deprecated/event/api/target/excalibur-event-api-%{excalidep_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logger/target/excalibur-logger-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logkit/target/avalon-logkit-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/api/target/excalibur-pool-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/impl/target/excalibur-pool-impl-%{components_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
commons-collections \
concurrent \
junit \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd deprecated/component-tests
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/deprecated/component/target/excalibur-component-%{excalidep_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/deprecated/testcase/target/excalibur-testcase-%{excalidep_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logger/target/excalibur-logger-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/containerkit/logkit/target/avalon-logkit-%{containerkit_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/api/target/excalibur-pool-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/impl/target/excalibur-pool-impl-%{components_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
junit \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd cornerstone/sockets/api
export CLASSPATH=""
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd cornerstone/threads/api
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/thread/api/target/excalibur-thread-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd cornerstone/connection/api
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/thread/api/target/excalibur-thread-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd cornerstone/connection/impl
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/cornerstone/connection/api/target/cornerstone-connection-api-%{cornerstone_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/cornerstone/sockets/api/target/cornerstone-sockets-api-%{cornerstone_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/cornerstone/threads/api/target/cornerstone-threads-api-%{cornerstone_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/thread/api/target/excalibur-thread-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/api/target/excalibur-pool-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/impl/target/excalibur-pool-impl-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/datasource/target/excalibur-datasource-%{components_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
commons-logging \
xerces-j2 \
xml-commons-jaxp-1.3-apis \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd cornerstone/datasources/api
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd cornerstone/datasources/impl
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/api/target/excalibur-pool-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/impl/target/excalibur-pool-impl-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/datasource/target/excalibur-datasource-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/cornerstone/datasources/api/target/cornerstone-datasources-api-%{cornerstone_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
xerces-j2 \
xml-commons-jaxp-1.3-apis \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd cornerstone/scheduler/api
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
xerces-j2 \
xml-commons-jaxp-1.3-apis \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd cornerstone/scheduler/impl
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/cornerstone/scheduler/api/target/cornerstone-scheduler-api-%{cornerstone_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/cornerstone/threads/api/target/cornerstone-threads-api-%{cornerstone_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/thread/api/target/excalibur-thread-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
xerces-j2 \
xml-commons-jaxp-1.3-apis \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd cornerstone/sockets/impl
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/cornerstone/sockets/api/target/cornerstone-sockets-api-%{cornerstone_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
xerces-j2 \
xml-commons-jaxp-1.3-apis \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd cornerstone/store/api
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd cornerstone/store/impl
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/cornerstone/store/api/target/cornerstone-store-api-%{cornerstone_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

pushd cornerstone/threads/impl
export CLASSPATH=""
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/cornerstone/threads/api/target/cornerstone-threads-api-%{cornerstone_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/api/target/avalon-framework-api-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/framework/impl/target/avalon-framework-impl-%{framework_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/thread/api/target/excalibur-thread-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/thread/impl/target/excalibur-thread-impl-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/api/target/excalibur-pool-api-%{components_version}.jar
CLASSPATH=$CLASSPATH:$EXCALIBUR_BASEDIR/components/pool/impl/target/excalibur-pool-impl-%{components_version}.jar
CLASSPATH=$CLASSPATH:$(build-classpath \
commons-collections \
concurrent \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd

%endif

mkdir aftmp
pushd aftmp
jar xf ../framework/api/target/avalon-framework-api-%{framework_version}.jar
jar xf ../framework/impl/target/avalon-framework-impl-%{framework_version}.jar
jar cf ../avalon-framework-%{framework_version}.jar *
popd
rm -rf aftmp

%install

# for poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

# for jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

# monolithic framework
install -pm 644 avalon-framework-%{framework_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/avalon-framework-%{framework_version}.jar
ln -s %{name}/avalon-framework-%{framework_version}.jar $RPM_BUILD_ROOT%{_javadir}/avalon-framework-%{framework_version}.jar
%add_to_maven_depmap org.apache.avalon.framework avalon-framework %{framework_version} JPP/%{name} avalon-framework
%add_to_maven_depmap avalon-framework avalon-framework %{framework_version} JPP/%{name} avalon-framework

%if %with repolib
%define repodir %{_javadir}/repository.jboss.com/apache-avalon/%{framework_version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE100} $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/@FRAMEWORK_VERSION@/%{framework_version}/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH3} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH4} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH5} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH6} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/avalon-framework-%{framework_version}.jar $RPM_BUILD_ROOT%{repodirlib}/avalon-framework.jar
%endif

# jars, depmapfrags, poms
install -pm 644 components/datasource/target/excalibur-datasource-%{components_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-datasource-%{components_version}.jar
%add_to_maven_depmap org.apache.excalibur.components excalibur-datasource %{components_version} JPP/%{name} excalibur-datasource
%if %{with_maven}
install -pm 644 components/datasource/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-datasource.pom
%endif

install -pm 644 components/monitor/target/excalibur-monitor-%{components_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-monitor-%{components_version}.jar
%add_to_maven_depmap org.apache.excalibur.components excalibur-monitor %{components_version} JPP/%{name} excalibur-monitor
%if %{with_maven}
install -pm 644 components/monitor/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-monitor.pom
%endif

install -pm 644 components/pool/api/target/excalibur-pool-api-%{components_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-pool-api-%{components_version}.jar
%add_to_maven_depmap org.apache.excalibur.components excalibur-pool-api %{components_version} JPP/%{name} excalibur-pool-api
%if %{with_maven}
install -pm 644 components/pool/api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-pool-api.pom
%endif

install -pm 644 components/pool/impl/target/excalibur-pool-impl-%{components_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-pool-impl-%{components_version}.jar
%add_to_maven_depmap org.apache.excalibur.components excalibur-pool-impl %{components_version} JPP/%{name} excalibur-pool-impl
%if %{with_maven}
install -pm 644 components/pool/impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-pool-impl.pom
%endif

install -pm 644 components/pool/instrumented/target/excalibur-pool-instrumented-%{components_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-pool-instrumented-%{components_version}.jar
%add_to_maven_depmap org.apache.excalibur.components excalibur-pool-instrumented %{components_version} JPP/%{name} excalibur-pool-instrumented
%if %{with_maven}
install -pm 644 components/pool/instrumented/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-pool-instrumented.pom
%endif

install -pm 644 components/sourceresolve/target/excalibur-sourceresolve-%{components_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-sourceresolve-%{components_version}.jar
%add_to_maven_depmap org.apache.excalibur.components excalibur-sourceresolve %{components_version} JPP/%{name} excalibur-sourceresolve
%if %{with_maven}
install -pm 644 components/sourceresolve/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-sourceresolve.pom
%endif

install -pm 644 components/store/target/excalibur-store-%{components_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-store-%{components_version}.jar
%add_to_maven_depmap org.apache.excalibur.components excalibur-store %{components_version} JPP/%{name} excalibur-store
%if %{with_maven}
install -pm 644 components/store/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-store.pom
%endif

install -pm 644 components/thread/api/target/excalibur-thread-api-%{components_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-thread-api-%{components_version}.jar
%add_to_maven_depmap org.apache.excalibur.components excalibur-thread-api %{components_version} JPP/%{name} excalibur-thread-api
%if %{with_maven}
install -pm 644 components/thread/api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-thread-api.pom
%endif

install -pm 644 components/thread/impl/target/excalibur-thread-impl-%{components_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-thread-impl-%{components_version}.jar
%add_to_maven_depmap org.apache.excalibur.components excalibur-thread-impl %{components_version} JPP/%{name} excalibur-thread-impl
%if %{with_maven}
install -pm 644 components/thread/impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-thread-impl.pom
%endif

install -pm 644 components/thread/instrumented/target/excalibur-thread-instrumented-%{components_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-thread-instrumented-%{components_version}.jar
%add_to_maven_depmap org.apache.excalibur.components excalibur-thread-instrumented %{components_version} JPP/%{name} excalibur-thread-instrumented
%if %{with_maven}
install -pm 644 components/thread/instrumented/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-thread-instrumented.pom
%endif

install -pm 644 components/xmlutil/target/excalibur-xmlutil-%{components_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-xmlutil-%{components_version}.jar
%add_to_maven_depmap org.apache.excalibur.components excalibur-xmlutil %{components_version} JPP/%{name} excalibur-xmlutil
%if %{with_maven}
install -pm 644 components/xmlutil/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-xmlutil.pom
%endif

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{components_version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{components_version}||g"`; done)

install -pm 644 containerkit/instrument/api/target/excalibur-instrument-api-%{containerkit_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-instrument-api-%{containerkit_version}.jar
%add_to_maven_depmap org.apache.excalibur.containerkit excalibur-instrument-api %{containerkit_version} JPP/%{name} excalibur-instrument-api
%if %{with_maven}
install -pm 644 containerkit/instrument/api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-instrument-api.pom
%endif

install -pm 644 containerkit/instrument/client/target/excalibur-instrument-client-%{containerkit_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-instrument-client-%{containerkit_version}.jar
%add_to_maven_depmap org.apache.excalibur.containerkit excalibur-instrument-client %{containerkit_version} JPP/%{name} excalibur-instrument-client
%if %{with_maven}
install -pm 644 containerkit/instrument/client/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-instrument-client.pom
%endif

install -pm 644 containerkit/instrument/mgr-api/target/excalibur-instrument-mgr-api-%{containerkit_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-instrument-mgr-api-%{containerkit_version}.jar
%add_to_maven_depmap org.apache.excalibur.containerkit excalibur-instrument-mgr-api %{containerkit_version} JPP/%{name} excalibur-instrument-mgr-api
%if %{with_maven}
install -pm 644 containerkit/instrument/mgr-api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-instrument-mgr-api.pom
%endif

install -pm 644 containerkit/instrument/mgr-http/target/excalibur-instrument-mgr-http-%{containerkit_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-instrument-mgr-http-%{containerkit_version}.jar
%add_to_maven_depmap org.apache.excalibur.containerkit excalibur-instrument-mgr-http %{containerkit_version} JPP/%{name} excalibur-instrument-mgr-http
%if %{with_maven}
install -pm 644 containerkit/instrument/mgr-http/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-instrument-mgr-http.pom
%endif

install -pm 644 containerkit/instrument/mgr-impl/target/excalibur-instrument-mgr-impl-%{containerkit_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-instrument-mgr-impl-%{containerkit_version}.jar
%add_to_maven_depmap org.apache.excalibur.containerkit excalibur-instrument-mgr-impl %{containerkit_version} JPP/%{name} excalibur-instrument-mgr-impl
%if %{with_maven}
install -pm 644 containerkit/instrument/mgr-impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-instrument-mgr-impl.pom
%endif

install -pm 644 containerkit/lifecycle/api/target/excalibur-lifecycle-api-%{containerkit_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-lifecycle-api-%{containerkit_version}.jar
%add_to_maven_depmap org.apache.excalibur.containerkit excalibur-lifecycle-api %{containerkit_version} JPP/%{name} excalibur-lifecycle-api
%if %{with_maven}
install -pm 644 containerkit/lifecycle/api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-lifecycle-api.pom
%endif

install -pm 644 containerkit/lifecycle/impl/target/excalibur-lifecycle-impl-%{containerkit_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-lifecycle-impl-%{containerkit_version}.jar
%add_to_maven_depmap org.apache.excalibur.containerkit excalibur-lifecycle-impl %{containerkit_version} JPP/%{name} excalibur-lifecycle-impl
%if %{with_maven}
install -pm 644 containerkit/lifecycle/impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-lifecycle-impl.pom
%endif

install -pm 644 containerkit/logger/target/excalibur-logger-%{containerkit_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-logger-%{containerkit_version}.jar
%add_to_maven_depmap org.apache.excalibur.containerkit excalibur-logger %{containerkit_version} JPP/%{name} excalibur-logger
%if %{with_maven}
install -pm 644 containerkit/logger/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-logger.pom
%endif

install -pm 644 containerkit/logkit/target/avalon-logkit-%{containerkit_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/avalon-logkit-%{containerkit_version}.jar
ln -s %{name}/avalon-logkit-%{containerkit_version}.jar $RPM_BUILD_ROOT%{_javadir}/avalon-logkit-%{containerkit_version}.jar
%add_to_maven_depmap org.apache.avalon.logkit avalon-logkit %{containerkit_version} JPP/%{name} avalon-logkit
%add_to_maven_depmap logkit logkit %{containerkit_version} JPP/%{name} avalon-logkit
%if %{with_maven}
install -pm 644 containerkit/logkit/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-avalon-logkit.pom
%endif

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{containerkit_version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{containerkit_version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{containerkit_version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{containerkit_version}||g"`; done)

install -pm 644 cornerstone/connection/api/target/cornerstone-connection-api-%{cornerstone_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/cornerstone-connection-api-%{cornerstone_version}.jar
%add_to_maven_depmap org.apache.avalon.cornerstone.connection cornerstone-connection-api %{cornerstone_version} JPP/%{name} cornerstone-connection-api
%if %{with_maven}
install -pm 644 cornerstone/connection/api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-connection-api.pom
%endif

install -pm 644 cornerstone/connection/impl/target/cornerstone-connection-impl-%{cornerstone_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/cornerstone-connection-impl-%{cornerstone_version}.jar
%add_to_maven_depmap org.apache.avalon.cornerstone.connection cornerstone-connection-impl %{cornerstone_version} JPP/%{name} cornerstone-connection-impl
%if %{with_maven}
install -pm 644 cornerstone/connection/impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-connection-impl.pom
%endif

install -pm 644 cornerstone/datasources/api/target/cornerstone-datasources-api-%{cornerstone_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/cornerstone-datasources-api-%{cornerstone_version}.jar
%add_to_maven_depmap org.apache.avalon.cornerstone.datasources cornerstone-datasources-api %{cornerstone_version} JPP/%{name} cornerstone-datasources-api
%if %{with_maven}
install -pm 644 cornerstone/datasources/api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-datasources-api.pom
%endif

install -pm 644 cornerstone/datasources/impl/target/cornerstone-datasources-impl-%{cornerstone_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/cornerstone-datasources-impl-%{cornerstone_version}.jar
%add_to_maven_depmap org.apache.avalon.cornerstone.datasources cornerstone-datasources-impl %{cornerstone_version} JPP/%{name} cornerstone-datasources-impl
%if %{with_maven}
install -pm 644 cornerstone/datasources/impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-datasources-impl.pom
%endif

install -pm 644 cornerstone/scheduler/api/target/cornerstone-scheduler-api-%{cornerstone_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/cornerstone-scheduler-api-%{cornerstone_version}.jar
%add_to_maven_depmap org.apache.avalon.cornerstone.scheduler cornerstone-scheduler-api %{cornerstone_version} JPP/%{name} cornerstone-scheduler-api
%if %{with_maven}
install -pm 644 cornerstone/scheduler/api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-scheduler-api.pom
%endif

install -pm 644 cornerstone/scheduler/impl/target/cornerstone-scheduler-impl-%{cornerstone_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/cornerstone-scheduler-impl-%{cornerstone_version}.jar
%add_to_maven_depmap org.apache.avalon.cornerstone.scheduler cornerstone-scheduler-impl %{cornerstone_version} JPP/%{name} cornerstone-scheduler-impl
%if %{with_maven}
install -pm 644 cornerstone/scheduler/impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-scheduler-impl.pom
%endif

install -pm 644 cornerstone/sockets/api/target/cornerstone-sockets-api-%{cornerstone_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/cornerstone-sockets-api-%{cornerstone_version}.jar
%add_to_maven_depmap org.apache.avalon.cornerstone.sockets cornerstone-sockets-api %{cornerstone_version} JPP/%{name} cornerstone-sockets-api
%if %{with_maven}
install -pm 644 cornerstone/sockets/api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-sockets-api.pom
%endif

install -pm 644 cornerstone/sockets/impl/target/cornerstone-sockets-impl-%{cornerstone_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/cornerstone-sockets-impl-%{cornerstone_version}.jar
%add_to_maven_depmap org.apache.avalon.cornerstone.sockets cornerstone-sockets-impl %{cornerstone_version} JPP/%{name} cornerstone-sockets-impl
%if %{with_maven}
install -pm 644 cornerstone/sockets/impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-sockets-impl.pom
%endif

install -pm 644 cornerstone/store/api/target/cornerstone-store-api-%{cornerstone_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/cornerstone-store-api-%{cornerstone_version}.jar
%add_to_maven_depmap org.apache.avalon.cornerstone.store cornerstone-store-api %{cornerstone_version} JPP/%{name} cornerstone-store-api
%if %{with_maven}
install -pm 644 cornerstone/store/api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-store-api.pom
%endif

install -pm 644 cornerstone/store/impl/target/cornerstone-store-impl-%{cornerstone_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/cornerstone-store-impl-%{cornerstone_version}.jar
%add_to_maven_depmap org.apache.avalon.cornerstone.store cornerstone-store-impl %{cornerstone_version} JPP/%{name} cornerstone-store-impl
%if %{with_maven}
install -pm 644 cornerstone/store/impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-store-impl.pom
%endif

install -pm 644 cornerstone/threads/api/target/cornerstone-threads-api-%{cornerstone_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/cornerstone-threads-api-%{cornerstone_version}.jar
%add_to_maven_depmap org.apache.avalon.cornerstone.threads cornerstone-threads-api %{cornerstone_version} JPP/%{name} cornerstone-threads-api
%if %{with_maven}
install -pm 644 cornerstone/threads/api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-threads-api.pom
%endif

install -pm 644 cornerstone/threads/impl/target/cornerstone-threads-impl-%{cornerstone_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/cornerstone-threads-impl-%{cornerstone_version}.jar
%add_to_maven_depmap org.apache.avalon.cornerstone.threads cornerstone-threads-impl %{cornerstone_version} JPP/%{name} cornerstone-threads-impl
%if %{with_maven}
install -pm 644 cornerstone/threads/impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-threads-impl.pom
%endif

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{cornerstone_version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{cornerstone_version}||g"`; done)

install -pm 644 deprecated/component/target/excalibur-component-%{excalidep_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-component-%{excalidep_version}.jar
%add_to_maven_depmap org.apache.excalibur.component excalibur-component %{excalidep_version} JPP/%{name} excalibur-component
%if %{with_maven}
install -pm 644 deprecated/component/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-component.pom
%endif

install -pm 644 deprecated/event/api/target/excalibur-event-api-%{excalidep_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-event-api-%{excalidep_version}.jar
%add_to_maven_depmap org.apache.excalibur.event excalibur-event-api %{excalidep_version} JPP/%{name} excalibur-event-api
%if %{with_maven}
install -pm 644 deprecated/event/api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-event-api.pom
%endif

install -pm 644 deprecated/event/impl/target/excalibur-event-impl-%{excalidep_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-event-impl-%{excalidep_version}.jar
%add_to_maven_depmap org.apache.excalibur.event excalibur-event-impl %{excalidep_version} JPP/%{name} excalibur-event-impl
%if %{with_maven}
install -pm 644 deprecated/event/impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-event-impl.pom
%endif

install -pm 644 deprecated/testcase/target/excalibur-testcase-%{excalidep_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-testcase-%{excalidep_version}.jar
%add_to_maven_depmap org.apache.excalibur.testcase excalibur-testcase %{excalidep_version} JPP/%{name} excalibur-testcase
%if %{with_maven}
install -pm 644 deprecated/testcase/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-testcase.pom
%endif

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{excalidep_version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{excalidep_version}||g"`; done)

install -pm 644 fortress/bean/target/excalibur-fortress-bean-%{fortress_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-fortress-bean-%{fortress_version}.jar
%add_to_maven_depmap org.apache.excalibur.fortress.bean excalibur-fortress-bean %{fortress_version} JPP/%{name} excalibur-fortress-bean
%if %{with_maven}
install -pm 644 fortress/bean/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-fortress-bean.pom
%endif

install -pm 644 fortress/container-api/target/excalibur-fortress-container-api-%{fortress_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-fortress-container-api-%{fortress_version}.jar
%add_to_maven_depmap org.apache.excalibur.fortress.container excalibur-fortress-container-api %{fortress_version} JPP/%{name} excalibur-fortress-container-api
%if %{with_maven}
install -pm 644 fortress/container-api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-fortress-container-api.pom
%endif

install -pm 644 fortress/container-impl/target/excalibur-fortress-container-impl-%{fortress_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-fortress-container-impl-%{fortress_version}.jar
%add_to_maven_depmap org.apache.excalibur.fortress.container excalibur-fortress-container-impl %{fortress_version} JPP/%{name} excalibur-fortress-container-impl
%if %{with_maven}
install -pm 644 fortress/container-impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-fortress-container-impl.pom
%endif

install -pm 644 fortress/examples/target/excalibur-fortress-examples-%{fortress_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-fortress-examples-%{fortress_version}.jar
%add_to_maven_depmap org.apache.excalibur.fortress.examples excalibur-fortress-examples %{fortress_version} JPP/%{name} excalibur-fortress-examples
%if %{with_maven}
install -pm 644 fortress/examples/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-fortress-examples.pom
%endif

install -pm 644 fortress/meta/target/excalibur-fortress-meta-%{fortress_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-fortress-meta-%{fortress_version}.jar
%add_to_maven_depmap org.apache.excalibur.fortress.meta excalibur-fortress-meta %{fortress_version} JPP/%{name} excalibur-fortress-meta
%if %{with_maven}
install -pm 644 fortress/meta/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-fortress-meta.pom
%endif

install -pm 644 fortress/migration/target/excalibur-fortress-migration-%{fortress_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-fortress-migration-%{fortress_version}.jar
%add_to_maven_depmap org.apache.excalibur.fortress.migration excalibur-fortress-migration %{fortress_version} JPP/%{name} excalibur-fortress-migration
%if %{with_maven}
install -pm 644 fortress/migration/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-fortress-migration.pom
%endif

%if %{with_maven}
install -pm 644 fortress/plugin/target/maven-fortress-plugin-%{fortress_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/maven-fortress-plugin-%{fortress_version}.jar
%add_to_maven_depmap org.apache.excalibur.fortress.meta maven-fortress-plugin %{fortress_version} JPP/%{name} maven-fortress-plugin
install -pm 644 fortress/plugin/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-maven-fortress-plugin.pom
%endif

install -pm 644 fortress/testcase/target/excalibur-fortress-testcase-%{fortress_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/excalibur-fortress-testcase-%{fortress_version}.jar
%add_to_maven_depmap org.apache.excalibur.fortress.testcase excalibur-fortress-testcase %{fortress_version} JPP/%{name} excalibur-fortress-testcase
%if %{with_maven}
install -pm 644 fortress/testcase/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-fortress-testcase.pom
%endif

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{fortress_version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{fortress_version}||g"`; done)

install -pm 644 framework/api/target/avalon-framework-api-%{framework_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/avalon-framework-api-%{framework_version}.jar
%add_to_maven_depmap org.apache.avalon.framework avalon-framework-api %{framework_version} JPP/%{name} avalon-framework-api
%if %{with_maven}
install -pm 644 framework/api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-avalon-framework-api.pom
%endif

install -pm 644 framework/impl/target/avalon-framework-impl-%{framework_version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/avalon-framework-impl-%{framework_version}.jar
%add_to_maven_depmap org.apache.avalon.framework avalon-framework-impl %{framework_version} JPP/%{name} avalon-framework-impl
%if %{with_maven}
install -pm 644 framework/impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-avalon-framework-impl.pom
%endif

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{framework_version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{framework_version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{framework_version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{framework_version}||g"`; done)

# other poms and depmap frags
#./components/pom.xml MISSING
install -pm 644 components/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-components.pom
%add_to_maven_depmap org.apache.excalibur.components excalibur-components-modules 1 JPP/%{name} excalibur-components
#./components/pool/pom.xml MISSING
install -pm 644 components/pool/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-pool.pom
%add_to_maven_depmap org.apache.excalibur.components excalibur-pool-modules 1 JPP/%{name} excalibur-pool
#./components/thread/pom.xml MISSING
install -pm 644 components/thread/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-thread.pom
%add_to_maven_depmap org.apache.excalibur.components excalibur-thread-modules 1 JPP/%{name} excalibur-thread
#./containerkit/instrument/pom.xml MISSING
install -pm 644 containerkit/instrument/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-instrument.pom
%add_to_maven_depmap org.apache.excalibur.containerkit excalibur-instrument-modules 1 JPP/%{name} excalibur-instrument
#./containerkit/lifecycle/pom.xml MISSING
install -pm 644 containerkit/lifecycle/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-lifecycle.pom
%add_to_maven_depmap org.apache.excalibur.containerkit excalibur-lifecycle-modules 1 JPP/%{name} excalibur-lifecycle
#./containerkit/pom.xml MISSING
install -pm 644 containerkit/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-containerkit.pom
%add_to_maven_depmap org.apache.excalibur.containerkit excalibur-containerkit 1 JPP/%{name} excalibur-containerkit
#./cornerstone/connection/pom.xml MISSING
install -pm 644 cornerstone/connection/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-connection.pom
%add_to_maven_depmap org.apache.avalon.cornerstone.connection cornerstone-connection 1 JPP/%{name} cornerstone-connection
#./cornerstone/datasources/pom.xml MISSING
install -pm 644 cornerstone/datasources/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-datasources.pom
%add_to_maven_depmap org.apache.avalon.cornerstone.datasources cornerstone-datasources 1 JPP/%{name} cornerstone-datasources
#./cornerstone/pom.xml MISSING
install -pm 644 cornerstone/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone.pom
%add_to_maven_depmap org.apache.avalon.cornerstone avalon-cornerstone-modules 1 JPP/%{name} cornerstone
#./cornerstone/scheduler/pom.xml MISSING
install -pm 644 cornerstone/scheduler/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-scheduler.pom
%add_to_maven_depmap org.apache.avalon.cornerstone.scheduler cornerstone-scheduler 1 JPP/%{name} cornerstone-scheduler
#./cornerstone/sockets/pom.xml MISSING
install -pm 644 cornerstone/sockets/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-sockets.pom
%add_to_maven_depmap org.apache.avalon.cornerstone.sockets cornerstone-sockets 1 JPP/%{name} cornerstone-sockets
#./cornerstone/store/pom.xml MISSING
install -pm 644 cornerstone/store/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-store.pom
%add_to_maven_depmap org.apache.avalon.cornerstone.store cornerstone-store 1 JPP/%{name} cornerstone-store
#./cornerstone/threads/pom.xml MISSING
install -pm 644 cornerstone/threads/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cornerstone-threads.pom
%add_to_maven_depmap org.apache.avalon.cornerstone.threads cornerstone-threads 1 JPP/%{name} cornerstone-threads
#./deprecated/event/pom.xml MISSING
install -pm 644 deprecated/event/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-event.pom
%add_to_maven_depmap org.apache.excalibur.event excalibur-event-modules 1 JPP/%{name} excalibur-event
#./deprecated/pom.xml MISSING
install -pm 644 deprecated/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-deprecated.pom
%add_to_maven_depmap org.apache.excalibur.deprecated excalibur-deprecated-modules 1 JPP/%{name} excalibur-deprecated
#./fortress/pom.xml MISSING
install -pm 644 fortress/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur-fortress.pom
%add_to_maven_depmap org.apache.excalibur.fortress excalibur-fortress-modules 1 JPP/%{name} excalibur-fortress
#./framework/pom.xml MISSING
install -pm 644 framework/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-avalon-framework.pom
%add_to_maven_depmap org.apache.avalon avalon-framework 1 JPP/%{name} avalon-framework
#./pom.xml MISSING
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-excalibur.pom
%add_to_maven_depmap org.apache.excalibur excalibur 1 JPP/%{name} excalibur

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-datasource-%{components_version}
cp -pr components/datasource/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-datasource-%{components_version}
ln -s %{name}-datasource-%{components_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-datasource

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-monitor-%{components_version}
cp -pr components/monitor/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-monitor-%{components_version}
ln -s %{name}-monitor-%{components_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-monitor

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-pool-api-%{components_version}
cp -pr components/pool/api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-pool-api-%{components_version}
ln -s %{name}-pool-api-%{components_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-pool-api

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-pool-impl-%{components_version}
cp -pr components/pool/impl/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-pool-impl-%{components_version}
ln -s %{name}-pool-impl-%{components_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-pool-impl

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-pool-instrumented-%{components_version}
cp -pr components/pool/instrumented/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-pool-instrumented-%{components_version}
ln -s %{name}-pool-instrumented-%{components_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-pool-instrumented

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-sourceresolve-%{components_version}
cp -pr components/sourceresolve/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-sourceresolve-%{components_version}
ln -s %{name}-sourceresolve-%{components_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-sourceresolve

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-store-%{components_version}
cp -pr components/store/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-store-%{components_version}
ln -s %{name}-store-%{components_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-store

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-thread-api-%{components_version}
cp -pr components/thread/api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-thread-api-%{components_version}
ln -s %{name}-thread-api-%{components_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-thread-api

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-thread-impl-%{components_version}
cp -pr components/thread/impl/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-thread-impl-%{components_version}
ln -s %{name}-thread-impl-%{components_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-thread-impl

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-thread-instrumented-%{components_version}
cp -pr components/thread/instrumented/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-thread-instrumented-%{components_version}
ln -s %{name}-thread-instrumented-%{components_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-thread-instrumented

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-xmlutil-%{components_version}
cp -pr components/xmlutil/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-xmlutil-%{components_version}
ln -s %{name}-xmlutil-%{components_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-xmlutil

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-instrument-api-%{containerkit_version}
cp -pr containerkit/instrument/api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-instrument-api-%{containerkit_version}
ln -s %{name}-instrument-api-%{containerkit_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-instrument-api

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-instrument-client-%{containerkit_version}
cp -pr containerkit/instrument/client/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-instrument-client-%{containerkit_version}
ln -s %{name}-instrument-client-%{containerkit_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-instrument-client

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-instrument-mgr-api-%{containerkit_version}
cp -pr containerkit/instrument/mgr-api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-instrument-mgr-api-%{containerkit_version}
ln -s %{name}-instrument-mgr-api-%{containerkit_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-instrument-mgr-api

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-instrument-mgr-http-%{containerkit_version}
cp -pr containerkit/instrument/mgr-http/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-instrument-mgr-http-%{containerkit_version}
ln -s %{name}-instrument-mgr-http-%{containerkit_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-instrument-mgr-http

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-instrument-mgr-impl-%{containerkit_version}
cp -pr containerkit/instrument/mgr-impl/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-instrument-mgr-impl-%{containerkit_version}
ln -s %{name}-instrument-mgr-impl-%{containerkit_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-instrument-mgr-impl

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-lifecycle-api-%{containerkit_version}
cp -pr containerkit/lifecycle/api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-lifecycle-api-%{containerkit_version}
ln -s %{name}-lifecycle-api-%{containerkit_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-lifecycle-api

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-lifecycle-impl-%{containerkit_version}
cp -pr containerkit/lifecycle/impl/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-lifecycle-impl-%{containerkit_version}
ln -s %{name}-lifecycle-impl-%{containerkit_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-lifecycle-impl

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-logger-%{containerkit_version}
cp -pr containerkit/logger/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-logger-%{containerkit_version}
ln -s %{name}-logger-%{containerkit_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-logger

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-avalon-logkit-%{containerkit_version}
cp -pr containerkit/logkit/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-avalon-logkit-%{containerkit_version}
ln -s %{name}-avalon-logkit-%{containerkit_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-avalon-logkit

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-connection-api-%{cornerstone_version}
cp -pr cornerstone/connection/api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-connection-api-%{cornerstone_version}
ln -s %{name}-cornerstone-connection-api-%{cornerstone_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-connection-api

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-connection-impl-%{cornerstone_version}
cp -pr cornerstone/connection/impl/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-connection-impl-%{cornerstone_version}
ln -s %{name}-cornerstone-connection-impl-%{cornerstone_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-connection-impl

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-datasources-api-%{cornerstone_version}
cp -pr cornerstone/datasources/api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-datasources-api-%{cornerstone_version}
ln -s %{name}-cornerstone-datasources-api-%{cornerstone_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-datasources-api

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-datasources-impl-%{cornerstone_version}
cp -pr cornerstone/datasources/impl/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-datasources-impl-%{cornerstone_version}
ln -s %{name}-cornerstone-datasources-impl-%{cornerstone_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-datasources-impl

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-scheduler-api-%{cornerstone_version}
cp -pr cornerstone/scheduler/api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-scheduler-api-%{cornerstone_version}
ln -s %{name}-cornerstone-scheduler-api-%{cornerstone_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-scheduler-api

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-scheduler-impl-%{cornerstone_version}
cp -pr cornerstone/scheduler/impl/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-scheduler-impl-%{cornerstone_version}
ln -s %{name}-cornerstone-scheduler-impl-%{cornerstone_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-scheduler-impl

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-sockets-api-%{cornerstone_version}
cp -pr cornerstone/sockets/api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-sockets-api-%{cornerstone_version}
ln -s %{name}-cornerstone-sockets-api-%{cornerstone_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-sockets-api

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-sockets-impl-%{cornerstone_version}
cp -pr cornerstone/sockets/impl/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-sockets-impl-%{cornerstone_version}
ln -s %{name}-cornerstone-sockets-impl-%{cornerstone_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-sockets-impl

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-store-api-%{cornerstone_version}
cp -pr cornerstone/store/api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-store-api-%{cornerstone_version}
ln -s %{name}-cornerstone-store-api-%{cornerstone_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-store-api

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-store-impl-%{cornerstone_version}
cp -pr cornerstone/store/impl/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-store-impl-%{cornerstone_version}
ln -s %{name}-cornerstone-store-impl-%{cornerstone_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-store-impl

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-threads-api-%{cornerstone_version}
cp -pr cornerstone/threads/api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-threads-api-%{cornerstone_version}
ln -s %{name}-cornerstone-threads-api-%{cornerstone_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-threads-api

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-threads-impl-%{cornerstone_version}
cp -pr cornerstone/threads/impl/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-threads-impl-%{cornerstone_version}
ln -s %{name}-cornerstone-threads-impl-%{cornerstone_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-cornerstone-threads-impl

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-component-%{excalidep_version}
cp -pr deprecated/component/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-component-%{excalidep_version}
ln -s %{name}-component-%{excalidep_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-component

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-event-api-%{excalidep_version}
cp -pr deprecated/event/api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-event-api-%{excalidep_version}
ln -s %{name}-event-api-%{excalidep_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-event-api

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-event-impl-%{excalidep_version}
cp -pr deprecated/event/impl/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-event-impl-%{excalidep_version}
ln -s %{name}-event-impl-%{excalidep_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-event-impl

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-testcase-%{excalidep_version}
cp -pr deprecated/testcase/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-testcase-%{excalidep_version}
ln -s %{name}-testcase-%{excalidep_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-testcase

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-bean-%{fortress_version}
cp -pr fortress/bean/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-bean-%{fortress_version}
ln -s %{name}-fortress-bean-%{fortress_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-bean

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-container-api-%{fortress_version}
cp -pr fortress/container-api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-container-api-%{fortress_version}
ln -s %{name}-fortress-container-api-%{fortress_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-container-api

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-container-impl-%{fortress_version}
cp -pr fortress/container-impl/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-container-impl-%{fortress_version}
ln -s %{name}-fortress-container-impl-%{fortress_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-container-impl

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-examples-%{fortress_version}
cp -pr fortress/examples/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-examples-%{fortress_version}
ln -s %{name}-fortress-examples-%{fortress_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-examples

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-meta-%{fortress_version}
cp -pr fortress/meta/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-meta-%{fortress_version}
ln -s %{name}-fortress-meta-%{fortress_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-meta

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-migration-%{fortress_version}
cp -pr fortress/migration/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-migration-%{fortress_version}
ln -s %{name}-fortress-migration-%{fortress_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-migration

%if %{with_maven}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-maven-fortress-plugin-%{fortress_version}
cp -pr fortress/plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-maven-fortress-plugin-%{fortress_version}
ln -s %{name}-maven-fortress-plugin-%{fortress_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-maven-fortress-plugin
%endif

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-testcase-%{fortress_version}
cp -pr fortress/testcase/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-testcase-%{fortress_version}
ln -s %{name}-fortress-testcase-%{fortress_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-fortress-testcase

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-avalon-framework-api-%{framework_version}
cp -pr framework/api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-avalon-framework-api-%{framework_version}
ln -s %{name}-avalon-framework-api-%{framework_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-avalon-framework-api

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-avalon-framework-impl-%{framework_version}
cp -pr framework/impl/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-avalon-framework-impl-%{framework_version}
ln -s %{name}-avalon-framework-impl-%{framework_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-avalon-framework-impl

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/fortress
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/fortress/bin
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/fortress/conf
install -d -m 755 $RPM_BUILD_ROOT%{_var}/log/fortress
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
ln -sf %{_datadir}/fortress/conf $RPM_BUILD_ROOT%{_sysconfdir}/fortress
ln -sf %{_var}/log/fortress $RPM_BUILD_ROOT%{_datadir}/fortress/logs

install -m 755 fortress/platform/src/bin/*.sh $RPM_BUILD_ROOT%{_datadir}/fortress/bin
install -m 755 fortress/platform/src/conf/* $RPM_BUILD_ROOT%{_datadir}/fortress/conf

%if %with repolib
%define repodir %{_javadir}/repository.jboss.com/apache-avalon-logkit/%{containerkit_version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE101} $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/@CONTAINERKIT_VERSION@/%{containerkit_version}/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH3} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH4} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH5} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH6} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/avalon-logkit-%{containerkit_version}.jar $RPM_BUILD_ROOT%{repodirlib}/logkit.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm \
        --exclude /usr/share/java/avalon-framework-%{framework_version}.jar
%endif

%files
%dir %{_javadir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%endif
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files avalon-framework
%{_javadir}/%{name}/avalon-framework-%{framework_version}.jar
%{_javadir}/%{name}/avalon-framework.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/avalon-framework*-%{framework_version}.jar.*
%endif

%if %with repolib
%define repodir %{_javadir}/repository.jboss.com/apache-avalon/%{framework_version}-brew
%files avalon-framework-repolib
%{repodir}
%endif

%files avalon-framework-api
%{_javadir}/%{name}/avalon-framework-api*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/avalon-framework-api*-%{framework_version}.jar.*
%endif

%files avalon-framework-impl
%{_javadir}/%{name}/avalon-framework-impl*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/avalon-framework-impl*-%{framework_version}.jar.*
%endif

%files avalon-logkit
%{_javadir}/%{name}/avalon-logkit*

%if %{gcj_support}
%{_libdir}/gcj/%{name}/avalon-logkit*-%{containerkit_version}.jar.*
%endif

%if %with repolib
%define repodir %{_javadir}/repository.jboss.com/apache-avalon-logkit/%{containerkit_version}-brew
%files avalon-logkit-repolib
%{repodir}
%endif

%files cornerstone-connection-api
%{_javadir}/%{name}/cornerstone-connection-api*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/cornerstone-connection-api*-%{cornerstone_version}.jar.*
%endif

%files cornerstone-connection-impl
%{_javadir}/%{name}/cornerstone-connection-impl*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/cornerstone-connection-impl*-%{cornerstone_version}.jar.*
%endif

%files cornerstone-datasources-api
%{_javadir}/%{name}/cornerstone-datasources-api*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/cornerstone-datasources-api*-%{cornerstone_version}.jar.*
%endif

%files cornerstone-datasources-impl
%{_javadir}/%{name}/cornerstone-datasources-impl*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/cornerstone-datasources-impl*-%{cornerstone_version}.jar.*
%endif

%files cornerstone-scheduler-api
%{_javadir}/%{name}/cornerstone-scheduler-api*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/cornerstone-scheduler-api*-%{cornerstone_version}.jar.*
%endif

%files cornerstone-scheduler-impl
%{_javadir}/%{name}/cornerstone-scheduler-impl*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/cornerstone-scheduler-impl*-%{cornerstone_version}.jar.*
%endif

%files cornerstone-sockets-api
%{_javadir}/%{name}/cornerstone-sockets-api*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/cornerstone-sockets-api*-%{cornerstone_version}.jar.*
%endif

%files cornerstone-sockets-impl
%{_javadir}/%{name}/cornerstone-sockets-impl*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/cornerstone-sockets-impl*-%{cornerstone_version}.jar.*
%endif

%files cornerstone-store-api
%{_javadir}/%{name}/cornerstone-store-api*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/cornerstone-store-api*-%{cornerstone_version}.jar.*
%endif

%files cornerstone-store-impl
%{_javadir}/%{name}/cornerstone-store-impl*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/cornerstone-store-impl*-%{cornerstone_version}.jar.*
%endif

%files cornerstone-threads-api
%{_javadir}/%{name}/cornerstone-threads-api*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/cornerstone-threads-api*-%{cornerstone_version}.jar.*
%endif

%files cornerstone-threads-impl
%{_javadir}/%{name}/cornerstone-threads-impl*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/cornerstone-threads-impl*-%{cornerstone_version}.jar.*
%endif

%files component
%{_javadir}/%{name}/excalibur-component.jar
%{_javadir}/%{name}/excalibur-component-%{excalidep_version}.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-component-%{excalidep_version}.jar.*
%endif

%files datasource
%{_javadir}/%{name}/excalibur-datasource*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-datasource-%{components_version}.jar.*
%endif

%files event-api
%{_javadir}/%{name}/excalibur-event-api*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-event-api-%{excalidep_version}.jar.*
%endif

%files event-impl
%{_javadir}/%{name}/excalibur-event-impl*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-event-impl-%{excalidep_version}.jar.*
%endif

%files fortress-bean
%{_javadir}/%{name}/excalibur-fortress-bean*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-fortress-bean-%{fortress_version}.jar.*
%endif

%files fortress-container-api
%{_javadir}/%{name}/excalibur-fortress-container-api*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-fortress-container-api-%{fortress_version}.jar.*
%endif

%files fortress-container-impl
%{_javadir}/%{name}/excalibur-fortress-container-impl*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-fortress-container-impl-%{fortress_version}.jar.*
%endif

%files fortress-examples
%{_javadir}/%{name}/excalibur-fortress-examples*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-fortress-examples-%{fortress_version}.jar.*
%endif

%files fortress-meta
%{_javadir}/%{name}/excalibur-fortress-meta*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-fortress-meta-%{fortress_version}.jar.*
%endif

%files fortress-migration
%{_javadir}/%{name}/excalibur-fortress-migration*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-fortress-migration-%{fortress_version}.jar.*
%endif

%files fortress-platform
%dir %{_datadir}/fortress
%dir %{_datadir}/fortress/bin
%dir %{_datadir}/fortress/conf
%{_datadir}/fortress/logs
%{_sysconfdir}/fortress
%{_var}/log/fortress
%attr(0755,root,root) %{_datadir}/fortress/bin/*
%attr(0755,root,root) %{_datadir}/fortress/conf/*

%files fortress-testcase
%{_javadir}/%{name}/excalibur-fortress-testcase*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-fortress-testcase-%{fortress_version}.jar.*
%endif

%files instrument-api
%{_javadir}/%{name}/excalibur-instrument-api*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-instrument-api-%{containerkit_version}.jar.*
%endif

%files instrument-client
%{_javadir}/%{name}/excalibur-instrument-client*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-instrument-client-%{containerkit_version}.jar.*
%endif

%files instrument-mgr-api
%{_javadir}/%{name}/excalibur-instrument-mgr-api*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-instrument-mgr-api-%{containerkit_version}.jar.*
%endif

%files instrument-mgr-http
%{_javadir}/%{name}/excalibur-instrument-mgr-http*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-instrument-mgr-http-%{containerkit_version}.jar.*
%endif

%files instrument-mgr-impl
%{_javadir}/%{name}/excalibur-instrument-mgr-impl*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-instrument-mgr-impl-%{containerkit_version}.jar.*
%endif

%files lifecycle-api
%{_javadir}/%{name}/excalibur-lifecycle-api*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-lifecycle-api-%{containerkit_version}.jar.*
%endif

%files lifecycle-impl
%{_javadir}/%{name}/excalibur-lifecycle-impl*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-lifecycle-impl-%{containerkit_version}.jar.*
%endif

%files logger
%{_javadir}/%{name}/excalibur-logger*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-logger-%{containerkit_version}.jar.*
%endif

%files monitor
%{_javadir}/%{name}/excalibur-monitor*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-monitor-%{components_version}.jar.*
%endif

%files pool-api
%{_javadir}/%{name}/excalibur-pool-api*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-pool-api-%{components_version}.jar.*
%endif

%files pool-impl
%{_javadir}/%{name}/excalibur-pool-impl*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-pool-impl-%{components_version}.jar.*
%endif

%files pool-instrumented
%{_javadir}/%{name}/excalibur-pool-instrumented*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-pool-instrumented-%{components_version}.jar.*
%endif

%files sourceresolve
%{_javadir}/%{name}/excalibur-sourceresolve*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-sourceresolve-%{components_version}.jar.*
%endif

%files store
%{_javadir}/%{name}/excalibur-store*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-store-%{components_version}.jar.*
%endif

%files testcase
%{_javadir}/%{name}/excalibur-testcase*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-testcase-%{excalidep_version}.jar.*
%endif

%files thread-api
%{_javadir}/%{name}/excalibur-thread-api*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-thread-api-%{components_version}.jar.*
%endif

%files thread-impl
%{_javadir}/%{name}/excalibur-thread-impl*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-thread-impl-%{components_version}.jar.*
%endif

%files thread-instrumented
%{_javadir}/%{name}/excalibur-thread-instrumented*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-thread-instrumented-%{components_version}.jar.*
%endif

%files xmlutil
%{_javadir}/%{name}/excalibur-xmlutil*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/excalibur-xmlutil-%{components_version}.jar.*
%endif

%if %{with_maven}
%files maven-fortress-plugin
%{_javadir}/%{name}/maven-fortress-plugin*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/maven-fortress-plugin-%{fortress_version}.jar.*
%endif
%endif

%files avalon-framework-api-javadoc
%{_javadocdir}/%{name}-avalon-framework-api-%{framework_version}
%{_javadocdir}/%{name}-avalon-framework-api

%files avalon-framework-impl-javadoc
%{_javadocdir}/%{name}-avalon-framework-impl-%{framework_version}
%{_javadocdir}/%{name}-avalon-framework-impl

%files avalon-logkit-javadoc
%{_javadocdir}/%{name}-avalon-logkit-%{containerkit_version}
%{_javadocdir}/%{name}-avalon-logkit

%files cornerstone-connection-api-javadoc
%{_javadocdir}/%{name}-cornerstone-connection-api-%{cornerstone_version}
%{_javadocdir}/%{name}-cornerstone-connection-api

%files cornerstone-connection-impl-javadoc
%{_javadocdir}/%{name}-cornerstone-connection-impl-%{cornerstone_version}
%{_javadocdir}/%{name}-cornerstone-connection-impl

%files cornerstone-datasources-api-javadoc
%{_javadocdir}/%{name}-cornerstone-datasources-api-%{cornerstone_version}
%{_javadocdir}/%{name}-cornerstone-datasources-api

%files cornerstone-datasources-impl-javadoc
%{_javadocdir}/%{name}-cornerstone-datasources-impl-%{cornerstone_version}
%{_javadocdir}/%{name}-cornerstone-datasources-impl

%files cornerstone-scheduler-api-javadoc
%{_javadocdir}/%{name}-cornerstone-scheduler-api-%{cornerstone_version}
%{_javadocdir}/%{name}-cornerstone-scheduler-api

%files cornerstone-scheduler-impl-javadoc
%{_javadocdir}/%{name}-cornerstone-scheduler-impl-%{cornerstone_version}
%{_javadocdir}/%{name}-cornerstone-scheduler-impl

%files cornerstone-sockets-api-javadoc
%{_javadocdir}/%{name}-cornerstone-sockets-api-%{cornerstone_version}
%{_javadocdir}/%{name}-cornerstone-sockets-api

%files cornerstone-sockets-impl-javadoc
%{_javadocdir}/%{name}-cornerstone-sockets-impl-%{cornerstone_version}
%{_javadocdir}/%{name}-cornerstone-sockets-impl

%files cornerstone-store-api-javadoc
%{_javadocdir}/%{name}-cornerstone-store-api-%{cornerstone_version}
%{_javadocdir}/%{name}-cornerstone-store-api

%files cornerstone-store-impl-javadoc
%{_javadocdir}/%{name}-cornerstone-store-impl-%{cornerstone_version}
%{_javadocdir}/%{name}-cornerstone-store-impl

%files cornerstone-threads-api-javadoc
%{_javadocdir}/%{name}-cornerstone-threads-api-%{cornerstone_version}
%{_javadocdir}/%{name}-cornerstone-threads-api

%files cornerstone-threads-impl-javadoc
%{_javadocdir}/%{name}-cornerstone-threads-impl-%{cornerstone_version}
%{_javadocdir}/%{name}-cornerstone-threads-impl

%files component-javadoc
%{_javadocdir}/%{name}-component-%{excalidep_version}
%{_javadocdir}/%{name}-component

%files datasource-javadoc
%{_javadocdir}/%{name}-datasource-%{components_version}
%{_javadocdir}/%{name}-datasource

%files event-api-javadoc
%{_javadocdir}/%{name}-event-api-%{excalidep_version}
%{_javadocdir}/%{name}-event-api

%files event-impl-javadoc
%{_javadocdir}/%{name}-event-impl-%{excalidep_version}
%{_javadocdir}/%{name}-event-impl

%files fortress-bean-javadoc
%{_javadocdir}/%{name}-fortress-bean-%{fortress_version}
%{_javadocdir}/%{name}-fortress-bean

%files fortress-container-api-javadoc
%{_javadocdir}/%{name}-fortress-container-api-%{fortress_version}
%{_javadocdir}/%{name}-fortress-container-api

%files fortress-container-impl-javadoc
%{_javadocdir}/%{name}-fortress-container-impl-%{fortress_version}
%{_javadocdir}/%{name}-fortress-container-impl

%files fortress-examples-javadoc
%{_javadocdir}/%{name}-fortress-examples-%{fortress_version}
%{_javadocdir}/%{name}-fortress-examples

%files fortress-meta-javadoc
%{_javadocdir}/%{name}-fortress-meta-%{fortress_version}
%{_javadocdir}/%{name}-fortress-meta

%files fortress-migration-javadoc
%{_javadocdir}/%{name}-fortress-migration-%{fortress_version}
%{_javadocdir}/%{name}-fortress-migration

%if 0
%files fortress-platform-javadoc
%{_javadocdir}/%{name}-fortress-platform-%{fortress_version}
%{_javadocdir}/%{name}-fortress-platform
%endif

%files fortress-testcase-javadoc
%{_javadocdir}/%{name}-fortress-testcase-%{fortress_version}
%{_javadocdir}/%{name}-fortress-testcase

%files instrument-api-javadoc
%{_javadocdir}/%{name}-instrument-api-%{containerkit_version}
%{_javadocdir}/%{name}-instrument-api

%files instrument-client-javadoc
%{_javadocdir}/%{name}-instrument-client-%{containerkit_version}
%{_javadocdir}/%{name}-instrument-client

%files instrument-mgr-api-javadoc
%{_javadocdir}/%{name}-instrument-mgr-api-%{containerkit_version}
%{_javadocdir}/%{name}-instrument-mgr-api

%files instrument-mgr-http-javadoc
%{_javadocdir}/%{name}-instrument-mgr-http-%{containerkit_version}
%{_javadocdir}/%{name}-instrument-mgr-http

%files instrument-mgr-impl-javadoc
%{_javadocdir}/%{name}-instrument-mgr-impl-%{containerkit_version}
%{_javadocdir}/%{name}-instrument-mgr-impl

%files lifecycle-api-javadoc
%{_javadocdir}/%{name}-lifecycle-api-%{containerkit_version}
%{_javadocdir}/%{name}-lifecycle-api

%files lifecycle-impl-javadoc
%{_javadocdir}/%{name}-lifecycle-impl-%{containerkit_version}
%{_javadocdir}/%{name}-lifecycle-impl

%files logger-javadoc
%{_javadocdir}/%{name}-logger-%{containerkit_version}
%{_javadocdir}/%{name}-logger

%files monitor-javadoc
%{_javadocdir}/%{name}-monitor-%{components_version}
%{_javadocdir}/%{name}-monitor

%files pool-api-javadoc
%{_javadocdir}/%{name}-pool-api-%{components_version}
%{_javadocdir}/%{name}-pool-api

%files pool-impl-javadoc
%{_javadocdir}/%{name}-pool-impl-%{components_version}
%{_javadocdir}/%{name}-pool-impl

%files pool-instrumented-javadoc
%{_javadocdir}/%{name}-pool-instrumented-%{components_version}
%{_javadocdir}/%{name}-pool-instrumented

%files sourceresolve-javadoc
%{_javadocdir}/%{name}-sourceresolve-%{components_version}
%{_javadocdir}/%{name}-sourceresolve

%files store-javadoc
%{_javadocdir}/%{name}-store-%{components_version}
%{_javadocdir}/%{name}-store

%files testcase-javadoc
%{_javadocdir}/%{name}-testcase-%{excalidep_version}
%{_javadocdir}/%{name}-testcase

%files thread-api-javadoc
%{_javadocdir}/%{name}-thread-api-%{components_version}
%{_javadocdir}/%{name}-thread-api

%files thread-impl-javadoc
%{_javadocdir}/%{name}-thread-impl-%{components_version}
%{_javadocdir}/%{name}-thread-impl

%files thread-instrumented-javadoc
%{_javadocdir}/%{name}-thread-instrumented-%{components_version}
%{_javadocdir}/%{name}-thread-instrumented

%files xmlutil-javadoc
%{_javadocdir}/%{name}-xmlutil-%{components_version}
%{_javadocdir}/%{name}-xmlutil

%if %{with_maven}
%files maven-fortress-plugin-javadoc
%{_javadocdir}/%{name}-maven-fortress-plugin-%{fortress_version}
%{_javadocdir}/%{name}-maven-fortress-plugin
%endif

%changelog
* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt8_0.r508111.16jpp6
- fixed build with maven3

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt7_0.r508111.16jpp6
- remoded depracation on avalon-framework/logkut

* Mon Feb 06 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt6_0.r508111.16jpp6
- new jpp relase

* Mon Mar 14 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt6_0.r508111.14jpp6
- jpp 6 release; obsoletes; avalon-framework, avalon-logkit

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt6_0.r508111.13jpp5
- selected java5 compiler explicitly

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt5_0.r508111.13jpp5
- removed avalon-* provides (now separate packages)

* Sat Jan 24 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt4_0.r508111.13jpp5
- restored avalon-logkit provides

* Thu Jan 22 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt3_0.r508111.13jpp5
- restored avalon-* provides

* Sun Jan 18 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt2_0.r508111.13jpp5
- get rid of saxon 7

* Mon Dec 17 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_0.r508111.3jpp1.7
- converted from JPackage by jppimport script

