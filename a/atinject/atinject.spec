Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           atinject
Version:        1
Release:        alt7_22.20100611svn86jpp8
Summary:        Dependency injection specification for Java (JSR-330)
License:        ASL 2.0
URL:            http://code.google.com/p/atinject/
BuildArch:      noarch

# latest release doesn't generate javadocs and there is no source
# tarball with pom.xml or ant build file
#
# svn export -r86 http://atinject.googlecode.com/svn/trunk atinject-1
# rm -rf atinject-1/{lib,javadoc}/
# tar caf atinject-1.tar.xz atinject-1
Source0:        %{name}-%{version}.tar.xz

# These manifests based on the ones shipped by eclipse.org
Source1:        MANIFEST.MF
Source2:        MANIFEST-TCK.MF

Source3:        http://www.apache.org/licenses/LICENSE-2.0.txt

# Compile with source/target 1.5
Patch0:         %{name}-target-1.5.patch

BuildRequires:  javapackages-local
BuildRequires:  junit

Provides:       javax.inject
Source44: import.info

%description
This package specifies a means for obtaining objects in such a way as
to maximize reusability, testability and maintainability compared to
traditional approaches such as constructors, factories, and service
locators (e.g., JNDI). This process, known as dependency injection, is
beneficial to most nontrivial applications.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.

%package        tck
Group: Development/Java
Summary:        TCK for testing %{name} compatibility with JSR-330
Requires:       %{name} = %{version}
Requires:       junit

%description    tck
%{summary}.

%prep
%setup -q
cp %{SOURCE3} LICENSE
ln -s %{_javadir} lib

%patch0 -p1

# Fix dep in TCK pom
sed -i -e 's/pom\.groupId/project.groupId/' tck-pom.xml

# J2EE API symlinks
%mvn_file :javax.inject atinject javax.inject/atinject

# TCK sub-package
%mvn_file :javax.inject-tck atinject-tck
%mvn_package :javax.inject-tck tck

%build
set -e
alias rm=:
alias xargs=:
alias javadoc='javadoc -Xdoclint:none'
. ./build.sh

# Inject OSGi manifests required by Eclipse.
jar umf %{SOURCE1} build/dist/javax.inject.jar
jar umf %{SOURCE2} build/tck/dist/javax.inject-tck.jar

%mvn_artifact pom.xml build/dist/javax.inject.jar
%mvn_artifact tck-pom.xml build/tck/dist/javax.inject-tck.jar

%install
%mvn_install

# Javadocs
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}/tck
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}
cp -pr build/tck/javadoc/* %{buildroot}%{_javadocdir}/%{name}/tck

%files -f .mfiles
%doc LICENSE
%dir %{_javadir}/javax.inject
%dir %{_mavenpomdir}/javax.inject

%files tck -f .mfiles-tck

%files javadoc
%doc LICENSE
%{_javadocdir}/atinject

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1-alt7_22.20100611svn86jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:1-alt7_21.20100611svn86jpp8
- added osgi provides

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1-alt6_21.20100611svn86jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1-alt4_13.20100611svn86jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1-alt4_10.20100611svn86jpp7
- new release

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1-alt4_8.20100611svn86jpp7
- new fc release

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1-alt4_6.20100611svn86jpp7
- fc release

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1-alt3_8jpp6
- added fc compat symlink %{_javadir}/atinject.jar

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1-alt2_8jpp6
- target 5 build

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1-alt1_8jpp6
- new jpp relase

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1-alt1_2.20100611svn86jpp6
- fixed build

