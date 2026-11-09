%define latestver 27

Name: java-latest
Version: 1
Release: alt1

Summary: chooser of latest ALT Linux java compiler
Group: Development/Java
License: GPL2+ or Apache
Url: http://openjdk.org

ExclusiveArch: %java_arches

Requires(pre): java-%latestver-openjdk

BuildRequires(pre): rpm-macros-java    

%description
The virtual package provides dependencies on the latest
released version of the openjdk packages.

These packages are not recommended for use in production
environments or for building packages that require an LTS
version.

%files
%define jdkpackage() \
%package -n java-%1-latest \
Summary: %1 latest component of JDK \
ExclusiveArch: %java_arches \
Group: Development/Java \
Requires(pre): java-%latestver-openjdk-%1 \
\
%description -n java-%1-latest \
%1 latest component of JDK. \
\
%files -n java-%1-latest \
\

%jdkpackage demo
%jdkpackage devel
%jdkpackage headless
%jdkpackage javadoc
%jdkpackage jmods
%jdkpackage sources

%changelog
* Mon Nov 09 2026 Artem Semenov <savoptik@altlinux.org> 1-alt1
- initial build for ALT Sisyphus.
