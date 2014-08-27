Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          glassfish-legal
Version:       1.1
Release:       alt1_3jpp7
Summary:       Legal License for glassfish code
License:       CDDL or GPLv2 with exceptions
URL:           http://glassfish.java.net/
# svn export https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/ glassfish-legal-1.1
# tar czf glassfish-legal-1.1-src-svn.tar.gz glassfish-legal-1.1
Source0:       %{name}-%{version}-src-svn.tar.gz


BuildRequires: glassfish-master-pom
BuildRequires: maven-local
BuildRequires: maven-remote-resources-plugin

Requires:      glassfish-master-pom
BuildArch:     noarch
Source44: import.info

%description
An archive which contains license files for glassfish code.

%prep
%setup -q -n %{name}-%{version}

sed -i 's/\r//' src/main/resources/META-INF/LICENSE.txt
cp -p src/main/resources/META-INF/LICENSE.txt .

%build

%mvn_file :legal %{name}
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%changelog
* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3jpp7
- new release

