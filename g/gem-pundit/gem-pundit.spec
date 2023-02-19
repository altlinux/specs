%define        gemname pundit

Name:          gem-pundit
Version:       2.3.0
Release:       alt1
Summary:       Minimal authorization through OO design and pure Ruby classes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/varvet/pundit
Vcs:           https://github.com/varvet/pundit.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(actionpack) >= 3.0.0
BuildRequires: gem(activemodel) >= 3.0.0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(railties) >= 3.0.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(yard) >= 0
BuildRequires: gem(activesupport) >= 3.0.0
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(activesupport) >= 3.0.0
Obsoletes:     ruby-pundit < %EVR
Provides:      ruby-pundit = %EVR
Provides:      gem(pundit) = 2.3.0


%description
Pundit provides a set of helpers which guide you in leveraging regular Ruby
classes and object oriented design patterns to build a simple, robust and
scaleable authorization system.


%package       -n gem-pundit-doc
Version:       2.3.0
Release:       alt1
Summary:       Minimal authorization through OO design and pure Ruby classes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pundit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pundit) = 2.3.0

%description   -n gem-pundit-doc
Minimal authorization through OO design and pure Ruby classes documentation
files.

Pundit provides a set of helpers which guide you in leveraging regular Ruby
classes and object oriented design patterns to build a simple, robust and
scaleable authorization system.

%description   -n gem-pundit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pundit.


%package       -n gem-pundit-devel
Version:       2.3.0
Release:       alt1
Summary:       Minimal authorization through OO design and pure Ruby classes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pundit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pundit) = 2.3.0
Requires:      gem(actionpack) >= 3.0.0
Requires:      gem(activemodel) >= 3.0.0
Requires:      gem(bundler) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(railties) >= 3.0.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(yard) >= 0
Conflicts:     gem(rubocop) >= 2

%description   -n gem-pundit-devel
Minimal authorization through OO design and pure Ruby classes development
package.

Pundit provides a set of helpers which guide you in leveraging regular Ruby
classes and object oriented design patterns to build a simple, robust and
scaleable authorization system.

%description   -n gem-pundit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pundit.


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

%files         -n gem-pundit-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-pundit-devel
%doc README.md


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- ^ 2.1.1 -> 2.3.0

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- ^ 2.0.1 -> 2.1.1

* Sun Feb 03 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus
