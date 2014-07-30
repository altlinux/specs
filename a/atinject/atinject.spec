Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global artifactId javax.inject

Name:           atinject
Version:        1
Release:        alt4_10.20100611svn86jpp7
Summary:        Dependency injection specification for Java (JSR-330)

Group:          Development/Java
License:        ASL 2.0
URL:            http://code.google.com/p/atinject/
# latest release doesn't generate javadocs and there is no source
# tarball with pom.xml or ant build file
#
# svn export -r86 http://atinject.googlecode.com/svn/trunk atinject-1
# tar caf atinject-1.tar.xz atinject-1
Source0:        %{name}-%{version}.tar.xz
Source1:        MANIFEST.MF
BuildArch:      noarch

BuildRequires:       maven-local
BuildRequires:       maven-install-plugin
BuildRequires:       maven-jar-plugin
BuildRequires:       maven-surefire-provider-junit4
BuildRequires:       maven-surefire-plugin
BuildRequires:       maven-javadoc-plugin
BuildRequires:       maven-resources-plugin
BuildRequires:       maven-release-plugin
BuildRequires:       maven-compiler-plugin
BuildRequires:       zip


Requires:       jpackage-utils
Source44: import.info

%description
This package specifies a means for obtaining objects in such a way as
to maximize reusability, testability and maintainability compared to
traditional approaches such as constructors, factories, and service
locators (e.g., JNDI). This process, known as dependency injection, is
beneficial to most nontrivial applications.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.

%package        tck
Summary:        TCK for testing %{name} compatibility with JSR-330
Group:          Development/Java
Requires:       jpackage-utils
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       junit

%description    tck
%{summary}.


%prep
%setup -q

rm -rf lib/* javadoc/

ln -sf `build-classpath junit` lib/junit.jar
# fix insource
sed -i 's,javac -g,javac -source 1.5 -target 1.5 -g,' build.sh


%build
./build.sh
pushd build
for i in *.zip; do
    unzip $i
done

#Add OSGi manifest for Eclipse
mkdir -p META-INF/
cp %{SOURCE1} META-INF/MANIFEST.MF
zip -u javax.inject.jar META-INF/MANIFEST.MF

popd

%install
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 tck-pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-tck.pom

# jar files
install -pm 644 build/%{artifactId}.jar %{buildroot}%{_javadir}/%{name}.jar
install -pm 644 build/%{artifactId}-tck.jar %{buildroot}%{_javadir}/%{name}-tck.jar

%add_maven_depmap JPP-%{name}.pom %{name}.jar
%add_maven_depmap JPP-%{name}-tck.pom %{name}-tck.jar -f tck

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}

install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-tck
cp -pr build/tck/javadoc/* %{buildroot}%{_javadocdir}/%{name}-tck


%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar

%files tck
%{_mavendepmapfragdir}/%{name}-tck
%{_javadir}/%{name}-tck.jar
%{_mavenpomdir}/JPP-%{name}-tck.pom

%files javadoc
%doc %{_javadocdir}/%{name}
%doc %{_javadocdir}/%{name}-tck

%changelog
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

