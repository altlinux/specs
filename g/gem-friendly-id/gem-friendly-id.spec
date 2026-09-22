%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname friendly_id

Name:          gem-friendly-id
Version:       5.7.0
Release:       alt1
Summary:       FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for ActiveRecord
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/norman/friendly_id
Vcs:           https://github.com/norman/friendly_id.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(activerecord) >= 4.0.0
BuildRequires: gem(babosa) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(ffaker) >= 0
BuildRequires: gem(i18n) >= 0
BuildRequires: gem(minitest) >= 5.3
BuildRequires: gem(mocha) >= 2.1
BuildRequires: gem(pry) >= 0
BuildRequires: gem(railties) >= 4.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(standard) >= 0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(mocha) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.3
%ruby_alias_names friendly_id,friendly-id
Requires:      ruby >= 2.7.0
Requires:      gem(activerecord) >= 4.0.0
Obsoletes:     ruby-friendly_id < %EVR
Provides:      ruby-friendly_id = %EVR
Provides:      gem(friendly_id) = 5.7.0

%description
FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for
Active Record. It lets you create pretty URLs and work with human-friendly
strings as if they were numeric ids.

With FriendlyId, it's easy to make your application use URLs
like:

http://example.com/states/washington

instead of:

http://example.com/states/4323454


%if_enabled    doc
%package       -n gem-friendly-id-doc
Version:       5.7.0
Release:       alt1
Summary:       FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for ActiveRecord documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета friendly_id
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(friendly_id) = 5.7.0

%description   -n gem-friendly-id-doc
FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for
ActiveRecord documentation files.

FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for
Active Record. It lets you create pretty URLs and work with human-friendly
strings as if they were numeric ids.

With FriendlyId, it's easy to make your application use URLs
like:

http://example.com/states/washington

instead of:

http://example.com/states/4323454

%description   -n gem-friendly-id-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета friendly_id.
%endif


%if_enabled    devel
%package       -n gem-friendly-id-devel
Version:       5.7.0
Release:       alt1
Summary:       FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for ActiveRecord development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета friendly_id
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(friendly_id) = 5.7.0
Requires:      gem(babosa) >= 0
Requires:      gem(ffaker) >= 0
Requires:      gem(i18n) >= 0
Requires:      gem(minitest) >= 5.3
Requires:      gem(mocha) >= 2.1
Requires:      gem(railties) >= 4.0
Requires:      gem(simplecov) >= 0
Requires:      gem(yard) >= 0
Conflicts:     gem(mocha) >= 3

%description   -n gem-friendly-id-devel
FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for
ActiveRecord development package.

FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for
Active Record. It lets you create pretty URLs and work with human-friendly
strings as if they were numeric ids.

With FriendlyId, it's easy to make your application use URLs
like:

http://example.com/states/washington

instead of:

http://example.com/states/4323454

%description   -n gem-friendly-id-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета friendly_id.
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
%doc Changelog.md MIT-LICENSE README.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-friendly-id-doc
%doc Changelog.md MIT-LICENSE README.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-friendly-id-devel
%doc Changelog.md MIT-LICENSE README.md CONTRIBUTING.md
%endif


%changelog
* Tue Sep 22 2026 Pavel Skrylev <majioa@altlinux.org> 5.7.0-alt1
- ^ 5.5.1 -> 5.7.0

* Thu Jan 23 2025 Pavel Skrylev <majioa@altlinux.org> 5.5.1-alt1
- ^ 5.4.1 -> 5.5.1

* Mon Dec 21 2020 Pavel Skrylev <majioa@altlinux.org> 5.4.1-alt1
- ^ 5.3.0 -> 5.4.1
- ! spec

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 5.3.0-alt1
- ^ 5.2.5 -> 5.3.0
- * policify name

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 5.2.5-alt1
- > Ruby Policy 2.0
- ^ 5.2.4 -> 5.2.5

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 5.2.4-alt1
- Initial gemified build for Sisyphus
