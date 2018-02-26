BuildRequires: /proc
BuildRequires: jpackage-compat
# one of the sources is a zip file
BuildRequires: unzip
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

%define resolverdir %{_sysconfdir}/java/resolver

Summary:        Java XSLT processor
Name:           saxon
Version:        6.5.5
Release:        alt2_3jpp6
Epoch:          0
License:        MPL
Group:          Development/Java
URL:            http://saxon.sourceforge.net/
Source0:        http://download.sf.net/saxon/saxon6-5-5.zip
Source1:        %{name}.saxon.script
Source2:        %{name}.build.script
Source3:        %{name}.1
Source4:        %{name}-%{version}.pom
Source5:        %{name}-aelfred-%{version}.pom
Source6:        %{name}-jdom-%{version}.pom

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: jdom >= 0:1.1
BuildRequires: ant
Requires: jpackage-utils >= 0:1.7.5
Requires: jdom >= 0:1.1

Requires: alternatives >= 0:0.4
Provides:       jaxp_transform_impl
BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Source44: import.info

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

%package        aelfred
Summary:        Java XML parser
Group:          Development/Java

%description    aelfred
A slightly improved version of the AElfred Java XML parser from Microstar.

%package        manual
Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description    manual
%{summary}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildRequires: java-javadoc
BuildRequires: jdom-javadoc
Requires: java-javadoc
Requires: jdom-javadoc
BuildArch: noarch

%description    javadoc
%{summary}.

%package        demo
Summary:        Demos for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description    demo
%{summary}.

%package        jdom
Summary:        JDOM support for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jdom >= 0:1.1

%description    jdom
%{summary}.

%package        scripts
Summary:        Utility scripts for %{name}
Group:          Development/Java
Requires: jpackage-utils >= 0:1.7.5
Requires: %{name} = %{epoch}:%{version}-%{release}

%description    scripts
%{summary}.


%prep
%setup -q -c
unzip -q source.zip
cp -p %{SOURCE2} ./build.xml
# cleanup unnecessary stuff we'll build ourselves
rm -rf *.jar docs/api


%build
export CLASSPATH=%(build-classpath jdom)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
  -Dj2se.javadoc=%{_javadocdir}/java \
  -Djdom.javadoc=%{_javadocdir}/jdom

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

cp -p build/lib/%{name}-aelfred.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-aelfred-%{version}.jar

cp -p build/lib/%{name}-jdom.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-jdom-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do \
    ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE4} \
         $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
install -m 644 %{SOURCE5} \
         $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-aelfred.pom
%add_to_maven_depmap %{name} %{name}-aelfred %{version} JPP %{name}
install -m 644 %{SOURCE6} \
         $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-jdom.pom
%add_to_maven_depmap %{name} %{name}-jdom %{version} JPP %{name}

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr samples/* $RPM_BUILD_ROOT%{_datadir}/%{name}

# scripts
mkdir -p $RPM_BUILD_ROOT%{_bindir}
sed 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE1} \
  > $RPM_BUILD_ROOT%{_bindir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
sed 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE3} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

# jaxp_transform_impl ghost symlink
ln -s %{_sysconfdir}/alternatives \
  $RPM_BUILD_ROOT%{_javadir}/jaxp_transform_impl.jar

# fix newlines in docs
for i in doc/*.html; do
    tr -d \\r < $i > temp_file.html; mv temp_file.html $i
done
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxp_transform_impl_saxon<<EOF
%{_javadir}/jaxp_transform_impl.jar	%{_javadir}/%{name}.jar	25
EOF
chmod 755 $RPM_BUILD_ROOT%{_bindir}/*

%files
%_altdir/jaxp_transform_impl_saxon
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%exclude %{_javadir}/jaxp_transform_impl.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files aelfred
%{_javadir}/%{name}-aelfred*

%files jdom
%{_javadir}/%{name}-jdom*

%files manual
%doc doc/*.html

%files javadoc
%doc %{_javadocdir}/*

%files demo
%{_datadir}/%{name}

%files scripts
#%defattr(0755,root,root,0755)
%{_bindir}/%{name}
%attr(0644,root,root) %{_mandir}/man1/%{name}.1*

%changelog
* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:6.5.5-alt2_3jpp6
- new jpp release

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:6.5.5-alt2_1jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:6.5.5-alt1_1jpp5
- converted from JPackage by jppimport script

* Thu Jul 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:6.5.3-alt2_5jpp1.7
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:6.5.3-alt1_5jpp1.7
- converted from JPackage by jppimport script

