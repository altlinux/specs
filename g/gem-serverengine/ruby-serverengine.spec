%define        gemname serverengine

Name:          gem-serverengine
Version:       2.2.4
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
BuildRequires: gem(sigdump) >= 0.2.2 gem(sigdump) < 0.3
BuildRequires: gem(rake) >= 11.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 2.13.0 gem(rspec) < 4
BuildRequires: gem(rake-compiler-dock) >= 0.5.0 gem(rake-compiler-dock) < 2
BuildRequires: gem(rake-compiler) >= 0.9.4 gem(rake-compiler) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
%ruby_use_gem_dependency rake-compiler-dock >= 1.1.0,rake-compiler-dock < 2
Requires:      gem(sigdump) >= 0.2.2 gem(sigdump) < 0.3
Obsoletes:     ruby-serverengine < %EVR
Provides:      ruby-serverengine = %EVR
Provides:      gem(serverengine) = 2.2.4


%description
ServerEngine is a framework to implement robust multiprocess servers like
Unicorn.


%package       -n gem-serverengine-doc
Version:       2.2.4
Release:       alt1
Summary:       A framework to implement robust multiprocess servers like Unicorn documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета serverengine
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(serverengine) = 2.2.4

%description   -n gem-serverengine-doc
A framework to implement robust multiprocess servers like Unicorn documentation
files.

ServerEngine is a framework to implement robust multiprocess servers like
Unicorn.

%description   -n gem-serverengine-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета serverengine.


%package       -n gem-serverengine-devel
Version:       2.2.4
Release:       alt1
Summary:       A framework to implement robust multiprocess servers like Unicorn development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета serverengine
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(serverengine) = 2.2.4
Requires:      gem(rake) >= 11.0 gem(rake) < 14
Requires:      gem(rspec) >= 2.13.0 gem(rspec) < 4
Requires:      gem(rake-compiler-dock) >= 0.5.0 gem(rake-compiler-dock) < 2
Requires:      gem(rake-compiler) >= 0.9.4 gem(rake-compiler) < 2

%description   -n gem-serverengine-devel
A framework to implement robust multiprocess servers like Unicorn development
package.

ServerEngine is a framework to implement robust multiprocess servers like
Unicorn.

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
* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 2.2.4-alt1
- ^ 2.0.7 -> 2.2.4

* Sun Sep 30 2018 Mikhail Gordeev <obirvalger@altlinux.org> 2.0.7-alt1
- Initial build for Sisyphus
