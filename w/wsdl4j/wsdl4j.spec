AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
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

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'

%define _with_repolib 1

%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/ibm-wsdl4j/1.6.2-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0

%define cvs_version     1_6_2

Name:           wsdl4j
Version:        1.6.2
Release:        alt4_7jpp6
Epoch:          0
Summary:        Web Services Description Language Toolkit for Java
Group:          Development/Java
License:        CPL
URL:            http://sourceforge.net/projects/wsdl4j/
%if ! %{gcj_support}
BuildArch:      noarch
%endif
# cvs -d:pserver:anonymous@wsdl4j.cvs.sourceforge.net:/cvsroot/wsdl4j login 
# cvs -z3 -d:pserver:anonymous@wsdl4j.cvs.sourceforge.net:/cvsroot/wsdl4j export -r wsdl4j-1_6_2 wsdl4j 
Source0:        wsdl4j-%{version}-src.tar.gz
Source1:        wsdl4j-%{version}.pom
Source2:        wsdl4j-component-info.xml
BuildRequires: ant >= 0:1.7.1
BuildRequires: ant-junit
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: junit
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info
Source45: wsdl4j-1.5.2.jar-OSGi-MANIFEST.MF

%description
The Web Services Description Language for Java Toolkit (WSDL4J) allows the
creation, representation, and manipulation of WSDL documents describing
services.  This codebase will eventually serve as a reference implementation
of the standard created by JSR110.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%if %{with_repolib}
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n %{name}
find . -name '*.jar' | xargs -t %{__rm}

mkdir tmpsrc
%{jar} -cf tmpsrc/%{name}-src.jar src

%build
export CLASSPATH=
export OPT_JAR_LIST="ant/ant-junit junit"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Ddebug=true -Dbuild.compiler=modern compile test javadocs

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 build/lib/%{name}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 build/lib/qname.jar \
      $RPM_BUILD_ROOT%{_javadir}/wsdl-qname-%{version}.jar
touch $RPM_BUILD_ROOT%{_javadir}/qname.jar # for %ghost

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

%add_to_maven_depmap wsdl4j wsdl4j %{version} JPP wsdl4j

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.wsdl4j.pom

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{with_repolib}
        install -d -m 755 $RPM_BUILD_ROOT%{repodir}
        install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
        install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{repodir}/component-info.xml
        sed -i "s/@VERSION@/%{version}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
        tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
        sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
        install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
        install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
        cp -p $RPM_BUILD_ROOT%{_javadir}/wsdl4j.jar $RPM_BUILD_ROOT%{repodirlib}
        cp -p tmpsrc/%{name}-src.jar $RPM_BUILD_ROOT%{repodirlib}
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/qname_wsdl4j<<EOF
%{_javadir}/qname.jar	%{_javadir}/wsdl-qname.jar	00100
EOF

# inject OSGi manifest wsdl4j-1.5.2.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE45} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/wsdl4j.jar META-INF/MANIFEST.MF
# end inject OSGi manifest wsdl4j-1.5.2.jar-OSGi-MANIFEST.MF

%files
%_altdir/qname_wsdl4j
%doc license.html
%exclude %{_javadir}/qname.jar
%{_javadir}/wsdl-qname-%{version}.jar
%{_javadir}/wsdl-qname.jar
%{_javadir}/wsdl-qname.jar
%{_javadir}/wsdl4j-%{version}.jar
%{_javadir}/wsdl4j.jar
%{_datadir}/maven2/poms/*
%config(noreplace) %{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%{_libdir}/gcj/%{name}/qname-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt4_7jpp6
- jpp 6 release

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt4_5jpp6
- fixed OSGi provides

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt3_5jpp6
- added OSGi provides

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt2_6jpp5
- new jpp release

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt2_4jpp5
- alternatives 0.4

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt2_3jpp5
- converted from JPackage by jppimport script

* Thu Dec 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt2_2jpp1.7
- removed ghost jar

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_2jpp1.7
- updated to new jpackage release

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_4jpp1.7
- converted from JPackage by jppimport script

* Thu Mar 24 2005 Vladimir Lettiev <crux@altlinux.ru> 1.5-alt1
- 1.5
- rpm-build-java macroces

* Fri Sep 24 2004 Vladimir Lettiev <crux@altlinux.ru> 1.4-alt2
- corrected requires (xerces-j -> jaxp_parser_impl)

* Fri Sep 17 2004 Vladimir Lettiev <crux@altlinux.ru> 1.4-alt1
- Rebuild for ALT Linux Sisyphus
- spec cleanup

* Mon Aug 30 2004 Ralph Apel <r.apel at r-apel.de> 0:1.4-3jpp
- Build with ant-1.6.2

* Thu Jun 26 2003 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net> 0:1.4-2jpp
- Do not drop qname.jar

* Tue May 06 2003 David Walluck <david@anti-microsoft.org> 0:1.4-1jpp
- 1.4
- update for JPackage 1.5

* Sat Sep  7 2002 Ville Skyttä <ville.skytta at iki.fi> 1.1-1jpp
- First JPackage release.
