%define        _unpackaged_files_terminate_build 1
%define        gemname puppet-lint

Name:          gem-puppet-lint
Epoch:         1
Version:       4.2.3
Release:       alt1
Summary:       Check that your Puppet manifests conform to the style guide
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rodjek/puppet-lint/
Vcs:           https://github.com/rodjek/puppet-lint.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec-its) >= 1.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(json) >= 0
BuildRequires: gem(rspec-json_expectations) >= 1.4
BuildRequires: gem(serverspec) >= 0
BuildRequires: gem(puppetlabs_spec_helper) >= 0
BuildRequires: gem(puppet_litmus) >= 0
BuildRequires: gem(github_changelog_generator) >= 1.15.0
BuildRequires: gem(faraday-retry) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildConflicts: gem(rspec-its) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-json_expectations) >= 2
BuildConflicts: gem(github_changelog_generator) >= 1.16
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(rubocop-performance) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
Obsoletes:     ruby-puppet-lint < %EVR
Provides:      ruby-puppet-lint = %EVR
Provides:      gem(puppet-lint) = 4.2.3

%ruby_bindir_to %ruby_bindir

%description
The goal of this project is to implement as many of the recommended Puppet style
guidelines from the Puppet Labs style guide as practical. It is not meant to
validate syntax. Please use "puppet parser validate" for that.


%package       -n puppet-lint
Version:       4.2.3
Release:       alt1
Summary:       Check that your Puppet manifests conform to the style guide executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета puppet-lint
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puppet-lint) = 4.2.3

%description   -n puppet-lint
Check that your Puppet manifests conform to the style guide executable(s).

The goal of this project is to implement as many of the recommended Puppet style
guidelines from the Puppet Labs style guide as practical. It is not meant to
validate syntax. Please use "puppet parser validate" for that.

%description   -n puppet-lint -l ru_RU.UTF-8
Исполнямка для самоцвета puppet-lint.


%package       -n gem-puppet-lint-doc
Version:       4.2.3
Release:       alt1
Summary:       Check that your Puppet manifests conform to the style guide documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puppet-lint
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(puppet-lint) = 4.2.3

%description   -n gem-puppet-lint-doc
Check that your Puppet manifests conform to the style guide documentation
files.

The goal of this project is to implement as many of the recommended Puppet style
guidelines from the Puppet Labs style guide as practical. It is not meant to
validate syntax. Please use "puppet parser validate" for that.

%description   -n gem-puppet-lint-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета puppet-lint.


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

%files         -n puppet-lint
%doc README.md
%ruby_bindir/puppet-lint

%files         -n gem-puppet-lint-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 1:4.2.3-alt1
- ^ 2.5.0 -> 4.2.3 without devel

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1:2.5.0-alt1
- v 3.0.1 -> 2.5.0

* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt0.1
^ 3.0.1 pre (really 2.3.6)
^ Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Feb 06 2017 Denis Medvedev <nbr@altlinux.org> 3.0.0-alt1
- bump to version 3.0.0

* Wed Dec 23 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build for ALT Linux
