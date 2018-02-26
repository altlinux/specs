BuildRequires: /proc
BuildRequires: jpackage-compat
%global commitversion 157cf13
%global dlversion 0.0.2-0-g157cf13
%global cluster olabini

Name:     yecht
Version:  0.0.2
Release:  alt1_6jpp7
Summary:  A YAML processor based on Syck
Group:    Development/Java
License:  MIT
URL:            http://github.com/%{cluster}/%{name}
Source0:        %{url}/tarball/%{version}/%{cluster}-%{name}-%{dlversion}.tar.gz
Patch0:   fix-build-xml-classpaths.path

# https://bugzilla.redhat.com/show_bug.cgi?id=561455
Patch1:   add-javadocs-to-build-xml.patch

BuildRequires: jpackage-utils
BuildRequires: ant
Requires: jpackage-utils

BuildArch:      noarch
Source44: import.info

%description
Yecht is a Syck port, a YAML 1.0 processor for Ruby.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n olabini-%{name}-%{commitversion}
%patch0 -p1
%patch1

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
mkdir lib
ant
ant javadocs

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp lib/yecht-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/yecht-%{version}.jar
ln -s %{_javadir}/yecht-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/yecht.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/yecht-%{version}.jar
%{_javadir}/yecht.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_6jpp7
- new version

