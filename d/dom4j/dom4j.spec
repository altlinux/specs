Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
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

Summary:        Open Source XML framework for Java
Name:           dom4j
Version:        1.6.1
Release:        alt6_26jpp8
Epoch:          0
License:        BSD
URL:            http://sourceforge.net/projects/dom4j
# ./create-tarball.sh
Source0:        %{name}-%{version}-clean.tar.xz
Source1:        dom4j_rundemo.sh
Source2:        http://repo1.maven.org/maven2/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Source3:        create-tarball.sh
Patch0:         dom4j-1.6.1-build_xml.patch
# See https://bugzilla.redhat.com/show_bug.cgi?id=976180
Patch1:         dom4j-1.6.1-Remove-references-to-ConcurrentReaderHashMap.patch
Patch2:         dom4j-1.6.1-Port-to-JAXP-1.4.patch
# Needed by stapler web framework
Patch3:         dom4j-1.6.1-Add-ability-to-disable-HTML-handling.patch
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant >= 0:1.6
#BuildRequires:  junit
BuildRequires:  jtidy
#BuildRequires:  junitperf
BuildRequires:  isorelax
BuildRequires:  jaxen-bootstrap >= 0:1.1
BuildRequires:  msv-msv
BuildRequires:  relaxngDatatype
BuildRequires:  bea-stax
BuildRequires:  bea-stax-api
BuildRequires:  ws-jaxme
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xpp2
BuildRequires:  xpp3
BuildRequires:  msv-xsdlib
BuildRequires:  javapackages-local
BuildArch:      noarch
Source44: import.info

%description
dom4j is an Open Source XML framework for Java. dom4j allows you to read,
write, navigate, create and modify XML documents. dom4j integrates with 
DOM and SAX and is seamlessly integrated with full XPath support. 

%package demo
Group: Development/Java
Summary:        Samples for %{name}
Requires:       dom4j = 0:%{version}

%description demo
Samples for %{name}.

%package manual
Group: Development/Java
Summary:        Manual for %{name}
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.


%prep
%setup -q 
# replace run.sh
cp -p %{SOURCE1} run.sh
# fix for deleted jars
mv build.xml build.xml.orig
sed -e '/unjar/d' -e 's|,cookbook/\*\*,|,|' build.xml.orig > build.xml

%patch0 -b .sav
%patch1 -p1
%patch2 -p1
%patch3 -p1

%mvn_alias : org.jvnet.hudson.dom4j:dom4j
%mvn_file : %{name}/%{name} %{name}

%build
pushd lib
ln -sf $(build-classpath xpp2)
ln -sf $(build-classpath relaxngDatatype)
ln -sf $(build-classpath jaxme/jaxmeapi) 
ln -sf $(build-classpath msv-xsdlib) 
ln -sf $(build-classpath msv-msv) 
ln -sf $(build-classpath jaxen) 
ln -sf $(build-classpath bea-stax-api) 
#pushd test
#ln -sf $(build-classpath bea-stax-ri)
#ln -sf $(build-classpath junitperf)
#ln -sf $(build-classpath junit)
#popd
ln -sf $(build-classpath xpp3) 
pushd tools
ln -sf $(build-classpath jaxme/jaxmexs) 
ln -sf $(build-classpath xalan-j2) 
ln -sf $(build-classpath jaxme/jaxmejs) 
ln -sf $(build-classpath jtidy) 
ln -sf $(build-classpath isorelax) 
ln -sf $(build-classpath jaxme/jaxme2) 
ln -sf $(build-classpath xerces-j2) 
popd
popd

# FIXME: test needs to be fixed
ant all samples # test

%install
%mvn_artifact %{SOURCE2} build/%{name}.jar

pushd build/doc/javadoc
for f in `find -name \*.html -o -name \*.css`; do
  sed -i 's/\r//g' $f;
done
popd

%mvn_install -J build/doc/javadoc

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
rm -rf docs/apidocs docs/clover
pushd docs
for f in `find -name \*.html -o -name \*.css -o -name \*.java`; do
  sed -i 's/\r//g' $f;
done
popd

cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}
tr -d \\r <LICENSE.txt >tmp.file; mv tmp.file LICENSE.txt
cp -p LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/classes/org/dom4j
cp -pr xml $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/src
cp -pr src/samples $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/src
cp -pr build/classes/org/dom4j/samples $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/classes/org/dom4j
install -m 755 run.sh $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

%files -f .mfiles
%doc %{_docdir}/%{name}/LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc %{_docdir}/%{name}/LICENSE.txt

%files manual
%doc %{_docdir}/%{name}

%files demo
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/run.sh
%{_datadir}/%{name}-%{version}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt6_26jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt6_25jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt4_13jpp7
- update

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt4_13jpp6
- switched to jpp due to repolib and fixed build

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt3_7jpp7
- fc version

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_13jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_10jpp5
- use default jpp profile

* Wed Sep 10 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_8jpp5
- converted from JPackage by jppimport script

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_8jpp5
- converted from JPackage by jppimport script

* Sun May 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_4jpp1.7
- converted from JPackage by jppimport script

* Mon Apr 25 2005 Vladimir Lettiev <crux@altlinux.ru> 1.6-alt1
- Initial release for ALT Linux Sisyphus

