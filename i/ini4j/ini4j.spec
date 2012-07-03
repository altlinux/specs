Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6-compat
# Prevent brp-java-repack-jars from being run.
%global __jar_repack %{nil}

%global servlet_jar %{_javadir}/servlet.jar
%global jetty_jar %{_javadir}/jetty/jetty.jar

Name:           ini4j
Version:        0.4.1
Release:        alt1_2jpp6
Summary:        Java API for handling files in Windows .ini format

Group:          Development/Java
License:        ASL 2.0
URL:            http://www.ini4j.org/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.zip
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        %{name}-%{version}-build.xml

BuildArch:      noarch

# See http://ini4j.sourceforge.net/dependencies.html
BuildRequires: jpackage-utils
BuildRequires: ant
BuildRequires: tomcat5-servlet-2.4-api >= 5.5
BuildRequires: jetty6 >= 4.2.2

Requires: jpackage-utils
Requires: tomcat5-servlet-2.4-api >= 5.5

%description
The [ini4j] is a simple Java API for handling configuration files in Windows 
.ini format. Additionally, the library includes Java Preferences API 
implementation based on the .ini file.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep

%setup -q

cp -a %{SOURCE1} ./LICENSE-2.0.txt
cp -a %{SOURCE2} ./build.xml

find . -type f \( -iname "*.jar" -o -iname "*.class" \) | xargs -t %{__rm} -f

# remove test sources
%{__rm} -rf src/test
# remove site sources
%{__rm} -rf src/site

%build

%ant -Dbuild.servlet.jar=%{servlet_jar} -Dbuild.jetty.jar=%{jetty_jar} build javadoc

%install

# JAR
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && %{__ln_s} %{name}-%{version}.jar %{name}.jar)

# Javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}
%{__cp} -rp build/doc/api/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/*
%doc LICENSE-2.0.txt src/main/java/org/ini4j/package.html

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_2jpp6
- new version

* Sat Dec 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_4jpp6
- converted from JPackage by jppimport script

