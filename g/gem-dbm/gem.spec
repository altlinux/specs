%define        gemname dbm

Name:          gem-dbm
Version:       1.1.0
Release:       alt1
Summary:       Provides a wrapper for the UNIX-style Database Manager Library
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/dbm
Vcs:           https://github.com/ruby/dbm.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(test-unit) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(dbm) = 1.1.0


%description
Provides a wrapper for the UNIX-style Database Manager Library


%package       -n gem-dbm-devel
Version:       1.1.0
Release:       alt1
Summary:       Provides a wrapper for the UNIX-style Database Manager Library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dbm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dbm) = 1.1.0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-dbm-devel
Provides a wrapper for the UNIX-style Database Manager Library development
package.

%description   -n gem-dbm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dbm.


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
%ruby_gemextdir

%files         -n gem-dbm-devel


%changelog
* Fri Jul 01 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
