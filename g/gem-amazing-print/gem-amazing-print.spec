%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname amazing_print

Name:          gem-amazing-print
Version:       3.0.0
Release:       alt1.1
Summary:       Pretty print your Ruby objects with style
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/amazing-print/amazing_print
Vcs:           https://github.com/amazing-print/amazing_print.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(appraisal) >= 2.4.0
BuildRequires: gem(bigdecimal) >= 0
BuildRequires: gem(fakefs) >= 1.2
BuildRequires: gem(logger) >= 1.7
BuildRequires: gem(nokogiri) >= 1.18.9
BuildRequires: gem(ostruct) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rspec) >= 3.9
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-rspec) >= 3.6
BuildConflicts: gem(logger) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop-rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency nokogiri >= 1.18.9
%ruby_use_gem_dependency fakefs >= 1.2
%ruby_use_gem_dependency appraisal >= 2.4.0
%ruby_use_gem_dependency rubocop >= 1.15.0
%ruby_alias_names amazing_print,amazing-print
Requires:      ruby >= 3.1.0
Requires:      ruby >= 3.2.0
Provides:      amazing_print = %EVR
Provides:      gem(amazing_print) = 3.0.0

%description
Pretty print your Ruby objects with style -- in full color and with proper
indentation.

AmazingPrint is a fork of AwesomePrint which became stale and should be used in
its place to avoid conflicts. It is a Ruby library that pretty prints Ruby
objects in full color exposing their internal structure with proper indentation.
Rails ActiveRecord objects and usage within Rails templates are supported via
included mixins.


%if_enabled    doc
%package       -n gem-amazing-print-doc
Version:       3.0.0
Release:       alt1.1
Summary:       Pretty print your Ruby objects with style documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета amazing_print
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(amazing_print) = 3.0.0

%description   -n gem-amazing-print-doc
Pretty print your Ruby objects with style documentation files.

Pretty print your Ruby objects with style -- in full color and with proper
indentation.

AmazingPrint is a fork of AwesomePrint which became stale and should be used in
its place to avoid conflicts. It is a Ruby library that pretty prints Ruby
objects in full color exposing their internal structure with proper indentation.
Rails ActiveRecord objects and usage within Rails templates are supported via
included mixins.

%description   -n gem-amazing-print-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета amazing_print.
%endif


%if_enabled    devel
%package       -n gem-amazing-print-devel
Version:       3.0.0
Release:       alt1.1
Summary:       Pretty print your Ruby objects with style development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета amazing_print
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(amazing_print) = 3.0.0
Requires:      gem(appraisal) >= 2.4.0
Requires:      gem(bigdecimal) >= 0
Requires:      gem(fakefs) >= 1.2
Requires:      gem(logger) >= 1.7
Requires:      gem(nokogiri) >= 1.18.9
Requires:      gem(ostruct) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rspec) >= 3.9
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-rspec) >= 3.6
Conflicts:     gem(logger) >= 2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop-rspec) >= 4

%description   -n gem-amazing-print-devel
Pretty print your Ruby objects with style development package.

Pretty print your Ruby objects with style -- in full color and with proper
indentation.

AmazingPrint is a fork of AwesomePrint which became stale and should be used in
its place to avoid conflicts. It is a Ruby library that pretty prints Ruby
objects in full color exposing their internal structure with proper indentation.
Rails ActiveRecord objects and usage within Rails templates are supported via
included mixins.

%description   -n gem-amazing-print-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета amazing_print.
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
%doc CHANGELOG.md CONTRIBUTING.md README.md LICENSE
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-amazing-print-doc
%doc CHANGELOG.md CONTRIBUTING.md README.md LICENSE
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-amazing-print-devel
%doc CHANGELOG.md CONTRIBUTING.md README.md LICENSE
%endif


%changelog
* Tue Sep 22 2026 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1.1
- ! relaxed deps to some gems

* Tue Sep 22 2026 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ 2.0.0 -> 3.0.0

* Tue Oct 21 2025 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- ^ 1.6.0 -> 2.0.0

* Sat Aug 03 2024 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- ^ 1.4.0 -> 1.6.0

* Tue Oct 11 2022 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- ^ 1.3.0 -> 1.4.0

* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- ^ 1.2.2 -> 1.3.0

* Thu Dec 10 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.2-alt1
- + packaged gem with usage Ruby Policy 2.0
