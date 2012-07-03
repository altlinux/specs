# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:       simplevalidation
# upstream is pretty bad about version numbering
# this is a guess based on the version of a separate api "release" jar
Version:    0.4
Release:    alt1_1jpp6
Summary:    A library for adding user-interface input validation to Swing applications
Group:      Development/Java
License:    GPLv2 or CDDL
URL:        http://kenai.com/projects/simplevalidation
Source0:    http://kenai.com/projects/simplevalidation/downloads/download/validation-src.zip

BuildArch:  noarch

BuildRequires:  jpackage-utils

BuildRequires:  ant
BuildRequires:  dos2unix

Requires:   jpackage-utils
Source44: import.info

%description
This is a simple library for quickly adding validation code to Swing
user-interfaces. It handles validating user input when the user changes a
component's value, showing error messages and decorating components to
indicate which component is the source of the problem. It contains a large
number of built-in validators to handle most common situations, such as
validating numbers, email addresses, urls and so forth.

The primary goal is to make it easy to retrofit validation code on existing
UIs without needing to rewrite anything or add more than a few lines of code.


%package javadoc
Summary:    Javadocs for %{name}
Group:      Development/Java
Requires:   jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}


%prep
%setup -q -c

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;


%build
cd ValidationAPI
ant -Dplatforms.JDK_1.5.home=/usr/lib/jvm/java jar

dos2unix dist/javadoc/package-list
dos2unix dist/javadoc/stylesheet.css


%install
mkdir -p %{buildroot}%{_javadir}
cp -a ValidationAPI/dist/ValidationAPI.jar %{buildroot}%{_javadir}/ValidationAPI.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a ValidationAPI/dist/javadoc %{buildroot}%{_javadocdir}/%{name}


%files
%doc ValidationAPI/doc/overview.html
%doc ValidationAPI/doc/duckLogo.png
%{_javadir}/ValidationAPI.jar

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_1jpp6
- new version

