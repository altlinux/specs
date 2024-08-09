%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname amazing_print

Name:          gem-amazing-print
Version:       1.6.0
Release:       alt1
Summary:       Pretty print your Ruby objects with style
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/amazing-print/amazing_print
Vcs:           https://github.com/amazing-print/amazing_print.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bigdecimal) >= 0
BuildRequires: gem(fakefs) >= 1.2
BuildRequires: gem(nokogiri) >= 1.10
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rspec) >= 3.9
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-rspec) >= 2.4
BuildConflicts: gem(fakefs) >= 3
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-rspec) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency fakefs >= 2.5.0,fakefs < 3
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_alias_names amazing_print,amazing-print
Provides:      gem(amazing_print) = 1.6.0


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
Version:       1.6.0
Release:       alt1
Summary:       Pretty print your Ruby objects with style documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета amazing_print
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(amazing_print) = 1.6.0

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
Version:       1.6.0
Release:       alt1
Summary:       Pretty print your Ruby objects with style development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета amazing_print
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(amazing_print) = 1.6.0
Requires:      gem(bigdecimal) >= 0
Requires:      gem(fakefs) >= 1.2
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(pry) >= 0
Requires:      gem(rspec) >= 3.9
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-rspec) >= 2.4
Conflicts:     gem(fakefs) >= 3
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-rspec) >= 3

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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-amazing-print-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-amazing-print-devel
%doc README.md
%endif


%changelog
* Sat Aug 03 2024 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- ^ 1.4.0 -> 1.6.0

* Tue Oct 11 2022 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- ^ 1.3.0 -> 1.4.0

* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- ^ 1.2.2 -> 1.3.0

* Thu Dec 10 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.2-alt1
- + packaged gem with usage Ruby Policy 2.0
