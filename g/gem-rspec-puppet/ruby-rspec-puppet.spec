%define        gemname rspec-puppet

Name:          gem-rspec-puppet
Version:       2.9.0
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
BuildRequires: gem(rspec) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rspec) >= 0 gem(rspec) < 4
Obsoletes:     ruby-rspec-puppet < %EVR
Provides:      ruby-rspec-puppet = %EVR
Provides:      gem(rspec-puppet) = 2.9.0


%description
RSpec tests for your Puppet manifests & modules.


%package       -n rspec-puppet-init
Version:       2.9.0
Release:       alt1
Summary:       RSpec tests for your Puppet manifests executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rspec-puppet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-puppet) = 2.9.0

%description   -n rspec-puppet-init
RSpec tests for your Puppet manifests executable(s).

RSpec tests for your Puppet manifests & modules.

%description   -n rspec-puppet-init -l ru_RU.UTF-8
Исполнямка для самоцвета rspec-puppet.


%package       -n gem-rspec-puppet-doc
Version:       2.9.0
Release:       alt1
Summary:       RSpec tests for your Puppet manifests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-puppet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-puppet) = 2.9.0

%description   -n gem-rspec-puppet-doc
RSpec tests for your Puppet manifests documentation files.

RSpec tests for your Puppet manifests & modules.

%description   -n gem-rspec-puppet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-puppet.


%package       -n gem-rspec-puppet-devel
Version:       2.9.0
Release:       alt1
Summary:       RSpec tests for your Puppet manifests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-puppet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-puppet) = 2.9.0

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
