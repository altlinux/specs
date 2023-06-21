%define        _unpackaged_files_terminate_build 1
%define        gemname yard-spellcheck

Name:          gem-yard-spellcheck
Version:       0.1.5
Release:       alt1
Summary:       Spellcheck your YARD documentat
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/postmodern/yard-spellcheck#readme
Vcs:           https://github.com/postmodern/yard-spellcheck#readme.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(yard) >= 0.6
BuildRequires: gem(ffi-hunspell) >= 0.2
BuildRequires: gem(rubygems-tasks) >= 0.1
BuildRequires: gem(rspec) >= 2.4
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(ffi-hunspell) >= 1
BuildConflicts: gem(rubygems-tasks) >= 1
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      gem(yard) >= 0.6
Requires:      gem(ffi-hunspell) >= 0.2
Conflicts:     gem(yard) >= 1
Conflicts:     gem(ffi-hunspell) >= 1
Provides:      gem(yard-spellcheck) = 0.1.5


%description
Adds the 'spellcheck' command to YARD, which will spellcheck every docstring
within your documentation.


%package       -n yard-spellcheck
Version:       0.1.5
Release:       alt1
Summary:       Spellcheck your YARD documentat executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета yard-spellcheck
Group:         Other
BuildArch:     noarch

Requires:      gem(yard-spellcheck) = 0.1.5

%description   -n yard-spellcheck
Spellcheck your YARD documentat executable(s).

Adds the 'spellcheck' command to YARD, which will spellcheck every docstring
within your documentation.

%description   -n yard-spellcheck -l ru_RU.UTF-8
Исполнямка для самоцвета yard-spellcheck.


%package       -n gem-yard-spellcheck-doc
Version:       0.1.5
Release:       alt1
Summary:       Spellcheck your YARD documentat documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета yard-spellcheck
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(yard-spellcheck) = 0.1.5

%description   -n gem-yard-spellcheck-doc
Spellcheck your YARD documentat documentation files.

Adds the 'spellcheck' command to YARD, which will spellcheck every docstring
within your documentation.

%description   -n gem-yard-spellcheck-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета yard-spellcheck.


%package       -n gem-yard-spellcheck-devel
Version:       0.1.5
Release:       alt1
Summary:       Spellcheck your YARD documentat development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета yard-spellcheck
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(yard-spellcheck) = 0.1.5
Requires:      gem(rubygems-tasks) >= 0.1
Requires:      gem(rspec) >= 2.4
Conflicts:     gem(rubygems-tasks) >= 1
Conflicts:     gem(rspec) >= 4

%description   -n gem-yard-spellcheck-devel
Spellcheck your YARD documentat development package.

Adds the 'spellcheck' command to YARD, which will spellcheck every docstring
within your documentation.

%description   -n gem-yard-spellcheck-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета yard-spellcheck.


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

%files         -n yard-spellcheck
%doc README.md
%_bindir/yard-spellcheck

%files         -n gem-yard-spellcheck-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-yard-spellcheck-devel
%doc README.md


%changelog
* Wed Jun 21 2023 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1
- + packaged gem with Ruby Policy 2.0
