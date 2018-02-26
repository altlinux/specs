BuildRequires: mojo-parent
BuildRequires: mojo-maven2-plugin-jdepend velocity14
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
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

#def_with bootstrap
%bcond_with bootstrap
#def_with gcj_support
%bcond_with gcj_support
%bcond_without maven
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

%define base_name  logging
%define short_name commons-%{base_name}

Name:           apache-%{short_name}
Version:        1.1.1
Release:        alt3_6jpp6
Epoch:          0
Summary:        Apache Commons Logging Package
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/logging/
Source0:        %{short_name}-%{version}-src.tar.gz
#wget http://www.apache.org/dist/jakarta/commons/logging/source/commons-logging-1.1.1-src.tar.gz
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-component-info.xml
Source4:        %{short_name}-api-%{version}.pom

Patch0:         apache-commons-logging-pom.patch
Patch1:         apache-commons-logging-build.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: fonts-ttf-liberation
BuildRequires: ant >= 0:1.7
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
BuildRequires: maven2-default-skin
BuildRequires: mojo-maven2-plugin-build-helper
BuildRequires: mojo-maven2-plugin-rat
%endif
%if %without bootstrap
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: excalibur-avalon-logkit
BuildRequires: excalibur-avalon-framework
%endif
BuildRequires: log4j
BuildRequires: servlet_2_5_api
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{epoch}:%{version}-%{release}
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name} < %{epoch}:%{version}-%{release}

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires: servlet_2_5_api
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif
Source44: import.info
Source45: apache-commons-logging-1.1.1.jar-OSGi-MANIFEST.MF

%description
The commons-logging package provides a simple, component oriented
interface (org.apache.commons.logging.Log) together with wrappers for
logging systems. The user can choose at runtime which system they want
to use. In addition, a small number of basic implementations are
provided to allow users to use the package standalone. 
commons-logging was heavily influenced by Avalon's Logkit and Log4J. The
commons-logging abstraction is meant to minimixe the differences between
the two, and to allow a developer to not tie himself to a particular
logging implementation.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java
Provides:       jakarta-%{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-repolib < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-repolib < %{epoch}:%{version}-%{release}

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description    javadoc
%{summary}.

%if %with maven
%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
Provides:       jakarta-%{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-manual < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-manual < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description    manual
%{summary}.
%endif

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -b .sav0
%patch1 -b .sav1

cp -p %{SOURCE1} settings.xml

%{__perl} -pi -e 's/\r$//g' LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

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
cat > build.properties <<EOBM
junit.jar=$(build-classpath junit)
log4j.jar=$(build-classpath log4j)
log4j12.jar=$(build-classpath log4j)
%if %without bootstrap
logkit.jar=$(build-classpath excalibur/avalon-logkit)
avalon-framework.jar=$(build-classpath excalibur/avalon-framework)
%endif
servletapi.jar=$(build-classpath servlet_2_5_api)
EOBM

%if %without bootstrap
%if %with maven
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
export MAVEN_OPTS="-Dmaven2.jpp.mode=true -Dmaven2.jpp.depmap.file=%{SOURCE2} -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -Dmaven.test.failure.ignore=true -Dproject.build.directory=target"
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        install javadoc:javadoc site

%else

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
        -Djunit.jar=$(build-classpath junit) \
        -Dlogkit.jar=$(build-classpath excalibur/avalon-logkit) \
        -Davalon-framework.jar=$(build-classpath excalibur/avalon-framework) \
        -Dservletapi.jar=$(build-classpath servlet_2_5_api) \
        compile.tests javadoc

%endif
## FIXME: There are failures with gcj. Ignore them for now.
%if %{gcj_support}
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dtest.failonerror=false \
        -Djunit.jar=$(build-classpath junit) \
        -Dlogkit.jar=$(build-classpath excalibur/avalon-logkit) \
        -Davalon-framework.jar=$(build-classpath excalibur/avalon-framework) \
        -Dservletapi.jar=$(build-classpath servlet_2_5_api) \
    test
%endif
%else
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 compile-only javadoc
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 target/%{short_name}-%{version}.jar \
                $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 target/%{short_name}-api-%{version}.jar \
                $RPM_BUILD_ROOT%{_javadir}/%{name}-api-%{version}.jar
install -m 644 target/%{short_name}-adapters-%{version}.jar \
                $RPM_BUILD_ROOT%{_javadir}/%{name}-adapters-%{version}.jar

%add_to_maven_depmap %{short_name} %{short_name} %{version} JPP %{short_name}
%add_to_maven_depmap %{short_name} %{short_name}-api %{version} JPP %{short_name}-api
%add_to_maven_depmap %{short_name} %{short_name}-adapters %{version} JPP %{short_name}-adapters
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}.jar
ln -s %{name}-api-%{version}.jar %{buildroot}%{_javadir}/%{name}-api.jar
ln -s %{name}-api-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-api-%{version}.jar
ln -s %{name}-api-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-api.jar
ln -s %{name}-api-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-api-%{version}.jar
ln -s %{name}-api-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-api.jar
ln -s %{name}-adapters-%{version}.jar %{buildroot}%{_javadir}/%{name}-adapters.jar
ln -s %{name}-adapters-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-adapters-%{version}.jar
ln -s %{name}-adapters-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-adapters.jar
ln -s %{name}-adapters-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-adapters-%{version}.jar
ln -s %{name}-adapters-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-adapters.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{short_name}.pom
install -m 644 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{short_name}-api.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %without bootstrap
%if %with maven
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rm -rf target/site/apidocs
%else
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
%else
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}-%{version}

%if %without bootstrap
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p *.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p *.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %with maven
# manual
cp -pr target/site $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif
%endif

%if %with repolib
%{__install} -d -m 0755 %{buildroot}%{repodir}
%{__install} -d -m 0755 %{buildroot}%{repodirlib}
%{__install} -p -m 0644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml

%{__sed} -i 's/project name=""/project name="%{name}"/g' %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 0755 %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE2} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{short_name}.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

# inject OSGi manifest apache-commons-logging-1.1.1.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE45} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/commons-logging.jar META-INF/MANIFEST.MF
# end inject OSGi manifest apache-commons-logging-1.1.1.jar-OSGi-MANIFEST.MF

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%config(noreplace) %{_mavendepmapfragdir}/*
%dir %{_docdir}/%{name}-%{version}
%{_docdir}/%{name}-%{version}/*.txt
%{_docdir}/%{name}-%{version}/*.html
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/*

%if %without bootstrap
%if %with maven
%files manual
%doc %{_docdir}/%{name}-%{version}/site
%endif
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt3_6jpp6
- fixed build

* Sun Feb 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_6jpp6
- synced osgi manifest

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_6jpp6
- new version

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_2jpp6
- new version

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_8jpp5
- updated OSGi manifest

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_7jpp5
- rebuild with osgi provides

* Mon May 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_4jpp1.7
- updated to new jpackage release

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_3jpp1.7
- added eclipse manifest

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_3jpp1.7
- updated to new jpackage release

* Fri Nov 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_2jpp1.7
- updated to new jpackage release

* Fri Apr 27 2007 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt4
- added JPackage compatibility stuff

* Sun Aug 29 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt3
- Disabled check by default due to a circular build dependency

* Thu Jul 15 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt2
- Disabled avalon by default

* Thu Jun 17 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt1
- New upstream release
- Patch0 obsoleted

* Thu Feb 26 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.3-alt1
- Adapted for Sisyphus from the JPackage project
