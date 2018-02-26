BuildRequires: jaf bsf sun-mail
BuildRequires: /proc
BuildRequires: jpackage-1.4-compat
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

%define gcj_support 0

%define oname   wsif

Name:           ws-wsif
Version:        2.1.0
Release:        alt1_0.rc1.1jpp1.7
Epoch:          0
Summary:        Web Service Invocation Framework

Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://ws.apache.org/wsif/
Source0:        http://people.apache.org/dist/ws/wsif/wsif-all-2.1.0_RC1.tgz
Source1:        ws-wsif-LICENSE
Patch0:		ws-wsif-ProvidersInitialisationTest.patch
Patch1:		ws-wsif-build_xml.patch


BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: ant-nodeps >= 0:1.6
BuildRequires: junit >= 0:3.8.1
BuildRequires: axis >= 0:1.2
BuildRequires: jakarta-commons-discovery
BuildRequires: jakarta-commons-logging
BuildRequires: log4j
BuildRequires: servletapi5
BuildRequires: ws-soap = 0:2.3.1
BuildRequires: wsdl4j-jboss4 >= 0:1.5.2
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis
BuildRequires: ejb = 0:2.1
BuildRequires: geronimo-jms-1.1-api
Requires: axis >= 0:1.2
Requires: jakarta-commons-discovery
Requires: jakarta-commons-logging
Requires: log4j
Requires: servletapi5
Requires: ws-soap = 0:2.3.1
Requires: wsdl4j >= 0:1.5.2
Requires: xerces-j2
Requires: xml-commons-apis
Requires: ejb = 0:2.1
Requires: geronimo-jms-1.1-api
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
The Web Services Invocation Framework (WSIF) is a simple Java 
API for invoking Web services, no matter how or where the 
services are provided. 
WSIF enables developers to interact with abstract 
representations of Web services through their WSDL descriptions 
instead of working directly with the Simple Object Access 
Protocol (SOAP) APIs, which is the usual programming model. 
With WSIF, developers can work with the same programming model 
regardless of how the Web service is implemented and accessed.
WSIF allows stubless or completely dynamic invocation of a Web 
service, based upon examination of the meta-data about the 
service at runtime. It also allows updated implementations of 
a binding to be plugged into WSIF at runtime, and it allows 
the calling service to defer choosing a binding until runtime.
Finally, WSIF is closely based upon WSDL, so it can invoke any 
service that can be described in WSDL.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description    manual
%{summary}.


%prep
%setup -q -n %{oname}-%{version}_RC1
for j in $(find . -name "*.jar"); do
	mv $j $j.no
done
cp %{SOURCE1} LICENSE

%build
pushd lib
ln -sf $(build-classpath sun-mail-monolithic)
ln -sf $(build-classpath jaf)
ln -sf $(build-classpath bsf)
# lib/ant-1_5_1.jar.no
ln -sf $(build-classpath ant)
# lib/apache_soap-2_3_1.jar.no
ln -sf $(build-classpath ws-soap)
# lib/axis-1_0-ant.jar.no
ln -sf $(build-classpath axis/axis-ant)
# lib/axis-1_0.jar.no
ln -sf $(build-classpath axis/axis)
# lib/commons-discovery.jar.no
ln -sf $(build-classpath commons-discovery)
# lib/commons-logging.jar.no
ln -sf $(build-classpath commons-logging)
# lib/jaxrpc-1_1.jar.no
ln -sf $(build-classpath axis/jaxrpc)
# lib/junit-3_8_1.jar.no
ln -sf $(build-classpath junit)
# lib/log4j-1_2_4.jar.no
ln -sf $(build-classpath log4j)
# lib/optional-1_5_1.jar.no
ln -sf $(build-classpath ant/ant-nodeps)
# lib/qname-from-wsdl4j-20021124.jar.no
ln -sf $(build-classpath wsdl4j-jboss4/qname)
# lib/saaj-1_1.jar.no
ln -sf $(build-classpath axis/saaj)
# lib/servlet-2_2.jar.no
ln -sf $(build-classpath servletapi5)
# lib/soaprmi-1_1.jar.no
#
# lib/wsdl4j-20021124.jar.no
ln -sf $(build-classpath wsdl4j-jboss4)
# lib/xercesImpl-2_2_1.jar.no
ln -sf $(build-classpath xerces-j2)
# lib/xmlParserAPIs-2_2_1.jar.no
ln -sf $(build-classpath xml-commons-apis)
popd
export CLASSPATH=$(./classpath.sh build)
CLASSPATH=$CLASSPATH:$(build-classpath ejb jms):test:samples:build/lib/%{oname}.jar
ant -Ddebug=on all javadocs samples

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 build/lib/%{oname}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -m 644 LICENSE $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
# javadocs
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -rf doc/api
cp -pr doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%if %{gcj_support}
%post
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%doc %{_datadir}/%{name}-%{version}
%{_javadir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Wed Dec 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt1_0.rc1.1jpp1.7
- converted from JPackage by jppimport script

