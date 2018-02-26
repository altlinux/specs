Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define gcj_support 0


Name:           adaptx
Version:        0.9.14
Release:        alt1_1jpp5
Epoch:          0
Summary:        AdaptX
License:        Exolab Software License
Group:          Development/Java
Source0:        %{name}-%{version}-src.tar.gz
# svn export http://svn.codehaus.org/castor/adaptx/tags/%{version}

Patch0:         %{name}-%{version}-xsl.patch
Patch1:         %{name}-%{version}-build.patch
Patch2:         %{name}-%{version}-TransformerFactoryImpl.patch

Url:            http://castor.codehaus.org/
BuildRequires: ant >= 0:1.6
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: log4j
BuildRequires: xml-commons-apis
BuildRequires: xerces-j2
Requires: ant >= 0:1.6
Requires: jpackage-utils >= 0:1.7.3
Requires: log4j
Requires: xml-commons-apis
Requires: xerces-j2
%if ! %{gcj_support}
BuildArch: noarch
%endif
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description
Adaptx is an XSLT processor and XPath engine.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package manual
Summary:        Documentation for %{name}
Group:          Development/Documentation
Obsoletes:      adaptx-doc < %{epoch}:%{version}
Provides:       adaptx-doc = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description manual
Documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}-src
# remove CVS internal files
for dir in `find . -type d -name CVS`; do rm -rf $dir; done
# remove all binary libs
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2

%build
perl -p -i -e 's|classic|modern|' src/build.xml
#export CLASSPATH=$(build-classpath js log4j xerces-j2 xml-commons-apis)
export CLASSPATH=$(build-classpath xml-commons-apis log4j xerces-j2)
ant -buildfile src/build.xml jar javadoc
CLASSPATH=$CLASSPATH:dist/adaptx_%{version}.jar
ant -buildfile src/build.xml doc

%install

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.codehaus.castor %{name} %{version} JPP %{name}

# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{name}_%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} ${jar/-%{version}/}; done)
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rm -rf build/doc/javadoc

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc src/etc/contributors.html src/doc/license.txt
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%{_libdir}/gcj/%{name}
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}

%files manual
%doc build/doc/*

%changelog
* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.14-alt1_1jpp5
- new version

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0.9.13-alt1.6_3jpp5
- build fixed; from fedora 9

* Thu May 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.13-alt1_3jpp1.7
- converted from JPackage by jppimport script

