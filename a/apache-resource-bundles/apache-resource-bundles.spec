BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 3
%define name apache-resource-bundles
# Copyright (c) 2000-2010, JPackage Project
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


%define incubator_disclaimer_version 1.2
%define jar_version 1.5
%define license_header_version 1.2
%define source_release_assembly_descriptor_version 1.0

%define incubator_disclaimer_version_real 1.2-SNAPSHOT
%define jar_version_real 1.5-SNAPSHOT
%define license_header_version_real 1.2-SNAPSHOT
%define source_release_assembly_descriptor_version_real 1.0-SNAPSHOT

%global parent_version %{version}
%global parent_version_real %{version}
%global parent_epoch %{epoch}

Name:           apache-resource-bundles
Version:        3
Release:        alt2_2jpp6
Epoch:          0
Summary:        Apache Resource Bundles
License:        ASL 2.0
Group:          Development/Java
URL:            http://svn.apache.org/repos/asf/maven/resources/tags/apache-resource-bundles-3/
# svn export http://svn.apache.org/repos/asf/maven/resources/tags/apache-resource-bundles-3/ && tar cjf apache-resource-bundles-3.tar.bz2 apache-resource-bundles-3
# Exported revision 1055633.
Source0:        apache-resource-bundles-3.tar.bz2
Source1:        apache-resource-bundles-jpp-depmap.xml
Source2:        apache-resource-bundles-settings.xml
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires:       jpackage-utils
Requires:       maven2
Requires:       maven2-plugin-remote-resources
BuildRequires:  apache-commons-parent
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  maven2 >= 0:2.0.7
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven2-plugin-remote-resources
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-release
BuildRequires:  maven-shared-verifier >= 0:1.2
BuildRequires:  maven-surefire-maven-plugin
BuildArch:      noarch
Source44: import.info

%description
Apache Resource Bundles.

%package -n apache-incubator-disclaimer-resource-bundle
Version:        %{incubator_disclaimer_version}
Epoch:          0
Summary:        Apache Incubator Disclaimer Resource Bundle
Group:          Development/Java
Requires:       %{name} = %{parent_epoch}:%{parent_version}-%{release}

%description -n apache-incubator-disclaimer-resource-bundle
An archive which contains the standard Apache Incubator disclaimer.

%package -n apache-jar-resource-bundle
Version:        %{jar_version}
Epoch:          0
Summary:        Apache JAR Resource Bundle
Group:          Development/Java
Requires:       %{name} = %{parent_epoch}:%{parent_version}-%{release}

%description -n apache-jar-resource-bundle
An archive which contains templates for generating the necessary license files and notices for all Apache releases.

%package -n apache-license-header-resource-bundle
Version:        %{license_header_version}
Epoch:          0
Summary:        Apache License Header Resource Bundle
Group:          Development/Java
Requires:       %{name} = %{parent_epoch}:%{parent_version}-%{release}

%description -n apache-license-header-resource-bundle
An archive which contains the notice file template.

%package -n apache-source-release-assembly-descriptor
Version:        %{source_release_assembly_descriptor_version}
Epoch:          0
Summary:        Apache Source Release Assembly Descriptor
Group:          Development/Java
Requires:       %{name} = %{parent_epoch}:%{parent_version}-%{release}

%description -n apache-source-release-assembly-descriptor
This jar contains a customized source assembly descriptor to produce Apache compliant source bundles.

%if 0
%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.
%endif

%prep
%setup -q 

%{__cp} -p %{SOURCE2} maven2-settings.xml

%{__sed} -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

%{__mkdir} external_repo
%{__ln_s} %{_javadir} external_repo/JPP

%build
export M2SETTINGS=`pwd`/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:aggregate

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}/%{name}
%{__cp} -p apache-incubator-disclaimer-resource-bundle/target/apache-incubator-disclaimer-resource-bundle-%{incubator_disclaimer_version_real}.jar %{buildroot}%{_javadir}/%{name}/apache-incubator-disclaimer-resource-bundle-%{incubator_disclaimer_version_real}.jar
%{__cp} -p apache-jar-resource-bundle/target/apache-jar-resource-bundle-%{jar_version_real}.jar %{buildroot}%{_javadir}/%{name}/apache-jar-resource-bundle-%{jar_version_real}.jar
%{__cp} -p apache-license-header-resource-bundle/target/apache-license-header-resource-bundle-%{license_header_version_real}.jar %{buildroot}%{_javadir}/%{name}/apache-license-header-resource-bundle-%{license_header_version_real}.jar
%{__cp} -p apache-source-release-assembly-descriptor/target/apache-source-release-assembly-descriptor-%{source_release_assembly_descriptor_version_real}.jar %{buildroot}%{_javadir}/%{name}/apache-source-release-assembly-descriptor-%{source_release_assembly_descriptor_version_real}.jar
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{incubator_disclaimer_version_real}*; do %{__ln_s}f ${jar} `echo $jar | %{__sed} "s|-%{incubator_disclaimer_version_real}||g"`; done)
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{jar_version_real}*; do %{__ln_s}f ${jar} `echo $jar | %{__sed} "s|-%{jar_version_real}||g"`; done)
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{license_header_version_real}*; do %{__ln_s}f ${jar} `echo $jar | %{__sed} "s|-%{license_header_version_real}||g"`; done)
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{source_release_assembly_descriptor_version_real}*; do %{__ln_s}f ${jar} `echo $jar | %{__sed} "s|-%{source_release_assembly_descriptor_version_real}||g"`; done)

# pom
mkdir -p %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache apache-resource-bundles %{version_real} JPP %{name}
%{__cp} -p apache-incubator-disclaimer-resource-bundle/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.{name}-apache-incubator-disclaimer-resource-bundle.pom
%add_to_maven_depmap org.apache apache-incubator-disclaimer-resource-bundle %{incubator_disclaimer_version_real} JPP/%{name} apache-incubator-disclaimer-resource-bundle
%{__cp} -p apache-jar-resource-bundle/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-apache-jar-resource-bundle.pom
%add_to_maven_depmap org.apache apache-jar-resource-bundle  %{jar_version_real} JPP/%{name} apache-jar-resource-bundle
%{__cp} -p apache-license-header-resource-bundle/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-apache-license-header-resource-bundle.pom
%add_to_maven_depmap org.apache apache-license-header-resource-bundle %{license_header_version_real} JPP/%{name} apache-license-header-resource-bundle
%{__cp} -p apache-source-release-assembly-descriptor/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-apache-source-release-assembly-descriptor.pom
%add_to_maven_depmap org.apache apache-source-release-assembly-descriptor %{source_release_assembly_descriptor_version_real} JPP/%{name} apache-source-release-assembly-descriptor

%if 0
# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%endif

%files
%dir %{_javadir}/%{name}
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files -n apache-incubator-disclaimer-resource-bundle
%{_javadir}/%{name}/apache-incubator-disclaimer-resource-bundle-%{incubator_disclaimer_version_real}.jar
%{_javadir}/%{name}/apache-incubator-disclaimer-resource-bundle.jar
%{_datadir}/maven2/poms/JPP.{name}-apache-incubator-disclaimer-resource-bundle.pom

%files -n apache-jar-resource-bundle
%{_javadir}/%{name}/apache-jar-resource-bundle-%{jar_version_real}.jar
%{_javadir}/%{name}/apache-jar-resource-bundle.jar
%{_datadir}/maven2/poms/JPP.%{name}-apache-jar-resource-bundle.pom

%files -n apache-license-header-resource-bundle
%{_javadir}/%{name}/apache-license-header-resource-bundle-%{license_header_version_real}.jar
%{_javadir}/%{name}/apache-license-header-resource-bundle.jar
%{_datadir}/maven2/poms/JPP.%{name}-apache-license-header-resource-bundle.pom

%files -n apache-source-release-assembly-descriptor
%{_javadir}/%{name}/apache-source-release-assembly-descriptor-%{source_release_assembly_descriptor_version_real}.jar
%{_javadir}/%{name}/apache-source-release-assembly-descriptor.jar
%{_datadir}/maven2/poms/JPP.%{name}-apache-source-release-assembly-descriptor.pom

%if 0
%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%endif

%changelog
* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:3-alt2_2jpp6
- fixed build

* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:3-alt1_2jpp6
- new jpp relase

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:2-alt2_1jpp6
- apache-jar-resource-bundle is made compat package.

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:2-alt1_1jpp6
- new version
