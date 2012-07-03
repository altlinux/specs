Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:      brazil
Version:   2.3
Release:   alt2_8jpp7
Summary:   Extremely small footprint Java HTTP stack
Group:     Development/Java
License:   SPL
URL:       http://research.sun.com/brazil/

# source tarball and the script used to fetch it from Sun's Download Center
# script usage:
# $ sh get-brazil.sh
Source0:   %{name}-%{version}.tar.gz
Source1:   get-brazil.sh

# upsteam's build script doesn't build javadocs, so use our own, better script
Source2:   brazil-build.xml

# patch for removing sun proprietary signal handling api not in gcj
Patch0:    brazil-remove-proprietary-sun-api.patch


BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    ant
Requires:         jpackage-utils
Source44: import.info

%description
Brazil is as an extremely small footprint HTTP stack and flexible architecture 
for adding URL-based interfaces to arbitrary applications and devices from Sun 
Labs. This package contains the core set of classes that are not dependent on 
any other external Java libraries.

%package javadoc
Summary:   Javadocs for %{name}
Group:     Development/Java
Requires:  %{name} = %{version}-%{release}
Requires:  jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package demo
Summary:   Demos for %{name}
Group:     Development/Java
Requires:  %{name} = %{version}-%{release}
Requires:  tcl

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n %{name}-%{version}

# apply patches
%patch0 -p0

# fix permissions and interpreter in sample scripts
grep -lR -e ^\#\!/usr/sfw/bin/tclsh8.3 samples | xargs sed --in-place "s|/usr/sfw/bin/tclsh8.3|/usr/bin/tclsh|"
grep -lR -e ^\#\!/usr/bin/tclsh        samples | xargs chmod 755
grep -lR -e ^\#\!/bin/sh               samples | xargs chmod 755

%build
cp -p %{SOURCE2} build.xml
ant all

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p build/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# samples
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr samples %{buildroot}%{_datadir}/%{name}

%files
%doc srcs/license.terms
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%files demo
%doc %{_datadir}/%{name}/samples/README
%{_datadir}/%{name}

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_8jpp7
- fc version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_9jpp6
- new jpp relase

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_6jpp5
- updated from f13

* Mon Jul 28 2008 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_3jpp5
- converted from JPackage by jppimport script

