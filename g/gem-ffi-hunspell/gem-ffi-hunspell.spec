%define        _unpackaged_files_terminate_build 1
%define        gemname ffi-hunspell

Name:          gem-ffi-hunspell
Version:       0.6.1
Release:       alt1
Summary:       FFI bindings for Hunspell
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/postmodern/ffi-hunspell#readme
Vcs:           https://github.com/postmodern/ffi-hunspell.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubygems-tasks) >= 0.1
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(ffi) >= 1.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rubygems-tasks) >= 1
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(ffi) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ffi) >= 1.0
Conflicts:     gem(ffi) >= 2
Provides:      gem(ffi-hunspell) = 0.6.1


%description
Ruby FFI bindings for the Hunspell spell checker.


%package       -n gem-ffi-hunspell-doc
Version:       0.6.1
Release:       alt1
Summary:       FFI bindings for Hunspell documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ffi-hunspell
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ffi-hunspell) = 0.6.1

%description   -n gem-ffi-hunspell-doc
FFI bindings for Hunspell documentation files.

Ruby FFI bindings for the Hunspell spell checker.

%description   -n gem-ffi-hunspell-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ffi-hunspell.


%package       -n gem-ffi-hunspell-devel
Version:       0.6.1
Release:       alt1
Summary:       FFI bindings for Hunspell development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ffi-hunspell
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ffi-hunspell) = 0.6.1
Requires:      gem(bundler) >= 2.0
Requires:      gem(rake) >= 0
Requires:      gem(rubygems-tasks) >= 0.1
Requires:      gem(rspec) >= 3.0
Requires:      gem(yard) >= 0.9
Requires:      gem(kramdown) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rubygems-tasks) >= 1
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(yard) >= 1

%description   -n gem-ffi-hunspell-devel
FFI bindings for Hunspell development package.

Ruby FFI bindings for the Hunspell spell checker.

%description   -n gem-ffi-hunspell-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ffi-hunspell.


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

%files         -n gem-ffi-hunspell-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ffi-hunspell-devel
%doc README.md


%changelog
* Wed Jun 21 2023 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- + packaged gem with Ruby Policy 2.0
