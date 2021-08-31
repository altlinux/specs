%define        gemname iostruct

Name:          gem-iostruct
Version:       0.0.4
Release:       alt2
Summary:       A Struct that can read/write itself from/to IO-like objects
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/zed-0xff/iostruct
Vcs:           https://github.com/zed-0xff/iostruct.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Obsoletes:     ruby-iostruct < %EVR
Provides:      ruby-iostruct = %EVR
Provides:      gem(iostruct) = 0.0.4


%description
A Struct that can read/write itself from/to IO-like objects.


%package       -n gem-iostruct-doc
Version:       0.0.4
Release:       alt2
Summary:       A Struct that can read/write itself from/to IO-like objects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета iostruct
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(iostruct) = 0.0.4

%description   -n gem-iostruct-doc
A Struct that can read/write itself from/to IO-like objects documentation
files.

%description   -n gem-iostruct-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета iostruct.


%package       -n gem-iostruct-devel
Version:       0.0.4
Release:       alt2
Summary:       A Struct that can read/write itself from/to IO-like objects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета iostruct
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(iostruct) = 0.0.4
Requires:      gem(bundler) >= 1.3 gem(bundler) < 3
Requires:      gem(rake) >= 0

%description   -n gem-iostruct-devel
A Struct that can read/write itself from/to IO-like objects development
package.

%description   -n gem-iostruct-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета iostruct.


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

%files         -n gem-iostruct-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-iostruct-devel
%doc README.md


%changelog
* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.4-alt2
- ! spec

* Mon Aug 27 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.4-alt1.1
- Rebuild for new Ruby autorequirements.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.4-alt1
- Initial build for Sisyphus
