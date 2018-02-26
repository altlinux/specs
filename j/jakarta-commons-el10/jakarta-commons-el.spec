%define oldname jakarta-commons-el
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

%define base_name       el
%define short_name      commons-%{base_name}

Name:           jakarta-commons-el10
Version:        1.0
Release:        alt5_12jpp5
Epoch:          0
Summary:        Commons Expression Language
License:        ASL 2.0
Group:          Development/Java
URL:            http://jakarta.apache.org/commons/el/
Source0:        http://archive.apache.org/dist/jakarta/commons/el/source/commons-el-%{version}-src.tar.gz
Source1:        http://repo1.maven.org/maven2/commons-el/commons-el/1.0/commons-el-1.0.pom
Patch0:         %{short_name}-%{version}-license.patch
Patch1:         %{short_name}-eclipse-manifest.patch
Patch2:         jakarta-commons-el-enum.patch
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant
BuildRequires: jsp_2_0_api
BuildRequires: servlet_2_4_api
BuildRequires: junit
Requires: jsp_2_0_api
Requires: servlet_2_4_api
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3


%description
An implementation of standard interfaces and abstract classes for
javax.servlet.jsp.el which is part of the JSP 2.0 specification.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildRequires: java-javadoc

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p1 -b .license
pushd src/conf
%patch1 -p1
popd
%patch2 -p1

# Already clean
#find . -type f -name "*.jar" | xargs rm

cat > build.properties <<EOBP
build.compiler=modern
junit.jar=$(build-classpath junit)
servlet-api.jar=$(build-classpath servlet_2_4_api)
jsp-api.jar=$(build-classpath jsp_2_0_api)
servletapi.build.notrequired=true
jspapi.build.notrequired=true
EOBP

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant \
  -Dfinal.name=%{short_name} \
  -Dj2se.javadoc=%{_javadocdir}/java \
  jar javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{short_name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|jakarta-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap commons-el commons-el %{version} JPP %{name}

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt STATUS.html
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/jakarta-commons-el-1.0.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_12jpp5
- compat build

* Thu Apr 02 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt4_12jpp5
- new jpp release

* Wed Jan 14 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt4_11jpp5
- fixed build

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt3_11jpp5
- updated OSGi manifest

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt2.2_9jpp5
- rebuild with osgi provides

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_8.2jpp1.7
- added eclipse manifest

* Mon Jul 30 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_7jpp1.7
- converted from JPackage by jppimport script

* Mon May 21 2007 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.2
- added jpackage compat symlinks

* Sun Mar 27 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt0.1
- rpm-build-java macroces
- version from cvs 20050321

* Fri Sep 10 2004 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt1
- Rebuild for ALT Linux Sisyphus
- spec cleanup

* Fri Jan  9 2004 Kaj J. Niemi <kajtzu@fi.basen.net> - 0:1.0-1jpp
- First build for JPackage

* Wed Dec 17 2003 Kaj J. Niemi <kajtzu@fi.basen.net> - 0:1.0-0.2
- With Javadocs

* Wed Dec 17 2003 Kaj J. Niemi <kajtzu@fi.basen.net> - 0:1.0-0.1
- First build

