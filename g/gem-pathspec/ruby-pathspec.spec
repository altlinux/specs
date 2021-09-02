%define        gemname pathspec

Name:          gem-pathspec
Version:       1.0.0
Release:       alt1
Summary:       Use to match path patterns such as gitignore
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/highb/pathspec-ruby
Vcs:           https://github.com/highb/pathspec-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 2.1.4 gem(bundler) < 3
BuildRequires: gem(fakefs) >= 1.3 gem(fakefs) < 2
BuildRequires: gem(kramdown) >= 2.3 gem(kramdown) < 3
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.10.0 gem(rspec) < 4
BuildRequires: gem(rubocop) >= 1.7 gem(rubocop) < 2
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names pathspec-rb,pathspec
Obsoletes:     ruby-pathspec < %EVR
Provides:      ruby-pathspec = %EVR
Provides:      gem(pathspec) = 1.0.0


%description
Match Path Specifications, such as .gitignore, in Ruby!


%package       -n pathspec-rb
Version:       1.0.0
Release:       alt1
Summary:       Use to match path patterns such as gitignore executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета pathspec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pathspec) = 1.0.0

%description   -n pathspec-rb
Use to match path patterns such as gitignore executable(s).

Match Path Specifications, such as .gitignore, in Ruby!

%description   -n pathspec-rb -l ru_RU.UTF-8
Исполнямка для самоцвета pathspec.


%package       -n gem-pathspec-doc
Version:       1.0.0
Release:       alt1
Summary:       Use to match path patterns such as gitignore documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pathspec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pathspec) = 1.0.0

%description   -n gem-pathspec-doc
Use to match path patterns such as gitignore documentation files.

Match Path Specifications, such as .gitignore, in Ruby!

%description   -n gem-pathspec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pathspec.


%package       -n gem-pathspec-devel
Version:       1.0.0
Release:       alt1
Summary:       Use to match path patterns such as gitignore development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pathspec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pathspec) = 1.0.0
Requires:      gem(bundler) >= 2.1.4 gem(bundler) < 3
Requires:      gem(fakefs) >= 1.3 gem(fakefs) < 2
Requires:      gem(kramdown) >= 2.3 gem(kramdown) < 3
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.10.0 gem(rspec) < 4
Requires:      gem(rubocop) >= 1.7 gem(rubocop) < 2
Requires:      gem(simplecov) >= 0.17 gem(simplecov) < 1

%description   -n gem-pathspec-devel
Use to match path patterns such as gitignore development package.

Match Path Specifications, such as .gitignore, in Ruby!

%description   -n gem-pathspec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pathspec.


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

%files         -n pathspec-rb
%doc README.md
%_bindir/pathspec-rb

%files         -n gem-pathspec-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-pathspec-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.2.2pre -> 1.0.0

* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt0.1
- ^ 0.0.2 -> 0.2.2pre
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Dec 22 2015 Andrey Cherepanov <cas@altlinux.org> 0.0.2-alt1
- Initial build for ALT Linux
