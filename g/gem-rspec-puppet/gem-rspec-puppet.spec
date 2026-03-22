%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rspec-puppet

Name:          gem-rspec-puppet
Version:       5.0.0
Release:       alt1
Summary:       RSpec tests for your Puppet manifests
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rodjek/rspec-puppet/
Vcs:           https://github.com/rodjek/rspec-puppet.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(facter) >= 0
BuildRequires: gem(fuubar) >= 0
BuildRequires: gem(json_pure) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0
BuildRequires: gem(puppet) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-console) >= 0
BuildRequires: gem(sync) >= 0
BuildRequires: gem(voxpupuli-rubocop) >= 3.0.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(voxpupuli-rubocop) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency voxpupuli-rubocop >= 5.2.0,voxpupuli-rubocop < 6
Requires:      ruby >= 3.1.0
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(rspec) >= 4
Obsoletes:     ruby-rspec-puppet < %EVR
Provides:      ruby-rspec-puppet = %EVR
Provides:      gem(rspec-puppet) = 5.0.0

%description
RSpec tests for your Puppet manifests & modules.


%package       -n rspec-puppet-init
Version:       5.0.0
Release:       alt1
Summary:       RSpec tests for your Puppet manifests executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rspec-puppet
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rspec-puppet) = 5.0.0

%description   -n rspec-puppet-init
RSpec tests for your Puppet manifests executable(s).

RSpec tests for your Puppet manifests & modules.

%description   -n rspec-puppet-init -l ru_RU.UTF-8
Исполнямка для самоцвета rspec-puppet.


%if_enabled    doc
%package       -n gem-rspec-puppet-doc
Version:       5.0.0
Release:       alt1
Summary:       RSpec tests for your Puppet manifests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-puppet
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rspec-puppet) = 5.0.0

%description   -n gem-rspec-puppet-doc
RSpec tests for your Puppet manifests documentation files.

RSpec tests for your Puppet manifests & modules.

%description   -n gem-rspec-puppet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-puppet.
%endif


%if_enabled    devel
%package       -n gem-rspec-puppet-devel
Version:       5.0.0
Release:       alt1
Summary:       RSpec tests for your Puppet manifests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-puppet
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rspec-puppet) = 5.0.0
Requires:      gem(voxpupuli-rubocop) >= 3.0.0
Conflicts:     gem(voxpupuli-rubocop) >= 6

%description   -n gem-rspec-puppet-devel
RSpec tests for your Puppet manifests development package.

RSpec tests for your Puppet manifests & modules.

%description   -n gem-rspec-puppet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-puppet.
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
%doc CHANGELOG.md LICENSE README.md HISTORY.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n rspec-puppet-init
%doc CHANGELOG.md LICENSE README.md HISTORY.md
%_bindir/rspec-puppet-init

%if_enabled    doc
%files         -n gem-rspec-puppet-doc
%doc CHANGELOG.md LICENSE README.md HISTORY.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rspec-puppet-devel
%doc CHANGELOG.md LICENSE README.md HISTORY.md
%endif


%changelog
* Sun Mar 22 2026 Pavel Skrylev <majioa@altlinux.org> 5.0.0-alt1
- ^ 4.0.2 -> 5.0.0

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
