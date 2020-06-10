# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname echoe

Name:          gem-%pkgname
Version:       4.6.6
Release:       alt1
Summary:       A Rubygems packaging tool that provides Rake tasks for documentation, extension compiling, testing, and deployment
License:       AFL-3.0 and MIT
Group:         Development/Ruby
Url:           https://github.com/evan/echoe
Vcs:           https://github.com/evan/echoe.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.


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
* Mon Apr 13 2020 Pavel Skrylev <majioa@altlinux.org> 4.6.6-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
