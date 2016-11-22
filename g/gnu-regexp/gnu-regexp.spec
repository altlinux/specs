Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
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

Name:           gnu-regexp
Version:        1.1.4
Release:        alt1_21jpp8
Summary:        Java NFA regular expression engine implementation
# GPLv2+: gnu/regexp/util/Egrep.java
#         gnu/regexp/util/Grep.java
#         gnu/regexp/util/REApplet.java
# Public Domain: gnu/regexp/util/RETest.java
#                gnu/regexp/util/Tests.java
# Rest is LGPLv2+
# Note files under GPLv2+ and Public Domain are included in -demo subpackage
License:        LGPLv2+
Source0:        http://ftp.frugalware.org/pub/other/sources/gnu.regexp/gnu.regexp-1.1.4.tar.gz
Source1:        %{name}.build.xml
BuildRequires:  ant
BuildRequires:  gnu-getopt
URL:            http://savannah.gnu.org/projects/gnu-regexp
BuildArch:      noarch
Provides:       gnu.regexp = %{version}-%{release}
Obsoletes:      gnu.regexp < %{version}-%{release}
Source44: import.info

%description
The gnu.regexp package is a pure-Java implementation of a traditional
(non-POSIX) NFA regular expression engine. Its syntax can emulate many
popular development tools, including awk, sed, emacs, perl and grep. For
a relatively complete list of supported and non-supported syntax, refer
to the syntax and usage notes.

%package demo
Group: Development/Java
Summary:        Demo for %{name}
License:        LGPLv2+ and GPLv2+ and Public Domain
Requires:       %{name} = %{version}
Requires:       gnu-getopt
Provides:       gnu.regexp-demo = %{version}-%{release}
Obsoletes:      gnu.regexp-demo < %{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
License:        LGPLv2+ and GPLv2+ and Public Domain
Provides:       gnu.regexp-javadoc = %{version}-%{release}
Obsoletes:      gnu.regexp-javadoc < %{version}-%{release}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n gnu.regexp-%{version}
cp %{SOURCE1} build.xml

%build
export CLASSPATH=$(build-classpath gnu-getopt)
ant jar javadoc

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 build/lib/gnu.regexp.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/gnu.regexp.jar

# demo
install -d -m 755 %{buildroot}%{_datadir}/%{name}/gnu/regexp/util
install -p -m 644 build/classes/gnu/regexp/util/*.class \
  %{buildroot}%{_datadir}/%{name}/gnu/regexp/util

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp build/api/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc COPYING COPYING.LIB README TODO docs/*.html
%{_javadir}/*

%files demo
%{_datadir}/%{name}

%files javadoc
%doc COPYING COPYING.LIB
%doc %{_javadocdir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_21jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_20jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_18jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_17jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_16jpp7
- fc update

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_14jpp6
- new jpp release

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_13jpp5
- new jpackage release

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_10jpp1.7
- converted from JPackage by jppimport script

* Sat Apr 23 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1.4-alt1
- Initial build for ALT Linux Sisyphus

