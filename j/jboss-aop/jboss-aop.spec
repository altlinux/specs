Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-core
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

%bcond_without          jdk15

%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/jboss/aop/1.5.6.GA-brew
%define repodirlib %{repodir}/lib
%define repodirres %{repodir}/resources
%define repodirsrc %{repodir}/src


Name:           jboss-aop
Version:        1.5.6
Release:        alt5_9jpp5
Epoch:          0
Summary:        JBoss AOP Framework
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn export https://svn.jboss.org/repos/jbossas/tags/JBoss_AOP_1_5_6_GA/
# mv JBoss_AOP_1_5_6_GA jboss-aop-1.5.6-src
# tar czf jboss-aop-1.5.6.GA-src.tgz jboss-aop-1.5.6-src
Source0:        jboss-aop-1.5.6.GA-src.tgz
Source1:        jboss-aop-component-info.xml
Source2:        %{name}-%{version}-apache-jaxme-component-info.xml
Source3:        %{name}-%{version}-apache-logging-component-info.xml
Patch0:         %{name}-%{version}-scripts.patch
Patch1:         %{name}-%{version}-disable-license-fetching.patch
Patch2:         %{name}-%{version}-antpath.patch
# general requires
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant17 >= 0:1.6.2
BuildRequires: ant17-nodeps >= 0:1.6.2
BuildRequires: buildmagic
%if %with jdk15
%else
%endif
BuildRequires: concurrent-repolib
BuildRequires: dom4j-repolib
BuildRequires: dtdparser-repolib
BuildRequires: gnu-trove-repolib
BuildRequires: jakarta-commons-codec-repolib
BuildRequires: jakarta-commons-httpclient-repolib
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-slide-webdavclient-repolib
BuildRequires: javassist-repolib
BuildRequires: jboss-profiler-jvmti-repolib
BuildRequires: junit-repolib
BuildRequires: log4j-repolib
BuildRequires: qdox-repolib
BuildRequires: quartz-repolib
BuildRequires: snmptrapappender-repolib
BuildRequires: ws-jaxme
BuildRequires: xalan-j2-repolib
BuildRequires: xdoclet-repolib
BuildRequires: xerces-j2-repolib
BuildRequires: xml-commons-repolib
Requires: gnu-trove
Requires: javassist >= 0:3.1
Requires: jboss-common
Requires: qdox >= 0:1.5
Obsoletes:      jboss-aop-framework < %{epoch}:%{version}-%{release}
Provides:       jboss-aop-framework = %{epoch}:%{version}-%{release}
BuildArch:      noarch
%add_findreq_skiplist /usr/share/%name/bin/*

%description
JBoss AOP is a 100%% Pure Java aspected oriented framework 
usuable in any programming environment or tightly integrated 
with our application server. Aspects allow you to more easily 
modularize your code base when regular object oriented 
programming just doesn't fit the bill. It can provide a 
cleaner separation from application logic and system code. 
It provides a great way to expose integration points into 
your software. Combined with JDK 1.5 Annotations, it also 
is a great way to expand the Java language in a clean 
pluggable way rather than using annotations solely for 
code generation. 

%if %{with_repolib}
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n jboss-aop-%{version}-src
%patch0 -p0 -b .sav
%patch1 -p0 -b .sav
%patch2 -p0 -b .sav

rm aop/docs/reference/.cvsignore

# FIXME: (dwalluck): jbossbuild needs to be symlinked
find -type f -name '*.jar' -a ! -name jbossbuild.jar | xargs -t rm

# Build thirdparty
mkdir thirdpartyrepo

# No need to guess this list when dependencies change. Just make it do 
# for item in javadir/repository.jboss..../* 
# and then do a build, see what ends up in thirdparty/
for item in apache-codec apache-httpclient apache-log4j apache-slide \
            apache-xalan apache-xerces apache-xml-commons dom4j javassist \
            jboss/profiler/jvmti junit oswego-concurrent qdox quartz \
            snmptrapappender trove wutka-dtdparser xdoclet; do

    target=thirdpartyrepo/
    if [ "`dirname $item`" != "." ]; then
        target=$target/`dirname $item`
    fi

    mkdir -p $target
    cp -pr %{_javadir}/repository.jboss.com/$item $target

done

# Synchronize versions. We want to use the versions on the system -- update b-t.xml for it
for dir in `find thirdpartyrepo -type d -name lib`; do
    depversion=`basename \`dirname $dir\``
    depname=`echo $dir | sed -e s:thirdpartyrepo/::g -e s:/$depversion/lib::g`
    sed -i -e s:"<componentref name=\"$depname\" version=\".*\"/>":"<componentref name=\"$depname\" version=\"$depversion\"/>":g build/build-thirdparty.xml
done

# Whatever we don't have a repolib for, we manually copy over for now

# JaxMe
mkdir -p thirdpartyrepo/apache-jaxme/0.2-cvs/lib
ln -sf $(build-classpath jaxme/jaxmexs) thirdpartyrepo/apache-jaxme/0.2-cvs/lib/
cp -p %{SOURCE2} thirdpartyrepo/apache-jaxme/0.2-cvs/component-info.xml

# commons-logging
mkdir -p thirdpartyrepo/apache-logging/1.0.5.GA-jboss/lib
ln -sf $(build-classpath jakarta-commons-logging) thirdpartyrepo/apache-logging/1.0.5.GA-jboss/lib/commons-logging.jar
cp -p %{SOURCE3} thirdpartyrepo/apache-logging/1.0.5.GA-jboss/component-info.xml

#export CLASSPATH=$(build-classpath buildmagic)
export OPT_JAR_LIST=:
sed -i 's,fail unless="buildmagic.ant.compatible",fail if="never",' tools/etc/buildmagic/buildmagic.ent

ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -f build/build.xml -Djbossbuild.repository=file://`pwd`/thirdpartyrepo createthirdparty

%build
BUILD_ID=`date -u +%Y%m%d%H%M`_%{version}-%{release}

export CLASSPATH=$(build-classpath buildmagic jboss-common-core)
export OPT_JAR_LIST="ant17/ant17-nodeps"

ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -f build/build.xml -Dant.version="`%{_bindir}/ant -version`" -Djrockit.home=${JROCKITHOME} all

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

# install aop framework
install -p -m 644 aop/output/lib/jboss-aop.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-aop-%{version}.jar
install -p -m 644 aop/output/lib/jdk14-pluggable-instrumentor.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jdk14-pluggable-instrumentor-%{version}.jar
[ -f aop/output/lib/jrockit-pluggable-instrumentor.jar ] && install -p -m 644 aop/output/lib/jrockit-pluggable-instrumentor.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jrockit-pluggable-instrumentor-%{version}.jar
%if %with jdk15
install -p -m 644 aop/output/lib/jboss-aop-jdk50.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-aop-jdk50-%{version}.jar
install -p -m 644 aop/output/lib/pluggable-instrumentor.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/pluggable-instrumentor-%{version}.jar
install -p -m 644 aop/output/lib/jboss-aop-jdk50-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-aop-jdk50-client-%{version}.jar
%endif

# create all versionless symlinks
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# bin
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
for i in aop/src/resources/bin/*.sh; do
    install -p -m 755 $i $RPM_BUILD_ROOT%{_bindir}/%{name}-`basename $i .sh`
done

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr aop/output/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}
cp -pr aop/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}
install -m 644 aop/RELEASE_NOTES.txt $RPM_BUILD_ROOT%{_docdir}/%{name}

%if %{with_repolib}
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}.GA-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
cp -p $RPM_BUILD_ROOT%{_javadir}/jboss-aop/jboss-aop.jar $RPM_BUILD_ROOT%{repodirlib}
cp -p $RPM_BUILD_ROOT%{_javadir}/jboss-aop/jdk14-pluggable-instrumentor.jar $RPM_BUILD_ROOT%{repodirlib}
[ -f $RPM_BUILD_ROOT%{_javadir}/jboss-aop/jrockit-pluggable-instrumentor.jar ] && cp -p $RPM_BUILD_ROOT%{_javadir}/jboss-aop/jrockit-pluggable-instrumentor.jar $RPM_BUILD_ROOT%{repodirlib} || sed -i -e 's/.*jrockit.*$//g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
%if %with jdk15
cp -p $RPM_BUILD_ROOT%{_javadir}/jboss-aop/jboss-aop-jdk50.jar $RPM_BUILD_ROOT%{repodirlib}
cp -p $RPM_BUILD_ROOT%{_javadir}/jboss-aop/jboss-aop-jdk50-client.jar $RPM_BUILD_ROOT%{repodirlib}
cp -p $RPM_BUILD_ROOT%{_javadir}/jboss-aop/pluggable-instrumentor.jar $RPM_BUILD_ROOT%{repodirlib}
%endif
%endif

%files
%attr(0755,root,root) %{_bindir}/%{name}-annotationc
%attr(0755,root,root) %{_bindir}/%{name}-aopc
%attr(0755,root,root) %{_bindir}/%{name}-aopc15
%attr(0755,root,root) %{_bindir}/%{name}-create-pluggable-jboss-classloader
%attr(0755,root,root) %{_bindir}/%{name}-run-load-boot
%attr(0755,root,root) %{_bindir}/%{name}-run-load-system
%attr(0755,root,root) %{_bindir}/%{name}-run-load15
%attr(0755,root,root) %{_bindir}/%{name}-run-load15HotSwap
%attr(0755,root,root) %{_bindir}/%{name}-run-precompiled
%attr(0755,root,root) %{_bindir}/%{name}-run-precompiled15
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/jboss-aop-%{version}.jar
%{_javadir}/%{name}/jboss-aop.jar
%{_javadir}/%{name}/*pluggable-instrumentor-%{version}.jar
%{_javadir}/%{name}/*pluggable-instrumentor.jar
%if %with jdk15
%{_javadir}/%{name}/jboss-aop-jdk50-%{version}.jar
%{_javadir}/%{name}/jboss-aop-jdk50-client-%{version}.jar
%{_javadir}/%{name}/jboss-aop-jdk50-client.jar
%{_javadir}/%{name}/jboss-aop-jdk50.jar
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.6-alt5_9jpp5
- build with ant17

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.6-alt4_9jpp5
- fixed components-info

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.6-alt3_9jpp5
- fixed build

* Thu Sep 16 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.6-alt2_9jpp5
- ant 1.8 support

* Fri Jun 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.6-alt1_9jpp5
- new version

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.6-alt2_1jpp5
- fixed build w/java5

* Tue Dec 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.6-alt2_1jpp1.7
- added hack around req.shell dependencies

* Thu Nov 01 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.6-alt1_1jpp1.7
- converted from JPackage by jppimport script

