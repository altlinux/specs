%define        gemname signet

Name:          gem-signet
Version:       0.17.0
Release:       alt1
Summary:       Signet is an OAuth 1.0 / OAuth 2.0 implementation
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/google/signet/
Vcs:           https://github.com/googleapis/signet.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(google-style) >= 1.26.0 gem(google-style) < 1.27
BuildRequires: gem(kramdown) >= 1.5 gem(kramdown) < 3
BuildRequires: gem(launchy) >= 2.4 gem(launchy) < 3
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(redcarpet) >= 3.0 gem(redcarpet) < 4
BuildRequires: gem(rspec) >= 3.1 gem(rspec) < 4
BuildRequires: gem(yard) >= 0.9.12 gem(yard) < 1
BuildRequires: gem(bundler) >= 1.15
BuildRequires: gem(gems) >= 1.2 gem(gems) < 2
BuildRequires: gem(hurley) >= 0
BuildRequires: gem(addressable) >= 2.8 gem(addressable) < 3
BuildRequires: gem(faraday) >= 0.17.5 gem(faraday) < 3.a
BuildRequires: gem(jwt) >= 1.5 gem(jwt) < 3
BuildRequires: gem(multi_json) >= 1.10 gem(multi_json) < 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
Requires:      gem(addressable) >= 2.8 gem(addressable) < 3
Requires:      gem(faraday) >= 0.17.5 gem(faraday) < 3.a
Requires:      gem(jwt) >= 1.5 gem(jwt) < 3
Requires:      gem(multi_json) >= 1.10 gem(multi_json) < 2
Obsoletes:     ruby-signet < %EVR
Provides:      ruby-signet = %EVR
Provides:      gem(signet) = 0.17.0


%description
Signet is an OAuth 1.0 / OAuth 2.0 implementation.


%package       -n gem-signet-doc
Version:       0.17.0
Release:       alt1
Summary:       Signet is an OAuth 1.0 / OAuth 2.0 implementation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета signet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(signet) = 0.17.0

%description   -n gem-signet-doc
Signet is an OAuth 1.0 / OAuth 2.0 implementation documentation files.

%description   -n gem-signet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета signet.


%package       -n gem-signet-devel
Version:       0.17.0
Release:       alt1
Summary:       Signet is an OAuth 1.0 / OAuth 2.0 implementation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета signet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(signet) = 0.17.0
Requires:      gem(google-style) >= 1.26.0 gem(google-style) < 1.27
Requires:      gem(kramdown) >= 1.5 gem(kramdown) < 3
Requires:      gem(launchy) >= 2.4 gem(launchy) < 3
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(redcarpet) >= 3.0 gem(redcarpet) < 4
Requires:      gem(rspec) >= 3.1 gem(rspec) < 4
Requires:      gem(yard) >= 0.9.12 gem(yard) < 1
Requires:      gem(bundler) >= 1.15
Requires:      gem(gems) >= 1.2 gem(gems) < 2
Requires:      gem(hurley) >= 0

%description   -n gem-signet-devel
Signet is an OAuth 1.0 / OAuth 2.0 implementation development package.

%description   -n gem-signet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета signet.


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

%files         -n gem-signet-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-signet-devel
%doc README.md


%changelog
* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.17.0-alt1
- ^ 0.16.1 -> 0.17.0

* Wed Mar 30 2022 Pavel Skrylev <majioa@altlinux.org> 0.16.1-alt1
- ^ 0.15.0 -> 0.16.1

* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.15.0-alt1
- ^ 0.11.0 -> 0.15.0

* Fri Oct 12 2018 Andrey Cherepanov <cas@altlinux.org> 0.11.0-alt1
- New version.

* Tue Sep 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.10.0-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus
