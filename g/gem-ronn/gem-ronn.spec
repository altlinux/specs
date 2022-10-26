%define        gemname ronn

Name:          gem-ronn
Version:       0.7.3.1
Release:       alt1
Summary:       Ronn builds manuals from Markdown to roff format
License:       MIT
Group:         Development/Documentation
Url:           https://github.com/rtomayko/ronn/
Vcs:           https://github.com/rtomayko/ronn.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(hpricot) >= 0.8.2
BuildRequires: gem(rdiscount) >= 1.5.8
BuildRequires: gem(mustache) >= 0.7.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version ronn:0.7.3.1
Requires:      gem(hpricot) >= 0.8.2
Requires:      gem(rdiscount) >= 1.5.8
Requires:      gem(mustache) >= 0.7.0
Obsoletes:     ruby-ronn
Provides:      ruby-ronn
Provides:      gem(ronn) = 0.7.3.1


%description
Ronn builds manuals. It converts simple, human readable textfiles to roff for
terminal display, and also to HTML for the web. The source format includes all
of Markdown but has a more rigid structure and syntax extensions for features
commonly found in manpages (definition lists, link notation, etc.). The
ronn-format(7) manual page defines the format in detail.


%package       -n ronn
Version:       0.7.3.1
Release:       alt1
Summary:       Ronn builds manuals from Markdown to roff format executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ronn
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ronn) = 0.7.3.1

%description   -n ronn
Ronn builds manuals from Markdown to roff format executable(s).

Ronn builds manuals. It converts simple, human readable textfiles to roff for
terminal display, and also to HTML for the web. The source format includes all
of Markdown but has a more rigid structure and syntax extensions for features
commonly found in manpages (definition lists, link notation, etc.). The
ronn-format(7) manual page defines the format in detail.

%description   -n ronn -l ru_RU.UTF-8
Исполнямка для самоцвета ronn.


%package       -n gem-ronn-doc
Version:       0.7.3.1
Release:       alt1
Summary:       Ronn builds manuals from Markdown to roff format documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ronn
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ronn) = 0.7.3.1

%description   -n gem-ronn-doc
Ronn builds manuals from Markdown to roff format documentation files.

Ronn builds manuals. It converts simple, human readable textfiles to roff for
terminal display, and also to HTML for the web. The source format includes all
of Markdown but has a more rigid structure and syntax extensions for features
commonly found in manpages (definition lists, link notation, etc.). The
ronn-format(7) manual page defines the format in detail.

%description   -n gem-ronn-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ronn.


%package       -n gem-ronn-devel
Version:       0.7.3.1
Release:       alt1
Summary:       Ronn builds manuals from Markdown to roff format development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ronn
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ronn) = 0.7.3.1

%description   -n gem-ronn-devel
Ronn builds manuals from Markdown to roff format development package.

Ronn builds manuals. It converts simple, human readable textfiles to roff for
terminal display, and also to HTML for the web. The source format includes all
of Markdown but has a more rigid structure and syntax extensions for features
commonly found in manpages (definition lists, link notation, etc.). The
ronn-format(7) manual page defines the format in detail.

%description   -n gem-ronn-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ronn.


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

%files         -n ronn
%doc README.md
%_bindir/ronn

%files         -n gem-ronn-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ronn-devel
%doc README.md


%changelog
* Thu Oct 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.7.3.1-alt1
- ^ 0.7.3 -> 0.7.3[1]

* Sat Nov 13 2021 Michael Shigorin <mike@altlinux.org> 0.7.3-alt4.2
- added bootstrap knob to circumvent self-BR: gem-ronn

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt4.1
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt4
- fixed (!) spec according to changelog rules

* Thu Jul 25 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt3
- fixed (!) spec
- added (+) ronn gem build dependency

* Tue Apr 09 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1
- Initial build for Sisyphus
