Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
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


Name:           strutstestcase
Version:        2.1.4
Release:        alt1_1jpp5
Epoch:          0
Summary:        StrutsTestCase for JUnit

Group:          Development/Java
License:        Apache Software License
URL:            http://strutstestcase.sourceforge.net/
Source0:        http://downloads.sourceforge.net/strutstestcase/strutstest-214-src.zip
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/strutstestcase/strutstestcase/2.1.4-1.2-2.4/strutstestcase-2.1.4-1.2-2.4.pom

%if ! %{gcj_support}
BuildArch:      noarch
%endif

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: ant-trax
BuildRequires: junit
BuildRequires: jakarta-cactus
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-chain
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-digester
BuildRequires: jakarta-commons-logging
BuildRequires: jsp_2_0_api
BuildRequires: servlet_2_4_api
BuildRequires: struts
BuildRequires: struts-taglib
BuildRequires: struts-tiles
Requires: jakarta-cactus
Requires: jakarta-commons-collections
Requires: jakarta-commons-digester
Requires: jakarta-commons-logging
Requires: junit
Requires: jsp_2_0_api
Requires: servlet_2_4_api
Requires: struts
Requires: struts-taglib
Requires: struts-tiles
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

%description
StrutsTestCase is an extension of the JUnit TestCase class
that allows testing of individual Action objects with or 
without a running servlet engine. This framework provides 
both mock servlet objects as well as Cactus support to 
simulate the environment.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.


%prep
%setup -q -c -n %{name}-%{version}
for j in $(find . -name "*.jar"); do
	mv $j $j.no
done
%build
export LANG=C
pushd lib
ln -sf $(build-classpath cactus-14/cactus)
ln -sf $(build-classpath commons-beanutils)
ln -sf $(build-classpath commons-chain)
ln -sf $(build-classpath commons-collections)
ln -sf $(build-classpath commons-digester)
ln -sf $(build-classpath commons-logging)
ln -sf $(build-classpath junit)
ln -sf $(build-classpath struts)
ln -sf $(build-classpath struts-extras)
ln -sf $(build-classpath struts-taglib)
ln -sf $(build-classpath struts-tiles)
#
ln -sf $(build-classpath jsp_2_0_api) jsp-2.0.jar
ln -sf $(build-classpath servlet_2_4_api) servletapi-2.4.jar
popd

ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Dbuild_2.4=true build test package docs

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 dist/strutstest/strutstest-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-1.2-2.4-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
%add_to_maven_depmap %{name} %{name} %{version}-1.2-2.4 JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/strutstest/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-*-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.4-alt1_1jpp5
- new jpp release

* Thu May 14 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.4-alt1_0jpp5
- new version

* Thu May 14 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt3_3jpp5
- build with new struts

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_3jpp5
- fixed build with java 5

* Sat Nov 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_3jpp1.7
- converted from JPackage by jppimport script

