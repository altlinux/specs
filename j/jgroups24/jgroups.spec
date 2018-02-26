%define oldname jgroups
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

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'

%define _without_tests 1
%define _with_repolib 0

%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/jgroups/2.4.1.SP4-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

# If you don't want to run the unit tests
# give rpmbuild option '--without tests'

%define with_tests %{!?_without_tests:1}%{?_without_tests:0}
%define without_tests %{?_without_tests:1}%{!?_without_tests:0}



Name:           jgroups24
Version:        2.4.1
Release:        alt3_1.SP4.1jpp5
Epoch:          1
Summary:        Toolkit for reliable multicast communication
License:        LGPLv2+
URL:            http://www.jgroups.org/
Group:          Development/Java
# cvs -d:pserver:anonymous@javagroups.cvs.sourceforge.net:/cvsroot/javagroups login
# cvs -z3 -d:pserver:anonymous@javagroups.cvs.sourceforge.net:/cvsroot/javagroups export -r JGroups_2_4_1_SP4 JGroups
# mv JGroups JGroups-2.4.1-sp4.src
# tar czf JGroups-2.4.1-sp4-src.tgz JGroups-2.4.1-sp4.src
Source0:        JGroups-2.4.1-sp4-src.tgz
Patch0:         jgroups-2.3-build_xml.patch
Source1:	jgroups-component-info.xml
Patch1: jgroups-2.3-build_xml-alt-quickhack.patch 

# To use JGroups one needs:
# commons-logging.jar
Requires: jakarta-commons-logging
# concurrent.jar
Requires: concurrent
# log4j.jar
Requires: log4j
# To run JGroups you need to have an XML parser installed on your system.
# If you use JDK 1.4 or higher, you can use the parser that is shipped with it.
Requires: jaxp_parser_impl
# If you want to use the JGroups JMS protocol ( org.jgroups.protocols.JMS ),
# then you will also need to place jms.jar somewhere in your CLASSPATH. 
Requires: jms
# Place the JAR files somewhere in your CLASSPATH , and you're ready to start
# using JGroups.

# FIXME Do we need bsh at run-time?
Requires: bsh
#Optional:       mx4j

BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit
BuildRequires: ant-trax
BuildRequires: bsh
BuildRequires: concurrent
BuildRequires: jakarta-commons-logging
BuildRequires: jaxp_parser_impl
BuildRequires: jms
BuildRequires: junit
BuildRequires: log4j
BuildRequires: mx4j
BuildRequires: xalan-j2
BuildArch:      noarch

BuildRequires: xalan-j2
BuildRequires: xalan-j2

%description
JGroups is a toolkit for reliable multicast communication. (Note that
this doesn't necessarily mean IP Multicast, JGroups can also use
transports such as TCP). It can be used to create groups of processes
whose members can send messages to each other. The main features include

    * Group creation and deletion. Group members can be spread across
      LANs or WANs
    * Joining and leaving of groups
    * Membership detection and notification about joined/left/crashed members
    * Detection and removal of crashed members
    * Sending and receiving of member-to-group messages (point-to-multipoint)
    * Sending and receiving of member-to-member messages (point-to-point)

To use JGroups one needs:
 commons-logging.jar
 concurrent.jar
 log4j.jar

To run JGroups you need to have an XML parser installed on your system.
If you use JDK 1.4 or higher, you can use the parser that is shipped with it.

If you want to use the JGroups JMS protocol ( org.jgroups.protocols.JMS ),
then you will also need to place jms.jar somewhere in your CLASSPATH. 

Place the JAR files somewhere in your CLASSPATH , and you're ready to start
using JGroups.

%if %{with_repolib}
%package repolib
Summary:	Artifacts to be uploaded to a repository library
Group:	        Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio
%endif

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description    manual
%{summary}.

%prep
%setup -q -n JGroups-2.4.1-sp4.src
find . -type f -name .cvsignore | xargs rm
for j in $(find . -name "*.jar"); do
    rm $j
done

# this test requires bouncycastle
rm tests/junit/org/jgroups/protocols/ENCRYPTAsymmetricTest.java

%patch0 -b .sav

%if %{with_repolib}
tag=`echo %{oldname}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{SOURCE1}
%endif

%patch1 -b .alt

%build
export CLASSPATH=
export OPT_JAR_LIST="ant-launcher ant/ant-junit ant/ant-trax junit xalan-j2 xalan-j2-serializer"
pushd lib
ln -sf $(build-classpath ant) .
ln -sf $(build-classpath ant-launcher) .
ln -sf $(build-classpath ant/ant-junit) .
#BUILD/JGroups-2.4.1.src/lib/bcprov-jdk14-117.jar.no
ln -sf $(build-classpath bsh) .
ln -sf $(build-classpath commons-logging) .
ln -sf $(build-classpath concurrent) .
ln -sf $(build-classpath jms) .
ln -sf $(build-classpath junit) .
ln -sf $(build-classpath log4j) .
ln -sf $(build-classpath mx4j/mx4j-jmx) .
ln -sf $(build-classpath xalan-j2) .
ln -sf $(build-classpath xalan-j2-serializer) .
popd
%if %{without_tests}
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadoc gossip-service jgroups-service
%else
#export ANT_OPTS="-Djava.net.preferIPv4Stack=true"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadoc gossip-service jgroups-service unittests testreport
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{oldname}-all.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 dist/%{oldname}-core.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-core-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

# javadoc
install -p -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
(cd $RPM_BUILD_ROOT%{_javadocdir} && ln -sf %{name}-%{version} %{name})

# services
install -p -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -m 644 dist/%{oldname}*.sar \
        $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

# docs
install -p -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{with_repolib}
	install -d -m 755 $RPM_BUILD_ROOT%{repodir}
	install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
	install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
	install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
	install -m 755 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
	install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
	cp -p $RPM_BUILD_ROOT%{_javadir}/jgroups24.jar $RPM_BUILD_ROOT%{repodirlib}/jgroups.jar
%endif

%files
%{_javadir}/*.jar
%{_datadir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%if %{with_repolib}
%files repolib
%{repodir}
%endif

%changelog
* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 1:2.4.1-alt3_1.SP4.1jpp5
- compat build

* Sat Sep 27 2008 Igor Vlasenko <viy@altlinux.ru> 1:2.4.1-alt2_1.SP4.1jpp5
- fixed build

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:2.4.1-alt1_1.SP4.1jpp5
- converted from JPackage by jppimport script

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2.9.2-alt1_3jpp1.7
- converted from JPackage by jppimport script

