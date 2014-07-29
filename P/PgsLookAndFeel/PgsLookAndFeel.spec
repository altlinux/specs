# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		PgsLookAndFeel
Version:	1.1
Release:	alt1_8.20090805cvsjpp7
Summary:	Nice looking LookAndFeel for Swing
License:	ASL 2.0
Group:		Development/Java
URL:		https://pgslookandfeel.dev.java.net/

#This is a cvs snapshot, to get this tarball :
#if you don't have an account in https://www.dev.java.net, create an account via https://www.dev.java.net/servlets/Join
#otherwise set the cvs root and login : cvs -d :pserver:username@cvs.dev.java.net:/cvs login
#then to checkout the project source repository : cvs -d :pserver:username@cvs.dev.java.net:/cvs checkout pgslookandfeel
#this information was taken from https://www.dev.java.net/servlets/ProjectSource
#create the tarball : tar -cjvf PgsLookAndFeel-1.1.tar.bz2 pgslookandfeel

Source0:	%{name}-%{version}.tar.bz2
#Source1: LICENSE file, taken from upstream binary tarball
Source1:	LICENSE.txt
#Source2: README file, taken from upstream binary tarball
Source2:	README.txt

#Patch0: disable checking for a license of jide, since we are using an oss one
Patch0:		PgsLookAndFeel-PlafOptions.java.patch
#Patch1: use the system libraries instead of the provided ones
Patch1:		PgsLookAndFeel-build.xml.patch

BuildArch:	noarch

BuildRequires:	jpackage-utils
BuildRequires:	ant
BuildRequires:	laf-plugin
BuildRequires:	jide-oss

Requires:	jpackage-utils
Requires:	laf-plugin
Source44: import.info

%description
The PgsLookAndFeel is a nice looking LookAndFeel for Swing.

It aims be a very modern cross-platform LookAndFeel with
nice features and much interaction for users.

%package javadoc
Summary:	User documentation for PgsLookAndFeel
Group:		Development/Java
Requires:	%{name} = %{version}
BuildArch: noarch

%description javadoc
User documentation for %{name}.

%prep
%setup -q -n pgslookandfeel
%patch0 -p1
%patch1 -p1
#remove any existing compiled classes and jars
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.class' -exec rm -f '{}' \;

#remove CVS files and directories
rm -rf `find -name 'CVS'`

install -p -m 644 %{SOURCE1} .
install -p -m 644 %{SOURCE2} .

# copy resources (build.xml is missing this ...)
install -dm 755 classes/com/pagosoft/plaf/icons
cp -p src/com/pagosoft/plaf/icons/*.png \
	classes/com/pagosoft/plaf/icons
cp -p src/com/pagosoft/plaf/*.properties \
	classes/com/pagosoft/plaf

%build
%ant

%install
install -D -p -m 644 jar/%{name}.jar \
	%{buildroot}%{_javadir}/%{name}-%{version}.jar
install -D -p -m 644 jar/%{name}-jide.jar \
	%{buildroot}%{_javadir}/%{name}-jide-%{version}.jar

install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -rf -p www/* %{buildroot}%{_javadocdir}/%{name}

pushd %{buildroot}%{_javadir}
	for jar in *-%{version}*; do
		ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
	done
popd

%files
%doc *.txt
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_8.20090805cvsjpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_7.20090805cvsjpp7
- new version

