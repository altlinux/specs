%define        gemname fast_xs

Name:          gem-fast-xs
Version:       0.8.0
Release:       alt1
Summary:       fast_xs provides C extensions for escaping text
License:       Unlicense
Group:         Development/Ruby
Url:           http://rubyforge.org/projects/fast-xs
Vcs:           http://rubyforge.org/projects/fast-xs.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rdoc) >= 4.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(fast_xs) = 0.8.0


%description
fast_xs provides C extensions for escaping text.

The original String.


%package       -n gem-fast-xs-doc
Version:       0.8.0
Release:       alt1
Summary:       fast_xs provides C extensions for escaping text documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fast_xs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fast_xs) = 0.8.0

%description   -n gem-fast-xs-doc
fast_xs provides C extensions for escaping text documentation files.

The original String.

%description   -n gem-fast-xs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fast_xs.


%package       -n gem-fast-xs-devel
Version:       0.8.0
Release:       alt1
Summary:       fast_xs provides C extensions for escaping text development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fast_xs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fast_xs) = 0.8.0
Requires:      gem(rdoc) >= 4.0

%description   -n gem-fast-xs-devel
fast_xs provides C extensions for escaping text development package.

The original String.

%description   -n gem-fast-xs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fast_xs.


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

%files         -n gem-fast-xs-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-fast-xs-devel
%doc README.rdoc
%ruby_includedir/*


%changelog
* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- + packaged gem with Ruby Policy 2.0
