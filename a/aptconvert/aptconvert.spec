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


Name:           aptconvert
Summary:        Convert Almost Plain Text files
Url:            http://www.xmlmind.com/aptconvert.html
Version:        050713
Release:        alt1_3jpp5
Epoch:          0
License:        BSD-style
Group:          Development/Java
Source0:        http://www.xmlmind.com/_aptconvert/aptconvert-050713.tar.gz
Source1:        aptconvert-build.xml
Source2:        aptconvert-050713.pom

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: regexp
BuildRequires: gnu-regexp
Requires: gnu-regexp
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3


%description
Aptconvert is a command-line tool that can be used to convert
the APT format to HTML, XHTML, PDF, PostScript, (MS Word
loadable) RTF, DocBook SGML and DocBook XML.
The APT format (Almost Plain Text) is a simple markup language
(like HTML) than can be used to write simple article-like
documents (like HTML). Unlike HTML, APT uses as few markup as
possible to express the structure of the document. Instead,
APT uses paragraph indentation.

%package jakarta
Summary:        %{name} with jakarta-regexp
Group:          Development/Java
Requires: regexp
%if %{gcj_support}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description jakarta
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description manual
%{summary}.

%prep
%setup -q -n %{name}-%{version}
chmod -R go=u-w *
for f in $(find . -name "*.jar"); do
    mv $f $f.no
done


%build
cp %{SOURCE1} build.xml

export CLASSPATH=$(build-classpath gnu-regexp)
mv java/fr/pixware/util/jakarta .
ant -Dbuild.sysclasspath=first jar javadoc
mv aptall.jar aptall-gnu.jar
mv docs/javadoc docs/gnu-javadoc
mv jakarta java/fr/pixware/util
mv java/fr/pixware/util/gnu .
export CLASSPATH=$(build-classpath regexp)
ant -Dbuild.sysclasspath=first jar javadoc
mv aptall.jar aptall-jakarta.jar
mv docs/javadoc docs/jakarta-javadoc

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 aptall-gnu.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}-gnu-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && ln -sf %{name}-gnu-%{version}.jar %{name}-%{version}.jar)
install -m 644 aptall-jakarta.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-jakarta-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jakarta
cp -pr docs/gnu-javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/jakarta-javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jakarta
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr distrib/legal.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr distrib/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}


%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %{_docdir}/%{name}-%{version}/legal.txt
%{_javadir}/%{name}-gnu-%{version}.jar
%{_javadir}/%{name}-gnu.jar
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-gnu-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files jakarta
%doc %{_docdir}/%{name}-%{version}/legal.txt
%{_javadir}/%{name}-jakarta-%{version}.jar
%{_javadir}/%{name}-jakarta.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-jakarta-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%changelog
* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:050713-alt1_3jpp5
- new jpp release

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:050713-alt1_2jpp5
- fixed repocop warnings

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:050713-alt1_2jpp1.7
- converted from JPackage by jppimport script

