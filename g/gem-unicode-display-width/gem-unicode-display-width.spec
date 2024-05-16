%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname unicode-display_width

Name:          gem-unicode-display-width
Version:       2.5.0
Release:       alt1
Summary:       Monospace Unicode character width in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/janlelis/unicode-display_width
Vcs:           https://github.com/janlelis/unicode-display_width.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 3.4
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(unicode-emoji) >= 0
BuildRequires: gem(irb) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names unicode-display_width,unicode-display-width
Obsoletes:     ruby-unicode-display-width < %EVR
Provides:      ruby-unicode-display-width = %EVR
Provides:      gem(unicode-display_width) = 2.5.0


%description
Determines the monospace display width of a string in Ruby. Implementation based
on EastAsianWidth.txt and other data, 100% in Ruby. It does not rely on the OS
vendor (like wcwidth()) to provide an up-to-date method for measuring string
width.


%if_enabled    doc
%package       -n gem-unicode-display-width-doc
Version:       2.5.0
Release:       alt1
Summary:       Monospace Unicode character width in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета unicode-display_width
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(unicode-display_width) = 2.5.0

%description   -n gem-unicode-display-width-doc
Monospace Unicode character width in Ruby documentation files.
%description   -n gem-unicode-display-width-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета unicode-display_width.
%endif


%if_enabled    devel
%package       -n gem-unicode-display-width-devel
Version:       2.5.0
Release:       alt1
Summary:       Monospace Unicode character width in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета unicode-display_width
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(unicode-display_width) = 2.5.0
Requires:      gem(rspec) >= 3.4
Requires:      gem(rake) >= 13.0
Requires:      gem(unicode-emoji) >= 0
Requires:      gem(irb) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rake) >= 14

%description   -n gem-unicode-display-width-devel
Monospace Unicode character width in Ruby development package.
%description   -n gem-unicode-display-width-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета unicode-display_width.
%endif


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

%if_enabled    doc
%files         -n gem-unicode-display-width-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-unicode-display-width-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- ^ 2.0.0 -> 2.5.0

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- ^ 1.6.0 -> 2.0.0

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- ^ 1.4.1 -> 1.6.0

* Thu Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- ^ 1.4.0 -> 1.4.1
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus
