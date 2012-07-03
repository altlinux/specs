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


Name:           java2html
Version:        1.4
Release:        alt1_1jpp5
Epoch:          0
Summary:        Java to HTML converter
License:        GPL v2
Url:            http://www.java2html.com/
Group:          Development/Java
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.j2h.script
## cvs -d:pserver:anonymous@java2html.cvs.sourceforge.net:/cvsroot/java2html login
## cvs -z3 -d:pserver:anonymous@java2html.cvs.sourceforge.net:/cvsroot/java2html export -r r1_4 .
Patch0:         java2html-build.patch

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 1.6.5
BuildRequires: ant-nodeps
BuildRequires: javacc3

Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

BuildArch:      noarch

%description
Java2HTML is a simple-to-use open-source tool which converts
a bunch of Java Source Code into a colourized  and browsable
HTML representation.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}
ln -s $(build-classpath javacc3) javacc.jar
%patch0 -b .sav0

%build
ant \
    -Djava_home=%{_jvmdir}/java  \
    -Djavac_bin=%{_jvmdir}/java/bin/javac \
    -Djavacc_home=$(pwd) \
    -f build/build.xml zip


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/temp/releaseZip/j2h.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

# create unprefixed and unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done
)
%add_to_maven_depmap %{name} j2h %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/temp/releaseZip/docsapi/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr build/temp/releaseZip/*.txt build/temp/releaseZip/*.html build/temp/releaseZip/api_examples \
       $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/j2h

%files
%{_javadir}/*.jar
%attr(755,root,root) %{_bindir}/j2h
%doc %{_docdir}/%{name}-%{version}/*
%dir %{_docdir}/%{name}-%{version}
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp5
- new version

