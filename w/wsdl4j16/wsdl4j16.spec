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

%define _with_repolib 1

%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/ibm-wsdl4j/1.6.2-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define uversion        1_6_2


%define name            wsdl4j16

# -----------------------------------------------------------------------------

Summary:        Web Services Description Language Toolkit for Java
Name:           %{name}
Version:        1.6.2
Release:        alt2_1jpp5
Epoch:		    0
Group:          Development/Java
License:        CPL
URL:            http://sourceforge.net/projects/wsdl4j
BuildArch:      noarch
Source0:        wsdl4j-src-%{version}.zip
# http://sourceforge.net/project/downloading.php?group_id=128811&use_mirror=superb-east&filename=wsdl4j-src-1.6.2.zip
Source1:	    wsdl4j-component-info.xml
Requires: jaxp_parser_impl
BuildRequires: jpackage-utils >= 0:1.5
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit
BuildRequires: junit

Provides:       wsdl4j = %{epoch}:%{version}-%{release}

%description
The Web Services Description Language for Java Toolkit (WSDL4J) allows the
creation, representation, and manipulation of WSDL documents describing
services.  This codebase will eventually serve as a reference implementation
of the standard created by JSR110.

%if %{with_repolib}
%package	 repolib
Summary:	 Artifacts to be uploaded to a repository library
Group:	Development/Java

%description	 repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio
%endif

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n wsdl4j-%{uversion}

%if %{with_repolib}
tag=`echo wsdl4j-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{SOURCE1}
%endif

mkdir tmpsrc

%{jar} -cf tmpsrc/wsdl4j-src.jar src

%build
export CLASSPATH=
export OPT_JAR_LIST="ant/ant-junit junit"
# Latest sources don't come with the TCK tests anymore
#ant -Dbuild.compiler=modern compile test javadocs
ant -Ddebug=true -Dbuild.compiler=modern compile javadocs

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/wsdl4j

vjar=$(echo %{name}.jar | sed s+.jar+-%{version}.jar+g)
install -m 644 build/lib/wsdl4j.jar $RPM_BUILD_ROOT%{_javadir}/wsdl4j/$vjar
pushd $RPM_BUILD_ROOT%{_javadir}/wsdl4j
    ln -fs $vjar %{name}.jar
popd

vjar=$(echo qname16.jar | sed s+.jar+-%{version}.jar+g)
install -m 644 build/lib/qname.jar $RPM_BUILD_ROOT%{_javadir}/wsdl4j/$vjar
pushd $RPM_BUILD_ROOT%{_javadir}/wsdl4j
   ln -fs $vjar qname16.jar
popd

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{with_repolib}
	install -d -m 755 $RPM_BUILD_ROOT%{repodir}
	install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
	install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
	install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
	install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
	cp -p $RPM_BUILD_ROOT%{_javadir}/wsdl4j/%{name}.jar $RPM_BUILD_ROOT%{repodirlib}/wsdl4j.jar
    cp tmpsrc/wsdl4j-src.jar $RPM_BUILD_ROOT%{repodirlib}
%endif

%files
%doc license.html
%{_javadir}/wsdl4j*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %{with_repolib}
%files repolib
%{repodir}
%endif

%changelog
* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt2_1jpp5
- version for jbossas

