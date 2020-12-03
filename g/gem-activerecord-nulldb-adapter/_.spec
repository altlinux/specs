# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname activerecord-nulldb-adapter

Name:          gem-%pkgname
Version:       0.5.1
Release:       alt1
Summary:       An ActiveRecord null database adapter for greater speed and isolation in unit tests
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/nulldb/nulldb
Vcs:           https://github.com/nulldb/nulldb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.

A database backend that translates database interactions into no-ops. Using
NullDB enables you to test your model business logic - including after_save
hooks - without ever touching a real database.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --use=%gemname --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Thu Dec 03 2020 Pavel Skrylev <majioa@altlinux.org> 0.5.1-alt1
- + packaged gem with usage Ruby Policy 2.0
