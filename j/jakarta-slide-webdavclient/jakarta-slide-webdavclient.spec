BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 2.1
%define name jakarta-slide-webdavclient
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

%bcond_without integration
%bcond_without repolib

%global namedversion %{version}

%global repodir %{_javadir}/repository.jboss.com/apache-slide/%{namedversion}-brew
%global repodirlib %{repodir}/lib
%global repodirsrc %{repodir}/src

%global base_name slide


Name:           jakarta-%{base_name}-webdavclient
Version:        2.1
Release:        alt8_16jpp6
Epoch:          0
Summary:        Slide WebDAV client
Group:          Development/Java
License:        ASL 2.0
URL:            http://jakarta.apache.org/slide/
Source0:        jakarta-slide-webdavclient-src-2.1.tar.gz
Source1:        jakarta-slide-webdavclient.sh
Source2:        jakarta-slide-webdavclient-2.2-WebdavResource.java
Source3:        jakarta-slide-webdavclient-component-info.xml
Source4:        http://mirrors.ibiblio.org/pub/mirrors/maven2/slide/slide-webdavlib/2.1/slide-webdavlib-2.1.pom
# FIXME Temporary fix !!!
Patch0:         jakarta-slide-webdavclient-3.0-compat.patch
Patch1:         jakarta-slide-webdavclient-build-jdk15.patch
Patch2:         jakarta-slide-webdavclient-jdk15.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       commons-httpclient
Requires:       commons-transaction11
Requires:       jdom
Requires:       jpackage-utils
Requires:       jca_1_5_api
Requires:       jta_1_1_api
Requires:       servlet_api
Requires:       xml-im-exporter
BuildRequires:  ant
BuildRequires:  ant-antlr
BuildRequires:  antlr
BuildRequires:  commons-httpclient >= 3.0
BuildRequires:  commons-transaction11
BuildRequires:  jpackage-utils
BuildRequires:  jta_1_1_api
BuildRequires:  jca_1_5_api
BuildRequires:  servlet_api
BuildRequires:  jdom
BuildRequires:  xml-im-exporter
%if %with repolib
BuildRequires:  maven2
BuildRequires:  maven2-plugin-deploy
%endif
BuildArch:      noarch
Source44: import.info

%description
Slide includes a fully featured WebDAV client library and command line
client.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n jakarta-slide-webdavclient-src-%{namedversion}
%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1
%patch2 -p0 -b .sav2

%{__cp} -p %{SOURCE2} clientlib/src/java/org/apache/webdav/lib/WebdavResource.java

%build
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/antlr`
export CLASSPATH=`%{_bindir}/build-classpath antlr commons-httpclient commons-transaction11 jca_1_5_api jta_1_1_api servlet_2_5_api jdom xml-im-exporter`
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first

%install

%{__mkdir_p} %{buildroot}%{_javadir}/%{base_name}

%{__cp} -p dist/lib/jakarta-slide-webdavlib-%{namedversion}.jar %{buildroot}%{_javadir}/%{base_name}/%{name}-webdavlib-%{namedversion}.jar
%{__ln_s} %{name}-webdavlib-%{namedversion}.jar %{buildroot}%{_javadir}/%{base_name}/jakarta-%{base_name}-webdavlib-%{namedversion}.jar

%{__cp} -p dist/lib/jakarta-slide-commandline-%{namedversion}.jar %{buildroot}%{_javadir}/%{base_name}/%{name}-commandline-%{namedversion}.jar
%{__ln_s} %{name}-commandline-%{namedversion}.jar %{buildroot}%{_javadir}/%{base_name}/jakarta-%{base_name}-commandline-%{namedversion}.jar

(cd %{buildroot}%{_javadir}/%{base_name} && for jar in *-%{namedversion}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{namedversion}||g"`; done)
(cd %{buildroot}%{_javadir}/%{base_name} && for jar in jakarta-*.jar; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|jakarta-||g"`; done)
(cd %{buildroot}%{_javadir}/%{base_name} && for jar in jakarta-slide-*.jar; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|jakarta-slide-||g"`; done)

%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -p %{SOURCE1} %{buildroot}%{_bindir}/webdavclient

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
%{__cp} -pr dist/doc/clientjavadoc/* %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
%{__ln_s} %{name}-%{namedversion} %{buildroot}%{_javadocdir}/%{name}

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE4} %{buildroot}%{_datadir}/maven2/poms/JPP.%{base_name}-%{name}-webdavlib.pom
%add_to_maven_depmap slide %{base_name}-webdavlib %{namedversion} JPP/%{base_name} %{base_name}-webdavlib
%add_to_maven_depmap slide webdavlib %{namedversion} JPP/%{base_name} webdavlib

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE2} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP.%{base_name}-%{name}-webdavlib.pom %{buildroot}%{repodirlib}/jakarta-slide-webdavlib.pom
%{__cp} -p %{buildroot}%{_javadir}/%{base_name}/%{name}-webdavlib-%{namedversion}.jar %{buildroot}%{repodirlib}/jakarta-slide-webdavlib.jar
%endif

%if %with repolib
# %{_bindir}/mvn-jpp deploy:deploy-file \
#     -Dfile=%{buildroot}%{_javadir}/%{base_name}/jakarta-slide-webdavlib-%{namedversion}.jar \
#     -Durl=file:%{buildroot}%{_javadir}/repository.jboss.com/maven2-brew \
#     -DgroupId=apache-slide \
#     -DartifactId=jakarta-slide-webdavlib \
#     -Dversion=%{namedversion} \
#     -Dpackaging=jar

mvn-jpp install:install-file \
    -Dfile=%{buildroot}%{_javadir}/%{base_name}/jakarta-slide-webdavlib-%{namedversion}.jar \
    -DlocalRepositoryPath=%{buildroot}%{_javadir}/repository.jboss.com/maven2-brew \
    -DgroupId=apache-slide \
    -DartifactId=jakarta-slide-webdavlib \
    -Dversion=%{namedversion} \
    -Dpackaging=jar
%endif

%files
%doc LICENSE
%attr(0755,root,root) %{_bindir}/webdavclient
%dir %{_javadir}*/%{base_name}
%{_javadir}*/%{base_name}/%{name}-webdavlib-%{namedversion}.jar
%{_javadir}*/%{base_name}/%{name}-webdavlib.jar
%{_javadir}*/%{base_name}/%{base_name}-webdavlib-%{namedversion}.jar
%{_javadir}*/%{base_name}/%{base_name}-webdavlib.jar
%{_javadir}*/%{base_name}/jakarta-%{base_name}-webdavlib-%{namedversion}.jar
%{_javadir}*/%{base_name}/jakarta-%{base_name}-webdavlib.jar
%{_javadir}*/%{base_name}/webdavlib-%{namedversion}.jar
%{_javadir}*/%{base_name}/webdavlib.jar
%{_javadir}*/%{base_name}/%{name}-commandline-%{namedversion}.jar
%{_javadir}*/%{base_name}/%{name}-commandline.jar
%{_javadir}*/%{base_name}/%{base_name}-commandline-%{namedversion}.jar
%{_javadir}*/%{base_name}/%{base_name}-commandline.jar
%{_javadir}*/%{base_name}/jakarta-%{base_name}-commandline-%{namedversion}.jar
%{_javadir}*/%{base_name}/jakarta-%{base_name}-commandline.jar
%{_javadir}*/%{base_name}/commandline-%{namedversion}.jar
%{_javadir}*/%{base_name}/commandline.jar
%{_javadir}*/%{base_name}/%{base_name}-webdavclient-commandline-%{namedversion}.jar
%{_javadir}*/%{base_name}/%{base_name}-webdavclient-commandline.jar
%{_javadir}*/%{base_name}/webdavclient-commandline-%{namedversion}.jar
%{_javadir}*/%{base_name}/webdavclient-commandline.jar
%{_javadir}*/%{base_name}/%{base_name}-webdavclient-webdavlib-%{namedversion}.jar
%{_javadir}*/%{base_name}/%{base_name}-webdavclient-webdavlib.jar
%{_javadir}*/%{base_name}/webdavclient-webdavlib-%{namedversion}.jar
%{_javadir}*/%{base_name}/webdavclient-webdavlib.jar
%{_datadir}/maven2/poms/JPP.%{base_name}-%{name}-webdavlib.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}*
%exclude %dir %{_javadocdir}
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt8_16jpp6
- fixed build with maven3

* Wed Jan 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt7_16jpp6
- fixed repolib jar

* Wed Jan 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt6_16jpp6
- restored repolib

* Tue Jan 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt5_16jpp6
- restored repolib

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt4_16jpp6
- new jpp relase

* Tue Feb 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt4_13jpp6
- build with commons-transaction11

* Wed Oct 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt4_10jpp6
- fixed repolib version

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt3_10jpp6
- jpp6 update

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt3_8jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_8jpp5
- converted from JPackage by jppimport script

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_4jpp1.7
- added pom file and maven maps

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_4jpp1.7
- converted from JPackage by jppimport script

