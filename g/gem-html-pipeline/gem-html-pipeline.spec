%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname html-pipeline

Name:          gem-html-pipeline
Version:       3.2.4
Release:       alt1
Summary:       HTML processing filters and utilities
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jch/html-pipeline
Vcs:           https://github.com/jch/html-pipeline.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(amazing_print) >= 0
BuildRequires: gem(awesome_print) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(commonmarker) >= 2.6
BuildRequires: gem(debug) >= 0
BuildRequires: gem(gemoji) >= 4.1
BuildRequires: gem(gemojione) >= 4.3
BuildRequires: gem(minitest) >= 6.0
BuildRequires: gem(minitest-bisect) >= 1.6
BuildRequires: gem(minitest-focus) >= 1.1
BuildRequires: gem(minitest-mock) >= 5.27
BuildRequires: gem(nokogiri) >= 1.13
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rouge) >= 4.1
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-standard) >= 0
BuildRequires: gem(selma) >= 0.4
BuildRequires: gem(sorbet) >= 0
BuildRequires: gem(sorbet-runtime) >= 0
BuildRequires: gem(tapioca) >= 0
BuildRequires: gem(zeitwerk) >= 2.5
BuildConflicts: gem(commonmarker) >= 3
BuildConflicts: gem(gemoji) >= 5
BuildConflicts: gem(gemojione) >= 5
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(minitest-bisect) >= 2
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(minitest-mock) >= 6
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rouge) >= 5
BuildConflicts: gem(selma) >= 1
BuildConflicts: gem(zeitwerk) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.2
Requires:      rubygems >= 3.3.22
Requires:      gem(awesome_print) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-standard) >= 0
Requires:      gem(selma) >= 0.4
Requires:      gem(zeitwerk) >= 2.5
Conflicts:     gem(selma) >= 1
Conflicts:     gem(zeitwerk) >= 3
Provides:      gem(html-pipeline) = 3.2.4

%description
HTML processing filters and utilities. This module is a small framework for
defining CSS-based content filters and applying them to user provided content.


%if_enabled    doc
%package       -n gem-html-pipeline-doc
Version:       3.2.4
Release:       alt1
Summary:       HTML processing filters and utilities documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета html-pipeline
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(html-pipeline) = 3.2.4

%description   -n gem-html-pipeline-doc
HTML processing filters and utilities documentation files.

HTML processing filters and utilities. This module is a small framework for
defining CSS-based content filters and applying them to user provided content.

%description   -n gem-html-pipeline-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета html-pipeline.
%endif


%if_enabled    devel
%package       -n gem-html-pipeline-devel
Version:       3.2.4
Release:       alt1
Summary:       HTML processing filters and utilities development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета html-pipeline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(html-pipeline) = 3.2.4
Requires:      gem(amazing_print) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(commonmarker) >= 2.6
Requires:      gem(debug) >= 0
Requires:      gem(gemoji) >= 4.1
Requires:      gem(gemojione) >= 4.3
Requires:      gem(minitest) >= 6.0
Requires:      gem(minitest-bisect) >= 1.6
Requires:      gem(minitest-focus) >= 1.1
Requires:      gem(minitest-mock) >= 5.27
Requires:      gem(nokogiri) >= 1.13
Requires:      gem(rake) >= 0
Requires:      gem(rouge) >= 4.1
Requires:      gem(sorbet) >= 0
Requires:      gem(tapioca) >= 0
Conflicts:     gem(commonmarker) >= 3
Conflicts:     gem(gemoji) >= 5
Conflicts:     gem(gemojione) >= 5
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(minitest-bisect) >= 2
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(minitest-mock) >= 6
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(rouge) >= 5

%description   -n gem-html-pipeline-devel
HTML processing filters and utilities development package.

HTML processing filters and utilities. This module is a small framework for
defining CSS-based content filters and applying them to user provided content.

%description   -n gem-html-pipeline-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета html-pipeline.
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
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-html-pipeline-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-html-pipeline-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Tue Sep 22 2026 Pavel Skrylev <majioa@altlinux.org> 3.2.4-alt1
- ^ 2.14.3 -> 3.2.4
- * define explicit dependencies

* Tue Apr 28 2026 Artem Semenov <savoptik@altlinux.org> 2.14.3-alt1
- Initial build for Sisyphus
