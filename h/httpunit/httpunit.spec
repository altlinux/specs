BuildRequires: /proc  maven-dependency-plugin
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
%define version 1.7
%define name httpunit
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

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/httpunit/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           httpunit
Version:        1.7
Release:        alt2_4jpp6
Epoch:          0
Summary:        Library for testing websites programmatically
License:        MIT
Group:          Development/Java
URL:            http://httpunit.sourceforge.net/
# svn export https://httpunit.svn.sourceforge.net/svnroot/httpunit/tags/httpunit_1_7/httpunit httpunit-1.7 && tar cjf httpunit-1.7.tar.bz2 httpunit-1.7
# Exported revision 1078.
Source0:        httpunit-1.7.tar.bz2
Source1:        httpunit-component-info.xml
Source2:        httpunit-jpp-depmap.xml
Patch0:         httpunit.build.patch
Patch1:         httpunit-JavaScript-NotAFunctionException.patch
Patch2:         httpunit-servlettest.patch
Patch3:         httpunit-no-mojo.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
# 1.6R5
Requires:       rhino >= 0:1.6
Requires:       junit >= 0:3.8.1
Requires:       nekohtml >= 0:0.9.5
Requires:       servlet_2_5_api
# 4aug2000r7-dev
Requires:       jtidy
Requires:       xerces-j2 >= 0:2.6.1
Requires:       xml-commons-jaxp-1.3-apis
#
Requires:       jpackage-utils
# 1.6R5
BuildRequires:  rhino >= 0:1.6
BuildRequires:  junit >= 0:3.8.1
BuildRequires:  nekohtml >= 0:0.9.5
# 2.4
BuildRequires:  servlet_2_5_api
# 4aug2000r7-dev
BuildRequires:  jtidy
BuildRequires:  xerces-j2 >= 0:2.6.1
BuildRequires:  xml-commons-jaxp-1.3-apis
# scope=test
BuildRequires:  javamail_1_4_api
#
BuildRequires:  commons-parent
BuildRequires:  jpackage-utils
BuildRequires:  maven2
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-deploy
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-release
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-jxr
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-surefire-report-maven-plugin
%if 0
BuildRequires:  mojo-maven2-plugin-build-helper
BuildRequires:  mojo-maven2-plugin-cobertura
%endif
BuildArch:      noarch
Source44: import.info
Patch33: httpunit-1.7-alt-jtidy8.patch

%description
HttpUnit emulates the relevant portions of browser behavior, including form
submission, JavaScript, basic http authentication, cookies and automatic page
redirection, and allows Java test code to examine returned pages either as
text, an XML DOM, or containers of forms, tables, and links.
A companion framework, ServletUnit is included in the package.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description manual
Documentation for %{name}.

%package demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q
%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1
%patch2 -p0 -b .sav2
%patch3 -p0 -b .sav3

%{__rm} .cvsignore doc/.cvsignore doc/tutorial/.cvsignore

%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%patch33 -p1

%build
export LANG=en_US.ISO8859-1
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -Dmaven.repo.local=`pwd`/maven2-brew -Dmaven2.jpp.depmap.file=%{SOURCE2} -DaltDeploymentRepository=oss-releases::default::file:`pwd`/maven2-brew -Dmaven.test.failure.ignore install javadoc:aggregate

find maven2-brew \! -path '*/httpunit/httpunit/*' -type f -delete ||:
find maven2-brew \! -path '*/httpunit/httpunit/*' -type d -exec rmdir -p {} \; ||:

%install

%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p target/httpunit-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__cp} -p target/httpunit-%{version}-sources.jar %{buildroot}%{_javadir}/%{name}-%{version}-sources.jar
%{__cp} -p target/httpunit-%{version}-test-sources.jar %{buildroot}%{_javadir}/%{name}-%{version}-test-sources.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*.jar; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap httpunit httpunit %{version} JPP %{name}

%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__cp} -pr examples %{buildroot}%{_datadir}/%{name}

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE1} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE2} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH1} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH2} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH3} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom %{buildroot}%{repodirlib}/httpunit.pom
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/httpunit.jar
%endif

%if %with repolib
%{__mkdir_p} %{buildroot}%{_javadir}/repository.jboss.com
%{__cp} -pr maven2-brew %{buildroot}%{_javadir}/repository.jboss.com
%endif

%files
%{_javadir}*/%{name}-%{version}.jar
%{_javadir}*/%{name}.jar
%{_javadir}*/%{name}-%{version}-sources.jar
%{_javadir}*/%{name}-sources.jar
%{_javadir}*/%{name}-%{version}-test-sources.jar
%{_javadir}*/%{name}-test-sources.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc --no-dereference doc/*

%files demo
%{_datadir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}*
%exclude %dir %{_javadocdir}
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt2_4jpp6
- fixed build with maven3

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_4jpp6
- new jpp relase

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_1jpp5
- new version

* Wed Jul 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

