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


Name:           jsap
Version:        2.1
Release:        alt1_3jpp5
Epoch:          0
Summary:        A Java-based Simple Argument Parser
License:        LGPL
Group:          Development/Java
Source0:        http://prdownloads.sourceforge.net/jsap/JSAP-2.1-src.tar.gz
URL:            http://www.martiansoftware.com/jsap/
Requires: xstream
BuildRequires: xstream-javadoc jpackage-utils >= 0:5.0.0 ant ant-junit /bin/bash
BuildArch:      noarch

%description 
JSAP not only syntactically validates your program's command line
arguments, but it converts those arguments into objects you specify. If you
tell JSAP that one of your parameters is an Integer, for example, and the
user does not provide a String that can be converted to an Integer when
invoking the program, JSAP will throw a ParseException when you have it
parse the command line. If no exception is thrown, you are guaranteed an
Integer when you request that parameter's value from your program. There's
a pretty big (and growing) list of return types suppored by JSAP, including
Integers, Floats, Dates, URLs, and even java.awt.Colors; you can also add
your own in a matter of minutes.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
Manual for %{name}.

%prep
%setup -q -c

%build
mv JSAP-%{version}/* .
export CLASSPATH=%(build-classpath xstream)
ant \
  -Dversion=%{version} \
  -Dj2se.apiurl=%{_javadocdir}/java \
  -Dxstream.apiurl=%{_javadocdir}/xstream/core \
  jar javadoc
mv doc/javadoc .

%install
rm -fr $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/JSAP-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%files
%doc LICENSE.TXT CHANGELOG.TXT
%{_javadir}/*.jar

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%doc doc/*


%changelog
* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_3jpp5
- new jpackage release

* Fri Dec 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

