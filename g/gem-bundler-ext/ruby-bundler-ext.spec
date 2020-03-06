%define        pkgname bundler-ext
%define        gemname bundler_ext

Name:          gem-%pkgname
Version:       0.4.0
Release:       alt2
Summary:       Simple library leveraging the Bundler Gemfile DSL
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bundlerext/bundler_ext
Vcs:           https://github.com/bundlerext/bundler_ext.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
Simple library leveraging the Bundler Gemfile DSL to load gems already on the
system and managed by the systems package manager (like yum/apt).

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
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt2
- > Ruby Policy 2.0
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus
