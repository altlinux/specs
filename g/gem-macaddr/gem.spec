%define        gemname macaddr

Name:          gem-macaddr
Version:       1.7.2
Release:       alt1
Summary:       macaddr
License:       Ruby
Group:         Development/Ruby
Url:           https://github.com/ahoward/macaddr
Vcs:           https://github.com/ahoward/macaddr.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(systemu) >= 2.6.5 gem(systemu) < 2.7

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(systemu) >= 2.6.5 gem(systemu) < 2.7
Provides:      gem(macaddr) = 1.7.2


%description
cross platform mac address determination for ruby


%package       -n gem-macaddr-doc
Version:       1.7.2
Release:       alt1
Summary:       macaddr documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета macaddr
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(macaddr) = 1.7.2

%description   -n gem-macaddr-doc
macaddr documentation files.

cross platform mac address determination for ruby

%description   -n gem-macaddr-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета macaddr.


%package       -n gem-macaddr-devel
Version:       1.7.2
Release:       alt1
Summary:       macaddr development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета macaddr
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(macaddr) = 1.7.2

%description   -n gem-macaddr-devel
macaddr development package.

cross platform mac address determination for ruby

%description   -n gem-macaddr-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета macaddr.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-macaddr-doc
%doc README
%ruby_gemdocdir

%files         -n gem-macaddr-devel
%doc README


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 1.7.2-alt1
- + packaged gem with Ruby Policy 2.0
