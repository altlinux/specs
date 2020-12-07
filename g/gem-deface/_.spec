# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname deface

Name:          gem-%pkgname
Version:       1.5.3
Release:       alt1
Summary:       Rails plugin that allows you to customize ERB views
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/spree/deface
Vcs:           https://github.com/spree/deface.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Rails plugin that allows you to customize ERB views in a Rails application
without editing the underlying view.

It allows you to easily target html & erb elements as the hooks for
customization using CSS selectors as supported by Nokogiri.


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
* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 1.5.3-alt1
- + packaged gem with usage Ruby Policy 2.0
