BuildRequires: maven-project
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             idlj-maven-plugin
Version:          1.2.1
Release:          alt2_9jpp8
Summary:          The CORBA IDL Compiler Maven Plugin 
License:          ASL 2.0
# http://www.mojohaus.org/plugins.html
URL:              http://mojo.codehaus.org/idlj-maven-plugin

# svn export http://svn.codehaus.org/mojo/tags/idlj-maven-plugin-1.2.1 idlj-maven-plugin-1.2.1
# tar cafJ idlj-maven-plugin-1.2.1.tar.xz idlj-maven-plugin-1.2.1
Source0:          idlj-maven-plugin-%{version}.tar.xz
Source1:          LICENSE-2.0.txt

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(avalon-logkit:avalon-logkit)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:    mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:    mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:    mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:    mvn(org.jacorb:jacorb-idl-compiler)
Source44: import.info

%description
The CORBA IDL Compiler Maven Plugin is used for processing IDL files into java sources.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

%pom_change_dep :plexus-compiler-api org.codehaus.plexus:
%pom_change_dep org.jacorb: :jacorb-idl-compiler
#%% pom_xpath_set "pom:dependency[pom:artifactId = 'jacorb-idl-compiler']/pom:optional" false

cp %{SOURCE1} .

%build
# Failed tests because of DEBUG: java.lang.NoClassDefFoundError: org/apache/maven/artifact/DependencyResolutionRequiredException
# Mabye related to http://jira.codehaus.org/browse/MNG-5449 ?
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_9jpp8
- fixed build with new maven-reporting-impl

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_9jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_8jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_7jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_6jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_5jpp8
- java 8 mass update

