%define        gemname strptime

Name:          gem-strptime
Version:       0.2.5
Release:       alt1
Summary:       A fast strpitme engine
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/nurse/strptime/
Vcs:           https://github.com/nurse/strptime.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rake-compiler-dock) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(yard) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-strptime < %EVR
Provides:      ruby-strptime = %EVR
Provides:      gem(strptime) = 0.2.5


%description
Welcome to your new gem! In this directory, you'll find the files you need to
be able to package up your Ruby library into a gem. Put your Ruby code in the
file lib/strptime. To experiment with that code, run bin/console for an
interactive prompt.


%package       -n gem-strptime-doc
Version:       0.2.5
Release:       alt1
Summary:       A fast strpitme engine documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета strptime
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(strptime) = 0.2.5

%description   -n gem-strptime-doc
A fast strpitme engine documentation files.

Welcome to your new gem! In this directory, you'll find the files you need to
be able to package up your Ruby library into a gem. Put your Ruby code in the
file lib/strptime. To experiment with that code, run bin/console for an
interactive prompt.

%description   -n gem-strptime-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета strptime.


%package       -n gem-strptime-devel
Version:       0.2.5
Release:       alt1
Summary:       A fast strpitme engine development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета strptime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(strptime) = 0.2.5
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rake-compiler-dock) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(yard) >= 0

%description   -n gem-strptime-devel
A fast strpitme engine development package.

Welcome to your new gem! In this directory, you'll find the files you need to
be able to package up your Ruby library into a gem. Put your Ruby code in the
file lib/strptime. To experiment with that code, run bin/console for an
interactive prompt.

%description   -n gem-strptime-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета strptime.


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
%ruby_gemextdir

%files         -n gem-strptime-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-strptime-devel
%doc README.md
%ruby_includedir/*


%changelog
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.5-alt1
- ^ 0.2.3 -> 0.2.5

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt4
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt3
- > Ruby Policy 2.0

* Fri Feb 22 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.3-alt2
- Fix license

* Sun Sep 30 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus
