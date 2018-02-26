Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: xml-commons-resolver
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
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

#def_with manual
%bcond_with             manual

%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/apache-xerces/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define cvs_version        2_9_1
%define gcj_support        %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

Name:           xerces-j2
Version:        2.9.1
Release:        alt2_2jpp6
Epoch:          0
Summary:        Java XML parser
License:        ASL 2.0
URL:            http://xerces.apache.org/xerces2-j/
Group:          Development/Java
# svn export https://svn.apache.org/repos/asf/xerces/java/tags/Xerces-J_2_9_1/
Source0:        http://www.apache.org/dist/xml/xerces-j/Xerces-J-src.%{version}.tar.bz2
Source3:        %{name}-version.sh
Source4:        %{name}-constants.sh
Source5:        %{name}-component-info.xml
Patch0:         %{name}-build.patch
Patch1:         %{name}-libgcj.patch
Provides:       jaxp_parser_impl
Obsoletes:      xerces-j2-dom3 < %{epoch}:%{version}-%{release}
Provides:       xerces-j2-dom3 = %{epoch}:%{version}-%{release}
Requires: xalan-j2
Requires: xml-commons-jaxp-1.3-apis
Requires: xml-commons-resolver12 >= 0:1.1
Requires(post): alternatives >= 0:0.4
Requires(preun): alternatives >= 0:0.4
BuildRequires: ant >= 0:1.5
BuildRequires: jaxp_parser_impl
BuildRequires: xalan-j2
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: xml-commons-resolver12 >= 0:1.3
BuildRequires: xml-stylebook
%if %{with_repolib}
BuildRequires: xml-commons-repolib = 0:1.3.04
%endif
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info
Source45: xerces-j2-2.9.0.jar-OSGi-MANIFEST.MF
Provides: xerces-j = %version-%release
Obsoletes: xerces-j <= 2.9.0-alt4

%description
Welcome to the future! Xerces2 is the next generation of high
performance, fully compliant XML parsers in the Apache Xerces family.
This new version of Xerces introduces the Xerces Native Interface (XNI),
a complete framework for building parser components and configurations
that is extremely modular and easy to program.

The Apache Xerces2 parser is the reference implementation of XNI but
other parser components, configurations, and parsers can be written
using the Xerces Native Interface. For complete design and
implementation documents, refer to the XNI Manual.

Xerces 2 is a fully conforming XML Schema processor. For more
information, refer to the XML Schema page.

Xerces 2 also provides a partial implementation of Document Object Model
Level 3 Core, Load and Save and Abstract Schemas [deprecated] Working
Drafts. For more information, refer to the DOM Level 3 Implementation
page.

%if %{with_repolib}
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc-impl
Summary:        Javadoc for %{name} implementation
Group:          Development/Documentation

%description javadoc-impl
Javadoc for %{name} implementation.

%package javadoc-apis
Summary:        Javadoc for %{name} apis
Group:          Development/Documentation
Obsoletes:      xerces-j2-dom3-javadoc < %{epoch}:%{version}-%{release}
Provides:       xerces-j2-dom3-javadoc = %{epoch}:%{version}-%{release}

%description javadoc-apis
Javadoc for %{name} apis.

%package javadoc-xni
Summary:        Javadoc for %{name} xni
Group:          Development/Documentation

%description javadoc-xni
Javadoc for %{name} xni.

%package javadoc-other
Summary:        Javadoc for other %{name} components
Group:          Development/Documentation

%description javadoc-other
Javadoc for other %{name} components.

%if %with manual
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif

%package demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%package scripts
Summary:        Additional utility scripts for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jpackage-utils >= 0:1.6

%description scripts
Additional utility scripts for %{name}.

%prep
%setup -q -n Xerces-J_%{cvs_version}

%{_bindir}/find -name '*.jar' -o -name '*.class' | %{_bindir}/xargs -t rm

mkdir -p tools/org/apache/xerces/util
cp -p tools/src/XJavac.java tools/org/apache/xerces/util/XJavac.java
cp -p tools/src/ExperimentalTaglet.java tools/org/apache/xerces/util/ExperimentalTaglet.java
cp -p tools/src/InternalTaglet.java tools/org/apache/xerces/util/InternalTaglet.java

mkdir -p tools/bin

%patch0 -p1 -b .build
%patch1 -p0 -b .libgcj

%build
pushd tools
%{javac} -classpath $(build-classpath ant) org/apache/xerces/util/XJavac.java
%{jar} cf bin/xjavac.jar org/apache/xerces/util/XJavac.class
%{javac} -classpath %{java_home}/lib/tools.jar org/apache/xerces/util/ExperimentalTaglet.java org/apache/xerces/util/InternalTaglet.java
%{jar} cf bin/xerces2taglets.jar org/apache/xerces/util/ExperimentalTaglet.class org/apache/xerces/util/InternalTaglet.class
popd

export ANT_OPTS="-Djava.awt.headless=true"
export CLASSPATH=$(build-classpath xalan-j2-serializer):%{java_home}/jre/lib/rt.jar
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
        -Dbuild.compiler=modern \
        -Dtools.dir=%{_javadir} \
        -Djar.apis=xml-commons-jaxp-1.3-apis.jar \
        -Djar.resolver=xml-commons-resolver12.jar \
        -Djar.serializer=xalan-j2-serializer.jar \
        clean jars javadocs \
%if %with manual
docs
%else

%endif

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/xercesImpl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *.jar; do ln -sf ${jar} dom3-${jar}; done)
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xercesImpl-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-impl-%{version}
cp -pr build/docs/javadocs/xerces2/* \
  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-impl-%{version}
ln -s %{name}-impl-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-impl

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-apis-%{version}
cp -pr build/docs/javadocs/api/* \
  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-apis-%{version}
ln -s %{name}-apis-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-apis

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-xni-%{version}
cp -pr build/docs/javadocs/xni/* \
  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-xni-%{version}
ln -s %{name}-xni-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-xni

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-other-%{version}
cp -pr build/docs/javadocs/other/* \
  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-other-%{version}
ln -s %{name}-other-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-other

# FIXME: (dwalluck): breaks -bi --short-circuit
rm -rf build/docs/javadocs

%if %with manual
# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if !%{gcj_support}
cp -pr build/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif
%endif

# scripts
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/%{name}-version
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/%{name}-constants

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -p build/xercesSamples.jar \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}-samples.jar
cp -pr data $RPM_BUILD_ROOT%{_datadir}/%{name}

%if %{with_repolib}
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/xercesImpl.jar
cp -p %{_javadir}/repository.jboss.com/apache-xml-commons/1.3.04-brew/lib/resolver.jar $RPM_BUILD_ROOT%{repodirlib}/resolver.jar
cp -p %{_javadir}/repository.jboss.com/apache-xml-commons/1.3.04-brew/lib/xml-apis.jar $RPM_BUILD_ROOT%{repodirlib}/xml-apis.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxp_parser_impl_%{name}<<EOF
%{_javadir}/jaxp_parser_impl.jar	%{_javadir}/%{name}.jar	40
EOF
chmod 755 $RPM_BUILD_ROOT%{_bindir}/*

# inject OSGi manifest xerces-j2-2.9.0.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE45} META-INF/MANIFEST.MF
zip -u %buildroot/usr/share/java/xerces-j2.jar META-INF/MANIFEST.MF
ln -s xerces-j2.jar $RPM_BUILD_ROOT%_javadir/xerces-j.jar

%files
%_altdir/jaxp_parser_impl_%{name}
%doc LICENSE LICENSE-SAX.html LICENSE.DOM-documentation.html
%doc LICENSE.DOM-software.html LICENSE.resolver.txt
%doc LICENSE.serializer.txt NOTICE NOTICE.resolver.txt
%doc NOTICE.serializer.txt README Readme.html
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/dom3-%{name}-%{version}.jar
%{_javadir}/dom3-%{name}.jar
%{_javadir}/xercesImpl-%{version}.jar
%{_javadir}/xercesImpl.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/xercesImpl.jar.db
%{_libdir}/gcj/%{name}/xercesImpl.jar.so
%endif
%_javadir/xerces-j.jar

%files javadoc-impl
%{_javadocdir}/%{name}-impl-%{version}
%{_javadocdir}/%{name}-impl

%files javadoc-apis
%{_javadocdir}/%{name}-apis-%{version}
%{_javadocdir}/%{name}-apis

%files javadoc-other
%{_javadocdir}/%{name}-other-%{version}
%{_javadocdir}/%{name}-other

%files javadoc-xni
%{_javadocdir}/%{name}-xni-%{version}
%{_javadocdir}/%{name}-xni

%if %with manual
%files manual
%doc %{_docdir}/%{name}-%{version}/
%endif

%files demo
%{_datadir}/%{name}
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-samples.jar.db
%{_libdir}/gcj/%{name}/%{name}-samples.jar.so
%endif

%files scripts
#%defattr(0755,root,root,0755)
%{_bindir}/xerces-j2-constants
%{_bindir}//xerces-j2-version

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt2_2jpp6
- build w/java6

* Fri Dec 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt1_2jpp6
- added OSGi provides

* Tue Jan 13 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.9.0-alt6_12jpp5
- added repolib as in jpp 5.0 template

* Sat Apr 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.9.0-alt5_2jpp1.7
- fixed script permissions

* Wed Feb 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.9.0-alt4_2jpp1.7
- converted from JPackage by jppimport script

* Wed Feb 06 2008 Igor Vlasenko <viy@altlinux.ru> 2.9.0-alt4
- added Provides: xerces-j2-demo to demo.
- demo subpackage is now xerces-j2 compatible.

* Tue Aug 21 2007 Igor Vlasenko <viy@altlinux.ru> 2.9.0-alt3
- rebuilt with java-1.5.0

* Mon May 21 2007 Igor Vlasenko <viy@altlinux.ru> 2.9.0-alt2
- NMU: 
  * fixes for X-less build
  * fixed bug in alternatives (jaxp_parser_impl.jar)
  * javadocs are split almost as they should be
  * added scripts subpackage

* Tue Apr 24 2007 Eugene Ostapets <eostapets@altlinux.ru> 2.9.0-alt1
- 2.9.0 

* Tue Apr 24 2007 Eugene Ostapets <eostapets@altlinux.ru> 2.8.1-alt2
- fix build with java-1.6-sun
- add compatibility with JPackage

* Wed Nov 15 2006 Eugene Ostapets <eostapets@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Sat Mar 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.8.0-alt1
- 2.8.0
- Updated Patch1

* Sun Feb 26 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.1-alt2
- Fixes to build with JDK 1.5

* Wed Jul 27 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.1-alt1
- New upstream release

* Mon Jun 27 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.0-alt1
- New upstream release
- Raised jaxp_parser_impl.jar alternative level to 130
  to reflect the JAXP 1.3 implementation
- Updated Patch1
- Use rpm-build-java macros
- Conditionally build samples, disabled by default
  (can not compile with 1.4.2)

* Tue Aug 31 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.2-alt2
- New alternatives format

* Mon Mar 08 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.2-alt1
- Remove JDK version hardcoding

* Sun Feb 22 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.2-alt0.1
- Updated to upstream release 2.6.2

* Wed Jan 21 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt3.1
- Temporarily hardcode the JDK

* Sat Dec 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt3
- Patches from Alexey Borovskoy
- Use xvfb-run to start fake X server
- Migration to new alternatives scheme

* Sat Dec 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt2
- Added update-alternatives to install-time dependencies
- Corrected timing of updating alternatives during uninstall/upgrade
- Set JAVA_HOME to the commonly known J2SE directory

* Thu Dec 11 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt1
- New upstream release

* Thu Sep 11 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.0-alt1
- Updated to 2.5.0, renamed to xerces-j because xerces 1.x is obsolete
- Dropped README from the docs as it contains nothing but build instructions
- Remove JAXP api docs from javadoc, link to xml-commons-apis instead

* Sun Nov 17 2002 Mikhail Zabaluev <mhz@altlinux.ru> 2.2.1-alt1
- Ported the package over from the JPackage project. Thank you guys.
