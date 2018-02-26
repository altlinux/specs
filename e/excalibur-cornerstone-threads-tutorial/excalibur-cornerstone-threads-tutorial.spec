Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2005, JPackage Project
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

%define grname		excalibur
%define usname		cornerstone-threads-tutorial

Name:		excalibur-cornerstone-threads-tutorial
Version:	2.1
Release:	alt4_2jpp5
Epoch:		0
Summary:	Cornerstone Threads Tutorial
License:	Apache Software License 2.0
Url:		http://excalibur.apache.org/
Group:		Development/Java
Source0:	http://www.apache.org/dist/excalibur/cornerstone-threads/source/cornerstone-threads-tutorial-2.1-src.tar.gz
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        excalibur-cornerstone-threads-tutorial-2.1-jpp-depmap.xml
Source5:        excalibur-cornerstone-threads-project-common.xml
Source6:        excalibur-buildsystem.tar.gz
Source7:        excalibur-cornerstone-project-common.xml
Patch0:         excalibur-cornerstone-threads-tutorial-2.1-project_xml.patch
BuildRequires: maven1-plugins >= 0:1.1
BuildRequires: junit
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: saxon
BuildRequires: saxon-scripts
BuildRequires: excalibur-avalon-framework-api
BuildRequires: excalibur-avalon-framework-impl
BuildRequires: excalibur-cornerstone-threads-api
BuildRequires: excalibur-thread-api

Requires: excalibur-avalon-framework-api
Requires: excalibur-avalon-framework-impl
Requires: excalibur-cornerstone-threads-api
Requires: excalibur-thread-api
BuildArch:	noarch

%description
The Cornerstone Threads Tutorial.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description manual
%{summary}.

%prep
%setup -q -n %{usname}-%{version}
# remove all binary libs
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
	mv $j $j.no
done
cp %{SOURCE5} project-common.xml
gzip -dc %{SOURCE6} | tar xf -
mkdir cornerstone
cp %{SOURCE7} cornerstone/project-common.xml
mv src/main src/java

%patch0 -b .sav

%build
export DEPCAT=$(pwd)/excalibur-cornerstone-threads-tutorial-2.1-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > excalibur-cornerstone-threads-tutorial-2.1-depmap.new.xml
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

#rm -rf .maven/repository/JPP/jars
#mkdir -p .maven/repository/JPP/jars
#build-jar-repository -s -p .maven/repository/JPP/jars \
#excalibur/avalon-framework-api \
#excalibur/avalon-framework-impl \
#excalibur/cornerstone-threads-api \
#excalibur/excalibur-thread-api \


export MAVEN_HOME_LOCAL=$(pwd)/.maven

maven -Dmaven.compile.target=1.5 -Dmaven.compile.source=1.5 -Dmaven.javadoc.source=1.5  \
	-Dmaven.repo.remote=file:/usr/share/maven1/repository \
	-Dmaven.home.local=$MAVEN_HOME_LOCAL \
	jar javadoc


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{grname}
install -m 644 \
target/%{usname}-%{version}.jar \
$RPM_BUILD_ROOT%{_javadir}/%{grname}/%{usname}-%{version}.jar

# create unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir}/%{grname} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/docs/apidocs/* \
	$RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}


%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi


%files 
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{grname}/*.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt4_2jpp5
- fixed build with java 7

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt3_2jpp5
- fixed build with moved maven1

* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_2jpp5
- use maven1-plugins

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_2jpp5
- fixed repocop warnings

* Fri Jul 20 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

