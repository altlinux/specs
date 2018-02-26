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

%define gcj_support 0

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}


Name:           velocity-tools
Version:        1.4
Release:        alt4_2jpp6
Epoch:          0
Summary:        Velocity application building tools
License:        Apache Software License
URL:            http://velocity.apache.org/tools/releases/1.4/
Group:          Development/Java
Source0:         http://apache.speedbone.de/velocity/tools/1.4/velocity-tools-1.4-src.tar.gz
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        sslext-1.2-0.jar
Source4:        %{name}-site.xml


BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-digester
BuildRequires:  apache-commons-lang
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-validator
BuildRequires:  dom4j
BuildRequires:  jaxen >= 0:1.1
BuildRequires:  servlet_2_3_api
BuildRequires:  struts >= 0:1.3.8
BuildRequires:  struts-taglib >= 0:1.3.8
BuildRequires:  struts-tiles >= 0:1.3.8
# FIXME
#BuildRequires:  struts-sslext >= 0:1.2
BuildRequires:  velocity >= 0:1.4
BuildRequires:  velocity-dvsl
BuildRequires:  oro >= 0:2.0.8
%if %{with_maven}
BuildRequires:  maven2 >= 2.0.8
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-project-info-reports
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-site
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  mojo-maven2-plugin-taglist
BuildRequires:  maven2-default-skin
BuildRequires:  apache-commons-parent
BuildRequires:  fonts-ttf-liberation
%endif

Requires:  apache-commons-beanutils
Requires:  apache-commons-collections
Requires:  apache-commons-digester
Requires:  apache-commons-lang
Requires:  apache-commons-logging
Requires:  apache-commons-validator
Requires:  dom4j
Requires:  jaxen >= 0:1.1
Requires:  servlet_2_3_api
Requires:  struts >= 0:1.3.8
Requires:  struts-taglib >= 0:1.3.8
Requires:  struts-tiles >= 0:1.3.8
Requires:  velocity
Requires:  velocity-dvsl
Requires:  oro
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Source44: import.info

%description
VelocityTools is a collection of Velocity subprojects with a common
goal of creating tools and infrastructure for building both web and
non-web applications using the Velocity template engine.

%package        manual
Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description    manual
Documentation for %{name}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%package        demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n %{name}-%{version}-src
# Remove all binary libs used in compiling the package.
#FIXME Use struts-sslext package
find lib -name "*.jar" -and -not -name sslext-1.2.jar -print | xargs rm -f
cp %{SOURCE1} settings.xml
mkdir -p src/site
cp %{SOURCE4} src/site/site.xml


%if %{with_maven}
mkdir -p .m2/repository/JPP/
install -Dm644 %{SOURCE3} .m2/repository/sslext/sslext/1.2-0/sslext-1.2-0.jar
%else

mkdir -p lib
(cd lib
cp %{SOURCE3} .
ln -sf $(build-classpath commons-beanutils)
ln -sf $(build-classpath commons-collections)
ln -sf $(build-classpath commons-digester)
ln -sf $(build-classpath commons-lang)
ln -sf $(build-classpath commons-logging)
ln -sf $(build-classpath commons-validator)
ln -sf $(build-classpath dom4j)
ln -sf $(build-classpath jaxen)
ln -sf $(build-classpath oro)
ln -sf $(build-classpath servlet_2_3_api)
ln -sf $(build-classpath struts)
ln -sf $(build-classpath struts-taglib)
ln -sf $(build-classpath struts-tiles)
ln -sf $(build-classpath velocity)
ln -sf $(build-classpath velocity-dvsl)
)
%endif

%build
%if %{with_maven}
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.mode=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc 
#	site
%else
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dskip.jar.loading=true jar.struts jar.view jar.generic javadoc docs
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%if ! %{with_maven}
install -m 644 dist/%{name}-generic-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-generic-%{version}.jar
install -m 644 dist/%{name}-view-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-view-%{version}.jar
%endif
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %{with_maven}
#cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%else
cp -pr docs/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rm -rf docs/javadoc
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
cp LICENSE README.txt WHY_THREE_JARS.txt VLS_README.txt STATUS \
                  $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %{with_maven}
#cp -pr target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
%else
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
%endif

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr examples test $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE
%doc %{_docdir}/%{name}-%{version}/STATUS
%doc %{_docdir}/%{name}-%{version}/*.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

#files manual
#%doc %{_docdir}/%{name}-%{version}/site
# hack; explicitly added docdir if not owned
#%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}-%{version}

%changelog
* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt4_2jpp6
- fixed build with maven3

* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_2jpp6
- new jpp relase

* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_1jpp5
- removed velocity from requires (temporally, due to v15/16 conlict)

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_1jpp5
- build with velocity15

* Wed Apr 01 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp5
- new version

* Fri Feb 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp5
- fixed build

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp1.7
- updated to new jpackage release

* Fri Nov 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

