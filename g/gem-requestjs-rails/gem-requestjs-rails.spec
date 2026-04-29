%define _unpackaged_files_terminate_build 1
%define  pkgname requestjs-rails

Name:    gem-%pkgname
Version: 0.0.14
Release: alt1

Summary: Request.JS for Rails
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rails/requestjs-rails
VCS:     https://github.com/rails/requestjs-rails

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-ruby
BuildRequires: rpm-build-ruby

%description
Rails Request.JS encapsulates the logic to send by default some headers that are required by rails applications like the `X-CSRF-Token`.

%package doc
Summary: Documentation files for %name gem
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup

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
* Tue Apr 28 2026 Artem Semenov <savoptik@altlinux.org> 0.0.14-alt1
- Initial build for Sisyphus
