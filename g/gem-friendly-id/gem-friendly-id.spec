%define        gemname friendly_id

Name:          gem-friendly-id
Version:       5.5.0
Release:       alt1
Summary:       FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for ActiveRecord
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/norman/friendly_id
Vcs:           https://github.com/norman/friendly_id.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(railties) >= 4.0
BuildRequires: gem(minitest) >= 5.3
BuildRequires: gem(mocha) >= 1.1
BuildRequires: gem(yard) >= 0
BuildRequires: gem(i18n) >= 0
BuildRequires: gem(ffaker) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(standard) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(activerecord) >= 4.0.0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(mocha) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names friendly_id,friendly-id
Requires:      gem(activerecord) >= 4.0.0
Obsoletes:     ruby-friendly_id < %EVR
Provides:      ruby-friendly_id = %EVR
Provides:      gem(friendly_id) = 5.5.0


%description
FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for
Active Record. It lets you create pretty URLs and work with human-friendly
strings as if they were numeric ids.

With FriendlyId, it's easy to make your application use URLs like:

http://example.com/states/washington

instead of:

http://example.com/states/4323454


%package       -n gem-friendly-id-doc
Version:       5.5.0
Release:       alt1
Summary:       FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for ActiveRecord documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета friendly_id
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(friendly_id) = 5.5.0

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


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-friendly-id-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 5.5.0-alt1
- ^ 5.4.1 -> 5.5.0 (no devel)

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
