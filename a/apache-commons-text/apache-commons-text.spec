%define _unpackaged_files_terminate_build 1
%define jarname commons-text
 
Name:    apache-%jarname
Version: 1.13.1
Release: alt1
Summary: Apache Commons Text is a library focused on algorithms working on strings

License: Apache-2.0
Group: Development/Java
URL: https://commons.apache.org/proper/%jarname

Source0: https://archive.apache.org/dist/commons/text/source/%jarname-%version-src.tar.gz

BuildArch: noarch
 
BuildRequires: maven-local
BuildRequires: jpackage-generic-compat
BuildRequires: mvn(org.apache.commons:commons-parent:pom:)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.mockito:mockito-core)
 
%description
The Commons Text library provides additions to the standard JDK's text handling.
Our goal is to provide a consistent set of tools for processing text generally
from computing distances between Strings to being able to efficiently do String
escaping of various types.

#{?javadoc_package}

%prep
%setup -n %jarname-%version-src
	
# delete precompiled jar and class files
find -type f '(' -name '*.jar' -o -name '*.class' ')' -print -delete
 
# mockito-inline was merged into mockito-core
%pom_change_dep :mockito-inline :mockito-core

%build
# Architecture-specific javadoc
%mvn_build -f --skip-javadoc
 
%install
%mvn_install
%files -f .mfiles
%doc README.md RELEASE-NOTES.txt LICENSE.txt NOTICE.txt

%changelog
* Wed Apr 23 2025 Andrey Cherepanov <cas@altlinux.org> 1.13.1-alt1
- Initial build for Sisyphus.
