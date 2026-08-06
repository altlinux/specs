%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname multi_json

Name:          gem-multi-json
Version:       1.21.1
Release:       alt1
Summary:       A common interface to multiple JSON libraries
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/intridea/multi_json
Vcs:           https://github.com/intridea/multi_json.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(activesupport) >= 7.1
BuildRequires: gem(fast_jsonparser) >= 0.6
BuildRequires: gem(json) >= 2.0
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(mutant-minitest) >= 0.12
BuildRequires: gem(oj) >= 3.0
BuildRequires: gem(rake) >= 13.1.0
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-minitest) >= 0.13.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(standard) >= 1.35.1
BuildRequires: gem(steep) >= 1.10
BuildRequires: gem(yajl-ruby) >= 1.3
BuildRequires: gem(yard) >= 0.9.34
BuildRequires: gem(yardstick) >= 0.9.9
BuildConflicts: gem(activesupport) >= 9
BuildConflicts: gem(fast_jsonparser) >= 1
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(oj) >= 4
BuildConflicts: gem(yajl-ruby) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rubocop-minitest >= 0.13.0,rubocop-minitest < 1
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency activesupport >= 7.1,activesupport < 8
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_alias_names multi_json,multi-json
Requires:      ruby >= 3.2
BuildRequires: gem(concurrent-ruby) >= 1.2
BuildConflicts: gem(concurrent-ruby) >= 2
Obsoletes:     ruby-multi_json < %EVR
Provides:      ruby-multi_json = %EVR
Provides:      gem(multi_json) = 1.21.1

%description
A common interface to multiple JSON libraries, including Oj, Yajl, the JSON gem
(with C-extensions), the pure-Ruby JSON gem, NSJSONSerialization, gson.rb,
JrJackson, and OkJson.


%if_enabled    doc
%package       -n gem-multi-json-doc
Version:       1.21.1
Release:       alt1
Summary:       A common interface to multiple JSON libraries documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета multi_json
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(multi_json) = 1.21.1

%description   -n gem-multi-json-doc
A common interface to multiple JSON libraries documentation files.

A common interface to multiple JSON libraries, including Oj, Yajl, the JSON gem
(with C-extensions), the pure-Ruby JSON gem, NSJSONSerialization, gson.rb,
JrJackson, and OkJson.

%description   -n gem-multi-json-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета multi_json.
%endif


%if_enabled    devel
%package       -n gem-multi-json-devel
Version:       1.21.1
Release:       alt1
Summary:       A common interface to multiple JSON libraries development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета multi_json
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(multi_json) = 1.21.1
Requires:      gem(activesupport) >= 7.1
Requires:      gem(concurrent-ruby) >= 1.2
Requires:      gem(fast_jsonparser) >= 0.6
Requires:      gem(json) >= 2.0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(mutant-minitest) >= 0.12
Requires:      gem(oj) >= 3.0
Requires:      gem(rake) >= 13.1.0
Requires:      gem(rdoc) >= 6.1.1
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-minitest) >= 0.13.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(standard) >= 1.35.1
Requires:      gem(steep) >= 1.10
Requires:      gem(yajl-ruby) >= 1.3
Requires:      gem(yard) >= 0.9.34
Requires:      gem(yardstick) >= 0.9.9
Conflicts:     gem(activesupport) >= 9
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(fast_jsonparser) >= 1
Conflicts:     gem(json) >= 3
Conflicts:     gem(oj) >= 4
Conflicts:     gem(yajl-ruby) >= 2

%description   -n gem-multi-json-devel
A common interface to multiple JSON libraries development package.

A common interface to multiple JSON libraries, including Oj, Yajl, the JSON gem
(with C-extensions), the pure-Ruby JSON gem, NSJSONSerialization, gson.rb,
JrJackson, and OkJson.

%description   -n gem-multi-json-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета multi_json.
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
%doc LICENSE.md README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-multi-json-doc
%doc LICENSE.md README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-multi-json-devel
%doc LICENSE.md README.md CHANGELOG.md CONTRIBUTING.md
%endif


%changelog
* Thu Aug 06 2026 Pavel Skrylev <majioa@altlinux.org> 1.21.1-alt1
- ^ 1.15.0 -> 1.21.1

* Wed Sep 16 2020 Pavel Skrylev <majioa@altlinux.org> 1.15.0-alt1
- ^ 1.14.1 -> 1.15.0

* Mon Apr 13 2020 Pavel Skrylev <majioa@altlinux.org> 1.14.1-alt1
- > Ruby Policy 2.0
- ^ 1.13.1 -> 1.14.1
- ! spec tags and syntax

* Wed Aug 29 2018 Andrey Cherepanov <cas@altlinux.org> 1.13.1-alt2.1
- Rebuild for new Ruby autorequirements.

* Sun Jul 08 2018 Andrey Cherepanov <cas@altlinux.org> 1.13.1-alt2
- Package as gem.

* Thu Jan 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.13.1-alt1
- New version.

* Tue Jan 09 2018 Andrey Cherepanov <cas@altlinux.org> 1.13.0-alt1
- New version.

* Sat Sep 09 2017 Andrey Cherepanov <cas@altlinux.org> 1.12.2-alt1.1
- Rebuild with Ruby 2.4.1

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.12.2-alt1
- New version

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.12.1-alt1
- New version

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 1.9.2-alt1
- Initial build for ALT Linux
