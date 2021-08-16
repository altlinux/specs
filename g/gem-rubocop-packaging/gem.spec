%define        gemname rubocop-packaging

Name:          gem-rubocop-packaging
Version:       0.5.1
Release:       alt1
Summary:       Automatic downstream compatability checking tool for Ruby code
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/utkarsh2102/rubocop-packaging
Vcs:           https://github.com/utkarsh2102/rubocop-packaging.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bump) >= 0.8 gem(bump) < 1
BuildRequires: gem(pry) >= 0.13 gem(pry) < 1
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(yard) >= 0.9 gem(yard) < 1
BuildRequires: gem(rubocop) >= 0.89 gem(rubocop) < 2.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rubocop) >= 0.89 gem(rubocop) < 2.0
Provides:      gem(rubocop-packaging) = 0.5.1


%description
A collection of RuboCop cops to check for downstream compatability issues in the
Ruby code.


%package       -n gem-rubocop-packaging-doc
Version:       0.5.1
Release:       alt1
Summary:       Automatic downstream compatability checking tool for Ruby code documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-packaging
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-packaging) = 0.5.1

%description   -n gem-rubocop-packaging-doc
Automatic downstream compatability checking tool for Ruby code documentation
files.

A collection of RuboCop cops to check for downstream compatability issues in the
Ruby code.

%description   -n gem-rubocop-packaging-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-packaging.


%package       -n gem-rubocop-packaging-devel
Version:       0.5.1
Release:       alt1
Summary:       Automatic downstream compatability checking tool for Ruby code development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-packaging
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-packaging) = 0.5.1
Requires:      gem(bump) >= 0.8 gem(bump) < 1
Requires:      gem(pry) >= 0.13 gem(pry) < 1
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(yard) >= 0.9 gem(yard) < 1

%description   -n gem-rubocop-packaging-devel
Automatic downstream compatability checking tool for Ruby code development
package.

A collection of RuboCop cops to check for downstream compatability issues in the
Ruby code.

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
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.1-alt1
- + packaged gem with Ruby Policy 2.0
