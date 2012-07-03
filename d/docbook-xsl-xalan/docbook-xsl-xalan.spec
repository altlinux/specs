Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: docbook-xsl-java-xalan = 1.67
Obsoletes: docbook-xsl-java-xalan
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

Name:           docbook-xsl-xalan
Version:        1.00
Release:        alt2_0jpp5
Epoch:          0
Summary:        DocBook Xalan Extensions
License:        Artistic
Group:          Development/Java
URL:            http://wiki.docbook.org/topic/DocBookXslStylesheets
Source0:        http://downloads.sourceforge.net/docbook/%name-%version.tar.bz2
Requires: docbook-style-xsl
Requires: xalan-j2 >= 0:2.7
BuildRequires: ant
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: xalan-j2 >= 0:2.7
BuildArch:      noarch

%description
These are Java extensions for use with the DocBook XML stylesheets
and the Xalan XSLT engine.

To use the DocBook Xalan extensions, add the absolute path to the
%{name}.jar file to your Java classpath and process your documents
with the Xalan XSLT engine and with the value of the DocBook XSL
stylesheets "use.extensions" parameter set to 1.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%{__rm} -r classes javadoc
%{__rm} xalan*.jar

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} -Dplatform.active=jpackage -Dplatforms.jpackage.home=%{java_home} -Djavac.classpath=$(build-classpath xalan-j2) -Ddist.jar=%{name}-%{version}.jar -Djar.compress=true

%install

%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS BUGS COPYING INSTALL README VERSION
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Nov 28 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.00-alt2_0jpp5
- fixed description

* Thu Nov 27 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.00-alt1_0jpp5
- first build for Sisyphus
