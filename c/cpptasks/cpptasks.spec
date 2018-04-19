Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		cpptasks
Version:	1.0b5
Release:	alt2_20jpp8
Summary:	Compile and link task for ant

License:	ASL 2.0
URL:		http://ant-contrib.sourceforge.net/
Source0:	http://downloads.sourceforge.net/ant-contrib/cpptasks-1.0b5.tar.gz
Source1:	%{name}-README.fedora

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(xerces:xercesImpl)

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
%pom_remove_plugin :maven-source-plugin

# No need to assemble distribution tarballs
%pom_remove_plugin :maven-assembly-plugin

# Fix dependency on ant
%pom_change_dep ant:ant org.apache.ant:ant
%pom_remove_dep ant:ant-nodeps
%pom_remove_dep ant:ant-trax

%mvn_file :%{name} ant/%{name}

%build
%mvn_build

%install
%mvn_install

# Place a file into ant's config dir
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/
echo "ant/%{name}" > $RPM_BUILD_ROOT/%{_sysconfdir}/ant.d/%{name}

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE
%doc README.fedora
%{_sysconfdir}/ant.d/%{name}

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.0b5-alt2_20jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0b5-alt2_19jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0b5-alt2_18jpp8
- new jpp release

* Sun Feb 14 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0b5-alt2_16jpp8
- updated gradle support

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

