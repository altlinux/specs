%define _unpackaged_files_terminate_build 1

Name: colormath
Version: 3.7.1
Release: alt1

Summary: Kotlin color space conversion library
License: MIT
Group: Development/Java
URL: https://github.com/ajalt/colormath
VCS: https://github.com/ajalt/colormath

Source0: %name-%version.tar
Patch0: %name-%version.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-gradle-plugin)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit)
BuildRequires: mvn(junit:junit)

BuildArch: noarch

%description
Colormath converts between color spaces and provides color manipulation tools.
This package contains the Kotlin common metadata and JVM library artifacts.

%prep
%setup -q
%patch0 -p1

if [ "$(getconf LONG_BIT)" = 32 ]; then
    sed -i \
        -e '/^org\.gradle\.jvmargs/s/-Xmx4g/-Xmx768m/' \
        -e '/^kotlin\.daemon\.jvmargs/s/-Xmx4g/-Xmx512m/' \
        gradle.properties
fi

%build
%gradle_publish

%install
%gradle_register --artifacts=colormath
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 3.7.1-alt1
- Initial build for ALT.
