%define        gemname rubocop

Name:          gem-rubocop
Version:       1.36.0
Release:       alt1
Summary:       A Ruby static code analyzer and formatter
License:       MIT
Group:         Development/Ruby
Url:           https://www.rubocop.org/
Vcs:           https://github.com/rubocop-hq/rubocop.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(json) >= 2.3 gem(json) < 3
BuildRequires: gem(parallel) >= 1.10 gem(parallel) < 2
BuildRequires: gem(parser) >= 3.1.2.1
BuildRequires: gem(rainbow) >= 2.2.2 gem(rainbow) < 4.0
BuildRequires: gem(regexp_parser) >= 1.8 gem(regexp_parser) < 3.0
BuildRequires: gem(rexml) >= 3.2.5 gem(rexml) < 4.0
BuildRequires: gem(rubocop-ast) >= 1.7.0 gem(rubocop-ast) < 2
BuildRequires: gem(ruby-progressbar) >= 1.7 gem(ruby-progressbar) < 2
BuildRequires: gem(unicode-display_width) >= 1.4.0 gem(unicode-display_width) < 3.0
BuildRequires: gem(bundler) >= 1.15.0 gem(bundler) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop-ast >= 1.7.0,rubocop-ast < 2
Requires:      gem(json) >= 2.3 gem(json) < 3
Requires:      gem(parallel) >= 1.10 gem(parallel) < 2
Requires:      gem(parser) >= 3.1.2.1
Requires:      gem(rainbow) >= 2.2.2 gem(rainbow) < 4.0
Requires:      gem(regexp_parser) >= 1.8 gem(regexp_parser) < 3.0
Requires:      gem(rexml) >= 3.2.5 gem(rexml) < 4.0
Requires:      gem(rubocop-ast) >= 1.7.0 gem(rubocop-ast) < 2
Requires:      gem(ruby-progressbar) >= 1.7 gem(ruby-progressbar) < 2
Requires:      gem(unicode-display_width) >= 1.4.0 gem(unicode-display_width) < 3.0
Requires:      gem-regexp-parser >= 1.7.1-alt1.1
Requires:      gem-parser >= 2.7.1.4-alt1.1
Provides:      gem(rubocop) = 1.36.0


%description
A Ruby static code analyzer and formatter, based on the community Ruby style
guide.


%package       -n rubocop
Version:       1.36.0
Release:       alt1
Summary:       A Ruby static code analyzer and formatter executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rubocop
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop) = 1.36.0

%description   -n rubocop
A Ruby static code analyzer and formatter executable(s).

A Ruby static code analyzer and formatter, based on the community Ruby style
guide.

%description   -n rubocop -l ru_RU.UTF-8
Исполнямка для самоцвета rubocop.


%package       -n gem-rubocop-doc
Version:       1.36.0
Release:       alt1
Summary:       A Ruby static code analyzer and formatter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop) = 1.36.0

%description   -n gem-rubocop-doc
A Ruby static code analyzer and formatter documentation files.

A Ruby static code analyzer and formatter, based on the community Ruby style
guide.

%description   -n gem-rubocop-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop.


%package       -n gem-rubocop-devel
Version:       1.36.0
Release:       alt1
Summary:       A Ruby static code analyzer and formatter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop) = 1.36.0
Requires:      gem(bundler) >= 1.15.0 gem(bundler) < 3

%description   -n gem-rubocop-devel
A Ruby static code analyzer and formatter development package.

A Ruby static code analyzer and formatter, based on the community Ruby style
guide.

%description   -n gem-rubocop-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop.


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

%files         -n rubocop
%doc README.md
%_bindir/rubocop

%files         -n gem-rubocop-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-devel
%doc README.md


%changelog
* Wed Sep 21 2022 Pavel Skrylev <majioa@altlinux.org> 1.36.0-alt1
- ^ 1.27.0 -> 1.36.0

* Sat Apr 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.27.0-alt1
- ^ 1.15.0 -> 1.27.0

* Sun May 30 2021 Pavel Skrylev <majioa@altlinux.org> 1.15.0-alt1
- ^ 1.13.0 -> 1.15.0

* Fri Apr 23 2021 Pavel Skrylev <majioa@altlinux.org> 1.13.0-alt1
- ^ 0.88.0 -> 1.13.0

* Fri Jul 17 2020 Pavel Skrylev <majioa@altlinux.org> 0.88.0-alt1.1
- ! dep to gem-regexp-parser, and gem-parser (closes #38650)
- ! spec syntax

* Tue Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 0.88.0-alt1
- ^ 0.74.0 -> 0.88.0
- ! executable runnning (closes #38650)

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.74.0-alt1.1
- ! spec according to changelog rules

* Sat Aug 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.74.0-alt1
- ^ v0.74.0
- ! spec

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 0.66.0-alt1
- Bump to 0.66.0

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 0.65.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
