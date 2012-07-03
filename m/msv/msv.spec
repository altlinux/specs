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
#

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with bootstrap
%bcond_with bootstrap
#def_with gcj_support
%bcond_with gcj_support

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define cvsversion 20050722 

Name:           msv
Version:        1.2
Release:        alt4_0.20050722.7jpp6
Epoch:          0
Summary:        Multischema Validator
License:        BSD-style
Group:          Development/Java
URL:            http://msv.dev.java.net
Source0:        msv-20050722.tar.gz
Source1:        msv.pom
Source2:        xsdlib.pom
Patch0:         msv-msv-build_xml.patch
Patch1:         msv-relames-build_xml.patch
Patch2:         msv-xsdlib-build_xml.patch
Patch3:         msv-xmlgen-build_xml.patch
# Backported from CVS tip; can go away with an update
# Allow compilation with JDK 1.5
Patch4:         msv-jdk15.patch
Patch5:         msv-nocrimson.patch
Provides:       msv-msv = %{epoch}:%{version}-%{release}
Provides:       msv-strict = %{epoch}:%{version}-%{release}
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: isorelax
Requires: jpackage-utils
Requires: relaxngDatatype
Requires: servletapi5
Requires: xerces-j2
Requires: xml-commons-jaxp-1.3-apis
Requires: xml-commons-resolver11
Requires: msv-xsdlib
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant
BuildRequires: javacc
BuildRequires: junit
%if %without bootstrap
BuildRequires: jdom
BuildRequires: saxon
%endif
BuildRequires: isorelax
BuildRequires: relaxngDatatype
BuildRequires: servletapi5
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: xml-commons-resolver11
Obsoletes:      msv-strict < %{epoch}:%{version}-%{release}
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info
Provides: msv-msv = %version-%release
Obsoletes: msv-msv < %version-%release

%description
The Sun Multi-Schema XML Validator (MSV) is a Java 
technology tool to validate XML documents against 
several kinds of XML schemata. It supports RELAX NG, 
RELAX Namespace, RELAX Core, TREX, XML DTDs, and a 
subset of XML Schema Part 1. This latest (version 1.2) 
release includes several bug fixes and adds better 
conformance to RELAX NG/W3C XML standards and JAXP 
masquerading. 

NOTE: This specific build of msv does not support
'crimson' (use xerces instead)

%package javadoc
Summary:        Javadoc for MSV proper
Group:          Development/Documentation
Obsoletes:      msv-strict-javadoc < %{epoch}:%{version}-%{release}
Provides:       msv-strict-javadoc = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation
Requires: jpackage-utils
Requires: msv-msv
Requires: msv-xsdlib

%description demo
%{summary}.

%package relames
Summary:        Relames 
Group:          Development/Java
Requires: isorelax
Requires: jpackage-utils
Requires: relaxngDatatype
Requires: xalan-j2
Requires: xerces-j2
Requires: xml-commons-jaxp-1.3-apis
Requires: xml-commons-resolver11
Requires: msv-msv
Requires: msv-xsdlib

%description relames
%{summary}.

%package relames-javadoc
Summary:        Javadoc for relames
Group:          Development/Documentation

%description relames-javadoc
%{summary}.

%package rngconv
Summary:        rngconv
Group:          Development/Java
Requires: isorelax
Requires: jpackage-utils
Requires: relaxngDatatype
Requires: xerces-j2
Requires: xml-commons-jaxp-1.3-apis
Requires: msv-msv
Requires: msv-xsdlib

%description rngconv
%{summary}.

%package xmlgen
Summary:        xmlgen
Group:          Development/Java
Requires: isorelax
Requires: jpackage-utils
Requires: relaxngDatatype
Requires: xml-commons-jaxp-1.3-apis
Requires: xerces-j2
Requires: msv-msv
Requires: msv-xsdlib

%description xmlgen
%{summary}.

%package xmlgen-javadoc
Summary:        Javadoc for xmlgen
Group:          Development/Documentation

%description xmlgen-javadoc
%{summary}.

%package xsdlib
Summary:        xsdlib
Group:          Development/Java
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jpackage-utils
Requires: relaxngDatatype
Obsoletes:      xsdlib < %{epoch}:%{version}-%{release}
Provides:       xsdlib = %{epoch}:%{version}-%{release}

%description xsdlib
%{summary}.

 Sun XML Datatypes Library. An implementation of W3C XML Schema Part 2.

%package xsdlib-javadoc
Summary:        Javadoc for xsdlib
Group:          Development/Documentation
Obsoletes:      xsdlib-javadoc < %{epoch}:%{version}-%{release}
Provides:       xsdlib-javadoc = %{epoch}:%{version}-%{release}

%description xsdlib-javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n %{name}-%{cvsversion}
# remove all binary libs
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}
# delete Class-Path: from manifests
for m in `%{_bindir}/find -type f -name MANIFEST.MF`; do
    sed -i -e '/^Class-[Pp]ath:/d' $m
done

for f in `%{_bindir}/find -type f -name copyright.txt`; do
    %{__mv} ${f} ${f}.orig
    %{_bindir}/iconv -f iso8859-1 -t utf8 -o ${f} ${f}.orig
    %{__rm} ${f}.orig
done

%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
%patch4 -b .sav
%patch5 -b .sav

pushd shared/lib
ln -s $(build-classpath ant) ant.jar
#ln -s $(build-classpath crimson) crimson.jar
#ln -s $(build-classpath dom4j) dom4j.jar
ln -s $(build-classpath isorelax) isorelax.jar
ln -s $(build-classpath junit) junit.jar
ln -s $(build-classpath relaxngDatatype) relaxngDatatype.jar
# FIXME The following doesn't seem to cause resolver to be found
ln -s $(build-classpath xml-commons-resolver11) resolver.jar
%if %without bootstrap
ln -s $(build-classpath jdom) jdom.jar
ln -s $(build-classpath saxon) saxon.jar
%endif
ln -s $(build-classpath servletapi5) servlet.jar
# FIXME The following doesn't seem to cause xalan to be found
ln -s $(build-classpath xalan-j2) xalan.jar
ln -s $(build-classpath xerces-j2) xercesImpl.jar
ln -s $(build-classpath xml-commons-jaxp-1.3-apis) xmlParserAPIs.jar
popd

%build
export CLASSPATH=$(%{_bindir}/build-classpath xalan-j2 xml-commons-resolver11)
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=first release

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}

install -p -m 644 package/msv.jar \
  %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} 
ln -s msv-%{version}.jar msv-msv-%{version}.jar
)
install -p -m 644 package/relames.jar \
  %{buildroot}%{_javadir}/%{name}-relames-%{version}.jar
install -p -m 644 package/rngconv.jar \
  %{buildroot}%{_javadir}/%{name}-rngconv-%{version}.jar
install -p -m 644 package/xmlgen.jar \
  %{buildroot}%{_javadir}/%{name}-xmlgen-%{version}.jar
install -p -m 644 package/xsdlib.jar \
  %{buildroot}%{_javadir}/%{name}-xsdlib-%{version}.jar
(cd %{buildroot}%{_javadir} 
ln -s msv-%{version}.jar msv-strict-%{version}.jar
ln -s msv-xsdlib-%{version}.jar xsdlib-%{version}.jar
)
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -s ${jar} `echo $jar | sed "s|-%{version}||g"`; done)

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap msv msv %{cvsversion} JPP %{name}
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-xsdlib.pom
%add_to_maven_depmap msv xsdlib %{cvsversion} JPP %{name}-xsdlib

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}/msv
cp -pr msv/dist/javadoc/* \
                %{buildroot}%{_javadocdir}/%{name}-%{version}/msv
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}/relames
cp -pr relames/dist/javadoc/* \
                %{buildroot}%{_javadocdir}/%{name}-%{version}/relames
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}/xmlgen
cp -pr generator/dist/javadoc/* \
                %{buildroot}%{_javadocdir}/%{name}-%{version}/xmlgen
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}/xsdlib
cp -pr xsdlib/dist/javadoc/* \
                %{buildroot}%{_javadocdir}/%{name}-%{version}/xsdlib
(cd %{buildroot}%{_javadocdir}
ln -s %{name}-%{version}/msv %{name}-msv
ln -s %{name}-%{version}/relames %{name}-relames
ln -s %{name}-%{version}/xsdlib %{name}-xsdlib
)

# docs
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}/msv
install -p -m 644 msv/doc/* \
                  %{buildroot}%{_docdir}/%{name}-%{version}/msv
rm %{buildroot}%{_docdir}/%{name}-%{version}/msv/Apache-LICENSE-1.1.txt
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}/relames
install -p -m 644 relames/doc/* \
                  %{buildroot}%{_docdir}/%{name}-%{version}/relames
rm %{buildroot}%{_docdir}/%{name}-%{version}/relames/Apache-LICENSE-1.1.txt
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}/rngconv
install -p -m 644 rngconverter/doc/* \
                  %{buildroot}%{_docdir}/%{name}-%{version}/rngconv
rm %{buildroot}%{_docdir}/%{name}-%{version}/rngconv/Apache-LICENSE-1.1.txt
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}/xmlgen
install -p -m 644 generator/doc/* \
                  %{buildroot}%{_docdir}/%{name}-%{version}/xmlgen
rm %{buildroot}%{_docdir}/%{name}-%{version}/xmlgen/Apache-LICENSE-1.1.txt
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}/xsdlib
install -p -m 644 xsdlib/doc/* \
                  %{buildroot}%{_docdir}/%{name}-%{version}/xsdlib
rm %{buildroot}%{_docdir}/%{name}-%{version}/xsdlib/Apache-LICENSE-1.1.txt

#examples
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/msv
cp -pr msv/dist/examples/* %{buildroot}%{_datadir}/%{name}-%{version}/msv
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/xsdlib
cp -pr xsdlib/dist/examples/* %{buildroot}%{_datadir}/%{name}-%{version}/xsdlib

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %dir %{_docdir}/%{name}-%{version}
%doc %dir %{_docdir}/%{name}-%{version}/msv
%doc %{_docdir}/%{name}-%{version}/msv/license.txt
%doc %{_docdir}/%{name}-%{version}/msv/copyright.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-msv-%{version}.jar
%{_javadir}/%{name}-msv.jar
%{_javadir}/msv-strict-%{version}.jar
%{_javadir}/msv-strict.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-msv*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/msv
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/msv
%{_javadocdir}/%{name}-msv

%files demo
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/msv
%{_datadir}/%{name}-%{version}/xsdlib

%files relames
%doc %dir %{_docdir}/%{name}-%{version}
%doc %dir %{_docdir}/%{name}-%{version}/relames
#%doc %{_docdir}/%{name}-%{version}/relames/license.txt
%doc %{_docdir}/%{name}-%{version}/relames/copyright.txt
%{_javadir}/%{name}-relames-%{version}.jar
%{_javadir}/%{name}-relames.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-relames*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/relames
%doc %dir %{_docdir}/%{name}-%{version}

%files relames-javadoc
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/relames
%{_javadocdir}/%{name}-relames

%files rngconv
%doc %dir %{_docdir}/%{name}-%{version}
%doc %dir %{_docdir}/%{name}-%{version}/rngconv
%doc %{_docdir}/%{name}-%{version}/rngconv/license.txt
%doc %{_docdir}/%{name}-%{version}/rngconv/copyright.txt
%{_javadir}/%{name}-rngconv-%{version}.jar
%{_javadir}/%{name}-rngconv.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-rngconv*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/rngconv
%doc %dir %{_docdir}/%{name}-%{version}

%files xmlgen
%doc %dir %{_docdir}/%{name}-%{version}
%doc %dir %{_docdir}/%{name}-%{version}/xmlgen
%doc %{_docdir}/%{name}-%{version}/xmlgen/license.txt
%doc %{_docdir}/%{name}-%{version}/xmlgen/copyright.txt
%{_javadir}/%{name}-xmlgen-%{version}.jar
%{_javadir}/%{name}-xmlgen.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-xmlgen*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}
%doc %dir %{_docdir}/%{name}-%{version}/xmlgen

%files xmlgen-javadoc
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/xmlgen

%files xsdlib
%doc %dir %{_docdir}/%{name}-%{version}
%doc %dir %{_docdir}/%{name}-%{version}/xsdlib
%doc %{_docdir}/%{name}-%{version}/xsdlib/license.txt
%doc %{_docdir}/%{name}-%{version}/xsdlib/copyright.txt
%{_javadir}/%{name}-xsdlib-%{version}.jar
%{_javadir}/%{name}-xsdlib.jar
%{_javadir}/xsdlib-%{version}.jar
%{_javadir}/xsdlib.jar
%{_datadir}/maven2/poms/JPP-%{name}-xsdlib.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-xsdlib*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/xsdlib
%doc %dir %{_docdir}/%{name}-%{version}

%files xsdlib-javadoc
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/xsdlib
%{_javadocdir}/%{name}-xsdlib

%files manual
%doc %dir %{_docdir}/%{name}-%{version}
%doc %dir %{_docdir}/%{name}-%{version}/msv
%doc %dir %{_docdir}/%{name}-%{version}/relames
%doc %dir %{_docdir}/%{name}-%{version}/rngconv
%doc %dir %{_docdir}/%{name}-%{version}/xmlgen
%doc %dir %{_docdir}/%{name}-%{version}/xsdlib
%doc %{_docdir}/%{name}-%{version}/msv/ChangeLog.txt
%doc %{_docdir}/%{name}-%{version}/msv/*.html
%doc %{_docdir}/%{name}-%{version}/msv/*.gif
%doc %{_docdir}/%{name}-%{version}/msv/README.txt
%doc %{_docdir}/%{name}-%{version}/relames/README.txt
%doc %{_docdir}/%{name}-%{version}/rngconv/README.txt
%doc %{_docdir}/%{name}-%{version}/xmlgen/*.html
%doc %{_docdir}/%{name}-%{version}/xmlgen/README.txt
%doc %{_docdir}/%{name}-%{version}/xsdlib/*.html
%doc %{_docdir}/%{name}-%{version}/xsdlib/README.txt
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/relames
%doc %dir %{_docdir}/%{name}-%{version}/xsdlib
%doc %dir %{_docdir}/%{name}-%{version}/rngconv
%doc %dir %{_docdir}/%{name}-%{version}/msv
%doc %dir %{_docdir}/%{name}-%{version}/xmlgen
%doc %dir %{_docdir}/%{name}-%{version}

%changelog
* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt4_0.20050722.7jpp6
- ant 18 support; added description (closes: #22125)

* Sun Jan 11 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt4_0.20050722.6jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_0.20050722.6jpp5
- fixed docdir ownership

* Fri Sep 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_0.20050722.6jpp5
- converted from JPackage by jppimport script

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_0.20050722.6jpp5
- converted from JPackage by jppimport script

* Sun Jul 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_0.20050722.3jpp1.7
- build without bootstrap

* Sat Apr 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1_0.20050722.3jpp1.7
- converted from JPackage by jppimport script

* Mon Apr 25 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2-alt0.1
- Initial build for ALT Linux Sisyphus
- cvs version 20050424
