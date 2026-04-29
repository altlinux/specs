%define  pkgname html-pipeline
%define _unpackaged_files_terminate_build 1

Name:    gem-%pkgname
Version: 2.14.3
Release: alt1

Summary: HTML processing filters and utilities
License: MIT
Group:   Development/Ruby
Url:     https://github.com/jch/html-pipeline
VCS:     https://github.com/jch/html-pipeline

BuildArch: noarch

Source: %pkgname-%version.tar

BuildRequires(pre): rpm-macros-ruby
BuildRequires: rpm-build-ruby

%description
HTML processing filters and utilities. This module is a small
framework for defining CSS-based content filters and applying them to user
provided content.

%package doc
Summary: Documentation files for %name gem
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc *.md
%ruby_gemspec
%ruby_gemlibdir

%files doc
%ruby_gemdocdir

%changelog
* Tue Apr 28 2026 Artem Semenov <savoptik@altlinux.org> 2.14.3-alt1
- Initial build for Sisyphus
