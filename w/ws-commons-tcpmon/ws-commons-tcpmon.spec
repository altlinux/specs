Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /usr/bin/dos2unix
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2007, JPackage Project
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

# If you don't want to build with maven
# give rpmbuild option '--without maven'

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}


Summary:        Tcpmon WS Utility
URL:            http://ws.apache.org/commons/tcpmon
Source0:        ws-commons-tcpmon-1.0.tar.gz
# svn export http://svn.apache.org/repos/asf/webservices/commons/tags/tcpmon/1_0/tcpmon/ ws-commons-tcpmon-1.0
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        ws-commons-tcpmon-1.0-jpp-depmap.xml
Source5:        ws-commons-tcpmon-build.xml
Patch0:         ws-commons-tcpmon-1.0-project_xml.patch
Patch1:         ws-commons-tcpmon-script.patch

Name:           ws-commons-tcpmon
Version:        1.0
Release:        alt6_1jpp5
Epoch:          0
License:        Apache Software License 2
Group:          Development/Java
BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: ant >= 0:1.6
BuildRequires: junit
%if %{with_maven}
BuildRequires: maven1 >= 0:1.1
BuildRequires: maven1-plugins-base
BuildRequires: maven1-plugin-license
BuildRequires: maven1-plugin-test
BuildRequires: maven1-plugin-xdoc
BuildRequires: saxon
BuildRequires: saxon-scripts
%endif
Requires: jpackage-utils >= 0:1.7.2
Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
TCPMon is a utility that allows the messages to be viewed 
and resent. It is very much useful as a debug tool. It has 
originally being part of Axis1 and now stands as an 
independent project.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%if %{with_maven}
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description manual
%{summary}.
%endif

%prep
%setup -q -n %{name}-%{version}
chmod -R go=u-w *
for j in $(find . -name "*.jar"); do
       mv $j $j.no
done
%patch0 -b .sav
%patch1 -b .sav
cp %{SOURCE5} build.xml

%if %{with_maven}
if [ ! -f %{SOURCE4} ]; then
export DEPCAT=$(pwd)/%{name}-%{version}-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > %{name}-%{version}-depmap.new.xml
fi
%endif

%build
%if %{with_maven}
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

export MAVEN_HOME_LOCAL=$(pwd)/.maven

maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
      -Dmaven.repo.remote=file:/usr/share/maven1/repository \
      -Dmaven.home.local=$MAVEN_HOME_LOCAL \
      jar:install javadoc:generate 
#      site
%else
export CLASSPATH=
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
%endif

%install

# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 0644 target/tcpmon-SNAPSHOT.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# bin
install -d -m 0755 $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 scripts/tcpmon.sh   $RPM_BUILD_ROOT%{_bindir}/%{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %{with_maven}
rm -rf target/docs/apidocs
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
#cp -pr target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
%endif

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete
dos2unix $RPM_BUILD_ROOT%_bindir/*

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -sf %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%dir %{_docdir}/%{name}-%{version}
%{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/*
%attr(0755,root,root) %{_bindir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

#if %{with_maven}
#%files manual
#%{_docdir}/%{name}-%{version}/site
#endif

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6_1jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_1jpp5
- use maven1

* Sat Dec 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_1jpp5
- fixed build; dropped manual due to jelly velocity tag problem

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_1jpp5
- fixed repocop warnings

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp5
- fixed build (dos2unix in bindir)

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

