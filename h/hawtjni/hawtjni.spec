BuildRequires: /proc xbean
BuildRequires: jpackage-compat
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support
%bcond_without example
%bcond_without repolib

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%global arch_name %{_target_os}_%{_target_cpu}


Name:           hawtjni
Version:        1.1
Release:        alt2_4jpp6
Epoch:          0
Summary:        HawtJNI
License:        ASL 2.0
URL:            http://hawtjni.fusesource.org
Group:          Development/Java
# git clone git://forge.fusesource.com/hawtjni.git
# git checkout hawtjni-1.1
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Patch0:         hawtjni-plexus-archiver-unarchiver.patch
Patch1:         hawtjni-pom.patch
Patch2:         hawtjni-ac-prereq.patch
Patch3:         hawtjni-asm.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: %{name}-example-native = %{epoch}:%{version}-%{release}
Requires: jpackage-utils
Requires: autoconf
Requires: automake
Requires: libtool
Requires: maven2-plugin-eclipse
Requires: maven2-plugin-idea
Requires: maven2-plugin-shade
Requires: objectweb-asm
Requires: plexus-io
Requires: fusesource-pom
BuildRequires: apache-commons-parent
%if %with example
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
%endif
BuildRequires: maven2-plugin-eclipse
BuildRequires: maven2-plugin-idea
BuildRequires: maven2-plugin-shade
BuildRequires: maven-surefire-provider-junit4
BuildRequires: objectweb-asm
BuildRequires: plexus-io
BuildRequires: fusesource-pom
Source44: import.info
Patch33: hawtjni-pom-alt.patch

%description
A JNI code generator based on the JNI generator used by the eclipse SWT
project.

%package example-%{arch_name}
Summary:        Native jar for %{name}
Group:          Development/Documentation
Provides:       %{name}-example-native = %{epoch}:%{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}

%description example-%{arch_name}
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%if 0
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q
%patch0 -p0 -b .sav0
%if %without example
%patch1 -p0 -b .sav1
%endif
%patch2 -p0 -b .sav2
%patch3 -p0 -b .sav3
%patch33 -p1 -b .sav33

cp -p %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml

mkdir -p external_repo
ln -s %{_javadir} external_repo/JPP

%build
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
export M2_SETTINGS=$(pwd)/settings.xml
%{_bindir}/mvn-jpp \
        -e \
        -s $M2_SETTINGS \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -DaltDeploymentRepository=oss-releases::default::file://$(pwd)/maven2-brew \
	-Daggregate=true \
        deploy \
        javadoc:javadoc \
%if 0
        javadoc:aggregate \
        site
%endif

%install

mkdir -p %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_datadir}/maven2/poms

%if %with example
cp -p maven2-brew/org/fusesource/hawtjni/hawtjni-example/%{version}/hawtjni-example-%{version}-linux*.jar %{buildroot}%{_javadir}/
cp maven2-brew/org/fusesource/hawtjni/hawtjni-example/%{version}/hawtjni-example-%{version}-native-src.zip %{buildroot}%{_javadir}/
cp maven2-brew/org/fusesource/hawtjni/hawtjni-example/%{version}/hawtjni-example-%{version}.jar %{buildroot}%{_javadir}/
cp maven2-brew/org/fusesource/hawtjni/hawtjni-example/%{version}/hawtjni-example-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-example.pom
%add_to_maven_depmap org.fusesource.hawtjni hawtjni-example %{version} JPP %{name}-example
%endif

cp -p maven2-brew/org/fusesource/hawtjni/hawtjni-generator/%{version}/hawtjni-generator-%{version}.jar %{buildroot}%{_javadir}/
cp -p maven2-brew/org/fusesource/hawtjni/hawtjni-generator/%{version}/hawtjni-generator-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-generator.pom
%add_to_maven_depmap org.fusesource.hawtjni hawtjni-generator %{version} JPP %{name}-generator

cp -p maven2-brew/org/fusesource/hawtjni/hawtjni-pom/%{version}/hawtjni-pom-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-pom.pom
%add_to_maven_depmap org.fusesource.hawtjni hawtjni-pom %{version} JPP %{name}-pom

cp -p maven2-brew/org/fusesource/hawtjni/hawtjni-runtime/%{version}/hawtjni-runtime-%{version}.jar %{buildroot}%{_javadir}/
cp -p maven2-brew/org/fusesource/hawtjni/hawtjni-runtime/%{version}/hawtjni-runtime-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-runtime.pom
%add_to_maven_depmap org.fusesource.hawtjni hawtjni-runtime %{version} JPP %{name}-runtime

cp -p maven2-brew/org/fusesource/hawtjni/maven-hawtjni-plugin/%{version}/maven-hawtjni-plugin-%{version}.jar %{buildroot}%{_javadir}/
cp -p maven2-brew/org/fusesource/hawtjni/maven-hawtjni-plugin/%{version}/maven-hawtjni-plugin-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-maven-hawtjni-plugin.pom
%add_to_maven_depmap org.fusesource.hawtjni maven-hawtjni-plugin %{version} JPP maven-hawtjni-plugin

(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} ${jar/-%{version}/}; done)

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if 0
# manual
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr target/site/* %{buildroot}%{_docdir}/%{name}-%{version}
rm -r %{buildroot}%{_docdir}/%{name}-%{version}/apidocs
%endif

%if %with repolib
%{__mkdir_p} %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%{__cp} -pr maven2-brew/* %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%endif

%files
%if %with example
%{_javadir}*/hawtjni-example-%{version}-native-src.zip
%{_javadir}*/hawtjni-example-native-src.zip
%{_javadir}*/hawtjni-example-%{version}.jar
%{_javadir}*/hawtjni-example.jar
%endif
%{_javadir}*/maven-hawtjni-plugin-1.1.jar
%{_javadir}*/maven-hawtjni-plugin.jar
%{_javadir}*/%{name}-generator-%{version}.jar
%{_javadir}*/%{name}-generator.jar
%{_javadir}*/%{name}-runtime-%{version}.jar
%{_javadir}*/%{name}-runtime.jar
%if %with example
%{_datadir}/maven2/poms/JPP-%{name}-example.pom
%endif
%{_datadir}/maven2/poms/JPP-%{name}-generator.pom
%{_datadir}/maven2/poms/JPP-%{name}-pom.pom
%{_datadir}/maven2/poms/JPP-%{name}-runtime.pom
%{_datadir}/maven2/poms/JPP-maven-hawtjni-plugin.pom
%{_mavendepmapfragdir}/%{name}

%if %with example
%files example-%{arch_name}
%{_javadir}*/hawtjni-example-%{version}-linux*.jar
%{_javadir}*/hawtjni-example-linux*.jar
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if 0
%files manual
%doc %{_docdir}/%{name}-%{version}
%endif

%if %with repolib
%files repolib
%dir %{_javadir}*/
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_4jpp6
- fixed build:
  + changed objectweb-asm version in hawtjni-asm.patch to 3.3.1
  + added hawtjni-pom-alt.patch to fix shading

* Fri Feb 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_4jpp6
- new version

