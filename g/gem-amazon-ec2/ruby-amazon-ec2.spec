%define        gemname amazon-ec2

Name:          gem-amazon-ec2
Version:       0.9.17
Release:       alt3.1
Summary:       A Ruby Gem that gives you full access to several of the Amazon Web Services API from your Ruby/Ruby on Rails apps
License:       MIT or Ruby
Group:         Development/Ruby
Url:           https://github.com/grempe/amazon-ec2
Vcs:           https://github.com/grempe/amazon-ec2.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(xml-simple) >= 1.0.12
BuildRequires: gem(mocha) >= 0.9.9 gem(mocha) < 2
# BuildRequires: gem(test-spec) >= 0.10.0
# BuildRequires: gem(rcov) >= 0.9.9
# BuildRequires: gem(perftools.rb) >= 0.5.4
BuildRequires: gem(yard) >= 0.6.2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
Requires:      gem(xml-simple) >= 1.0.12
Obsoletes:     ruby-amazon-ec2 < %EVR
Provides:      ruby-amazon-ec2 = %EVR
Provides:      gem(amazon-ec2) = 0.9.17


%description
A Ruby Gem that gives you full access to several of the Amazon Web Services API
from your Ruby/Ruby on Rails apps.


%package       -n amazon-ec2
Version:       0.9.17
Release:       alt3.1
Summary:       A Ruby Gem that gives you full access to several of the Amazon Web Services API from your Ruby/Ruby on Rails apps executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета amazon-ec2
Group:         Other
BuildArch:     noarch

Requires:      gem(amazon-ec2) = 0.9.17

%description   -n amazon-ec2
A Ruby Gem that gives you full access to several of the Amazon Web Services API
from your Ruby/Ruby on Rails apps executable(s).

%description   -n amazon-ec2 -l ru_RU.UTF-8
Исполнямка для самоцвета amazon-ec2.


%package       -n gem-amazon-ec2-doc
Version:       0.9.17
Release:       alt3.1
Summary:       A Ruby Gem that gives you full access to several of the Amazon Web Services API from your Ruby/Ruby on Rails apps documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета amazon-ec2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(amazon-ec2) = 0.9.17

%description   -n gem-amazon-ec2-doc
A Ruby Gem that gives you full access to several of the Amazon Web Services API
from your Ruby/Ruby on Rails apps documentation files.

%description   -n gem-amazon-ec2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета amazon-ec2.


%package       -n gem-amazon-ec2-devel
Version:       0.9.17
Release:       alt3.1
Summary:       A Ruby Gem that gives you full access to several of the Amazon Web Services API from your Ruby/Ruby on Rails apps development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета amazon-ec2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(amazon-ec2) = 0.9.17
Requires:      gem(mocha) >= 0.9.9 gem(mocha) < 2
# Requires:      gem(test-spec) >= 0.10.0
# Requires:      gem(rcov) >= 0.9.9
# Requires:      gem(perftools.rb) >= 0.5.4
Requires:      gem(yard) >= 0.6.2

%description   -n gem-amazon-ec2-devel
A Ruby Gem that gives you full access to several of the Amazon Web Services API
from your Ruby/Ruby on Rails apps development package.

%description   -n gem-amazon-ec2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета amazon-ec2.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n amazon-ec2
%doc README.rdoc
%_bindir/awshell
%_bindir/ec2-gem-example.rb
%_bindir/ec2-gem-profile.rb
%_bindir/ec2sh
%_bindir/setup.rb

%files         -n gem-amazon-ec2-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-amazon-ec2-devel
%doc README.rdoc


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.9.17-alt3.1
- ! spec

* Mon Mar 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.17-alt3
- Removed unnecessary test dep.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.17-alt2.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.17-alt2
- Fix tests.

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.17-alt1
- Initial build for Sisyphus.
