%define        _unpackaged_files_terminate_build 1
%define        gemname nanotest

Name:          gem-nanotest
Version:       0.9.4.1
Release:       alt1
Summary:       When all you need is #assert
License:       Unlicense
Group:         Development/Ruby
Url:           http://github.com/mynyml/nanotest
Vcs:           https://github.com/mynyml/nanotest.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(nanotest) = 0.9.4.1


%description
Extremely mynymal test framework. Perfect for DIY lovers. Nanotest provides the
bare mynymum needed; for everything else, there's ruby.


%package       -n gem-nanotest-doc
Version:       0.9.4.1
Release:       alt1
Summary:       When all you need is #assert documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета nanotest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(nanotest) = 0.9.4.1

%description   -n gem-nanotest-doc
When all you need is #assert documentation files.

Extremely mynymal test framework. Perfect for DIY lovers. Nanotest provides the
bare mynymum needed; for everything else, there's ruby.

%description   -n gem-nanotest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета nanotest.


%package       -n gem-nanotest-devel
Version:       0.9.4.1
Release:       alt1
Summary:       When all you need is #assert development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета nanotest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(nanotest) = 0.9.4.1
Requires:      gem(minitest) >= 0

%description   -n gem-nanotest-devel
When all you need is #assert development package.

Extremely mynymal test framework. Perfect for DIY lovers. Nanotest provides the
bare mynymum needed; for everything else, there's ruby.

%description   -n gem-nanotest-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета nanotest.


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

%files         -n gem-nanotest-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-nanotest-devel
%doc README.md


%changelog
* Fri Apr 14 2023 Pavel Skrylev <majioa@altlinux.org> 0.9.4.1-alt1
- + packaged gem with Ruby Policy 2.0
