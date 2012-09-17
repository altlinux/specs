BuildRequires: /proc
BuildRequires: jpackage-compat
Name: inamik-tableformatter
Version: 0.96.2
Release: alt1_5jpp7
Summary: A set of Java classes to print text in tabulated form
License: GPLv2+
Group: Development/Java
URL: http://trac.inamik.com/trac/jtable_format
# Downloaded manually from http://download.inamik.com/jtable_format/
Source0: com.inamik.utils.tableformatter-%{version}-src.tar.gz
Patch0: inamik-tableformatter-buildfixes.patch
BuildArch: noarch
BuildRequires: jpackage-utils
BuildRequires: ant
Requires: jpackage-utils
Source44: import.info

%description
A set of Java classes to print text in tabulated form. With these
classes you can organize 'cells' of data into rows and columns. Each
cell can contain multiple lines of text and may specify a horizontal
alignment (left, center, right) and a vertical alignment (top, center,
bottom). When you are ready to print the data, these classes will
ensure that all cells in a given column have the same width and all
cells in a given row have the same height.

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n com.inamik.utils.tableformatter-%{version}
%patch0 -p1 -b .buildfixes

%build
ant

# Sanitize line endings
find -name \*.txt -print0 | xargs -0 -e sed -i 's/\r//'
sed -i 's/\r//' TestTableFormatter.java

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/com.inamik.utils.tableformatter-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/com.inamik.utils.tableformatter.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rf javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE.txt README.txt TODO.txt VERSION.txt TestTableFormatter.java
%{_javadir}/*

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.96.2-alt1_5jpp7
- new version

