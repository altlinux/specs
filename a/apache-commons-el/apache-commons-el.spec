Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

%global base_name       el
%global short_name      commons-%{base_name}


Name:           apache-%{short_name}
Version:        1.0
Release:        alt1_40jpp8
Summary:        The Apache Commons Extension Language
License:        ASL 1.1
URL:            http://commons.apache.org/%{base_name}
BuildArch:      noarch
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        http://repo1.maven.org/maven2/%{short_name}/%{short_name}/%{version}/%{short_name}-%{version}.pom
Patch0:         %{short_name}-%{version}-license.patch
Patch1:         %{short_name}-eclipse-manifest.patch
Patch2:         %{short_name}-enum.patch
BuildRequires:  ant
BuildRequires:  junit
BuildRequires:  javapackages-local
BuildRequires:  apache-commons-logging
BuildRequires:  glassfish-jsp-api
BuildRequires:  glassfish-servlet-api
Source44: import.info
Obsoletes: jakarta-%{short_name} < 1:%{version}-%{release}
Conflicts: jakarta-%{short_name} < 1:%{version}-%{release}

%description
An implementation of standard interfaces and abstract classes for
javax.servlet.jsp.el which is part of the JSP 2.0 specification.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
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
servlet-api.jar=$(build-classpath glassfish-servlet-api)
jsp-api.jar=$(build-classpath glassfish-jsp-api)
servletapi.build.notrequired=true
jspapi.build.notrequired=true
EOBP

# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1015612
find . -iname 'ELParser.java' -exec sed -i 's:enum:enum1:g' \{\} \;

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} \
  -Dfinal.name=%{short_name} \
  -Dj2se.javadoc=%{_javadocdir}/java \
  jar javadoc


%install
%mvn_artifact %{SOURCE1} dist/%{short_name}.jar
%mvn_alias "commons-el:commons-el" "org.apache.commons:commons-el"
%mvn_file : %{name} %{short_name}
%mvn_install -J dist/docs/api


%files -f .mfiles
%doc --no-dereference LICENSE.txt
%doc STATUS.html

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt


%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_40jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_38jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_37jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_36jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_35jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_29jpp7
- new release

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

