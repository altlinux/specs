AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
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
#def_with gcj_support
%bcond_with gcj_support
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/apache-%{base_name}/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirres %{repodir}/resources
%define repodirsrc %{repodir}/src

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define base_name httpclient
%define short_name commons-%{base_name}

Name:           apache-commons-httpclient
Version:        3.1
Release:        alt5_6jpp6
Epoch:          1
Summary:        Apache Commons HTTPClient Package
License:        ASL 2.0
Source0:        http://www.apache.org/dist/httpcomponents/commons-httpclient/source/commons-httpclient-3.1-src.tar.gz
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-component-info.xml
Source4:        commons-httpclient-3.1-pom.xml
URL:            http://commons.apache.org/httpclient/
Group:          Development/Java
%if ! %{gcj_support}
Buildarch:      noarch
%endif

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: java-javadoc
BuildRequires: fonts-ttf-liberation
BuildRequires: ant >= 0:1.7
BuildRequires: ant-junit
BuildRequires: junit
%if %with maven
BuildRequires: apache-commons-parent >= 0:12
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-report-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-idea
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-default-skin
BuildRequires: maven-jxr
BuildRequires: mojo-maven2-plugin-jdepend
BuildRequires: mojo-maven2-plugin-taglist
%endif
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-logging-javadoc

Requires: apache-commons-codec
Requires: apache-commons-logging

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0

Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name} < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-httpclient = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-httpclient < %{epoch}:%{version}-%{release}
Provides:       jakarta-commons-httpclient3 = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-commons-httpclient3 < %{epoch}:%{version}-%{release}
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif
Source44: import.info
Source45: jakarta-commons-httpclient-3.1.jar-OSGi-MANIFEST.MF

%description
The Hyper-Text Transfer Protocol (HTTP) is perhaps the most significant
protocol used on the Internet today. Web services, network-enabled
appliances and the growth of network computing continue to expand the
role of the HTTP protocol beyond user-driven web browsers, and increase
the number of applications that may require HTTP support.
Although the java.net package provides basic support for accessing
resources via HTTP, it doesn't provide the full flexibility or
functionality needed by many applications. The Jakarta Commons HTTP
Client component seeks to fill this void by providing an efficient,
up-to-date, and feature-rich package implementing the client side of the
most recent HTTP standards and recommendations.
Designed for extension while providing robust support for the base HTTP
protocol, the HTTP Client component may be of interest to anyone
building HTTP-aware client applications such as web browsers, web
service clients, or systems that leverage or extend the HTTP protocol
for distributed communication.

%if %with repolib
%package repolib
Summary:	 Artifacts to be uploaded to a repository library
Group:	         Development/Java
Provides:       %{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-repolib < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-repolib < %{epoch}:%{version}-%{release}

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       %{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%package demo
Summary:        Demos for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides:       %{short_name}-demo = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-demo < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name}-demo = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-demo < %{epoch}:%{version}-%{release}

%description demo
%{summary}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Documentation
Requires: %{name}-javadoc = %{epoch}:%{version}-%{release}
Provides:       %{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-manual < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-manual < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n commons-httpclient-%{version}
mkdir lib # duh
rm -rf docs/apidocs docs/*.patch docs/*.orig docs/*.rej

# Use javax classes, not com.sun ones
# assume no filename contains spaces
pushd src
    for j in $(find . -name "*.java" -exec grep -l 'com\.sun\.net\.ssl' {} \;); do
        sed -e 's|com\.sun\.net\.ssl|javax.net.ssl|' $j > tempf
        cp tempf $j
    done
    rm tempf
popd

%if %with repolib
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{SOURCE3}
%endif
cp %{SOURCE4} pom.xml

%if %with maven
cp -p %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP
%endif

%build
export LANG=en_US.ISO8859-1
%if %with maven
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
export MAVEN_OPTS="-Dmaven2.jpp.mode=true -Dmaven2.jpp.depmap.file=%{SOURCE2} -Dmaven.repo.local=${MAVEN_REPO_LOCAL}"
%if 0
mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
-Dmaven.test.skip=true \
        -e \
        -s $(pwd)/settings.xml \
        one:convert
%else
cp %{SOURCE4} pom.xml
%endif
mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
-Dmaven.test.skip=true \
        -e \
        -s $(pwd)/settings.xml \
        install javadoc:javadoc site
%else

export CLASSPATH=$(build-classpath jsse jce commons-codec commons-logging junit)
export OPT_JAR_LIST="ant/ant-junit junit"
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dbuild.sysclasspath=first \
  -Djavadoc.j2sdk.link=%{_javadocdir}/java \
  -Djavadoc.logging.link=%{_javadocdir}/commons-logging \
  dist \
%if 0
test
%endif
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
%if %with maven
install -m 644 target/%{short_name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%else
install -m 644 dist/%{short_name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%endif
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}.jar

# compat symlink
pushd $RPM_BUILD_ROOT%{_javadir}
ln -s commons-httpclient.jar commons-httpclient3.jar
popd

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-commons-httpclient.pom
%add_to_maven_depmap commons-httpclient commons-httpclient %{version} JPP commons-httpclient

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %with maven
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rm -rf target/site/apidocs
%else
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rm -rf dist/docs/api
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}-%{version}

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr src/examples src/contrib $RPM_BUILD_ROOT%{_datadir}/%{name}

# manual and docs
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %with maven
cp -pr target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%else
cp -pr dist/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif
ln -s %{_javadocdir}/%{name} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/apidocs

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__install} -m 0644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml

%{__sed} -i 's/project name=""/project name="%{name}"/g' %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
#%{__install} -m 0644 %{PATCH0} %{buildroot}%{repodirsrc}/
%{__install} -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}/
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{short_name}.jar
%endif

# inject OSGi manifest jakarta-commons-httpclient-3.1.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE45} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/commons-httpclient.jar META-INF/MANIFEST.MF
# end inject OSGi manifest jakarta-commons-httpclient-3.1.jar-OSGi-MANIFEST.MF

%files
%doc LICENSE.txt README.txt RELEASE_NOTES.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif

%files javadoc
%{_javadocdir}/*

%files demo
%{_datadir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%if %with repolib
%files repolib
%{repodir}
%endif

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt5_6jpp6
- fixed build with java 7

* Fri Jul 22 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt4_6jpp6
- disabled tests thank to new hasher

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt3_6jpp6
- renamed to apache-commons-httpclient

* Sun Jan 09 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt3_1jpp6
- added OSGi manifest

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt2_1jpp6
- jpackage 6.0

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt2_1jpp6
- new version

* Mon Jan 12 2009 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt2_0.3jpp5
- updated OSGi manifest

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt1.1_0jpp5
- rebuild with osgi provides

* Thu Dec 06 2007 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt2.2_1jpp1.7
- added eclipse manifest

* Thu Aug 02 2007 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Fri May 04 2007 Igor Vlasenko <viy@altlinux.ru> 3.0-alt2
- added jpackage compat symlinks

* Tue Dec 20 2005 Vladimir Lettiev <crux@altlinux.ru> 3.0-alt1
- Final release 3.0

* Sat Jul 02 2005 Vladimir Lettiev <crux@altlinux.ru> 3.0-alt0.3
- 3.0-rc3
- manual package is back
- changed rpmgroup for packages with documentation

* Tue Mar 22 2005 Vladimir Lettiev <crux@altlinux.ru> 3.0-alt0.2
- rpm-build-java macroces
- 3.0-beta1 (cvs 20050321)

* Sun Oct 24 2004 Vladimir Lettiev <crux@altlinux.ru> 3.0-alt0.1
- 3.0-dev (cvs 20041024)

* Wed Oct 13 2004 Vladimir Lettiev <crux@altlinux.ru> 2.0.1-alt2
- changes to suit ALT java-policy

* Fri Sep 17 2004 Vladimir Lettiev <crux@altlinux.ru> 2.0.1-alt1
- 2.0.1
- Rebuild for ALT Linux Sisyphus
- spec cleanup

