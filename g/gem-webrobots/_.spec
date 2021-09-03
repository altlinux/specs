%define        gemname webrobots

Name:          gem-webrobots
Version:       0.1.2.1
Release:       alt1
Summary:       A Ruby library to help write robots.txt compliant web robots
License:       2-clause BSDL
Group:         Development/Ruby
Url:           https://github.com/knu/webrobots
Vcs:           https://github.com/knu/webrobots.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0.9.2.2 gem(rake) < 14
BuildRequires: gem(racc) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(shoulda) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(vcr) >= 0
BuildRequires: gem(rdoc) > 2.4.2 gem(rdoc) < 7
BuildRequires: gem(bundler) >= 1.2 gem(bundler) < 3
BuildRequires: gem(nokogiri) >= 1.4 gem(nokogiri) < 2
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(coveralls) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_version webrobots:0.1.2.1
Provides:      gem(webrobots) = 0.1.2.1


%description
This is a library to help write robots.txt compliant web robots.


%package       -n gem-webrobots-doc
Version:       0.1.2.1
Release:       alt1
Summary:       A Ruby library to help write robots.txt compliant web robots documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета webrobots
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(webrobots) = 0.1.2.1

%description   -n gem-webrobots-doc
A Ruby library to help write robots.txt compliant web robots documentation
files.

This is a library to help write robots.txt compliant web robots.

%description   -n gem-webrobots-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета webrobots.


%package       -n gem-webrobots-devel
Version:       0.1.2.1
Release:       alt1
Summary:       A Ruby library to help write robots.txt compliant web robots development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета webrobots
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(webrobots) = 0.1.2.1
Requires:      gem(rake) >= 0.9.2.2 gem(rake) < 14
Requires:      gem(racc) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(shoulda) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(vcr) >= 0
Requires:      gem(rdoc) > 2.4.2 gem(rdoc) < 7
Requires:      gem(bundler) >= 1.2 gem(bundler) < 3
Requires:      gem(nokogiri) >= 1.4 gem(nokogiri) < 2
Requires:      gem(simplecov) >= 0
Requires:      gem(coveralls) >= 0

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
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.2.1-alt1
- ^ 0.1.2 -> 0.1.2.1

* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
