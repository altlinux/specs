Packager: Igor Vlasenko <viy@altlinux.ru>
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support
#def_with bootstrap
%bcond_with bootstrap
%bcond_without repolib

%define reltag patch02
%define repodir %{_javadir}/repository.jboss.com/apache-xalan/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define cvs_version 2_7_1

Name:           xalan-j2
Version:        2.7.1
Release:        alt2_1jpp6
Epoch:          0
Summary:        Java XSLT processor
License:        ASL 2.0
Source0:        http://www.apache.org/dist/xml/xalan-j/xalan-j_%{cvs_version}-src.tar.gz
Source1:        xalan-j2-2.7.0-component-info.xml
#Patch0:         %{name}-noxsltcdeps.patch
#Patch1:         %{name}-manifest.patch
#Patch2:         %{name}-crosslink.patch
# Fix the XALANJ-2376:
#TransformerFactory.newTransformer(source) returns null instead throwing
#an exception and according to the specs newTransformer() should not
#return null.
Patch3:         %{name}-XALANJ-2376.patch
# has been merged into 2.7.1 sources
#Patch4:         %{name}-XALANJ-2321-AVT.patch
URL:            http://xalan.apache.org/
Group:          Development/Java
Provides:       jaxp_transform_impl
Requires: jaxp_parser_impl
Requires(post): alternatives >= 0:0.4
Requires(preun): alternatives >= 0:0.4
BuildRequires: ant
BuildRequires: java-javadoc
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: xerces-j2 >= 0:2.7.1
BuildRequires: xml-commons-jaxp-1.3-apis
%if %without bootstrap
BuildRequires: java-cup
BuildRequires: bcel
BuildRequires: jlex
BuildRequires: regexp
BuildRequires: sed
BuildRequires: servlet_2_4_api
BuildRequires: xml-stylebook
%endif
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info
Source45: xalan-j2-serializer-2.7.1.jar-OSGi-MANIFEST.MF
BuildRequires: dos2unix
Provides: xalan-j = %{name}-%{version}
Obsoletes: xalan-j <= 2.7.0-alt3

%description
Xalan is an XSLT processor for transforming XML documents into HTML,
text, or other XML document types. It implements the W3C Recommendations
for XSL Transformations (XSLT) and the XML Path Language (XPath). It can
be used from the command line, in an applet or a servlet, or as a module
in other program.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%if %without bootstrap
%package        xsltc
Summary:        XSLT compiler
Group:          Development/Java
Requires: java-cup
Requires: bcel
Requires: jlex
Requires: regexp
Requires: jaxp_parser_impl

%description    xsltc
The XSLT Compiler is a Java-based tool for compiling XSLT stylesheets into
lightweight and portable Java byte codes called translets.
%endif

%package        manual
Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description    manual
Documentation for %{name}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%if %without bootstrap
%package        demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: servlet_2_4_api

%description    demo
Demonstrations and samples for %{name}.
%endif

%prep
%setup -q -n xalan-j_%{cvs_version}
#%patch0 -p0
#%patch1 -p0
#%patch2 -p0
%patch3 -p0
#%patch4 -p0
# Remove all binary libs, except ones needed to build docs and N/A elsewhere.
for j in $(find . -name "*.jar"); do
        #mv $j $j.no
        rm $j
done

# FIXME: who knows where the sources are? xalan-j1 ?
#mv tools/xalan2jdoc.jar.no tools/xalan2jdoc.jar
#mv tools/xalan2jtaglet.jar.no tools/xalan2jtaglet.jar

%{__chmod} 0755 samples/extensions/sql/*.sh
# xerces-j2 2.9.1 in repolib
if grep 2.7.1 %{SOURCE1}; then
subst s,2.7.1,2.9.1, %{SOURCE1}
else
echo Hook is deprecated!!! delete it.
fi

%build
pushd lib
ln -sf $(build-classpath java-cup-runtime) runtime.jar
ln -sf $(build-classpath bcel) BCEL.jar
ln -sf $(build-classpath regexp) regexp.jar
ln -sf $(build-classpath xerces-j2) xercesImpl.jar
ln -sf $(build-classpath xml-commons-jaxp-1.3-apis) xml-apis.jar
popd
pushd tools
ln -sf $(build-classpath java-cup) java_cup.jar
ln -sf $(build-classpath ant) ant.jar
ln -sf $(build-classpath jlex) JLex.jar
ln -sf $(build-classpath xml-stylebook) stylebook-1.0-b3_xalan-2.jar
popd
export CLASSPATH=$(build-classpath servlet_2_4_api)
export OPT_JAR_LIST=:
%if %with bootstrap
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Djava.awt.headless=true \
  -Dapi.j2se=%{_javadocdir}/java \
  -Dbuild.xalan-interpretive.jar=build/xalan-interpretive.jar \
  xalan-interpretive.jar
%else
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Djava.awt.headless=true \
  -Dapi.j2se=%{_javadocdir}/java \
  -Dbuild.xalan-interpretive.jar=build/xalan-interpretive.jar \
  xalan-interpretive.jar\
  xsltc.unbundledjar \
  docs \
  xsltc.docs \
  javadocs \
  samples \
  servlet
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 build/xalan-interpretive.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%if %without bootstrap
install -p -m 644 build/xsltc.jar \
  $RPM_BUILD_ROOT%{_javadir}/xsltc-%{version}.jar
%endif
install -p -m 644 build/serializer.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-serializer-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# add a symlink to serializer.jar to match upstream jar naming
ln -sf %{name}-serializer-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/serializer.jar
ln -sf %{name}.jar $RPM_BUILD_ROOT%{_javadir}/xalan.jar

%if %without bootstrap
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
# FIXME: (dwalluck): breaks --short-circuit
rm -rf build/docs/apidocs

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 build/xalansamples.jar \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}-samples.jar
install -p -m 644 build/xalanservlet.war \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}-servlet.war
cp -pr samples $RPM_BUILD_ROOT%{_datadir}/%{name}

# fix link between manual and javadoc
(cd build/docs; ln -sf %{_javadocdir}/%{name}-%{version} apidocs)
%endif

# jaxp_transform_impl ghost symlink
ln -s %{_sysconfdir}/alternatives \
  $RPM_BUILD_ROOT%{_javadir}/jaxp_transform_impl.jar

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}.%{reltag}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
#install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
#install -p -m 644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
#install -p -m 644 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH3} $RPM_BUILD_ROOT%{repodirsrc}
#install -p -m 644 %{PATCH4} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/serializer.jar $RPM_BUILD_ROOT%{repodirlib}/serializer.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/xalan.jar $RPM_BUILD_ROOT%{repodirlib}/xalan.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxp_transform_impl_%{name}<<EOF
%{_javadir}/jaxp_transform_impl.jar	%{_javadir}/%{name}.jar	30
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxp_transform_impl_%{name}-xsltc<<EOF
%{_javadir}/jaxp_transform_impl.jar	%{_javadir}/xsltc.jar	10
EOF

# inject OSGi manifest xalan-j2-serializer-2.7.1.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE45} META-INF/MANIFEST.MF
zip -u %buildroot/usr/share/java/xalan-j2-serializer.jar META-INF/MANIFEST.MF

find $RPM_BUILD_ROOT -name '*.sh' -print0 | xargs -0 dos2unix
grep -r -m 1 -l -Z '^#!/bin/sh' $RPM_BUILD_ROOT%_bindir | xargs -0 dos2unix
ln -s xalan-j2.jar $RPM_BUILD_ROOT/%{_javadir}/xalan-j.jar
ln -s xalan-j2 $RPM_BUILD_ROOT/%{_javadocdir}/xalan-j
# end inject OSGi manifest xalan-j2-serializer-2.7.1.jar-OSGi-MANIFEST.MF

%files
%{_javadir}/xalan-j.jar
%_altdir/jaxp_transform_impl_%{name}
%doc KEYS LICENSE.txt NOTICE.txt readme.html
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-serializer-%{version}.jar
%{_javadir}/%{name}-serializer.jar
%{_javadir}/serializer.jar
%{_javadir}/xalan.jar
%exclude %{_javadir}/jaxp_transform_impl.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%{_libdir}/gcj/%{name}/%{name}-serializer-%{version}.jar.*
%endif

%if %without bootstrap
%files xsltc
%_altdir/jaxp_transform_impl_%{name}-xsltc
%{_javadir}/xsltc-%{version}.jar
%{_javadir}/xsltc.jar

%if %{gcj_support}
%{_libdir}/gcj/%{name}/xsltc-%{version}.jar.*
%endif

%files manual
%doc --no-dereference build/docs/*

%files javadoc
%{_javadocdir}/xalan-j
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-samples.jar.*
%endif
%endif

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sun Dec 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt2_1jpp6
- fixed xerces dependency in repolib

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt1_1jpp6
- added OSGi provides to serializer.jar

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.7.0-alt6_10jpp5
- fixed repocop warnings

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.7.0-alt6_9jpp5
- jpp5 build

* Tue May 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.7.0-alt6_7jpp1.7
- rebuild on x86_64; added explicit source and target 1.4
- obsoletes: xalan-j

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.7.0-alt5_7jpp1.7
- rebuild on x86_64; added explicit source and target 1.4
- obsoletes: xalan-j

* Sat Apr 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.7.0-alt3_7jpp1.7
- converted from JPackage by jppimport script

* Tue Jun 20 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.0-alt3
- Fixed the dependency in xalan-j-manual

* Sat Mar 04 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.0-alt2
- Install serializer.jar

* Sun Feb 26 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.0-alt1
- 2.7.0
- Use new xml-commons-external

* Sat Jan 15 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt3
- Enable xsltc by default
- Converted to rpm-build-java macros
- Stripped the source archive from unnecessary jars.
  Building from original archive is still available via --with origsrc

* Fri Aug 27 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt2
- Do not BuildRequire system stylebook as it BuildRequires xalan-j
- New alternatives format (ugh)
- Grouped everything under Development/Java

* Sat Apr 17 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt1
- New upstream release
- Updated manifest patch

* Mon Jan 12 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.2-alt3
- Migration to the new alternatives scheme

* Fri Dec 19 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.2-alt2
- Build using XML APIs and a JAXP parser installed in the system
- Enabled javadoc back
- Added update-alternatives to install-time dependencies
- Added xml-commons-apis to Requires

* Thu Dec 18 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.2-alt1
- New upstream release

* Sat Sep 13 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.1-alt1
- Ported to ALT Linux from JPackage project
- Don't build xsltc and demo for now, due to dependencies.
