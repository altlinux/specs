Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
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


Name:		monolog
Version:	2.0
Release:	alt2_3jpp5
Epoch:		0
Summary:	API for monitoring and logging
License:	LGPL
URL:		http://monolog.objectweb.org/
Group:		Development/Java
Source0:	monolog_%{version}_src.tar.gz
## cvs -d:pserver:anonymous@cvs.forge.objectweb.org:/cvsroot/monolog login
##  cvs -z3 -d:pserver:anonymous@cvs.forge.objectweb.org:/cvsroot/monolog export -r MONOLOG_1_9_2 monolog
Source1:	http://repo1.maven.org/maven2/org/objectweb/monolog/monolog/2.1.12/monolog-2.1.12.pom
Patch0:         monolog_2.0_build.patch

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: junit
BuildRequires: log4j
BuildRequires: mx4j
BuildRequires: objectweb-anttask
BuildRequires: p6spy
BuildRequires: velocity
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

BuildArch:      noarch
Patch33: monolog-java6.patch

%description
Monolog is an API of monitoring and logging.

%package	javadoc
Summary:	Javadoc for %{name}
Group:		Development/Documentation
BuildArch: noarch

%description	javadoc
Javadoc for %{name}.


%prep
%setup -q -n %{name}
find . -name "*.jar" -exec rm -f {} \;
%patch0 -b .sav0
# also build ow_util_io.jar (required by medor)
mv shared.old/src/io src/org/objectweb/util
mv shared.old/archive/ow_util_io.xml archive
%patch33 -p0

%build
export CLASSPATH=$(build-classpath junit log4j mx4j/mx4j objectweb-anttask p6spy velocity)
pushd externals
for jar in $(echo $CLASSPATH | sed 's/:/ /g'); do
ln -sf ${jar} .
done
popd
ant jar jdoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

rm -f output/dist/lib/ow_util_all*.jar
rm -f output/dist/lib/ow_util_ant*.jar
for jar in output/dist/lib/*.jar; do
install -m 644 ${jar} \
$RPM_BUILD_ROOT%{_javadir}/%{name}/`basename ${jar} .jar`-%{version}.jar
done

(cd $RPM_BUILD_ROOT%{_javadir}//%{name} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-ow_%{name}.pom
%add_to_maven_depmap org.objectweb.monolog %{name} %{version} JPP/%{name} ow_%{name}

# javadoc
install -p -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/dist/jdoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
(cd $RPM_BUILD_ROOT%{_javadocdir} && ln -sf %{name}-%{version} %{name})

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_3jpp5
- fixes for java6 support

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_3jpp5
- new jpp release

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_2jpp5
- fixed build w/java5

* Mon Jul 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

