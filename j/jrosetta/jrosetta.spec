BuildRequires: maven-assembly-plugin
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jrosetta
Version:        1.0.4
Release:        alt2_14jpp8
Summary:        A common base to build a graphical console

Group:          Development/Other
License:        GPLv2
URL:            http://dev.artenum.com/projects/JRosetta
Source0:        http://maven.artenum.com/content/groups/public/com/artenum/%{name}/%{version}/%{name}-%{version}-sources.jar

BuildArch:      noarch

BuildRequires:  maven-local

Requires:       java
Source44: import.info

%description
JRosetta provides a common base for graphical component that could be used
to build a graphical console in Swing with the latest requirements, such as
command history, completion and so on for instance for scripting language
or command line.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
# remove jar format related directory
rm -fr ../META-INF
#wrong-file-end-of-line-encoding
cp -p CHANGE.txt CHANGE.txt.CRLF
sed -i -e 's/\r//' CHANGE.txt
touch -r CHANGE.txt.CRLF CHANGE.txt
rm CHANGE.txt.CRLF
# remove deployement dependency
%pom_xpath_remove "pom:build/pom:extensions" pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt COPYRIGHT.txt CHANGE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_14jpp8
- added BR: maven-assembly-plugin for javapackages 5

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_14jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_13jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_12jpp8
- new version

* Fri Aug 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_7jpp7
- re-imported for xmvn migration

* Fri Apr 19 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- New version (ALT #28870)
- Build by maven

* Thu Sep 10 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt2
- Fix BuildRequires (ALT #21518)

* Thu Jul 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1
- initial from Fedora

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 kwizart < kwizart at gmail.com > - 1.0.2-1
- Fix License (GPLv2 only)
- Fix Summary
- Update to 1.0.2 - previous patch merged upstream

* Mon Oct 27 2008 kwizart < kwizart at gmail.com > - 1.0.1-1
- Initial Package

