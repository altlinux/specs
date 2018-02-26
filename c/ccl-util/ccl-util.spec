# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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


Name:           ccl-util
Version:        32.69
Release:        alt4_5jpp6
Epoch:          0
Summary:        Reusable Framework/Utils
License:        GPLv2+
Group:          Development/Java
URL:            http://www.kclee.de/clemens/java/ccl/
Source0:        http://www.kclee.de/clemens/java/ccl/ccl32.69.zip
# based on <http://mirrors.ibiblio.org/pub/mirrors/maven2/javancss/ccl/26.46/ccl-26.46.pom>
Source1:        ccl-32.69.pom
Patch0:         ccl-build_xml.patch
Patch1:         ccl-MainTest.patch
Patch2:         ccl-util-JCFUtil.patch
Patch3:         ccl-util-Test.patch
Patch4:         ccl-util-Util.patch
Patch5:         ccl-util-servlet.patch
Provides:       ccl = %{epoch}:%{version}-%{release}
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       gif89encoder
Requires:       javahelp2
Requires:       jpackage-utils
Requires:       servlet_2_5_api
BuildRequires:  jpackage-utils
BuildRequires:  javahelp2
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  gif89encoder
BuildRequires:  junit
BuildRequires:  servlet_2_5_api
BuildArch:      noarch
Source44: import.info

%description
Features
* Basic GUI/Swing application framework and utility classes
* Additional string methods
* Vector methods
* File methods
* Debug and assertion support
* Test framework

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n ccl%{version}
%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1
%patch2 -p0 -b .sav2
%patch3 -p0 -b .sav3
%patch4 -p0 -b .sav4
%patch5 -p0 -b .sav5

%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t rm
%{_bindir}/find -type f -name "*~" | %{_bindir}/xargs -t rm
%{_bindir}/find -type d -name .xvpics | %{_bindir}/xargs -t rm -r

%if 0
rm -r doc/guiexample
rm -r src/ccl/swing
%endif
rm -r src/junit

pushd lib
ln -s $(build-classpath gif89encoder) .
ln -s $(build-classpath javahelp2) jhbasic.jar
ln -s $(build-classpath junit) ccljunit.jar
ln -s $(build-classpath servlet_2_5_api) servlet.jar
popd

%build
export OPT_JAR_LIST=:
export CLASSPATH=
ant -Dant.build.javac.source=1.3 -Dant.build.javac.target=1.3 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 
pushd classes
%{jar} cf ../lib/ccl.jar *
popd

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p lib/ccl.jar %{buildroot}%{_javadir}/ccl-%{version}.jar
ln -s ccl-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -s ${jar} `echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# pom
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

# depmaps
%add_to_maven_depmap javancss ccl %{version} JPP %{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr doc/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# manual
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr doc/* %{buildroot}%{_docdir}/%{name}-%{version}
cp -p README.TXT %{buildroot}%{_docdir}/%{name}-%{version}
rm -r %{buildroot}%{_docdir}/%{name}-%{version}/api

%files
%doc README.TXT
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/ccl-%{version}.jar
%{_javadir}/ccl.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:32.69-alt4_5jpp6
- built with java 6 due to com.sun.image.codec.jpeg

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:32.69-alt3_5jpp6
- new jpp relase

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:32.69-alt3_3jpp5
- new jpp release

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:32.69-alt3_2jpp5
- fixed repocop warnings

* Fri Oct 17 2008 Igor Vlasenko <viy@altlinux.ru> 0:32.69-alt2_2jpp5
- fixed build with 5.0

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:32.69-alt1_2jpp1.7
- converted from JPackage by jppimport script

