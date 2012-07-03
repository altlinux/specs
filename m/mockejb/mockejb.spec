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
#

%define gcj_support 0

# If you want tests to be built,
# give rpmbuild option '--with tests'
%define with_tests %{!?_with_tests:0}%{?_with_tests:1}
%define without_tests %{?_without_tests:1}%{!?_without_tests:0}


Summary:        Framework for running EJBs
Name:           mockejb
Version:        0.6
Release:        alt3_0.b2.3jpp5
Epoch:          0
License:        Apache Software License
URL:            http://mockejb.sourceforge.net/
Group:          Development/Java
Source0:        mockejb-0.6-beta2.zip
Source1:        mockejb-0.6-beta2.pom
Patch0:         mockejb-0.6-build_properties.patch
Patch1:         mockejb-AllTests.patch
Patch2:         mockejb-MockEjbContext.patch
Patch3:         mockejb-build_mockejb.patch

BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: asm
BuildRequires: aspectj
BuildRequires: cglib
BuildRequires: easymock
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-cactus
BuildRequires: jakarta-oro
BuildRequires: geronimo-j2ee-1.4-apis
BuildRequires: xdoclet
BuildRequires: xml-commons-apis
%if %{with_tests}
BuildRequires: mockrunner
%endif
Requires: jakarta-commons-logging
%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4

%description
MockEJB is a lightweight framework for running EJBs. MockEJB 
implements javax.ejb APIs and creates Home and EJBObject 
implementation classes for your EJBs. Internally, MockEJB relies 
on dynamic proxies and interceptors. MockEJB has two primary usages:
* It allows for running EJBs outside of the container for unit 
  testing.You can run EJBs directly from your favorite IDE with 
  the minimal setup effort.
* It allows for deploying mock EJBs (i.e., mock EJB implementation 
  classes) into the container. Mock EJBs provide very effective way 
  of isolating EJBs under test from the rest of the application. 
  Mock EJBs return predefined test data and can override the actual 
  "non-mock" deployed EJBs. Once again, the purpose of MockEJB is 
  twofold and it works inside and outside of the container. So you 
  can benefit from it even if you continue running all your test 
  classes inside the container using Cactus. 
Additionally, MockEJB comes with the "mock" implementation of non-EJB 
APIs. Currently it provides in-memory JNDI and JMS implementations 
which can be used independently from MockEJB's EJB support.
MockEJB is not a full-blown EJB container. It does not fully implement 
J2EE/EJB specs, however it supports all vital APIs. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Documentation

%description manual
%{summary}.

%prep
%setup -q -n %{name}-%{version}-beta2
# remove all binary libs
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
cp build.properties.sample build.properties

%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
cp build.properties build_test.properties

%build
mkdir cactus-lib
pushd cactus-lib
ln -sf $(build-classpath aspectjrt) .
ln -sf $(build-classpath cactus-14/cactus) .
ln -sf $(build-classpath asm/asm) .
%if %{with_tests}
ln -sf $(build-classpath mockrunner/mockrunner) .
ln -sf $(build-classpath mockrunner/mockrunner-ejb) .
%endif
popd
export OPT_JAR_LIST="ant/ant-junit junit"
%if %{with_tests}
export CLASSPATH=$(build-classpath mockrunner)
ant build test
%else
ant -f build_mockejb.xml build
%endif

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp -p build/%{name}/%{name}-%{version}-beta2/lib/%{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# pom and depmap frags
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%add_to_maven_depmap org.mockejb %{name} %{version} JPP %{name}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/%{name}/%{name}-%{version}-beta2/doc/javadoc/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
rm -rf build/%{name}/%{name}-%{version}-beta2/doc/{javadoc,java2html}

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr build/%{name}/%{name}-%{version}-beta2/doc/* \
    $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%{_javadir}/*.jar
%doc %{_docdir}/%{name}-%{version}/ReleaseNotes.html
%{_datadir}/maven2
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt3_0.b2.3jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt2_0.b2.3jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt1_0.b2.3jpp5
- converted from JPackage by jppimport script

