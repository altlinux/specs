# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2011, JPackage Project
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

%global ucname PDFBox


Name:           pdfbox
Summary:        PDFBox pdf library
Url:            http://www.pdfbox.org/
Version:        0.7.3
Release:        alt2_3jpp6
Epoch:          0
License:        BSD
Group:          Development/Java
BuildArch:      noarch
Source0:        %{ucname}-%{version}.zip
Source1:        pdfbox-extract-expected.txt
Source2:        fdeb.pdf
Source3:        FreedomExpressions.pdf
Source4:        FreedomExpressions.fdf
Source5:        pdf_with_lots_of_fields.pdf
# XXX: modified to remove jempbox and update bouncycastle version
Source6:        http://mirrors.ibiblio.org/pub/mirrors/maven2/pdfbox/pdfbox/0.7.3/pdfbox-0.7.3.pom

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  ant-nodeps
BuildRequires:  bouncycastle
BuildRequires:  fontbox
BuildRequires:  junit
BuildRequires:  lucene
BuildRequires:  lucene-demo

Requires:       bouncycastle
Requires:       fontbox
Requires:       lucene
Requires:       lucene-demo
Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
PDFBox is a Java PDF Library. This project will allow 
access to all of the components in a PDF document. 
More PDF manipulation features will be added as the 
project matures. This ships with a utility to take a 
PDF document and output a text file.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n %{ucname}-%{version}
chmod -R go=u-w *
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
mkdir -p test/input
cp Resources/cmap/00_ReadMe.pdf test/input
cp %{SOURCE1} test/input/00_ReadMe.pdf.txt
cp %{SOURCE2} test/input/
cp %{SOURCE3} test/input/
cp %{SOURCE4} test/input/
cp %{SOURCE5} test/input/

build-jar-repository external \
ant \
bcmail \
bcprov \
fontbox \
junit \
lucene \
lucene-demos 

%build
export OPT_JAR_LIST="ant/ant-nodeps ant/ant-junit junit"

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
    -Dant.jar=$(build-classpath ant) \
    -Dcheckstyle.jar=$(build-classpath checkstyle4) \
    -Dfontbox.jar=$(build-classpath fontbox) \
    -Dlucene.jar=$(build-classpath lucene) \
    -Dlucene-demos.jar=$(build-classpath lucene-demos) \
    -Dbcprov.jar=$(build-classpath bcprov) \
    -Dbcmail.jar=$(build-classpath bcmail) \
    -Djunit.jar=$(build-classpath junit) \
test package javadoc


%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 lib/%{ucname}-%{version}-dev.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# 
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/Resources
cp -pr Resources/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/Resources

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -rf docs/javadoc 
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%{_javadir}/*.jar
%{_datadir}/%{name}-%{version}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7.3-alt2_3jpp6
- new jpp relase

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.7.3-alt2_1jpp5
- rebuild with new lucene

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.7.3-alt1_1jpp5
- new jpackage release

* Wed Jan 16 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.7.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

