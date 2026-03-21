%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname capistrano

Name:          gem-capistrano
Version:       3.20.0
Release:       alt1
Summary:       Capistrano -- Welcome to easy deployment with Ruby over SSH
License:       MIT
Group:         Development/Ruby
Url:           https://capistranorb.com/
Vcs:           https://github.com/capistrano/capistrano.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(airbrussh) >= 1.0.0
BuildRequires: gem(cucumber) >= 10.1
BuildRequires: gem(i18n) >= 0
BuildRequires: gem(mocha) >= 3.0
BuildRequires: gem(rake) >= 10.0.0
BuildRequires: gem(rspec) >= 3.13
BuildRequires: gem(rubocop) = 1.81.7
BuildRequires: gem(sshkit) >= 1.9.0
BuildConflicts: gem(cucumber) >= 11
BuildConflicts: gem(mocha) >= 4
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.5
Requires:      gem(airbrussh) >= 1.0.0
Requires:      gem(i18n) >= 0
Requires:      gem(rake) >= 10.0.0
Requires:      gem(sshkit) >= 1.9.0
Obsoletes:     ruby-capistrano < %EVR
Provides:      ruby-capistrano = %EVR
Provides:      capistrano = %EVR
Provides:      gem(capistrano) = 3.20.0

%description
Capistrano is a framework for building automated deployment scripts. Although
Capistrano itself is written in Ruby, it can easily be used to deploy projects
of any language or framework, be it Rails, Java, or PHP.


%package       -n cap
Version:       3.20.0
Release:       alt1
Summary:       Capistrano -- Welcome to easy deployment with Ruby over SSH executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета capistrano
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(capistrano) = 3.20.0

%description   -n cap
Capistrano -- Welcome to easy deployment with Ruby over SSH
executable(s).

Capistrano is a framework for building automated deployment scripts. Although
Capistrano itself is written in Ruby, it can easily be used to deploy projects
of any language or framework, be it Rails, Java, or PHP.

%description   -n cap -l ru_RU.UTF-8
Исполнямка для самоцвета capistrano.


%if_enabled    doc
%package       -n gem-capistrano-doc
Version:       3.20.0
Release:       alt1
Summary:       Capistrano -- Welcome to easy deployment with Ruby over SSH documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета capistrano
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(capistrano) = 3.20.0

%description   -n gem-capistrano-doc
Capistrano -- Welcome to easy deployment with Ruby over SSH documentation
files.

Capistrano is a framework for building automated deployment scripts. Although
Capistrano itself is written in Ruby, it can easily be used to deploy projects
of any language or framework, be it Rails, Java, or PHP.

%description   -n gem-capistrano-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета capistrano.
%endif


%if_enabled    devel
%package       -n gem-capistrano-devel
Version:       3.20.0
Release:       alt1
Summary:       Capistrano -- Welcome to easy deployment with Ruby over SSH development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета capistrano
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(capistrano) = 3.20.0

%description   -n gem-capistrano-devel
Capistrano -- Welcome to easy deployment with Ruby over SSH development
package.

Capistrano is a framework for building automated deployment scripts. Although
Capistrano itself is written in Ruby, it can easily be used to deploy projects
of any language or framework, be it Rails, Java, or PHP.

%description   -n gem-capistrano-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета capistrano.
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
%doc CHANGELOG.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n cap
%doc CHANGELOG.md CONTRIBUTING.md LICENSE.txt README.md
%_bindir/cap
%_bindir/capify

%if_enabled    doc
%files         -n gem-capistrano-doc
%doc CHANGELOG.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-capistrano-devel
%doc CHANGELOG.md CONTRIBUTING.md LICENSE.txt README.md
%endif


%changelog
* Fri Mar 20 2026 Pavel Skrylev <majioa@altlinux.org> 3.20.0-alt1
- ^ 3.17.1 -> 3.20.0

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
