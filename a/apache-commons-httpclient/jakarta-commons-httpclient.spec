# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%define oldname jakarta-commons-httpclient
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2007, JPackage Project
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

%global short_name httpclient

Name:           apache-commons-httpclient
Version:        3.1
Release:        alt6_13jpp7
Epoch:          1
Summary: Jakarta Commons HTTPClient implements the client side of HTTP standards
License:        ASL 2.0 and (ASL 2.0 or LGPLv2+)
Source0:        http://archive.apache.org/dist/httpcomponents/commons-httpclient/source/commons-httpclient-3.1-src.tar.gz
Source1:        http://repo.maven.apache.org/maven2/commons-httpclient/commons-httpclient/%{version}/commons-httpclient-%{version}.pom
Patch0:         %{oldname}-disablecryptotests.patch
# Add OSGi MANIFEST.MF bits
Patch1:         %{oldname}-addosgimanifest.patch
Patch2:         %{oldname}-encoding.patch
# CVE-2012-5783: missing connection hostname check against X.509 certificate name
# https://fisheye6.atlassian.com/changelog/httpcomponents?cs=1422573
Patch3:         %{oldname}-CVE-2012-5783.patch
URL:            http://jakarta.apache.org/commons/httpclient/
Group:          Development/Java
BuildArch:      noarch

BuildRequires:  jpackage-utils >= 0:1.5
BuildRequires:  ant
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-logging >= 0:1.0.3
#BuildRequires:  java-javadoc
BuildRequires:  apache-commons-logging-javadoc
BuildRequires:  junit

Requires:       jpackage-utils
Requires:       apache-commons-logging >= 0:1.0.3
Requires:       apache-commons-codec

Provides:       commons-httpclient = %{epoch}:%{version}-%{release}
Obsoletes:      commons-httpclient < %{epoch}:%{version}-%{release}
Provides:       jakarta-commons-httpclient3 = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-commons-httpclient3 < %{epoch}:%{version}-%{release}
Source44: import.info
# jpackage compat
Provides:       jakarta-commons-httpclient = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-commons-httpclient < %{epoch}:%{version}-%{release}

%description
The Hyper-Text Transfer Protocol (HTTP) is perhaps the most significant
protocol used on the Internet today. Web services, network-enabled
appliances and the growth of network computing continue to expand the
role of the HTTP protocol beyond user-driven web browsers, and increase
the number of applications that may require HTTP support.
Although the java.net package provides basic support for accessing
resources via HTTP, it doesn't provide the full flexibility or
functionality needed by many applications. The Jakarta Commons HTTP
Client component seeks to fill this void by providing an efficient,
up-to-date, and feature-rich package implementing the client side of the
most recent HTTP standards and recommendations.
Designed for extension while providing robust support for the base HTTP
protocol, the HTTP Client component may be of interest to anyone
building HTTP-aware client applications such as web browsers, web
service clients, or systems that leverage or extend the HTTP protocol
for distributed communication.

%package        javadoc
Summary:        Javadoc for %{oldname}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.

%package        demo
Summary:        Demos for %{oldname}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    demo
%{summary}.

%package        manual
Summary:        Manual for %{oldname}
Group:          Development/Java
Requires:       %{name}-javadoc = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description    manual
%{summary}.


%prep
%setup -q -n commons-httpclient-%{version}
mkdir lib # duh
rm -rf docs/apidocs docs/*.patch docs/*.orig docs/*.rej

%patch0

pushd src/conf
%{__sed} -i 's/\r//' MANIFEST.MF
%patch1
popd

%patch2
%patch3 -p2

# Use javax classes, not com.sun ones
# assume no filename contains spaces
pushd src
    for j in $(find . -name "*.java" -exec grep -l 'com\.sun\.net\.ssl' {} \;); do
        sed -e 's|com\.sun\.net\.ssl|javax.net.ssl|' $j > tempf
        cp tempf $j
    done
    rm tempf
popd

%build
ant \
  -Dbuild.sysclasspath=first \
  -Djavadoc.j2sdk.link=%{_javadocdir}/java \
  -Djavadoc.logging.link=%{_javadocdir}/jakarta-commons-logging \
  -Dtest.failonerror=false \
  -Dlib.dir=%{_javadir} \
  -Djavac.encoding=UTF-8 \
  dist test


%install
# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/commons-httpclient.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{oldname}.jar
# compat symlink
pushd $RPM_BUILD_ROOT%{_javadir}
ln -s jakarta-commons-httpclient.jar commons-httpclient3.jar
ln -s jakarta-commons-httpclient.jar commons-httpclient.jar
popd

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
mv dist/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{oldname}
cp -pr src/examples src/contrib $RPM_BUILD_ROOT%{_datadir}/%{oldname}

# manual and docs
rm -f dist/docs/{BUILDING,TESTING}.txt

# maven POM and depmap
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{oldname}.pom
%add_maven_depmap JPP-%{oldname}.pom %{oldname}.jar
# jpp compat
#ln -sf %{name}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}.jar

%files
%doc LICENSE NOTICE
%doc README RELEASE_NOTES
%{_javadir}/%{oldname}.jar
%{_javadir}/commons-httpclient3.jar
%{_javadir}/commons-httpclient.jar
%{_mavenpomdir}/JPP-%{oldname}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%doc %{_javadocdir}/%{oldname}

%files demo
%{_datadir}/%{oldname}

%files manual
%doc dist/docs/*


%changelog
* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt6_13jpp7
- updated provides

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt5_13jpp7
- update

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt5_6jpp6
- fixed build with java 7

* Fri Jul 22 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt4_6jpp6
- disabled tests thank to new hasher

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt3_6jpp6
- renamed to apache-commons-httpclient

* Sun Jan 09 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt3_1jpp6
- added OSGi manifest

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt2_1jpp6
- jpackage 6.0

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt2_1jpp6
- new version

* Mon Jan 12 2009 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt2_0.3jpp5
- updated OSGi manifest

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt1.1_0jpp5
- rebuild with osgi provides

* Thu Dec 06 2007 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt2.2_1jpp1.7
- added eclipse manifest

* Thu Aug 02 2007 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Fri May 04 2007 Igor Vlasenko <viy@altlinux.ru> 3.0-alt2
- added jpackage compat symlinks

* Tue Dec 20 2005 Vladimir Lettiev <crux@altlinux.ru> 3.0-alt1
- Final release 3.0

* Sat Jul 02 2005 Vladimir Lettiev <crux@altlinux.ru> 3.0-alt0.3
- 3.0-rc3
- manual package is back
- changed rpmgroup for packages with documentation

* Tue Mar 22 2005 Vladimir Lettiev <crux@altlinux.ru> 3.0-alt0.2
- rpm-build-java macroces
- 3.0-beta1 (cvs 20050321)

* Sun Oct 24 2004 Vladimir Lettiev <crux@altlinux.ru> 3.0-alt0.1
- 3.0-dev (cvs 20041024)

* Wed Oct 13 2004 Vladimir Lettiev <crux@altlinux.ru> 2.0.1-alt2
- changes to suit ALT java-policy

* Fri Sep 17 2004 Vladimir Lettiev <crux@altlinux.ru> 2.0.1-alt1
- 2.0.1
- Rebuild for ALT Linux Sisyphus
- spec cleanup

