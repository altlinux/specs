%define        gemname hoe-seattlerb

Name:          gem-hoe-seattlerb
Version:       1.3.5
Release:       alt1
Summary:       Hoe plugins providing tasks used by seattle.rb including minitest, perforce, and email providing full front-to-back release/announce automation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/hoe-seattlerb
Vcs:           https://github.com/seattlerb/hoe-seattlerb.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.14 gem(minitest) < 6
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.22 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Provides:      gem(hoe-seattlerb) = 1.3.5


%description
Hoe plugins providing tasks used by seattle.rb including minitest, perforce, and
email providing full front-to-back release/announce automation.


%package       -n gem-hoe-seattlerb-doc
Version:       1.3.5
Release:       alt1
Summary:       Hoe plugins providing tasks used by seattle.rb including minitest, perforce, and email providing full front-to-back release/announce automation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-seattlerb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-seattlerb) = 1.3.5

%description   -n gem-hoe-seattlerb-doc
Hoe plugins providing tasks used by seattle.rb including minitest, perforce, and
email providing full front-to-back release/announce automation documentation
files.

Hoe plugins providing tasks used by seattle.rb including minitest, perforce, and
email providing full front-to-back release/announce automation.

%description   -n gem-hoe-seattlerb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-seattlerb.


%package       -n gem-hoe-seattlerb-devel
Version:       1.3.5
Release:       alt1
Summary:       Hoe plugins providing tasks used by seattle.rb including minitest, perforce, and email providing full front-to-back release/announce automation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-seattlerb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-seattlerb) = 1.3.5
Requires:      gem(minitest) >= 5.14 gem(minitest) < 6
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.22 gem(hoe) < 4

%description   -n gem-hoe-seattlerb-devel
Hoe plugins providing tasks used by seattle.rb including minitest, perforce, and
email providing full front-to-back release/announce automation development
package.

Hoe plugins providing tasks used by seattle.rb including minitest, perforce, and
email providing full front-to-back release/announce automation.

%description   -n gem-hoe-seattlerb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-seattlerb.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.txt
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-hoe-seattlerb-doc
%doc README.txt
%ruby_gemdocdir

%files         -n gem-hoe-seattlerb-devel
%doc README.txt


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.5-alt1
- + packaged gem with Ruby Policy 2.0
