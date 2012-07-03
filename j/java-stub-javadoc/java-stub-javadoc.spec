Packager: Igor Vlasenko <viy@altlinux.ru>
Name: java-stub-javadoc
Version: 0.1
Release: alt1

Summary: fake java-javadoc package
Group: Development/Java
License: Apache
URL: https://www.zarb.org/pipermail/jpackage-discuss/2005-May/007893.html

Requires(post,preun): alternatives >= 0.4
Provides: java-javadoc = %version
Obsoletes: java-javadoc = 0.1-alt1

#Source: %name-%version-src.tar.bz2
BuildArch: noarch
BuildRequires: rpm-build-java

%description
fake java-javadoc package is required for succesfull javadoc 
linkage in abcence of native manuals. Note that native java manuals 
from Sun are non-distributable, though the openjdk's ones are.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%name
#install -m 644 #{SOURCE0} $RPM_BUILD_ROOT%{_javadocdir}/%name
touch $RPM_BUILD_ROOT%{_javadocdir}/%name/package-list

%__install -d -m 755 %buildroot%_altdir
cat <<EOF > %buildroot%_altdir/%name
%_javadocdir/java	%_javadocdir/%name	10
EOF

%files
%doc 
%_javadocdir/%name
%_altdir/%name

%changelog
* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1
- name is changed not to shadow java-1.6.0-openjdk-javadoc
