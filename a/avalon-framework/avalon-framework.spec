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

%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/apache-avalon/4.1.5-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src
%define short_name      framework

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'

%define _without_maven 1

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}


Name:           avalon-framework
Version:        4.1.5
Release:        alt3_2jpp5
Epoch:          0
Summary:        Java components interfaces
License:        ASL 1.1
Url:            http://avalon.apache.org/%{short_name}/
Group:          Development/Java
#Vendor:                JPackage Project
#Distribution:  JPackage
Source0:        http://www.apache.org/dist/avalon/avalon-framework/v4.1.5/avalon-framework-4.1.5.src.tar.gz
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        avalon-framework-4.1.5-jpp-depmap.xml
Source5:        avalon-framework-component-info.xml
Source6:        %{name}-api-build.xml
Source7:        %{name}-impl-build.xml
Source8:        %{name}-site-build.xml

Patch0:         avalon-framework-4.1.5-site_project_properties.patch
Patch1:         avalon-framework-4.1.5-project_xml.patch
Patch2:         avalon-framework-4.1.5-maven_xml.patch
Patch3:         avalon-framework-4.1.5-disable-testbuild-tests.patch
Patch4:         avalon-framework-4.1.5-xalan-serializer.patch

%if %{with_maven}
BuildRequires: maven-plugins >= 1.0.2
BuildRequires: saxon-scripts
BuildRequires: maven-plugins-base
BuildRequires: maven-plugin-changes
BuildRequires: maven-plugin-license
BuildRequires: maven-plugin-jdepend
BuildRequires: maven-plugin-site
BuildRequires: maven-plugin-tasklist
BuildRequires: maven-plugin-test
BuildRequires: maven-plugin-xdoc
%else
BuildRequires: ant
%endif

BuildRequires: xerces-j2
BuildRequires: xalan-j2
BuildRequires: junit
BuildRequires: log4j
BuildRequires: avalon-logkit
BuildRequires: xml-commons-apis
BuildRequires: jpackage-utils >= 0:1.5
BuildRequires: sed

Requires: jpackage-utils >= 0:1.5
Requires: avalon-logkit
Requires: xml-commons-apis
Requires: xalan-j2
Requires: log4j
Requires(post): jpackage-utils >= 0:1.5
Requires(postun): jpackage-utils >= 0:1.5

BuildArch:      noarch

%description
The Avalon framework consists of interfaces that define relationships
between commonly used application components, best-of-practice pattern
enforcements, and several lightweight convenience implementations of the
generic components.
What that means is that we define the central interface Component. We
also define the relationship (contract) a component has with peers,
ancestors and children. This documentation introduces you to those
patterns, interfaces and relationships.

%if %{with_repolib}
%package         repolib
Summary:         Artifacts to be uploaded to a repository library
Group:  Development/Java

%description     repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio
%endif

%package manual
Summary:        Manual for %{name}
Group:          Development/Java

%description manual
Documentation for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav -p2
%patch4

tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{SOURCE5}

/bin/cp -f %{SOURCE6} api/build.xml
/bin/cp -f %{SOURCE7} impl/build.xml
/bin/cp -f %{SOURCE8} site/build.xml

%build

%if %{with_maven}
export DEPCAT=$(pwd)/avalon-framework-4.1.5-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > avalon-framework-4.1.5-depmap.new.xml
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

for p in $(find . -name project.properties); do
    echo >> $p
    echo maven.repo.remote=file:/usr/share/maven1/repository >> $p
    echo maven.home.local=$(pwd)/.maven >> $p
done

mkdir -p .maven/repository/maven/jars
build-jar-repository .maven/repository/maven/jars maven-jelly-tags

# For RHEl4, we don't have all plugins. Also, we don't want it 
# connecting to the net for things.

%if %{RHEL4}==1

# Remove checkstyle, developer-activity,file-activity and linkcheck 
# plugin requirements from the xdoc plugin for RHEL4.

pushd /usr/share/maven/plugins/ >& /dev/null
MAVEN_XDOC_PLUGIN=`ls -t maven-xdoc* | sed s/\.jar$//g`
popd >& /dev/null
 
pushd $(pwd)/.maven/ >& /dev/null
mkdir -p cache/$MAVEN_XDOC_PLUGIN
cd cache/$MAVEN_XDOC_PLUGIN
jar xf /usr/share/maven/plugins/$MAVEN_XDOC_PLUGIN.jar
sed -i -e 's@<attainGoal name="maven-checkstyle-plugin:register"/>@@g' plugin.jelly
sed -i -e 's@<attainGoal name="maven-developer-activity-plugin:register"/>@@g' plugin.jelly
sed -i -e 's@<attainGoal name="maven-file-activity-plugin:register"/>@@g' plugin.jelly
sed -i -e 's@<attainGoal name="maven-linkcheck-plugin:register"/>@@g' plugin.jelly
sed -i -e 's@<attainGoal name="maven-changelog-plugin:register"/>@@g' plugin.jelly
sed -i -e 's@<attainGoal name="maven-jxr-plugin:register"/>@@g' plugin.jelly
popd >& /dev/null

%endif

export MAVEN_HOME_LOCAL=$(pwd)/.maven
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=$MAVEN_HOME_LOCAL \
        avalon:build avalon:site

mkdir tmp
pushd tmp
jar xf ../target/%{name}-api-%{version}.jar
jar xf ../target/%{name}-impl-%{version}.jar
rm -rf META-INF
jar cf ../target/%{name}-all-%{version}.jar *
popd

%else

# Else build it with ant
pushd api
mkdir -p target/lib
build-jar-repository target/lib avalon-logkit
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dnoget=true dist
popd

pushd impl
mkdir -p target/lib
build-jar-repository target/lib xml-commons-apis xerces-j2 xalan-j2 xalan-j2-serializer log4j avalon-logkit junit
ln -s ../../../api/target/avalon-framework-api-%{version}.jar target/lib/
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dnoget=true dist
popd

pushd site
mkdir -p target/lib
build-jar-repository target/lib log4j avalon-logkit
ln -s ../../../api/target/avalon-framework-api-%{version}.jar target/lib/
ln -s ../../../impl/target/avalon-framework-impl-%{version}.jar target/lib/
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dnoget=true dist
popd

mkdir target

# Create the all jar
mkdir tmp
pushd tmp
jar xf ../api/target/%{name}-api-%{version}.jar
jar xf ../impl/target/%{name}-impl-%{version}.jar
rm -rf META-INF
jar cf ../target/%{name}-all-%{version}.jar *
popd

# Mimic structure from maven, so that %%install section stays the same
cp api/target/%{name}-api-%{version}.jar target/
cp impl/target/%{name}-impl-%{version}.jar target/

%endif


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{name}-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{name}-impl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{name}-all-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
# create unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)
# create compatibility symlink
(cd $RPM_BUILD_ROOT%{_javadir} && ln -sf %{name}-all.jar %{name}.jar)

%if %{with_maven}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr site/target/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
rm -rf site/target/docs/api

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr site/target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%else
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr site/dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# no manual
%endif

%if %{with_repolib}
        install -d -m 755 $RPM_BUILD_ROOT%{repodir}
        install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
        install -m 755 %{SOURCE5} $RPM_BUILD_ROOT%{repodir}/component-info.xml
        install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
        install -m 755 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
        install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
        install -m 755 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
        cp $RPM_BUILD_ROOT%{_javadir}/avalon-framework.jar $RPM_BUILD_ROOT%{repodirlib}
%endif

%files
%{_javadir}/*.jar
%if %{with_maven}
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%endif

%if %{with_maven}
%files manual
%doc %{_docdir}/%{name}-%{version}
%endif

%files javadoc
%{_javadocdir}/%{name}


%if %{with_repolib}
%files repolib
%{repodir}
%endif

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.1.5-alt3_2jpp5
- fixed build with moved maven1

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.1.5-alt2_2jpp5
- fixed build

* Sat Jan 24 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.1.5-alt1_2jpp5
- restored in separate package due to repolib

