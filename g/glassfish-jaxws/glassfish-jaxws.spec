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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

# FIXME: this option is not finished
#def_with bundled
%bcond_with bundled
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/sun-jaxws/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

# FIXME: This should be 2.1 (2.1.3 is the impl version)
%define apiver 2.1.3
%define jaxbver 2.1.9

# FIXME: (dwalluck): This package has many bundled jars

Name:           glassfish-jaxws
Version:        2.1.3
Release:        alt2_8jpp6
Epoch:          0
Summary:        Java API for XML Web Services API
License:        CDDL 1.0/GPLv2
Group:          Development/Java
URL:            https://jax-ws-sources.dev.java.net/
# cvs -z3 -Q -d:pserver:guest@cvs.dev.java.net:/cvs export -D20071218 -d glassfish-jaxws-2.1.3 jax-ws-sources/jaxws-ri && tar cjf glassfish-jaxws-2.1.3-src.tar.bz2 glassfish-jaxws-2.1.3
Source0:        glassfish-jaxws-2.1.3-src.tar.bz2
Source1:	%{name}-component-info.xml
Patch0:         glassfish-jaxws-pom.patch
Patch1:         glassfish-jaxws-no-findbugs.patch
Provides:       jaxws_api = 0:2.1
Provides:       jaxws_2_1_api = 0:%{version}-%{release}
Requires(post): jpackage-utils
Requires(post): alternatives >= 0:0.4
Requires(postun): jpackage-utils
Requires(preun): alternatives >= 0:0.4
Requires: jpackage-utils
%if %without bundled
Requires: glassfish-jaxb
Requires: sun-saaj-1.3-impl
Requires: sun-xmlstreambuffer
Requires: wstx
Requires: sun-mimepull
# FIXME: This is added in place of annotation_1_0_api
Requires: jboss-ejb-3.0-api
Requires: jaf_1_1_api
Requires: jaxb_2_1_api
Requires: stax_1_0_api
Requires: stax-ex
Requires: sun-fi
Requires: saaj_1_3_api
Requires: servlet_2_5_api
Requires: sun-sjsxp
Requires: sun-ws-metadata-2.0-api
%if 0
# FIXME: this doesn't work, using sun-ws-metadata-2.0-api instead
Requires: ws_metadata_2_0_api
%endif
Requires: xml-commons-resolver11
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: ant-nodeps
BuildRequires: ant-trax
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: jaf_1_1_api
BuildRequires: sun-fi >= 0:1.2.2
BuildRequires: jaxb_2_1_api
BuildRequires: glassfish-jaxb >= 0:%{jaxbver}
##BuildRequires:  glassfish-jaxws >= 0:2.1.3
# jsr173_api (or bea-stax-api)
BuildRequires: codehaus-stax11-api
# jsr181-api (or geronimo-ws-metadata-2.0-api)
BuildRequires: sun-ws-metadata-2.0-api
# jsr250-api (or {geronimo,sun}-annotation-1.0-api)
BuildRequires: jboss-ejb-3.0-api
# FIXME: Need upgrade to 1.3
BuildRequires: sun-mimepull >= 0:1.2
%if 1
BuildRequires: saaj_1_3_api
# FIXME: wants 1.3.3
BuildRequires: sun-saaj-1.3-impl >= 0:1.3.1
%endif
BuildRequires: sun-sjsxp >= 0:1.0
BuildRequires: stax-ex >= 0:1.2
BuildRequires: sun-xmlstreambuffer >= 0:0.7
BuildRequires: wstx >= 0:3.2.1
BuildRequires: servlet_2_5_api
BuildRequires: javatools-package-rename-task
BuildRequires: sun-htmlmacro
BuildRequires: jakarta-commons-jelly-tags-jsl >= 0:1.0
BuildRequires: sun-jaxws-2.1-api
BuildRequires: xml-commons-resolver11
%if 0
BuildRequires: findbugs
%endif
%endif
BuildArch:      noarch
Source44: import.info

%description
The Java API for XML-Based Web Services (JAX-WS) 2.1
according to JSR-224 MR2i.

%if %with repolib
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
Provides:       jaxws-javadoc = 0:2.1
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1

%{__perl} -pi \
    -e 's/\@API_VERSION\@/%{apiver}/g;' \
    -e 's/\@VERSION\@/%{version}/g;' \
    -e 's/\@JAXB_VERSION\@/%{jaxbver}/g;' \
    etc/poms/jaxws-api.pom etc/poms/jaxws-rt.pom etc/poms/jaxws-tools.pom

%{__perl} -pi \
    -e 's/com\.sun\.org\.apache\.xml\.internal/org.apache.xml/g;' \
    rt/src/com/sun/xml/ws/util/xml/XmlUtil.java tools/wscompile/src/com/sun/tools/ws/wscompile/WsimportOptions.java

%if %without bundled
# FIXME: These jars are still bundled, and http.jar is part of Sun JDK6.
%{_bindir}/find -type f -name "*.jar" -a -not -name jaxws-asm.jar -a -not -name installer-builder.jar -a -not -name maven-repository-importer.jar -a -not -name http.jar | %{_bindir}/xargs -t %{__rm}
pushd lib
# remove all jars
%{__ln_s} $(build-classpath jaf_1_1_api) activation.jar
%{__ln_s} $(build-classpath sun-fi) FastInfoset.jar
%{__ln_s} $(build-classpath glassfish-jaxb/jaxb-api) .
%{__ln_s} $(build-classpath glassfish-jaxb/jaxb-impl) .
%{__ln_s} $(build-classpath glassfish-jaxb/jaxb-xjc) .
# XXX
%if 0
%{__ln_s} $(build-classpath sun-jaxws/jaxws-api) .
%else
%{__ln_s} $(build-classpath sun-jaxws-2.1-api) jaxws-api.jar
%endif
# XXX: jaxws-rt
# XXX: jaxws-tools
%{__ln_s} $(build-classpath codehaus-stax11-api) jsr173_api.jar
%{__ln_s} $(build-classpath sun-ws-metadata-2.0-api) jsr181-api.jar
%{__ln_s} $(build-classpath jboss-ejb-3.0-api) jsr250-api.jar
%{__ln_s} $(build-classpath sun-mimepull) mimepull.jar
# XXX: not right
%if 0
%{__ln_s} $(build-classpath xml-commons-resolver12) resolver.jar
%endif
%if 0
%{__ln_s} $(build-classpath sun-saaj-1.3-api) saaj-api.jar
%{__ln_s} $(build-classpath sun-saaj-1.3-impl) saaj-impl.jar
%endif
%{__ln_s} $(build-classpath servlet_2_5_api) servlet.jar
%{__ln_s} $(build-classpath sun-sjsxp) sjsxp.jar
%{__ln_s} $(build-classpath stax-ex) .
%{__ln_s} $(build-classpath sun-xmlstreambuffer) streambuffer.jar
%{__ln_s} $(build-classpath sun-htmlmacro) htmlmacro.jar
%{__ln_s} $(build-classpath jakarta-commons-jelly-tags-jsl) jakarta-commons-jelly-tags-jsl.jar
%{__ln_s} $(build-classpath wstx/wstx-lgpl) woodstox.jar

%{__ln_s} $(build-classpath javatools-package-rename-task) package-rename-task.jar

%{__ln_s} $(build-classpath xml-commons-resolver11) resolver.jar

%if 0
%{__mkdir_p} etc/findbugs
%{__cp} -pr %{_datadir}/findbugs/* etc/findbugs/
%endif
popd
%endif

%build
export CLASSPATH=
export OPT_JAR_LIST=$(%{__cat} %{_sysconfdir}/ant.d/{junit,trax})
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=first -Djar.suffix=%{version} javadocs-spi dist dist-zip-with-src push-to-maven-prepare

%install

# FIXME
%{__cp} -p $(build-classpath sun-jaxws-2.1-api) build/lib/jaxws-api.jar

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__mkdir_p} %{buildroot}%{_javadir}/sun-jaxws/
###
%{__cp} -p build/lib/jaxws-api.jar %{buildroot}%{_javadir}/sun-jaxws/jaxws-api.jar
%{__cp} -p build/lib/jaxws-rt.jar %{buildroot}%{_javadir}/sun-jaxws/jaxws-rt.jar
%{__cp} -p build/lib/jaxws-tools.jar %{buildroot}%{_javadir}/sun-jaxws/jaxws-tools.jar
###
pushd %{buildroot}%{_javadir}/sun-jaxws
%{__ln_s} $(build-classpath sun-fi) FastInfoset.jar
%{__ln_s} $(build-classpath stax_1_0_api) jsr173_api.jar
%{__ln_s} $(build-classpath ws_metadata_2_0_api) jsr181-api.jar
%{__ln_s} $(build-classpath jboss-ejb-3.0-api) jsr250-api.jar
%if 1
%{__ln_s} $(build-classpath saaj_1_3_api) saaj-api.jar
%{__ln_s} $(build-classpath sun-saaj-1.3-impl) saaj-impl.jar
%endif
%{__ln_s} $(build-classpath sun-sjsxp) sjsxp.jar
%{__ln_s} $(build-classpath stax-ex) stax-ex.jar
%{__ln_s} $(build-classpath sun-xmlstreambuffer) streambuffer.jar
popd
# FIXME: Do not have these two built from sources
%{__cp} -p build/lib/http.jar %{buildroot}%{_javadir}/sun-jaxws/http.jar
%{__cp} -p build/lib/resolver.jar %{buildroot}%{_javadir}/sun-jaxws/resolver.jar
###

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr build/javadocs/spi/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p etc/poms/jaxws-api.pom %{buildroot}%{_datadir}/maven2/poms/JPP.sun-jaxws-jaxws-api.pom
%add_to_maven_depmap javax.xml.ws jaxws-api %{apiver} JPP/sun-jaxws jaxws-api
%add_to_maven_depmap sun-jaxws jaxws-api %{apiver} JPP/sun-jaxws jaxws-api
%{__cp} -p etc/poms/jaxws-rt.pom %{buildroot}%{_datadir}/maven2/poms/JPP.sun-jaxws-jaxws-rt.pom
%add_to_maven_depmap com.sun.xml.ws jaxws-rt %{version} JPP/sun-jaxws jaxws-rt
%add_to_maven_depmap sun-jaxws jaxws-rt %{version} JPP/sun-jaxws jaxws-rt
%{__cp} -p etc/poms/jaxws-tools.pom %{buildroot}%{_datadir}/maven2/poms/JPP.sun-jaxws-jaxws-tools.pom
%add_to_maven_depmap com.sun.xml.ws jaxws-tools %{version} JPP/sun-jaxws jaxws-tools
%add_to_maven_depmap sun-jaxws jaxws-tools %{version} JPP/sun-jaxws jaxws-tools
###
%if 0
# XXX: provided by sun-ws-metadata-2.0-api RPM
%{__cp} -p etc/poms/jsr181.pom %{buildroot}%{_datadir}/maven2/poms/JPP.sun-jaxws-jsr181-api.pom
%add_to_maven_depmap javax.jws jsr181-api 1.0-MR1 JPP/sun-jaxws jsr181-api
%endif
###

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE1} %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH1} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/sun-jaxws/jaxws-api.jar %{buildroot}%{repodirlib}/
%{__cp} -p %{buildroot}%{_javadir}/sun-jaxws/jaxws-rt.jar %{buildroot}%{repodirlib}/
%{__cp} -p %{buildroot}%{_javadir}/sun-jaxws/jaxws-tools.jar %{buildroot}%{repodirlib}/
%{__cp} -p %{buildroot}%{_javadir}/sun-jaxws/jsr173_api.jar %{buildroot}%{repodirlib}/
%{__cp} -p %{buildroot}%{_javadir}/sun-jaxws/jsr181-api.jar %{buildroot}%{repodirlib}/
%{__cp} -p %{buildroot}%{_javadir}/sun-jaxws/jsr250-api.jar %{buildroot}%{repodirlib}/
###
%{__cp} -p %{buildroot}%{_javadir}/sun-jaxws/http.jar %{buildroot}%{repodirlib}/
%{__cp} -p %{buildroot}%{_javadir}/sun-jaxws/resolver.jar %{buildroot}%{repodirlib}/
###
%{__cp} -p %{buildroot}%{_javadir}/sun-jaxws/FastInfoset.jar %{buildroot}%{repodirlib}/
%if 1
%{__cp} -p %{buildroot}%{_javadir}/sun-jaxws/saaj-api.jar %{buildroot}%{repodirlib}/
%{__cp} -p %{buildroot}%{_javadir}/sun-jaxws/saaj-impl.jar %{buildroot}%{repodirlib}/
%endif
%{__cp} -p %{buildroot}%{_javadir}/sun-jaxws/sjsxp.jar %{buildroot}%{repodirlib}/
%{__cp} -p %{buildroot}%{_javadir}/sun-jaxws/streambuffer.jar %{buildroot}%{repodirlib}/
%{__cp} -p %{buildroot}%{_javadir}/sun-jaxws/stax-ex.jar %{buildroot}%{repodirlib}/
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP.sun-jaxws-jaxws-api.pom %{buildroot}%{repodirlib}/jaxws-api.pom
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP.sun-jaxws-jaxws-rt.pom %{buildroot}%{repodirlib}/jaxws-rt.pom
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP.sun-jaxws-jaxws-tools.pom %{buildroot}%{repodirlib}/jaxws-tools.pom
###
%if 0
# XXX: provided by sun-ws-metadata-2.0-api RPM
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP.sun-jaxws-jsr181-api.pom %{buildroot}%{repodirlib}/jsr181-api.pom
%endif
###
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxws_2_1_api_glassfish-jaxws<<EOF
%{_javadir}/jaxws_2_1_api.jar	%{_javadir}/sun-jaxws/jaxws-api.jar	20107
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxws_api_glassfish-jaxws<<EOF
%{_javadir}/jaxws_api.jar	%{_javadir}/sun-jaxws/jaxws-api.jar	20107
EOF

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%files
%_altdir/jaxws_api_glassfish-jaxws
%_altdir/jaxws_2_1_api_glassfish-jaxws
%doc CDDL-1.0-license.txt
%dir %{_javadir}/sun-jaxws
###
%{_javadir}/sun-jaxws/http.jar
%{_javadir}/sun-jaxws/resolver.jar
###
%{_javadir}/sun-jaxws/jaxws-api.jar
%{_javadir}/sun-jaxws/jaxws-rt.jar
%{_javadir}/sun-jaxws/jaxws-tools.jar
###
%{_javadir}/sun-jaxws/FastInfoset.jar
%{_javadir}/sun-jaxws/jsr173_api.jar
%{_javadir}/sun-jaxws/jsr181-api.jar
%{_javadir}/sun-jaxws/jsr250-api.jar
%if 1
%{_javadir}/sun-jaxws/saaj-api.jar
%{_javadir}/sun-jaxws/saaj-impl.jar
%endif
%{_javadir}/sun-jaxws/sjsxp.jar
%{_javadir}/sun-jaxws/stax-ex.jar
%{_javadir}/sun-jaxws/streambuffer.jar
###
%{_datadir}/maven2/poms/JPP.sun-jaxws-jaxws-api.pom
%{_datadir}/maven2/poms/JPP.sun-jaxws-jaxws-rt.pom
%{_datadir}/maven2/poms/JPP.sun-jaxws-jaxws-tools.pom
###
%if 0
# XXX: provided by sun-ws-metadata-2.0-api RPM
%{_datadir}/maven2/poms/JPP.sun-jaxws-jsr181-api.pom
%endif
###
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_8jpp6
- fixed components-info
- hack: added saaj-api/impl.jar though jaxws is built w/o them,
  for jbossas compatibility

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_8jpp6
- new version

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_4jpp5
- fixed components-info

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_4jpp5
- fixed repocop warnings

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_3jpp5.1
- NMU (by repocop): the following fixes applied:
 * windows-thumbnail-database-in-package for glassfish-jaxws-javadoc

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_3jpp5
- converted from JPackage by jppimport script

