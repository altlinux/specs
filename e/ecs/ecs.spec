Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.4.2
%define name ecs
%define full_name jakarta-%{name}

Name:           ecs
Version:        1.4.2
Release:        alt1_3jpp6
Epoch:          0
Summary:        Tools for generating HTML/XML/... elements
License:        Apache Software License
URL:            http://jakarta.apache.org/ecs/
Source0:        http://www.apache.org/dist/jakarta/ecs/source/ecs-1.4.2-src.tar.gz
Patch0:         %{name}-build.patch
Group:          Development/Java
BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.6
BuildRequires: ant >= 0:1.7
BuildRequires: regexp
BuildRequires: xerces-j2
BuildRequires: xerces-j2-javadoc-impl
BuildRequires: xml-commons-apis-javadoc
Requires: regexp
#Requires:       xerces-j2
Provides:       %{name}-manual = %{epoch}:%{version}-%{release}
Source44: import.info

%description
The Element Construction Set is a Java API for generating elements for
various markup languages it directly supports HTML 4.0 and XML, but
can easily be extended to create tags for any markup language. It is
designed and implemented by Stephan Nagy and Jon S. Stevens.

%package        javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -b .sav0
find . -name "*.jar" -exec rm -f {} \;
rm -rf docs/apidocs

%build
export CLASSPATH=%(build-classpath regexp xerces-j2)
ant \
  -Dbuild.compiler=modern \
  -Dxerces.javadoc=%{_javadocdir}/xerces-j2-impl \
  -Djaxp.javadoc=%{_javadocdir}/xml-commons-apis \
  -buildfile build/build-ecs.xml \
  jar javadocs

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -m 0644 bin/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rm -rf docs/apidocs

%files
%doc AUTHORS ChangeLog LICENSE.txt README RELEASE_NOTES.txt docs/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}

%changelog
* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt1_3jpp6
- new version

