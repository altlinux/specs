# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++ java-devel-default
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           ritopt
Version:        0.2.1
Release:        alt1_18jpp8
Summary:        A Java library for parsing command-line options
License:        GPLv2+
Group:          Development/Java
Url:            http://ritopt.sourceforge.net/
BuildArch:      noarch

Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-all.tar.gz
## Patch for javadoc build
Patch0:         %{name}-0.2.1-javadoc.patch

BuildRequires:  jpackage-utils
BuildRequires:  java-devel
BuildRequires:  ant
BuildRequires:  tex(latex)

Requires:       jpackage-utils
Source44: import.info

%description
Ritopt is an options parser for the Java programming language

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch
%description javadoc
Documentation for the ritopt library

%prep
%setup -q 
sed -i 's/\r//' NEWS
sed -i 's/\r//' ChangeLog
sed -i 's/\r//' AUTHORS
sed -i 's/\r//' README
%patch0 -p0 -b .javadoc

%build
# Upstream uses autotools, but it's easier just to call the commands directly

# Compile the classes and make a jar file
mkdir classes
javac -d classes -source 1.5 -target 1.5 java/gnu/dtools/ritopt/*.java
cd classes
jar cvf %{name}-%{version}.jar gnu
cd ..

# Generate the javadoc
mkdir javadoc
javadoc -d javadoc java/gnu/dtools/ritopt/*.java

# Latex the documentation
cd tut
pdflatex tutorial.tex

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 classes/%{name}-%{version}.jar $RPM_BUILD_ROOT/%{_javadir}/%{name}.jar
install -d -m 755 ${RPM_BUILD_ROOT}%{_javadocdir}/
cp -r javadoc ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}

%files
%doc tut/tutorial.pdf AUTHORS ChangeLog NEWS README
%{_javadir}/*.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_18jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_17jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_16jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_15jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_14jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_8jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_6jpp7
- new version

