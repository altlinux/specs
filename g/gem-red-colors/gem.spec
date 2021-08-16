%define        gemname red-colors

Name:          gem-red-colors
Version:       0.3.0
Release:       alt1
Summary:       Red Colors provides a wide array of features for dealing with colors. This includes conversion between colorspaces, desaturation, and parsing colors
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/red-data-tools/red-colors
Vcs:           https://github.com/red-data-tools/red-colors.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(matrix) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(kramdown) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(matrix) >= 0
Provides:      gem(red-colors) = 0.3.0

%description
Red Colors provides a wide array of features for dealing with colors. This
includes conversion between colorspaces, desaturation, and parsing colors.


%package       -n gem-red-colors-doc
Version:       0.3.0
Release:       alt1
Summary:       Red Colors provides a wide array of features for dealing with colors. This includes conversion between colorspaces, desaturation, and parsing colors documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета red-colors
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(red-colors) = 0.3.0

%description   -n gem-red-colors-doc
Red Colors provides a wide array of features for dealing with colors. This
includes conversion between colorspaces, desaturation, and parsing colors
documentation files.

%description   -n gem-red-colors-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета red-colors.


%package       -n gem-red-colors-devel
Version:       0.3.0
Release:       alt1
Summary:       Red Colors provides a wide array of features for dealing with colors. This includes conversion between colorspaces, desaturation, and parsing colors development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета red-colors
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(red-colors) = 0.3.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(kramdown) >= 0

%description   -n gem-red-colors-devel
Red Colors provides a wide array of features for dealing with colors. This
includes conversion between colorspaces, desaturation, and parsing colors
development package.

%description   -n gem-red-colors-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета red-colors.


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

%files         -n gem-red-colors-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-red-colors-devel
%doc README.md


%changelog
* Mon Jun 28 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
