%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname jekyll-seo-tag

Name:          gem-jekyll-seo-tag
Version:       2.8.0
Release:       alt1
Summary:       A Jekyll plugin to add metadata tags for search engines and social networks to better index and display your site's content
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jekyll/jekyll-seo-tag
Vcs:           https://github.com/jekyll/jekyll-seo-tag.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.15
%if_enabled check
BuildRequires: gem(html-proofer) >= 3.7
BuildRequires: gem(jekyll) >= 3.8
BuildRequires: gem(rspec) >= 3.5
BuildRequires: gem(rubocop-jekyll) >= 0.12.0
BuildConflicts: gem(html-proofer) >= 6
BuildConflicts: gem(jekyll) >= 5.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop-jekyll) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop-jekyll >= 0.15,rubocop-jekyll < 1
%ruby_use_gem_dependency html-proofer >= 5.0.0,html-proofer < 6
Requires:      ruby >= 2.5.0
Requires:      gem(jekyll) >= 3.8
Conflicts:     gem(jekyll) >= 5.0
Provides:      gem(jekyll-seo-tag) = 2.8.0

%description
A Jekyll plugin to add metadata tags for search engines and social networks to
better index and display your site's content.


%if_enabled    doc
%package       -n gem-jekyll-seo-tag-doc
Version:       2.8.0
Release:       alt1
Summary:       A Jekyll plugin to add metadata tags for search engines and social networks to better index and display your site's content documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jekyll-seo-tag
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jekyll-seo-tag) = 2.8.0

%description   -n gem-jekyll-seo-tag-doc
A Jekyll plugin to add metadata tags for search engines and social networks to
better index and display your site's content documentation files.

%description   -n gem-jekyll-seo-tag-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jekyll-seo-tag.
%endif


%if_enabled    devel
%package       -n gem-jekyll-seo-tag-devel
Version:       2.8.0
Release:       alt1
Summary:       A Jekyll plugin to add metadata tags for search engines and social networks to better index and display your site's content development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jekyll-seo-tag
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jekyll-seo-tag) = 2.8.0
Requires:      gem(bundler) >= 1.15
Requires:      gem(html-proofer) >= 3.7
Requires:      gem(rspec) >= 3.5
Requires:      gem(rubocop-jekyll) >= 0.12.0
Conflicts:     gem(html-proofer) >= 6
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop-jekyll) >= 1

%description   -n gem-jekyll-seo-tag-devel
A Jekyll plugin to add metadata tags for search engines and social networks to
better index and display your site's content development package.

%description   -n gem-jekyll-seo-tag-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета jekyll-seo-tag.
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
%doc History.markdown LICENSE.txt
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-jekyll-seo-tag-doc
%doc History.markdown LICENSE.txt
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-jekyll-seo-tag-devel
%doc History.markdown LICENSE.txt
%endif


%changelog
* Mon Jan 27 2025 Pavel Skrylev <majioa@altlinux.org> 2.8.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
