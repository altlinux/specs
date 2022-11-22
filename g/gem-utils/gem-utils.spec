%define        gemname utils

Name:          gem-utils
Version:       0.32.0
Release:       alt1
Summary:       Some useful command line utilities
License:       GPL-2.0
Group:         Development/Ruby
Url:           http://github.com/flori/utils
Vcs:           https://github.com/flori/utils.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(gem_hadar) >= 1.12.0 gem(gem_hadar) < 2
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(tins) >= 1.14 gem(tins) < 2
BuildRequires: gem(term-ansicolor) >= 1.3 gem(term-ansicolor) < 2
BuildRequires: gem(pstree) >= 0.3 gem(pstree) < 1
BuildRequires: gem(infobar) >= 0
BuildRequires: gem(mize) >= 0
BuildRequires: gem(search_ui) >= 0
BuildRequires: gem(all_images) >= 0.0.2
BuildRequires: gem(gem_hadar) >= 1.12.0 gem(gem_hadar) < 2
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(tins) >= 1.14 gem(tins) < 2
BuildRequires: gem(term-ansicolor) >= 1.3 gem(term-ansicolor) < 2
BuildRequires: gem(pstree) >= 0.3 gem(pstree) < 1
BuildRequires: gem(infobar) >= 0
BuildRequires: gem(mize) >= 0
BuildRequires: gem(search_ui) >= 0
BuildRequires: gem(all_images) >= 0.0.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency gem_hadar >= 1.12.0,gem_hadar < 2
Requires:      gem(tins) >= 1.14 gem(tins) < 2
Requires:      gem(term-ansicolor) >= 1.3 gem(term-ansicolor) < 2
Requires:      gem(pstree) >= 0.3 gem(pstree) < 1
Requires:      gem(infobar) >= 0
Requires:      gem(mize) >= 0
Requires:      gem(search_ui) >= 0
Requires:      gem(all_images) >= 0.0.2
Provides:      gem(utils) = 0.32.0


%description
This ruby gem provides some useful command line utilities.


%package       -n utils
Version:       0.32.0
Release:       alt1
Summary:       Some useful command line utilities executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета utils
Group:         Other
BuildArch:     noarch

Requires:      gem(utils) = 0.32.0

%description   -n utils
Some useful command line utilities executable(s).

This ruby gem provides some useful command line utilities.

%description   -n utils -l ru_RU.UTF-8
Исполнямка для самоцвета utils.


%package       -n gem-utils-doc
Version:       0.32.0
Release:       alt1
Summary:       Some useful command line utilities documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета utils
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(utils) = 0.32.0

%description   -n gem-utils-doc
Some useful command line utilities documentation files.

This ruby gem provides some useful command line utilities.

%description   -n gem-utils-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета utils.


%package       -n gem-utils-devel
Version:       0.32.0
Release:       alt1
Summary:       Some useful command line utilities development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета utils
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(utils) = 0.32.0
Requires:      gem(gem_hadar) >= 1.12.0 gem(gem_hadar) < 2
Requires:      gem(byebug) >= 0

%description   -n gem-utils-devel
Some useful command line utilities development package.

This ruby gem provides some useful command line utilities.

%description   -n gem-utils-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета utils.


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

%files         -n utils
%doc README.md
%_bindir/ascii7
%_bindir/blameline
%_bindir/check-yaml
%_bindir/classify
%_bindir/create_cstags
%_bindir/create_tags
%_bindir/discover
%_bindir/edit
%_bindir/edit_wait
%_bindir/enum
%_bindir/fix-brew
%_bindir/git-empty
%_bindir/git-versions
%_bindir/irb_connect
%_bindir/json_check
%_bindir/long_lines
%_bindir/myex
%_bindir/number_files
%_bindir/on_change
%_bindir/path
%_bindir/probe
%_bindir/rd2md
%_bindir/search
%_bindir/sedit
%_bindir/serve
%_bindir/ssh-tunnel
%_bindir/ssl_cert_info
%_bindir/strip_spaces
%_bindir/untest
%_bindir/utils-utilsrc
%_bindir/vcf2alias

%files         -n gem-utils-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-utils-devel
%doc README.md


%changelog
* Tue Nov 22 2022 Pavel Skrylev <majioa@altlinux.org> 0.32.0-alt1
- ^ 0.30.0 -> 0.32.0

* Wed Jul 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.30.0-alt1
- + packaged gem with Ruby Policy 2.0
