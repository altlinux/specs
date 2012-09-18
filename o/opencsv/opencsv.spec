BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           opencsv
Version:        2.3
Release:        alt1_3jpp7
Summary:        A very simple csv (comma-separated values) parser library for Java
Group:          Development/Java
License:        ASL 2.0
URL:            http://opencsv.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src-with-libs.tar.gz
BuildArch:      noarch

BuildRequires:     jpackage-utils
BuildRequires:     ant
BuildRequires:     junit
BuildRequires:     ant-junit
Requires:          jpackage-utils
Source44: import.info

%description
Support for all the basic csv-type things you're likely to want to do.


%package javadoc
Summary:           Javadocs for opencsv
Group:             Development/Java
Requires:          %{name} = %{version}-%{release}
Requires:          jpackage-utils
BuildArch: noarch

%description javadoc
opencsv development documentation.


%prep
%setup -q # -n %{name}-%{version}

### making sure we dont use it
rm -rf lib/* doc deploy

ln -s %{_javadir}/junit4.jar lib/

%{__sed} -i 's/\r//' examples/MockResultSet.java
%{__sed} -i 's/\r//' examples/JdbcExample.java
%{__sed} -i 's/\r//' examples/addresses.csv
%{__sed} -i 's/\r//' examples/AddressExample.java


%build
ant jar # includes clean & build
#ant test # not JDK >=1.6.0 compatible
ant javadoc


%install

# jar
install -d $RPM_BUILD_ROOT%{_javadir}
install -m644 deploy/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -rp doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%doc examples
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%files javadoc
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/%{name}-%{version}/*


%changelog
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_3jpp7
- new version

