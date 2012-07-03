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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_with gcj_support
%bcond_with maven
%bcond_with manual
%bcond_without repolib
%bcond_with sf_plugins

%define repodir %{_javadir}/repository.jboss.com/jaxen/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           jaxen
Version:        1.1.3
Release:        alt3_1jpp6
Epoch:          0
Summary:        XPath engine written in Java
License:        Open Source
Url:            http://jaxen.codehaus.org/
Group:          Development/Java
Source0:        http://dist.codehaus.org/jaxen/distributions/jaxen-1.1.3-src.tar.gz
Source1:        pom-maven2jpp-mapdeps.xsl
Source2:        %{name}-1.1.1-jpp-depmap.xml
Source3:        %{name}-1.1.1-jpp-disable-mojo-depmap.xml
Source4:        %{name}-1.1.2-build.xml
Source5:        jaxen-1.1.2.pom
Source6:        jaxen-component-info.xml
Patch0:         jaxen-project_xml.patch
Patch1:         %{name}-1.1.1-fix-css-path.patch
Patch2:         %{name}-1.1.2-disable-mojo-plugins.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: dom4j >= 0:1.6.1
Requires: jdom >= 0:1.0-1
Requires: xalan-j2
Requires: xerces-j2
Requires: xom
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: junit
%if %with maven
BuildRequires: maven >= 0:1.1
BuildRequires: saxon
BuildRequires: saxon-scripts
BuildRequires: maven-plugins-base >= 0:1.1
BuildRequires: maven-plugin-changes >= 0:1.1
BuildRequires: maven-plugin-checkstyle >= 0:1.1
BuildRequires: maven-plugin-file-activity >= 0:1.1
BuildRequires: maven-plugin-developer-activity >= 0:1.1
BuildRequires: maven-plugin-jdepend >= 0:1.1
BuildRequires: maven-plugin-jxr >= 0:1.1
BuildRequires: maven-plugin-license >= 0:1.1
BuildRequires: maven-plugin-linkcheck >= 0:1.1
BuildRequires: maven-plugin-pmd >= 0:1.1
BuildRequires: maven-plugin-tasklist >= 0:1.1
BuildRequires: maven-plugin-test >= 0:1.1
BuildRequires: maven-plugin-xdoc >= 0:1.1
BuildRequires: xml-commons-jaxp-1.3-apis
%if %with sf_plugins
BuildRequires: sf-cobertura-maven-plugin
BuildRequires: sf-findbugs-maven-plugin
%endif
%endif
BuildRequires: dom4j >= 0:1.6.1
BuildRequires: jdom >= 0:1.0-1
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xom
Provides:       jaxen-bootstrap = %{epoch}:%{version}-%{release}
Obsoletes:      jaxen-bootstrap < %{epoch}:%{version}-%{release}
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
Jaxen is an XPath engine written in Java to work against a variety of XML
based object models such as DOM, dom4j and JDOM together with Java
Beans.

%if %with maven
%if %with manual
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif
%endif

%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation
Requires: jaxen = %{epoch}:%{version}-%{release}

%description demo
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q
%{__perl} -pi -e 's/\r$//g' LICENSE.txt

cp -p %{SOURCE4} build.xml

%patch0 -b .sav0
%patch1 -b .sav1
%if %without sf_plugins
%patch2 -b .sav2
%endif

%build
%if %with maven
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    %{_bindir}/saxon -o project.xml project.xml.orig %{SOURCE1} map=%{SOURCE2}
    popd
done

%if %without sf_plugins
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    %{_bindir}/saxon -o project.xml project.xml.orig %{SOURCE1} map=%{SOURCE3}
    popd
done
%endif

mkdir .maven

%if %with manual
maven \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=$(pwd)/.maven \
        jar javadoc xdoc
%else
maven \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=$(pwd)/.maven \
        jar javadoc
%endif
%else
export CLASSPATH=$(build-classpath dom4j jdom xerces-j2 xml-commons-jaxp-1.3-apis xom)
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dversion=%{version} jar javadoc
%endif

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 0644 target/jaxen-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap jaxen jaxen %{version} JPP %{name}

pushd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}.jar; do
        ln -s ${jar} `echo $jar| sed "s|-%{version}\.jar|.jar|g"`;
done
popd

# poms
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%if %with maven
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%else
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %with maven
%if %with manual
cp -pr target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/apidocs/
%endif
%endif

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/samples
cp -pr src/java/samples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/samples

%if %with repolib
install -d -m 0755 $RPM_BUILD_ROOT%{repodir}
install -d -m 0755 $RPM_BUILD_ROOT%{repodirlib}
install -d -m 0755 $RPM_BUILD_ROOT%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE6} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
install -p -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/jaxen.jar $RPM_BUILD_ROOT%{repodirlib}/jaxen.jar
%if %with maven
install -m 755 %{SOURCE4} $RPM_BUILD_ROOT%{repodirsrc}/
%endif
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%if %with maven
%if %with manual
%files manual
%{_docdir}/%{name}-%{version}
%endif
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}-%{version}

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt3_1jpp6
- fixed build with moved maven1

* Tue Oct 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt2_1jpp6
- rebuild with target=5 (to avoid class poisoning)

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_1jpp6
- new version

* Mon Jun 15 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_3jpp5
- added repolib

* Fri Nov 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Mon Apr 30 2007 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.4beta2
- added JPackage compat stuff

* Fri Mar 24 2006 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt0.3beta2
- Fix typo in requires of javadoc package

* Wed Mar 22 2006 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt0.2beta2
- Fix build with j2se1.5

* Sat Apr 23 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt0.1beta2
- Initial build for ALT Linux Sisyphus

