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

%define resolverdir %{_sysconfdir}/java/resolver

Name:           saxon7
Version:        7.9.1
Release:        alt3_6jpp5
Epoch:          0
Summary:        Java XSLT processor
License:        MPL
Group:          Development/Java
URL:            http://saxon.sourceforge.net/
Source0:        http://download.sf.net/saxon/saxon7-9-1.zip
Source1:        %{name}.saxon.script
Source2:        %{name}.build.script
Source3:        %{name}.1
Patch0:         saxon7-java5-enum.patch
Patch1:         saxon7-build.patch
Provides:       jaxp_transform_impl
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires(post): alternatives >= 0:0.4
Requires(preun): alternatives >= 0:0.4
Requires: xml-commons-jaxp-1.1-apis
BuildRequires: ant
BuildRequires: java-javadoc
BuildRequires: jdom >= 0:1.0-0.b7
BuildRequires: jdom-javadoc >= 0:1.0-0.b9.3jpp
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: xml-commons-jaxp-1.1-apis
%if ! %{gcj_support}
%endif
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif

%description
The SAXON package is a collection of tools for processing XML documents.
The main components are:

- An XSLT processor, which implements the Version 1.0 XSLT and XPath
  Recommendations from the World Wide Web Consortium, found at
  http://www.w3.org/TR/1999/REC-xslt-19991116 and
  http://www.w3.org/TR/1999/REC-xpath-19991116 with a number of powerful
  extensions. This version of Saxon also includes many of the new features
  defined in the XSLT 1.1 working draft, but for conformance and portability
  reasons these are not available if the stylesheet header specifies
  version="1.0".

- A Java library, which supports a similar processing model to XSL, but allows
  full programming capability, which you need if you want to perform complex
  processing of the data or to access external services such as a relational
  database.

So you can use SAXON with any SAX-compliant XML parser by writing XSLT
stylesheets, by writing Java applications, or by any combination of the two.

%package manual
Summary:        Manual for %{name}
Group:          Development/Java

%description manual
Manual for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demos for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%package sql
Summary:        SQL support for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description sql
SQL support for %{name}.

%package jdom
Summary:        JDOM support for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jdom >= 0:1.0-0.b7

%description jdom
JDOM support for %{name}.

%package scripts
Summary:        Utility scripts for %{name}
Group:          Development/Java
Requires: jpackage-utils >= 0:1.7.3
Requires: %{name} = %{epoch}:%{version}-%{release}

%description scripts
Utility scripts for %{name}.

%prep
%setup -q -c
mkdir src
(cd src
unzip -qq ../source.zip
find . -type d -name CVS | xargs -t rm -r)
cp -p %{SOURCE2} ./build.xml
# cleanup unnecessary stuff we'll build ourselves
find . -name "*.jar" | xargs -t rm
%patch0 -p1
%patch1 -p1

%build
export CLASSPATH=$(build-classpath jdom)
export OPT_JAR_LIST=:
%{ant}

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p build/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap net.sf.saxon saxon %{version} JPP %{name}

cp -p build/lib/%{name}-sql.jar %{buildroot}%{_javadir}/%{name}-sql-%{version}.jar
%add_to_maven_depmap net.sf.saxon saxon-sql %{version} JPP %{name}-sql
cp -p build/lib/%{name}-jdom.jar %{buildroot}%{_javadir}/%{name}-jdom-%{version}.jar
%add_to_maven_depmap net.sf.saxon saxon-jdom %{version} JPP %{name}-jdom
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# demo
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr samples/* %{buildroot}%{_datadir}/%{name}

# scripts
mkdir -p %{buildroot}%{_bindir}
sed 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE1} \
  > %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
sed 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE3} \
  > %{buildroot}%{_mandir}/man1/%{name}.1

# jaxp_transform_impl ghost symlink
ln -s %{_sysconfdir}/alternatives \
  %{buildroot}%{_javadir}/jaxp_transform_impl.jar
# jaxp_parser_impl ghost symlink
#ln -s %{_sysconfdir}/alternatives \
#  %{buildroot}%{_javadir}/jaxp_parser_impl.jar

# manual
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr doc/*.html %{buildroot}%{_docdir}/%{name}-%{version}/

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxp_transform_impl_%{name}<<EOF
%{_javadir}/jaxp_transform_impl.jar	%{_javadir}/%{name}.jar	25
EOF
chmod 755 $RPM_BUILD_ROOT%{_bindir}/*

%files
%_altdir/jaxp_transform_impl_%{name}
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%exclude %{_javadir}/jaxp_transform_impl.jar
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files sql
%{_javadir}/%{name}-sql*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-sql-%{version}.jar.*
%endif

%files jdom
%{_javadir}/%{name}-jdom*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-jdom-%{version}.jar.*
%endif

%files manual
%doc %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}
%{_javadocdir}/%{name}-%{version}

%files demo
%{_datadir}/%{name}

%files scripts
#%defattr(0755,root,root,0755)
%{_bindir}/%{name}
%attr(0644,root,root) %{_mandir}/man1/%{name}.1*


%changelog
* Tue Mar 17 2009 Igor Vlasenko <viy@altlinux.ru> 0:7.9.1-alt3_6jpp5
- fixed build

