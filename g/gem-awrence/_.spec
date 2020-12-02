# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname awrence

Name:          gem-%pkgname
Version:       1.1.1
Release:       alt1
Summary:       Camelize your snake keys when working with JSON APIs
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/futurechimp/awrence
Vcs:           https://github.com/futurechimp/awrence.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Have you ever needed to automatically convert Rubyish snake_case to JSON-style
camelBack or CamelCase hash keys?

Awrence to the rescue.

This gem recursively converts all snake_case keys in a hash structure to
camelBack or CamelCase.


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
%ruby_build

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
* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with usage Ruby Policy 2.0
