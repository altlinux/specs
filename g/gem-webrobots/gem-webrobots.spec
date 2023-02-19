%define        gemname webrobots

Name:          gem-webrobots
Version:       0.1.2.5
Release:       alt0.1
Summary:       A Ruby library to help write robots.txt compliant web robots
License:       2-clause BSDL
Group:         Development/Ruby
Url:           https://github.com/knu/webrobots
Vcs:           https://github.com/knu/webrobots.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0.9.2.2
BuildRequires: gem(racc) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(shoulda) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(vcr) >= 0
BuildRequires: gem(rdoc) > 2.4.2
BuildRequires: gem(bundler) >= 1.2
BuildRequires: gem(nokogiri) >= 1.4.7
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(coveralls) >= 0
BuildConflicts: gem(nokogiri) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Provides:      gem(webrobots) = 0.1.2.5

%ruby_use_gem_version webrobots:0.1.2.5

%description
This is a library to help write robots.txt compliant web robots.


%package       -n gem-webrobots-doc
Version:       0.1.2.5
Release:       alt0.1
Summary:       A Ruby library to help write robots.txt compliant web robots documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета webrobots
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(webrobots) = 0.1.2.5

%description   -n gem-webrobots-doc
A Ruby library to help write robots.txt compliant web robots documentation
files.

This is a library to help write robots.txt compliant web robots.

%description   -n gem-webrobots-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета webrobots.


%package       -n gem-webrobots-devel
Version:       0.1.2.5
Release:       alt0.1
Summary:       A Ruby library to help write robots.txt compliant web robots development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета webrobots
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(webrobots) = 0.1.2.5
Requires:      gem(rake) >= 0.9.2.2
Requires:      gem(racc) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(shoulda) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(vcr) >= 0
Requires:      gem(rdoc) > 2.4.2
Requires:      gem(bundler) >= 1.2
Requires:      gem(nokogiri) >= 1.4.7
Requires:      gem(simplecov) >= 0
Requires:      gem(coveralls) >= 0
Conflicts:     gem(nokogiri) >= 2

%description   -n gem-webrobots-devel
A Ruby library to help write robots.txt compliant web robots development
package.

This is a library to help write robots.txt compliant web robots.

%description   -n gem-webrobots-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета webrobots.


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

%files         -n gem-webrobots-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-webrobots-devel
%doc README.rdoc


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 0.1.2.5-alt0.1
- ^ 0.1.2[1] -> 0.1.2p5

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.2.1-alt1
- ^ 0.1.2 -> 0.1.2[1]

* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
