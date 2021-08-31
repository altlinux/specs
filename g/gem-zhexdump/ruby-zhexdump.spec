%define        gemname zhexdump

Name:          gem-zhexdump
Version:       0.0.2
Release:       alt2
Summary:       A highly flexible hexdump implementation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/zed-0xff/zhexdump
Vcs:           https://github.com/zed-0xff/zhexdump.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-zhexdump < %EVR
Provides:      ruby-zhexdump = %EVR
Provides:      gem(zhexdump) = 0.0.2


%description
A very flexible hexdump implementation.


%package       -n gem-zhexdump-doc
Version:       0.0.2
Release:       alt2
Summary:       A highly flexible hexdump implementation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета zhexdump
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(zhexdump) = 0.0.2

%description   -n gem-zhexdump-doc
A highly flexible hexdump implementation documentation files.

%description   -n gem-zhexdump-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета zhexdump.


%package       -n gem-zhexdump-devel
Version:       0.0.2
Release:       alt2
Summary:       A highly flexible hexdump implementation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета zhexdump
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(zhexdump) = 0.0.2
Requires:      gem(rspec) >= 0 gem(rspec) < 4

%description   -n gem-zhexdump-devel
A highly flexible hexdump implementation development package.

%description   -n gem-zhexdump-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета zhexdump.


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

%files         -n gem-zhexdump-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-zhexdump-devel
%doc README.md


%changelog
* Tue Jun 29 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.2-alt2
- ! spec

* Mon Aug 27 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.2-alt1.1
- Rebuild for new Ruby autorequirements.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus
