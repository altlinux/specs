Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
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

%bcond_with     bootstrap
%bcond_with     maven

%define gcj_support 0

%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define version_full %{version}.0.jboss

%define repodir %{_javadir}/repository.jboss.com/apache-logging/%{version_full}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define base_name  logging
%define short_name commons-%{base_name}

Name:           jakarta-%{short_name}-jboss
Version:        1.1
Release:        alt2_4jpp5
Epoch:          0
Summary:        Jakarta Commons Logging Package
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/%{base_name}/
# cvs -d:pserver:anonymous@anoncvs.forge.jboss.com:/cvsroot/jboss export -r JBoss_Apache_Common_Logging_1_1_0 apache/commons-logging 
# (cd apache && tar cjf ../commons-logging-1.1-src.tar.gz commons-logging)
Source0:        %{short_name}-%{version}-src.tar.gz
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        %{short_name}-%{version}-jpp-depmap.xml
Source5:        %{short_name}-%{version}.pom
Source6:        %{short_name}-api-%{version}.pom
Source7:        %{short_name}-component-info.xml

Patch0:         %{short_name}-%{version}-build_xml.patch
BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: ant >= 0:1.6
%if %with maven
BuildRequires: maven-plugins >= 0:1.1
BuildRequires: maven-plugins-base
BuildRequires: maven-plugin-jdepend
BuildRequires: maven-plugin-jxr
BuildRequires: maven-plugin-license
BuildRequires: maven-plugin-linkcheck
BuildRequires: maven-plugin-xdoc
BuildRequires: saxon
BuildRequires: saxon-scripts
%endif
%if %without bootstrap
BuildRequires: ant-junit
BuildRequires: junit
%if 0
BuildRequires: excalibur-avalon-logkit
BuildRequires: excalibur-avalon-framework
%endif
%endif
BuildRequires: log4j
BuildRequires: servletapi4
BuildRequires: zip
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif

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

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.

%if %with maven
%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description    manual
%{summary}.
%endif

%if %{with_repolib}
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

# -----------------------------------------------------------------------------

%prep
%setup -q -n %{short_name}
%patch0 -b .sav
perl -pi -e 's/\r$//g' LICENSE.txt RELEASE-NOTES.txt
mkdir -p META-INF
cp -p LICENSE.txt NOTICE.txt META-INF

# -----------------------------------------------------------------------------

%build
cat > build.properties <<EOBM
junit.jar=$(build-classpath junit)
log4j.jar=$(build-classpath log4j)
log4j12.jar=$(build-classpath log4j)
%if %without bootstrap
# XXX: (dwalluck): This is built without avalon support upstream
%if 0
logkit.jar=$(build-classpath excalibur/avalon-logkit)
avalon-framework.jar=$(build-classpath excalibur/avalon-framework)
%endif
%endif
servletapi.jar=$(build-classpath servletapi4)
EOBM
#  <property name="junit.jar"               value="junit-3.8.1.jar"/>
#  <property name="log4j12.jar"             value="log4j-1.2.12.jar"/>
#  <property name="log4j13.jar"             value="log4j-1.3.0.jar"/>
#  <property name="logkit.jar"              value="logkit-1.0.1.jar"/>
#  <property name="avalon-framework.jar"    value="avalon-framework-4.1.3.jar"/>
#  <property name="servletapi.jar"          value="servletapi-2.3.jar"/>

%if %without bootstrap
%if %with maven
export DEPCAT=$(pwd)/commons-logging-1.1-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > commons-logging-1.1-depmap.new.xml

for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

mkdir -p .maven/repository/JPP/plugins/
pushd .maven/repository/JPP/plugins/
ln -sf /usr/share/maven/plugins/maven-xdoc-plugin-*.jar maven-xdoc-plugin.jar
popd

export MAVEN_HOME_LOCAL=$(pwd)/.maven
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=$MAVEN_HOME_LOCAL \
        jar:install javadoc:generate xdoc:transform

%else
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
        -Djunit.jar=$(build-classpath junit) \
%if 0
        -Dlogkit.jar=$(build-classpath excalibur/avalon-logkit) \
        -Davalon-framework.jar=$(build-classpath excalibur/avalon-framework) \
%endif
        -Dservletapi.jar=$(build-classpath servletapi4) \
        compile.tests javadoc
%endif
## FIXME: There are failures with gcj. Ignore them for now.
%if %{gcj_support}
  ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dtest.failonerror=false \
        -Djunit.jar=$(build-classpath junit) \
%if 0
        -Dlogkit.jar=$(build-classpath excalibur/avalon-logkit) \
        -Davalon-framework.jar=$(build-classpath excalibur/avalon-framework) \
%endif
        -Dservletapi.jar=$(build-classpath servletapi4) \
    test
%else
  ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
        -Djunit.jar=$(build-classpath junit) \
%if 0
        -Dlogkit.jar=$(build-classpath excalibur/avalon-logkit) \
        -Davalon-framework.jar=$(build-classpath excalibur/avalon-framework) \
%endif
        -Dservletapi.jar=$(build-classpath servletapi4) \
    test
%endif
%else
        ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 compile-only javadoc
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -p -m 644 target/%{short_name}-%{version}.jar \
                $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -p -m 644 target/%{short_name}-api-%{version}.jar \
                $RPM_BUILD_ROOT%{_javadir}/%{name}-api-%{version}.jar
install -p -m 644 target/%{short_name}-adapters-%{version}.jar \
                $RPM_BUILD_ROOT%{_javadir}/%{name}-adapters-%{version}.jar
%add_to_maven_depmap %{short_name} %{short_name}-jboss %{version} JPP %{short_name}-jboss
%add_to_maven_depmap %{short_name} %{short_name}-jboss-api %{version} JPP %{short_name}-jboss-api
%add_to_maven_depmap %{short_name} %{short_name}-jbiss-adapters %{version} JPP %{short_name}-jboss-adapters
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|jakarta-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{short_name}-jboss.pom
install -pm 644 %{SOURCE6} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{short_name}-jboss-api.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %without bootstrap
%if %with maven
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rm -rf target/docs/apidocs
%else
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
%else
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %without bootstrap
%if %with maven
# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
cp -pr target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
%endif
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %{with_repolib}
        install -d -m 755 $RPM_BUILD_ROOT%{repodir}
        install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
        install -p -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{repodir}/component-info.xml
        tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
        sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
        sed -i "s/@VERSION@/%{version_full}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
        install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
        install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
        install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
        cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/commons-logging.jar
        pushd src/java
        zip -qr $RPM_BUILD_ROOT%{repodirlib}/commons-logging-src.zip *
        popd
        zip -qur $RPM_BUILD_ROOT%{repodirlib}/commons-logging-src.zip META-INF
%endif

%post
%update_maven_depmap
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%postun
%update_maven_depmap
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%doc LICENSE.txt PROPOSAL.html RELEASE-NOTES.txt README-jboss.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-adapters-%{version}.jar
%{_javadir}/%{name}-adapters.jar
%{_javadir}/%{name}-api-%{version}.jar
%{_javadir}/%{name}-api.jar
%{_javadir}/%{short_name}-jboss-%{version}.jar
%{_javadir}/%{short_name}-jboss.jar
%{_javadir}/%{short_name}-jboss-adapters-%{version}.jar
%{_javadir}/%{short_name}-jboss-adapters.jar
%{_javadir}/%{short_name}-jboss-api-%{version}.jar
%{_javadir}/%{short_name}-jboss-api.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %without bootstrap
%if %with maven
%files manual
%doc %{_docdir}/%{name}-%{version}/site
%endif
%endif

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_4jpp5
- fixed build with moved maven1

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_4jpp5
- converted from JPackage by jppimport script

