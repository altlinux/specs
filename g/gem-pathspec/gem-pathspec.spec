%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname pathspec

Name:          gem-pathspec
Version:       2.1.0
Release:       alt1
Summary:       Use to match path patterns such as gitignore
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/highb/pathspec-ruby
Vcs:           https://github.com/highb/pathspec-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(benchmark-ips) >= 2.0
BuildRequires: gem(bundler) >= 2.1.4
BuildRequires: gem(fakefs) >= 2.5
BuildRequires: gem(irb) >= 1.14
BuildRequires: gem(kramdown) >= 2.3
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.10
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(simplecov) >= 0.17
BuildConflicts: gem(benchmark-ips) >= 3
BuildConflicts: gem(irb) >= 2
BuildConflicts: gem(kramdown) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4
%ruby_use_gem_dependency rubocop >= 1.15.0
%ruby_use_gem_dependency simplecov >= 0.17
%ruby_use_gem_dependency fakefs >= 2.5
Requires:      ruby >= 3.2.0
Obsoletes:     ruby-pathspec < %EVR
Provides:      ruby-pathspec = %EVR
Provides:      pathspec = %EVR
Provides:      gem(pathspec) = 2.1.0

%description
Match Path Specifications, such as .gitignore, in Ruby!


%package       -n pathspec-rb
Version:       2.1.0
Release:       alt1
Summary:       Use to match path patterns such as gitignore executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета pathspec
Group:         Other
BuildArch:     noarch

Requires:      gem(pathspec) = 2.1.0

%description   -n pathspec-rb
Use to match path patterns such as gitignore executable(s).

Match Path Specifications, such as .gitignore, in Ruby!

%description   -n pathspec-rb -l ru_RU.UTF-8
Исполнямка для самоцвета pathspec.


%if_enabled    doc
%package       -n gem-pathspec-doc
Version:       2.1.0
Release:       alt1
Summary:       Use to match path patterns such as gitignore documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pathspec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pathspec) = 2.1.0

%description   -n gem-pathspec-doc
Use to match path patterns such as gitignore documentation files.

Match Path Specifications, such as .gitignore, in Ruby!

%description   -n gem-pathspec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pathspec.
%endif


%if_enabled    devel
%package       -n gem-pathspec-devel
Version:       2.1.0
Release:       alt1
Summary:       Use to match path patterns such as gitignore development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pathspec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pathspec) = 2.1.0
Requires:      gem(benchmark-ips) >= 2.0
Requires:      gem(bundler) >= 2.1.4
Requires:      gem(fakefs) >= 2.5
Requires:      gem(irb) >= 1.14
Requires:      gem(kramdown) >= 2.3
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.10
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(simplecov) >= 0.17
Conflicts:     gem(benchmark-ips) >= 3
Conflicts:     gem(irb) >= 2
Conflicts:     gem(kramdown) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-pathspec-devel
Use to match path patterns such as gitignore development package.

Match Path Specifications, such as .gitignore, in Ruby!

%description   -n gem-pathspec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pathspec.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n pathspec-rb
%doc CHANGELOG.md LICENSE README.md
%_bindir/pathspec-rb

%if_enabled    doc
%files         -n gem-pathspec-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-pathspec-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Thu Sep 24 2026 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 1.1.3 -> 2.1.0

* Sat Aug 03 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1
- ^ 1.0.0 -> 1.1.3

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.2.2pre -> 1.0.0

* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt0.1
- ^ 0.0.2 -> 0.2.2pre
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Dec 22 2015 Andrey Cherepanov <cas@altlinux.org> 0.0.2-alt1
- Initial build for ALT Linux
