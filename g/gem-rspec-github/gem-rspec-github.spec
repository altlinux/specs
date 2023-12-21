%define        _unpackaged_files_terminate_build 1
%define        gemname rspec-github

Name:          gem-rspec-github
Version:       2.4.0
Release:       alt1
Summary:       Formatter for RSpec to show errors in GitHub action annotations
License:       MIT
Group:         Development/Ruby
Url:           https://drieam.github.io/rspec-github
Vcs:           https://github.com/drieam/rspec-github.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.12.0
BuildRequires: gem(rubocop-ast) >= 1.4.0
BuildRequires: gem(rspec-core) >= 3.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-ast) >= 2
BuildConflicts: gem(rspec-core) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-ast >= 1.7.0,rubocop-ast < 2
Requires:      gem(rspec-core) >= 3.0
Conflicts:     gem(rspec-core) >= 4
Provides:      gem(rspec-github) = 2.4.0

%ruby_use_gem_version rspec-github:2.4.0

%description
Formatter for RSpec to show errors in GitHub action annotations


%package       -n gem-rspec-github-doc
Version:       2.4.0
Release:       alt1
Summary:       Formatter for RSpec to show errors in GitHub action annotations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-github
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-github) = 2.4.0

%description   -n gem-rspec-github-doc
Formatter for RSpec to show errors in GitHub action annotations documentation
files.

%description   -n gem-rspec-github-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-github.


%package       -n gem-rspec-github-devel
Version:       2.4.0
Release:       alt1
Summary:       Formatter for RSpec to show errors in GitHub action annotations development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-github
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-github) = 2.4.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.12.0
Requires:      gem(rubocop-ast) >= 1.4.0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-ast) >= 2

%description   -n gem-rspec-github-devel
Formatter for RSpec to show errors in GitHub action annotations development
package.

%description   -n gem-rspec-github-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-github.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-rspec-github-doc
%ruby_gemdocdir

%files         -n gem-rspec-github-devel


%changelog
* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- + packaged gem with Ruby Policy 2.0
