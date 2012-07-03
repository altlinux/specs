Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define oname         wsdl4j

# -----------------------------------------------------------------------------

Summary:        WSDL4J patched
Name:           wsdl4j-jboss4
Version:        1.5.2
Release:	alt1_3jpp5
Epoch:		0
Group:          Development/Java
License:        IBM Common Public License
URL:            http://sourceforge.net/projects/wsdl4j
BuildArch:      noarch
Source0:        wsdl4j-%{version}-src.tar.gz
##cvs -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/wsdl4j login
##cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/wsdl4j export -r wsdl4j-1_5_2 wsdl4j
Patch0:		%{name}-%{version}-jboss4-WSDLReaderImpl.patch
Requires: jaxp_parser_impl
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: junit

%description
The Web Services Description Language for Java Toolkit (WSDL4J) allows the
creation, representation, and manipulation of WSDL documents describing
services.  This codebase will eventually serve as a reference implementation
of the standard created by JSR110.

WSDLReaderImpl patched to add setEntityResolver method.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -b .sav

%build
export OPT_JAR_LIST="ant/ant-junit junit"
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java
ant -Dbuild.compiler=modern compile test javadocs

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}

vjar=$(echo %{name}.jar | sed s+.jar+-%{version}.jar+g)
install -m 644 build/lib/%{oname}.jar $RPM_BUILD_ROOT%{_javadir}/$vjar
pushd $RPM_BUILD_ROOT%{_javadir}
   ln -fs $vjar %{name}.jar
popd

vjar=$(echo qname.jar | sed s+.jar+-%{version}.jar+g)
install -m 644 build/lib/qname.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$vjar
pushd $RPM_BUILD_ROOT%{_javadir}/%{name}
   ln -fs $vjar qname.jar
popd

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files
%doc license.html
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%changelog
* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_3jpp5
- new jpp release

* Tue Dec 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_2jpp1.7
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
