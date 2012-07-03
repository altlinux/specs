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

%define gcj_support 0
%define bootstrap %{?_with_bootstrap:1}%{!?_with_bootstrap:%{?_without_bootstrap:0}%{!?_without_bootstrap:%{?_bootstrap:%{_bootstrap}}%{!?_bootstrap:0}}}


Summary:        ObjectWeb Ant task
Name:           objectweb-anttask
Version:        1.3.2
Release:        alt4_5jpp6
Epoch:          0
Group:          Development/Java
License:        LGPL
URL:            http://asm.objectweb.org/
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source0:        ow_util_ant_tasks_1.3.2.zip
Source1:        asm-2.1.tar.gz
Patch0:         ow_util_ant_tasks_build_xml.patch
Patch1:         ow_util_ant_tasks_DependencyAnalyzer.patch
Patch2:         ow_util_ant_tasks_MultipleCopy.patch
BuildRequires:  jpackage-utils >= 0:1.7.6
BuildRequires:  xalan-j2
BuildRequires:  ant >= 0:1.7.1
%if ! %{bootstrap}
BuildRequires:  asm2
Requires:       asm2
%endif
Provides:       owanttask
%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Source44: import.info

%description
ObjectWeb Ant task

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -c -q -n %{name}
%if %{bootstrap}
tar xzf %{SOURCE1} asm-2.1/src
cp -R asm-2.1/src/* src
%endif
find . -name "*.class" -exec rm {} \;
find . -name "*.jar" -exec rm {} \;
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
ln -sf $(build-classpath asm2/asm2) externals
ln -sf $(build-classpath xalan-j2) externals

%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar jdoc

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 output/lib/ow_util_ant_tasks.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf %{name}-%{version}.jar %{name}.jar
popd

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/jdoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
(cd $RPM_BUILD_ROOT%{_javadocdir} && ln -sf %{name}-%{version} %{name})

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt4_5jpp6
- new jpp relase

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt4_4jpp5
- new jpp release

* Wed Nov 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt4_3jpp1.7
- force build with java4

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt3_3jpp1.7
- full-fledged build

* Wed May 16 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt2_3jpp1.7
- fixed build with ant-1.7.0

* Wed Mar 22 2006 Vladimir Lettiev <crux@altlinux.ru> 1.2-alt2
- Fix build with j2se-1.5

* Thu Apr 28 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2-alt1
- Initial release


