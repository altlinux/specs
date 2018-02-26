Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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

%define gcj_support 0

%define jaxwsver  2.1

Name:           sun-jaxws-2.1-impl
Version:        2.1.3
Release:        alt5_1jpp5
Epoch:          0
Summary:        Java API for XML Web Services API
License:        CDDL
Url:            https://jax-ws-sources.dev.java.net/
Source0:        sun-jaxws-2.1-impl-2.1.3.tar.gz
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs login
#  cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r jaxws213 -d sun-jaxws-2.1-impl-2.1.3 jax-ws-sources/jaxws-ri  

Patch0:          sun-jaxws-2.1-impl-build.patch
Patch1:          sun-jaxws-2.1-impl-XmlUtil.patch
Patch2:          sun-jaxws-2.1-impl-build-bundle.patch

Group:          Development/Java
BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
BuildRequires: findbugs
BuildRequires: annotation_1_0_api
BuildRequires: jaf_1_1_api
BuildRequires: jaxb_2_1_api
BuildRequires: jaxws_2_1_api
BuildRequires: junit
BuildRequires: saaj_1_3_api
BuildRequires: servlet_2_5_api
BuildRequires: stax_1_0_api
BuildRequires: stax-ex >= 0:1.2
BuildRequires: sun-codemodel
BuildRequires: sun-fi >= 0:1.2.2
BuildRequires: sun-jaxb-2.1-impl >= 0:2.1.6
BuildRequires: sun-mimepull
BuildRequires: sun-txw2
BuildRequires: sun-xmlstreambuffer
BuildRequires: ws_metadata_2_0_api
BuildRequires: xml-commons-resolver12

Requires: annotation_1_0_api
Requires: ant >= 0:1.6.5
Requires: jaf_1_1_api
Requires: jaxb_2_1_api
Requires: jaxws_2_1_api
Requires: junit
Requires: saaj_1_3_api
Requires: stax_1_0_api
Requires: stax-ex >= 0:1.2
Requires: sun-codemodel
Requires: sun-fi >= 0:1.2.2
Requires: sun-jaxb-2.1-impl >= 0:2.1.6
Requires: sun-mimepull
Requires: sun-txw2
Requires: sun-xmlstreambuffer
Requires: ws_metadata_2_0_api
Requires: xml-commons-resolver12

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
The Reference Implementation for XML-Based Web Services (JAX-WS) 2.1 
according to JSR-224 MR2

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
mv lib/http.jar.no lib/http.jar
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2

%build
export CLASSPATH=$(build-classpath \
annotation_1_0_api \
jaf_1_1_api \
jaxb_2_1_api \
jaxws_2_1_api \
saaj_1_3_api \
servlet_2_5_api \
stax_1_0_api \
stax-ex \
sun-codemodel \
sun-fi \
sun-jaxb-2.1-impl \
sun-jaxb-2.1-impl-xjc \
sun-mimepull \
sun-txw2 \
sun-xmlstreambuffer \
ws_metadata_2_0_api \
)
ln -sf $(build-classpath sun-jaxb-2.1-tools/taglets) tools/lib
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 main architecture-document

sed -i -e 's/@VERSION@/%{version}/' \
       -e 's/@API_VERSION@/2.1/' \
       -e 's/@JAXB_VERSION@/2.1.6/' \
       etc/poms/jaxws-rt.pom
sed -i -e 's/@VERSION@/%{version}/' \
       -e 's/@JAXB_VERSION@/2.1.6/' \
       etc/poms/jaxws-tools.pom


%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 build/lib/http.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-http-%{version}.jar
install -m 644 build/lib/jaxws-rt.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-rt-%{version}.jar
install -m 644 build/lib/jaxws-tools.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tools-%{version}.jar
%add_to_maven_depmap com.sun.xml.ws jaxws-rt %{jaxwsver} JPP %{name}-rt
%add_to_maven_depmap com.sun.xml.ws jaxws-tools %{jaxwsver} JPP %{name}-tools

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 etc/poms/jaxws-rt.pom \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-rt.pom
install -pm 644 etc/poms/jaxws-tools.pom \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-tools.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 644 CDDL-1.0-license.txt \
           $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
install -m 644 CDDL+GPLv2.html \
           $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
install -m 644 CDDL+GPLv2.txt \
           $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/


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
%{_docdir}/%{name}-%{version}/CDDL*
%{_javadir}/%{name}*.jar
%{_datadir}/maven2/poms/*
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

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt5_1jpp5
- fixed build with java 7

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt4_1jpp5
- fixes for java6 support

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt3_1jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_1jpp5
- fixed docdir ownership

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_1jpp5
- converted from JPackage by jppimport script

