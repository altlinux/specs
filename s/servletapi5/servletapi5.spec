BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2010, JPackage Project
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

%define base_name servletapi
%define full_name jakarta-%{base_name}

Name:           servletapi5
Version:        5.5.27
Release:	alt1_0jpp6
Epoch:          0
Summary:        Java Servlet 2.4 and JSP 2.0 API classes
License:        Apache License
Group:          Development/Java
Source0:        %{full_name}-4-src.tar.gz
Source1:        %{name}-%{version}.pom
Source2:        jspapi5-%{version}.pom
Url:            http://tomcat.apache.org/

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  aqute-bnd
BuildArch:      noarch
Provides:       servlet
Provides:       servlet_api
Provides:       servlet_2_4_api
Provides:       jsp_api
Provides:       jsp_2_0_api
Source44: import.info

%description
This subproject contains the source code for the implementation classes
of the Java Servlet and JSP APIs (packages javax.servlet).

%package javadoc
Group:            Development/Documentation
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{full_name}-4-src

%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 dist -Dservletapi.build=build -Dservletapi.dist=dist
pushd dist/lib
echo Bundle-SymbolicName: javax.servlet > servlet.osgi
echo Bundle-Version: 2.4.0 >> servlet.osgi
java -jar $(build-classpath aqute-bnd) wrap -properties servlet.osgi servlet.jar
rm servlet.jar
mv servlet.bar servlet.jar
popd

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
install -m 644 dist/lib/servlet.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap javax.servlet servlet-api 2.4 JPP servlet_2_4_api
%add_to_maven_depmap tomcat servlet-api %{version} JPP %{name}
%add_to_maven_depmap javax.servlet jsp-api 2.0 JPP jsp_2_0_api
%add_to_maven_depmap tomcat jsp-api %{version} JPP %{name}
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_%{name}<<EOF
%{_javadir}/servlet.jar	%{_javadir}/%{name}-%{version}.jar	20300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_2_4_api_%{name}<<EOF
%{_javadir}/servlet_2_4_api.jar	%{_javadir}/%{name}-%{version}.jar	20300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_api_%{name}<<EOF
%{_javadir}/servlet_api.jar	%{_javadir}/%{name}-%{version}.jar	20300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_2_0_api_%{name}<<EOF
%{_javadir}/jsp_2_0_api.jar	%{_javadir}/%{name}-%{version}.jar	10200
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_api_%{name}<<EOF
%{_javadir}/jsp_api.jar	%{_javadir}/%{name}-%{version}.jar	10200
EOF

cat >>$RPM_BUILD_ROOT/%_altdir/servletapi_%{name}<<EOF
%{_javadir}/servletapi.jar	%{_javadir}/%{name}-%{version}.jar	20300
EOF

%files
%_altdir/jsp_api_%{name}
%_altdir/jsp_2_0_api_%{name}
%_altdir/servlet_api_%{name}
%_altdir/servlet_2_4_api_%{name}
%_altdir/servlet_%{name}
%doc LICENSE README.txt
%{_javadir}/*.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%_altdir/servletapi_*

%files javadoc
%{_javadocdir}/*

%changelog
* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.5.27-alt1_0jpp6
- compat build
