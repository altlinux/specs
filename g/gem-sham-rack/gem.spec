%define        gemname sham_rack

Name:          gem-sham-rack
Version:       1.4.1
Release:       alt1
Summary:       Net::HTTP-to-Rack plumbing
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/mdub/sham_rack
Vcs:           https://github.com/mdub/sham_rack.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rack) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rack) >= 0
Provides:      gem(sham_rack) = 1.4.1


%description
ShamRack plumbs Net::HTTP directly into Rack, for quick and easy HTTP testing.


%package       -n gem-sham-rack-doc
Version:       1.4.1
Release:       alt1
Summary:       Net::HTTP-to-Rack plumbing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sham_rack
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sham_rack) = 1.4.1

%description   -n gem-sham-rack-doc
Net::HTTP-to-Rack plumbing documentation files.

ShamRack plumbs Net::HTTP directly into Rack, for quick and easy HTTP testing.

%description   -n gem-sham-rack-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sham_rack.


%package       -n gem-sham-rack-devel
Version:       1.4.1
Release:       alt1
Summary:       Net::HTTP-to-Rack plumbing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sham_rack
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sham_rack) = 1.4.1

%description   -n gem-sham-rack-devel
Net::HTTP-to-Rack plumbing development package.

ShamRack plumbs Net::HTTP directly into Rack, for quick and easy HTTP testing.

%description   -n gem-sham-rack-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sham_rack.


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

%files         -n gem-sham-rack-doc
%ruby_gemdocdir

%files         -n gem-sham-rack-devel


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- + packaged gem with Ruby Policy 2.0
