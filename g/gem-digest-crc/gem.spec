%define        gemname digest-crc

Name:          gem-digest-crc
Version:       0.6.4
Release:       alt1
Summary:       A Cyclic Redundancy Check (CRC) library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/postmodern/digest-crc#readme
Vcs:           https://github.com/postmodern/digest-crc.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
Patch:         gemspec.yml.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 12.0.0 gem(rake) < 14
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency github-markup >= 4.0.0,github-markup < 5
Requires:      gem(rake) >= 12.0.0 gem(rake) < 14
Provides:      gem(digest-crc) = 0.6.4

%description
Adds support for calculating Cyclic Redundancy Check (CRC) to the Digest module.


%package       -n gem-digest-crc-doc
Version:       0.6.4
Release:       alt1
Summary:       A Cyclic Redundancy Check (CRC) library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета digest-crc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(digest-crc) = 0.6.4

%description   -n gem-digest-crc-doc
A Cyclic Redundancy Check (CRC) library for Ruby documentation files.

Adds support for calculating Cyclic Redundancy Check (CRC) to the Digest module.

%description   -n gem-digest-crc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета digest-crc.


%package       -n gem-digest-crc-devel
Version:       0.6.4
Release:       alt1
Summary:       A Cyclic Redundancy Check (CRC) library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета digest-crc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(digest-crc) = 0.6.4
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3

%description   -n gem-digest-crc-devel
A Cyclic Redundancy Check (CRC) library for Ruby development package.

Adds support for calculating Cyclic Redundancy Check (CRC) to the Digest module.

%description   -n gem-digest-crc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета digest-crc.


%prep
%setup
%autopatch -p1

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
%ruby_gemextdir

%files         -n gem-digest-crc-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-digest-crc-devel
%doc README.md
%ruby_includedir/*


%changelog
* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.4-alt1
- ^ 0.6.3 -> 0.6.4

* Thu Jun 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.6.3-alt1
- + packaged gem with Ruby Policy 2.0
