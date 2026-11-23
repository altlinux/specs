%define _unpackaged_files_terminate_build 1

Name: korlibs-encoding
Version: 6.1.0
Release: alt1

Summary: Kotlin encoding utilities from Korlibs
License: MIT
Group: Development/Java
URL: https://github.com/korlibs/korlibs-encoding
VCS: https://github.com/korlibs/korlibs-encoding.git

Source: %name-%version.tar
Source1: LICENSE
Patch0: 0001-Build-the-Common-and-JVM-publications.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-gradle-plugin)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit)
BuildRequires: mvn(junit:junit)

%description
Korlibs Encoding provides common and JVM encoding utilities, including ASCII,
Base64, and hexadecimal encoders and decoders.

%prep
%setup -q
%autopatch -p1
cp %SOURCE1 LICENSE

# Detect the 32-bit x86 build environment for this noarch RPM.
case "$(uname -m):$(getconf LONG_BIT)" in
    i?86:32|x86_64:32)
        sed -i \
            -e 's/^org\.gradle\.jvmargs=.*/org.gradle.jvmargs=-Xmx1024m/' \
            -e '/^kotlin\.daemon\.jvmargs=/d' \
            gradle.properties
        printf '%s\n' 'kotlin.compiler.execution.strategy=in-process' \
            'org.gradle.workers.max=1' >> gradle.properties
        ;;
esac

%build
%gradle_publish -PkorlibsVersion=%version

%install
%gradle_register --artifacts=korlibs-encoding,korlibs-encoding-jvm
%gradle_install

%check
%gradle_check -PkorlibsVersion=%version

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 6.1.0-alt1
- Initial build for ALT.
