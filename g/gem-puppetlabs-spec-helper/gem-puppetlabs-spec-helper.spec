%define        _unpackaged_files_terminate_build 1
%define        gemname puppetlabs_spec_helper

Name:          gem-puppetlabs-spec-helper
Version:       7.0.2
Release:       alt1
Summary:       Standard tasks and configuration for module spec tests
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://github.com/puppetlabs/puppetlabs_spec_helper
Vcs:           https://github.com/puppetlabs/puppetlabs_spec_helper.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(puppet) >= 0
BuildRequires: gem(codecov) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-console) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.1
BuildRequires: gem(rspec-its) >= 1.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(fakefs) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(mocha) >= 1.0
BuildRequires: gem(pathspec) >= 0.2
BuildRequires: gem(puppet-lint) >= 4.0
BuildRequires: gem(puppet-syntax) >= 3.0
BuildRequires: gem(rspec-github) >= 2.0
BuildRequires: gem(rspec-puppet) >= 4.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-its) >= 2
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(mocha) >= 2
BuildConflicts: gem(pathspec) >= 2.0.0
BuildConflicts: gem(puppet-lint) >= 5
BuildConflicts: gem(puppet-syntax) >= 4
BuildConflicts: gem(rspec-github) >= 3
BuildConflicts: gem(rspec-puppet) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
Requires:      gem(mocha) >= 1.0
Requires:      gem(pathspec) >= 0.2
Requires:      gem(puppet-lint) >= 4.0
Requires:      gem(puppet-syntax) >= 3.0
Requires:      gem(rspec-github) >= 2.0
Requires:      gem(rspec-puppet) >= 4.0
Conflicts:     gem(mocha) >= 2
Conflicts:     gem(pathspec) >= 2.0.0
Conflicts:     gem(puppet-lint) >= 5
Conflicts:     gem(puppet-syntax) >= 4
Conflicts:     gem(rspec-github) >= 3
Conflicts:     gem(rspec-puppet) >= 5
Provides:      gem(puppetlabs_spec_helper) = 7.0.2


%description
Contains rake tasks and a standard spec_helper for running spec tests on puppet
modules.


%package       -n gem-puppetlabs-spec-helper-doc
Version:       7.0.2
Release:       alt1
Summary:       Standard tasks and configuration for module spec tests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puppetlabs_spec_helper
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(puppetlabs_spec_helper) = 7.0.2

%description   -n gem-puppetlabs-spec-helper-doc
Standard tasks and configuration for module spec tests documentation
files.

Contains rake tasks and a standard spec_helper for running spec tests on puppet
modules.

%description   -n gem-puppetlabs-spec-helper-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета puppetlabs_spec_helper.


%package       -n gem-puppetlabs-spec-helper-devel
Version:       7.0.2
Release:       alt1
Summary:       Standard tasks and configuration for module spec tests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puppetlabs_spec_helper
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puppetlabs_spec_helper) = 7.0.2
Requires:      gem(puppet) >= 0
Requires:      gem(codecov) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-console) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry-stack_explorer) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.1
Requires:      gem(rspec-its) >= 1.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(fakefs) >= 0
Requires:      gem(yard) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-its) >= 2
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-rspec) >= 3
Conflicts:     gem(rubocop-performance) >= 2

%description   -n gem-puppetlabs-spec-helper-devel
Standard tasks and configuration for module spec tests development
package.

Contains rake tasks and a standard spec_helper for running spec tests on puppet
modules.

%description   -n gem-puppetlabs-spec-helper-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета puppetlabs_spec_helper.


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

%files         -n gem-puppetlabs-spec-helper-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-puppetlabs-spec-helper-devel
%doc README.md


%changelog
* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 7.0.2-alt1
- + packaged gem with Ruby Policy 2.0
