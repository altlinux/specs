%define        _unpackaged_files_terminate_build 1
%define        gemname rubocop-packaging

Name:          gem-rubocop-packaging
Version:       0.5.2
Release:       alt1
Summary:       Automatic downstream compatability checking tool for Ruby code
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/utkarsh2102/rubocop-packaging
Vcs:           https://github.com/utkarsh2102/rubocop-packaging.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bump) >= 0.8
BuildRequires: gem(pry) >= 0.13
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(rubocop) >= 1.15.0
BuildConflicts: gem(bump) >= 1
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(rubocop) >= 2
Provides:      gem(rubocop-packaging) = 0.5.2


%description
A collection of RuboCop cops to check for downstream compatability issues in the
Ruby code.


%package       -n gem-rubocop-packaging-doc
Version:       0.5.2
Release:       alt1
Summary:       Automatic downstream compatability checking tool for Ruby code documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-packaging
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-packaging) = 0.5.2

%description   -n gem-rubocop-packaging-doc
Automatic downstream compatability checking tool for Ruby code documentation
files.

%description   -n gem-rubocop-packaging-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-packaging.


%package       -n gem-rubocop-packaging-devel
Version:       0.5.2
Release:       alt1
Summary:       Automatic downstream compatability checking tool for Ruby code development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-packaging
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-packaging) = 0.5.2
Requires:      gem(bump) >= 0.8
Requires:      gem(pry) >= 0.13
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(yard) >= 0.9
Conflicts:     gem(bump) >= 1
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(yard) >= 1

%description   -n gem-rubocop-packaging-devel
Automatic downstream compatability checking tool for Ruby code development
package.

%description   -n gem-rubocop-packaging-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-packaging.


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

%files         -n gem-rubocop-packaging-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-packaging-devel
%doc README.md


%changelog
* Fri Dec 01 2023 Pavel Skrylev <majioa@altlinux.org> 0.5.2-alt1
- ^ 0.5.1 -> 0.5.2

* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.1-alt1
- + packaged gem with Ruby Policy 2.0
