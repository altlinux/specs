BuildRequires: javapackages-local
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: docbook-dtds
%define _without_tests 1
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
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

Name:           mx4j
Version:        3.0.1
Release:        alt4_22jpp8
Epoch:          1
Summary:        Open source implementation of JMX Java API
License:        ASL 1.1
Group:          Development/Other
Source0:        %{name}-%{version}-src.tar.gz
Source1:        %{name}-build.policy
Source2:        CatalogManager.properties

Source3:        http://repo1.maven.org/maven2/mx4j/mx4j/%{version}/mx4j-%{version}.pom
Source4:        http://repo1.maven.org/maven2/mx4j/mx4j-jmx/%{version}/mx4j-jmx-%{version}.pom
Source5:        http://repo1.maven.org/maven2/mx4j/mx4j-jmx-remote/%{version}/mx4j-jmx-remote-%{version}.pom
Source6:        http://repo1.maven.org/maven2/mx4j/mx4j-remote/%{version}/mx4j-remote-%{version}.pom
Source7:        http://repo1.maven.org/maven2/mx4j/mx4j-tools/%{version}/mx4j-tools-%{version}.pom
# not available
Source8:        http://repo1.maven.org/maven2/mx4j/mx4j-impl/2.1.1/mx4j-impl-2.1.1.pom
Source9:        http://repo1.maven.org/maven2/mx4j/mx4j-rimpl/2.1.1/mx4j-rimpl-2.1.1.pom
Source10:       http://repo1.maven.org/maven2/mx4j/mx4j-rjmx/2.1.1/mx4j-rjmx-2.1.1.pom

Patch0:         mx4j-javaxssl.patch
Patch1:         mx4j-%{version}.patch
Patch2:         mx4j-build.patch
Patch3:         mx4j-docbook.patch
Patch5:         mx4j-caucho-build.patch
Patch6:         mx4j-no-iiop.patch
URL:            http://mx4j.sourceforge.net/
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-apache-resolver
BuildRequires:  javamail >= 0:1.2
BuildRequires:  log4j >= 0:1.2.7
BuildRequires:  apache-commons-logging >= 0:1.0.1
BuildRequires:  xml-commons-apis
BuildRequires:  bcel >= 0:5.0
BuildRequires:  coreutils
BuildRequires:  axis >= 0:1.1
BuildRequires:  wsdl4j
BuildRequires:  apache-commons-discovery
BuildRequires:  docbook-dtds >= 0:1.0
BuildRequires:  docbook-style-xsl >= 0:1.61
BuildRequires:  xml-commons-resolver
BuildRequires:  xml-commons
BuildRequires:  xerces-j2
BuildRequires:  dos2unix
BuildArch:      noarch
Requires:       javamail >= 0:1.2
Requires:       log4j >= 0:1.2.7
Requires:       apache-commons-logging >= 0:1.0.1
Requires:       xml-commons-apis
Requires:       bcel >= 0:5.0
Requires:       axis >= 0:1.1
Requires:       xml-commons-resolver
Requires:       xml-commons
Source44: import.info

%description
OpenJMX is an open source implementation of the
Java(TM) Management Extensions (JMX).

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package manual
Group:          Development/Other
Summary:        Documentation for %{name}
BuildArch: noarch

%description    manual
Documentation for %{name}.

%prep
%setup -q

# FIXME To enable iiop when rmic becomes available
# turn off patch6 and turn on patch4
# Patch4 is a backport of upstream changes (MX4J) and may go
# away on future releases
%patch0 -p1
%patch1 -p0
%patch2 -b .sav
%patch3 -p1
%patch5 -p1
%patch6 -p1

cp %{SOURCE1} build
cp %{_sourcedir}/CatalogManager.properties %{_builddir}/%{name}-%{version}/build/

cp %{SOURCE8} %{name}-impl-%{version}.pom
cp %{SOURCE9} %{name}-rimpl-%{version}.pom
cp %{SOURCE10} %{name}-rjmx-%{version}.pom
sed -i "s|<version>2.1.1</version>|<version>%{version}</version>|" %{name}-*-%{version}.pom

pushd lib
   ln -sf $(build-classpath xml-commons-apis) xml-apis.jar
   ln -sf $(build-classpath xerces-j2) xercesImpl.jar
   ln -sf $(build-classpath xalan-j2) xalan.jar
   ln -sf $(build-classpath commons-logging) .
   ln -sf $(build-classpath log4j) .
   ln -sf $(build-classpath bcel) .
   ln -sf $(build-classpath axis/axis) .
   ln -sf $(build-classpath axis/jaxrpc) .
   ln -sf $(build-classpath axis/saaj) .
   ln -sf $(build-classpath wsdl4j) .
   ln -sf $(build-classpath commons-discovery) .
   ln -sf $(build-classpath servlet25) servlet.jar
   ln -sf $(build-classpath javamail/mail) .
   ln -sf $(build-classpath xml-commons-resolver) .
popd

%build

export OPT_JAR_LIST="ant/ant-junit junit xmlunit jaxp_transform_impl ant/ant-apache-resolver xml-commons-resolver xalan-j2-serializer"

cd build
ant -Dbuild.sysclasspath=first compile.jmx compile.rjmx compile.tools javadocs docs

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 dist/lib/%{name}-impl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-impl.jar
install -m 644 dist/lib/%{name}-jmx.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jmx.jar
install -m 644 dist/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}.jar
install -m 644 dist/lib/%{name}-tools.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-tools.jar
install -m 644 dist/lib/%{name}-rjmx.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-rjmx.jar
install -m 644 dist/lib/%{name}-rimpl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-rimpl.jar
install -m 644 dist/lib/%{name}-remote.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-remote.jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}/boa
install -m 644 dist/lib/boa/%{name}-rjmx-boa.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/boa/%{name}-rjmx-boa.jar
install -m 644 dist/lib/boa/%{name}-rimpl-boa.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/boa/%{name}-rimpl-boa.jar
install -m 644 dist/lib/boa/%{name}-remote-boa.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/boa/%{name}-remote-boa.jar

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{SOURCE3} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar
install -pm 644 %{SOURCE4} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-jmx.pom
%add_maven_depmap JPP.%{name}-%{name}-jmx.pom %{name}/%{name}-jmx.jar
install -pm 644 %{SOURCE6} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-remote.pom
%add_maven_depmap JPP.%{name}-%{name}-remote.pom %{name}/%{name}-remote.jar
install -pm 644 %{SOURCE7} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-tools.pom
%add_maven_depmap JPP.%{name}-%{name}-tools.pom %{name}/%{name}-tools.jar

install -pm 644 %{name}-impl-%{version}.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-impl.pom
%add_maven_depmap JPP.%{name}-%{name}-impl.pom %{name}/%{name}-impl.jar
install -pm 644 %{name}-rimpl-%{version}.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-rimpl.pom
%add_maven_depmap JPP.%{name}-%{name}-rimpl.pom %{name}/%{name}-rimpl.jar
install -pm 644 %{name}-rjmx-%{version}.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-rjmx.pom
%add_maven_depmap JPP.%{name}-%{name}-rjmx.pom %{name}/%{name}-rjmx.jar

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
dos2unix dist/docs/styles.css README.txt LICENSE.txt
cp -r dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jmxri_mx4j<<EOF
%{_javadir}/jmxri.jar	%{_javadir}/%{name}/%{name}-jmx.jar	10
EOF

%pre
rm -f %{_javadir}/%{name}.jar

%files -f .mfiles
%_altdir/jmxri_mx4j
%{_javadir}/%{name}/boa/
%doc LICENSE.txt
%doc README.txt

%files javadoc
%{_javadocdir}/%{name}

%files manual
%doc dist/docs/*

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt4_22jpp8
- added BR: javapackages-local for javapackages 5

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt3_22jpp8
- updated dependencies

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt2_22jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt2_21jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt2_18jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt2_17jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt2_15jpp7
- fixed xml-commons dep

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt1_15jpp7
- fc version

* Tue Jan 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.0.2-alt1_1jpp6
- new version

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt7_9jpp5
- fixed 0-priority alternative

* Sat Jan 24 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt6_9jpp5
- rebuild for repocop

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt6_8jpp5
- converted from JPackage by jppimport script

* Thu Aug 14 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt6_7jpp1.7
- fixed unpackaged dir

* Fri Mar 07 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt5_7jpp1.7
- added mx4j-3.0.1-alt-local-xsl-stylesheets.patch

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt4_7jpp1.7
- full-fledged build

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt3_7jpp1.7
- updated to new jpackage release

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt3
- provides jmxri; jpp compatible symlinks

* Wed Aug 10 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.0.1-alt2
- Added /proc to BuildRequires

* Sat Jul 30 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.0.1-alt1
- New upstream release

* Fri Feb 25 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.0.0-alt1
- New upstream release

* Thu Jan 20 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.1.1-alt1
- New upstream release

* Tue Nov 23 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.1.0-alt1
- New upstream release
- Package the all-in-one jars containing both API and implementation
- Provided jmx_impl alternative (thanks to Vladimir Lettiev for insight)

* Tue Jul 13 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.0.1-alt1
- New package for Sisyphus.
