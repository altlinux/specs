%def_disable snapshot

%define binary_name sass
%define _name dart-%binary_name
%define ver_major 1.101
%define import_path sass-sass
%define sass_version 3.1.0

%def_disable bootstrap

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: The reference implementation of Sass, written in Dart.
License: MIT
Group: Text tools
Url: https://sass-lang.com/dart-sass/

Vcs: https://github.com/sass/dart-sass.git

%if_disabled snapshot
Source: https://github.com/sass/dart-sass/archive/%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
%{?_disable_bootstrap:Source1: %_name-%version-vendor.tar}
# https://github.com/sass/sass.git
Source2: sass-%sass_version.tar

ExcludeArch: %ix86

#BuildRequires(pre): rpm-build-dartlang
BuildRequires: /proc buf
BuildRequires: dart-lang-sdk

%description
%{summary}.

%prep
%setup -n %_name-%version %{?_disable_bootstrap: -a1} -a2
export PUB_CACHE="${PWD}/.pub_cache"
%{?_enable_bootstrap:
dart --disable-analytics
dart pub get
dart pub outdated
tar -cf %_sourcedir/%_name-%version-vendor.tar pubspec.lock .dart_tool .pub_cache build}

mkdir -p build
  ln -sf ../sass-%sass_version build/language

%build
export PUB_CACHE="${PWD}/.pub_cache"
dart pub get --offline
UPDATE_SASS_PROTOCOL=false dart run grinder protobuf
dart compile exe \
    -Dversion=%version \
    -Dprotocol-version=$(cat build/language/spec/EMBEDDED_PROTOCOL_VERSION) \
    -o %binary_name \
    bin/%binary_name.dart

%install
# binary
install -vDm755 -t %buildroot%_bindir %binary_name
# embedded-protocol protobuf file
install -vDm644 -t %buildroot/%_datadir/%_name build/language/spec/embedded_sass.proto

%files
%_bindir/%binary_name
%_datadir/%_name/
%doc *.md

%changelog
* Wed Jun 17 2026 Yuri N. Sedunov <aris@altlinux.org> 1.101.0-alt1
- 1.101.0

* Fri May 22 2026 Yuri N. Sedunov <aris@altlinux.org> 1.100.0-alt1
- 1.100.0

* Fri Apr 03 2026 Yuri N. Sedunov <aris@altlinux.org> 1.99.0-alt1
- 1.99.0

* Sat Mar 21 2026 Yuri N. Sedunov <aris@altlinux.org> 1.98.0-alt1
- 1.98.0

* Wed Feb 04 2026 Yuri N. Sedunov <aris@altlinux.org> 1.97.3-alt1
- 1.97.3

* Tue Jan 20 2026 Yuri N. Sedunov <aris@altlinux.org> 1.97.2-alt1
- 1.97.2

* Thu Dec 04 2025 Yuri N. Sedunov <aris@altlinux.org> 1.94.2-alt1
- 1.94.2

* Tue Aug 26 2025 Yuri N. Sedunov <aris@altlinux.org> 1.91.0-alt1
- 1.91.0

* Mon Aug 11 2025 Yuri N. Sedunov <aris@altlinux.org> 1.90.0-alt1
- 1.90.0

* Fri Jun 13 2025 Yuri N. Sedunov <aris@altlinux.org> 1.89.2-alt1
- first build for Sisyphus



