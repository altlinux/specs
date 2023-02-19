# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname deface

Name:          gem-deface
Version:       1.9.0
Release:       alt1.1
Summary:       Rails plugin that allows you to customize ERB views
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/spree/deface
Vcs:           https://github.com/spree/deface.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(erubis) >= 0
BuildRequires: gem(gem-release) >= 0
BuildRequires: gem(rspec) >= 3.1.0
BuildRequires: gem(haml) >= 4.0
BuildRequires: gem(slim) >= 4.1
BuildRequires: gem(simplecov) >= 0.6.4
BuildRequires: gem(generator_spec) >= 0.8
BuildRequires: gem(nokogiri) >= 1.6
BuildRequires: gem(actionview) >= 5.2
BuildRequires: gem(railties) >= 5.2
BuildRequires: gem(rainbow) >= 2.1.0
BuildRequires: gem(polyglot) >= 0
BuildConflicts: gem(haml) >= 7
BuildConflicts: gem(slim) >= 5
BuildConflicts: gem(generator_spec) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency haml >= 6.1.1,haml < 7
Requires:      gem(nokogiri) >= 1.6
Requires:      gem(actionview) >= 5.2
Requires:      gem(railties) >= 5.2
Requires:      gem(rainbow) >= 2.1.0
Requires:      gem(polyglot) >= 0
Provides:      gem(deface) = 1.9.0


%description
Rails plugin that allows you to customize ERB views in a Rails application
without editing the underlying view.

It allows you to easily target html & erb elements as the hooks for
customization using CSS selectors as supported by Nokogiri.


%package       -n gem-deface-doc
Version:       1.9.0
Release:       alt1.1
Summary:       Rails plugin that allows you to customize ERB views documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета deface
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(deface) = 1.9.0

%description   -n gem-deface-doc
Rails plugin that allows you to customize ERB views documentation files.

Rails plugin that allows you to customize ERB views in a Rails application
without editing the underlying view.

It allows you to easily target html & erb elements as the hooks for
customization using CSS selectors as supported by Nokogiri.

%description   -n gem-deface-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета deface.


%package       -n gem-deface-devel
Version:       1.9.0
Release:       alt1.1
Summary:       Rails plugin that allows you to customize ERB views development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета deface
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(deface) = 1.9.0
Requires:      gem(test-unit) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(appraisal) >= 0
Requires:      gem(erubis) >= 0
Requires:      gem(gem-release) >= 0
Requires:      gem(rspec) >= 3.1.0
Requires:      gem(haml) >= 4.0
Requires:      gem(slim) >= 4.1
Requires:      gem(simplecov) >= 0.6.4
Requires:      gem(generator_spec) >= 0.8
Conflicts:     gem(haml) >= 7
Conflicts:     gem(slim) >= 5
Conflicts:     gem(generator_spec) >= 1

%description   -n gem-deface-devel
Rails plugin that allows you to customize ERB views development package.

Rails plugin that allows you to customize ERB views in a Rails application
without editing the underlying view.

It allows you to easily target html & erb elements as the hooks for
customization using CSS selectors as supported by Nokogiri.

%description   -n gem-deface-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета deface.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-deface-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-deface-devel
%doc README.markdown


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 1.9.0-alt1.1
- ! fixed dep to haml

* Mon Oct 03 2022 Pavel Skrylev <majioa@altlinux.org> 1.9.0-alt1
- ^ 1.5.3 -> 1.9.0

* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 1.5.3-alt1
- + packaged gem with usage Ruby Policy 2.0
