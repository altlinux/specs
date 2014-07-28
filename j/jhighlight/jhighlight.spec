Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jhighlight
Version:        1.0
Release:        alt3_4jpp7
Summary:        An embeddable pure Java syntax highlighting library

Group:          Development/Java
License:        LGPLv2+
URL:            http://svn.rifers.org/jhighlight

# svn export http://svn.rifers.org/jhighlight/tags/release-1.0/ jhighlight-1.0
# find jhighlight-1.0/ -name *.jar
# tar cJf jhighlight-1.0.tar.xz jhighlight-1.0/
Source0:        %{name}-%{version}.tar.xz
Source1:        http://central.maven.org/maven2/com/uwyn/%{name}/%{version}/%{name}-%{version}.pom

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  jflex
BuildRequires:  jpackage-utils
BuildRequires:  tomcat-servlet-3.0-api

Requires:       jflex
Requires:       jpackage-utils
Requires:       tomcat-servlet-3.0-api
Source44: import.info

%description
JHighlight is an embeddable pure Java syntax highlighting library that supports
Java, Groovy, C++, HTML, XHTML, XML and LZX languages and outputs to XHTML. It
also supports RIFE (http://rifers.org) templates tags and highlights them
clearly so that you can easily identify the difference between your RIFE markup
and the actual marked up source.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find -name '*.class' -delete
find -name '*.jar' -delete

pushd lib/
ln -s %{_javadir}/jflex.jar
ln -s %{_javadir}/tomcat-servlet-3.0-api.jar
popd

%build
ant

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
unzip build/dist/%{name}-javadocs-%{version}.zip -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -d -m 0755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc README
%doc COPYING
%doc LICENSE_LGPL.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE_LGPL.txt
%doc COPYING


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_4jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_3jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp6
- new jpp relase

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_1jpp5
- fixes for java6 support

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp5
- converted from JPackage by jppimport script

