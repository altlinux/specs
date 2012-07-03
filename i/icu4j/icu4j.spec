AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
# required for install
BuildRequires: unzip
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

%global with_eclipse 1

%global section free

%global eclipse_base            %{_libdir}/eclipse
# Note:  this next section looks weird having an arch specified in a
# noarch specfile but the parts of the build
# All arches line up between Eclipse and Linux kernel names except i386 -> x86
%ifarch %{ix86}
%global eclipse_arch    x86
%else
%global eclipse_arch   %{_arch}
%endif

Name:           icu4j
Version:        4.4.2
Release:        alt1_2jpp6
Epoch:          1
Summary:        International Components for Unicode for Java
License:        MIT and EPL 
URL:            http://site.icu-project.org/
Group:          Development/Java
#http://source.icu-project.org/repos/icu/icu4j/tags/release-4-4-2-eclipse37-20110208/ icu4j-4.4.2
#tar caf icu4j-4.4.2.tar.xz icu4j-4.4.2/
Source0:        icu4j-4.4.2.tar.xz
Source1:        %{name}-4.4.2.pom

Patch0:         %{name}-crosslink.patch
BuildRequires:  ant >= 1.7.0
# FIXME:  is this necessary or is it just adding strings in the hrefs in
# the docs?
BuildRequires:  java-javadoc
# This is to ensure we get OpenJDK and not GCJ
BuildRequires:  jpackage-utils >= 0:1.5
Requires:       jpackage-utils
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
# This is to ensure we get OpenJDK and not GCJ
%if %{with_eclipse}
BuildRequires:  eclipse-pde >= 0:3.2.1
%global         debug_package %{nil}
%else
BuildArch:      noarch
%endif
Source44: import.info
%define java_bin %_jvmdir/java/bin

%description
The International Components for Unicode (ICU) library provides robust and
full-featured Unicode services on a wide variety of platforms. ICU supports
the most current version of the Unicode standard, and provides support for
supplementary characters (needed for GB 18030 repertoire support).

Java provides a very strong foundation for global programs, and IBM and the
ICU team played a key role in providing globalization technology into Sun's
Java. But because of its long release schedule, Java cannot always keep
up-to-date with evolving standards. The ICU team continues to extend Java's
Unicode and internationalization support, focusing on improving
performance, keeping current with the Unicode standard, and providing
richer APIs, while remaining as compatible as possible with the original
Java text and internationalization API design.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
Requires:       java-javadoc
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%if %{with_eclipse}
%package eclipse
Summary:        Eclipse plugin for %{name}
Group:          Development/Java
Requires:       jpackage-utils

%description eclipse
Eclipse plugin support for %{name}.

%endif

%prep
%setup -q 
#%patch0 -p0

cp %{SOURCE1} .

%{__sed} -i 's/\r//' APIChangeReport.html
%{__sed} -i 's/\r//' readme.html

sed --in-place "s/ .*bootclasspath=.*//g" build.xml
sed --in-place "s/<date datetime=.*when=\"after\"\/>//" build.xml
sed --in-place "/javac1.3/d" build.xml
sed --in-place "s:/usr/lib:%{_libdir}:g" build.xml

%build
%ant -Dicu4j.javac.source=1.5 -Dicu4j.javac.target=1.5 -Dj2se.apidoc=%{_javadocdir}/java jar docs
%if %{with_eclipse}
pushd eclipse-build
  %ant -Dj2se.apidoc=%{_javadocdir}/java -Declipse.home=%{eclipse_base} \
    -Declipse.basews=gtk -Declipse.baseos=linux \
    -Declipse.basearch=%{eclipse_arch} \
    -Declipse.pde.dir=%{eclipse_base}/dropins/sdk/plugins/`ls %{eclipse_base}/dropins/sdk/plugins/|grep org.eclipse.pde.build_`
popd
%endif
  
%install
# jars
%__mkdir_p %{buildroot}%{_javadir}
%__cp -ap %{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -pr doc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %{with_eclipse}
# eclipse
install -d -m755 %{buildroot}/%{eclipse_base}

unzip -qq -d %{buildroot}/%{eclipse_base} eclipse-build/out/projects/ICU4J.com.ibm.icu/com.ibm.icu-com.ibm.icu.zip
%endif

# maven stuff
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
cp %{name}-4.4.2.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap com.ibm.icu %{name} %{version} JPP %{name}

%files
%doc readme.html APIChangeReport.html
%{_javadir}/%{name}*.jar
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*.pom

%files javadoc
%doc %{_javadocdir}/*

%if %{with_eclipse}
%files eclipse
%dir %{_libdir}/eclipse
%dir %{_libdir}/eclipse/features
%dir %{_libdir}/eclipse/plugins
%{_libdir}/eclipse/features/*
%{_libdir}/eclipse/plugins/*
%doc readme.html
%endif

%changelog
* Thu Sep 08 2011 Igor Vlasenko <viy@altlinux.ru> 1:4.4.2-alt1_2jpp6
- update to new release by jppimport

* Mon Feb 28 2011 Igor Vlasenko <viy@altlinux.ru> 1:4.2.1-alt1_1jpp6
- new version

* Mon Jan 25 2010 Igor Vlasenko <viy@altlinux.ru> 1:4.0.1-alt1_3jpp6
- new version

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.8.1-alt1_4jpp6
- new version

* Fri Jul 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.6.1-alt1.6_2jpp5
- build for eclipse 3.3.2

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.6.1-alt1_1.3jpp5.0
- converted from JPackage by jppimport script

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.4.5-alt1_1jpp1.7
- converted from JPackage by jppimport script

