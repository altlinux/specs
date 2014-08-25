Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           modello
Version:        1.7
Release:        alt1_2jpp7
Epoch:          0
Summary:        Modello Data Model toolkit
# The majority of files are under MIT license, but some of them are
# ASL 2.0 or BSD-licensed.
License:        ASL 2.0 and BSD and MIT
URL:            http://modello.codehaus.org/
Source0:        http://repo2.maven.org/maven2/org/codehaus/%{name}/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-javac)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)

Provides:       modello-maven-plugin = %{epoch}:%{version}-%{release}
Obsoletes:      modello-maven-plugin < 0:1.0-0.a8.3jpp
Source44: import.info

%description
Modello is a Data Model toolkit in use by the Apache Maven Project.

Modello is a framework for code generation from a simple model.
Modello generates code from a simple model format based on a plugin
architecture, various types of code and descriptors can be generated
from the single model, including Java POJOs, XML
marshallers/unmarshallers, XSD and documentation.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q 
cp -p %{SOURCE1} LICENSE
# We don't generate site; don't pull extra dependencies.
%pom_remove_plugin :maven-site-plugin

%build
# skip tests because we have too old xmlunit in Fedora now (1.0.8)
%mvn_build -f

%install
%mvn_install

%jpackage_script org.codehaus.modello.ModelloCli "" "" modello:plexus-containers/plexus-container-default:plexus/classworlds:plexus/utils:plexus/plexus-build-api:xbean/xbean-reflect:guava %{name} true

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE
%{_bindir}/*
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_2jpp7
- new version

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_0jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt5_3jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt4_3jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_3jpp7
- new version

* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_1jpp6
- fixed build with new plexus-containers

* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_1jpp6
- fixed build with maven3

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp6
- new jpp release

* Thu Sep 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.2.a15.5jpp6
- reverted to a15

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.a17.1jpp5
- fixes for java6 support

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a17.1jpp5
- rebuild with maven

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a17.1jpp5
- new version a17

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a15.1jpp5
- fixed build w/java5

* Fri Dec 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a15.1jpp1.7
- new version

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a8.6jpp1.7
- build with maven2

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a8.6jpp1.7
- converted from JPackage by jppimport script

