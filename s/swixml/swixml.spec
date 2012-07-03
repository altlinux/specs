BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2011, JPackage Project
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



Name:           swixml
Summary:        SwiXml GUI generating engine
Url:            http://www.swixml.org/
Version:        1.5
Release:        alt1_0.b149.3jpp6
Epoch:          0
License:        BSD
Group:          Development/Java
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source0:        http://www.swixml.org/swixml_149.zip
Source1:        swixml-1.5.149.pom
Patch0:         swixml-1.5-MacApp.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
BuildRequires: java2html
BuildRequires: jdom
Requires: jdom
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
SwiXml, is a small GUI generating engine for Java 
applications and applets. Graphical User Interfaces 
are described in XML documents that are parsed at 
runtime and rendered into javax.swing objects. 
Depending on the application, XML descriptors may 
be deployed with the remaining code or loaded from 
a remote server at runtime. This late binding of the 
GUI has many advantages. Enabling features in an 
application based on a license code or a user's role 
does not have to be hard coded anymore. Instead an 
XML document describing the application's GUI could 
be dynamically loaded.
Generating the GUI based on descriptors also has some 
of the advantages that code generators provide, but 
without generating the none-maintainable code. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
Documents for %{name}.

%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation

%description demo
Samples for %{name}.

%prep
%setup -q -n %{name}_149
chmod -R go=u-w *
find . -name "*.jar" -exec rm -f {} \;
rm src/org/swixml/MacApp.java

%patch0 -b .sav0

%build
export CLASSPATH=$(build-classpath java2html jdom)
ant  -Dbuild.sysclasspath=first package javadoc

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
%add_to_maven_depmap org.swixml %{name} %{version}.149 JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# examples
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/samples
cp -pr samples/* $RPM_BUILD_ROOT%{_datadir}/%{name}/samples
cp -p *.txt $RPM_BUILD_ROOT%{_datadir}/%{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html
cp -pr build/html/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/tagdocs
cp -pr build/tagdocs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/tagdocs

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.txt
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%files demo
%{_docdir}/%{name}-%{version}
%{_datadir}/%{name}/samples

%changelog
* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_0.b149.3jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_0.b149.2jpp5
- new jpackage release

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_0.b144.1jpp1.7
- converted from JPackage by jppimport script

