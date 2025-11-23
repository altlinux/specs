%define _unpackaged_files_terminate_build 1
%def_with check

Name: plumelib-options
Version: 2.0.3
Release: alt1

Summary: Command-line option processing for Java
License: MIT
Group: Development/Java
Url: https://github.com/plume-lib/options
Vcs: https://github.com/plume-lib/options.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: jpackage-default
BuildRequires: xgradle
BuildRequires: checker-qual
BuildRequires: apache-commons-lang3
BuildRequires: apache-commons-text
BuildRequires: classgraph
BuildRequires: plumelib-reflection-util
%if_with check
BuildRequires: junit5
%endif

%description
Thus, the programmer is freed from writing duplicative, boilerplate code. The
user documentation is automatically generated and never gets out of sync with
the rest of the program.

The programmer does not have to write any code, only declare and document
variables. For each field that you want to set from a command-line argument,
you write Javadoc and an @Option annotation. Then, the field is automatically
set from a command-line option of the same name, and usage messages and printed
documentation are generated automatically.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register

%gradle_install

%check
%gradle_check -Dfile.encoding=UTF-8

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Sun Nov 23 2025 Ivan Khanas <xeno@altlinux.org> 2.0.3-alt1
- First build for ALT.
