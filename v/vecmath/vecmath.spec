BuildRequires: /proc
BuildRequires: jpackage-compat
%global tardate 20090922

Name:		vecmath
Version:	0
Release:	alt1_5.20090922cvsjpp7
Summary:	The 3D vector math Java package, javax.vecmath
Group:		Development/Java
# License is GNU General Public License, version 2, with the Classpath Exception
License:	GPLv2 with exceptions
URL:		https://vecmath.dev.java.net/
## Source pulled from upstream CVS.
# https://vecmath.dev.java.net/servlets/ProjectSource
## Tarball created with
## (you need to create a username)
# cvs -d :pserver:username@cvs.dev.java.net:/cvs login
# cvs -d :pserver:username@cvs.dev.java.net:/cvs checkout vecmath
# tar cf vecmath-%{tardate}.tar vecmath
# xz vecmath-%{tardate}.tar
Source0:	%{name}-%{tardate}.tar.bz2
BuildArch:	noarch

BuildRequires:	ant
BuildRequires:	jpackage-utils

Requires:	jpackage-utils
Source44: import.info

%description
The 3D vector math Java package, javax.vecmath.

%prep
%setup -q -n %{name}
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
ant

%install
install -D -p -m 644 build/debug/lib/ext/vecmath.jar %{buildroot}%{_javadir}/vecmath.jar

%files
%doc docs/api-changes* LICENSE.txt LICENSE-SPEC.html
%{_javadir}/vecmath.jar

%changelog
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt1_5.20090922cvsjpp7
- new version

