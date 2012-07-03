# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           clapham
Version:        0.1.003
Release:        alt1_5jpp7
Summary:        Railroad diagram generator for computer languages
URL:            http://clapham.hydromatic.net/
License:        GPLv2
# NOTE: Clapham is not under a GPLv2+ license, because it only allows
# use of later versions if they are "approved by The Eigenbase Project".
Group:          Engineering

Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.zip
Source1:        %{name}.sh

# Remove use of Apache Ivy, unnecessary to build Fedora RPM:
Patch0:         %{name}-noivy.patch

# Set library paths for Fedora:
Patch1:         %{name}-libdir.patch

# Replace gratuitous use of Microsoft Word (non-Unicode) character codes in
# a source file:
Patch2:         %{name}-msword.patch

BuildArch:      noarch

BuildRequires:  dos2unix
BuildRequires:  batik javacc
BuildRequires:  ant ant-nodeps jpackage-utils

Requires:       batik xml-commons-apis
Requires:       jpackage-utils
Source44: import.info


%description
Clapham is an open-source railroad diagram generator.
Railroad diagrams are a graphical way of representing the grammar of a
computer language. When a computer language is large, even people who
use the language day-to-day have trouble remembering its nuances. A
railroad diagram represents the grammar visually, and is easier to
understand by non- or semi-technical users.

%package javadoc
Group: Engineering
Summary:        Javadocs for clapham
Requires:       %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains the API documentation for the Clapham railroad
diagram generator.

%prep
%setup -q
%patch0 -p1 -b .noivy
%patch1 -p1 -b .libdir
%patch2 -p1 -b .msword
rm ivy.xml ivysettings.xml
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
dos2unix README.txt

%build
ant jar javadoc

%install
mkdir -p %{buildroot}%{_javadir}
install -m644 %{name}.jar %{buildroot}%{_javadir}/
mkdir -p %{buildroot}%{_bindir}
install -m644 %{SOURCE1} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_javadocdir}
cp -a doc/api %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%attr(755, root, root) %{_bindir}/%{name}
%doc README.txt
%doc VERSION.txt
# example input files:
%doc testsrc/net/hydromatic/%{name}/example/*.bnf
%doc testsrc/net/hydromatic/%{name}/example/*.java
# example code:
%doc testsrc/net/hydromatic/%{name}/test/*.java

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.003-alt1_5jpp7
- new version

