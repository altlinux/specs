BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jnr-constants
Version:        0.7
Release:        alt1_4jpp7
Summary:        Java Native Runtime constants 
Group:          Development/Java
License:        MIT
URL:            http://github.com/wmeissner/jnr-constants/
Source0:        http://download.github.com/wmeissner-jnr-constants-0.7-0-g8b45ca7.tar.gz
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  jpackage-utils
Requires:       jpackage-utils
Source44: import.info

%description
Provides java values for common platform C constants (e.g. errno).

%prep
%setup -q -n wmeissner-%{name}-8b45ca7
find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
ant jar

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}

# project was renamed from 'constantine' to jnr-constants, but jar has
# yet to be renamed http://fedoraproject.org/wiki/Packaging/Java#Jar_file_naming
cp -p dist/constantine.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/constantine.jar

%files
%doc LICENSE
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/constantine.jar

%changelog
* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_4jpp7
- new version

