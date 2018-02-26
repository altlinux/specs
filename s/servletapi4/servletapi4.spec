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

Name:           servletapi4
Version:        4.0.4
Release:	alt2_7jpp6
Epoch:          0
Summary:        Java Servlet 2.3 and JSP 1.2 API classes
License:        Apache License
Group:          Development/Java
Source0:        %{full_name}-4-src.tar.gz
Source1:        servletapi4-4.0.4.pom
Url:            http://tomcat.apache.org/
Requires(preun):  alternatives
Requires(post):   alternatives
Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  aqute-bndlib
BuildArch:      noarch
Provides:       servlet
Provides:       servlet_api
Provides:       servlet_2_3_api
Provides:       jsp_api
Provides:       jsp_1_2_api
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
echo Bundle-Version: 2.3.0 >> servlet.osgi
java -jar $(build-classpath aqute-bndlib) wrap -properties servlet.osgi servlet.jar
rm servlet.jar
mv servlet.bar servlet.jar
popd

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
install -m 644 dist/lib/servlet.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap javax.servlet servlet-api 2.3 JPP servlet_2_3_api
%add_to_maven_depmap tomcat servlet-api %{version} JPP %{name}
%add_to_maven_depmap javax.servlet jsp-api 1.2 JPP jsp_1_2_api
%add_to_maven_depmap tomcat jsp-api %{version} JPP %{name}
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_servletapi4<<EOF
%{_javadir}/servlet.jar	%{_javadir}/%{name}-%{version}.jar	20300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_2_3_api_servletapi4<<EOF
%{_javadir}/servlet_2_3_api.jar	%{_javadir}/%{name}-%{version}.jar	20300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_api_servletapi4<<EOF
%{_javadir}/servlet_api.jar	%{_javadir}/%{name}-%{version}.jar	20300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_1_2_api_servletapi4<<EOF
%{_javadir}/jsp_1_2_api.jar	%{_javadir}/%{name}-%{version}.jar	10200
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_api_servletapi4<<EOF
%{_javadir}/jsp_api.jar	%{_javadir}/%{name}-%{version}.jar	10200
EOF

cat >>$RPM_BUILD_ROOT/%_altdir/servletapi_%{name}<<EOF
%{_javadir}/servletapi.jar	%{_javadir}/%{name}-%{version}.jar	20300
EOF

%files
%_altdir/jsp_api_servletapi4
%_altdir/jsp_1_2_api_servletapi4
%_altdir/servlet_api_servletapi4
%_altdir/servlet_2_3_api_servletapi4
%_altdir/servlet_servletapi4
%doc LICENSE README.txt
%{_javadir}/*.jar
%{_datadir}/maven2/*
%{_mavendepmapfragdir}/*
%_altdir/servletapi_*

%files javadoc
%{_javadocdir}/*

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt2_7jpp6
- new jpp relase

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt2_6jpp5
- fixes for java6 support

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt1_6jpp5
- alternatives 0.4

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt1_5jpp5
- converted from JPackage by jppimport script

* Tue Dec 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt1_4jpp1.7
- added servletapi alternative

* Sat Apr 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt0.5_4jpp1.7
- converted from JPackage by jppimport script

* Wed Apr 18 2007 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt0.5.20040901
- added servletapi4.jar (JPackage compat)

* Wed Apr 18 2007 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt0.4.20040901
- added Provides: servlet = api_version

* Sun Dec 19 2004 Mikhail Zabaluev <mhz@altlinux.ru> 4.0.0-alt0.3.20040901
- Renamed to jakarta-servletapi4
- Updated to the last CVS change
- Switched to the new alternatives format
- Use macros from rpm-build-java

* Sun Jul 04 2004 Mikhail Zabaluev <mhz@altlinux.ru> 4.0.0-alt0.2.20040703
- Updated to the last nightly build
- Introduced an alternative to manage servletapi.jar symlink

* Sat Jun 12 2004 Mikhail Zabaluev <mhz@altlinux.ru> 4.0.0-alt0.1.20040611
- Ported to Sisyphus from JPackage
- Package from Alexey Borovskoy used as well
