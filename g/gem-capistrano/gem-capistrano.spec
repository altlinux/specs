%define        gemname capistrano

Name:          gem-capistrano
Version:       3.17.1
Release:       alt1
Summary:       Capistrano -- Welcome to easy deployment with Ruby over SSH
License:       MIT
Group:         Development/Ruby
Url:           https://capistranorb.com/
Vcs:           https://github.com/capistrano/capistrano.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rspec-core) >= 3.4.4
BuildRequires: gem(cucumber) >= 0
BuildRequires: gem(danger) >= 0
BuildRequires: gem(rubocop) >= 0.48.1
BuildRequires: gem(airbrussh) >= 1.0.0
BuildRequires: gem(i18n) >= 0
BuildRequires: gem(rake) >= 10.0.0
BuildRequires: gem(sshkit) >= 1.9.0
BuildConflicts: gem(rspec-core) >= 4
BuildConflicts: gem(psych) >= 5
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rspec-core >= 3.10.1,rspec-core < 4
%ruby_use_gem_dependency psych >= 4.0.3,psych < 5
Requires:      gem(airbrussh) >= 1.0.0
Requires:      gem(i18n) >= 0
Requires:      gem(rake) >= 10.0.0
Requires:      gem(sshkit) >= 1.9.0
Obsoletes:     ruby-capistrano < %EVR
Provides:      ruby-capistrano = %EVR
Provides:      gem(capistrano) = 3.17.1


%description
Capistrano is a framework for building automated deployment scripts. Although
Capistrano itself is written in Ruby, it can easily be used to deploy projects
of any language or framework, be it Rails, Java, or PHP.


%package       -n cap
Version:       3.17.1
Release:       alt1
Summary:       Capistrano -- Welcome to easy deployment with Ruby over SSH executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета capistrano
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(capistrano) = 3.17.1

%description   -n cap
Capistrano -- Welcome to easy deployment with Ruby over SSH
executable(s).

Capistrano is a framework for building automated deployment scripts. Although
Capistrano itself is written in Ruby, it can easily be used to deploy projects
of any language or framework, be it Rails, Java, or PHP.

%description   -n cap -l ru_RU.UTF-8
Исполнямка для самоцвета capistrano.


%package       -n gem-capistrano-doc
Version:       3.17.1
Release:       alt1
Summary:       Capistrano -- Welcome to easy deployment with Ruby over SSH documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета capistrano
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(capistrano) = 3.17.1

%description   -n gem-capistrano-doc
Capistrano -- Welcome to easy deployment with Ruby over SSH documentation
files.

Capistrano is a framework for building automated deployment scripts. Although
Capistrano itself is written in Ruby, it can easily be used to deploy projects
of any language or framework, be it Rails, Java, or PHP.

%description   -n gem-capistrano-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета capistrano.


%package       -n gem-capistrano-devel
Version:       3.17.1
Release:       alt1
Summary:       Capistrano -- Welcome to easy deployment with Ruby over SSH development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета capistrano
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(capistrano) = 3.17.1
Requires:      gem(mocha) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rspec-core) >= 3.4.4
Requires:      gem(danger) >= 0
Requires:      gem(rubocop) >= 0.48.1
Conflicts:     gem(rspec-core) >= 4
Conflicts:     gem(psych) >= 5
Conflicts:     gem(rubocop) >= 2

%description   -n gem-capistrano-devel
Capistrano -- Welcome to easy deployment with Ruby over SSH development
package.

Capistrano is a framework for building automated deployment scripts. Although
Capistrano itself is written in Ruby, it can easily be used to deploy projects
of any language or framework, be it Rails, Java, or PHP.

%description   -n gem-capistrano-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета capistrano.


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

%files         -n cap
%doc README.md
%_bindir/cap
%_bindir/capify

%files         -n gem-capistrano-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-capistrano-devel
%doc README.md


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 3.17.1-alt1
- ^ 3.16.0 -> 3.17.1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.16.0-alt1
- ^ 3.11.0 -> 3.16.0

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 3.11.0-alt1.1
- Fix spec

* Mon Feb 18 2019 Pavel Skrylev <majioa@altlinux.org> 3.11.0-alt1
- Bump to 3.11.0;
- Use Ruby Policy 2.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.10-alt1.3
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.5.10-alt1.2
- Rebuild with Ruby 2.4.1

* Fri Dec 07 2012 Led <led@altlinux.ru> 2.5.10-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sat Dec 05 2009 Igor Zubkov <icesik@altlinux.org> 2.5.10-alt1
- build for Sisyphus
