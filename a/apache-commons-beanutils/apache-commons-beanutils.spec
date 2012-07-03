BuildRequires: /proc
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

%bcond_without maven
%bcond_without repolib

%define gcj_support 0

%define repodir %{_javadir}/repository.jboss.com/apache-%{base_name}/%{version}clean-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define base_name beanutils
%define short_name commons-beanutils

Name:           apache-commons-beanutils
Version:        1.8.3
Release:        alt3_4jpp6
Epoch:          0
Summary:        Apache Commons BeanUtils Package
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/%{base_name}/
Source0:        http://www.apache.org/dist/commons/beanutils/source/commons-beanutils-1.8.3-src.tar.gz
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-component-info.xml
Source4:        commons-beanutils-bean-collections-1.8.3.pom
Source5:        commons-beanutils-core-1.8.3.pom

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7
BuildRequires: ant-junit
BuildRequires: junit
%if %with maven
BuildRequires: apache-commons-parent >= 0:12
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-idea
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
%endif
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-collections-testframework
BuildRequires: jakarta-commons-logging
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires: apache-commons-collections
Requires: jakarta-commons-logging
Obsoletes:      %{short_name} < %{epoch}:%{version}-%{release}
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Source44: import.info

%description
The scope of this package is to create a package of Java utility methods
for accessing and modifying the properties of arbitrary JavaBeans.  No
dependencies outside of the JDK are required, so the use of this package
is very lightweight.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java
Obsoletes:      %{short_name}-repolib < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-repolib < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name}-repolib = %{epoch}:%{version}-%{release}

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Obsoletes:      %{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%if %with maven
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
Obsoletes:      %{short_name}-manual < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-manual < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name}-manual = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description manual
%{summary}.
%endif

%prep
%setup -q -n %{short_name}-%{version}-src
cp -p %{SOURCE1} settings.xml

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
mkdir -p ${MAVEN_REPO_LOCAL}
export MAVEN_OPTS="-Dmaven2.jpp.mode=true -Dmaven2.jpp.depmap.file=%{SOURCE2} -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -Dproject.build.directory=$(pwd)/target"
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
	-Dmaven.test.skip=true \
	-s $(pwd)/settings.xml \
        install javadoc:javadoc
%else

export CLASSPATH=$(build-classpath commons-collections commons-logging)
export OPT_JAR_LIST="ant/ant-junit junit"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first test dist
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
%if %with maven
install -m 644 target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 target/%{short_name}-bean-collections-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-bean-collections-%{version}.jar
install -m 644 target/%{short_name}-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-core-%{version}.jar
%else
install -m 644 dist/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 dist/%{short_name}-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-core-%{version}.jar
install -m 644 dist/%{short_name}-bean-collections-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-bean-collections-%{version}.jar
%endif
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}.jar
ln -s %{name}-core-%{version}.jar %{buildroot}%{_javadir}/%{name}-core.jar
ln -s %{name}-core-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-core-%{version}.jar
ln -s %{name}-core-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-core.jar
ln -s %{name}-core-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-core-%{version}.jar
ln -s %{name}-core-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-core.jar
ln -s %{name}-bean-collections-%{version}.jar %{buildroot}%{_javadir}/%{name}-bean-collections.jar
ln -s %{name}-bean-collections-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-bean-collections-%{version}.jar
ln -s %{name}-bean-collections-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-bean-collections.jar
ln -s %{name}-bean-collections-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-bean-collections-%{version}.jar
ln -s %{name}-bean-collections-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-bean-collections.jar

%add_to_maven_depmap %{short_name} %{short_name} %{version} JPP %{short_name}
%add_to_maven_depmap org.apache.commons %{short_name} %{version} JPP %{short_name}
%add_to_maven_depmap %{short_name} %{short_name}-core %{version} JPP %{short_name}-core
%add_to_maven_depmap org.apache.commons %{short_name}-core %{version} JPP %{short_name}-core
%add_to_maven_depmap %{short_name} %{short_name}-bean-collections %{version} JPP %{short_name}-bean-collections
%add_to_maven_depmap org.apache.commons %{short_name}-bean-collections %{version} JPP %{short_name}-bean-collections

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{short_name}.pom
install -pm 644 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{short_name}-bean-collections.pom
install -pm 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{short_name}-core.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %with maven
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
# FIXME: (dwalluck): This breaks rpmbuild -bi --short-circuit
rm -rf target/site/apidocs
%else
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/jakarta-%{short_name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/jakarta-%{short_name}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %with maven
cp -pr target/site $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif
%{__ln_s} %{name}-%{version} %{buildroot}%{_docdir}/jakarta-%{short_name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}clean-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml

%{__sed} -i 's/project name=""/project name="%{name}"/g' %{buildroot}%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/commons-beanutils.jar $RPM_BUILD_ROOT%{repodirlib}
%endif

%files
%doc *.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/*
%{_javadocdir}/

%if %with maven
%files manual
%{_docdir}/*
%endif

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_4jpp6
- fixed build

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt2_4jpp6
- fixed repolib

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt1_4jpp6
- new version

