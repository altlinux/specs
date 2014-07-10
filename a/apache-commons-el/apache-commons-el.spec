Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat

%global base_name       el
%global short_name      commons-%{base_name}


Name:           apache-%{short_name}
Version:        1.0
Release:        alt1_26jpp7
Summary:        The Apache Commons Extension Language
License:        ASL 1.1
Group:          Development/Java
URL:            http://commons.apache.org/%{base_name}
BuildArch:      noarch
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        http://repo1.maven.org/maven2/%{short_name}/%{short_name}/%{version}/%{short_name}-%{version}.pom
Patch0:         %{short_name}-%{version}-license.patch
Patch1:         %{short_name}-eclipse-manifest.patch
Patch2:         %{short_name}-enum.patch
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant
BuildRequires:  tomcat-jsp-2.2-api
BuildRequires:  tomcat-servlet-3.0-api
BuildRequires:  junit
Source44: import.info
Obsoletes: jakarta-%{short_name} < 1:%{version}-%{release}
Conflicts: jakarta-%{short_name} < 1:%{version}-%{release}

%description
An implementation of standard interfaces and abstract classes for
javax.servlet.jsp.el which is part of the JSP 2.0 specification.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils

Provides:       jakarta-%{short_name}-javadoc = 0:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < 0:%{version}-%{release}
BuildArch: noarch


%description    javadoc
%{summary}.


%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p1 -b .license
%patch1 -p1
%patch2 -p1

# remove all precompiled stuff
find . -type f -name "*.jar" -exec rm -f {} \;

cat > build.properties <<EOBP
build.compiler=modern
junit.jar=$(build-classpath junit)
servlet-api.jar=$(build-classpath tomcat-servlet-3.0-api)
jsp-api.jar=$(build-classpath tomcat-jsp-2.2-api)
servletapi.build.notrequired=true
jspapi.build.notrequired=true
EOBP

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} \
  -Dfinal.name=%{short_name} \
  -Dj2se.javadoc=%{_javadocdir}/java \
  jar javadoc


%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 dist/%{short_name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}*; do
    ln -sf ${jar} `echo $jar| sed "s|apache-||g"`
    ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
    ln -sf ${jar} `echo $jar| sed "s|apache-\(.*\)-%{version}|\1|g"`
done
popd # come back from javadir

# pom
install -pD -T -m 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{short_name}.pom
%add_to_maven_depmap org.apache.commons %{short_name} %{version} JPP %{short_name}

# following line is only for backwards compatibility. New packages
# should use proper groupid org.apache.commons
%add_to_maven_depmap commons-el commons-el %{version} JPP %{short_name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE.txt STATUS.html
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{short_name}-%{version}.jar
%{_javadir}/%{short_name}.jar
%{_mavenpomdir}/JPP-%{short_name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}


%changelog
* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_26jpp7
- fc update

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt6_0.r936225.4jpp6
- added OSGi manifest

* Wed Apr 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt5_0.r936225.4jpp6
- added OSGi manifest

* Mon Jan 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt4_0.r936225.4jpp6
- excluded repolib from main package

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt3_0.r936225.4jpp6
- add obsoletes

* Wed Dec 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt3_0.r936225.3jpp6
- really fixed broken symlink

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt2_0.r936225.3jpp6
- fixed broken symlink

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_0.r936225.3jpp6
- new version

