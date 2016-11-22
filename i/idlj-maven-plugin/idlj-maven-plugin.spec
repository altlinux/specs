Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             idlj-maven-plugin
Version:          1.2.1
Release:          alt1_6jpp8
Summary:          The CORBA IDL Compiler Maven Plugin 
License:          ASL 2.0
URL:              http://mojo.codehaus.org/idlj-maven-plugin

# svn export http://svn.codehaus.org/mojo/tags/idlj-maven-plugin-1.2.1 idlj-maven-plugin-1.2.1
# tar cafJ idlj-maven-plugin-1.2.1.tar.xz idlj-maven-plugin-1.2.1
Source0:          idlj-maven-plugin-%{version}.tar.xz
Source1:          LICENSE-2.0.txt

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mojo-parent
BuildRequires:    plexus-utils
BuildRequires:    plexus-compiler
BuildRequires:    jacorb
BuildRequires:    junit
BuildRequires:    avalon-logkit
Source44: import.info

%description
The CORBA IDL Compiler Maven Plugin is used for processing IDL files into java sources.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n idlj-maven-plugin-%{version}

sed -i "s|>plexus<|>org.codehaus.plexus<|g" pom.xml
sed -i "s|>idl-compiler<|>jacorb-idl-compiler<|g" pom.xml

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
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_6jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_5jpp8
- java 8 mass update

