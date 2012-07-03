# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
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

Name:           jsch
Version:        0.1.48
Release:        alt1_1jpp7
Epoch:          0
Summary:        Pure Java implementation of SSH2
Group:          Development/Java
License:        BSD
URL:            http://www.jcraft.com/jsch/
Source0:        http://download.sourceforge.net/sourceforge/jsch/jsch-%{version}.zip
# wget \
# http://download.eclipse.org/tools/orbit/downloads/drops/R20090825191606/bundles/com.jcraft.jsch_0.1.41.v200903070017.jar
# unzip com.jcraft.jsch_*.jar META-INF/MANIFEST.MF
# mv META-INF/MANIFEST.MF .
# sed -i "/^Name/d" MANIFEST.MF
# sed -i "/^SHA1/d" MANIFEST.MF
# dos2unix MANIFEST.MF
# sed -i "/^$/d" MANIFEST.MF
# unix2dos MANIFEST.MF
Source1:        MANIFEST.MF
Source2:        plugin.properties

BuildRequires:  jpackage-utils >= 0:1.5
BuildRequires:  jzlib >= 0:1.0.5
BuildRequires:  ant
BuildRequires:  zip

BuildArch:      noarch

Requires:       jzlib >= 0:1.0.5
Requires:       jpackage-utils
Source44: import.info

%description
JSch allows you to connect to an sshd server and use port forwarding, 
X11 forwarding, file transfer, etc., and you can integrate its 
functionality into your own Java programs.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.

%package        demo
Summary:        Examples for %{name}
Group:          Development/Java

%description    demo
%{summary}.


%prep
%setup -q

%build
export CLASSPATH=$(build-classpath jzlib)
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 dist javadoc 

# inject the OSGi Manifest
mkdir META-INF
cp %{SOURCE1} META-INF
cp %{SOURCE2} plugin.properties
zip dist/lib/%{name}-*.jar META-INF/MANIFEST.MF
zip dist/lib/%{name}-*.jar plugin.properties

%install
# jars
install -Dpm 644 dist/lib/%{name}-*.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# examples
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%{_javadir}/*.jar
%doc LICENSE.txt

%files javadoc
%doc %{_javadocdir}/%{name}*
%doc LICENSE.txt

%files demo
%doc %{_datadir}/%{name}*
%doc LICENSE.txt


%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.1.48-alt1_1jpp7
- update to new release by jppimport

* Sat Nov 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.1.45-alt1_1jpp6
- update to new release by jppimport

* Sat Oct 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.1.44-alt2_4jpp6
- fixed target

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.1.44-alt1_4jpp6
- update to new release by jppimport

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.1.44-alt1_3jpp6
- update to new release by jppimport

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.1.44-alt1_2jpp6
- new version

* Mon Jan 25 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1.41-alt1_2jpp5
- new version

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1.39-alt1_1.1jpp5
- new version

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1.31-alt1.3_2jpp5
- rebuild with osgi provides

* Mon Nov 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.1.31-alt1_1.2jpp1.7
- build for ALTLinux

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.1.28-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Fri Mar 03 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.25-alt1
- 0.1.25
- Patch0: add source and target attributes to javac

* Wed Oct 05 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.22-alt1
- 0.1.22

* Wed Aug 03 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.21-alt1
- Updated to 0.1.21

* Tue Jan 04 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.18-alt1
- New upstream release
- Use macros provided by rpm-build-java
- Examples packaged

* Mon Sep 20 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.17-alt1
- New upstream release

* Mon Jun 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.15-alt1
- New upstream release

* Sun Mar 28 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.14-alt1
- Package created
