%define        gemname tomlrb

Name:          gem-tomlrb
Version:       2.0.1
Release:       alt1
Summary:       A Racc based TOML parser
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fbernier/tomlrb
Vcs:           https://github.com/fbernier/tomlrb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-tomlrb < %EVR
Provides:      ruby-tomlrb = %EVR
Provides:      gem(tomlrb) = 2.0.1


%description
A Racc based TOML Ruby parser supporting the 1.0.0 version of the spec.


%package       -n gem-tomlrb-doc
Version:       2.0.1
Release:       alt1
Summary:       A Racc based TOML parser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tomlrb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tomlrb) = 2.0.1

%description   -n gem-tomlrb-doc
A Racc based TOML parser documentation files.

A Racc based TOML Ruby parser supporting the 1.0.0 version of the spec.

%description   -n gem-tomlrb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tomlrb.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-tomlrb-doc
%ruby_gemdocdir


%changelog
* Tue Jun 29 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- ^ 1.2.6 -> 2.0.1

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.6-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.6-alt1
- Initial build for Sisyphus
