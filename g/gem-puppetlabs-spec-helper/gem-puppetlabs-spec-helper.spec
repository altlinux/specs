%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname puppetlabs_spec_helper

Name:          gem-puppetlabs-spec-helper
Version:       8.0.0
Release:       alt1
Summary:       Standard tasks and configuration for module spec tests
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://github.com/puppetlabs/puppetlabs_spec_helper
Vcs:           https://github.com/puppetlabs/puppetlabs_spec_helper.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(fakefs) >= 0
BuildRequires: gem(mocha) >= 1.0
BuildRequires: gem(pathspec) >= 0.2
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0
BuildRequires: gem(puppet) >= 0
BuildRequires: gem(puppet-lint) >= 4.0
BuildRequires: gem(puppet-syntax) >= 4.1.1
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.1
BuildRequires: gem(rspec-github) >= 2.0
BuildRequires: gem(rspec-its) >= 1.0
BuildRequires: gem(rspec-puppet) >= 5.0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-console) >= 0
BuildRequires: gem(voxpupuli-rubocop) >= 2.8.0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(pathspec) >= 3
BuildConflicts: gem(puppet-lint) >= 5
BuildConflicts: gem(puppet-syntax) >= 8
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-github) >= 4
BuildConflicts: gem(rspec-its) >= 3
BuildConflicts: gem(rspec-puppet) >= 6
BuildConflicts: gem(voxpupuli-rubocop) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency voxpupuli-rubocop >= 5.2.0,voxpupuli-rubocop < 6
%ruby_use_gem_dependency puppet-syntax >= 7.2.0,puppet-syntax < 8
%ruby_alias_names puppetlabs_spec_helper,puppetlabs-spec-helper
Requires:      ruby >= 3.1.0
Requires:      gem(mocha) >= 1.0
Requires:      gem(pathspec) >= 0.2
Requires:      gem(puppet-lint) >= 4.0
Requires:      gem(puppet-syntax) >= 4.1.1
Requires:      gem(rspec-github) >= 2.0
Requires:      gem(rspec-puppet) >= 5.0
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(pathspec) >= 3
Conflicts:     gem(puppet-lint) >= 5
Conflicts:     gem(puppet-syntax) >= 8
Conflicts:     gem(rspec-github) >= 4
Conflicts:     gem(rspec-puppet) >= 6
Provides:      gem(puppetlabs_spec_helper) = 8.0.0

%description
Contains rake tasks and a standard spec_helper for running spec tests on puppet
modules.


%if_enabled    doc
%package       -n gem-puppetlabs-spec-helper-doc
Version:       8.0.0
Release:       alt1
Summary:       Standard tasks and configuration for module spec tests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puppetlabs_spec_helper
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(puppetlabs_spec_helper) = 8.0.0

%description   -n gem-puppetlabs-spec-helper-doc
Standard tasks and configuration for module spec tests documentation
files.

Contains rake tasks and a standard spec_helper for running spec tests on puppet
modules.

%description   -n gem-puppetlabs-spec-helper-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета puppetlabs_spec_helper.
%endif


%if_enabled    devel
%package       -n gem-puppetlabs-spec-helper-devel
Version:       8.0.0
Release:       alt1
Summary:       Standard tasks and configuration for module spec tests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puppetlabs_spec_helper
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(puppetlabs_spec_helper) = 8.0.0
Requires:      gem(fakefs) >= 0
Requires:      gem(mocha) >= 1.0
Requires:      gem(pathspec) >= 0.2
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry-stack_explorer) >= 0
Requires:      gem(puppet) >= 0
Requires:      gem(puppet-lint) >= 4.0
Requires:      gem(puppet-syntax) >= 4.1.1
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.1
Requires:      gem(rspec-github) >= 2.0
Requires:      gem(rspec-its) >= 1.0
Requires:      gem(rspec-puppet) >= 5.0
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-console) >= 0
Requires:      gem(voxpupuli-rubocop) >= 2.8.0
Requires:      gem(yard) >= 0
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(pathspec) >= 3
Conflicts:     gem(puppet-lint) >= 5
Conflicts:     gem(puppet-syntax) >= 8
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-github) >= 4
Conflicts:     gem(rspec-its) >= 3
Conflicts:     gem(rspec-puppet) >= 6
Conflicts:     gem(voxpupuli-rubocop) >= 6

%description   -n gem-puppetlabs-spec-helper-devel
Standard tasks and configuration for module spec tests development
package.

Contains rake tasks and a standard spec_helper for running spec tests on puppet
modules.

%description   -n gem-puppetlabs-spec-helper-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета puppetlabs_spec_helper.
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
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-puppetlabs-spec-helper-doc
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-puppetlabs-spec-helper-devel
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 8.0.0-alt1
- ^ 7.0.2 -> 8.0.0

* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 7.0.2-alt1
- + packaged gem with Ruby Policy 2.0
