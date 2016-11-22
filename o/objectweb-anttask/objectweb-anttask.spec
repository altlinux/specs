# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
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

%global _with_bootstrap 0

%global with_bootstrap %{!?_with_bootstrap:0}%{?_with_bootstrap:1}
%global without_bootstrap %{?_with_bootstrap:0}%{!?_with_bootstrap:1}


Summary:        ObjectWeb Ant task
Name:           objectweb-anttask
Version:        1.3.2
Release:        alt4_12jpp8
Epoch:          0
Group:          Development/Java
License:        LGPLv2+
URL:            http://forge.objectweb.org/projects/monolog/
BuildArch:      noarch
Source0:        http://download.forge.objectweb.org/monolog/ow_util_ant_tasks_1.3.2.zip
BuildRequires:  ant >= 0:1.6
BuildRequires: javapackages-tools rpm-build-java

%if %{without_bootstrap}
BuildRequires:  asm2
Requires:       asm2
%endif
Requires:       ant
Source44: import.info

%description
ObjectWeb Ant task

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -c -q -n %{name}

# extract jars iff in bootstrap mode
%if %{without_bootstrap}
find . -name "*.class" -exec rm {} \;
find . -name "*.jar" -exec rm {} \;
%endif

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java
export CLASSPATH=$(build-classpath asm2/asm2)
ant -Dbuild.compiler=modern -Dbuild.sysclasspath=first jar jdoc

%install
# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 output/lib/ow_util_ant_tasks.jar\
 $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr output/jdoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
echo "%{name}" > $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/%{name}

%files
%doc doc/* 
%doc output/jdoc/*
%{_javadir}/*
%{_sysconfdir}/ant.d/*

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt4_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt4_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt4_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt4_8jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt4_7jpp7
- fc update

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


