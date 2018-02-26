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

# If you want the demo to be built,
# give rpmbuild option '--with demo'

%define with_demo %{?_with_demo:1}%{!?_with_demo:0}
%define without_demo %{!?_with_demo:1}%{?_with_demo:0}


%define oname           jfreechart

Name:                   jfreechart0
Version:                0.9.21
Release:                alt2_6jpp1.7
Epoch:                  0
Summary:                Charts Generation library
License:                LGPL
URL:                    http://www.jfree.org/jfreechart/
Source0:                http://www.jfree.org/%{oname}/%{oname}-%{version}.tar.gz
Patch0:                 jfreechart-0.9.21-build_xml.patch
Group:                  Development/Java
Requires: jcommon0 >= 0.9.7
BuildRequires: ant
BuildRequires: jcommon0 >= 0.9.7
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: junit
BuildRequires: servlet
BuildRequires: xml-commons-apis
%if ! %{gcj_support}
BuildArch:      noarch
%endif
#Provides:               %{oname} = %{epoch}:%{version}-%{release}
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description
Free Java class library for generating charts.

%if %{with_demo}
%package demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires: %{name} = %{version}-%{release}
Requires: servlet
%if %{gcj_support}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description demo
Demos for %{name}.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
Javadoc for %{name}.
Requires(post):   /bin/rm,/bin/ln
Requires(postun): /bin/rm

%description javadoc -l fr
Javadoc pour %{name}.

%prep
%setup -q -n %{oname}-%{version}
## remove all binary libs
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%if %{without_demo}
%patch0 -b .sav
%endif

%build
export LANG=en_US.ISO8859-1
%if %{with_demo}
mv %{oname}-%{version}-demo.jar.no %{oname}-%{version}-demo.jar
%endif
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f ant/build.xml -Djunit.jar=%{_javadir}/junit.jar -Djcommon.jar=%{_javadir}/jcommon0.jar -Dservlet.jar=%{_javadir}/servlet.jar -Dgnujaxp.jar=%{_javadir}/xml-commons-apis.jar -Dbuildstable=true -Dproject.outdir=. -Dbasedir=. 

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{oname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%if %{with_demo}
install -m 644 %{oname}-%{version}-demo.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-demo-%{version}.jar
%endif
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

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

%if %{gcj_support}
%post demo
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun demo
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%doc licence-LGPL.txt README.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%if %{with_demo}
%files demo
%{_javadir}/%{name}-demo-%{version}.jar
%{_javadir}/%{name}-demo.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-demo-%{version}.jar.*
%endif
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.21-alt2_6jpp1.7
- fixed build with java 7

* Mon Jul 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.21-alt1_6jpp1.7
- converted from JPackage by jppimport script

