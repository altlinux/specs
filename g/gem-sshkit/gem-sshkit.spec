%define        gemname sshkit

Name:          gem-sshkit
Version:       1.21.3
Release:       alt1
Summary:       A toolkit for deploying code and assets to servers in a repeatable, testable, reliable way
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/capistrano/sshkit
Vcs:           https://github.com/capistrano/sshkit.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(danger) >= 0
BuildRequires: gem(minitest) >= 5.0.0
BuildRequires: gem(minitest-reporters) >= 0
BuildRequires: gem(rainbow) >= 2.2.2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0.49.1
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(bcrypt_pbkdf) >= 0
BuildRequires: gem(ed25519) >= 1.2
BuildRequires: gem(net-ssh) >= 2.8.0
BuildRequires: gem(net-scp) >= 1.1.2
BuildConflicts: gem(rainbow) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(ed25519) >= 2.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rainbow >= 3.1.0,rainbow < 4
Requires:      gem(net-ssh) >= 2.8.0
Requires:      gem(net-scp) >= 1.1.2
Provides:      gem(sshkit) = 1.21.3


%description
SSHKit is a toolkit for running commands in a structured way on one or more
servers.


%package       -n gem-sshkit-doc
Version:       1.21.3
Release:       alt1
Summary:       A toolkit for deploying code and assets to servers in a repeatable, testable, reliable way documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sshkit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sshkit) = 1.21.3

%description   -n gem-sshkit-doc
A toolkit for deploying code and assets to servers in a repeatable, testable,
reliable way documentation files.

SSHKit is a toolkit for running commands in a structured way on one or more
servers.

%description   -n gem-sshkit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sshkit.


%package       -n gem-sshkit-devel
Version:       1.21.3
Release:       alt1
Summary:       A toolkit for deploying code and assets to servers in a repeatable, testable, reliable way development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sshkit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sshkit) = 1.21.3
Requires:      gem(danger) >= 0
Requires:      gem(minitest) >= 5.0.0
Requires:      gem(minitest-reporters) >= 0
Requires:      gem(rainbow) >= 2.2.2
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0.49.1
Requires:      gem(mocha) >= 0
Requires:      gem(bcrypt_pbkdf) >= 0
Requires:      gem(ed25519) >= 1.2
Conflicts:     gem(rainbow) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(ed25519) >= 2.0

%description   -n gem-sshkit-devel
A toolkit for deploying code and assets to servers in a repeatable, testable,
reliable way development package.

SSHKit is a toolkit for running commands in a structured way on one or more
servers.

%description   -n gem-sshkit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sshkit.


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

%files         -n gem-sshkit-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sshkit-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.21.3-alt1
- ^ 1.21.2 -> 1.21.3

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.21.2-alt1
- ^ 1.18.2 -> 1.21.2

* Thu Mar 07 2019 Pavel Skrylev <majioa@altlinux.org> 1.18.2-alt1
- Initial build for Sisyphus with usage of Ruby Policy 2.0.
