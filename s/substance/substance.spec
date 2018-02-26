Packager: Igor Vlasenko <viy@altlinux.ru>
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

Name:           substance
Version:        5.3
Release:        alt2_1jpp6
Summary:        Substance Look and Feel
License:        BSD
Group:          Development/Java
Url:            https://substance.dev.java.net/
Source0:        substance-5.3.tgz
# svn export https://substance.dev.java.net/svn/substance/tags/release_5_3_reykjavik substance-5.3
Patch0:         substance-build.patch

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant
BuildRequires: ant-nodeps
BuildRequires: asm2
BuildRequires: fest-assert
BuildRequires: fest-reflect
BuildRequires: fest-swing
BuildRequires: fest-util
BuildRequires: jgoodies-forms
BuildRequires: laf-plugin
BuildRequires: laf-widget
BuildRequires: swingx
Requires: jgoodies-forms
Requires: laf-plugin
Requires: laf-widget
Requires: swingx
BuildArch:      noarch

%description
A configurable and customizable production-quality Java look and feel
library for Swing applications.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q 
%patch0 -b .sav
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
ln -sf %{_javadir}/asm2-all.jar       lib/asm-all-2.2.2.jar
ln -sf %{_javadir}/jgoodies-forms.jar lib/forms-1.2.0.jar
ln -sf %{_javadir}/laf-plugin.jar     lib/laf-plugin-50.jar
ln -sf %{_javadir}/laf-widget.jar     lib
ln -sf %{_javadir}/swingx.jar         lib
ln -sf %{_javadir}/fest/assert.jar    lib/test/fest-assert-1.1.jar
ln -sf %{_javadir}/fest/reflect.jar   lib/test/fest-reflect-1.1.jar
ln -sf %{_javadir}/fest/swing.jar     lib/test/fest-swing-1.2a3.jar
ln -sf %{_javadir}/fest/util.jar      lib/test/fest-util-1.1.jar

%build
export LANG=en_US.ISO8859-1
export OPT_JAR_LIST="ant/ant-nodeps"
%ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
        -Djdk.home=%{_jvmdir}/java all javadoc

%install
[ -d "%{buildroot}" -a "%{buildroot}" != "" ] && %__rm -rf "%{buildroot}"

# jar
%__install -dm 755 %{buildroot}%{_javadir}
%__install -m 644 drop/%{name}.jar \
        %{buildroot}%{_javadir}/%{name}-%{version}.jar
%__install -m 644 drop/%{name}-lite.jar \
        %{buildroot}%{_javadir}/%{name}-lite-%{version}.jar
%__install -m 644 drop/%{name}-lite-feel.jar \
        %{buildroot}%{_javadir}/%{name}-lite-feel-%{version}.jar
%__install -m 644 drop/%{name}-tools.jar \
        %{buildroot}%{_javadir}/%{name}-tools-%{version}.jar
%__install -m 644 drop/%{name}-tst.jar \
        %{buildroot}%{_javadir}/%{name}-tst-%{version}.jar
%__install -m 644 drop/%{name}-tst-lite.jar \
        %{buildroot}%{_javadir}/%{name}-tst-lite-%{version}.jar
pushd %{buildroot}%{_javadir}
        for jar in *-%{version}*; do
                ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
        done
popd

# javadoc
%__install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -pr docs/* \
        %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} \
        %{buildroot}%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%doc www/*

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 5.3-alt2_1jpp6
- fixed build with java 7

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 5.3-alt1_1jpp6
- new version

