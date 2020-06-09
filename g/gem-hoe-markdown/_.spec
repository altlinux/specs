# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname hoe-markdown

Name:          gem-%pkgname
Version:       1.1.0
Release:       alt1
Summary:       Hoe (rubygem) plugin to hyperlink your markdown documentation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/flavorjones/hoe-markdown
Vcs:           https://github.com/flavorjones/hoe-markdown.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Hoe plugin with markdown helpers, for example to hyperlink github issues and
github usernames in markdown files.

Hoe::Markdown is a Hoe plugin to help manage your project's markdown files. It's
intended for gem maintainers, but the underlying library of markdown
manipulation methods might be generally useful.


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
* Tue Jun 9 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with usage Ruby Policy 2.0
