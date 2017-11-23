Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           istack-commons
Version:        2.21
Release:        alt1_7jpp8
Summary:        Common code for some Glassfish projects
License:        CDDL-1.1 and GPLv2 with exceptions
URL:            http://istack-commons.java.net
# svn export https://svn.java.net/svn/istack-commons~svn/tags/istack-commons-2.21/ istack-commons-2.21
# find istack-commons-2.21/ -name '*.class' -delete
# find istack-commons-2.21/ -name '*.jar' -delete
# rm -rf istack-commons-2.21/test/lib/*.zip istack-commons-2.21/runtime/lib/*.zip
# tar -zcvf istack-commons-2.21.tar.gz istack-commons-2.21
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(com.sun.codemodel:codemodel)
BuildRequires:  mvn(com.sun:tools)
BuildRequires:  mvn(dom4j:dom4j)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:file-management)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http-lightweight)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-io)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-connector-basic)
BuildRequires:  mvn(org.eclipse.aether:aether-impl)
BuildRequires:  mvn(org.eclipse.aether:aether-spi)
BuildRequires:  mvn(org.eclipse.aether:aether-transport-file)
BuildRequires:  mvn(org.eclipse.aether:aether-transport-wagon)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.testng:testng)
Source44: import.info

%description
Code shared between JAXP, JAXB, SAAJ, and JAX-WS projects.

%package maven-plugin
Group: Development/Java
Summary:        istack-commons Maven Mojo
Obsoletes:      maven-istack-commons-plugin < %{version}-%{release}
Provides:       maven-istack-commons-plugin = %{version}-%{release}

%description maven-plugin
This package contains the istack-commons Maven Mojo.

%package -n import-properties-plugin
Group: Development/Java
Summary:        istack-commons import properties plugin

%description -n import-properties-plugin
This package contains the istack-commons import properties Maven Mojo.

%package buildtools
Group: Development/Java
Summary:        istack-commons buildtools
Obsoletes:      %{name} < %{version}-%{release}

%description buildtools
This package contains istack-commons buildtools.

%package runtime
Group: Development/Java
Summary:        istack-commons runtime
Obsoletes:      %{name} < %{version}-%{release}

%description runtime
This package contains istack-commons runtime.

%package soimp
Group: Development/Java
Summary:        istack-commons soimp
Obsoletes:      %{name} < %{version}-%{release}

%description soimp
This package contains istack-commons soimp.

%package test
Group: Development/Java
Summary:        istack-commons test
Obsoletes:      %{name} < %{version}-%{release}

%description test
This package contains istack-commons test.

%package tools
Group: Development/Java
Summary:        istack-commons tools
Obsoletes:      %{name} < %{version}-%{release}

%description tools
This package contains istack-commons tools.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%pom_remove_plugin org.glassfish.copyright:glassfish-copyright-maven-plugin
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin

# backward compatibility symlinks
%mvn_file com.sun.istack:%{name}-buildtools %{name}-buildtools %{name}/%{name}-buildtools
%mvn_file com.sun.istack:%{name}-runtime %{name}-runtime %{name}/%{name}-runtime
%mvn_file com.sun.istack:%{name}-soimp %{name}-soimp %{name}/%{name}-soimp
%mvn_file com.sun.istack:%{name}-test %{name}-test %{name}/%{name}-test
%mvn_file com.sun.istack:%{name}-tools %{name}-tools %{name}/%{name}-tools

# Unused & unavailable dep
%pom_remove_dep org.sonatype.sisu:sisu-inject-plexus import-properties-plugin

# get rid of scope "import", our tools don't know how to handle such deps
%pom_remove_dep com.sun:tools tools
%pom_add_dep com.sun:tools tools

%build

%mvn_build -s -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles-istack-commons
%dir %{_javadir}/%{name}
%doc Licence.txt

%files -n %{name}-maven-plugin -f .mfiles-%{name}-maven-plugin
%doc Licence.txt

%files -n import-properties-plugin -f .mfiles-import-properties-plugin
%doc Licence.txt

%files buildtools -f .mfiles-istack-commons-buildtools
%doc Licence.txt

%files runtime -f .mfiles-istack-commons-runtime
%doc Licence.txt

%files soimp -f .mfiles-istack-commons-soimp
%doc Licence.txt

%files test -f .mfiles-istack-commons-test
%doc Licence.txt

%files tools -f .mfiles-istack-commons-tools
%doc Licence.txt

%files javadoc -f .mfiles-javadoc
%doc Licence.txt


%changelog
* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.21-alt1_7jpp8
- new fc release

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.21-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.21-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.21-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 2.21-alt1_3jpp8
- new version

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.17-alt1_2jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt4_5jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt3_5jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt1_5jpp7
- new version

