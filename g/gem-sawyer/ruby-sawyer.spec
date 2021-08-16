%define        gemname sawyer

Name:          gem-sawyer
Version:       0.8.2
Release:       alt1
Summary:       Secret User Agent of HTTP
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/sawyer
Vcs:           https://github.com/lostisland/sawyer.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(faraday) > 0.8 gem(faraday) < 2.0
BuildRequires: gem(addressable) >= 2.3.5

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(faraday) > 0.8 gem(faraday) < 2.0
Requires:      gem(addressable) >= 2.3.5
Obsoletes:     ruby-sawyer < %EVR
Provides:      ruby-sawyer = %EVR
Provides:      gem(sawyer) = 0.8.2


%description
Sawyer is an experimental hypermedia agent for Ruby built on top of Faraday.


%package       -n gem-sawyer-doc
Version:       0.8.2
Release:       alt1
Summary:       Secret User Agent of HTTP documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sawyer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sawyer) = 0.8.2

%description   -n gem-sawyer-doc
Secret User Agent of HTTP documentation files.

Sawyer is an experimental hypermedia agent for Ruby built on top of Faraday.

%description   -n gem-sawyer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sawyer.


%package       -n gem-sawyer-devel
Version:       0.8.2
Release:       alt1
Summary:       Secret User Agent of HTTP development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sawyer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sawyer) = 0.8.2

%description   -n gem-sawyer-devel
Secret User Agent of HTTP development package.

Sawyer is an experimental hypermedia agent for Ruby built on top of Faraday.

%description   -n gem-sawyer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sawyer.


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

%files         -n gem-sawyer-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sawyer-devel
%doc README.md


%changelog
* Mon Jun 28 2021 Pavel Skrylev <majioa@altlinux.org> 0.8.2-alt1
- ^ 0.8.1 -> 0.8.2

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.1-alt2
- > Ruby Policy 2.0
- ^ addressable dep -> ~2.6

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon May 15 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.8.1-alt1
- Initial build in Sisyphus
