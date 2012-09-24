Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-core
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

%define base_name jaxme

Name:           ws-jaxme-poms
Version:        0.5.2
Release:        alt1_1jpp5
Epoch:          0
Summary:        Open source implementation of JAXB - pom files

Group:          Development/Java
License:        Apache Software License
URL:            http://ws.apache.org/jaxme/

Source2:        jaxme2-0.5.2.pom
Source3:        jaxme2-rt-0.5.2.pom
Source4:        jaxmeapi-0.5.2.pom
Source5:        jaxmejs-0.5.2.pom
Source6:        jaxmepm-0.5.2.pom
Source7:        jaxmexs-0.5.2.pom

BuildArch:      noarch

BuildRequires: ws-jaxme
Requires: ws-jaxme

%description
A Java/XML binding compiler takes as input a schema 
description (in most cases an XML schema, but it may 
be a DTD, a RelaxNG schema, a Java class inspected 
via reflection, or a database schema). The output is 
a set of Java classes:
* A Java bean class matching the schema description. 
  (If the schema was obtained via Java reflection, 
  the original Java bean class.)
* Read a conforming XML document and convert it into 
  the equivalent Java bean.
* Vice versa, marshal the Java bean back into the 
  original XML document.

This package contains POM files for ws-jaxme.

%prep

%build

%install
%add_to_maven_depmap org.apache.ws.jaxme jaxme2 %{version} JPP/jaxme jaxme2
%add_to_maven_depmap org.apache.ws.jaxme jaxme2-rt %{version} JPP/jaxme jaxme2-rt
%add_to_maven_depmap org.apache.ws.jaxme jaxmeapi %{version} JPP/jaxme jaxmeapi
%add_to_maven_depmap org.apache.ws.jaxme jaxmejs %{version} JPP/jaxme jaxmejs
%add_to_maven_depmap org.apache.ws.jaxme jaxmepm %{version} JPP/jaxme jaxmepm
%add_to_maven_depmap org.apache.ws.jaxme jaxmexs %{version} JPP/jaxme jaxmexs

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.jaxme-jaxme2.pom
install -pm 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.jaxme-jaxme2-rt.pom
install -pm 644 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.jaxme-jaxmeapi.pom
install -pm 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.jaxme-jaxmejs.pom
install -pm 644 %{SOURCE6} \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.jaxme-jaxmepm.pom
install -pm 644 %{SOURCE7} \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.jaxme-jaxmexs.pom

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt1_1jpp5
- jpp poms for ws-jaxme
