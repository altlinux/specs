# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           aopalliance
Version:        1.0
Release:        alt3_5jpp7
Epoch:          0
Summary:        Java/J2EE AOP standards
Group:          Development/Java
License:        Public Domain
URL:            http://aopalliance.sourceforge.net/
# cvs -d:pserver:anonymous@aopalliance.cvs.sourceforge.net:/cvsroot/aopalliance login
# password empty
# cvs -z3 -d:pserver:anonymous@aopalliance.cvs.sourceforge.net:/cvsroot/aopalliance export -r HEAD aopalliance
Source0:        aopalliance-src.tar.gz
Source1:        http://repo1.maven.org/maven2/aopalliance/aopalliance/1.0/aopalliance-1.0.pom
Source2:        %{name}-MANIFEST.MF

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  zip
BuildArch:      noarch
Source44: import.info

%description
Java/J2EE AOP standards

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{summary}.

%prep
%setup -q -n aopalliance

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} -Dbuild.sysclasspath=only jar javadoc

%install
# inject OSGi manifest
mkdir -p META-INF
cp -p %{SOURCE2} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/%{name}.jar META-INF/MANIFEST.MF


install -dm 755 %{buildroot}%{_javadir}

install -pm 644 build/aopalliance.jar \
  %{buildroot}%{_javadir}/%{name}.jar
install -dm 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}*/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_5jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_3jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_7jpp6
- new jpp relase

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_5jpp6
- new jpp release

* Fri Feb 13 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_6jpp5
- new version

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_3jpp5
- converted from JPackage by jppimport script

* Wed May 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

