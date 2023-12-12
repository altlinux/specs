%define        _unpackaged_files_terminate_build 1
%define        gemname amazon-ec2

Name:          gem-amazon-ec2
Version:       0.9.17.13
Release:       alt0.1
Summary:       A Ruby Gem that gives you full access to several of the Amazon Web Services API from your Ruby/Ruby on Rails apps
License:       MIT or Ruby
Group:         Development/Ruby
Url:           https://github.com/grempe/amazon-ec2
Vcs:           https://github.com/grempe/amazon-ec2.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(mocha) >= 0.9.9
BuildRequires: gem(test-unit) >= 2.1.2
BuildRequires: gem(test-spec) >= 0.10.0
BuildRequires: gem(rcov) >= 0.9.9
BuildRequires: gem(yard) >= 0.6.2
BuildRequires: gem(xml-simple) >= 1.0.12
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(xml-simple) >= 1.0.12
Obsoletes:     ruby-amazon-ec2 < %EVR
Provides:      ruby-amazon-ec2 = %EVR
Provides:      gem(amazon-ec2) = 0.9.17.13

%ruby_use_gem_version amazon-ec2:0.9.17.13
%ruby_bindir_to %ruby_bindir

%description
A Ruby Gem that gives you full access to several of the Amazon Web Services API
from your Ruby/Ruby on Rails apps.


%package       -n amazon-ec2
Version:       0.9.17.13
Release:       alt0.1
Summary:       A Ruby Gem that gives you full access to several of the Amazon Web Services API from your Ruby/Ruby on Rails apps executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета amazon-ec2
Group:         Other
BuildArch:     noarch

Requires:      gem(amazon-ec2) = 0.9.17.13

%description   -n amazon-ec2
A Ruby Gem that gives you full access to several of the Amazon Web Services API
from your Ruby/Ruby on Rails apps executable(s).

%description   -n amazon-ec2 -l ru_RU.UTF-8
Исполнямка для самоцвета amazon-ec2.


%package       -n gem-amazon-ec2-doc
Version:       0.9.17.13
Release:       alt0.1
Summary:       A Ruby Gem that gives you full access to several of the Amazon Web Services API from your Ruby/Ruby on Rails apps documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета amazon-ec2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(amazon-ec2) = 0.9.17.13

%description   -n gem-amazon-ec2-doc
A Ruby Gem that gives you full access to several of the Amazon Web Services API
from your Ruby/Ruby on Rails apps documentation files.

%description   -n gem-amazon-ec2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета amazon-ec2.


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
%ruby_bindir/awshell
%ruby_bindir/ec2-gem-example.rb
%ruby_bindir/ec2-gem-profile.rb
%ruby_bindir/ec2sh
%ruby_bindir/setup.rb

%files         -n gem-amazon-ec2-doc
%doc README.rdoc
%ruby_gemdocdir


%changelog
* Tue Nov 28 2023 Pavel Skrylev <majioa@altlinux.org> 0.9.17.13-alt0.1
- ^ 0.9.17 -> 0.9.17p13 without devel

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
