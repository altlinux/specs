Epoch: 0
Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:		cpptasks
Version:	1.0b5
Release:	alt2_15jpp8
Summary:	Compile and link task for ant

License:	ASL 2.0
URL:		http://ant-contrib.sourceforge.net/
Source0:	http://downloads.sourceforge.net/ant-contrib/cpptasks-1.0b5.tar.gz
Source1:	%{name}-README.fedora

BuildRequires:	ant
BuildRequires:	maven-local

BuildArch:	noarch
Source44: import.info

%description
This ant task can compile various source languages and produce
executables, shared libraries (aka DLL's) and static libraries. Compiler
adaptors are currently available for several C/C++ compilers, FORTRAN,
MIDL and Windows Resource files.

%package        javadoc
Group: Development/Java
Summary:	Javadoc for %{name}
BuildArch: noarch

%description	javadoc
Javadoc documentation for %{summary}.

%prep
%setup -q

find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;

sed -i 's/\r//' NOTICE 

cp -p %{SOURCE1} ./README.fedora

# Use default compiler configuration
%pom_remove_plugin :maven-compiler-plugin

# Let xmvn generate javadocs
%pom_remove_plugin :maven-javadoc-plugin

# Fix dependency on ant
%pom_remove_dep ant:ant
%pom_remove_dep ant:ant-nodeps
%pom_remove_dep ant:ant-trax
%pom_add_dep org.apache.ant:ant

%mvn_file :%{name} ant/%{name}

%build
%mvn_build

%install
%mvn_install

# Place a file into ant's config dir
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/
echo "ant/%{name}" > $RPM_BUILD_ROOT/%{_sysconfdir}/ant.d/%{name}
# jpp compat
ln -s ant/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
%add_to_maven_depmap ant-contrib %{name} %{namedversion} JPP %{name}

# poms
install -D -m 644 pom.xml $RPM_BUILD_ROOT%_mavenpomdir/JPP-%{name}.pom


%files -f .mfiles
%doc LICENSE NOTICE README.fedora
%{_sysconfdir}/ant.d/%{name}

%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/*
%_mavenpomdir/*


%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0b5-alt2_15jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0b5-alt2_12jpp7
- new release

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0b5-alt2_9jpp7
- update

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0b5-alt2_8jpp7
- added jpp compatible symlink

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0b5-alt1_8jpp7
- fc version

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.b5.1jpp5
- fixed build

* Tue May 19 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b5.1jpp5
- new version

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b4.1jpp5
- fixed repocop warnings

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b4.1jpp1.7
- converted from JPackage by jppimport script

