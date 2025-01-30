%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubocop-jekyll

Name:          gem-rubocop-jekyll
Version:       0.14.0
Release:       alt1
Summary:       Code style check for Jekyll and Jekyll plugins
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jekyll/rubocop-jekyll
Vcs:           https://github.com/jekyll/rubocop-jekyll.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(jekyll) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 1.2
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      ruby >= 2.7.0
Provides:      gem(rubocop-jekyll) = 0.14.0

%description
A RuboCop extension to enforce common code style in Jekyll and Jekyll plugins


%if_enabled    doc
%package       -n gem-rubocop-jekyll-doc
Version:       0.14.0
Release:       alt1
Summary:       Code style check for Jekyll and Jekyll plugins documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-jekyll
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-jekyll) = 0.14.0

%description   -n gem-rubocop-jekyll-doc
Code style check for Jekyll and Jekyll plugins documentation files.

A RuboCop extension to enforce common code style in Jekyll and Jekyll plugins

%description   -n gem-rubocop-jekyll-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-jekyll.
%endif


%if_enabled    devel
%package       -n gem-rubocop-jekyll-devel
Version:       0.14.0
Release:       alt1
Summary:       Code style check for Jekyll and Jekyll plugins development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-jekyll
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-jekyll) = 0.14.0
Requires:      gem(jekyll) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 1.2
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2

%description   -n gem-rubocop-jekyll-devel
Code style check for Jekyll and Jekyll plugins development package.

A RuboCop extension to enforce common code style in Jekyll and Jekyll plugins

%description   -n gem-rubocop-jekyll-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-jekyll.
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
%doc LICENSE README.md History.markdown
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rubocop-jekyll-doc
%doc LICENSE README.md History.markdown
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubocop-jekyll-devel
%doc LICENSE README.md History.markdown
%endif


%changelog
* Mon Jan 27 2025 Pavel Skrylev <majioa@altlinux.org> 0.14.0-alt1
- ^ 0.11.0 -> 0.14.0

* Tue Sep 14 2021 Pavel Skrylev <majioa@altlinux.org> 0.11.0-alt1
- + packaged gem with Ruby Policy 2.0
