%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    devel
%define        gemname jekyll-theme-minimal

Name:          gem-jekyll-theme-minimal
Version:       0.2.0
Release:       alt1
Summary:       Minimal is a Jekyll theme for GitHub Pages
License:       CC0-1.0
Group:         Development/Ruby
Url:           https://github.com/pages-themes/minimal
Vcs:           https://github.com/pages-themes/minimal.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(html-proofer) >= 3.0
BuildRequires: gem(jekyll) > 3.5
BuildRequires: gem(jekyll-seo-tag) >= 2.0
BuildRequires: gem(rubocop-github) >= 0.16
BuildRequires: gem(w3c_validators) >= 1.3
BuildConflicts: gem(html-proofer) >= 6
BuildConflicts: gem(jekyll) >= 5.0
BuildConflicts: gem(jekyll-seo-tag) >= 3
BuildConflicts: gem(rubocop-github) >= 1
BuildConflicts: gem(w3c_validators) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency html-proofer >= 5.0.0,html-proofer < 6
Requires:      ruby >= 2.4.0
Requires:      gem(jekyll) > 3.5
Requires:      gem(jekyll-seo-tag) >= 2.0
Conflicts:     gem(jekyll) >= 5.0
Conflicts:     gem(jekyll-seo-tag) >= 3
Provides:      gem(jekyll-theme-minimal) = 0.2.0

%ruby_use_gem_version jekyll-theme-minimal:0.2.0

%description
Minimal is a Jekyll theme for GitHub Pages


%if_enabled    devel
%package       -n gem-jekyll-theme-minimal-devel
Version:       0.2.0
Release:       alt1
Summary:       Minimal is a Jekyll theme for GitHub Pages development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jekyll-theme-minimal
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jekyll-theme-minimal) = 0.2.0
Requires:      gem(html-proofer) >= 3.0
Requires:      gem(rubocop-github) >= 0.16
Requires:      gem(w3c_validators) >= 1.3
Conflicts:     gem(html-proofer) >= 6
Conflicts:     gem(rubocop-github) >= 1
Conflicts:     gem(w3c_validators) >= 2

%description   -n gem-jekyll-theme-minimal-devel
Minimal is a Jekyll theme for GitHub Pages development package.

%description   -n gem-jekyll-theme-minimal-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета jekyll-theme-minimal.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    devel
%files         -n gem-jekyll-theme-minimal-devel
%doc LICENSE README.md
%endif


%changelog
* Mon Jan 27 2025 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
