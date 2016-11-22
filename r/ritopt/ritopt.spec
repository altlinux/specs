# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++ java-devel-default
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           ritopt
Version:        0.2.1
Release:        alt1_15jpp8
Summary:        A Java library for parsing command-line options
License:        GPLv2+
Group:          Development/Java
Url:            http://ritopt.sourceforge.net/
BuildArch:      noarch

Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-all.tar.gz
## Patch for javadoc build
Patch0:         %{name}-0.2.1-javadoc.patch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant
BuildRequires: /usr/bin/latex texlive-latex-recommended

Requires: javapackages-tools rpm-build-java
Source44: import.info

%description
Ritopt is an options parser for the Java programming language

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch
%description javadoc
Documentation for the ritopt library

%prep
%setup -q 
%{__sed} -i 's/\r//' NEWS
%{__sed} -i 's/\r//' ChangeLog
%{__sed} -i 's/\r//' AUTHORS
%{__sed} -i 's/\r//' README
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

