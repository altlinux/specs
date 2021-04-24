# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname did_you_mean

Name:          gem-did-you-mean
Version:       1.5.0
Release:       alt1
Summary:       "Did you mean?" experience in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/yuki24/did_you_mean
Vcs:           https://github.com/yuki24/did_you_mean.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(did_you_mean) = 1.5.0

%description
The gem that has been saving people from typos since 2014.


%package       -n gem-did-you-mean-doc
Version:       1.5.0
Release:       alt1
Summary:       "Did you mean?" experience in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета did_you_mean
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(did_you_mean) = 1.5.0

%description   -n gem-did-you-mean-doc
"Did you mean?" experience in Ruby documentation files.

The gem that has been saving people from typos since 2014.

%description   -n gem-did-you-mean-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета did_you_mean.


%package       -n gem-did-you-mean-devel
Version:       1.5.0
Release:       alt1
Summary:       "Did you mean?" experience in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета did_you_mean
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(did_you_mean) = 1.5.0
Requires:      gem(rake) >= 0

%description   -n gem-did-you-mean-devel
"Did you mean?" experience in Ruby development package.

The gem that has been saving people from typos since 2014.

%description   -n gem-did-you-mean-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета did_you_mean.


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

%files         -n gem-did-you-mean-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-did-you-mean-devel
%doc README.md


%changelog
* Sat Apr 24 2021 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- ^ 1.3.0 -> 1.5.0

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt2.1
- ! spec according to changelog rules

* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt2
- ! Use Ruby Policy 2.0

* Thu Jan 17 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus
