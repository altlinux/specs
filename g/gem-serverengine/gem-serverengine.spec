%define        gemname serverengine

Name:          gem-serverengine
Version:       2.3.1
Release:       alt1
Summary:       A framework to implement robust multiprocess servers like Unicorn
License:       Apache 2.0
Group:         Development/Ruby
Url:           https://github.com/treasure-data/serverengine
Vcs:           https://github.com/treasure-data/serverengine.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 11.0
BuildRequires: gem(rspec) >= 2.13.0
BuildRequires: gem(rake-compiler-dock) >= 0.5.0
BuildRequires: gem(rake-compiler) >= 0.9.4
BuildRequires: gem(timecop) >= 0.9.5
BuildRequires: gem(rr) >= 3.1
BuildRequires: gem(sigdump) >= 0.2.2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rake-compiler-dock) >= 2
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(timecop) >= 0.10
BuildConflicts: gem(rr) >= 4
BuildConflicts: gem(sigdump) >= 0.3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
%ruby_use_gem_dependency rake-compiler-dock >= 1.2.1,rake-compiler-dock < 2
Requires:      gem(sigdump) >= 0.2.2
Conflicts:     gem(sigdump) >= 0.3
Obsoletes:     ruby-serverengine < %EVR
Provides:      ruby-serverengine = %EVR
Provides:      gem(serverengine) = 2.3.1


%description
ServerEngine is a framework to implement robust multiprocess servers like
Unicorn.


%package       -n gem-serverengine-doc
Version:       2.3.1
Release:       alt1
Summary:       A framework to implement robust multiprocess servers like Unicorn documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета serverengine
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(serverengine) = 2.3.1

%description   -n gem-serverengine-doc
A framework to implement robust multiprocess servers like Unicorn documentation
files.

%description   -n gem-serverengine-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета serverengine.


%package       -n gem-serverengine-devel
Version:       2.3.1
Release:       alt1
Summary:       A framework to implement robust multiprocess servers like Unicorn development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета serverengine
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(serverengine) = 2.3.1
Requires:      gem(rake) >= 11.0
Requires:      gem(rspec) >= 2.13.0
Requires:      gem(rake-compiler-dock) >= 0.5.0
Requires:      gem(rake-compiler) >= 0.9.4
Requires:      gem(timecop) >= 0.9.5
Requires:      gem(rr) >= 3.1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rake-compiler-dock) >= 2
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(timecop) >= 0.10
Conflicts:     gem(rr) >= 4

%description   -n gem-serverengine-devel
A framework to implement robust multiprocess servers like Unicorn development
package.

%description   -n gem-serverengine-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета serverengine.


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

%files         -n gem-serverengine-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-serverengine-devel
%doc README.md


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt1
- ^ 2.2.5 -> 2.3.1

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 2.2.5-alt1
- ^ 2.2.4 -> 2.2.5

* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 2.2.4-alt1
- ^ 2.0.7 -> 2.2.4

* Sun Sep 30 2018 Mikhail Gordeev <obirvalger@altlinux.org> 2.0.7-alt1
- Initial build for Sisyphus
