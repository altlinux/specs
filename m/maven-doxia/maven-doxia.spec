# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define fedora 21
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

%if 0%{?fedora}
%bcond_without itext
%bcond_without markdown
%endif

Name:           maven-doxia
Version:        1.4
Release:        alt1_2jpp7
Epoch:          0
Summary:        Content generation framework
License:        ASL 2.0
Group:          Development/Java
URL:            http://maven.apache.org/doxia/

Source0:        http://repo2.maven.org/maven2/org/apache/maven/doxia/doxia/%{version}/doxia-%{version}-source-release.zip


# TODO: push upstream
# abstract class should not be annotated as component because maven
# will pick it up and try to instantiate
Patch1:         0001-doxia-core-remove-plexus-component-annotation.patch

# Build against iText 2.x
# http://jira.codehaus.org/browse/DOXIA-53
Patch2:         0004-Fix-itext-dependency.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  plexus-cli
BuildRequires:  maven-local
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-shared-reporting-impl
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-doxia-tools
BuildRequires:  modello-maven-plugin
BuildRequires:  classworlds
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-validator
BuildRequires:  apache-commons-configuration
BuildRequires:  junit
BuildRequires:  jakarta-oro
BuildRequires:  plexus-i18n
BuildRequires:  plexus-utils
BuildRequires:  plexus-velocity
BuildRequires:  plexus-build-api
BuildRequires:  velocity
BuildRequires:  fop
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  plexus-containers-component-javadoc
BuildRequires:  plexus-containers-container-default
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-project
BuildRequires:  xmlgraphics-commons
BuildRequires:  avalon-framework
BuildRequires:  geronimo-parent-poms
BuildRequires:  geronimo-jms
BuildRequires:  javamail
%if %{with itext}
BuildRequires:  itext
%endif
%if %{with markdown}
BuildRequires:  pegdown
%endif

Obsoletes:      maven-doxia-book < %{epoch}:%{version}-%{release}
Obsoletes:      maven-doxia-maven-plugin < %{epoch}:%{version}-%{release}
Source44: import.info


%description
Doxia is a content generation framework which aims to provide its
users with powerful techniques for generating static and dynamic
content. Doxia can be used to generate static sites in addition to
being incorporated into dynamic content generation systems like blogs,
wikis and content management systems.


%package core
Group: Development/Java
Summary: Core module for %{name}

%description core
This package provides %{summary}.

%package logging-api
Group: Development/Java
Summary: Logging-api module for %{name}

%description logging-api
This package provides %{summary}.

%package module-apt
Group: Development/Java
Summary: APT module for %{name}

%description module-apt
This package provides %{summary}.

%package module-confluence
Group: Development/Java
Summary: Confluence module for %{name}

%description module-confluence
This package provides %{summary}.

%package module-docbook-simple
Group: Development/Java
Summary: Simplified DocBook module for %{name}

%description module-docbook-simple
This package provides %{summary}.

%package module-fml
Group: Development/Java
Summary: FML module for %{name}

%description module-fml
This package provides %{summary}.

%package module-fo
Group: Development/Java
Summary: FO module for %{name}

%description module-fo
This package provides %{summary}.

%if %{with itext}
%package module-itext
Group: Development/Java
Summary: iText module for %{name}

%description module-itext
This package provides %{summary}.
%endif

%if %{with markdown}
%package module-markdown
Group: Development/Java
Summary: Markdown module for %{name}

%description module-markdown
This package provides %{summary}.
%endif

%package module-latex
Group: Development/Java
Summary: Latex module for %{name}

%description module-latex
This package provides %{summary}.

%package module-rtf
Group: Development/Java
Summary: RTF module for %{name}

%description module-rtf
This package provides %{summary}.

%package modules
Group: Development/Java
Summary: Doxia modules for several markup languages.

%description modules
This package provides %{summary}.

%package module-twiki
Group: Development/Java
Summary: TWiki module for %{name}

%description module-twiki
This package provides %{summary}.

%package module-xdoc
Group: Development/Java
Summary: XDoc module for %{name}

%description module-xdoc
This package provides %{summary}.

%package module-xhtml
Group: Development/Java
Summary: XHTML module for %{name}

%description module-xhtml
This package provides %{summary}.

%package sink-api
Group: Development/Java
Summary: Sink-api module for %{name}

%description sink-api
This package provides %{summary}.

%package test-docs
Group: Development/Java
Summary: Test-docs module for %{name}

%description test-docs
This package provides %{summary}.

%package javadoc
Summary: Javadoc for %{name}
Group:   Development/Java
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n doxia-%{version}
%patch1 -p1
%patch2 -p1

# we don't have clirr-maven-plugin
%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin pom.xml

# use java 5 generics in modello plugin
%pom_xpath_inject "pom:plugin[pom:artifactId[text()='modello-maven-plugin']]"\
"/pom:executions/pom:execution/pom:configuration" \
"<useJava5>true</useJava5>" doxia-modules/doxia-module-fml/pom.xml

%if %{without itext}
%pom_disable_module doxia-module-itext doxia-modules
%endif
%if %{without markdown}
%pom_disable_module doxia-module-markdown doxia-modules
%endif

%build
# tests disabled because some use old plexus-container and don't work
# with new
%mvn_build -f -s

%install
%mvn_install


%files -f .mfiles-doxia
%doc LICENSE NOTICE
%files core -f .mfiles-doxia-core
%files logging-api -f .mfiles-doxia-logging-api
%doc LICENSE NOTICE
%files module-apt -f .mfiles-doxia-module-apt
%files module-confluence -f .mfiles-doxia-module-confluence
%files module-docbook-simple -f .mfiles-doxia-module-docbook-simple
%files module-fml -f .mfiles-doxia-module-fml
%files module-fo -f .mfiles-doxia-module-fo
%if %{with itext}
%files module-itext -f .mfiles-doxia-module-itext
%endif
%if %{with markdown}
%files module-markdown -f .mfiles-doxia-module-markdown
%endif
%files module-latex -f .mfiles-doxia-module-latex
%files module-rtf -f .mfiles-doxia-module-rtf
%files modules -f .mfiles-doxia-modules
%files module-twiki -f .mfiles-doxia-module-twiki
%files module-xdoc -f .mfiles-doxia-module-xdoc
%files module-xhtml -f .mfiles-doxia-module-xhtml
%files sink-api -f .mfiles-doxia-sink-api
%files test-docs -f .mfiles-doxia-test-docs
%doc LICENSE NOTICE
%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt4_4jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_4jpp7
- fixed build

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_4jpp7
- use fc geronimo

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp7
- new release

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

