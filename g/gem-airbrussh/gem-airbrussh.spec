%define        gemname airbrussh

Name:          gem-airbrussh
Version:       1.4.1
Release:       alt1
Summary:       Airbrussh pretties up your SSHKit and Capistrano output
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mattbrictson/airbrussh
Vcs:           https://github.com/mattbrictson/airbrussh.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 12.0
BuildRequires: gem(minitest) >= 5.10
BuildRequires: gem(minitest-reporters) >= 1.1
BuildRequires: gem(mocha) >= 1.2
BuildRequires: gem(coveralls_reborn) >= 0.24.0
BuildRequires: gem(rubocop) >= 0.50.0
BuildRequires: gem(guard) >= 2.2.2
BuildRequires: gem(guard-minitest) >= 0
BuildRequires: gem(rb-fsevent) >= 0
BuildRequires: gem(terminal-notifier-guard) >= 0
BuildRequires: gem(sshkit) > 1.7.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-reporters) >= 2
BuildConflicts: gem(mocha) >= 2
BuildConflicts: gem(coveralls_reborn) >= 0.25
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(sshkit) > 1.7.0
Provides:      gem(airbrussh) = 1.4.1


%description
Airbrussh is a concise log formatter for Capistrano and SSHKit. It displays
well-formatted, useful log output that is easy to read. Airbrussh also saves
Capistrano's verbose output to a separate log file just in case you need
additional details for troubleshooting.

As of April 2016, Airbrussh is bundled with Capistrano 3.5, and is Capistrano's
default formatter! There is nothing additional to install or enable. Continue
reading to learn more about Airbrussh's features and configuration options.

If you aren't yet using Capistrano 3.5 (or wish to use Airbrussh with SSHKit
directly), refer to the advanced/legacy usage section for installation
instructions.


%package       -n gem-airbrussh-doc
Version:       1.4.1
Release:       alt1
Summary:       Airbrussh pretties up your SSHKit and Capistrano output documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета airbrussh
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(airbrussh) = 1.4.1

%description   -n gem-airbrussh-doc
Airbrussh pretties up your SSHKit and Capistrano output documentation
files.

Airbrussh is a concise log formatter for Capistrano and SSHKit. It displays
well-formatted, useful log output that is easy to read. Airbrussh also saves
Capistrano's verbose output to a separate log file just in case you need
additional details for troubleshooting.

As of April 2016, Airbrussh is bundled with Capistrano 3.5, and is Capistrano's
default formatter! There is nothing additional to install or enable. Continue
reading to learn more about Airbrussh's features and configuration options.

If you aren't yet using Capistrano 3.5 (or wish to use Airbrussh with SSHKit
directly), refer to the advanced/legacy usage section for installation
instructions.

%description   -n gem-airbrussh-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета airbrussh.


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

%files         -n gem-airbrussh-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- ^ 1.4.0 -> 1.4.1 (no devel)

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- ^ 1.3.1 -> 1.4.0

* Thu Mar 07 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus with usage of Ruby Policy 2.0.
