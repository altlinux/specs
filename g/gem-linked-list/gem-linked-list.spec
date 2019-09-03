%define  pkgname linked-list

Name:    gem-%pkgname
Version: 0.0.13
Release: alt1

Summary: Ruby implementation of Doubly Linked List, following some Ruby idioms.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/spectator/linked-list

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
%summary

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
%ruby_gemspec
%ruby_gemlibdir
%doc *.md

%files doc
%ruby_gemdocdir

%changelog
* Mon Sep 02 2019 Yuri N. Sedunov <aris@altlinux.org> 0.0.13-alt1
- first build for Sisyphus


