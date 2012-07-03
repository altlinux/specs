# hack
BuildRequires: geronimo-corba-2.3-apis geronimo-qname-1.1-api
Requires: geronimo-corba-2.3-apis geronimo-qname-1.1-api

BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with tests
%bcond_with tests

%define bname       geronimo

%define sver_activation_1_0_2 1.2
%define sver_activation_1_1 1.0
%define sver_annotation_1_0 1.1.0
%define sver_corba_1_0 1.0
%define sver_corba_2_3 1.1
%define sver_corba_3_0 1.1
%define sver_ejb_2_1 1.1
%define sver_ejb_3_0 1.0
%define sver_el_1_0 1.0
%define sver_interceptor_3_0 1.0
%define sver_j2ee_connector_1_5 1.1.1
%define sver_j2ee_deployment_1_1 1.1
%define sver_javaee_deployment_1_1MR3 1.0
%define sver_j2ee_jacc_1_0 1.1
%define sver_jacc_1_1 1.1
%define sver_j2ee_management_1_0 1.1
%define sver_j2ee_management_1_1 1.0
%define sver_javamail_1_3_1 1.3
%define sver_javamail_1_4 1.1
%define sver_jaxr_1_0 1.1
%define sver_jaxrpc_1_1 1.1
%define sver_jms_1_1 1.1
%define sver_jpa_3_0 1.1.0
%define sver_jsp_2_0 1.1
%define sver_jsp_2_1 1.0
%define sver_jta_1_0_1B 1.1.1
%define sver_jta_1_1 1.1.0
%define sver_qname_1_1 1.1
%define sver_saaj_1_1 1.1
%define sver_servlet_2_4 1.1.1
%define sver_servlet_2_5 1.1
%define sver_stax_1_0 1.0
%define sver_ws_metadata_2_0 1.1.1
%define sver_commonj_1_1 1.0

Summary:        Geronimo J2EE server J2EE specifications
URL:            http://geronimo.apache.org/
Name:           geronimo-specs
Version:        1.2
Release:        alt8_16jpp6
Epoch:          0
License:        ASL 2.0
Group:          Development/Java
Source0:        %{name}-%{version}-src.tar.gz
# STEPS TO CREATE THE SOURCE FILE
# mkdir geronimo-specs-1.2
# cd geronimo-specs-1.2
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-activation_1.0.2_spec-1.2/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-activation_1.1_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-annotation_1.0_spec-1.1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-ejb_2.1_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-ejb_3.0_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-el_1.0_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-interceptor_3.0_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-j2ee-connector_1.5_spec-1.1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-j2ee-deployment_1.1_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-j2ee-jacc_1.0_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-j2ee-management_1.0_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-j2ee-management_1.1_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jacc_1.1_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-javaee-deployment_1.1MR3_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-javamail_1.3.1_spec-1.3/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-javamail_1.4_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jaxr_1.0_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jaxrpc_1.1_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jms_1.1_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jpa_3.0_spec-1.1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jsp_2.0_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jsp_2.1_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jta_1.0.1B_spec-1.1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jta_1.1_spec-1.1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-qname_1.1_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-saaj_1.1_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-servlet_2.4_spec-1.1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-servlet_2.5_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-stax-api_1.0_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-ws-metadata_2.0_spec-1.1.1/
# # AND FOR COMPLETENESS
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/1_1_1/geronimo-spec-commonj/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/1_1_1/geronimo-spec-corba/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/1_1_1/geronimo-spec-corba-2.3/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/1_1_1/geronimo-spec-corba-3.0/
# # AS WELL AS
# svn export http://svn.apache.org/repos/asf/geronimo/specs/trunk/geronimo-jaspi_1.0_spec/
# # AND
# curl -O http://svn.apache.org/repos/asf/geronimo/specs/trunk/pom.xml
# curl -O http://svn.apache.org/repos/asf/geronimo/specs/trunk/LICENSE.txt
# curl -O http://svn.apache.org/repos/asf/geronimo/specs/trunk/NOTICE.txt
# curl -O http://svn.apache.org/repos/asf/geronimo/specs/trunk/README.txt
# 

Source1:        %{name}-jpp-depmap.xml
Source2:        %{name}-settings.xml

Patch0:         geronimo-specs-1.2-pom_xml.patch
Patch1:         geronimo-specs-jta-1.0.1B-pom_xml.patch
Patch2:         geronimo-specs-j2ee-connector-1.5-pom_xml.patch
Patch3:         geronimo-specs-servlet-2.4-pom_xml.patch
Patch4:         geronimo-specs-j2ee-1.4-pom_xml.patch
Patch5:         geronimo-specs-corba-2.3-pom_xml.patch

Patch101:       geronimo-specs-1.2-servlet_2.5-pom_xml.patch

BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  maven2 >= 0:2.0.4
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven-shared-file-management
BuildRequires:  sed
BuildRequires:  saxon
BuildRequires:  saxon-scripts
# TODO: USE   org.apache.geronimo.genesis.plugins:tools-maven-plugin
BuildRequires:  geronimo-genesis
BuildRequires:  maven-plugin-bundle
BuildRequires:  apache-commons-parent

BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-idea
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-one
BuildRequires:  maven-release
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven-surefire-plugin
BuildRequires:  excalibur-avalon-framework
BuildRequires:  excalibur-avalon-logkit
BuildRequires:  mojo-maven2-plugin-idlj
BuildRequires:  jacorb >= 0:2.3.0-11
BuildRequires:  junit >= 0:3.8.1
BuildRequires:  mockobjects >= 0:0.09
BuildRequires:  mockobjects < 0:0.10
BuildRequires:  mockobjects-jdk1.4-j2ee1.4 >= 0:0.09
BuildRequires:  mockobjects-jdk1.4-j2ee1.4 < 0:0.10
BuildRequires:  mx4j >= 0:2.0.1
BuildRequires:  ws-scout
# FIXME: (dwalluck): bootstrap issues
# BuildRequires:  geronimo-specs
# FIXED: (rapel) disregard the following
# for maven2-plugin-jar
# BuildRequires:  maven-shared-archiver

Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
# The main package has links to all specs, so it requires all subpackages
# except j2ee-schema (not linked) and javadocs
Requires:       geronimo-commonj-1.1-apis = %{version}-%{release}
Requires:       geronimo-jaf-1.0.2-api = %{version}-%{release}
Requires:       geronimo-jaf-1.1-api = %{version}-%{release}
Requires:       geronimo-annotation-1.0-api = %{version}-%{release}
Requires:       geronimo-corba-1.0-apis = %{version}-%{release}
Requires:       geronimo-corba-2.3-apis = %{version}-%{release}
Requires:       geronimo-corba-3.0-apis = %{version}-%{release}
Requires:       geronimo-ejb-2.1-api = %{version}-%{release}
Requires:       geronimo-ejb-3.0-api = %{version}-%{release}
Requires:       geronimo-el-1.0-api = %{version}-%{release}
Requires:       geronimo-interceptor-3.0-api = %{version}-%{release}
Requires:       geronimo-j2ee-1.4-apis = %{version}-%{release}
Requires:       geronimo-j2ee-connector-1.5-api = %{version}-%{release}
Requires:       geronimo-j2ee-deployment-1.1-api = %{version}-%{release}
Requires:       geronimo-javaee-deployment-1.1-api = %{version}-%{release}
Requires:       geronimo-jacc-1.0-api = %{version}-%{release}
Requires:       geronimo-jacc-1.1-api = %{version}-%{release}
Requires:       geronimo-j2ee-management-1.0-api = %{version}-%{release}
Requires:       geronimo-j2ee-management-1.1-api = %{version}-%{release}
Requires:       geronimo-javamail-1.3.1-api = %{version}-%{release}
Requires:       geronimo-javamail-1.4-api = %{version}-%{release}
Requires:       geronimo-jaxr-1.0-api = %{version}-%{release}
Requires:       geronimo-jaxrpc-1.1-api = %{version}-%{release}
Requires:       geronimo-jms-1.1-api = %{version}-%{release}
Requires:       geronimo-jpa-3.0-api = %{version}-%{release}
Requires:       geronimo-jsp-2.0-api = %{version}-%{release}
Requires:       geronimo-jsp-2.1-api = %{version}-%{release}
Requires:       geronimo-jta-1.0.1B-api = %{version}-%{release}
Requires:       geronimo-jta-1.1-api = %{version}-%{release}
Requires:       geronimo-qname-1.1-api = %{version}-%{release}
Requires:       geronimo-saaj-1.1-api = %{version}-%{release}
Requires:       geronimo-servlet-2.4-api = %{version}-%{release}
Requires:       geronimo-servlet-2.5-api = %{version}-%{release}
Requires:       geronimo-stax-1.0-api = %{version}-%{release}
Requires:       geronimo-ws-metadata-2.0-api = %{version}-%{release}
BuildArch:      noarch
Source44: import.info
Patch33: geronimo-specs-1.2-pom_xml-alt-kill-parent.patch
# poms moved to corresponding subpackages
Provides:  geronimo-specs-poms = %version-%release
Conflicts: geronimo-specs-poms < 1.2-alt4_17jpp6
Obsoletes: geronimo-specs-poms < 1.2-alt4_17jpp6

%description
Geronimo is Apache's ASF-licenced J2EE server project.
These are the J2EE-Specifications
Note: You should use the subpackages for the Specifications
that you actually need.  The ones installed by the main package
are deprecated and will disapear in future releases.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package -n geronimo-commonj-1.1-apis
Summary:        CommonJ APIs
Group:          Development/Java
Provides:       commonj_1_1_apis = %{version}-%{release}
Provides:       commonj_apis = 0:1.1
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-commonj-1.1-apis
CommonJ Spec

%package -n geronimo-jaf-1.0.2-api
Summary:        J2EE JAF v1.0.2 API
Group:          Development/Java
Provides:       jaf = 0:1.0.2
# TODO: drop asap
Provides:       jaf_1_0_2_api = %{version}-%{release}
Provides:       activation_1_0_2_api = %{version}-%{release}
Provides:       jaf_api = 0:1.0.2
Provides:       activation_api = 0:1.0.2
# Don't obsolete jaf, classpathx-jaf provides it
# Don't even obsolete it versioned, as sun-jaf is at 1.1
#Obsoletes:     jaf
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes: geronimo-specs-activation < 1.1

%description -n geronimo-jaf-1.0.2-api
Java Activation Framework 1.0.2

%package -n geronimo-jaf-1.1-api
Summary:        J2EE JAF v1.1 API
Group:          Development/Java
Provides:       jaf = 0:1.1
# TODO: drop asap
Provides:       jaf_1_1_api = %{version}-%{release}
Provides:       activation_1_1_api = %{version}-%{release}
Provides:       jaf_api = 0:1.1
Provides:       activation_api = 0:1.1
# Don't obsolete jaf, classpathx-jaf provides it
# Don't even obsolete it versioned, as sun-jaf is at 1.1
#Obsoletes:     jaf
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-jaf-1.1-api
Java Activation Framework 1.1

%package -n geronimo-annotation-1.0-api
Summary:        JEE Common Annotations v1.0
Group:          Development/Java
Provides:       annotation_1_0_api
Provides:       annotation_api = 0:1.0
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-annotation-1.0-api
JEE Common Annotations v1.0

%package -n geronimo-corba-1.0-apis
Summary:        CORBA v1.0 APIs
Group:          Development/Java
Provides:       corba_1_0_apis = %{version}-%{release}
Provides:       corba_apis = 0:1.0
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-corba-1.0-apis
CORBA 1.0 Spec

%package -n geronimo-corba-2.3-apis
Summary:        CORBA v2.3 APIs
Group:          Development/Java
Provides:       corba_2_3_apis = %{version}-%{release}
Provides:       corba_apis = 0:2.3
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-corba-2.3-apis
CORBA 2.3 Spec

%package -n geronimo-corba-3.0-apis
Summary:        CORBA v3.0 APIs
Group:          Development/Java
Provides:       corba_3_0_apis = %{version}-%{release}
Provides:       corba_apis = 0:3.0
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes: geronimo-specs-corba < 1.1

%description -n geronimo-corba-3.0-apis
CORBA 3.0 Spec

%package -n geronimo-ejb-2.1-api
Summary:        J2EE EJB v2.1 API
Group:          Development/Java
Provides:       ejb = 0:2.1
# TODO: drop asap
Provides:       ejb_2_1_api = %{version}-%{release}
Provides:       ejb_api = 0:2.1
# drop the following asap
Provides:       ejb
#Obsoletes:     ejb
Obsoletes:      geronimo-specs-compat <= 0:1.0
Requires:       jta_1_0_1B_api
Requires(preun):  alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes: geronimo-specs-ejb < 1.1

%description -n geronimo-ejb-2.1-api
Enterprise JavaBeans Specification 2.1

%package -n geronimo-ejb-3.0-api
Summary:        J2EE EJB v3.0 API
Group:          Development/Java
Provides:       ejb = 0:3.0
# TODO: drop asap
Provides:       ejb_3_0_api = %{version}-%{release}
Provides:       ejb_api = 0:3.0
#Obsoletes:     ejb
Obsoletes:      geronimo-specs-compat <= 0:1.0
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       annotation_1_0_api
Requires:       interceptor_3_0_api
Requires:       jta_1_1_api

%description -n geronimo-ejb-3.0-api
Enterprise JavaBeans Specification 3.0

%package -n geronimo-el-1.0-api
Summary:        Expression Language v1.0 API
Group:          Development/Java
Provides:       el_1_0_api = %{version}-%{release}
Provides:       el_api = 0:1.0
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-el-1.0-api
Expression Language 1.0

%package -n geronimo-interceptor-3.0-api
Summary:        Interceptor v3.0 API
Group:          Development/Java
Provides:       interceptor_3_0_api = %{version}-%{release}
Provides:       interceptor_api = 0:3.0
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-interceptor-3.0-api
Interceptor 3.0

%package -n geronimo-j2ee-1.4-apis
Summary:        J2EE v1.4 APIs
Group:          Development/Java
Provides:       jaf_api = 0:1.0.2
Provides:       jaf_1_0_2_api = %{epoch}:%{version}-%{release}
Provides:       commonj_apis = 0:1.1
Provides:       commonj_1_1_apis = %{epoch}:%{version}-%{release}
Provides:       corba_apis = 0:2.3
Provides:       corba_2_3_apis = %{epoch}:%{version}-%{release}
Provides:       ejb_api = 0:2.1
Provides:       ejb_2_1_api = %{epoch}:%{version}-%{release}
Provides:       j2ee_connector_api = 0:1.5
Provides:       j2ee_connector_1_5_api = %{epoch}:%{version}-%{release}
Provides:       j2ee_deployment_api = 0:1.1
Provides:       j2ee_deployment_1_1_api = %{epoch}:%{version}-%{release}
Provides:       j2ee_management_api = 0:1.0
Provides:       j2ee_management_1_0_api = %{epoch}:%{version}-%{release}
Provides:       jacc_api = 0:1.0
Provides:       jacc_1_0_api = %{epoch}:%{version}-%{release}
Provides:       javamail_api = 0:1.3.1
Provides:       javamail_1_3_1_api = %{epoch}:%{version}-%{release}
Provides:       jaxr_api = 0:1.0
Provides:       jaxr_1_0_api = %{epoch}:%{version}-%{release}
Provides:       jaxrpc_api = 0:1.1
Provides:       jaxrpc_1_1_api = %{epoch}:%{version}-%{release}
Provides:       jms_api = 0:1.1
Provides:       jms_1_1_api = %{epoch}:%{version}-%{release}
Provides:       jsp_api = 0:2.0
Provides:       jsp_2_0_api = %{epoch}:%{version}-%{release}
Provides:       jta_api = 0:1.0.1B
Provides:       jta_1_0_1B_api = %{epoch}:%{version}-%{release}
Provides:       qname_api = 0:1.1
Provides:       qname_1_1_api = %{epoch}:%{version}-%{release}
Provides:       saaj_api = 0:1.1
Provides:       saaj_1_1_api = %{epoch}:%{version}-%{release}
Provides:       servlet_api = 0:2.4
Provides:       servlet_2_4_api = %{epoch}:%{version}-%{release}
# XXX: (dwalluck): section added for backwards compatibility with Fedora 9
#
#Provides:      commonj = 0:1.1
### should also provide ejb.jar!
###Provides:       ejb = 0:2.1
#Provides:      corba = 0:2.3
Provides:       j2ee-connector = 0:1.5
Provides:       j2ee-deployment = 0:1.1
Provides:       j2ee-management = 0:1.0
Provides:       jacc = 0:1.0
### should also provide javamail.jar!
###Provides:       jaf = 0:1.0.2
###Provides:       javamail = 0:1.3.1
Provides:       jaxr = 0:1.0
Provides:       jaxrpc = 0:1.1
Provides:       jms = 0:1.1
Provides:       jsp = 0:2.0
Provides:       jta = 0:1.0.1B
#Provides:      qname = 0:1.1
Provides:       saaj = 0:1.1
Provides:       servlet = 0:2.4
# added Epoch
Provides:       geronimo-corba-2.3-apis = %{epoch}:%{version}-%{release}
# added Epoch
Provides:       geronimo-qname-1.1-api = %{epoch}:%{version}-%{release}
# Do not provide it as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#Provides:      javamail = 0:1.3.1
#
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-j2ee-1.4-apis
J2EE Specification (the complete set in one jar)

%package -n geronimo-j2ee-connector-1.5-api
Summary:        J2EE Connector v1.5 API
Group:          Development/Java
Provides:       j2ee_connector_1_5_api = %{version}-%{release}
Provides:       j2ee_connector_api = 0:1.5
# drop the following asap
Provides:       j2ee-connector = 0:1.5
Obsoletes:      j2ee-connector
Requires:       jta_1_0_1B_api
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes:      geronimo-specs-compat <= 0:1.0
Obsoletes: geronimo-specs-j2ee-connector < 1.1

%description -n geronimo-j2ee-connector-1.5-api
J2EE Connector Architecture Specification

%package -n geronimo-j2ee-deployment-1.1-api
Summary:        J2EE Deployment v1.1 API
Group:          Development/Java
Provides:       j2ee_deployment_1_1_api = %{version}-%{release}
Provides:       j2ee_deployment_api = 0:1.1
# drop the following asap
Provides:       j2ee-deployment = 0:1.1
Obsoletes:      j2ee-deployment
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes:      geronimo-specs-compat <= 0:1.0
Obsoletes: geronimo-specs-j2ee-deployment < 1.1

%description -n geronimo-j2ee-deployment-1.1-api
J2EE Application Deployment Specification

%package -n geronimo-javaee-deployment-1.1-api
Summary:        JEE Deployment v1.1 API
Group:          Development/Java
Provides:       javaee_deployment_1_1_api = %{version}-%{release}
Provides:       javaee_deployment_api = 0:1.1
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-javaee-deployment-1.1-api
JEE Application Deployment Specification

%package -n geronimo-jacc-1.0-api
Summary:        J2EE JACC v1.0 API
Group:          Development/Java
Provides:       jacc = 0:1.0
# TODO: drop asap
Provides:       jacc_1_0_api = %{version}-%{release}
Provides:       jacc_api = 0:1.0
Requires:       servlet_2_4_api
Requires(preun): alternatives
Requires(post): alternatives
Obsoletes:      geronimo-specs-compat <= 0:1.0
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes: geronimo-specs-j2ee-jacc < 1.1

%description -n geronimo-jacc-1.0-api
Java Authorization Contract for Containers Specification

%package -n geronimo-jacc-1.1-api
Summary:        J2EE JACC v1.1 API
Group:          Development/Java
Provides:       jacc_1_1_api = %{version}-%{release}
Provides:       jacc_api = 0:1.1
Requires:       servlet_2_5_api
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-jacc-1.1-api
Java Authorization Contract for Containers Specification

%package -n geronimo-j2ee-management-1.0-api
Summary:        J2EE Management v1.0 API
Group:          Development/Java
Provides:       j2ee_management_1_0_api = %{version}-%{release}
Provides:       j2ee_management_api = 0:1.0
# drop the following asap
Provides:       j2ee-management = 0:1.0
#Obsoletes:     j2ee-management
Requires:       ejb_2_1_api
Requires(preun):  alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes: geronimo-specs-j2ee-management < 1.1

%description -n geronimo-j2ee-management-1.0-api
J2EE Application Management Specification 1.0

%package -n geronimo-j2ee-management-1.1-api
Summary:        J2EE Management v1.1 API
Group:          Development/Java
Provides:       j2ee_management_1_1_api = %{version}-%{release}
Provides:       j2ee_management_api = 0:1.1
# drop the following asap
Provides:       j2ee-management = 0:1.1
#Obsoletes:     j2ee-management
Requires:       ejb_3_0_api
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-j2ee-management-1.1-api
J2EE Application Management Specification 1.1

%package -n geronimo-javamail-1.3.1-api
Summary:        J2EE JavaMail v1.3.1 API
Group:          Development/Java
Provides:       javamail_1_3_1_api = %{version}-%{release}
Provides:       javamail_api = 0:1.3.1
Requires:       jaf_1_0_2_api
Requires(preun): alternatives
Requires(post): alternatives
# Do not provide javamail as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#Provides:      javamail = 0:1.3.1
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes: geronimo-specs-javamail < 1.1

%description -n geronimo-javamail-1.3.1-api
JavaMail API 1.3.1

%package -n geronimo-javamail-1.4-api
Summary:        J2EE JavaMail v1.4 API
Group:          Development/Java
Provides:       javamail_1_4_api = %{version}-%{release}
Provides:       javamail_api = 0:1.4
Requires:       jaf_1_1_api
Requires(preun):  alternatives
Requires(post):  alternatives
# Do not provide javamail as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#Provides:      javamail = 0:1.4
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-javamail-1.4-api
JavaMail API 1.4

%package -n geronimo-jaxr-1.0-api
Summary:        J2EE JAXR v1.0 API
Group:          Development/Java
Provides:       jaxr_1_0_api = %{version}-%{release}
Provides:       jaxr_api = 0:1.0
# drop the following asap
Provides:       jaxr = 0:1.0
Obsoletes:      jaxr-api
Requires:       jaf_1_0_2_api
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes: geronimo-specs-jaxr < 1.1

%description -n geronimo-jaxr-1.0-api
Java API for XML Registries (JAXR)

%package -n geronimo-jaxrpc-1.1-api
Summary:        J2EE JAXRPC v1.1 API
Group:          Development/Java
Provides:       jaxrpc = 0:1.1
# TODO: drop asap
Provides:       jaxrpc_1_1_api = %{version}-%{release}
Provides:       jaxrpc_api = 0:1.1
Requires:       qname_1_1_api
Requires:       saaj_1_1_api
Requires:       servlet_2_4_api
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes: geronimo-specs-jaxrpc < 1.1

%description -n geronimo-jaxrpc-1.1-api
Java API for XML-Based RPC (JAXRPC)

%package -n geronimo-jms-1.1-api
Summary:        J2EE JMS v1.1 API
Group:          Development/Java
Provides:       jms_1_1_api = %{version}-%{release}
Provides:       jms_api = 0:1.1
# drop the following asap
Provides:       jms = 0:1.1
Obsoletes:      jms
Requires(preun): alternatives
Requires(post): alternatives
Obsoletes:      geronimo-specs-compat <= 0:1.0
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes: geronimo-specs-jms < 1.1

%description -n geronimo-jms-1.1-api
JMS Specification

%package -n geronimo-jpa-3.0-api
Summary:        JPA v3.0 API
Group:          Development/Java
Provides:       jpa_3_0_api = %{version}-%{release}
Provides:       jpa_api = 0:3.0
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-jpa-3.0-api
JPA Specification

%package -n geronimo-jsp-2.0-api
Summary:        J2EE JSP v2.0 API
Group:          Development/Java
Provides:       jsp = 0:2.0
# TODO: drop asap
Provides:       jsp_2_0_api = %{version}-%{release}
Provides:       jsp_api = 0:2.0
Requires:       servlet_2_4_api
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes: geronimo-specs-jsp < 1.1

%description -n geronimo-jsp-2.0-api
JavaServer Pages Specification 2.0

%package -n geronimo-jsp-2.1-api
Summary:        J2EE JSP v2.1 API
Group:          Development/Java
Provides:       jsp = 0:2.1
# TODO: drop asap
Provides:       jsp_2_1_api = %{version}-%{release}
Provides:       jsp_api = 0:2.1
Requires:       servlet_2_5_api
Requires:       el_1_0_api
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-jsp-2.1-api
JavaServer Pages Specification 2.1

%package -n geronimo-jta-1.0.1B-api
Summary:        J2EE JTA v1.0.1B API
Group:          Development/Java
Provides:       jta_1_0_1B_api = %{version}-%{release}
Provides:       jta_api = 0:1.0.1B
# drop the following asap
Provides:       jta = 0:1.0.1B
# Don't obsolete jta, as this is provided by java-1.4.2-gcj-compat
#Obsoletes:     jta
Requires(preun): alternatives
Requires(post): alternatives
Obsoletes:      geronimo-specs-compat <= 0:1.0
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes: geronimo-specs-jta < 1.1

%description -n geronimo-jta-1.0.1B-api
Java Transaction API Specification 1.0.1B

%package -n geronimo-jta-1.1-api
Summary:        J2EE JTA v1.1 API
Group:          Development/Java
Provides:       jta_1_1_api = %{version}-%{release}
Provides:       jta_api = 0:1.1
# drop the following asap
Provides:       jta = 0:1.1
# Don't obsolete jta, as this is provided by java-1.4.2-gcj-compat
#Obsoletes:     jta
Requires(preun): alternatives
Requires(post): alternatives
Obsoletes:      geronimo-specs-compat <= 0:1.0
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-jta-1.1-api
Java Transaction API Specification 1.1

%package -n geronimo-qname-1.1-api
Summary:        Namespace v1.1 API
Group:          Development/Java
Provides:       qname_1_1_api = %{version}-%{release}
Provides:       qname_api = 0:1.1
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes: geronimo-specs-qname < 1.1

%description -n geronimo-qname-1.1-api
javax.xml.namespace.QName API

%package -n geronimo-saaj-1.1-api
Summary:        J2EE SAAJ v1.1 API
Group:          Development/Java
Provides:       saaj = 0:1.1
# TODO: drop asap
Provides:       saaj_1_1_api = %{version}-%{release}
Provides:       saaj_api = 0:1.1
Requires:       jaf_1_0_2_api
Requires(preun): alternatives
Requires(post):  alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes: geronimo-specs-saaj < 1.1

%description -n geronimo-saaj-1.1-api
SOAP with Attachments API for Java (SAAJ)

%package -n geronimo-servlet-2.4-api
Summary:        J2EE Servlet v2.4 API
Group:          Development/Java
Provides:       servlet = 0:2.4
# TODO: drop asap
Provides:       servlet_2_4_api = %{version}-%{release}
Provides:       servlet_api = 0:2.4
Requires(preun): alternatives
Requires(post):  alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes: geronimo-specs-servlet < 1.1

%description -n geronimo-servlet-2.4-api
J2EE Servlet v2.4 API

%package -n geronimo-servlet-2.5-api
Summary:        J2EE Servlet v2.5 API
Group:          Development/Java
Provides:       servlet = 0:2.5
# TODO: drop asap
Provides:       servlet_2_5_api = %{version}-%{release}
Provides:       servlet_api = 0:2.5
Requires(preun): alternatives
Requires(post):  alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-servlet-2.5-api
J2EE Servlet v2.5 API

%package -n geronimo-stax-1.0-api
Summary:        XML Stax v1.0 API
Group:          Development/Java
Provides:       stax_1_0_api = %{version}-%{release}
Provides:       stax_api = 0:1.0
Requires(preun): alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-stax-1.0-api
XML STax v1.0 API

%package -n geronimo-ws-metadata-2.0-api
Summary:        Webservices Metadata v2.0 API
Group:          Development/Java
Provides:       ws_metadata_2_0_api = %{version}-%{release}
Provides:       ws_metadata_api = 0:2.0
Requires(preun):  alternatives
Requires(post): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n geronimo-ws-metadata-2.0-api
Webservices Metadata v2.0 API

%prep
%setup -q -n %{name}-%{version}
chmod -R go=u-w *
mkdir etc
cp -p LICENSE.txt etc

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1
%patch2 -p0 -b .sav2
%patch3 -p0 -b .sav3
%patch4 -p0 -b .sav4
%patch5 -p0 -b .sav5
cp -p %{SOURCE2} settings.xml
%patch101 -p0 -b .rap
%patch33 -p0

%build
export LANG=en_US.ISO8859-1

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
export CLASSPATH=
export SETTINGS=$(pwd)/settings.xml
export MAVEN_OPTS="-XX:MaxPermSize=256m"

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  install:install-file \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -DgroupId=mockobjects \
    -DartifactId=mockobjects-jdk1.4-j2ee1.3 \
    -Dversion=0.09 \
    -Dpackaging=jar \
    -Dfile=$(build-classpath mockobjects-jdk1.4-j2ee1.4)

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
    -P jdk1.5 \
    -s ${SETTINGS} \
    -Daggregate=false \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=true \
    -Dmaven2.jpp.depmap.file=%{SOURCE1} \
%if %without tests
    -Dmaven.test.skip=true \
%endif
    install

# workaround loop: FIXME
rm -rf geronimo-jaspi_1.0_spec
for d in geronimo*; do
pushd $d
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=true \
    -Dmaven2.jpp.depmap.file=%{SOURCE1} \
    javadoc:javadoc
#   -P jdk1.5 \
#   -Daggregate=false \
popd
done

pushd geronimo-spec-j2ee
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
    -s ${SETTINGS} \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=true \
    -Dmaven2.jpp.depmap.file=%{SOURCE1} \
%if %without tests
    -Dmaven.test.skip=true \
%endif
    assembly:assembly
popd

%install

# Directory for poms
install -d -m 0755 %{buildroot}%{_datadir}/maven2/poms

# subpackage jars
install -d -m 755 %{buildroot}%{_javadir}

install -p -m 0644 \
  geronimo-activation_1.0.2_spec-1.2/target/geronimo-activation_1.0.2_spec-%{version}.jar \
  %{buildroot}%{_javadir}/geronimo-jaf-1.0.2-api-%{sver_activation_1_0_2}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-jaf-1.0.2-api-%{sver_activation_1_0_2}.jar \
         geronimo-jaf-1.0.2-api.jar
popd
touch %{buildroot}%{_javadir}/jaf.jar # for %ghost
touch %{buildroot}%{_javadir}/jaf_api.jar # for %ghost
touch %{buildroot}%{_javadir}/jaf_1_0_2_api.jar # for %ghost
install -p -m 0644 geronimo-activation_1.0.2_spec-1.2/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-jaf-1.0.2-api.pom
%add_to_maven_depmap_at geronimo-jaf-1.0.2-api  org.apache.geronimo.specs geronimo-activation_1.0.2_spec %{sver_activation_1_0_2} JPP geronimo-jaf-1.0.2-api

install -p -m 0644 \
  geronimo-activation_1.1_spec-1.0/target/geronimo-activation_1.1_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-jaf-1.1-api-%{sver_activation_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-jaf-1.1-api-%{sver_activation_1_1}.jar \
         geronimo-jaf-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/jaf.jar # for %ghost
touch %{buildroot}%{_javadir}/jaf_api.jar # for %ghost
touch %{buildroot}%{_javadir}/jaf_1_1_api.jar # for %ghost
install -p -m 0644 geronimo-activation_1.1_spec-1.0/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-jaf-1.1-api.pom
%add_to_maven_depmap_at geronimo-jaf-1.1-api  org.apache.geronimo.specs geronimo-activation_1.1_spec %{sver_activation_1_1} JPP geronimo-jaf-1.1-api

install -p -m 0644 \
  geronimo-annotation_1.0_spec-1.1.0/target/geronimo-annotation_1.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-annotation-1.0-api-%{sver_annotation_1_0}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-annotation-1.0-api-%{sver_annotation_1_0}.jar \
         geronimo-annotation-1.0-api.jar
popd
touch %{buildroot}%{_javadir}/annotation_api.jar # for %ghost
touch %{buildroot}%{_javadir}/annotation_1_0_api.jar # for %ghost
install -p -m 0644 geronimo-annotation_1.0_spec-1.1.0/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-annotation-1.0-api.pom
%add_to_maven_depmap_at geronimo-annotation-1.0-api  org.apache.geronimo.specs geronimo-annotation_1.0_spec %{sver_annotation_1_0} JPP geronimo-annotation-1.0-api

install -p -m 0644 \
  geronimo-spec-corba-2.3/target/geronimo-corba_2.3_spec-null.jar \
  %{buildroot}%{_javadir}/geronimo-corba-2.3-apis-%{sver_corba_2_3}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-corba-2.3-apis-%{sver_corba_2_3}.jar \
         geronimo-corba-2.3-apis.jar
popd
touch %{buildroot}%{_javadir}/corba_apis.jar # for %ghost
touch %{buildroot}%{_javadir}/corba_2_3_apis.jar # for %ghost
install -p -m 0644 geronimo-spec-corba-2.3/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-corba-2.3-apis.pom
%add_to_maven_depmap_at geronimo-corba-2.3-apis  org.apache.geronimo.specs geronimo-corba_2.3_spec %{sver_corba_2_3} JPP geronimo-corba-2.3-apis

install -p -m 0644 \
  geronimo-spec-corba-3.0/target/geronimo-corba_3.0_spec-null.jar \
  %{buildroot}%{_javadir}/geronimo-corba-3.0-apis-%{sver_corba_3_0}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-corba-3.0-apis-%{sver_corba_3_0}.jar \
         geronimo-corba-3.0-apis.jar
popd
touch %{buildroot}%{_javadir}/corba_apis.jar # for %ghost
touch %{buildroot}%{_javadir}/corba_3_0_apis.jar # for %ghost
install -p -m 0644 geronimo-spec-corba-3.0/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-corba-3.0-apis.pom
%add_to_maven_depmap_at geronimo-corba-3.0-apis  org.apache.geronimo.specs geronimo-corba_3.0_spec %{sver_corba_3_0} JPP geronimo-corba-3.0-apis

install -p -m 0644 \
  geronimo-spec-corba/target/geronimo-spec-corba-null.jar \
  %{buildroot}%{_javadir}/geronimo-corba-1.0-apis-%{sver_corba_1_0}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-corba-1.0-apis-%{sver_corba_1_0}.jar \
         geronimo-corba-1.0-apis.jar
popd
touch %{buildroot}%{_javadir}/corba_apis.jar # for %ghost
touch %{buildroot}%{_javadir}/corba_1_0_apis.jar # for %ghost
install -p -m 0644 geronimo-spec-corba/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-corba-1.0-apis.pom
%add_to_maven_depmap_at geronimo-corba-1.0-apis  geronimo-spec geronimo-spec-corba %{sver_corba_1_0} JPP geronimo-corba-1.0-apis

install -p -m 0644 \
  geronimo-ejb_2.1_spec-1.1/target/geronimo-ejb_2.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-ejb-2.1-api-%{sver_ejb_2_1}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-ejb-2.1-api-%{sver_ejb_2_1}.jar \
         geronimo-ejb-2.1-api.jar
popd
touch %{buildroot}%{_javadir}/ejb.jar # for %ghost
touch %{buildroot}%{_javadir}/ejb_api.jar # for %ghost
touch %{buildroot}%{_javadir}/ejb_2_1_api.jar # for %ghost
install -p -m 0644 geronimo-ejb_2.1_spec-1.1/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-ejb-2.1-api.pom
%add_to_maven_depmap_at geronimo-ejb-2.1-api  org.apache.geronimo.specs geronimo-ejb_2.1_spec %{sver_ejb_2_1} JPP geronimo-ejb-2.1-api

install -p -m 0644 \
  geronimo-ejb_3.0_spec-1.0/target/geronimo-ejb_3.0_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-ejb-3.0-api-%{sver_ejb_3_0}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-ejb-3.0-api-%{sver_ejb_3_0}.jar \
         geronimo-ejb-3.0-api.jar
popd
touch %{buildroot}%{_javadir}/ejb.jar # for %ghost
touch %{buildroot}%{_javadir}/ejb_api.jar # for %ghost
touch %{buildroot}%{_javadir}/ejb_3_0_api.jar # for %ghost
install -p -m 0644 geronimo-ejb_3.0_spec-1.0/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-ejb-3.0-api.pom
%add_to_maven_depmap_at geronimo-ejb-3.0-api  org.apache.geronimo.specs geronimo-ejb_3.0_spec %{sver_ejb_3_0} JPP geronimo-ejb-3.0-api

install -p -m 0644 \
  geronimo-el_1.0_spec-1.0/target/geronimo-el_1.0_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-el-1.0-api-%{sver_el_1_0}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-el-1.0-api-%{sver_el_1_0}.jar \
         geronimo-el-1.0-api.jar
popd
touch %{buildroot}%{_javadir}/el_api.jar # for %ghost
touch %{buildroot}%{_javadir}/el_1_0_api.jar # for %ghost
install -p -m 0644 geronimo-el_1.0_spec-1.0/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-el-1.0-api.pom
%add_to_maven_depmap_at geronimo-el-1.0-api  org.apache.geronimo.specs geronimo-el_1.0_spec %{sver_el_1_0} JPP geronimo-el-1.0-api

install -p -m 0644 \
  geronimo-interceptor_3.0_spec-1.0/target/geronimo-interceptor_3.0_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-interceptor-3.0-api-%{sver_interceptor_3_0}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-interceptor-3.0-api-%{sver_interceptor_3_0}.jar \
         geronimo-interceptor-3.0-api.jar
popd
touch %{buildroot}%{_javadir}/interceptor_api.jar # for %ghost
touch %{buildroot}%{_javadir}/interceptor_3_0_api.jar # for %ghost
install -p -m 0644 geronimo-interceptor_3.0_spec-1.0/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-interceptor-3.0-api.pom
%add_to_maven_depmap_at geronimo-interceptor-3.0-api  org.apache.geronimo.specs geronimo-interceptor_3.0_spec %{sver_interceptor_3_0} JPP geronimo-interceptor-3.0-api

install -p -m 0644 \
  geronimo-j2ee-connector_1.5_spec-1.1.1/target/geronimo-j2ee-connector_1.5_spec-1.1.1.jar \
  %{buildroot}%{_javadir}/geronimo-j2ee-connector-1.5-api-%{sver_j2ee_connector_1_5}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-j2ee-connector-1.5-api-%{sver_j2ee_connector_1_5}.jar \
         geronimo-j2ee-connector-1.5-api.jar
popd
touch %{buildroot}%{_javadir}/j2ee-connector.jar # for %ghost
touch %{buildroot}%{_javadir}/j2ee_connector_api.jar # for %ghost
touch %{buildroot}%{_javadir}/j2ee_connector_1_5_api.jar # for %ghost
install -p -m 0644 geronimo-j2ee-connector_1.5_spec-1.1.1/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-j2ee-connector-1.5-api.pom
%add_to_maven_depmap_at geronimo-j2ee-connector-1.5-api  org.apache.geronimo.specs geronimo-j2ee-connector_1.5_spec %{sver_j2ee_connector_1_5} JPP geronimo-j2ee-connector-1.5-api

install -p -m 0644 \
  geronimo-j2ee-deployment_1.1_spec-1.1/target/geronimo-j2ee-deployment_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-j2ee-deployment-1.1-api-%{sver_j2ee_deployment_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-j2ee-deployment-1.1-api-%{sver_j2ee_deployment_1_1}.jar \
         geronimo-j2ee-deployment-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/j2ee-deployment.jar # for %ghost
touch %{buildroot}%{_javadir}/j2ee_deployment_api.jar # for %ghost
touch %{buildroot}%{_javadir}/j2ee_deployment_1_1_api.jar # for %ghost
install -p -m 0644 geronimo-j2ee-deployment_1.1_spec-1.1/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-j2ee-deployment-1.1-api.pom
%add_to_maven_depmap_at geronimo-j2ee-deployment-1.1-api  org.apache.geronimo.specs geronimo-j2ee-deployment_1.1_spec %{sver_j2ee_deployment_1_1} JPP geronimo-j2ee-deployment-1.1-api

install -p -m 0644 \
  geronimo-javaee-deployment_1.1MR3_spec-1.0/target/geronimo-javaee-deployment_1.1MR3_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-javaee-deployment-1.1-api-%{sver_javaee_deployment_1_1MR3}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-javaee-deployment-1.1-api-%{sver_javaee_deployment_1_1MR3}.jar \
         geronimo-javaee-deployment-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/javaee_deployment_1_1MR3_api.jar # for %ghost
touch %{buildroot}%{_javadir}/javaee_deployment_api.jar # for %ghost
install -p -m 0644 geronimo-javaee-deployment_1.1MR3_spec-1.0/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-javaee-deployment-1.1-api.pom
%add_to_maven_depmap_at geronimo-javaee-deployment-1.1-api  org.apache.geronimo.specs geronimo-javaee-deployment_1.1_spec %{sver_javaee_deployment_1_1MR3} JPP geronimo-javaee-deployment-1.1-api

install -p -m 0644 \
  geronimo-j2ee-jacc_1.0_spec-1.1/target/geronimo-j2ee-jacc_1.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jacc-1.0-api-%{sver_j2ee_jacc_1_0}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-jacc-1.0-api-%{sver_j2ee_jacc_1_0}.jar \
         geronimo-jacc-1.0-api.jar
popd
touch %{buildroot}%{_javadir}/jacc.jar # for %ghost
touch %{buildroot}%{_javadir}/jacc_api.jar # for %ghost
touch %{buildroot}%{_javadir}/jacc_1_0_api.jar # for %ghost
install -p -m 0644 geronimo-j2ee-jacc_1.0_spec-1.1/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-jacc-1.0-api.pom
%add_to_maven_depmap_at geronimo-jacc-1.0-api  org.apache.geronimo.specs geronimo-j2ee-jacc_1.0_spec %{sver_j2ee_jacc_1_0} JPP geronimo-jacc-1.0-api

install -p -m 0644 \
  geronimo-jacc_1.1_spec-1.0/target/geronimo-jacc_1.1_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-jacc-1.1-api-%{sver_jacc_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-jacc-1.1-api-%{sver_jacc_1_1}.jar \
         geronimo-jacc-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/jacc_api.jar # for %ghost
touch %{buildroot}%{_javadir}/jacc_1_1_api.jar # for %ghost
install -p -m 0644 geronimo-jacc_1.1_spec-1.0/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-jacc-1.1-api.pom
%add_to_maven_depmap_at geronimo-jacc-1.1-api  org.apache.geronimo.specs geronimo-j2ee-jacc_1.1_spec %{sver_jacc_1_1} JPP geronimo-jacc-1.1-api

install -p -m 0644 \
  geronimo-j2ee-management_1.0_spec-1.1/target/geronimo-j2ee-management_1.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-j2ee-management-1.0-api-%{sver_j2ee_management_1_0}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-j2ee-management-1.0-api-%{sver_j2ee_management_1_0}.jar \
         geronimo-j2ee-management-1.0-api.jar
popd
touch %{buildroot}%{_javadir}/j2ee-management.jar # for %ghost
touch %{buildroot}%{_javadir}/j2ee_management_api.jar # for %ghost
touch %{buildroot}%{_javadir}/j2ee_management_1_0_api.jar # for %ghost
install -p -m 0644 geronimo-j2ee-management_1.0_spec-1.1/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-j2ee-management-1.0-api.pom
%add_to_maven_depmap_at geronimo-j2ee-management-1.0-api  org.apache.geronimo.specs geronimo-j2ee-management_1.0_spec %{sver_j2ee_management_1_0} JPP geronimo-j2ee-management-1.0-api

install -p -m 0644 \
  geronimo-j2ee-management_1.1_spec-1.0/target/geronimo-j2ee-management_1.1_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-j2ee-management-1.1-api-%{sver_j2ee_management_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-j2ee-management-1.1-api-%{sver_j2ee_management_1_1}.jar \
         geronimo-j2ee-management-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/j2ee-management.jar # for %ghost
touch %{buildroot}%{_javadir}/j2ee_management_api.jar # for %ghost
touch %{buildroot}%{_javadir}/j2ee_management_1_1_api.jar # for %ghost
install -p -m 0644 geronimo-j2ee-management_1.1_spec-1.0/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-j2ee-management-1.1-api.pom
%add_to_maven_depmap_at geronimo-j2ee-management-1.1-api  org.apache.geronimo.specs geronimo-j2ee-management_1.1_spec %{sver_j2ee_management_1_1} JPP geronimo-j2ee-management-1.1-api

install -p -m 0644 \
  geronimo-javamail_1.3.1_spec-1.3/target/geronimo-javamail_1.3.1_spec-1.3.jar \
  %{buildroot}%{_javadir}/geronimo-javamail-1.3.1-api-%{sver_javamail_1_3_1}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-javamail-1.3.1-api-%{sver_javamail_1_3_1}.jar \
         geronimo-javamail-1.3.1-api.jar
popd
# Do not provide it as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#touch %{buildroot}%{_javadir}/javamail.jar # for %ghost
# but:
touch %{buildroot}%{_javadir}/javamail_api.jar # for %ghost
touch %{buildroot}%{_javadir}/javamail_1_3_1_api.jar # for %ghost
install -p -m 0644 geronimo-javamail_1.3.1_spec-1.3/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-javamail-1.3.1-api.pom
%add_to_maven_depmap_at geronimo-javamail-1.3.1-api  org.apache.geronimo.specs geronimo-javamail_1.3.1_spec %{sver_javamail_1_3_1} JPP geronimo-javamail-1.3.1-api

install -p -m 0644 \
  geronimo-javamail_1.4_spec-1.1/target/geronimo-javamail_1.4_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-javamail-1.4-api-%{sver_javamail_1_4}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-javamail-1.4-api-%{sver_javamail_1_4}.jar \
         geronimo-javamail-1.4-api.jar
popd
# Do not provide it as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#touch %{buildroot}%{_javadir}/javamail.jar # for %ghost
# but:
touch %{buildroot}%{_javadir}/javamail_api.jar # for %ghost
touch %{buildroot}%{_javadir}/javamail_1_4_api.jar # for %ghost
install -p -m 0644 geronimo-javamail_1.4_spec-1.1/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-javamail-1.4-api.pom
%add_to_maven_depmap_at geronimo-javamail-1.4-api  org.apache.geronimo.specs geronimo-javamail_1.4_spec %{sver_javamail_1_4} JPP geronimo-javamail-1.4-api

install -p -m 0644 \
  geronimo-jaxr_1.0_spec-1.1/target/geronimo-jaxr_1.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jaxr-1.0-api-%{sver_jaxr_1_0}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-jaxr-1.0-api-%{sver_jaxr_1_0}.jar \
         geronimo-jaxr-1.0-api.jar
popd
touch %{buildroot}%{_javadir}/jaxr.jar # for %ghost
touch %{buildroot}%{_javadir}/jaxr_api.jar # for %ghost
touch %{buildroot}%{_javadir}/jaxr_1_0_api.jar # for %ghost
install -p -m 0644 geronimo-jaxr_1.0_spec-1.1/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-jaxr-1.0-api.pom
%add_to_maven_depmap_at geronimo-jaxr-1.0-api  org.apache.geronimo.specs geronimo-jaxr_1.0_spec %{sver_jaxr_1_0} JPP geronimo-jaxr-1.0-api

install -p -m 0644 \
  geronimo-jaxrpc_1.1_spec-1.1/target/geronimo-jaxrpc_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jaxrpc-1.1-api-%{sver_jaxrpc_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-jaxrpc-1.1-api-%{sver_jaxrpc_1_1}.jar \
         geronimo-jaxrpc-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/jaxrpc.jar # for %ghost
touch %{buildroot}%{_javadir}/jaxrpc_api.jar # for %ghost
touch %{buildroot}%{_javadir}/jaxrpc_1_1_api.jar # for %ghost
install -p -m 0644 geronimo-jaxrpc_1.1_spec-1.1/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-jaxrpc-1.1-api.pom
%add_to_maven_depmap_at geronimo-jaxrpc-1.1-api  org.apache.geronimo.specs geronimo-jaxrpc_1.1_spec %{sver_jaxrpc_1_1} JPP geronimo-jaxrpc-1.1-api

rm -rf j2eetemp
mkdir j2eetemp
pushd j2eetemp
jar xf ../geronimo-j2ee-connector_1.5_spec-1.1.1/target/geronimo-j2ee-connector_1.5_spec-1.1.1.jar
jar xf ../geronimo-j2ee-jacc_1.0_spec-1.1/target/geronimo-j2ee-jacc_1.0_spec-1.1.jar
jar xf ../geronimo-j2ee-management_1.0_spec-1.1/target/geronimo-j2ee-management_1.0_spec-1.1.jar
jar xf ../geronimo-jta_1.0.1B_spec-1.1.1/target/geronimo-jta_1.0.1B_spec-1.1.1.jar
jar xf ../geronimo-ejb_2.1_spec-1.1/target/geronimo-ejb_2.1_spec-1.1.jar
jar xf ../geronimo-jsp_2.0_spec-1.1/target/geronimo-jsp_2.0_spec-1.1.jar
jar xf ../geronimo-qname_1.1_spec-1.1/target/geronimo-qname_1.1_spec-1.1.jar
jar xf ../geronimo-j2ee-deployment_1.1_spec-1.1/target/geronimo-j2ee-deployment_1.1_spec-1.1.jar
jar xf ../geronimo-activation_1.0.2_spec-1.2/target/geronimo-activation_1.0.2_spec-%{version}.jar
jar xf ../geronimo-saaj_1.1_spec-1.1/target/geronimo-saaj_1.1_spec-1.1.jar
jar xf ../geronimo-jaxr_1.0_spec-1.1/target/geronimo-jaxr_1.0_spec-1.1.jar
jar xf ../geronimo-jaxrpc_1.1_spec-1.1/target/geronimo-jaxrpc_1.1_spec-1.1.jar
jar xf ../geronimo-spec-corba-2.3/target/geronimo-corba_2.3_spec-null.jar
jar xf ../geronimo-jms_1.1_spec-1.1/target/geronimo-jms_1.1_spec-1.1.jar
jar xf ../geronimo-servlet_2.4_spec-1.1.1/target/geronimo-servlet_2.4_spec-1.1.1.jar
jar xf ../geronimo-javamail_1.3.1_spec-1.3/target/geronimo-javamail_1.3.1_spec-1.3.jar
jar xf ../geronimo-spec-commonj/target/geronimo-commonj_1.1_spec-null.jar
rm -rf META-INF
jar cf ../geronimo-spec-j2ee/target/geronimo-j2ee_1.4_spec-1.2-jar-with-dependencies.jar *
popd
install -p -m 0644 \
  geronimo-spec-j2ee/target/geronimo-j2ee_1.4_spec-1.2-jar-with-dependencies.jar \
  %{buildroot}%{_javadir}/geronimo-j2ee-1.4-apis-%{version}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-j2ee-1.4-apis-%{version}.jar \
         geronimo-j2ee-1.4-apis.jar
popd
install -p -m 0644 geronimo-spec-j2ee/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-j2ee-1.4-apis.pom
%add_to_maven_depmap_at geronimo-j2ee-1.4-apis  org.apache.geronimo.specs geronimo-j2ee_1.4_spec %{version} JPP geronimo-j2ee-1.4-apis

install -p -m 0644 \
  geronimo-jms_1.1_spec-1.1/target/geronimo-jms_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jms-1.1-api-%{sver_jms_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-jms-1.1-api-%{sver_jms_1_1}.jar \
         geronimo-jms-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/jms.jar # for %ghost
touch %{buildroot}%{_javadir}/jms_api.jar # for %ghost
touch %{buildroot}%{_javadir}/jms_1_1_api.jar # for %ghost
install -p -m 0644 geronimo-jms_1.1_spec-1.1/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-jms-1.1-api.pom
%add_to_maven_depmap_at geronimo-jms-1.1-api  org.apache.geronimo.specs geronimo-jms_1.1_spec %{sver_jms_1_1} JPP geronimo-jms-1.1-api

install -p -m 0644 \
  geronimo-jpa_3.0_spec-1.1.0/target/geronimo-jpa_3.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jpa-3.0-api-%{sver_jpa_3_0}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-jpa-3.0-api-%{sver_jpa_3_0}.jar \
         geronimo-jpa-3.0-api.jar
popd
touch %{buildroot}%{_javadir}/jpa_api.jar # for %ghost
touch %{buildroot}%{_javadir}/jpa_3_0_api.jar # for %ghost
install -p -m 0644 geronimo-jpa_3.0_spec-1.1.0/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-jpa-3.0-api.pom
%add_to_maven_depmap_at geronimo-jpa-3.0-api  org.apache.geronimo.specs geronimo-jpa_3.0_spec %{sver_jpa_3_0} JPP geronimo-jpa-3.0-api

install -p -m 0644 \
  geronimo-jsp_2.0_spec-1.1/target/geronimo-jsp_2.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jsp-2.0-api-%{sver_jsp_2_0}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-jsp-2.0-api-%{sver_jsp_2_0}.jar \
         geronimo-jsp-2.0-api.jar
popd
touch %{buildroot}%{_javadir}/jsp.jar # for %ghost
touch %{buildroot}%{_javadir}/jsp_api.jar # for %ghost
touch %{buildroot}%{_javadir}/jsp_2_0_api.jar # for %ghost
install -p -m 0644 geronimo-jsp_2.0_spec-1.1/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-jsp-2.0-api.pom
%add_to_maven_depmap_at geronimo-jsp-2.0-api  org.apache.geronimo.specs geronimo-jsp_2.0_spec %{sver_jsp_2_0} JPP geronimo-jsp-2.0-api

install -p -m 0644 \
  geronimo-jsp_2.1_spec-1.0/target/geronimo-jsp_2.1_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-jsp-2.1-api-%{sver_jsp_2_1}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-jsp-2.1-api-%{sver_jsp_2_1}.jar \
         geronimo-jsp-2.1-api.jar
popd
touch %{buildroot}%{_javadir}/jsp.jar # for %ghost
touch %{buildroot}%{_javadir}/jsp_api.jar # for %ghost
touch %{buildroot}%{_javadir}/jsp_2_1_api.jar # for %ghost
install -p -m 0644 geronimo-jsp_2.1_spec-1.0/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-jsp-2.1-api.pom
%add_to_maven_depmap_at geronimo-jsp-2.1-api  org.apache.geronimo.specs geronimo-jsp_2.1_spec %{sver_jsp_2_1} JPP geronimo-jsp-2.1-api

install -p -m 0644 \
  geronimo-jta_1.0.1B_spec-1.1.1/target/geronimo-jta_1.0.1B_spec-1.1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jta-1.0.1B-api-%{sver_jta_1_0_1B}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-jta-1.0.1B-api-%{sver_jta_1_0_1B}.jar \
         geronimo-jta-1.0.1B-api.jar
popd
touch %{buildroot}%{_javadir}/jta.jar # for %ghost
touch %{buildroot}%{_javadir}/jta_api.jar # for %ghost
touch %{buildroot}%{_javadir}/jta_1_0_1B_api.jar # for %ghost
install -p -m 0644 geronimo-jta_1.0.1B_spec-1.1.1/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-jta-1.0.1B-api.pom
%add_to_maven_depmap_at geronimo-jta-1.0.1B-api  org.apache.geronimo.specs geronimo-jta_1.0.1B_spec %{sver_jta_1_0_1B} JPP geronimo-jta-1.0.1B-api

install -p -m 0644 \
  geronimo-jta_1.1_spec-1.1.0/target/geronimo-jta_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jta-1.1-api-%{sver_jta_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-jta-1.1-api-%{sver_jta_1_1}.jar \
         geronimo-jta-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/jta.jar # for %ghost
touch %{buildroot}%{_javadir}/jta_api.jar # for %ghost
touch %{buildroot}%{_javadir}/jta_1_1_api.jar # for %ghost
install -p -m 0644 geronimo-jta_1.1_spec-1.1.0/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-jta-1.1-api.pom
%add_to_maven_depmap_at geronimo-jta-1.1-api  org.apache.geronimo.specs geronimo-jta_1.1_spec %{sver_jta_1_1} JPP geronimo-jta-1.1-api

install -p -m 0644 \
  geronimo-qname_1.1_spec-1.1/target/geronimo-qname_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-qname-1.1-api-%{sver_qname_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-qname-1.1-api-%{sver_qname_1_1}.jar \
         geronimo-qname-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/qname_api.jar # for %ghost
touch %{buildroot}%{_javadir}/qname_1_1_api.jar # for %ghost
install -p -m 0644 geronimo-qname_1.1_spec-1.1/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-qname-1.1-api.pom
%add_to_maven_depmap_at geronimo-qname-1.1-api  org.apache.geronimo.specs geronimo-qname_1.1_spec %{sver_qname_1_1} JPP geronimo-qname-1.1-api

install -p -m 0644 \
  geronimo-saaj_1.1_spec-1.1/target/geronimo-saaj_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-saaj-1.1-api-%{sver_saaj_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-saaj-1.1-api-%{sver_saaj_1_1}.jar \
         geronimo-saaj-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/saaj.jar # for %ghost
touch %{buildroot}%{_javadir}/saaj_api.jar # for %ghost
touch %{buildroot}%{_javadir}/saaj_1_1_api.jar # for %ghost
install -p -m 0644 geronimo-saaj_1.1_spec-1.1/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-saaj-1.1-api.pom
%add_to_maven_depmap_at geronimo-saaj-1.1-api  org.apache.geronimo.specs geronimo-saaj_1.1_spec %{sver_saaj_1_1} JPP geronimo-saaj-1.1-api

install -p -m 0644 \
  geronimo-servlet_2.4_spec-1.1.1/target/geronimo-servlet_2.4_spec-1.1.1.jar \
  %{buildroot}%{_javadir}/geronimo-servlet-2.4-api-%{sver_servlet_2_4}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-servlet-2.4-api-%{sver_servlet_2_4}.jar \
         geronimo-servlet-2.4-api.jar
popd
touch %{buildroot}%{_javadir}/servlet.jar # for %ghost
touch %{buildroot}%{_javadir}/servlet_api.jar # for %ghost
touch %{buildroot}%{_javadir}/servlet_2_4_api.jar # for %ghost
install -p -m 0644 geronimo-servlet_2.4_spec-1.1.1/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-servlet-2.4-api.pom
%add_to_maven_depmap_at geronimo-servlet-2.4-api  org.apache.geronimo.specs geronimo-servlet_2.4_spec %{sver_servlet_2_4} JPP geronimo-servlet-2.4-api

install -p -m 0644 \
  geronimo-servlet_2.5_spec-1.1/target/geronimo-servlet_2.5_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-servlet-2.5-api-%{sver_servlet_2_5}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-servlet-2.5-api-%{sver_servlet_2_5}.jar \
         geronimo-servlet-2.5-api.jar
popd
touch %{buildroot}%{_javadir}/servlet.jar # for %ghost
touch %{buildroot}%{_javadir}/servlet_api.jar # for %ghost
touch %{buildroot}%{_javadir}/servlet_2_5_api.jar # for %ghost
install -p -m 0644 geronimo-servlet_2.5_spec-1.1/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-servlet-2.5-api.pom
%add_to_maven_depmap_at geronimo-servlet-2.5-api  org.apache.geronimo.specs geronimo-servlet_2.5_spec %{sver_servlet_2_5}.0.1 JPP geronimo-servlet-2.5-api

install -p -m 0644 \
  geronimo-stax-api_1.0_spec-1.0/target/geronimo-stax-api_1.0_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-stax-1.0-api-%{sver_stax_1_0}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-stax-1.0-api-%{sver_stax_1_0}.jar \
         geronimo-stax-1.0-api.jar
popd
touch %{buildroot}%{_javadir}/stax_api.jar # for %ghost
touch %{buildroot}%{_javadir}/stax_1_0_api.jar # for %ghost
install -p -m 0644 geronimo-stax-api_1.0_spec-1.0/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-stax-1.0-api.pom
%add_to_maven_depmap_at geronimo-stax-1.0-api  org.apache.geronimo.specs geronimo-stax_1.0_spec %{sver_stax_1_0} JPP geronimo-stax-1.0-api

install -p -m 0644 \
  geronimo-ws-metadata_2.0_spec-1.1.1/target/geronimo-ws-metadata_2.0_spec-1.1.1.jar \
  %{buildroot}%{_javadir}/geronimo-ws-metadata-2.0-api-%{sver_ws_metadata_2_0}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-ws-metadata-2.0-api-%{sver_ws_metadata_2_0}.jar \
         geronimo-ws-metadata-2.0-api.jar
popd
touch %{buildroot}%{_javadir}/ws_metadata_api.jar # for %ghost
touch %{buildroot}%{_javadir}/ws_metadata_2_0_api.jar # for %ghost
install -p -m 0644 geronimo-ws-metadata_2.0_spec-1.1.1/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-ws-metadata-2.0-api.pom
%add_to_maven_depmap_at geronimo-ws-metadata-2.0-api  org.apache.geronimo.specs geronimo-ws-metadata_2.0_spec %{sver_ws_metadata_2_0} JPP geronimo-ws-metadata-2.0-api

install -p -m 0644 \
  geronimo-spec-commonj/target/geronimo-commonj_1.1_spec-null.jar \
  %{buildroot}%{_javadir}/geronimo-commonj-1.1-apis-%{sver_commonj_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -s geronimo-commonj-1.1-apis-%{sver_commonj_1_1}.jar \
         geronimo-commonj-1.1-apis.jar
popd
touch %{buildroot}%{_javadir}/commonj_apis.jar # for %ghost
touch %{buildroot}%{_javadir}/commonj_1_1_apis.jar # for %ghost
install -p -m 0644 geronimo-spec-commonj/pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-commonj-1.1-apis.pom
%add_to_maven_depmap_at geronimo-commonj-1.1-apis  org.apache.geronimo.specs geronimo-commonj_1.1_spec %{sver_commonj_1_1} JPP geronimo-commonj-1.1-apis

# Add the parent geronimo-specs pom
cp -p pom.xml \
  %{buildroot}/%{_datadir}/maven2/poms/JPP-geronimo-specs.pom
%add_to_maven_depmap_at geronimo-specs  org.apache.geronimo.specs specs 1.1 JPP geronimo-specs

# main package jars
install -d -m 0755 %{buildroot}%{_javadir}/geronimo
find  %{buildroot}%{_javadir}

pushd %{buildroot}%{_javadir}/geronimo
  ln -s ../geronimo-commonj-1.1-apis-%{sver_commonj_1_1}.jar spec-commonj-1.1-%{sver_commonj_1_1}.jar
  ln -s spec-commonj-1.1-%{sver_commonj_1_1}.jar spec-commonj-1.1.jar

  ln -s ../geronimo-jaf-1.0.2-api-%{sver_activation_1_0_2}.jar spec-jaf-1.0.2-%{sver_activation_1_0_2}.jar
  ln -s spec-jaf-1.0.2-%{sver_activation_1_0_2}.jar spec-jaf-1.0.2.jar

  ln -s ../geronimo-jaf-1.1-api-%{sver_activation_1_1}.jar spec-jaf-1.1-%{sver_activation_1_1}.jar
  ln -s spec-jaf-1.1-%{sver_activation_1_1}.jar spec-jaf-1.1.jar

  ln -s ../geronimo-annotation-1.0-api-%{sver_annotation_1_0}.jar spec-annotation-1.0-%{sver_annotation_1_0}.jar
  ln -s spec-annotation-1.0-%{sver_annotation_1_0}.jar spec-annotation-1.0.jar

  ln -s ../geronimo-ejb-2.1-api-%{sver_ejb_2_1}.jar spec-ejb-2.1-%{sver_ejb_2_1}.jar
  ln -s spec-ejb-2.1-%{sver_ejb_2_1}.jar spec-ejb-2.1.jar

  ln -s ../geronimo-ejb-3.0-api-%{sver_ejb_3_0}.jar spec-ejb-3.0-%{sver_ejb_3_0}.jar
  ln -s spec-ejb-3.0-%{sver_ejb_3_0}.jar spec-ejb-3.0.jar

  ln -s ../geronimo-el-1.0-api-%{sver_el_1_0}.jar spec-el-1.0-%{sver_el_1_0}.jar
  ln -s spec-el-1.0-%{sver_el_1_0}.jar spec-el-1.0.jar

  ln -s ../geronimo-interceptor-3.0-api-%{sver_interceptor_3_0}.jar spec-interceptor-3.0-%{sver_interceptor_3_0}.jar
  ln -s spec-interceptor-3.0-%{sver_interceptor_3_0}.jar spec-interceptor-3.0.jar

  ln -s ../geronimo-j2ee-connector-1.5-api-%{sver_j2ee_connector_1_5}.jar \
    spec-j2ee-connector-1.5-%{sver_j2ee_connector_1_5}.jar
  ln -s spec-j2ee-connector-1.5-%{sver_j2ee_connector_1_5}.jar spec-j2ee-connector-1.5.jar

  ln -s ../geronimo-j2ee-deployment-1.1-api-%{sver_j2ee_deployment_1_1}.jar \
    spec-j2ee-deployment-1.1-%{sver_j2ee_deployment_1_1}.jar
  ln -s spec-j2ee-deployment-1.1-%{sver_j2ee_deployment_1_1}.jar spec-j2ee-deployment-1.1.jar

  ln -s ../geronimo-javaee-deployment-1.1-api-%{sver_javaee_deployment_1_1MR3}.jar \
    spec-javaee-deployment-1.1-%{sver_javaee_deployment_1_1MR3}.jar
  ln -s spec-javaee-deployment-1.1-%{sver_javaee_deployment_1_1MR3}.jar spec-javaee-deployment-1.1.jar

  ln -s ../geronimo-jacc-1.0-api-%{sver_j2ee_jacc_1_0}.jar spec-jacc-1.0-%{sver_j2ee_jacc_1_0}.jar
  ln -s spec-jacc-1.0-%{sver_j2ee_jacc_1_0}.jar spec-jacc-1.0.jar

  ln -s ../geronimo-jacc-1.1-api-%{sver_jacc_1_1}.jar spec-jacc-1.1-%{sver_jacc_1_1}.jar
  ln -s spec-jacc-1.1-%{sver_jacc_1_1}.jar spec-jacc-1.1.jar

  ln -s ../geronimo-j2ee-management-1.0-api-%{sver_j2ee_management_1_0}.jar \
    spec-j2ee-management-1.0-%{sver_j2ee_management_1_0}.jar
  ln -s spec-j2ee-management-1.0-%{sver_j2ee_management_1_0}.jar spec-j2ee-management-1.0.jar

  ln -s ../geronimo-j2ee-management-1.1-api-%{sver_j2ee_management_1_1}.jar \
    spec-j2ee-management-1.1-%{sver_j2ee_management_1_1}.jar
  ln -s spec-j2ee-management-1.1-%{sver_j2ee_management_1_1}.jar spec-j2ee-management-1.1.jar

  ln -s ../geronimo-j2ee-1.4-apis-%{version}.jar spec-j2ee-1.4-%{version}.jar
  ln -s spec-j2ee-1.4-%{version}.jar spec-j2ee-1.4.jar

  ln -s ../geronimo-jms-1.1-api-%{sver_jms_1_1}.jar spec-jms-1.1-%{sver_jms_1_1}.jar
  ln -s spec-jms-1.1-%{sver_jms_1_1}.jar spec-jms-1.1.jar

  ln -s ../geronimo-jpa-3.0-api-%{sver_jpa_3_0}.jar spec-jpa-3.0-%{sver_jpa_3_0}.jar
  ln -s spec-jpa-3.0-%{sver_jpa_3_0}.jar spec-jpa-3.0.jar

  ln -s ../geronimo-jsp-2.0-api-%{sver_jsp_2_0}.jar spec-jsp-2.0-%{sver_jsp_2_0}.jar
  ln -s spec-jsp-2.0-%{sver_jsp_2_0}.jar spec-jsp-2.0.jar

  ln -s ../geronimo-jsp-2.1-api-%{sver_jsp_2_1}.jar spec-jsp-2.1-%{sver_jsp_2_1}.jar
  ln -s spec-jsp-2.1-%{sver_jsp_2_1}.jar spec-jsp-2.1.jar

  ln -s ../geronimo-jta-1.0.1B-api-%{sver_jta_1_0_1B}.jar spec-jta-1.0.1B-%{sver_jta_1_0_1B}.jar
  ln -s spec-jta-1.0.1B-%{sver_jta_1_0_1B}.jar spec-jta-1.0.1B.jar

  ln -s ../geronimo-jta-1.1-api-%{sver_jta_1_1}.jar spec-jta-1.1-%{sver_jta_1_1}.jar
  ln -s spec-jta-1.1-%{sver_jta_1_1}.jar spec-jta-1.1.jar

  ln -s ../geronimo-servlet-2.4-api-%{sver_servlet_2_4}.jar spec-servlet-2.4-%{sver_servlet_2_4}.jar
  ln -s spec-servlet-2.4-%{sver_servlet_2_4}.jar spec-servlet-2.4.jar

  ln -s ../geronimo-servlet-2.5-api-%{sver_servlet_2_5}.jar spec-servlet-2.5-%{sver_servlet_2_5}.jar
  ln -s spec-servlet-2.5-%{sver_servlet_2_5}.jar spec-servlet-2.5.jar

  ln -s ../geronimo-stax-1.0-api-%{sver_stax_1_0}.jar spec-stax-1.0-%{sver_stax_1_0}.jar
  ln -s spec-stax-1.0-%{sver_stax_1_0}.jar spec-stax-1.0.jar

  ln -s ../geronimo-ws-metadata-2.0-api-%{sver_ws_metadata_2_0}.jar spec-ws-metadata-2.0-%{sver_ws_metadata_2_0}.jar
  ln -s spec-ws-metadata-2.0-%{sver_ws_metadata_2_0}.jar spec-ws-metadata-2.0.jar
popd

#install -p -m 0644 modules/j2ee-schema/target/geronimo-j2ee-schema-1.0-M4.jar \
#          %{buildroot}%{_javadir}/geronimo/spec-j2ee-schema-1.0-M4.jar
#pushd %{buildroot}%{_javadir}/geronimo
#  ln -s spec-j2ee-schema-1.0-M4.jar spec-j2ee-schema-1.0.jar
#popd

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jaf-1.0.2
    cp -pr geronimo-activation_1.0.2_spec-1.2/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jaf-1.0.2
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jaf-1.1
    cp -pr geronimo-activation_1.1_spec-1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jaf-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/annotation-1.0
    cp -pr geronimo-annotation_1.0_spec-1.1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/annotation-1.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/commonj-1.1
    cp -pr geronimo-spec-commonj/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/commonj-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/corba-1.0
    cp -pr geronimo-spec-corba/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/corba-1.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/corba-2.3
    cp -pr geronimo-spec-corba-2.3/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/corba-2.3
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/corba-3.0
    cp -pr geronimo-spec-corba-3.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/corba-3.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/ejb-2.1
    cp -pr geronimo-ejb_2.1_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/ejb-2.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/ejb-3.0
    cp -pr geronimo-ejb_3.0_spec-1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/ejb-3.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/el-1.0
    cp -pr geronimo-el_1.0_spec-1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/el-1.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/interceptor-3.0
    cp -pr geronimo-interceptor_3.0_spec-1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/interceptor-3.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/j2ee-connector-1.5
    cp -pr geronimo-j2ee-connector_1.5_spec-1.1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/j2ee-connector-1.5
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/j2ee-deployment-1.1
    cp -pr geronimo-j2ee-deployment_1.1_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/j2ee-deployment-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/javaee-deployment-1.1
    cp -pr geronimo-javaee-deployment_1.1MR3_spec-1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/javaee-deployment-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/j2ee-management-1.0
    cp -pr geronimo-j2ee-management_1.0_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/j2ee-management-1.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/j2ee-management-1.1
    cp -pr geronimo-j2ee-management_1.1_spec-1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/j2ee-management-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/javamail-1.3.1
    cp -pr geronimo-javamail_1.3.1_spec-1.3/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/javamail-1.3.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/javamail-1.4
    cp -pr geronimo-javamail_1.4_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/javamail-1.4
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jaxrpc-1.1
    cp -pr geronimo-jaxrpc_1.1_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jaxrpc-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jaxr-1.0
    cp -pr geronimo-jaxr_1.0_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jaxr-1.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jms-1.1
    cp -pr geronimo-jms_1.1_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jms-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jpa-3.0
    cp -pr geronimo-jpa_3.0_spec-1.1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jpa-3.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jsp-2.0
    cp -pr geronimo-jsp_2.0_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jsp-2.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jsp-2.1
    cp -pr geronimo-jsp_2.1_spec-1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jsp-2.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jta-1.0.1B
    cp -pr geronimo-jta_1.0.1B_spec-1.1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jta-1.0.1B
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jta-1.1
    cp -pr geronimo-jta_1.1_spec-1.1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jta-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/qname-1.1
    cp -pr geronimo-qname_1.1_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/qname-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/saaj-1.1
    cp -pr geronimo-saaj_1.1_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/saaj-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/servlet-2.4
    cp -pr geronimo-servlet_2.4_spec-1.1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/servlet-2.4
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/servlet-2.5
    cp -pr geronimo-servlet_2.5_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/servlet-2.5
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/stax-1.0
    cp -pr geronimo-stax-api_1.0_spec-1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/stax-1.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/ws-metadata-2.0
    cp -pr geronimo-ws-metadata_2.0_spec-1.1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/ws-metadata-2.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jacc-1.0
    cp -pr geronimo-j2ee-jacc_1.0_spec-1.1/target/site/apidocs/* \
         %{buildroot}%{_javadocdir}/%{name}-%{version}/jacc-1.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jacc-1.1
    cp -pr geronimo-jacc_1.1_spec-1.0/target/site/apidocs/* \
         %{buildroot}%{_javadocdir}/%{name}-%{version}/jacc-1.1

ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} # ghost symlink

# documents
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jaf-1.0.2
    cp -pr geronimo-activation_1.0.2_spec-1.2/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jaf-1.0.2
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jaf-1.1
    cp -pr geronimo-activation_1.1_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jaf-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/annotation-1.0
    cp -pr geronimo-annotation_1.0_spec-1.1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/annotation-1.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/commonj-1.1
    cp -pr geronimo-spec-commonj/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/commonj-1.1
#install -d -m 755 \
#       %{buildroot}%{_docdir}/%{name}-%{version}/corba-1.0
#    cp -pr geronimo-spec-corba/LICENSE.txt \
#       %{buildroot}%{_docdir}/%{name}-%{version}/corba-1.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/corba-2.3
    cp -pr geronimo-spec-corba-2.3/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/corba-2.3
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/corba-3.0
    cp -pr geronimo-spec-corba-3.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/corba-3.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/ejb-2.1
    cp -pr geronimo-ejb_2.1_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/ejb-2.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/ejb-3.0
    cp -pr geronimo-ejb_3.0_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/ejb-3.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/el-1.0
    cp -pr geronimo-el_1.0_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/el-1.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/interceptor-3.0
    cp -pr geronimo-interceptor_3.0_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/interceptor-3.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-connector-1.5
    cp -pr geronimo-j2ee-connector_1.5_spec-1.1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-connector-1.5
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-deployment-1.1
    cp -pr geronimo-j2ee-deployment_1.1_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-deployment-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/javaee-deployment-1.1
    cp -pr geronimo-javaee-deployment_1.1MR3_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/javaee-deployment-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-management-1.0
    cp -pr geronimo-j2ee-management_1.0_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-management-1.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-management-1.1
    cp -pr geronimo-j2ee-management_1.1_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-management-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/javamail-1.3.1
    cp -pr geronimo-javamail_1.3.1_spec-1.3/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/javamail-1.3.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/javamail-1.4
    cp -pr geronimo-javamail_1.4_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/javamail-1.4
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jaxrpc-1.1
    cp -pr geronimo-jaxrpc_1.1_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jaxrpc-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jaxr-1.0
    cp -pr geronimo-jaxr_1.0_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jaxr-1.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jms-1.1
    cp -pr geronimo-jms_1.1_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jms-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jpa-3.0
    cp -pr geronimo-jpa_3.0_spec-1.1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jpa-3.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jsp-2.0
    cp -pr geronimo-jsp_2.0_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jsp-2.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jsp-2.1
    cp -pr geronimo-jsp_2.1_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jsp-2.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jta-1.0.1B
    cp -pr geronimo-jta_1.0.1B_spec-1.1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jta-1.0.1B
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jta-1.1
    cp -pr geronimo-jta_1.1_spec-1.1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jta-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/qname-1.1
    cp -pr geronimo-qname_1.1_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/qname-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/saaj-1.1
    cp -pr geronimo-saaj_1.1_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/saaj-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/servlet-2.4
    cp -pr geronimo-servlet_2.4_spec-1.1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/servlet-2.4
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/servlet-2.5
    cp -pr geronimo-servlet_2.5_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/servlet-2.5
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/stax-1.0
    cp -pr geronimo-stax-api_1.0_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/stax-1.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/ws-metadata-2.0
    cp -pr geronimo-ws-metadata_2.0_spec-1.1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/ws-metadata-2.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jacc-1.0
    cp -pr geronimo-j2ee-jacc_1.0_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jacc-1.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jacc-1.1
    cp -pr geronimo-jacc_1.1_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jacc-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-1.4
    cp -pr geronimo-spec-j2ee/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-1.4
cp -pr etc/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/commonj_apis_geronimo-commonj-1.1-apis<<EOF
%{_javadir}/commonj_apis.jar	%{_javadir}/geronimo-commonj-1.1-apis.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/commonj_1_1_apis_geronimo-commonj-1.1-apis<<EOF
%{_javadir}/commonj_1_1_apis.jar	%{_javadir}/geronimo-commonj-1.1-apis.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaf_geronimo-jaf-1.0.2-api<<EOF
%{_javadir}/jaf.jar	%{_javadir}/geronimo-jaf-1.0.2-api.jar	10002
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaf_api_geronimo-jaf-1.0.2-api<<EOF
%{_javadir}/jaf_api.jar	%{_javadir}/geronimo-jaf-1.0.2-api.jar	10002
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaf_1_0_2_api_geronimo-jaf-1.0.2-api<<EOF
%{_javadir}/jaf_1_0_2_api.jar	%{_javadir}/geronimo-jaf-1.0.2-api.jar	10002
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaf_geronimo-jaf-1.1-api<<EOF
%{_javadir}/jaf.jar	%{_javadir}/geronimo-jaf-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaf_api_geronimo-jaf-1.1-api<<EOF
%{_javadir}/jaf_api.jar	%{_javadir}/geronimo-jaf-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaf_1_1_api_geronimo-jaf-1.1-api<<EOF
%{_javadir}/jaf_1_1_api.jar	%{_javadir}/geronimo-jaf-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/annotation_api_geronimo-annotation-1.0-api<<EOF
%{_javadir}/annotation_api.jar	%{_javadir}/geronimo-annotation-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/annotation_1_0_api_geronimo-annotation-1.0-api<<EOF
%{_javadir}/annotation_1_0_api.jar	%{_javadir}/geronimo-annotation-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/corba_apis_geronimo-corba-1.0-apis<<EOF
%{_javadir}/corba_apis.jar	%{_javadir}/geronimo-corba-1.0-apis.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/corba_1_0_apis_geronimo-corba-1.0-apis<<EOF
%{_javadir}/corba_1_0_apis.jar	%{_javadir}/geronimo-corba-1.0-apis.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/corba_apis_geronimo-corba-2.3-apis<<EOF
%{_javadir}/corba_apis.jar	%{_javadir}/geronimo-corba-2.3-apis.jar	20300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/corba_2_3_apis_geronimo-corba-2.3-apis<<EOF
%{_javadir}/corba_2_3_apis.jar	%{_javadir}/geronimo-corba-2.3-apis.jar	20300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/corba_apis_geronimo-corba-3.0-apis<<EOF
%{_javadir}/corba_apis.jar	%{_javadir}/geronimo-corba-3.0-apis.jar	30000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/corba_3_0_apis_geronimo-corba-3.0-apis<<EOF
%{_javadir}/corba_3_0_apis.jar	%{_javadir}/geronimo-corba-3.0-apis.jar	30000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ejb_geronimo-ejb-2.1-api<<EOF
%{_javadir}/ejb.jar	%{_javadir}/geronimo-ejb-2.1-api.jar	20100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ejb_api_geronimo-ejb-2.1-api<<EOF
%{_javadir}/ejb_api.jar	%{_javadir}/geronimo-ejb-2.1-api.jar	20100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ejb_2_1_api_geronimo-ejb-2.1-api<<EOF
%{_javadir}/ejb_2_1_api.jar	%{_javadir}/geronimo-ejb-2.1-api.jar	20100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ejb_geronimo-ejb-3.0-api<<EOF
%{_javadir}/ejb.jar	%{_javadir}/geronimo-ejb-3.0-api.jar	30000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ejb_api_geronimo-ejb-3.0-api<<EOF
%{_javadir}/ejb_api.jar	%{_javadir}/geronimo-ejb-3.0-api.jar	30000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ejb_3_0_api_geronimo-ejb-3.0-api<<EOF
%{_javadir}/ejb_3_0_api.jar	%{_javadir}/geronimo-ejb-3.0-api.jar	30000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/el_api_geronimo-el-1.0-api<<EOF
%{_javadir}/el_api.jar	%{_javadir}/geronimo-el-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/el_1_0_api_geronimo-el-1.0-api<<EOF
%{_javadir}/el_1_0_api.jar	%{_javadir}/geronimo-el-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/interceptor_api_geronimo-interceptor-3.0-api<<EOF
%{_javadir}/interceptor_api.jar	%{_javadir}/geronimo-interceptor-3.0-api.jar	30000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/interceptor_3_0_api_geronimo-interceptor-3.0-api<<EOF
%{_javadir}/interceptor_3_0_api.jar	%{_javadir}/geronimo-interceptor-3.0-api.jar	30000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee-connector_geronimo-j2ee-connector-1.5-api<<EOF
%{_javadir}/j2ee-connector.jar	%{_javadir}/geronimo-j2ee-connector-1.5-api.jar	10500
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee_connector_api_geronimo-j2ee-connector-1.5-api<<EOF
%{_javadir}/j2ee_connector_api.jar	%{_javadir}/geronimo-j2ee-connector-1.5-api.jar	10500
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee_connector_1_5_api_geronimo-j2ee-connector-1.5-api<<EOF
%{_javadir}/j2ee_connector_1_5_api.jar	%{_javadir}/geronimo-j2ee-connector-1.5-api.jar	10500
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee-deployment_geronimo-j2ee-deployment-1.1-api<<EOF
%{_javadir}/j2ee-deployment.jar	%{_javadir}/geronimo-j2ee-deployment-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee_deployment_api_geronimo-j2ee-deployment-1.1-api<<EOF
%{_javadir}/j2ee_deployment_api.jar	%{_javadir}/geronimo-j2ee-deployment-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee_deployment_1_1_api_geronimo-j2ee-deployment-1.1-api<<EOF
%{_javadir}/j2ee_deployment_1_1_api.jar	%{_javadir}/geronimo-j2ee-deployment-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/javaee_deployment_api_geronimo-javaee-deployment-1.1-api<<EOF
%{_javadir}/javaee_deployment_api.jar	%{_javadir}/geronimo-javaee-deployment-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/javaee_deployment_1_1MR3_api_geronimo-javaee-deployment-1.1-api<<EOF
%{_javadir}/javaee_deployment_1_1MR3_api.jar	%{_javadir}/geronimo-javaee-deployment-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jacc_geronimo-jacc-1.0-api<<EOF
%{_javadir}/jacc.jar	%{_javadir}/geronimo-jacc-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jacc_api_geronimo-jacc-1.0-api<<EOF
%{_javadir}/jacc_api.jar	%{_javadir}/geronimo-jacc-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jacc_1_0_api_geronimo-jacc-1.0-api<<EOF
%{_javadir}/jacc_1_0_api.jar	%{_javadir}/geronimo-jacc-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jacc_api_geronimo-jacc-1.1-api<<EOF
%{_javadir}/jacc_api.jar	%{_javadir}/geronimo-jacc-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jacc_1_1_api_geronimo-jacc-1.1-api<<EOF
%{_javadir}/jacc_1_1_api.jar	%{_javadir}/geronimo-jacc-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee-management_geronimo-j2ee-management-1.0-api<<EOF
%{_javadir}/j2ee-management.jar	%{_javadir}/geronimo-j2ee-management-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee_management_api_geronimo-j2ee-management-1.0-api<<EOF
%{_javadir}/j2ee_management_api.jar	%{_javadir}/geronimo-j2ee-management-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee_management_1_0_api_geronimo-j2ee-management-1.0-api<<EOF
%{_javadir}/j2ee_management_1_0_api.jar	%{_javadir}/geronimo-j2ee-management-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee-management_geronimo-j2ee-management-1.1-api<<EOF
%{_javadir}/j2ee-management.jar	%{_javadir}/geronimo-j2ee-management-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee_management_api_geronimo-j2ee-management-1.1-api<<EOF
%{_javadir}/j2ee_management_api.jar	%{_javadir}/geronimo-j2ee-management-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee_management_1_1_api_geronimo-j2ee-management-1.1-api<<EOF
%{_javadir}/j2ee_management_1_1_api.jar	%{_javadir}/geronimo-j2ee-management-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/javamail_api_geronimo-javamail-1.3.1-api<<EOF
%{_javadir}/javamail_api.jar	%{_javadir}/geronimo-javamail-1.3.1-api.jar	10301
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/javamail_1_3_1_api_geronimo-javamail-1.3.1-api<<EOF
%{_javadir}/javamail_1_3_1_api.jar	%{_javadir}/geronimo-javamail-1.3.1-api.jar	10301
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/javamail_api_geronimo-javamail-1.4-api<<EOF
%{_javadir}/javamail_api.jar	%{_javadir}/geronimo-javamail-1.4-api.jar	10400
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/javamail_1_4_api_geronimo-javamail-1.4-api<<EOF
%{_javadir}/javamail_1_4_api.jar	%{_javadir}/geronimo-javamail-1.4-api.jar	10400
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxr_geronimo-jaxr-1.0-api<<EOF
%{_javadir}/jaxr.jar	%{_javadir}/geronimo-jaxr-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxr_api_geronimo-jaxr-1.0-api<<EOF
%{_javadir}/jaxr_api.jar	%{_javadir}/geronimo-jaxr-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxr_1_0_api_geronimo-jaxr-1.0-api<<EOF
%{_javadir}/jaxr_1_0_api.jar	%{_javadir}/geronimo-jaxr-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxrpc_geronimo-jaxrpc-1.1-api<<EOF
%{_javadir}/jaxrpc.jar	%{_javadir}/geronimo-jaxrpc-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxrpc_api_geronimo-jaxrpc-1.1-api<<EOF
%{_javadir}/jaxrpc_api.jar	%{_javadir}/geronimo-jaxrpc-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxrpc_1_1_api_geronimo-jaxrpc-1.1-api<<EOF
%{_javadir}/jaxrpc_1_1_api.jar	%{_javadir}/geronimo-jaxrpc-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jms_geronimo-jms-1.1-api<<EOF
%{_javadir}/jms.jar	%{_javadir}/geronimo-jms-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jms_api_geronimo-jms-1.1-api<<EOF
%{_javadir}/jms_api.jar	%{_javadir}/geronimo-jms-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jms_1_1_api_geronimo-jms-1.1-api<<EOF
%{_javadir}/jms_1_1_api.jar	%{_javadir}/geronimo-jms-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jpa_api_geronimo-jpa-3.0-api<<EOF
%{_javadir}/jpa_api.jar	%{_javadir}/geronimo-jpa-3.0-api.jar	30000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jpa_3_0_api_geronimo-jpa-3.0-api<<EOF
%{_javadir}/jpa_3_0_api.jar	%{_javadir}/geronimo-jpa-3.0-api.jar	30000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_geronimo-jsp-2.0-api<<EOF
%{_javadir}/jsp.jar	%{_javadir}/geronimo-jsp-2.0-api.jar	20000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_api_geronimo-jsp-2.0-api<<EOF
%{_javadir}/jsp_api.jar	%{_javadir}/geronimo-jsp-2.0-api.jar	20000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_2_0_api_geronimo-jsp-2.0-api<<EOF
%{_javadir}/jsp_2_0_api.jar	%{_javadir}/geronimo-jsp-2.0-api.jar	20000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_geronimo-jsp-2.1-api<<EOF
%{_javadir}/jsp.jar	%{_javadir}/geronimo-jsp-2.1-api.jar	20100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_api_geronimo-jsp-2.1-api<<EOF
%{_javadir}/jsp_api.jar	%{_javadir}/geronimo-jsp-2.1-api.jar	20100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_2_1_api_geronimo-jsp-2.1-api<<EOF
%{_javadir}/jsp_2_1_api.jar	%{_javadir}/geronimo-jsp-2.1-api.jar	20100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jta_geronimo-jta-1.0.1B-api<<EOF
%{_javadir}/jta.jar	%{_javadir}/geronimo-jta-1.0.1B-api.jar	10001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jta_api_geronimo-jta-1.0.1B-api<<EOF
%{_javadir}/jta_api.jar	%{_javadir}/geronimo-jta-1.0.1B-api.jar	10001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jta_1_0_1B_api_geronimo-jta-1.0.1B-api<<EOF
%{_javadir}/jta_1_0_1B_api.jar	%{_javadir}/geronimo-jta-1.0.1B-api.jar	10001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jta_geronimo-jta-1.1-api<<EOF
%{_javadir}/jta.jar	%{_javadir}/geronimo-jta-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jta_api_geronimo-jta-1.1-api<<EOF
%{_javadir}/jta_api.jar	%{_javadir}/geronimo-jta-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jta_1_1_api_geronimo-jta-1.1-api<<EOF
%{_javadir}/jta_1_1_api.jar	%{_javadir}/geronimo-jta-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/qname_api_geronimo-qname-1.1-api<<EOF
%{_javadir}/qname_api.jar	%{_javadir}/geronimo-qname-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/qname_1_1_api_geronimo-qname-1.1-api<<EOF
%{_javadir}/qname_1_1_api.jar	%{_javadir}/geronimo-qname-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/saaj_geronimo-saaj-1.1-api<<EOF
%{_javadir}/saaj.jar	%{_javadir}/geronimo-saaj-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/saaj_api_geronimo-saaj-1.1-api<<EOF
%{_javadir}/saaj_api.jar	%{_javadir}/geronimo-saaj-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/saaj_1_1_api_geronimo-saaj-1.1-api<<EOF
%{_javadir}/saaj_1_1_api.jar	%{_javadir}/geronimo-saaj-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_geronimo-servlet-2.4-api<<EOF
%{_javadir}/servlet.jar	%{_javadir}/geronimo-servlet-2.4-api.jar	20400
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_api_geronimo-servlet-2.4-api<<EOF
%{_javadir}/servlet_api.jar	%{_javadir}/geronimo-servlet-2.4-api.jar	20400
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_2_4_api_geronimo-servlet-2.4-api<<EOF
%{_javadir}/servlet_2_4_api.jar	%{_javadir}/geronimo-servlet-2.4-api.jar	20400
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_geronimo-servlet-2.5-api<<EOF
%{_javadir}/servlet.jar	%{_javadir}/geronimo-servlet-2.5-api.jar	20500
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_api_geronimo-servlet-2.5-api<<EOF
%{_javadir}/servlet_api.jar	%{_javadir}/geronimo-servlet-2.5-api.jar	20500
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_2_5_api_geronimo-servlet-2.5-api<<EOF
%{_javadir}/servlet_2_5_api.jar	%{_javadir}/geronimo-servlet-2.5-api.jar	20500
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/stax_api_geronimo-stax-1.0-api<<EOF
%{_javadir}/stax_api.jar	%{_javadir}/geronimo-stax-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/stax_1_0_api_geronimo-stax-1.0-api<<EOF
%{_javadir}/stax_1_0_api.jar	%{_javadir}/geronimo-stax-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ws_metadata_api_geronimo-ws-metadata-2.0-api<<EOF
%{_javadir}/ws_metadata_api.jar	%{_javadir}/geronimo-ws-metadata-2.0-api.jar	20000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ws_metadata_2_0_api_geronimo-ws-metadata-2.0-api<<EOF
%{_javadir}/ws_metadata_2_0_api.jar	%{_javadir}/geronimo-ws-metadata-2.0-api.jar	20000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaf_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/jaf_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaf_1_0_2_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/jaf_1_0_2_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/commonj_apis_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/commonj_apis.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/commonj_1_1_apis_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/commonj_1_1_apis.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/corba_apis_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/corba_apis.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/corba_2_3_apis_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/corba_2_3_apis.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ejb_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/ejb_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ejb_2_1_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/ejb_2_1_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee-connector_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/j2ee-connector.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee_connector_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/j2ee_connector_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee_1_5_connector_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/j2ee_connector_1_5_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee_deployment_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/j2ee_deployment_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee_deployment_1_1_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/j2ee_deployment_1_1_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee_management_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/j2ee_management_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee_management_1_0_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/j2ee_management_1_0_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jacc_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/jacc_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jacc_1_0_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/jacc_1_0_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/javamail_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/javamail_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/javamail_1_3_1_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/javamail_1_3_1_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxr_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/jaxr_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxr_1_0_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/jaxr_1_0_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxrpc_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/jaxrpc_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxrpc_1_1_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/jaxrpc_1_1_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jms_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/jms_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jms_1_1_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/jms_1_1_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/jsp_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_2_0_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/jsp_2_0_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jta_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/jta_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jta_1_0_1B_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/jta_1_0_1B_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/qname_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/qname_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/qname_1_1_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/qname_1_1_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/saaj_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/saaj_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/saaj_1_1_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/saaj_1_1_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/servlet_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_2_4_api_geronimo-j2ee-1.4-apis<<EOF
%{_javadir}/servlet_2_4_api.jar	%{_javadir}/geronimo-j2ee-1.4-apis.jar	00001
EOF

%if 0
%triggerpostun -n geronimo-ejb-2.1-api -- ejb <= 0:2.1-3jpp_2rh
# Remove file from old non-free packages
rm -f %{_javadir}/ejb.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/ejb %{_javadir}/ejb.jar
%endif

%if 0
%triggerpostun -n geronimo-ejb-3.0-api -- ejb <= 0:2.1-3jpp_2rh
# Remove file from old non-free packages
rm -f %{_javadir}/ejb.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/ejb %{_javadir}/ejb.jar
%endif

%if 0
%triggerpostun -n geronimo-j2ee-connector-1.5-api -- j2ee-connector <= 0:1.5-3jpp_2rh
# Remove file from old non-free packages
rm -f %{_javadir}/j2ee-connector.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/j2ee-connector %{_javadir}/j2ee-connector.jar
%endif

%if 0
%triggerpostun -n geronimo-j2ee-deployment-1.1-api -- j2ee-deployment <= 0:1.1-1jpp_1rh
# Remove file from old non-free packages
rm -f %{_javadir}/j2ee-deployment.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/j2ee-deployment %{_javadir}/j2ee-deployment.jar
%endif

%if 0
%triggerpostun -n geronimo-jacc-1.0-api -- jacc <= 0:1.0-1jpp
# Remove file from old non-free packages
rm -f %{_javadir}/jacc.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/jacc %{_javadir}/jacc.jar
%endif

%if 0
%triggerpostun -n geronimo-jacc-1.1-api -- jacc <= 0:1.0-1jpp
# Remove file from old non-free packages
rm -f %{_javadir}/jacc.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/jacc %{_javadir}/jacc.jar
%endif

%if 0
%triggerpostun -n geronimo-j2ee-management-1.0-api -- j2ee-management <= 0:1.0-1jpp_1rh
# Remove file from old non-free packages
rm -f %{_javadir}/j2ee-management.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/j2ee-management %{_javadir}/j2ee-management.jar
%endif

%if 0
%triggerpostun -n geronimo-j2ee-management-1.1-api -- j2ee-management <= 0:1.0-1jpp_1rh
# Remove file from old non-free packages
rm -f %{_javadir}/j2ee-management.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/j2ee-management %{_javadir}/j2ee-management.jar
%endif

%if 0
%triggerpostun -n geronimo-jaxr-1.0-api -- jaxr-api <= 0:1.0-1jpp
# Remove file from old non-free packages
rm -f %{_javadir}/jaxr.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/jaxr %{_javadir}/jaxr.jar
%endif

%if 0
%triggerpostun -n geronimo-jms-1.1-api -- jms <= 0:1.1-3jpp_2rh
# Remove file from old non-free packages
rm -f %{_javadir}/jms.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/jms %{_javadir}/jms.jar
%endif

%if 0
%triggerpostun -n geronimo-jta-1.0.1B-api -- jta <= 0:1.0.1-0.b.3jpp_2rh
# Remove file from old non-free packages
rm -f %{_javadir}/jta.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/jta %{_javadir}/jta.jar
%endif

%if 0
%triggerpostun -n geronimo-jta-1.1-api -- jta <= 0:1.0.1-0.b.3jpp_2rh
# Remove file from old non-free packages
rm -f %{_javadir}/jta.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/jta %{_javadir}/jta.jar
%endif

%files
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%dir %{_javadir}*/geronimo
%{_javadir}*/geronimo/spec-annotation-1.0-*.jar
%{_javadir}*/geronimo/spec-annotation-1.0.jar
%{_javadir}*/geronimo/spec-commonj-1.1-*.jar
%{_javadir}*/geronimo/spec-commonj-1.1.jar
%{_javadir}*/geronimo/spec-ejb-2.1-*.jar
%{_javadir}*/geronimo/spec-ejb-2.1.jar
%{_javadir}*/geronimo/spec-ejb-3.0-*.jar
%{_javadir}*/geronimo/spec-ejb-3.0.jar
%{_javadir}*/geronimo/spec-el-1.0-*.jar
%{_javadir}*/geronimo/spec-el-1.0.jar
%{_javadir}*/geronimo/spec-interceptor-3.0-*.jar
%{_javadir}*/geronimo/spec-interceptor-3.0.jar
%{_javadir}*/geronimo/spec-j2ee-1.4-*.jar
%{_javadir}*/geronimo/spec-j2ee-1.4.jar
%{_javadir}*/geronimo/spec-j2ee-connector-1.5-*.jar
%{_javadir}*/geronimo/spec-j2ee-connector-1.5.jar
%{_javadir}*/geronimo/spec-j2ee-deployment-1.1-*.jar
%{_javadir}*/geronimo/spec-j2ee-deployment-1.1.jar
%{_javadir}*/geronimo/spec-j2ee-management-1.0-*.jar
%{_javadir}*/geronimo/spec-j2ee-management-1.0.jar
%{_javadir}*/geronimo/spec-j2ee-management-1.1-*.jar
%{_javadir}*/geronimo/spec-j2ee-management-1.1.jar
%{_javadir}*/geronimo/spec-jacc-1.0-*.jar
%{_javadir}*/geronimo/spec-jacc-1.0.jar
%{_javadir}*/geronimo/spec-jacc-1.1-*.jar
%{_javadir}*/geronimo/spec-jacc-1.1.jar
%{_javadir}*/geronimo/spec-jaf-1.0.2-*.jar
%{_javadir}*/geronimo/spec-jaf-1.0.2.jar
%{_javadir}*/geronimo/spec-jaf-1.1-*.jar
%{_javadir}*/geronimo/spec-jaf-1.1.jar
%{_javadir}*/geronimo/spec-javaee-deployment-1.1-*.jar
%{_javadir}*/geronimo/spec-javaee-deployment-1.1.jar
%{_javadir}*/geronimo/spec-jms-1.1-*.jar
%{_javadir}*/geronimo/spec-jms-1.1.jar
%{_javadir}*/geronimo/spec-jpa-3.0-*.jar
%{_javadir}*/geronimo/spec-jpa-3.0.jar
%{_javadir}*/geronimo/spec-jsp-2.0-*.jar
%{_javadir}*/geronimo/spec-jsp-2.0.jar
%{_javadir}*/geronimo/spec-jsp-2.1-*.jar
%{_javadir}*/geronimo/spec-jsp-2.1.jar
%{_javadir}*/geronimo/spec-jta-1.0.1B-*.jar
%{_javadir}*/geronimo/spec-jta-1.0.1B.jar
%{_javadir}*/geronimo/spec-jta-1.1-*.jar
%{_javadir}*/geronimo/spec-jta-1.1.jar
%{_javadir}*/geronimo/spec-servlet-2.4-*.jar
%{_javadir}*/geronimo/spec-servlet-2.4.jar
%{_javadir}*/geronimo/spec-servlet-2.5-*.jar
%{_javadir}*/geronimo/spec-servlet-2.5.jar
%{_javadir}*/geronimo/spec-stax-1.0-*.jar
%{_javadir}*/geronimo/spec-stax-1.0.jar
%{_javadir}*/geronimo/spec-ws-metadata-2.0-*.jar
%{_javadir}*/geronimo/spec-ws-metadata-2.0.jar
%{_datadir}/maven2/poms/JPP-geronimo-specs.pom
%{_mavendepmapfragdir}/%{name}
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files -n geronimo-commonj-1.1-apis
%_altdir/commonj_1_1_apis_geronimo-commonj-1.1-apis
%_altdir/commonj_apis_geronimo-commonj-1.1-apis
%{_javadir}*/geronimo-commonj-1.1-apis*.jar
%exclude %{_javadir}*/commonj_1_1_apis.jar
%exclude %{_javadir}*/commonj_apis.jar
%{_datadir}/maven2/poms/JPP-geronimo-commonj-1.1-apis.pom
%doc %{_docdir}/%{name}-%{version}/commonj-1.1/LICENSE.txt
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/commonj-1.1
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-commonj-1.1-apis
%{_mavendepmapfragdir}/geronimo-commonj-1.1-apis
%{_mavendepmapfragdir}/geronimo-commonj-1.1-apis

%files -n geronimo-jaf-1.0.2-api
%_altdir/jaf_1_0_2_api_geronimo-jaf-1.0.2-api
%_altdir/jaf_api_geronimo-jaf-1.0.2-api
%_altdir/jaf_geronimo-jaf-1.0.2-api
%doc %{_docdir}/%{name}-%{version}/jaf-1.0.2/LICENSE.txt
%{_javadir}*/geronimo-jaf-1.0.2-api*.jar
%exclude %{_javadir}*/jaf.jar
%exclude %{_javadir}*/jaf_api.jar
%exclude %{_javadir}*/jaf_1_0_2_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-jaf-1.0.2-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/jaf-1.0.2
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-jaf-1.0.2-api
%{_mavendepmapfragdir}/geronimo-jaf-1.0.2-api
%{_mavendepmapfragdir}/geronimo-jaf-1.0.2-api

%files -n geronimo-jaf-1.1-api
%_altdir/jaf_1_1_api_geronimo-jaf-1.1-api
%_altdir/jaf_api_geronimo-jaf-1.1-api
%_altdir/jaf_geronimo-jaf-1.1-api
%{_javadir}*/geronimo-jaf-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/jaf-1.1/LICENSE.txt
%exclude %{_javadir}*/jaf.jar
%exclude %{_javadir}*/jaf_api.jar
%exclude %{_javadir}*/jaf_1_1_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-jaf-1.1-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}
%doc %dir %{_docdir}/%{name}-%{version}/jaf-1.1
%{_mavendepmapfragdir}/geronimo-jaf-1.1-api
%{_mavendepmapfragdir}/geronimo-jaf-1.1-api
%{_mavendepmapfragdir}/geronimo-jaf-1.1-api

%files -n geronimo-annotation-1.0-api
%_altdir/annotation_1_0_api_geronimo-annotation-1.0-api
%_altdir/annotation_api_geronimo-annotation-1.0-api
%doc %{_docdir}/%{name}-%{version}/annotation-1.0/LICENSE.txt
%exclude %{_javadir}*/annotation_api.jar
%exclude %{_javadir}*/annotation_1_0_api.jar
%{_javadir}*/geronimo-annotation-1.0-api*.jar
%{_datadir}/maven2/poms/JPP-geronimo-annotation-1.0-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/annotation-1.0
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-annotation-1.0-api
%{_mavendepmapfragdir}/geronimo-annotation-1.0-api
%{_mavendepmapfragdir}/geronimo-annotation-1.0-api

%files -n geronimo-corba-1.0-apis
%_altdir/corba_1_0_apis_geronimo-corba-1.0-apis
%_altdir/corba_apis_geronimo-corba-1.0-apis
%{_javadir}*/geronimo-corba-1.0-apis*.jar
#%doc %{_docdir}/%{name}-%{version}/corba-1.0/LICENSE.txt
%exclude %{_javadir}*/corba_apis.jar
%exclude %{_javadir}*/corba_1_0_apis.jar
%{_datadir}/maven2/poms/JPP-geronimo-corba-1.0-apis.pom
%{_mavendepmapfragdir}/geronimo-corba-1.0-apis
%{_mavendepmapfragdir}/geronimo-corba-1.0-apis
%{_mavendepmapfragdir}/geronimo-corba-1.0-apis

%files -n geronimo-corba-2.3-apis
%_altdir/corba_2_3_apis_geronimo-corba-2.3-apis
%_altdir/corba_apis_geronimo-corba-2.3-apis
%{_javadir}*/geronimo-corba-2.3-apis*.jar
%doc %{_docdir}/%{name}-%{version}/corba-2.3/LICENSE.txt
%exclude %{_javadir}*/corba_apis.jar
%exclude %{_javadir}*/corba_2_3_apis.jar
%{_datadir}/maven2/poms/JPP-geronimo-corba-2.3-apis.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/corba-2.3
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-corba-2.3-apis
%{_mavendepmapfragdir}/geronimo-corba-2.3-apis
%{_mavendepmapfragdir}/geronimo-corba-2.3-apis

%files -n geronimo-corba-3.0-apis
%_altdir/corba_3_0_apis_geronimo-corba-3.0-apis
%_altdir/corba_apis_geronimo-corba-3.0-apis
%{_javadir}*/geronimo-corba-3.0-apis*.jar
%doc %{_docdir}/%{name}-%{version}/corba-3.0/LICENSE.txt
%exclude %{_javadir}*/corba_apis.jar
%exclude %{_javadir}*/corba_3_0_apis.jar
%{_datadir}/maven2/poms/JPP-geronimo-corba-3.0-apis.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/corba-3.0
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-corba-3.0-apis
%{_mavendepmapfragdir}/geronimo-corba-3.0-apis
%{_mavendepmapfragdir}/geronimo-corba-3.0-apis

%files -n geronimo-ejb-2.1-api
%_altdir/ejb_2_1_api_geronimo-ejb-2.1-api
%_altdir/ejb_api_geronimo-ejb-2.1-api
%_altdir/ejb_geronimo-ejb-2.1-api
%doc %{_docdir}/%{name}-%{version}/ejb-2.1/LICENSE.txt
%exclude %{_javadir}*/ejb.jar
%exclude %{_javadir}*/ejb_api.jar
%exclude %{_javadir}*/ejb_2_1_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-ejb-2.1-api.pom
%{_javadir}*/geronimo-ejb-2.1-api*.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/ejb-2.1
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-ejb-2.1-api
%{_mavendepmapfragdir}/geronimo-ejb-2.1-api
%{_mavendepmapfragdir}/geronimo-ejb-2.1-api
%{_mavendepmapfragdir}/geronimo-ejb-2.1-api

%files -n geronimo-ejb-3.0-api
%_altdir/ejb_3_0_api_geronimo-ejb-3.0-api
%_altdir/ejb_api_geronimo-ejb-3.0-api
%_altdir/ejb_geronimo-ejb-3.0-api
%doc %{_docdir}/%{name}-%{version}/ejb-3.0/LICENSE.txt
%exclude %{_javadir}*/ejb.jar
%exclude %{_javadir}*/ejb_api.jar
%exclude %{_javadir}*/ejb_3_0_api.jar
%{_javadir}*/geronimo-ejb-3.0-api*.jar
%{_datadir}/maven2/poms/JPP-geronimo-ejb-3.0-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/ejb-3.0
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-ejb-3.0-api
%{_mavendepmapfragdir}/geronimo-ejb-3.0-api
%{_mavendepmapfragdir}/geronimo-ejb-3.0-api
%{_mavendepmapfragdir}/geronimo-ejb-3.0-api

%files -n geronimo-el-1.0-api
%_altdir/el_1_0_api_geronimo-el-1.0-api
%_altdir/el_api_geronimo-el-1.0-api
%{_javadir}*/geronimo-el-1.0-api*.jar
%doc %{_docdir}/%{name}-%{version}/el-1.0/LICENSE.txt
%exclude %{_javadir}*/el_api.jar
%exclude %{_javadir}*/el_1_0_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-el-1.0-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/el-1.0
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-el-1.0-api
%{_mavendepmapfragdir}/geronimo-el-1.0-api
%{_mavendepmapfragdir}/geronimo-el-1.0-api

%files -n geronimo-interceptor-3.0-api
%_altdir/interceptor_3_0_api_geronimo-interceptor-3.0-api
%_altdir/interceptor_api_geronimo-interceptor-3.0-api
%doc %{_docdir}/%{name}-%{version}/interceptor-3.0/LICENSE.txt
%exclude %{_javadir}*/interceptor_api.jar
%exclude %{_javadir}*/interceptor_3_0_api.jar
%{_javadir}*/geronimo-interceptor-3.0-api*.jar
%{_datadir}/maven2/poms/JPP-geronimo-interceptor-3.0-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}
%doc %dir %{_docdir}/%{name}-%{version}/interceptor-3.0
%{_mavendepmapfragdir}/geronimo-interceptor-3.0-api
%{_mavendepmapfragdir}/geronimo-interceptor-3.0-api
%{_mavendepmapfragdir}/geronimo-interceptor-3.0-api

%files -n geronimo-j2ee-1.4-apis
%_altdir/servlet_2_4_api_geronimo-j2ee-1.4-apis
%_altdir/servlet_api_geronimo-j2ee-1.4-apis
%_altdir/saaj_1_1_api_geronimo-j2ee-1.4-apis
%_altdir/saaj_api_geronimo-j2ee-1.4-apis
%_altdir/qname_1_1_api_geronimo-j2ee-1.4-apis
%_altdir/qname_api_geronimo-j2ee-1.4-apis
%_altdir/jta_1_0_1B_api_geronimo-j2ee-1.4-apis
%_altdir/jta_api_geronimo-j2ee-1.4-apis
%_altdir/jsp_2_0_api_geronimo-j2ee-1.4-apis
%_altdir/jsp_api_geronimo-j2ee-1.4-apis
%_altdir/jms_1_1_api_geronimo-j2ee-1.4-apis
%_altdir/jms_api_geronimo-j2ee-1.4-apis
%_altdir/jaxrpc_1_1_api_geronimo-j2ee-1.4-apis
%_altdir/jaxrpc_api_geronimo-j2ee-1.4-apis
%_altdir/jaxr_1_0_api_geronimo-j2ee-1.4-apis
%_altdir/jaxr_api_geronimo-j2ee-1.4-apis
%_altdir/javamail_1_3_1_api_geronimo-j2ee-1.4-apis
%_altdir/javamail_api_geronimo-j2ee-1.4-apis
%_altdir/jacc_1_0_api_geronimo-j2ee-1.4-apis
%_altdir/jacc_api_geronimo-j2ee-1.4-apis
%_altdir/j2ee_management_1_0_api_geronimo-j2ee-1.4-apis
%_altdir/j2ee_management_api_geronimo-j2ee-1.4-apis
%_altdir/j2ee_deployment_1_1_api_geronimo-j2ee-1.4-apis
%_altdir/j2ee_deployment_api_geronimo-j2ee-1.4-apis
%_altdir/j2ee_1_5_connector_api_geronimo-j2ee-1.4-apis
%_altdir/j2ee_connector_api_geronimo-j2ee-1.4-apis
%_altdir/j2ee-connector_geronimo-j2ee-1.4-apis
%_altdir/ejb_2_1_api_geronimo-j2ee-1.4-apis
%_altdir/ejb_api_geronimo-j2ee-1.4-apis
%_altdir/corba_2_3_apis_geronimo-j2ee-1.4-apis
%_altdir/corba_apis_geronimo-j2ee-1.4-apis
%_altdir/commonj_1_1_apis_geronimo-j2ee-1.4-apis
%_altdir/commonj_apis_geronimo-j2ee-1.4-apis
%_altdir/jaf_1_0_2_api_geronimo-j2ee-1.4-apis
%_altdir/jaf_api_geronimo-j2ee-1.4-apis
%doc %{_docdir}/%{name}-%{version}/j2ee-1.4/LICENSE.txt
%{_javadir}*/geronimo-j2ee-1.4-apis*.jar
%{_datadir}/maven2/poms/JPP-geronimo-j2ee-1.4-apis.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/j2ee-1.4
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-j2ee-1.4-apis
%{_mavendepmapfragdir}/geronimo-j2ee-1.4-apis
%{_mavendepmapfragdir}/geronimo-j2ee-1.4-apis

%files -n geronimo-j2ee-connector-1.5-api
%_altdir/j2ee_connector_1_5_api_geronimo-j2ee-connector-1.5-api
%_altdir/j2ee_connector_api_geronimo-j2ee-connector-1.5-api
%_altdir/j2ee-connector_geronimo-j2ee-connector-1.5-api
%{_javadir}*/geronimo-j2ee-connector-1.5-api*.jar
%doc %{_docdir}/%{name}-%{version}/j2ee-connector-1.5/LICENSE.txt
%exclude %{_javadir}*/j2ee-connector.jar
%exclude %{_javadir}*/j2ee_connector_api.jar
%exclude %{_javadir}*/j2ee_connector_1_5_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-j2ee-connector-1.5-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/j2ee-connector-1.5
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-j2ee-connector-1.5-api
%{_mavendepmapfragdir}/geronimo-j2ee-connector-1.5-api
%{_mavendepmapfragdir}/geronimo-j2ee-connector-1.5-api
%{_mavendepmapfragdir}/geronimo-j2ee-connector-1.5-api

%files -n geronimo-j2ee-deployment-1.1-api
%_altdir/j2ee_deployment_1_1_api_geronimo-j2ee-deployment-1.1-api
%_altdir/j2ee_deployment_api_geronimo-j2ee-deployment-1.1-api
%_altdir/j2ee-deployment_geronimo-j2ee-deployment-1.1-api
%{_javadir}*/geronimo-j2ee-deployment-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/j2ee-deployment-1.1/LICENSE.txt
%exclude %{_javadir}*/j2ee-deployment.jar
%exclude %{_javadir}*/j2ee_deployment_api.jar
%exclude %{_javadir}*/j2ee_deployment_1_1_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-j2ee-deployment-1.1-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/j2ee-deployment-1.1
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-j2ee-deployment-1.1-api
%{_mavendepmapfragdir}/geronimo-j2ee-deployment-1.1-api
%{_mavendepmapfragdir}/geronimo-j2ee-deployment-1.1-api
%{_mavendepmapfragdir}/geronimo-j2ee-deployment-1.1-api

%files -n geronimo-javaee-deployment-1.1-api
%_altdir/javaee_deployment_1_1MR3_api_geronimo-javaee-deployment-1.1-api
%_altdir/javaee_deployment_api_geronimo-javaee-deployment-1.1-api
%{_javadir}*/geronimo-javaee-deployment-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/javaee-deployment-1.1/LICENSE.txt
%exclude %{_javadir}*/javaee_deployment_api.jar
%exclude %{_javadir}*/javaee_deployment_1_1MR3_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-javaee-deployment-1.1-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/javaee-deployment-1.1
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-javaee-deployment-1.1-api
%{_mavendepmapfragdir}/geronimo-javaee-deployment-1.1-api
%{_mavendepmapfragdir}/geronimo-javaee-deployment-1.1-api

%files -n geronimo-jacc-1.0-api
%_altdir/jacc_1_0_api_geronimo-jacc-1.0-api
%_altdir/jacc_api_geronimo-jacc-1.0-api
%_altdir/jacc_geronimo-jacc-1.0-api
%{_javadir}*/geronimo-jacc-1.0-api*.jar
%doc %{_docdir}/%{name}-%{version}/jacc-1.0/LICENSE.txt
%exclude %{_javadir}*/jacc.jar
%exclude %{_javadir}*/jacc_api.jar
%exclude %{_javadir}*/jacc_1_0_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-jacc-1.0-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/jacc-1.0
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-jacc-1.0-api
%{_mavendepmapfragdir}/geronimo-jacc-1.0-api
%{_mavendepmapfragdir}/geronimo-jacc-1.0-api
%{_mavendepmapfragdir}/geronimo-jacc-1.0-api

%files -n geronimo-jacc-1.1-api
%_altdir/jacc_1_1_api_geronimo-jacc-1.1-api
%_altdir/jacc_api_geronimo-jacc-1.1-api
%{_javadir}*/geronimo-jacc-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/jacc-1.1/LICENSE.txt
%exclude %{_javadir}*/jacc_api.jar
%exclude %{_javadir}*/jacc_1_1_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-jacc-1.1-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/jacc-1.1
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-jacc-1.1-api
%{_mavendepmapfragdir}/geronimo-jacc-1.1-api
%{_mavendepmapfragdir}/geronimo-jacc-1.1-api
%{_mavendepmapfragdir}/geronimo-jacc-1.1-api

%files -n geronimo-j2ee-management-1.0-api
%_altdir/j2ee_management_1_0_api_geronimo-j2ee-management-1.0-api
%_altdir/j2ee_management_api_geronimo-j2ee-management-1.0-api
%_altdir/j2ee-management_geronimo-j2ee-management-1.0-api
%{_javadir}*/geronimo-j2ee-management-1.0-api*.jar
%doc %{_docdir}/%{name}-%{version}/j2ee-management-1.0/LICENSE.txt
%exclude %{_javadir}*/j2ee-management.jar
%exclude %{_javadir}*/j2ee_management_api.jar
%exclude %{_javadir}*/j2ee_management_1_0_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-j2ee-management-1.0-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/j2ee-management-1.0
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-j2ee-management-1.0-api
%{_mavendepmapfragdir}/geronimo-j2ee-management-1.0-api
%{_mavendepmapfragdir}/geronimo-j2ee-management-1.0-api
%{_mavendepmapfragdir}/geronimo-j2ee-management-1.0-api

%files -n geronimo-j2ee-management-1.1-api
%_altdir/j2ee_management_1_1_api_geronimo-j2ee-management-1.1-api
%_altdir/j2ee_management_api_geronimo-j2ee-management-1.1-api
%_altdir/j2ee-management_geronimo-j2ee-management-1.1-api
%{_javadir}*/geronimo-j2ee-management-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/j2ee-management-1.1/LICENSE.txt
%exclude %{_javadir}*/j2ee-management.jar
%exclude %{_javadir}*/j2ee_management_api.jar
%exclude %{_javadir}*/j2ee_management_1_1_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-j2ee-management-1.1-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/j2ee-management-1.1
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-j2ee-management-1.1-api
%{_mavendepmapfragdir}/geronimo-j2ee-management-1.1-api
%{_mavendepmapfragdir}/geronimo-j2ee-management-1.1-api
%{_mavendepmapfragdir}/geronimo-j2ee-management-1.1-api

%files -n geronimo-javamail-1.3.1-api
%_altdir/javamail_1_3_1_api_geronimo-javamail-1.3.1-api
%_altdir/javamail_api_geronimo-javamail-1.3.1-api
%{_javadir}*/geronimo-javamail-1.3.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/javamail-1.3.1/LICENSE.txt
# Do not provide it as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#%ghost %{_javadir}*/javamail.jar
%exclude %{_javadir}*/javamail_api.jar
%exclude %{_javadir}*/javamail_1_3_1_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-javamail-1.3.1-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}
%doc %dir %{_docdir}/%{name}-%{version}/javamail-1.3.1
%{_mavendepmapfragdir}/geronimo-javamail-1.3.1-api
%{_mavendepmapfragdir}/geronimo-javamail-1.3.1-api
%{_mavendepmapfragdir}/geronimo-javamail-1.3.1-api

%files -n geronimo-javamail-1.4-api
%_altdir/javamail_1_4_api_geronimo-javamail-1.4-api
%_altdir/javamail_api_geronimo-javamail-1.4-api
%doc %{_docdir}/%{name}-%{version}/javamail-1.4/LICENSE.txt
%{_javadir}*/geronimo-javamail-1.4-api*.jar
# Do not provide it as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#%ghost %{_javadir}*/javamail.jar
%exclude %{_javadir}*/javamail_api.jar
%exclude %{_javadir}*/javamail_1_4_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-javamail-1.4-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/javamail-1.4
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-javamail-1.4-api
%{_mavendepmapfragdir}/geronimo-javamail-1.4-api
%{_mavendepmapfragdir}/geronimo-javamail-1.4-api

%files -n geronimo-jaxr-1.0-api
%_altdir/jaxr_1_0_api_geronimo-jaxr-1.0-api
%_altdir/jaxr_api_geronimo-jaxr-1.0-api
%_altdir/jaxr_geronimo-jaxr-1.0-api
%{_javadir}*/geronimo-jaxr-1.0-api*.jar
%doc %{_docdir}/%{name}-%{version}/jaxr-1.0/LICENSE.txt
%exclude %{_javadir}*/jaxr.jar
%exclude %{_javadir}*/jaxr_api.jar
%exclude %{_javadir}*/jaxr_1_0_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-jaxr-1.0-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/jaxr-1.0
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-jaxr-1.0-api
%{_mavendepmapfragdir}/geronimo-jaxr-1.0-api
%{_mavendepmapfragdir}/geronimo-jaxr-1.0-api
%{_mavendepmapfragdir}/geronimo-jaxr-1.0-api

%files -n geronimo-jaxrpc-1.1-api
%_altdir/jaxrpc_1_1_api_geronimo-jaxrpc-1.1-api
%_altdir/jaxrpc_api_geronimo-jaxrpc-1.1-api
%_altdir/jaxrpc_geronimo-jaxrpc-1.1-api
%{_javadir}*/geronimo-jaxrpc-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/jaxrpc-1.1/LICENSE.txt
%exclude %{_javadir}*/jaxrpc.jar
%exclude %{_javadir}*/jaxrpc_api.jar
%exclude %{_javadir}*/jaxrpc_1_1_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-jaxrpc-1.1-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}
%doc %dir %{_docdir}/%{name}-%{version}/jaxrpc-1.1
%{_mavendepmapfragdir}/geronimo-jaxrpc-1.1-api
%{_mavendepmapfragdir}/geronimo-jaxrpc-1.1-api
%{_mavendepmapfragdir}/geronimo-jaxrpc-1.1-api

%files -n geronimo-jms-1.1-api
%_altdir/jms_1_1_api_geronimo-jms-1.1-api
%_altdir/jms_api_geronimo-jms-1.1-api
%_altdir/jms_geronimo-jms-1.1-api
%{_javadir}*/geronimo-jms-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/jms-1.1/LICENSE.txt
%exclude %{_javadir}*/jms.jar
%exclude %{_javadir}*/jms_api.jar
%exclude %{_javadir}*/jms_1_1_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-jms-1.1-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/jms-1.1
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-jms-1.1-api
%{_mavendepmapfragdir}/geronimo-jms-1.1-api
%{_mavendepmapfragdir}/geronimo-jms-1.1-api
%{_mavendepmapfragdir}/geronimo-jms-1.1-api

%files -n geronimo-jpa-3.0-api
%_altdir/jpa_3_0_api_geronimo-jpa-3.0-api
%_altdir/jpa_api_geronimo-jpa-3.0-api
%{_javadir}*/geronimo-jpa-3.0-api*.jar
%doc %{_docdir}/%{name}-%{version}/jpa-3.0/LICENSE.txt
%exclude %{_javadir}*/jpa_api.jar
%exclude %{_javadir}*/jpa_3_0_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-jpa-3.0-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/jpa-3.0
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-jpa-3.0-api
%{_mavendepmapfragdir}/geronimo-jpa-3.0-api
%{_mavendepmapfragdir}/geronimo-jpa-3.0-api

%files -n geronimo-jsp-2.0-api
%_altdir/jsp_2_0_api_geronimo-jsp-2.0-api
%_altdir/jsp_api_geronimo-jsp-2.0-api
%_altdir/jsp_geronimo-jsp-2.0-api
%{_javadir}*/geronimo-jsp-2.0-api*.jar
%doc %{_docdir}/%{name}-%{version}/jsp-2.0/LICENSE.txt
%exclude %{_javadir}*/jsp.jar
%exclude %{_javadir}*/jsp_api.jar
%exclude %{_javadir}*/jsp_2_0_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-jsp-2.0-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/jsp-2.0
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-jsp-2.0-api
%{_mavendepmapfragdir}/geronimo-jsp-2.0-api
%{_mavendepmapfragdir}/geronimo-jsp-2.0-api

%files -n geronimo-jsp-2.1-api
%_altdir/jsp_2_1_api_geronimo-jsp-2.1-api
%_altdir/jsp_api_geronimo-jsp-2.1-api
%_altdir/jsp_geronimo-jsp-2.1-api
%{_javadir}*/geronimo-jsp-2.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/jsp-2.1/LICENSE.txt
%exclude %{_javadir}*/jsp.jar
%exclude %{_javadir}*/jsp_api.jar
%exclude %{_javadir}*/jsp_2_1_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-jsp-2.1-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/jsp-2.1
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-jsp-2.1-api
%{_mavendepmapfragdir}/geronimo-jsp-2.1-api
%{_mavendepmapfragdir}/geronimo-jsp-2.1-api

%files -n geronimo-jta-1.0.1B-api
%_altdir/jta_1_0_1B_api_geronimo-jta-1.0.1B-api
%_altdir/jta_api_geronimo-jta-1.0.1B-api
%_altdir/jta_geronimo-jta-1.0.1B-api
%{_javadir}*/geronimo-jta-1.0.1B-api*.jar
%doc %{_docdir}/%{name}-%{version}/jta-1.0.1B/LICENSE.txt
%exclude %{_javadir}*/jta.jar
%exclude %{_javadir}*/jta_api.jar
%exclude %{_javadir}*/jta_1_0_1B_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-jta-1.0.1B-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/jta-1.0.1B
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-jta-1.0.1B-api
%{_mavendepmapfragdir}/geronimo-jta-1.0.1B-api
%{_mavendepmapfragdir}/geronimo-jta-1.0.1B-api
%{_mavendepmapfragdir}/geronimo-jta-1.0.1B-api

%files -n geronimo-jta-1.1-api
%_altdir/jta_1_1_api_geronimo-jta-1.1-api
%_altdir/jta_api_geronimo-jta-1.1-api
%_altdir/jta_geronimo-jta-1.1-api
%{_javadir}*/geronimo-jta-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/jta-1.1/LICENSE.txt
%exclude %{_javadir}*/jta.jar
%exclude %{_javadir}*/jta_api.jar
%exclude %{_javadir}*/jta_1_1_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-jta-1.1-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/jta-1.1
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-jta-1.1-api
%{_mavendepmapfragdir}/geronimo-jta-1.1-api
%{_mavendepmapfragdir}/geronimo-jta-1.1-api
%{_mavendepmapfragdir}/geronimo-jta-1.1-api

%files -n geronimo-qname-1.1-api
%_altdir/qname_1_1_api_geronimo-qname-1.1-api
%_altdir/qname_api_geronimo-qname-1.1-api
%{_javadir}*/geronimo-qname-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/qname-1.1/LICENSE.txt
%exclude %{_javadir}*/qname_api.jar
%exclude %{_javadir}*/qname_1_1_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-qname-1.1-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/qname-1.1
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-qname-1.1-api
%{_mavendepmapfragdir}/geronimo-qname-1.1-api
%{_mavendepmapfragdir}/geronimo-qname-1.1-api

%files -n geronimo-saaj-1.1-api
%_altdir/saaj_1_1_api_geronimo-saaj-1.1-api
%_altdir/saaj_api_geronimo-saaj-1.1-api
%_altdir/saaj_geronimo-saaj-1.1-api
%{_javadir}*/geronimo-saaj-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/saaj-1.1/LICENSE.txt
%exclude %{_javadir}*/saaj.jar
%exclude %{_javadir}*/saaj_api.jar
%exclude %{_javadir}*/saaj_1_1_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-saaj-1.1-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/saaj-1.1
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-saaj-1.1-api
%{_mavendepmapfragdir}/geronimo-saaj-1.1-api
%{_mavendepmapfragdir}/geronimo-saaj-1.1-api

%files -n geronimo-servlet-2.4-api
%_altdir/servlet_2_4_api_geronimo-servlet-2.4-api
%_altdir/servlet_api_geronimo-servlet-2.4-api
%_altdir/servlet_geronimo-servlet-2.4-api
%{_javadir}*/geronimo-servlet-2.4-api*.jar
%doc %{_docdir}/%{name}-%{version}/servlet-2.4/LICENSE.txt
%exclude %{_javadir}*/servlet.jar
%exclude %{_javadir}*/servlet_api.jar
%exclude %{_javadir}*/servlet_2_4_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-servlet-2.4-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/servlet-2.4
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-servlet-2.4-api
%{_mavendepmapfragdir}/geronimo-servlet-2.4-api
%{_mavendepmapfragdir}/geronimo-servlet-2.4-api

%files -n geronimo-servlet-2.5-api
%_altdir/servlet_2_5_api_geronimo-servlet-2.5-api
%_altdir/servlet_api_geronimo-servlet-2.5-api
%_altdir/servlet_geronimo-servlet-2.5-api
%{_javadir}*/geronimo-servlet-2.5-api*.jar
%doc %{_docdir}/%{name}-%{version}/servlet-2.5/LICENSE.txt
%exclude %{_javadir}*/servlet.jar
%exclude %{_javadir}*/servlet_api.jar
%exclude %{_javadir}*/servlet_2_5_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-servlet-2.5-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/servlet-2.5
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-servlet-2.5-api
%{_mavendepmapfragdir}/geronimo-servlet-2.5-api
%{_mavendepmapfragdir}/geronimo-servlet-2.5-api

%files -n geronimo-stax-1.0-api
%_altdir/stax_1_0_api_geronimo-stax-1.0-api
%_altdir/stax_api_geronimo-stax-1.0-api
%{_javadir}*/geronimo-stax-1.0-api*.jar
%doc %{_docdir}/%{name}-%{version}/stax-1.0/LICENSE.txt
%exclude %{_javadir}*/stax_api.jar
%exclude %{_javadir}*/stax_1_0_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-stax-1.0-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/stax-1.0
%doc %dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/geronimo-stax-1.0-api
%{_mavendepmapfragdir}/geronimo-stax-1.0-api
%{_mavendepmapfragdir}/geronimo-stax-1.0-api

%files -n geronimo-ws-metadata-2.0-api
%_altdir/ws_metadata_2_0_api_geronimo-ws-metadata-2.0-api
%_altdir/ws_metadata_api_geronimo-ws-metadata-2.0-api
%{_javadir}*/geronimo-ws-metadata-2.0-api*.jar
%doc %{_docdir}/%{name}-%{version}/ws-metadata-2.0/LICENSE.txt
%exclude %{_javadir}*/ws_metadata_api.jar
%exclude %{_javadir}*/ws_metadata_2_0_api.jar
%{_datadir}/maven2/poms/JPP-geronimo-ws-metadata-2.0-api.pom
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}
%doc %dir %{_docdir}/%{name}-%{version}/ws-metadata-2.0
%{_mavendepmapfragdir}/geronimo-ws-metadata-2.0-api
%{_mavendepmapfragdir}/geronimo-ws-metadata-2.0-api
%{_mavendepmapfragdir}/geronimo-ws-metadata-2.0-api

%changelog
* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt8_16jpp6
- fixed build with maven3

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt7_16jpp6
- fixed build

* Wed Jan 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt6_16jpp6
- maven depmap fragments moved to subpackages

* Tue Jan 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt5_16jpp6
- fixed pom subpackage

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt4_16jpp6
- new jpp release

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt4_13jpp6
- jpp6 build

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt4_13jpp5
- fixed build

* Fri Aug 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_13jpp5
- new jpp release

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_7jpp5
- removed extra provides from j2ee-apis
- alternatives 0.4 support

* Tue Oct 07 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_7jpp5
- fix unmets

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_7jpp5
- converted from JPackage by jppimport script

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_4jpp1.7
- added obsoletes

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_4jpp1.7
- updated to new jpackage release

* Sat Nov 24 2007 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.M5.9
- removed jspapi.jar symlink; will be handled by alternatives later.

* Fri Aug 31 2007 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.M5.8
- rebuild with new mx4j

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.M5.7
- added geronimo-j2ee-1.4-apis (using dirty hack)

* Fri May 25 2007 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.M5.6
- added lots of jpackage compatible symlinks (hack, should be alternatives)

* Thu May 24 2007 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.M5.5
- added lots of jpackage compatible provides

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.M5.4
- added provides: jsp

* Tue May 08 2007 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.M5.3
- added provides for jpackage

* Sun May 06 2007 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.M5.2
- rebuild with java 1.4

* Thu Nov 24 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt0.M5.1
- Initial build for ALT Linux Sisyphus 

