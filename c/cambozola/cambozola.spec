BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           cambozola
Version:        0.92
Release:        alt1_4jpp7
Summary:        A viewer for multipart jpeg streams

Group:          Development/Java
License:        GPLv2+
URL:            http://www.charliemouse.com/code/cambozola/index.html
Source0:        http://www.charliemouse.com:8080/code/cambozola/%{name}-latest.tar.gz

#patch to add javadoc generation in build.xml
Patch0:         %{name}-%{version}-add_javadoc.patch


BuildArch:      noarch
BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  ant-nodeps
Requires:       jpackage-utils
Source44: import.info

%description
Cambozola is a very simple (cheesy!) viewer for multipart jpeg streams
that are often pumped out by a streaming webcam server,
sending over multiple images per second.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p0

# Remove pre-built JAR and class files
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.class' -exec rm -f '{}' \;

%build
ant javadoc
ant


%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}.jar   \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -p dist/%{name}-server.jar   \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-server.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadoc/*  \
  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-server.jar
%doc LICENSE README.html


%files javadoc
%{_javadocdir}/%{name}


%changelog
* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1_4jpp7
- new version

