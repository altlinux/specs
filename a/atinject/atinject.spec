Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           atinject
Version:        1
Release:        alt4_13.20100611svn86jpp7
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
Source1:        MANIFEST.MF
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt

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
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       junit

%description    tck
%{summary}.


%prep
%setup -q
cp %{SOURCE2} LICENSE
ln -s %{_javadir} lib
# fix insource
sed -i 's,javac -g,javac -source 1.5 -target 1.5 -g,' build.sh


%build
set -e
alias rm=:
alias xargs=:
. ./build.sh

# Inject OSGi manifest required by Eclipse.
jar umf %{SOURCE1} build/dist/*.jar

%install
# Maven POMs
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -p -m 644 tck-pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-tck.pom

# JARs
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 build/dist/*.jar %{buildroot}%{_javadir}/%{name}.jar
install -p -m 644 build/tck/dist/*.jar %{buildroot}%{_javadir}/%{name}-tck.jar

# XMvn metadata
%add_maven_depmap
%add_maven_depmap JPP-%{name}-tck.pom %{name}-tck.jar -f tck

# Javadocs
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}/tck
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}
cp -pr build/tck/javadoc/* %{buildroot}%{_javadocdir}/%{name}/tck

# J2EE API symlinks
install -d -m 755 %{buildroot}%{_javadir}/javax.inject/
ln -sf ../%{name}.jar %{buildroot}%{_javadir}/javax.inject/

%files -f .mfiles
%doc LICENSE
%{_javadir}/javax.inject

%files tck -f .mfiles-tck

%files javadoc
%doc LICENSE
%doc %{_javadocdir}/%{name}

%changelog
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

