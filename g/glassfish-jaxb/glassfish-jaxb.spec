BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/sun-jaxb/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define apiver 2.1
%define jaxbver %{apiver}.9

Name:           glassfish-jaxb
Version:        2.1.9
Release:	alt3_7jpp6
Epoch:          0
Summary:        Java API for XML Web Services API
License:        CDDL/GPLv2
Group:          Development/Java
URL:            https://jax-ws-sources.dev.java.net/
# cvs -Q -d:pserver:guest@cvs.dev.java.net:/cvs export -r jaxb-2_1_9 -d glassfish-jaxb-2.1.9 jaxb2-sources/jaxb-ri && tar cjf glassfish-jaxb-2.1.9-src.tar.bz2 glassfish-jaxb-2.1.9
Source0:        glassfish-jaxb-2.1.9-src.tar.bz2
Source2:        %{name}-component-info.xml
Source3:        com-sun-xml-bind-component-info.xml
Patch0:         glassfish-2.1.9-no-22.patch
Provides:       jaxb_api = 0:%{jaxbver}
Provides:       jaxb_2_1_api = 0:%{version}-%{release}
%if 0
Requires: jaf = 1.1
Requires: stax_1_0_api
%endif
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
%if 0
BuildRequires: jaf = 1.1
BuildRequires: stax_1_0_api
%endif
BuildArch:      noarch
Source44: import.info

%description
The Java Architecture for XML Binding (JAXB) 2.1 API
according to JSR-222 MR1.

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
Provides:       jaxb-javadoc = 0:%{jaxbver}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
/bin/echo FIXME: bundled jars
%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t /bin/echo
%patch0 -p1

%{__perl} -p -i -e 's/\@API_VERSION\@/%{apiver}/;' tools/poms/jaxb-api.pom
%{__perl} -p -i -e 's/\@VERSION\@/%{version}/;' -e 's/\@API_VERSION\@/%{apiver}/;' tools/poms/jaxb-impl.pom
%{__perl} -p -i -e 's/\@VERSION\@/%{version}/;' tools/poms/jaxb1-impl.pom
%{__perl} -p -i -e 's/\@VERSION\@/%{version}/g;' tools/poms/jaxb-xjc.pom

mv CDDL+GPLv2.txt CDDL+GPLv2.txt.orig
%{_bindir}/iconv -f iso8859-1 -t utf8 -o CDDL+GPLv2.txt CDDL+GPLv2.txt.orig

%build
export CLASSPATH=`pwd`/tools/lib/rebundle/runtime/xsdlib.jar
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first dist
export CLASSPATH=${CLASSPATH}:apgen/build/classes:runtime/build/classes:runtime-deprecated/build/classes:runtime-fi/build/classes:runtime-staxex/build/classes:tools/jing-rnc-driver/build/classes:tools/pretty-printer/build/classes:tools/taglets/build/classes:tools/xmllint/build/classes:xjc/build/classes
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first architecture-document

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
#install -m 644 dist/lib/jaxb-api.jar $RPM_BUILD_ROOT%{_javadir}/jaxb-api.jar
/bin/touch $RPM_BUILD_ROOT%{_javadir}/jaxb-api.jar
#install -m 644 dist/lib/jaxb-api.jar $RPM_BUILD_ROOT%{_javadir}/jaxb_2_1_api.jar
/bin/touch $RPM_BUILD_ROOT%{_javadir}/jaxb_2_1_api.jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -p -m 644 dist/lib/jaxb-api.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 644 dist/lib/jaxb-impl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 644 dist/lib/jaxb1-impl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 644 dist/lib/jaxb-xjc.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/

# Commenting the bellow to fix 4.3 build
%if 0
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 jaxb.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

%add_to_maven_depmap javax.xml.bind jaxb-api %{version} JPP %{name}

(cd $RPM_BUILD_ROOT%{_javadir} 
ln -s %{name}-%{version}-api.jar jaxb_2_1_api.jar
ln -s %{name}-%{version}-api.jar jaxb_api.jar
ln -sf %{name}-%{version}-api.jar %{name}.jar)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom
%endif

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version} || :
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%add_to_maven_depmap javax.xml.bind jaxb-api %{version} JPP/%{name} jaxb-api
%{__install} -p -m 644 tools/poms/jaxb-api.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}.jaxb-api.pom
%add_to_maven_depmap com.sun.xml.bind jaxb-impl %{version} JPP/%{name} jaxb-impl
%{__install} -p -m 644 tools/poms/jaxb-impl.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}.jaxb-impl.pom
%add_to_maven_depmap com.sun.xml.bind jaxb1-impl %{version} JPP/%{name} jaxb1-impl
%{__install} -p -m 644 tools/poms/jaxb1-impl.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}.jaxb1-impl.pom
%add_to_maven_depmap com.sun.xml.bind jaxb-xjc %{version} JPP/%{name} jaxb-xjc
%{__install} -p -m 644 tools/poms/jaxb-xjc.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}.jaxb-xjc.pom

%if %with repolib
%{__install} -d -m 755 %{buildroot}%{repodir}
%{__install} -d -m 755 %{buildroot}%{repodirlib}
%{__install} -p -m 644 %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml

%{__sed} -i 's/project name=""/project name="%{name}"/g' %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 755 %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p dist/lib/jaxb-api.jar %{buildroot}%{repodirlib}/jaxb-api.jar
%{__cp} -p dist/lib/jaxb-impl.jar %{buildroot}%{repodirlib}/jaxb-impl.jar
%{__cp} -p dist/lib/jaxb-xjc.jar %{buildroot}%{repodirlib}/jaxb-xjc.jar
%define repodir %{_javadir}/repository.jboss.com/com/sun/xml/bind/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src
%{__install} -d -m 755 %{buildroot}%{repodir}
%{__install} -d -m 755 %{buildroot}%{repodirlib}
%{__install} -p -m 644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 755 %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p dist/lib/jaxb-xjc.jar %{buildroot}%{repodirlib}/jaxb-xjc.jar
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxb_2_1_api_glassfish-jaxb<<EOF
%{_javadir}/jaxb_2_1_api.jar	%{_javadir}/%{name}/jaxb-api.jar	20100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxb_api_glassfish-jaxb<<EOF
%{_javadir}/jaxb_api.jar	%{_javadir}/%{name}/jaxb-api.jar	20100
EOF

%files
%_altdir/jaxb_api_glassfish-jaxb
%_altdir/jaxb_2_1_api_glassfish-jaxb
%doc CDDL+GPLv2.html CDDL+GPLv2.txt HOWTO-build.txt
%{_javadir}/%{name}
%exclude %{_javadir}/jaxb_2_1_api.jar
%exclude %{_javadir}/jaxb-api.jar
%{_datadir}/maven2/poms/JPP.%{name}.jaxb-api.pom
%{_datadir}/maven2/poms/JPP.%{name}.jaxb-impl.pom
%{_datadir}/maven2/poms/JPP.%{name}.jaxb1-impl.pom
%{_datadir}/maven2/poms/JPP.%{name}.jaxb-xjc.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.9-alt3_7jpp6
- built with java 6

* Fri Feb 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.9-alt2_7jpp6
- removed compat symlink

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.9-alt1_7jpp6
- new version

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.4-alt1_7jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.4-alt1_6jpp5
- converted from JPackage by jppimport script

