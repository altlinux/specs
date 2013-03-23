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


Name:           docbook-maven
Version:        5.0
Release:        alt2_2jpp6
Epoch:          0
Summary:        Java support for Docbook
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn export https://docbook.svn.sourceforge.net/svnroot/docbook/trunk docbook-5.0 && tar cjf docbook-5.0.tar.bz2 docbook-5.0
# Exported revision 8940.
Source0:        docbook-5.0.tar.bz2
Source1:        docbook-jpp-depmap.xml
Source2:        docbook-settings.xml
Source3:        docbook-component-info.xml
Patch0:         docbook-fo-editor-build.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires:  apache-commons-parent >= 0:9
BuildRequires:  maven2 >= 0:2.0.7
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-release
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  mojo-maven2-plugin-build-helper
BuildRequires:  saxon6 >= 0:6.5.3
BuildRequires:  xalan-j2 >= 0:2.7
BuildArch:      noarch
Source44: import.info

%description
Java support for Docbook.

%package -n docbook-xml
Summary:        DocBook XML
Version:        5.0
Epoch:          0
Group:          Development/Java
Requires:       docbook-maven = 0:5.0

%description -n docbook-xml
DocBook XML.

%package -n docbook-xsl
Summary:        XSL stylesheets for transforming DocBook XML document instances
Version:        1.75.2
Epoch:          0
Group:          Development/Java
Requires:       docbook-maven = 0:5.0

%description -n docbook-xsl
These are XSL stylesheets for transforming DocBook XML document instances into
various output formats.

%package -n docbook-xsl-saxon
Summary:        Java extensions for use with the DocBook XML stylesheets Saxon
Version:        1.0.0
Epoch:          0
Group:          Development/Java
Requires:       docbook-maven = 0:5.0
Requires:       saxon6 >= 0:6.5.3

%description -n docbook-xsl-saxon
These are Java extensions for use with the DocBook XML stylesheets and the
Saxon XSLT engine.

%package -n docbook-xsl-xalan
Summary:        Java extensions for use with the DocBook XML stylesheets and Xalan-Java
Version:        1.0.0
Epoch:          0
Group:          Development/Java
Requires:       docbook-maven = 0:5.0
Requires:       xalan-j2 >= 0:2.7
Provides: docbook-xsl-java-xalan = 1.67

%description -n docbook-xsl-xalan
These are Java extensions for use with the DocBook XML stylesheets and the
Xalan-Java XSLT engine.

%package -n fo-editor
Summary:        DocBook FO editor
Version:        1.0.1
Epoch:          0
Group:          Development/Java

%description -n fo-editor
DocBook FO editor.

%package -n fo-editor-javadoc
Summary:        Javadoc for fo-editor
Version:        1.0.1
Epoch:          0
Group:          Development/Documentation
Requires:       jpackage-utils

%description -n fo-editor-javadoc
Javadoc for fo-editor.

%prep
%setup -q -n docbook-5.0
%patch0 -p0 -b .sav0
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}

pushd maven
%{__cp} -p %{SOURCE2} maven2-settings.xml

%{__sed} -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

%{__mkdir_p} external_repo
%{__ln_s} %{_javadir} external_repo/JPP
popd

%build
pushd maven
export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install
popd

pushd contrib/tools/fo-editor
export CLASSPATH=$(build-classpath log4j)
export OPT_JAR_LIST=:
%{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first compile javadoc dist_zip
popd

%install
%define version 5.0

%{__mkdir_p} %{buildroot}%{_javadir}
%{__mkdir_p} %{buildroot}%{_mavenpomdir}

%{__cp} -p maven/m2_repo/repository/net/sf/docbook/docbook/5.0/docbook-5.0.pom %{buildroot}%{_mavenpomdir}/JPP-docbook.pom
%add_to_maven_depmap net.sf.docbook docbook 5.0 JPP docbook

%{__cp} -p maven/m2_repo/repository/net/sf/docbook/docbook-xml/5.0-all/docbook-xml-5.0-all.pom %{buildroot}%{_mavenpomdir}/JPP-docbook-xml.pom
%{__cp} -p maven/m2_repo/repository/net/sf/docbook/docbook-xml/5.0-all/docbook-xml-5.0-all-resources.zip %{buildroot}%{_javadir}/docbook-xml-5.0-all-resources.zip
%{__ln_s} docbook-xml-5.0-all-resources.zip %{buildroot}%{_javadir}/docbook-xml-resources.zip
%add_to_maven_depmap net.sf.docbook docbook-xml 5.0-all JPP docbook-xml

%{__cp} -p maven/m2_repo/repository/net/sf/docbook/docbook-xsl/1.75.2/docbook-xsl-1.75.2.pom %{buildroot}%{_mavenpomdir}/JPP-docbook-xsl.pom
%{__cp} -p maven/m2_repo/repository/net/sf/docbook/docbook-xsl/1.75.2/docbook-xsl-1.75.2-ns-resources.zip %{buildroot}%{_javadir}/docbook-xsl-1.75.2-ns-resources.zip
%{__ln_s} docbook-xsl-1.75.2-ns-resources.zip %{buildroot}%{_javadir}/docbook-xsl-ns-resources.zip
%{__cp} -p maven/m2_repo/repository/net/sf/docbook/docbook-xsl/1.75.2/docbook-xsl-1.75.2-resources.zip %{buildroot}%{_javadir}/docbook-xsl-1.75.2-resources.zip
%{__ln_s} docbook-xsl-1.75.2-resources.zip %{buildroot}%{_javadir}/docbook-xsl-resources.zip
%add_to_maven_depmap net.sf.docbook docbook-xsl 1.75.2 JPP docbook-xsl

%{__cp} -p maven/m2_repo/repository/net/sf/docbook/docbook-xsl-saxon/1.0.0/docbook-xsl-saxon-1.0.0.pom %{buildroot}%{_mavenpomdir}/JPP-docbook-xsl-saxon.pom
%{__cp} -p maven/m2_repo/repository/net/sf/docbook/docbook-xsl-saxon/1.0.0/docbook-xsl-saxon-1.0.0.jar %{buildroot}%{_javadir}/docbook-xsl-saxon-1.0.0.jar
%{__ln_s} docbook-xsl-saxon-1.0.0.jar %{buildroot}%{_javadir}/docbook-xsl-saxon.jar
%add_to_maven_depmap net.sf.docbook docbook-xsl-saxon 1.0.0 JPP docbook-xsl-saxon

%{__cp} -p maven/m2_repo/repository/net/sf/docbook/docbook-xsl-xalan/1.0.0/docbook-xsl-xalan-1.0.0.pom %{buildroot}%{_mavenpomdir}/JPP-docbook-xsl-xalan.pom
%{__cp} -p maven/m2_repo/repository/net/sf/docbook/docbook-xsl-xalan/1.0.0/docbook-xsl-xalan-1.0.0.jar %{buildroot}%{_javadir}/docbook-xsl-xalan-1.0.0.jar
%{__ln_s} docbook-xsl-xalan-1.0.0.jar %{buildroot}%{_javadir}/docbook-xsl-xalan.jar
%add_to_maven_depmap net.sf.docbook docbook-xsl-xalan 1.0.0 JPP docbook-xsl-xalan

%{__mkdir_p} %{buildroot}%{_datadir}/fo-editor
%{__cp} -pr contrib/tools/fo-editor/dist/* %{buildroot}%{_datadir}/fo-editor

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/fo-editor-1.0.1
%{__cp} -pr contrib/tools/fo-editor/doc/* %{buildroot}%{_javadocdir}/fo-editor-1.0.1
%{__ln_s} fo-editor-1.0.1 %{buildroot}%{_javadocdir}/fo-editor

%files
%{_mavenpomdir}/JPP-docbook.pom
%{_mavendepmapfragdir}/%{name}

%files -n docbook-xml
%{_mavenpomdir}/JPP-docbook-xml.pom
%{_javadir}/docbook-xml-5.0-all-resources.zip
%{_javadir}/docbook-xml-resources.zip

%files -n docbook-xsl
%{_mavenpomdir}/JPP-docbook-xsl.pom
%{_javadir}/docbook-xsl-1.75.2-ns-resources.zip
%{_javadir}/docbook-xsl-ns-resources.zip
%{_javadir}/docbook-xsl-1.75.2-resources.zip
%{_javadir}/docbook-xsl-resources.zip

%files -n docbook-xsl-saxon
%{_mavenpomdir}/JPP-docbook-xsl-saxon.pom
%{_javadir}/docbook-xsl-saxon-1.0.0.jar
%{_javadir}/docbook-xsl-saxon.jar

%files -n docbook-xsl-xalan
%{_mavenpomdir}/JPP-docbook-xsl-xalan.pom
%{_javadir}/docbook-xsl-xalan-1.0.0.jar
%{_javadir}/docbook-xsl-xalan.jar

%files -n fo-editor
%dir %{_datadir}/fo-editor
%doc %{_datadir}/fo-editor/README
%{_datadir}/fo-editor/FOeditor.jar
%{_datadir}/fo-editor/configuration/attributes.xml
%{_datadir}/fo-editor/configuration/config.xml
%{_datadir}/fo-editor/configuration/graphics.xml
%{_datadir}/fo-editor/configuration/types.xml
%{_datadir}/fo-editor/run.bat
%{_datadir}/fo-editor/run.sh
%{_datadir}/fo-editor/templates/template.xml
#unpackaged directory: 
%dir %_datadir/fo-editor/configuration
%dir %_datadir/fo-editor/templates

%files -n fo-editor-javadoc
%{_javadocdir}/fo-editor-1.0.1
%{_javadocdir}/fo-editor

%changelog
* Sat Mar 23 2013 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt2_2jpp6
- complete build

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

