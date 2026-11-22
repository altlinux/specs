%define _unpackaged_files_terminate_build 1

Name: kaverit
Version: 2.14.0
Release: alt1

Summary: Kotlin type token and reflection library
License: Apache-2.0
Group: Development/Java
URL: https://github.com/kosi-libs/Kosi-Kaverit
VCS: https://github.com/kosi-libs/kaverit

Source0: %name-%version.tar
Patch0: %name-system.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlin-test
BuildRequires: mvn(junit:junit)

BuildArch: noarch

%description
Kaverit is a Kotlin type-token library for representing JVM types and their
optional generic parameters.

%prep
%setup -q
%patch0 -p1

if [ "$(getconf LONG_BIT)" = 32 ]; then
    sed -i \
        -e '/^org\.gradle\.jvmargs/s/-Xmx4g/-Xmx768m/' \
        -e 's/MaxMetaspaceSize=2g/MaxMetaspaceSize=384m/' \
        gradle.properties
fi

%build
%gradle_publish

%install
%gradle_register --artifacts=kaverit-jvm
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE.txt

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 2.14.0-alt1
- Initial build for ALT.
