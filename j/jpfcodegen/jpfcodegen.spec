# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jpfcodegen
Version:        0.4
Release:        alt1_11jpp8
Summary:        A tool for generating classes from JPF plug-ins

Group:          Development/Java
License:        LGPLv3
URL:            https://github.com/JabRef/jpfcodegen

BuildArch:      noarch
# svn export https://jabref.svn.sourceforge.net/svnroot/jabref/tags/jpfcodegen-0.4
# tar cvfj jpfcodegen-0.4.tbz jpfcodegen-0.4
Source0:        %{name}-%{version}.tbz
# Fix the build to use system jars
Patch0:         %{name}-build.patch
# Fix the build on javadoc
Patch1:         %{name}-javadoc.patch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant
BuildRequires:  jpf
BuildRequires:  velocity

Requires: javapackages-tools rpm-build-java
Source44: import.info

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch
%description javadoc
%{summary}.

%description
JPF Code Generator is a handy little tool that generates classes for
accessing the attributes and extensions of JPF plug-ins from plugin.xml
files. This has the advantage of providing a strongly typed access to the
plug-in and simplifies working with plug-ins.


%prep
%setup -q
%{__rm} -rf lib
%patch0 -b .build -p0
%patch1 -b .javadoc -p0
find tutorials -type f -exec sed -i 's/\r//' '{}' \;

%build
export CLASSPATH=`build-classpath jpf jpf-boot commons-logging velocity`
ant -v jars

# Generate the javadoc
mkdir javadoc
javadoc -d javadoc src/net/sf/jabref/plugin/util/*.java

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 JPFCodeGenerator-0.4.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -pm 644 JPFCodeGenerator-0.4-rt.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-rt.jar

install -d -m 755 ${RPM_BUILD_ROOT}%{_javadocdir}/
cp -r javadoc ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}

%files
%{_javadir}/*.jar
%doc lgpl-3.0.txt index.html tutorials/

%files javadoc
%doc lgpl-3.0.txt
%{_javadocdir}/%{name}


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_11jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_10jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_5jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_4jpp7
- new version

