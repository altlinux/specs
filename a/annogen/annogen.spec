Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           annogen 
Version:        0.1.0
Release:        alt1_5jpp7
Summary:        Java framework for JSR-175 annotations

Group:          Development/Java
License:        ASL 2.0
URL:            http://annogen.codehaus.org/
# svn export http://svn.codehaus.org/annogen/annogen/tags/release-0_1_0/ annogen-0.1.0
# find annogen-0.1.0/ -name '*.jar' -delete
# tar cJf annogen-0.1.0-CLEAN.tar.xz annogen-0.1.0
Source0:        %{name}-%{version}-CLEAN.tar.xz
Source1:        http://repo1.maven.org/maven2/annogen/annogen/0.1.0/annogen-0.1.0.pom
Patch0:         annogen-doc-build.patch
BuildArch:      noarch

BuildRequires: ant
BuildRequires: qdox
BuildRequires: jpackage-utils
BuildRequires: dos2unix
Requires:      jpackage-utils
Requires:      qdox
Source44: import.info

%description
Annogen is a framework which helps you work with JSR175 Annotations. 
In a nutshell, Annogen generates a proxy layer in front of your 
Annotations.

%package javadoc
Summary:      API documentation for %{name}
Group:        Development/Java
Requires:     jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1
find examples -type f | xargs dos2unix
find license -type f | xargs dos2unix
find docs -name '*.html' -o -name '*.css' | xargs dos2unix

%build
export CLASSPATH=$( build-classpath qdox)
for x in *.xml; do 
  sed -i -e "s/source='1.4'/source='1.5'/; s/target='1.4'/target='1.5'/" $x;
done
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 jars
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 docs

%install
install -d -m 755 %{buildroot}%{_javadir}
cp build/distribution/annogen-*.jar %{buildroot}%{_javadir}/%{name}.jar

install -d -m 755 %{buildroot}%{_mavenpomdir}
cp %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp build/docs/* %{buildroot}%{_javadocdir}/%{name}/

%files
%doc license/LICENSE.txt license/NOTICE.txt examples/
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc license/LICENSE.txt
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.1.0-alt1_5jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.1.0-alt1_3jpp7
- fc update

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt3_8jpp6
- fixed build with java 7 (fixed patch1)

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt2_8jpp6
- converted from JPackage by jppimport script

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt2_8jpp5
- selected java5 compiler explicitly

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt1_8jpp5
- new jpackage release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt1_3jpp5
- converted from JPackage by jppimport script

* Mon Dec 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

