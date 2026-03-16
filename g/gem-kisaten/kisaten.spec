%define _unpackaged_files_terminate_build 1
%define pkgname kisaten

Name:    gem-kisaten
Version: 0.1
Release: alt1

Summary: Ruby MRI extension for fuzzing Ruby code with afl-fuzz
License: MIT
Group:   Development/Ruby
Url:     https://github.com/twistlock/kisaten
VCS:     https://github.com/twistlock/kisaten

Provides: %pkgname = %EVR

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-ruby
BuildRequires: rpm-build-ruby
BuildRequires: gem-rake-compiler

%description
Kisaten is a Ruby extension that enables fuzzing instrumented Ruby code.
It implements a fork server and instrumentation that relies on AFL american fuzzy lop.

%package doc
Summary: Doc files fore %name
Group: Documentation
BuildArch: noarch

%description doc
%summary

%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspecdir/%pkgname-%version.gemspec
%ruby_gemslibdir/%pkgname-%version
%ruby_gemsextdir/%pkgname-%version

%files doc
%doc *.md doc
%ruby_gemsdocdir/%pkgname-%version

%changelog
* Wed Mar 11 2026 Artem Semenov <savoptik@altlinux.org> 0.1-alt1
- Initial build for Sisyphus
