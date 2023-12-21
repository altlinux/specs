%define        _unpackaged_files_terminate_build 1
%define        gemname rspec-puppet

Name:          gem-rspec-puppet
Version:       4.0.2
Release:       alt1
Summary:       RSpec tests for your Puppet manifests
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rodjek/rspec-puppet/
Vcs:           https://github.com/rodjek/rspec-puppet.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0
BuildRequires: gem(fuubar) >= 0
BuildRequires: gem(puppet) >= 0
BuildRequires: gem(facter) >= 0
BuildRequires: gem(json_pure) >= 0
BuildRequires: gem(sync) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(codecov) >= 0
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-console) >= 0
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rspec) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
Requires:      gem(rspec) >= 3.10.0
Obsoletes:     ruby-rspec-puppet < %EVR
Provides:      ruby-rspec-puppet = %EVR
Provides:      gem(rspec-puppet) = 4.0.2


%description
RSpec tests for your Puppet manifests & modules.


%package       -n rspec-puppet-init
Version:       4.0.2
Release:       alt1
Summary:       RSpec tests for your Puppet manifests executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rspec-puppet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-puppet) = 4.0.2

%description   -n rspec-puppet-init
RSpec tests for your Puppet manifests executable(s).

RSpec tests for your Puppet manifests & modules.

%description   -n rspec-puppet-init -l ru_RU.UTF-8
Исполнямка для самоцвета rspec-puppet.


%package       -n gem-rspec-puppet-doc
Version:       4.0.2
Release:       alt1
Summary:       RSpec tests for your Puppet manifests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-puppet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-puppet) = 4.0.2

%description   -n gem-rspec-puppet-doc
RSpec tests for your Puppet manifests documentation files.

RSpec tests for your Puppet manifests & modules.

%description   -n gem-rspec-puppet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-puppet.


%package       -n gem-rspec-puppet-devel
Version:       4.0.2
Release:       alt1
Summary:       RSpec tests for your Puppet manifests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-puppet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-puppet) = 4.0.2
Requires:      gem(pry) >= 0
Requires:      gem(pry-stack_explorer) >= 0
Requires:      gem(fuubar) >= 0
Requires:      gem(puppet) >= 0
Requires:      gem(facter) >= 0
Requires:      gem(json_pure) >= 0
Requires:      gem(sync) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(codecov) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-console) >= 0
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rspec) >= 3

%description   -n gem-rspec-puppet-devel
RSpec tests for your Puppet manifests development package.

RSpec tests for your Puppet manifests & modules.

%description   -n gem-rspec-puppet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-puppet.


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

%files         -n rspec-puppet-init
%doc README.md
%_bindir/rspec-puppet-init

%files         -n gem-rspec-puppet-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rspec-puppet-devel
%doc README.md


%changelog
* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 4.0.2-alt1
- ^ 2.9.0 -> 4.0.2

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.9.0-alt1
- ^ 2.7.5 -> 2.9.0

* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.5-alt1
^ v2.7.5
^ Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.6-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Wed Dec 23 2015 Andrey Cherepanov <cas@altlinux.org> 0.1.6-alt1
- Initial build for ALT Linux
